#!/usr/bin/env python3
"""Offline Chromium regression, including improvements borrowed from the supplied AE reader.
Uses the exact published HTML, JS and CSS bytes inlined into a DOM because file:// is blocked
by this execution environment. Requires Playwright/Chromium only for development testing.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).resolve().parent.parent
D=json.loads((P/'data/course.json').read_text())
G=json.loads((P/'data/guides.json').read_text())
html=(P/'index.html').read_text()
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+(P/'style.css').read_text()+'</style>')
for name in ('data.js','guides.js','app.js'):
 html=html.replace(f'<script src="{name}"></script>','<script>'+(P/name).read_text()+'</script>')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 context=browser.new_context(offline=True,viewport={'width':1440,'height':920},accept_downloads=True)
 page=context.new_page();errors=[];http=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('request',lambda r:http.append(r.url) if r.url.startswith(('http://','https://')) else None)
 page.set_content(html,wait_until='load')
 assert page.title().startswith('Premiere')
 def visit(r):
  page.evaluate('(r)=>{location.hash="#"+r;render(false)}',r)
  assert page.locator('#main h1').count()>0,r
 def key(t,r):
  if t=='shortcuts':return ' | '.join((r['command'],r['windows'],r['context']))
  if t=='effects':return ' | '.join((r['kind'],r['name']))
  if t=='transitions':return ' | '.join((r['category'],r['name']))
  if t=='panels':return r['name']
  return r['term']
 routes=0
 for l in D['lessons']:
  visit('lesson/'+l['id']);assert page.locator('#main h1').inner_text()==l['title'];routes+=1
 for s in D['stages']:
  visit('stage/'+str(s['id']));assert page.locator('.question').count()==3;routes+=1
 for r in D['recipes']:
  visit('recipe/'+r['id']);assert page.locator('#main h1').inner_text()==r['title'];routes+=1
 for r in D['troubleshooting']:
  visit('trouble/'+r['id']);assert page.locator('#main h1').inner_text()==r['title'];routes+=1
 for g in G:
  visit('guide/'+g['id']);assert page.locator('.guide-article').count()==1;routes+=1
 for t in ('shortcuts','effects','transitions','panels','glossary'):
  for r in D[t]:
   import urllib.parse
   visit('ref/'+t+'/'+urllib.parse.quote(key(t,r),safe=''))
   assert page.locator('.search-target').count()==1,(t,key(t,r))
   assert key(t,r)==page.locator('.search-target').get_attribute('data-ref-key')
   routes+=1
 print('Routes:',routes,flush=True)
 # Search opens the precise matching row, not a generic catalog landing page.
 visit('search')
 page.locator('#searchInput').fill('Lumetri')
 result=page.locator('a.search-result[href^="#ref/effects/"]').filter(has_text='Lumetri Color').first
 assert result.count()==1,'Missing exact effects deep link'
 result.click();page.wait_for_selector('.search-target',timeout=5000);assert page.locator('.search-target').count()==1
 assert 'Lumetri Color' in page.locator('.search-target').inner_text()
 # Check that reference filtering retains keyboard focus, and strips targeted route.
 page.locator('#refFilter').fill('Lumetri')
 assert page.locator('.ref-item').count()>=1
 assert page.evaluate('location.hash')=='#ref/effects'
 # Controls and completion state.
 visit('lesson/L001')
 page.locator('[data-check="L001:0"]').check()
 page.locator('[data-complete="L001"]').check()
 visit('stage/1')
 page.locator('[data-quiz="Q001"][data-choice="0"]').click()
 assert page.locator('[data-quiz="Q001"][data-choice="0"]').evaluate('(x)=>x===document.activeElement')
 # Reading settings propagate to fresh pages, one step is truly focused.
 visit('settings')
 for k in ('large','contrast','oneStep'):
  page.locator('#'+k+'Toggle').check()
  assert page.locator('#'+k+'Toggle').evaluate('(x)=>x===document.activeElement')
 visit('lesson/L021')
 assert page.locator('.practice-step:visible').count()==1
 page.emulate_media(media='print')
 assert page.locator('.practice-step:visible').count()==len(next(l['steps'] for l in D['lessons'] if l['id']=='L021'))
 page.emulate_media(media='screen')
 page.locator('[data-check="L021:0"]').check()
 assert page.locator('.practice-step:visible').count()==1
 assert page.locator('[data-check="L021:1"]').is_visible()
 # Export backwards-compatible schema and reading preferences.
 visit('settings')
 with page.expect_download() as down:page.locator('[data-action="export"]').click()
 saved=json.loads(Path(down.value.path()).read_text())
 assert saved['oneStep'] and saved['large'] and saved['contrast']
 assert saved['complete']['L001'] is True and saved['checks']['L021:0'] is True
 assert saved['schema']=='premiere-explained-progress-v1'
 # Import from v2: optional preferences are absent; they should default to false.
 old={k:v for k,v in saved.items() if k not in ('large','contrast','oneStep')}
 page.on('dialog',lambda dlg:dlg.accept())
 page.locator('#importFile').set_input_files({'name':'old.json','mimeType':'application/json','buffer':json.dumps(old).encode()})
 page.wait_for_function('state.oneStep===false && state.large===false && state.contrast===false')
 assert page.evaluate("state.complete['L001'] === true")
 previous=page.evaluate('JSON.stringify(state)')
 bads=[
  {'schema':'premiere-explained-progress-v1','complete':[], 'bookmarks':{},'checks':{},'answers':{},'notes':{}},
  {**old,'answers':{'Q001':99}},
  {**old,'checks':{'L999:0':True}},
  {**old,'complete':{'__proto__':True}},
  {**old,'notes':{'L001':22}},
 ]
 for i,bad in enumerate(bads):
  page.locator('#importFile').set_input_files({'name':f'invalid{i}.json','mimeType':'application/json','buffer':json.dumps(bad).encode()})
  page.wait_for_function('document.getElementById("toast").textContent.includes("Could not import")')
  assert page.evaluate('JSON.stringify(state)')==previous,f'Invalid import changed data: {i}'
 # In this sandbox, file:// and HTTP navigations are blocked by the harness and
 # about:blank localStorage is denied. Simulate a writable/blocked browser store
 # before loading the same published scripts; do not claim it is a real file test.
 corrupt=browser.new_context(offline=True,accept_downloads=True)
 cp=corrupt.new_page();cp.evaluate("""window.__store={'premiere_manual_progress':JSON.stringify({schema:'premiere-explained-progress-v1',checks:[]})};Object.defineProperty(window,'localStorage',{configurable:true,get(){return {setItem(k,v){window.__store[k]=v},getItem(k){return window.__store[k]||null},removeItem(k){delete window.__store[k]}}}})""")
 cp.set_content(html,wait_until='load')
 assert cp.evaluate('storageWorks === true && storedProgressInvalid === true')
 assert cp.evaluate('completed()')==0
 cp.evaluate('location.hash="#lesson/L001";render(false)')
 cp.locator('[data-complete="L001"]').check()
 assert cp.evaluate('completed()')==1
 assert cp.evaluate("JSON.parse(window.__store.premiere_manual_progress).complete.L001===true")
 corrupt.close()
 blocked=browser.new_context(offline=True,accept_downloads=True)
 bp=blocked.new_page();bp.evaluate("Object.defineProperty(window,'localStorage',{configurable:true,get(){throw Error('storage denied')}})")
 bp.set_content(html,wait_until='load')
 assert bp.evaluate('storageWorks===false')
 bp.evaluate('location.hash="#lesson/L001";render(false)')
 bp.locator('[data-complete="L001"]').check()
 assert bp.evaluate('completed()')==1
 with bp.expect_download() as out:bp.locator('#exportProgress').click()
 assert json.loads(Path(out.value.path()).read_text())['complete']['L001']
 blocked.close()
 # No layout overflow at requested phone/tablet widths with reading prefs.
 for w in (375,768):
  page.set_viewport_size({'width':w,'height':900})
  for route in ('overview','lesson/L060','ref/effects','ref/shortcuts','settings','guide/05-WINDOWS-VM'):
   visit(route)
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(w,route)
 assert not http,http
 assert not errors,errors
 print(f'PASS Chromium: {routes} offline content routes; exact reference lookup; print expansion; accessible prefs; JSON migration, adversarial imports; corrupt/blocked storage; responsive layout; 0 remote requests; 0 JS errors')
 browser.close()
