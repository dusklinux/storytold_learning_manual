"""Shared appearance, contrast, offline resources and native reader regressions."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
def luminance(rgb):
    values=[v/255 for v in rgb]
    values=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in values]
    return sum(a*b for a,b in zip(values,[.2126,.7152,.0722]))
def ratio(a,b):
    a,b=sorted([luminance(a),luminance(b)])
    return (b+.05)/(a+.05)
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  browser=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}))
  c=browser.new_context(offline=True,viewport={'width':1440,'height':1000});errors=[];remote=[]
  c.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
  c.on('request',lambda r:remote.append(r.url) if r.url.startswith(('http:','https:')) else None)
  p=c.new_page();p.goto((ROOT/'index.html').as_uri())
  assert p.evaluate('window.ManualPalette.current()')=='ember-dark'
  palettes=p.evaluate('window.ManualPalette.palettes');assert len(palettes)==6
  # All core text/link tokens meet WCAG normal-text contrast on all surfaces.
  for palette in palettes:
   p.select_option('#palette-select',palette['id'])
   assert p.evaluate('getComputedStyle(document.documentElement).colorScheme')==palette['mode']
   colors=p.evaluate("""()=>Object.fromEntries(['bg','paper','soft','ink','muted','accent','good','bad'].map(k=>{const hex=getComputedStyle(document.documentElement).getPropertyValue('--t-'+k).trim();return [k,hex.match(/[a-f0-9]{2}/gi).map(x=>parseInt(x,16))]}))""")
   for fg in ['ink','muted','accent','good','bad']:
    for bg in ['bg','paper','soft']:
     assert ratio(colors[fg],colors[bg])>=4.5,(palette['id'],fg,bg,ratio(colors[fg],colors[bg]))
   for app,route in [('photoshop','lesson/s01l01'),('premiere','lesson/L001'),('after-effects','lesson/logic')]:
    p.evaluate('(h)=>location.hash=h','#read/'+app+'/'+route);p.wait_for_selector('iframe[data-app="'+app+'"]')
    f=p.frame(url=lambda u:'/manuals/'+app+'/' in u);f.wait_for_function('(id)=>window.ManualPalette?.current()===id',arg=palette['id'],polling=50)
    f.wait_for_selector('#main h1')
    assert f.evaluate('getComputedStyle(document.documentElement).colorScheme')==palette['mode']
    assert f.evaluate("getComputedStyle(document.body).backgroundColor")==f.evaluate("()=>{const e=document.createElement('i');e.style.color='var(--t-bg)';document.body.append(e);const color=getComputedStyle(e).color;e.remove();return color}")
    for button in f.locator('.button.primary,.btn:not(.ghost):not(.light)').all():
     pair=button.evaluate(r"e=>[getComputedStyle(e).color,getComputedStyle(e).backgroundColor].map(v=>v.match(/\d+/g).slice(0,3).map(Number))")
     assert ratio(*pair)>=4.5,(palette['id'],app,pair)
    # Palette aliases must survive native rerenders and stronger-contrast preferences.
    f.evaluate("document.body.classList.add('high-contrast')")
    assert f.evaluate("getComputedStyle(document.body).getPropertyValue('--ink').trim()")
    f.evaluate("document.body.classList.remove('high-contrast')")
   p.get_by_role('link',name='Library',exact=True).click()
  p.select_option('#palette-select','woodland-dark');p.reload();assert p.locator('#palette-select').input_value()=='woodland-dark'
  p.evaluate("location.hash='#read/premiere/lesson/L001'");p.wait_for_selector('iframe[data-app="premiere"]');f=p.frame(url=lambda u:'/manuals/premiere/' in u);f.wait_for_function("window.ManualPalette?.current()==='woodland-dark'",polling=50)
  f.locator('#themeToggle').click();p.wait_for_function("window.ManualPalette.current()==='woodland-light'")
  assert f.locator('#themeToggle').get_attribute('aria-label')=='Switch to dark palette'
  for width in [320,768]:
   p.get_by_role('link',name='Library',exact=True).click();p.set_viewport_size({'width':width,'height':800});assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
  p.set_viewport_size({'width':1440,'height':1000});p.select_option('#palette-select','ember-dark')
  p.screenshot(path=ROOT/'test-results'/f'{name}-palette.png',full_page=True)
  p.emulate_media(media='print');assert p.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--t-bg').trim()")=='#fff';p.emulate_media(media='screen')
  # Standalone file URLs also default dark and retain functional theme controls.
  solo=c.new_page();solo.goto((ROOT/'manuals/photoshop/index.html').as_uri());solo.wait_for_selector('[data-action="theme"]');assert solo.evaluate('window.ManualPalette.current()')=='ember-dark'
  solo.locator('[data-action="theme"]').click();assert solo.evaluate('window.ManualPalette.current()')=='ember-light'
  blocked=browser.new_context(offline=True)
  blocked.add_init_script("""for(const method of ['getItem','setItem']){const original=Storage.prototype[method];Storage.prototype[method]=function(key,...args){if(key==='dusky-adobe-palette')throw Error('storage unavailable');return original.call(this,key,...args)}}""")
  bp=blocked.new_page();bp.goto((ROOT/'index.html').as_uri());bp.select_option('#palette-select','ocean-light');assert bp.evaluate('window.ManualPalette.current()')=='ocean-light';blocked.close()
  assert not errors,errors
  assert not remote,remote
  print('PASS',name,'six palettes, 90 text contrast pairs, all readers, native toggle sync, reload, standalone, mobile and offline',flush=True);browser.close()
