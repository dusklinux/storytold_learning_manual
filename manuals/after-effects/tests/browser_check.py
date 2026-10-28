#!/usr/bin/env python3
"""Real file:// browser regression. Optional: pip install playwright; playwright install firefox.
Run directly, outside unittest discovery: python tests/browser_check.py --browser both
"""
import argparse
import json
import shutil
import time
from pathlib import Path
lazy from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def run(name):
    data=json.loads((ROOT/'manual_data.json').read_text(encoding='utf-8'))
    with sync_playwright() as pw:
        browser=getattr(pw,name).launch(headless=True, **({'executable_path':shutil.which('chromium')} if name=='chromium' and shutil.which('chromium') else {}))
        context=browser.new_context(offline=True, viewport={'width':1440,'height':1000}, accept_downloads=True)
        requests=[];errors=[]
        context.on('request',lambda request: requests.append(request.url) if request.url.startswith(('http:','https:')) else None)
        page=context.new_page();page.on('pageerror',lambda error: errors.append(str(error)))
        page.goto((ROOT/'index.html').as_uri())
        page.wait_for_function("document.title.includes('26.5')")
        last_navigation=0.0
        def visit(route):
            nonlocal last_navigation
            if name=='firefox':
                delay=0.065-(time.monotonic()-last_navigation)
                if delay>0:page.wait_for_timeout(delay*1000)
            last_navigation=time.monotonic()
            page.evaluate('(route)=>{location.hash=route;render(false)}',route)
            assert page.locator('#main').inner_text().strip(), route
        routes=['home','lessons','topics','recipes','effects','shortcuts','troubleshoot','glossary','quiz','lab','audit','settings']
        routes += ['lesson/'+x['id'] for x in data['chapters']]
        routes += ['topic/'+x['id'] for x in data['topics']]
        routes += ['recipe/'+x['id'] for x in data['recipes']]
        routes += [kind+'/'+x['id'] for kind in ('effects','shortcuts') for x in data[kind]]
        routes += ['troubleshoot/'+x['id'] for x in data['troubleshooting']]
        routes += ['glossary/'+x['term'] for x in data['glossary']]
        for route_index,route in enumerate(routes):
            visit(route)
            if route_index and route_index%250==0:print(f'{name}: {route_index}/{len(routes)} routes',flush=True)
            if route.startswith(('effects/','shortcuts/','troubleshoot/','glossary/')):
                assert page.locator('.search-target').count()==1,route
        visit('search/Unmult')
        result=page.locator('a[href^="#effects/fx-"]').filter(has_text='Unmult').first
        result.click();page.wait_for_selector('.search-target')
        assert 'Unmult' in page.locator('.search-target').inner_text()
        page.locator('#listFilter').fill('Curl Noise')
        assert page.locator('.catalog-item').count()==1
        visit('effects');page.locator('#listFilter').fill('Curl Noise')
        assert page.locator('.catalog-item').count()==1
        page.locator('#listFilter').fill('');page.locator('#categoryFilter').select_option('Audio')
        assert 'Compressor' in page.locator('#main').inner_text()
        visit('lesson/logic');page.locator('[data-step="logic:0"]').check()
        assert page.locator('[data-step="logic:0"]').evaluate('(x)=>x===document.activeElement')
        page.reload();page.wait_for_selector('[data-step="logic:0"]:checked')
        page.locator('#oneStepToggle').check()
        assert page.locator('#oneStepToggle').evaluate('(x)=>x===document.activeElement')
        assert page.locator('.step:visible').count()==1
        page.emulate_media(media='print')
        assert page.locator('.step:visible').count()==len(next(x for x in data['chapters'] if x['id']=='logic')['steps'])
        page.emulate_media(media='screen')
        visit('quiz');page.locator('[data-q="0"][value="1"]').check()
        assert page.locator('[data-q="0"][value="1"]').evaluate('(x)=>x===document.activeElement')
        visit('lab');page.locator('#frameFps').select_option('23.976');page.locator('#frameCount').fill('24000')
        assert '1001.000' in page.locator('#frameOut').inner_text()
        page.locator('#frameCount').fill('1.5');assert 'whole' in page.locator('#frameOut').inner_text()
        visit('settings')
        with page.expect_download() as download:page.locator('[data-action="export"]').click()
        exported=json.loads(Path(download.value.path()).read_text())
        assert exported['manualVersion']=='26.5' and exported['steps']['logic:0']
        dialogs=[]
        def dialog_handler(dialog):dialogs.append(dialog.message);dialog.accept()
        page.on('dialog',dialog_handler)
        legacy={'manualVersion':'25.6','edition':1,'steps':{'logic:0':True,'install:0':True,'advanced3d:5':True},'answers':{'0':1,'1':2}}
        page.locator('#importProgress').set_input_files({'name':'legacy.json','mimeType':'application/json','buffer':json.dumps(legacy).encode()})
        page.wait_for_function("Object.keys(state.steps).length===1")
        assert page.evaluate("state.version==='26.5'&&state.steps['logic:0']&&!('1' in state.answers)")
        visit('settings');before=page.evaluate('JSON.stringify(state)')
        page.locator('#importProgress').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':b'{"manualVersion":"26.5","edition":2,"steps":[]}'} )
        page.wait_for_timeout(100)
        assert page.evaluate('JSON.stringify(state)')==before
        visit('lesson/logic');page.locator('.skip').focus();page.keyboard.press('Enter')
        assert page.evaluate("location.hash==='#lesson/logic'&&document.activeElement.id==='main'")
        for route in ('%bad%zz','effects/unknown','topic/unknown'):
            visit(route)
        for width in (375,768):
            page.set_viewport_size({'width':width,'height':900})
            for route in ('home','lesson/modern-operations','effects','shortcuts','settings','audit'):
                visit(route)
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,route)
            visit('settings');page.locator('#largeToggle').check();visit('lesson/flow-alpha')
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            visit('settings');page.locator('#largeToggle').uncheck()
        # Corrupt stored values must not crash or be spread into live state.
        page.evaluate("localStorage.setItem('ae_26_5_windows_manual_progress_v2',JSON.stringify({version:'26.5',edition:2,steps:[],answers:[]}))")
        page.reload();page.wait_for_selector('#main h1');assert page.evaluate('getProgress().completed')==0
        blocked=browser.new_context(offline=True)
        blocked.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw Error('storage blocked')}})")
        bpage=blocked.new_page();bpage.goto((ROOT/'index.html').as_uri()+'#settings');bpage.wait_for_selector('#main h1')
        assert 'blocked' in bpage.locator('#main').inner_text().lower()
        assert not requests, requests
        assert not errors, errors
        print(f'PASS {name}: {len(routes)} offline routes; exact search, filters, progress, migration, print, focus, calculator, mobile, corrupt/blocked storage; no HTTP requests or JS errors')
        browser.close()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser',choices=['chromium','firefox','both'],default='both')
    args=parser.parse_args()
    for name in (('chromium','firefox') if args.browser=='both' else (args.browser,)):run(name)


if __name__=='__main__':main()
