"""Real Chromium DOM tests via inline page injection when file:// is blocked by enterprise policy.
This tests interactive code in a real browser, but does NOT establish that file:// navigation succeeds
in an unrestricted browser. See AUDIT.md.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json,html
root=Path(__file__).resolve().parents[1]
# Same CSS/JS/data bytes are executed inline; only paths for external images are unavailable
# in about:blank under this container's administrator URLBlocklist.
css=(root/'assets/style.css').read_text();content=(root/'assets/content.js').read_text();app=(root/'assets/app.js').read_text()
page_html='<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style></head><body><a class="skip-link" id="skip-link" href="#main">Skip</a><div id="app"></div><script>'+content+'</script><script>'+app+'</script></body></html>'
logs=[]
def ok(label,fn):
 try:fn();logs.append(('PASS',label));print('PASS',label)
 except Exception as ex:logs.append(('FAIL',label));print('FAIL',label,str(ex)[:400]);raise

def nav(pg,hash):
 pg.evaluate('(h)=>location.hash=h',hash)
 pg.wait_for_timeout(80)

def assert_equals(a,b):
 assert a==b, f'{a!r} != {b!r}'
def assert_gte(a,b):
 assert a>=b, f'{a!r} < {b!r}'
def assert_true(a):
 assert a

with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 c=browser.new_context(viewport={'width':1440,'height':900},accept_downloads=True)
 c.set_offline(True)
 pg=c.new_page();errors=[];network=[]
 pg.on('pageerror',lambda e:errors.append(str(e)))
 pg.on('dialog',lambda dialog:dialog.accept())
 pg.on('request',lambda req:network.append(req.url) if req.url.startswith(('https://','http://')) else None)
 ok('Chromium inline DOM homepage loads with offline networking',lambda:(pg.set_content(page_html),pg.get_by_role('heading',name='Learn the craft. Keep the reference.').wait_for()))
 ok('skip-to-content focuses main without invalid route',lambda:(pg.locator('#skip-link').focus(),pg.keyboard.press('Enter'),assert_equals(pg.evaluate('location.hash'),''),assert_equals(pg.evaluate('document.activeElement.id'),'main')))
 ok('75 lesson links appear in sidebar',lambda:assert_equals(pg.locator('a.lesson-nav-link[href^="#/lesson/"]').count(),75))
 pg.screenshot(path=str(root/'audit/screenshots/simulated-desktop-home.png'),full_page=False)
 nav(pg,'#/lesson/s01l01')
 ok('lesson walkthrough and all structural sections',lambda:(pg.get_by_role('heading',name='What Photoshop edits: pixels versus vectors').wait_for(),assert_gte(pg.locator('.step-list li').count(),4),assert_gte(pg.locator('.lesson-section').count(),7)))
 ok('knowledge check grades',lambda:(pg.locator('input[name="quiz-s01l01"]').nth(2).check(),pg.get_by_role('button',name='Check answer').click(),pg.locator('.answer').wait_for()))
 ok('completion state updates layout',lambda:(pg.get_by_role('button',name='Mark lesson complete').click(),pg.get_by_role('button',name='✓ Completed · Undo').wait_for(),pg.locator('.topbar').get_by_text('1/75 lessons').wait_for()))
 ok('next lesson link works',lambda:assert_gte(pg.locator('a[href="#/lesson/s01l02"]').count(),1))
 nav(pg,'#/search')
 ok('search index returns filter and lesson matches',lambda:(pg.locator('#search-input').fill('Gaussian Blur'),assert_gte(pg.locator('.result').count(),3)))
 pg.screenshot(path=str(root/'audit/screenshots/simulated-desktop-search.png'),full_page=False)
 nav(pg,'#/library/shortcuts')
 ok('shortcuts render and filter',lambda:(assert_gte(pg.locator('.ref-table tbody tr').count(),60),pg.locator('#ref-filter').fill('Ctrl+T'),assert_gte(pg.locator('.ref-table tbody tr').count(),1)))
 nav(pg,'#/ref/tools/tool-pen')
 ok('tool detail',lambda:pg.get_by_role('heading',name='Pen',exact=True).wait_for())
 nav(pg,'#/ref/filters/filter-gaussian-blur')
 ok('filter detail',lambda:pg.get_by_role('heading',name='Gaussian Blur',exact=True).wait_for())
 ok('reference bookmarking',lambda:(pg.get_by_role('button',name='☆ Bookmark').click(),pg.get_by_role('button',name='★ Saved').wait_for()))
 nav(pg,'#/progress')
 ok('saved reference appears in bookmark list',lambda:assert_gte(pg.locator('a[href="#/ref/filters/filter-gaussian-blur"]').count(),1))
 ok('dark and light theme',lambda:(pg.locator('[data-action="theme"]').click(),assert_equals(pg.evaluate('document.documentElement.dataset.theme'),'dark'),pg.locator('[data-action="theme"]').click(),assert_equals(pg.evaluate('document.documentElement.dataset.theme'),'light')))
 nav(pg,'#/progress')
 with pg.expect_download() as dl:pg.locator('[data-action="export"]').click()
 file=root/'audit/progress-smoke.json';dl.value.save_as(file)
 data=json.loads(file.read_text())
 ok('portable JSON download carries completed lesson',lambda:(assert_equals(data['schema'],1),assert_true('s01l01' in data['state']['completed'])))
 # about:blank has no persistent localStorage, but simulated UI keeps its in-memory state.
 pg.set_content(page_html)
 nav(pg,'#/progress')
 ok('portable progress import from file',lambda:(pg.locator('#import-file').set_input_files(str(file)),pg.locator('.topbar').get_by_text('1/75 lessons').wait_for()))
 ok('keyboard / navigates to search',lambda:(pg.locator('body').click(position={'x':1000,'y':350}),pg.keyboard.press('/'),pg.locator('#search-input').wait_for()))
 assert not errors,errors
 assert not network,network
 print('PASS no JavaScript exceptions and no remote HTTP requests')
 c2=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,device_scale_factor=1)
 c2.set_offline(True);m=c2.new_page();m.set_content(page_html);nav(m,'#/lesson/s03l03')
 ok('mobile lesson layout',lambda:m.get_by_role('heading',name='Layer masks: hiding without deleting').wait_for())
 m.screenshot(path=str(root/'audit/screenshots/simulated-mobile-lesson.png'),full_page=False)
 ok('mobile navigation',lambda:(m.get_by_role('button',name='Open navigation').click(),m.locator('body.menu-open').wait_for(),m.locator('.menu-backdrop').click(force=True),m.locator('body:not(.menu-open)').wait_for()))
 ok('mobile has no horizontal overflow',lambda:assert_true(m.evaluate('document.documentElement.scrollWidth <= innerWidth+1')))
 print('COMPLETE:',len(logs),'real Chromium UI interactions under inline-content simulation')
 c2.close();c.close();browser.close()
