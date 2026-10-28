#!/usr/bin/env python3
"""Focused regressions for second-pass integration failures. Real offline file URLs."""
import argparse
import json
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
URL=(ROOT/'index.html').as_uri()


def run(name):
    with sync_playwright() as pw:
        executable=shutil.which('chromium')
        browser=getattr(pw,name).launch(headless=True,**({'executable_path':executable} if name=='chromium' and executable else {}))
        context=browser.new_context(offline=True,accept_downloads=True,viewport={'width':1440,'height':1000})
        errors=[];network=[];failed=[]
        context.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
        context.on('request',lambda req:network.append(req.url) if req.url.startswith(('http:','https:')) else None)
        context.on('requestfailed',lambda req:failed.append((req.url,req.failure)))
        page=context.new_page();accept_dialogs=True
        def dialog_handler(dialog):
            dialog.accept() if accept_dialogs else dialog.dismiss()
        page.on('dialog',dialog_handler)

        def visit(app,route):
            page.goto(URL+'#read/'+app+'/'+route)
            page.wait_for_selector('iframe[data-app="'+app+'"]')
            frame=page.frame(url=lambda u:'/manuals/'+app+'/' in u)
            if not frame:
                page.wait_for_timeout(100);frame=page.frame(url=lambda u:'/manuals/'+app+'/' in u)
            frame.wait_for_selector('#main h1')
            frame.wait_for_function('window.ManualAdapter!==undefined')
            return frame

        # Saved individual choices must survive global defaults and bundle round trips.
        ps=visit('photoshop','progress')
        page.get_by_role('link',name='Progress',exact=True).click()
        page.locator('[data-library-preference="large"]').check()
        page.get_by_role('button',name='Apply to all three',exact=True).click()
        ps.wait_for_function('window.ManualAdapter.get().largeText')
        page.locator('#switcher').select_option('photoshop')
        ps.wait_for_selector('[data-action="large"]');ps.locator('[data-action="large"]').click()
        ps.wait_for_function('!window.ManualAdapter.get().largeText')
        page.get_by_role('link',name='Progress',exact=True).click()
        with page.expect_download() as dl:page.get_by_role('button',name='Export all progress',exact=True).click()
        original=json.loads(Path(dl.value.path()).read_text())
        assert original['preferences']['large'] is True
        assert original['manuals']['photoshop']['state']['largeText'] is False
        ps=visit('photoshop','progress')
        assert ps.evaluate('window.ManualAdapter.get().largeText') is False
        print('PASS',name,'individual reading preferences survive reload',flush=True)

        # A fresh backup must query the reader even if its automatic notification was delayed.
        ps.evaluate("()=>{window.manualChanged=()=>{};const state=structuredClone(window.ManualAdapter.get());state.completed=['s01l01'];window.ManualAdapter.set(state)}")
        page.get_by_role('link',name='Progress',exact=True).click()
        with page.expect_download() as dl:page.get_by_role('button',name='Export all progress',exact=True).click()
        fresh=json.loads(Path(dl.value.path()).read_text())
        assert fresh['manuals']['photoshop']['state']['completed']==['s01l01']
        print('PASS',name,'export requests fresh reader state',flush=True)

        # Failure after another reader has changed must restore every original state and route.
        ae=page.frame(url=lambda u:'/manuals/after-effects/' in u)
        ae.evaluate("()=>{const old=window.ManualAdapter.set;let first=true;window.ManualAdapter.set=value=>{if(first){first=false;throw Error('injected restore failure')}old(value)}}")
        candidate=json.loads(json.dumps(fresh));candidate['manuals']['photoshop']['state']['completed']=[]
        page.locator('#import-library').set_input_files({'name':'candidate.json','mimeType':'application/json','buffer':json.dumps(candidate).encode()})
        page.wait_for_function("document.getElementById('backup-status').textContent.includes('injected restore failure')")
        assert ps.evaluate('window.ManualAdapter.get().completed')==['s01l01']
        assert not page.get_by_role('button',name='Export all progress',exact=True).is_disabled()
        print('PASS',name,'failed replacement rolls back and unlocks backup controls',flush=True)

        # Cancellation must preserve state; divergent preferences must not be reapplied after import.
        accept_dialogs=False
        page.locator('#import-library').set_input_files({'name':'cancel.json','mimeType':'application/json','buffer':json.dumps(original).encode()})
        page.wait_for_function("document.getElementById('import-library').value===''&&!document.querySelector('[data-action=\"export-library\"]').disabled")
        assert ps.evaluate('window.ManualAdapter.get().completed')==['s01l01']
        accept_dialogs=True
        page.locator('#import-library').set_input_files({'name':'backup.json','mimeType':'application/json','buffer':json.dumps(original).encode()})
        page.wait_for_function("document.getElementById('backup-status').textContent.includes('validated learning records imported')")
        ps=visit('photoshop','progress');assert ps.evaluate('window.ManualAdapter.get().largeText') is False

        # Query URLs describe the visible query, including an empty query after Back.
        page.evaluate("location.hash='#search/alpha'");page.wait_for_selector('#library-search')
        page.wait_for_function("document.getElementById('library-search').value==='alpha'")
        page.evaluate("location.hash='#search'");page.wait_for_function("document.getElementById('library-search').value===''")
        page.locator('#library-search').fill('ripple');page.get_by_role('link',name='Library',exact=True).click()
        page.wait_for_timeout(250);assert page.url.endswith('#home')
        print('PASS',name,'empty query and delayed URL update remain consistent',flush=True)

        # Native search uses replaceState; the standalone link must follow it too.
        ae=visit('after-effects','home');ae.locator('#globalSearch').fill('Unmult')
        page.wait_for_function("location.hash.includes('search/Unmult')")
        assert page.locator('#reader-controls a').get_attribute('href').endswith('#search/Unmult')
        page.locator('.skip').focus();page.keyboard.press('Enter')
        ae.wait_for_function("document.activeElement.id==='main'")
        print('PASS',name,'native search standalone link and skip-to-content focus',flush=True)

        # Exact version targets and omitted teaching are now represented.
        ps=visit('photoshop','changes/0')
        assert ps.locator('.search-target').count()==1
        assert ps.locator('.search-target').get_attribute('id')=='version-0'
        ps=visit('photoshop','home')
        ps.wait_for_function("[...document.querySelectorAll('img')].every(x=>x.complete&&x.naturalWidth>0)")
        assert ps.locator('img').count()>=8
        print('PASS',name,'version target and every Photoshop overview image decode',flush=True)

        # A root-store write failure must be visible and must not erase newer native progress.
        ps=visit('photoshop','lesson/s01l01')
        page.wait_for_timeout(250)
        page.evaluate("()=>{const old=Storage.prototype.setItem;Storage.prototype.setItem=function(k,v){if(k==='dusky-adobe-library-v1')throw Error('quota fixture');return old.call(this,k,v)}}")
        ps.locator('[data-action="complete"]').click()
        ps.wait_for_function("window.ManualAdapter.get().completed.includes('s01l01')")
        page.wait_for_function("document.getElementById('notice').textContent.includes('could not be saved')")
        ps=visit('photoshop','lesson/s01l01')
        ps.wait_for_function("window.ManualAdapter.get().completed.includes('s01l01')")
        print('PASS',name,'late storage failure warns; newer native progress wins on reload',flush=True)

        # Reproduce a delayed old navigation arriving after Back.
        delayed=browser.new_context(offline=True)
        delayed.add_init_script("""if(parent!==window){let held=false;addEventListener('message',e=>{if(!held&&e.data?.type==='navigate'&&e.data.route==='lesson/s01l02'){held=true;e.stopImmediatePropagation();const data=e.data,source=e.source;setTimeout(()=>dispatchEvent(new MessageEvent('message',{data,source})),400)}},true)}""")
        dp=delayed.new_page();dp.goto(URL+'#read/photoshop/lesson/s01l01');dp.wait_for_selector('iframe');dp.wait_for_timeout(100)
        df=dp.frame(url=lambda u:'/manuals/photoshop/' in u);df.wait_for_selector('#main h1')
        df.locator('a[href="#/lesson/s01l02"]').first.click();dp.wait_for_url('**#read/photoshop/lesson/s01l02');dp.go_back();dp.wait_for_timeout(500)
        assert dp.url.endswith('#read/photoshop/lesson/s01l01')
        assert df.url.endswith('#/lesson/s01l01')
        delayed.close();print('PASS',name,'late navigation cannot undo Back',flush=True)

        # Reader timeout must not replace a newer page, and the failed reader can be retried.
        recovery=browser.new_context(offline=True)
        recovery.add_init_script("""if(parent===window){const original=setTimeout;window.setTimeout=(fn,ms,...args)=>original(fn,ms===15000?400:ms,...args);let held=false;addEventListener('message',e=>{if(!held&&e.data?.type==='ready'&&e.data.app==='photoshop'){held=true;e.stopImmediatePropagation()}},true)}""")
        rp=recovery.new_page();rp.goto(URL+'#read/photoshop/home');rp.wait_for_selector('iframe',state='attached');rp.get_by_role('link',name='Library',exact=True).click();rp.wait_for_timeout(500)
        assert 'Three crafts.' in rp.locator('h1').inner_text()
        rp.locator('#switcher').select_option('photoshop');rp.wait_for_selector('iframe');rp.wait_for_timeout(150)
        rf=rp.frame(url=lambda u:'/manuals/photoshop/' in u);rf.wait_for_selector('#main h1')
        ep=recovery.new_page();ep.goto(URL+'#read/photoshop/home');ep.wait_for_selector('h1:text("Manual could not open")')
        ep.get_by_role('button',name='Retry opening manual',exact=True).click();ep.wait_for_selector('iframe')
        ef=ep.frame(url=lambda u:'/manuals/photoshop/' in u);ef.wait_for_selector('#main h1')
        recovery.close();print('PASS',name,'timeout leaves newer navigation intact and both retry paths work',flush=True)
        assert not errors,errors
        assert not network,network
        assert not failed,failed
        context.close();browser.close()
        print('PASS',name,'second-pass regressions; no JS errors, remote requests or failed assets',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--browser',choices=['chromium','firefox','both'],default='both');args=parser.parse_args()
    for name in (['chromium','firefox'] if args.browser=='both' else [args.browser]):run(name)
