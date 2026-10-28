"""Expanded, offline Chromium regression using the final self-contained index.html.

The test host blocks file:// navigation. This executes the identical inline HTML bytes
with page.set_content(), exercising the browser and interactions, but does not certify
native file URL launch or real persistent storage across browser restarts.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'content/content.json').read_text(encoding='utf-8'))
HTML=(ROOT/'index.html').read_text(encoding='utf-8')
passed=0

def test(name,cb):
 global passed
 cb();passed+=1;print('PASS',name,flush=True)

def ok(condition,message='assertion failed'):
 assert condition,message

with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 ctx=browser.new_context(offline=True,accept_downloads=True,viewport={'width':1440,'height':900})
 page=ctx.new_page();errors=[];network=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('request',lambda r:network.append(r.url) if r.url.startswith(('https://','http://')) else None)
 page.on('dialog',lambda d:d.accept())
 test('actual bundled inline HTML opens offline',lambda:(page.set_content(HTML),page.get_by_role('heading',name='Learn the craft. Keep the reference.').wait_for()))
 def nav(h):
  page.evaluate('(h)=>{location.hash=h;window.dispatchEvent(new HashChangeEvent("hashchange"))}',h)
  ok(page.locator('#main h1').count()==1,h)
 test('all 12 stage routes',lambda:[nav('#/stage/'+str(s['id'])) for s in DATA['stages']])
 test('all 75 lesson routes',lambda:[nav('#/lesson/'+l['id']) for l in DATA['lessons']])
 test('all detailed reference routes',lambda:[nav('#/ref/'+fam+'/'+r['id']) for fam in ('tools','filters','glossary','recipes','troubleshooting') for r in DATA[fam]])
 test('malformed and missing routes do not crash',lambda:[nav(h) for h in ('#/lesson/does-not-exist','#/ref/filters/bogus','#/%bad%zz','#/ref/%xy')])
 nav('#/progress')
 test('reading preferences are discoverable',lambda:ok(page.get_by_role('heading',name='Reading preferences').count()==1))
 def settings():
  page.locator('[data-action="large"]').click()
  ok(page.evaluate('document.documentElement.dataset.large')=='true')
  page.locator('[data-action="contrast"]').click()
  ok(page.evaluate('document.documentElement.dataset.contrast')=='true')
  page.locator('[data-action="focusstep"]').click()
  nav('#/lesson/s01l01')
  ok(page.locator('.step-list li:visible').count()==1)
  ok(page.locator('.step-list li').count()>=4)
  page.locator('[data-action="stepnext"]').click()
  ok('Step 2 of' in page.locator('.step-toolbar').inner_text())
  ok(page.locator('.step-list li:visible').count()==1)
  page.emulate_media(media='print')
  ok(page.locator('.step-list li:visible').count()==page.locator('.step-list li').count())
  page.emulate_media(media='screen')
 test('large text, contrast, focused steps, print restores all actions',settings)
 def answer():
  page.locator('input[name="quiz-s01l01"]').nth(2).check()
  page.get_by_role('button',name='Check answer').click()
  ok(page.locator('.answer').count()==1)
  page.locator('input[data-check]').first.check()
  page.locator('[data-action="complete"]').click()
  ok('1/75 lessons' in page.locator('.topbar').inner_text())
 test('quiz, checklist and lesson completion',answer)
 nav('#/progress')
 with page.expect_download() as dl:page.locator('[data-action="export"]').click()
 backup=json.loads(Path(dl.value.path()).read_text(encoding='utf-8'))
 test('export includes version, progress and preferences',lambda:(ok(backup['edition']=='1.2.0'),ok(backup['photoshop_version']=='27.11'),ok(backup['state']['largeText'] and backup['state']['highContrast'] and backup['state']['focusStep']),ok(backup['state']['completed']==['s01l01'])))
 def import_data(x,name):
  nav('#/progress')
  page.locator('#import-file').set_input_files({'name':name,'mimeType':'application/json','buffer':json.dumps(x).encode('utf-8')})
  page.wait_for_timeout(50)
 def invalid_imports():
  before=page.locator('.topbar').inner_text()
  for k,v in [('completed',['unknown-lesson']),('bookmarks',['#/ref/tools/not-a-real-tool'])]:
   x=json.loads(json.dumps(backup));x['state'][k]=v
   import_data(x,'invalid-'+k+'.json')
   ok('Import failed' in page.locator('#live-status').inner_text())
   ok(page.locator('.topbar').inner_text()==before)
  x=json.loads(json.dumps(backup));x['photoshop_version']='26.0'
  import_data(x,'wrong-release.json')
  ok('Import failed' in page.locator('#live-status').inner_text())
  ok(page.locator('.topbar').inner_text()==before)
  x=json.loads(json.dumps(backup));x['state']['checks']['s01l01:200']=True
  import_data(x,'invalid-check.json')
  ok('Import failed' in page.locator('#live-status').inner_text())
 test('invalid imports rejected atomically, including wrong Photoshop version',invalid_imports)
 def legacy_import():
  x=json.loads(json.dumps(backup));x['edition']='1.1.0';
  for k in ('largeText','highContrast','focusStep'):x['state'].pop(k,None)
  import_data(x,'previous-edition.json')
  ok('Validated progress backup imported.' in page.locator('#live-status').inner_text())
  ok('1/75 lessons' in page.locator('.topbar').inner_text())
  nav('#/progress')
  ok(page.locator('[data-action="large"]').get_attribute('aria-pressed')=='false')
 test('v1.1 progress backup remains importable',legacy_import)
 def search():
  nav('#/search')
  page.locator('#search-input').fill('Gaussian Blur')
  ok(page.locator('.result').count()>=3)
  page.locator('body').click(position={'x':1100,'y':350})
  page.keyboard.press('/')
  ok(page.locator('#search-input').count()==1)
 test('offline search and keyboard navigation',search)
 def blocked_storage():
  p=ctx.new_page();errs=[];p.on('pageerror',lambda e:errs.append(str(e)))
  p.add_init_script('Object.defineProperty(window,"localStorage",{get(){throw Error("blocked")}})')
  p.set_content(HTML)
  p.evaluate('location.hash="#/progress"')
  p.get_by_role('heading',name='Progress & portable backup').wait_for()
  # On about:blank origin localStorage is inherently disabled; the app must still work.
  ok(p.locator('#main h1').count()==1)
  ok(not errs,errs)
  p.close()
 test('browser storage unavailable without breaking reading',blocked_storage)
 def mobile():
  for w in (375,390,768):
   page.set_viewport_size({'width':w,'height':844})
   for h in ('#/home','#/lesson/s01l01','#/library/shortcuts','#/progress'):
    nav(h)
    ok(page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'),f'{w} {h}')
 test('responsive behavior at 375, 390 and 768 pixels',mobile)
 test('no runtime Javascript errors',lambda:ok(not errors,errors))
 test('no external HTTP requests offline',lambda:ok(not network,network))
 print('RESULT:',passed,'extended offline browser assertions passed')
 ctx.close();browser.close()
