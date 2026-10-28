"""Shortcut recall mode preserves original answers and contextual meanings."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 for name in ['chromium','firefox']:
  b=getattr(pw,name).launch(headless=True,**({'executable_path':shutil.which('chromium')} if name=='chromium' else {}));c=b.new_context(offline=True);p=c.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
  p.goto((ROOT/'index.html').as_uri()+'#compare');p.wait_for_selector('.key-group');assert not p.locator('.key-test').count()
  p.select_option('#key-mode','test');assert p.locator('.key-test').count()>0;assert not p.locator('[data-test-answer]:visible').count()
  p.keyboard.press('Alt+m');p.keyboard.press('l');assert p.locator('[data-test-answer]:visible').count()==1
  p.keyboard.press('j');assert p.locator('.key-test').nth(1).evaluate('x=>x===document.activeElement');p.keyboard.press('l');assert p.locator('[data-test-answer]:visible').count()==2
  p.keyboard.press('h');assert p.locator('[data-test-answer]:visible').count()==1
  p.keyboard.press('G');assert p.locator('.key-test').last.evaluate('x=>x===document.activeElement')
  p.keyboard.press('g');assert p.locator('.key-test').first.evaluate('x=>x===document.activeElement')
  p.locator('[data-action="reveal-all-keys"]').click();assert p.locator('[data-test-answer]:visible').count()==p.evaluate('window.LIBRARY_KEYS.length')
  # Exact original context and action for every card, including duplicate bindings.
  actual=p.locator('.key-test').evaluate_all("cards=>cards.map(c=>[c.querySelector('kbd').textContent,c.querySelector('[data-test-answer] a').textContent,c.querySelector('[data-test-answer] small').textContent])")
  expected=p.evaluate('window.LIBRARY_KEYS.map(x=>[x.key,x.action,x.context])');assert sorted(actual)==sorted(expected)
  p.locator('[data-action="hide-all-keys"]').click();assert not p.locator('[data-test-answer]:visible').count()
  p.select_option('#key-app','photoshop');assert all('Photoshop' in x for x in p.locator('.key-test h2').all_text_contents())
  p.locator('#compare-search').fill('Ctrl');assert not p.locator('[data-test-answer]:visible').count()
  p.locator('#compare-search').press_sequentially('jkl');assert p.locator('#compare-search').input_value()=='Ctrljkl'
  p.locator('#compare-search').fill('');p.locator('.key-test').first.focus();p.keyboard.press('Alt+m');p.keyboard.press('ArrowDown');p.keyboard.press('Enter');assert p.locator('.key-test').nth(1).locator('[data-test-answer]').is_visible()
  p.select_option('#key-mode','reference');assert p.locator('.key-record').count()>0;assert not p.locator('.key-test').count()
  for width in [320,768]:p.set_viewport_size({'width':width,'height':800});assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
  assert not errors,errors
  print('PASS',name,'recall and reference modes, j/k/h/l/g/G, arrow/Enter, all 680 original answers, reveal/hide all, app/text filters and mobile',flush=True);b.close()
