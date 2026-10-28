"""Native shortcut grouping, filtering, shared recall keys, and source preservation."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  b=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}));p=b.new_page(offline=True);errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
  p.goto((ROOT/'index.html').as_uri());p.keyboard.press('Alt+m')
  for app,route,filter_id,count in [('after-effects','shortcuts','#listFilter',386),('premiere','ref/shortcuts','#refFilter',182),('photoshop','library/shortcuts','#ref-filter',112)]:
   p.evaluate('(h)=>location.hash=h','#read/'+app+'/'+route);p.wait_for_selector('iframe[data-app="'+app+'"]');f=p.frame(url=lambda u:'/manuals/'+app+'/' in u);f.wait_for_selector('.shortcut-study-tools')
   headings=f.locator('[data-native-shortcut-reference] .shortcut-category').all_text_contents();assert len(headings)==len(set(headings))
   assert f.locator('#native-recall .key-test').count()==count,(name,app)
   before=f.evaluate('JSON.stringify(window.ManualAdapter.get())')
   f.select_option('select[aria-label="Shortcut view"]','test');assert not f.locator('[data-test-answer]:visible').count()
   f.locator('.key-test').first.press('l');assert f.locator('[data-test-answer]:visible').count()==1
   f.locator('.key-test').first.press('j');f.locator('.key-test').nth(1).press('l');assert f.locator('[data-test-answer]:visible').count()==2
   f.locator('[data-study-action="reveal"]').click();assert f.locator('[data-test-answer]:visible').count()==count
   f.locator('[data-study-action="hide"]').click();assert not f.locator('[data-test-answer]:visible').count()
   f.locator(filter_id).fill('project');f.wait_for_function('(count)=>document.querySelectorAll("#native-recall .key-test").length<count',arg=count,polling=50)
   assert f.locator('select[aria-label="Shortcut view"]').input_value()=='test'
   f.locator(filter_id).fill('');f.wait_for_function('(count)=>document.querySelectorAll("#native-recall .key-test").length===count',arg=count,polling=50)
   f.select_option('select[aria-label="Shortcut view"]','reference');assert f.locator('[data-native-shortcut-reference]').is_visible()
   assert f.evaluate('JSON.stringify(window.ManualAdapter.get())')==before
  assert not errors,errors
  print('PASS',name,'native category headings once, all 680 recall cards, j/l reveal, reveal/hide all, live filters and unchanged learning state',flush=True);b.close()
