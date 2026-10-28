"""Real file:// fuzzy-search interactions. Optional Playwright development dependency."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  browser=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}))
  context=browser.new_context(offline=True,viewport={'width':1440,'height':1000})
  errors=[];remote=[];failed=[]
  context.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
  context.on('request',lambda r:remote.append(r.url) if r.url.startswith(('http:','https:')) else None)
  context.on('requestfailed',lambda r:failed.append(r.url))
  page=context.new_page();page.goto((ROOT/'index.html').as_uri())
  assert not page.evaluate('Boolean(window.LibrarySearchEngine||window.LIBRARY_SEARCH)')
  page.keyboard.press('Control+k');page.wait_for_selector('#library-search')
  page.wait_for_function("document.activeElement.id==='library-search'")
  field=page.locator('#library-search');field.fill('gsblur')
  assert 'Gaussian Blur' in page.locator('.result strong').first.inner_text()
  assert page.locator('.result strong mark').count()>=6
  page.keyboard.press('ArrowDown');assert page.locator('.result').first.evaluate('(x)=>x===document.activeElement')
  page.keyboard.press('ArrowDown');assert page.locator('.result').nth(1).evaluate('(x)=>x===document.activeElement')
  page.keyboard.press('Escape');assert field.evaluate('(x)=>x===document.activeElement')
  page.locator('#app-filter').select_option('photoshop');page.locator('#app-filter').focus();page.keyboard.press('Escape');assert page.locator('#app-filter').evaluate('(x)=>x===document.activeElement');field.focus();page.keyboard.press('Enter')
  page.wait_for_url('**#read/photoshop/ref/filters/filter-gaussian-blur')
  page.wait_for_selector('iframe[data-app="photoshop"]')
  frame=page.frame(url=lambda u:'/manuals/photoshop/' in u);frame.wait_for_selector('#main h1')
  frame.locator('#main').focus();frame.locator('#main').press('Control+k');page.wait_for_selector('#library-search')
  page.wait_for_function("document.activeElement.id==='library-search'")
  field=page.locator('#library-search');field.fill('gausian blur');assert page.locator('.result').count()
  field.fill('zzqqxxvvzzqqxxvv');assert page.locator('.result').count()==0
  page.keyboard.press('ArrowDown');page.keyboard.press('Enter');assert '#search' in page.url
  page.keyboard.press('Escape');assert field.input_value()==''
  page.locator('#app-filter').select_option('');field.fill('mask')
  if page.locator('[data-action="more-search"]').count():
   n=page.locator('.result').count();page.locator('[data-action="more-search"]').click();assert page.locator('.result').count()>n;assert page.locator('.result').nth(n).evaluate('(x)=>x===document.activeElement')
  page.locator('#kind-filter').select_option('Field guide');field.fill('1001');assert page.locator('.result').count()>0
  assert page.locator('.result p mark').count()>0
  field.fill('<img src=x onerror=alert(1)>');assert page.locator('#search-results img').count()==0
  field.fill('alpha');page.wait_for_timeout(250);page.reload();page.wait_for_selector('#library-search');assert page.locator('#library-search').input_value()=='alpha'
  for width in [320,375,768]:
   page.set_viewport_size({'width':width,'height':900});page.locator('#kind-filter').select_option('');page.locator('#library-search').fill('gsblur')
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  (ROOT/'test-results').mkdir(exist_ok=True)
  page.screenshot(path=ROOT/'test-results'/f'{name}-fuzzy-search.png',full_page=True)
  delayed=browser.new_context(offline=True)
  delayed.add_init_script("""if(parent===window){let held=false;addEventListener('message',e=>{if(!held&&e.data?.type==='snapshot'&&e.data.app==='photoshop'){held=true;e.stopImmediatePropagation();const data=e.data,source=e.source;setTimeout(()=>dispatchEvent(new MessageEvent('message',{data,source})),1500)}},true)}""")
  dp=delayed.new_page();dp.goto((ROOT/'index.html').as_uri()+'#read/photoshop/progress')
  dp.wait_for_selector('iframe',state='attached');dp.get_by_role('link',name='Progress',exact=True).click()
  dp.locator('[data-library-preference="large"]').check();dp.get_by_role('button',name='Apply to all three',exact=True).click()
  df=dp.frame(url=lambda u:'/manuals/photoshop/' in u)
  try:df.wait_for_function('window.ManualAdapter?.get().largeText===true',polling=50)
  except Exception:
   print('LOADING PREFERENCE FAILURE',name,dp.locator('#notice').inner_text(),df.evaluate('window.ManualAdapter?.get()'),flush=True)
   raise
  delayed.close()
  assert not errors,errors
  assert not remote,remote
  assert not failed,failed
  print('PASS',name,'offline fuzzy ranking, highlights, full text, keyboard, reader shortcut, filters, pagination, URL reload, no matches and 320/375/768 px; zero JS errors or network requests',flush=True)
  browser.close()
