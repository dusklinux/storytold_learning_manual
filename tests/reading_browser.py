"""Full-height layout and non-destructive h/l navigation across offline readers."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  b=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}))
  c=b.new_context(offline=True,viewport={'width':1280,'height':800});errors=[]
  c.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
  p=c.new_page();p.goto((ROOT/'index.html').as_uri());p.keyboard.press('Alt+m')
  def layout(what):
   if not p.locator('#reading-tools').evaluate('e=>e.open'):p.locator('#reading-tools summary').click()
   p.locator('[data-layout="'+what+'"]').click()
   assert not p.locator('#reading-tools').evaluate('e=>e.open')
  for app,route in [('photoshop','lesson/s01l02'),('premiere','lesson/L002'),('after-effects','lesson/logic')]:
   p.evaluate('(h)=>location.hash=h','#read/'+app+'/'+route);p.wait_for_selector('iframe[data-app="'+app+'"]');f=p.frame(url=lambda u:'/manuals/'+app+'/' in u);f.wait_for_function('!!window.ManualReading',polling=50);f.wait_for_selector('#main h1');f.wait_for_function('(hash)=>location.hash===hash',arg=('#/' if app=='photoshop' else '#')+route,polling=50)
   if not p.locator('#reading-tools').evaluate('e=>e.open'):p.locator('#reading-tools summary').click()
   assert p.locator('#reading-tools summary').bounding_box()['width']<=40
   before=f.evaluate('JSON.stringify(window.ManualAdapter.get())')
   height=p.locator('iframe[data-app="'+app+'"]').bounding_box()['height']
   layout('focus');f.wait_for_function("document.documentElement.classList.contains('reader-focus')",polling=50)
   assert not p.locator('.library-bar').is_visible();assert not f.locator('.topbar').is_visible()
   assert p.locator('iframe[data-app="'+app+'"]').bounding_box()['height']==800
   assert height<800
   layout('map');f.wait_for_function("document.documentElement.classList.contains('reader-map-hide')",polling=50);assert not f.locator('.sidebar').is_visible()
   assert f.locator('#main').bounding_box()['x']<100
   f.locator('#main').focus();f.locator('#main').press('l');assert f.locator('.reader-step-current').count()==1
   f.locator('.reader-step-current').press('l');assert f.locator('.reader-step-current').evaluate('x=>Array.from(x.parentElement.children).indexOf(x)')==1
   f.locator('.reader-step-current').press('h');assert f.locator('.reader-step-current').evaluate('x=>Array.from(x.parentElement.children).indexOf(x)')==0
   assert f.evaluate('JSON.stringify(window.ManualAdapter.get())')==before
   old=p.url
   total=f.locator('.step-list>li,.steps>.step,.practice-step').count()
   for _ in range(total):f.locator('.reader-step-current').press('l')
   assert p.url==old,'Walkthrough navigation must not skip the rest of the lesson'
   assert f.locator('.reader-step-current').evaluate("x=>['H2','H3'].includes(x.tagName)")
   # Bottom-of-page l follows the actual next link, without marking completion.
   f.evaluate('window.scrollTo({top:document.documentElement.scrollHeight,behavior:"instant"})');old=p.url;f.locator('#main').press('l');p.wait_for_function('(old)=>location.href!==old',arg=old)
   # Independent controls: map can return while top bars stay hidden.
   layout('map');f.wait_for_function("document.documentElement.classList.contains('reader-map-show')",polling=50);assert f.locator('.sidebar').is_visible();assert not f.locator('.topbar').is_visible()
   layout('focus');f.wait_for_function("!document.documentElement.classList.contains('reader-focus')",polling=50);assert f.locator('.topbar').is_visible()
  # Native one-step controls move without checking off work.
  for app,route,enable,step in [('photoshop','lesson/s01l02','[data-action="focusstep"]','.step-list>li'),('premiere','lesson/L002',None,'.practice-step'),('after-effects','lesson/logic','#oneStepToggle','.steps>.step')]:
   p.evaluate('(h)=>location.hash=h','#read/'+app+'/'+route);p.wait_for_selector('iframe[data-app="'+app+'"]');f=p.frame(url=lambda u:'/manuals/'+app+'/' in u);f.wait_for_selector('#main h1');f.wait_for_function('(hash)=>location.hash===hash',arg=('#/' if app=='photoshop' else '#')+route,polling=50)
   if enable:f.locator(enable).click()
   else:f.evaluate("()=>{const s=window.ManualAdapter.get();s.oneStep=true;window.ManualAdapter.set(s)}")
   before=f.evaluate('JSON.stringify(window.ManualAdapter.get())');f.locator('#main').focus();f.locator('#main').press('l');f.wait_for_selector('.reader-step-current');assert f.locator('.reader-step-current').is_visible();assert f.evaluate('JSON.stringify(window.ManualAdapter.get())')==before
  p.emulate_media(media='print');assert not f.locator('.sidebar').is_visible();assert not p.locator('#reading-tools').is_visible();assert all(step.evaluate("x=>getComputedStyle(x).display!=='none'") for step in f.locator('.steps>.step').all());p.emulate_media(media='screen')
  # Shortcut restores bars even when focus is inside a reader.
  f.locator('#main').press('Alt+Shift+f');p.wait_for_function("document.documentElement.classList.contains('reader-focus')")
  p.reload();p.wait_for_selector('iframe');p.locator('#reading-tools').evaluate('e=>e.open=true');assert p.evaluate("document.documentElement.classList.contains('reader-focus')")
  layout('focus')
  p.set_viewport_size({'width':375,'height':800});f=p.frame(url=lambda u:'/manuals/after-effects/' in u);f.wait_for_selector('#main h1')
  # Explicit show/hide works even with the mobile sidebar normally off-screen.
  layout('map');layout('map')
  f.locator('#main').press('Escape');f.wait_for_function("document.documentElement.classList.contains('reader-map-hide')",polling=50)
  f.locator('#toggleMenu').click();f.wait_for_function("document.documentElement.classList.contains('reader-map-show')",polling=50)
  f.locator('#main').press('Escape');f.wait_for_function("document.documentElement.classList.contains('reader-map-hide')",polling=50)
  assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
  p.get_by_role('link',name='Library',exact=True).click();assert not p.locator('#reading-tools').is_visible();assert p.locator('.library-bar').is_visible()
  assert not errors,errors
  print('PASS',name,'full-height focus, independent map, h/l steps and lessons, untouched completion, native one-step modes, persistence, shortcuts and mobile',flush=True);b.close()
