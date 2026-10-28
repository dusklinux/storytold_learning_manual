"""Optional Vim navigation: real file URLs and cross-reader mode synchronization."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  b=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}));c=b.new_context(offline=True,viewport={'width':1280,'height':800});errors=[]
  c.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
  p=c.new_page();p.goto((ROOT/'index.html').as_uri())
  assert p.locator('#vim-toggle').get_attribute('aria-pressed')=='false'
  p.keyboard.press('Alt+m');assert p.locator('#vim-toggle').get_attribute('aria-pressed')=='true'
  p.keyboard.press('/');p.wait_for_selector('#library-search');assert 'without clearing' in p.locator('#search-help').inner_text();p.locator('#library-search').press_sequentially('maskjk')
  assert p.locator('#library-search').input_value()=='maskjk'
  p.locator('#library-search').fill('mask');p.keyboard.press('Escape');assert p.locator('.result').first.evaluate('(x)=>x===document.activeElement')
  p.keyboard.press('j');assert p.locator('.result').nth(1).evaluate('(x)=>x===document.activeElement')
  p.keyboard.press('k');assert p.locator('.result').first.evaluate('(x)=>x===document.activeElement')
  p.keyboard.press('G');assert p.locator('.result').last.evaluate('(x)=>x===document.activeElement')
  p.keyboard.press('g');assert p.locator('.result').first.evaluate('(x)=>x===document.activeElement')
  p.keyboard.press('/');assert p.locator('#library-search').evaluate('(x)=>x===document.activeElement')
  p.locator('#app-filter').focus();p.keyboard.press('j');assert p.locator('#app-filter').evaluate('(x)=>x===document.activeElement')
  for app,route in [('photoshop','lesson/s01l01'),('premiere','lesson/L001'),('after-effects','lesson/logic')]:
   p.evaluate('(v)=>location.hash=v','#read/'+app+'/'+route);p.wait_for_selector('iframe[data-app="'+app+'"]');f=p.frame(url=lambda u:'/manuals/'+app+'/' in u);f.wait_for_function('window.ManualVim?.enabled()',polling=50)
   f.locator('#main').focus();f.locator('#main').press('Alt+m');p.wait_for_function("document.getElementById('vim-toggle').getAttribute('aria-pressed')==='false'")
   f.locator('#main').press('Alt+m');p.wait_for_function("document.getElementById('vim-toggle').getAttribute('aria-pressed')==='true'")
   f.locator('#main').press('G');assert f.evaluate('scrollY')>0
   f.locator('#main').press('g');assert f.evaluate('scrollY')==0
   f.locator('#main').press('j');assert f.evaluate('scrollY')>0
   if app=='premiere':
    f.locator('[data-note="L001"]').press_sequentially('jk g G /');assert f.locator('[data-note="L001"]').input_value()=='jk g G /'
   f.locator('#main').press('/');p.wait_for_selector('#library-search')
   p.wait_for_function("document.activeElement.id==='library-search'")
  p.keyboard.press('Alt+m');assert p.locator('#vim-toggle').get_attribute('aria-pressed')=='false'
  p.locator('#library-search').fill('jk');assert p.locator('#library-search').input_value()=='jk'
  p.reload();p.wait_for_selector('#vim-toggle');assert p.locator('#vim-toggle').get_attribute('aria-pressed')=='false'
  for width in [320,768]:
   p.set_viewport_size({'width':width,'height':800});assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
  assert not errors,errors
  print('PASS',name,'Vim toggle, search navigation, typing/select preservation, three-reader scrolling, search handoff, persistence and mobile',flush=True);b.close()
