#!/usr/bin/env python3
"""Exercise the real file:// library with networking disabled.
Development dependency: playwright. Reading never requires this dependency.
"""
import argparse
import json
import shutil
from pathlib import Path
import time
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = (ROOT / 'index.html').as_uri()
ARTIFACTS = ROOT / 'test-results'
ARTIFACTS.mkdir(exist_ok=True)


def run(browser_name, exhaustive):
    with sync_playwright() as pw:
        executable = shutil.which('chromium')
        options = {'executable_path': executable} if browser_name == 'chromium' and executable else {}
        browser = getattr(pw, browser_name).launch(headless=True, **options)
        context = browser.new_context(offline=True, viewport={'width':1440,'height':1000}, accept_downloads=True)
        network, errors = [], []
        context.on('request', lambda req: network.append(req.url) if req.url.startswith(('http:', 'https:')) else None)
        context.on('page', lambda p: p.on('pageerror', lambda e: errors.append(str(e))))
        page = context.new_page()
        page.on('dialog', lambda d: d.accept())
        page.goto(URL)
        assert 'Three crafts.' in page.locator('h1').inner_text()
        assert len(page.frames) == 1, 'Chooser must not load readers eagerly'
        assert not page.evaluate('Boolean(window.LIBRARY_SEARCH)'), 'Search is lazy'
        page.screenshot(path=ARTIFACTS/f'{browser_name}-home.png', full_page=True)

        last_navigation=0.0
        def visit(app, route):
            nonlocal last_navigation
            # Default Firefox rate-limits combined parent/child History API calls.
            if browser_name=='firefox':
                delay=0.15-(time.monotonic()-last_navigation)
                if delay>0:
                    page.wait_for_timeout(delay*1000)
            last_navigation=time.monotonic()
            page.evaluate('(value)=>{location.hash=value}', '#read/' + app + '/' + route)
            frame = page.frame(url=lambda url: '/manuals/' + app + '/index.html' in url)
            if not frame:
                page.wait_for_function('(app)=>!!document.querySelector(`iframe[data-app="${app}"]`)', arg=app)
                deadline=time.monotonic()+15
                while not frame and time.monotonic()<deadline:
                    page.wait_for_timeout(10)
                    frame=page.frame(url=lambda url:'/manuals/'+app+'/index.html' in url)
            assert frame, app
            expected = '#' + ('/' if app == 'photoshop' else '') + route
            try:
                frame.wait_for_function('(expected)=>location.hash===expected && !!document.querySelector("#main h1")', arg=expected)
            except Exception:
                print('ROUTE FAILURE', app, route, 'root', page.url, 'frame', frame.url, 'notice', page.locator('#notice').inner_text(), flush=True)
                raise
            assert not any(text in frame.locator('#main h1').inner_text().lower() for text in ['not found', 'does not exist']), (app, route)
            return frame

        ps = visit('photoshop', 'lesson/s01l01')
        ps.locator('[data-action="complete"]').click()
        ps.locator('[data-action="bookmark"]').first.click()
        ps.locator('[data-check]').first.check()
        # Native links and back/forward must produce one coherent library history.
        ps.locator('a[href="#/lesson/s01l02"]').first.click()
        page.wait_for_url('**#read/photoshop/lesson/s01l02')
        page.go_back()
        ps.wait_for_function("location.hash==='#/lesson/s01l01'")
        page.go_forward()
        ps.wait_for_function("location.hash==='#/lesson/s01l02'")
        page.get_by_role('link', name='Library', exact=True).click()
        page.wait_for_selector('[data-progress="photoshop"]')
        assert '1 / 75' in page.locator('[data-progress="photoshop"]').inner_text()

        pr = visit('premiere', 'lesson/L001')
        pr.locator('[data-complete="L001"]').check()
        pr.locator('[data-note="L001"]').fill('Host Linux → Windows VM; preserve this note.')
        pr.locator('[data-bookmark="L001"]').click()
        ae = visit('after-effects', 'lesson/logic')
        ae.locator('[data-step="logic:0"]').check()
        page.locator('#switcher').select_option('photoshop')
        ps.wait_for_function("location.hash==='#/lesson/s01l02'")
        assert len(page.frames) == 4

        page.get_by_role('link', name='Search all', exact=True).click()
        page.locator('#library-search').fill('alpha')
        assert page.locator('.result').count() > 0
        for app in ['photoshop', 'premiere', 'after-effects']:
            page.locator('#app-filter').select_option(app)
            assert page.locator('.result').count() > 0
            assert all(app in h for h in page.locator('.result').evaluate_all('(xs)=>xs.map(x=>x.hash)'))
        page.locator('#app-filter').select_option('')
        page.locator('#kind-filter').select_option('Field guide')
        page.locator('#library-search').fill('1001')
        assert page.locator('.result').count() > 0, 'Must search inside field-guide bodies'
        page.locator('#kind-filter').select_option('Shortcut')
        page.locator('#library-search').fill('Ctrl+S')
        assert page.locator('.result').count() >= 3
        page.locator('#app-filter').select_option('photoshop')
        page.locator('.result').first.click()
        ps.wait_for_function("location.hash.startsWith('#/shortcut/')")
        assert 'Ctrl+S' in ps.locator('#main').inner_text()

        page.get_by_role('link', name='Compare keys', exact=True).click()
        page.locator('#compare-search').fill('Ctrl+N')
        assert page.locator('.key-record').count() >= 3
        assert 'Photoshop' in page.locator('#key-results').inner_text()
        assert 'Premiere Pro' in page.locator('#key-results').inner_text()
        assert 'After Effects' in page.locator('#key-results').inner_text()

        page.get_by_role('link', name='Progress', exact=True).click()
        for key in ['large', 'contrast', 'oneStep']:
            page.locator(f'[data-library-preference="{key}"]').check()
        page.get_by_role('button', name='Apply to all three', exact=True).click()
        ps.wait_for_function("document.documentElement.dataset.large==='true'")
        pr.wait_for_function("document.body.classList.contains('one-step')")
        ae.wait_for_function("document.body.classList.contains('high-contrast')")
        with page.expect_download() as download:
            page.get_by_role('button', name='Export all progress', exact=True).click()
        backup = json.loads(Path(download.value.path()).read_text())
        assert backup['manuals']['photoshop']['state']['completed'] == ['s01l01']
        assert backup['manuals']['premiere']['state']['notes']['L001'].endswith('preserve this note.')
        assert backup['manuals']['after-effects']['state']['steps']['logic:0']
        assert all(backup['preferences'].values())

        def imported(value):
            page.locator('#import-library').set_input_files({'name':'progress.json','mimeType':'application/json','buffer':json.dumps(value).encode()})

        bad = json.loads(json.dumps(backup))
        bad['manuals']['photoshop']['state']['completed'] = []
        bad['manuals']['premiere']['state']['notes']['L001'] = 'This partial import must not apply'
        bad['manuals']['after-effects']['state']['steps']['logic:999'] = True
        imported(bad)
        page.wait_for_function("document.getElementById('notice').textContent.startsWith('Import rejected:')")
        assert ps.evaluate('window.ManualAdapter.get().completed') == ['s01l01']
        assert pr.evaluate('window.ManualAdapter.get().complete.L001') is True
        assert not ae.evaluate("window.ManualAdapter.get().steps['logic:999']")
        modified = json.loads(json.dumps(backup))
        modified['manuals']['photoshop']['state']['completed'] = []
        modified['manuals']['premiere']['state']['notes']['L001'] = 'Restored note'
        modified['manuals']['after-effects']['state']['steps'] = {}
        imported(modified)
        page.wait_for_function("document.getElementById('notice').textContent==='All three validated learning records imported.'")
        assert ps.evaluate('window.ManualAdapter.get().completed') == []
        assert pr.evaluate('window.ManualAdapter.get().notes.L001') == 'Restored note'
        assert ae.evaluate('Object.keys(window.ManualAdapter.get().steps).length') == 0
        imported(backup)
        page.wait_for_function("document.getElementById('notice').textContent==='All three validated learning records imported.'")
        ps.wait_for_function('window.ManualAdapter.get().completed.length===1')

        page.reload()
        page.wait_for_selector('h1')
        ps = visit('photoshop', 'lesson/s01l01')
        ps.wait_for_function('window.ManualAdapter.get().completed.length===1')
        ps.evaluate('()=>{window.printCalls=0;window.print=()=>{window.printCalls++};}')
        page.get_by_role('button',name='Print manual',exact=True).click()
        ps.wait_for_function('window.printCalls===1')
        page.keyboard.press('Control+p')
        ps.wait_for_function('window.printCalls===2')
        ps.locator('#main').press('Control+p')
        ps.wait_for_function('window.printCalls===3')
        # Printing a focused lesson expands the native reader's practice steps.
        assert ps.locator('.step-list li:visible').count() == 1
        page.emulate_media(media='print')
        assert ps.locator('.step-list li').evaluate_all('(xs)=>xs.every(x=>getComputedStyle(x).display!=="none")')
        page.emulate_media(media='screen')

        # Exercise every emitted record through the real parent -> reader protocol.
        page.evaluate("location.hash='#search'")
        page.wait_for_selector('#library-search')
        records = page.evaluate('window.LIBRARY_SEARCH')
        tested = 0
        for record in records:
            if not exhaustive and record['kind'] not in ['Lesson', 'Field guide', 'Topic']:
                continue
            frame = visit(record['app'], record['route'])
            if record['app'] == 'premiere' and record['route'].startswith('ref/'):
                assert frame.locator('.search-target').count() == 1, record
            if record['app'] == 'after-effects' and record['kind'] in ['Effect', 'Shortcut', 'Term', 'Troubleshooting']:
                assert frame.locator('.search-target').count() == 1, record
            tested += 1
            if tested % 300 == 0:
                print(f'{browser_name}: {tested} catalog routes', flush=True)

        # Root pages and specialist layouts at narrow widths, including large text.
        for width in [375, 768]:
            page.set_viewport_size({'width':width,'height':900})
            for name in ['home', 'search', 'compare', 'settings']:
                page.evaluate('(name)=>{location.hash=name}', '#'+name)
                page.wait_for_selector('#workspace h1')
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), (width, name)
            for app, path in [('photoshop','lesson/s01l01'),('premiere','lesson/L001'),('after-effects','lesson/logic')]:
                f=visit(app,path)
                assert f.evaluate('document.documentElement.scrollWidth<=innerWidth'), (width, app)
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), (width, app, 'shell')
        page.screenshot(path=ARTIFACTS/f'{browser_name}-mobile.png', full_page=True)

        # Block storage in the real local-file suite, then preserve all progress in-session.
        blocked=browser.new_context(offline=True,accept_downloads=True)
        blocked.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw Error('blocked for test')}})")
        bp=blocked.new_page();bp.goto(URL+'#read/photoshop/lesson/s01l01')
        bf=bp.frame(url=lambda url:'/manuals/photoshop/' in url)
        if not bf:
            bp.wait_for_selector('iframe[data-app="photoshop"]')
            bf=bp.frame(url=lambda url:'/manuals/photoshop/' in url)
        bf.wait_for_selector('[data-action="complete"]');bf.locator('[data-action="complete"]').click()
        bp.get_by_role('link',name='Library',exact=True).click()
        bp.get_by_role('link',name='Continue Photoshop →',exact=True).click()
        bf.wait_for_function('window.ManualAdapter.get().completed.length===1')
        bp.get_by_role('link',name='Progress',exact=True).click()
        assert 'Unavailable' in bp.locator('#workspace').inner_text()
        with bp.expect_download() as dl:
            bp.get_by_role('button',name='Export all progress',exact=True).click()
        assert json.loads(Path(dl.value.path()).read_text())['manuals']['photoshop']['state']['completed']==['s01l01']
        blocked.close()
        assert not errors, errors
        assert not network, network
        print(f'PASS {browser_name}: {tested} catalog routes; offline file://, history, switching, search, keys, preferences, complete backup/restore, invalid import, reload, printing, mobile and blocked storage. Zero HTTP requests / JS errors.', flush=True)
        browser.close()


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser',choices=['chromium','firefox','both'],default='both')
    parser.add_argument('--exhaustive',action='store_true')
    args=parser.parse_args()
    for name in (['chromium','firefox'] if args.browser=='both' else [args.browser]):
        run(name,args.exhaustive)
