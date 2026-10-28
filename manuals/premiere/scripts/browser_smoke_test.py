#!/usr/bin/env python3
"""Real Chromium DOM-interaction test with inlined *published* local assets.
Requires Playwright and Chromium for testing only, not for using the manual.
Direct file:// navigation is not tested here (blocked by the author's test environment).
Run: python scripts/browser_smoke_test.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,tempfile
P=Path(__file__).resolve().parent.parent
html=(P/'index.html').read_text(encoding='utf-8')
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+ (P/'style.css').read_text(encoding='utf-8')+'</style>')
for f in ('data.js','guides.js','app.js'):
 html=html.replace(f'<script src="{f}"></script>','<script>'+ (P/f).read_text(encoding='utf-8')+'</script>')
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1360,'height':900},accept_downloads=True)
 errors=[]
 page.on('pageerror',lambda err:errors.append(str(err)))
 page.set_content(html,wait_until='load')
 assert 'Premiere, Explained' in page.title()
 # The previous implementation double-rotated choices and made every displayed correct answer last.
 qpositions=page.evaluate("D.quizzes.map(q => quizOrder(q).indexOf(q.answer))")
 assert sorted([qpositions.count(i) for i in range(4)])==[10,10,11,11],qpositions
 assert page.locator('.cardgrid .card').count()>=14
 assert page.locator('#globalCount').inner_text().startswith('0 / 105')
 # Accessibility: escape skip-link hash router and focus the actual main region.
 page.locator('#skipContent').focus()
 page.keyboard.press('Enter')
 assert page.evaluate('document.activeElement.id')=='main'
 assert page.url=='about:blank'
 # Study state and navigation.
 page.evaluate('location.hash="#lesson/L001"')
 assert page.locator('h1').first.inner_text()=='Video editing as decisions'
 page.locator('[data-complete="L001"]').check()
 assert '1 / 105' in page.locator('#globalCount').inner_text()
 page.locator('[data-bookmark="L001"]').first.click()
 assert 'Saved' in page.locator('[data-bookmark="L001"]').first.inner_text()
 page.locator('textarea[data-note="L001"]').fill('Self-testing notes')
 page.evaluate('location.hash="#stage/1"')
 page.locator('[data-quiz="Q001"][data-choice="0"]').click()
 assert 'Correct' in page.locator('.feedback').first.inner_text()
 assert '1 / 3' in page.locator('.quiz-score').inner_text()
 # Search and keyboard focus.
 page.keyboard.press('/')
 assert page.evaluate('document.activeElement.id')=='searchInput'
 page.locator('#searchInput').fill('Lumetri')
 page.wait_for_function("location.hash === '#search'")
 assert page.url.endswith('#search')
 assert page.locator('.search-result').count()>0
 # Theme, progress transfer, import overwrite.
 page.locator('#themeToggle').click()
 assert page.locator('html').get_attribute('data-theme')=='dark'
 with tempfile.TemporaryDirectory() as td:
  with page.expect_download() as pending:
   page.locator('#exportProgress').click()
  dest=Path(td)/'progress.json';pending.value.save_as(str(dest))
  saved=json.loads(dest.read_text(encoding='utf-8'))
  assert saved['complete']['L001']==True
  assert saved['bookmarks']['L001']==True
  assert saved['notes']['L001']=='Self-testing notes'
  assert saved['answers']['Q001']==0
  page.on('dialog',lambda dialog:dialog.accept())
  page.locator('#importProgress').click()
  page.locator('#importFile').set_input_files(str(dest))
  page.wait_for_function("document.getElementById('toast').textContent.includes('imported successfully')")
 # Quick reference filtering and interactive visuals.
 page.evaluate('location.hash="#ref/effects"')
 assert page.locator('.ref-item').count()>=140
 page.locator('#refFilter').fill('Lumetri')
 assert page.locator('.ref-item').count()>=1
 page.evaluate('location.hash="#guides"')
 assert page.locator('.cardgrid .card').count()==13
 page.evaluate('location.hash="#guide/01-EDITING-GEOMETRY"')
 assert 'Editing geometry' in page.locator('.guide-article h1').inner_text()
 page.evaluate('location.hash="#lesson/L022"')
 assert page.locator('[data-diagram]').count()==6
 page.locator('[data-diagram="slip"]').click()
 assert 'Slip' in page.locator('.diagram-note').inner_text()
 # Travel across all 105 lesson routes to catch null/undefined lookup issues.
 lesson_titles=[x['title'] for x in json.loads((P/'data/course.json').read_text(encoding='utf-8'))['lessons']]
 for n in range(1,106):
  page.evaluate(f'location.hash="#lesson/L{n:03d}"')
  page.wait_for_function("wanted => {const x=document.querySelector('h1');return x && x.textContent.trim()===wanted;}",arg=lesson_titles[n-1])
 # Mobile navigation and mobile progress transfer control.
 mobile=browser.new_page(viewport={'width':390,'height':844})
 mobile.on('pageerror',lambda err:errors.append('mobile: '+str(err)))
 mobile.set_content(html,wait_until='load')
 assert mobile.locator('#menuToggle').is_visible()
 mobile.locator('#menuToggle').click()
 assert mobile.locator('#menuToggle').get_attribute('aria-expanded')=='true'
 assert mobile.locator('#exportProgressSide').is_visible()
 assert mobile.locator('#importProgressSide').is_visible()
 assert not errors, '\n'.join(errors)
 print('PASS Chromium inlined-DOM smoke: navigation all 105 lessons; skip focus; quizzes; completion; bookmarks; notes; search; filters; guides; diagrams; theme; JSON export/import; mobile controls; zero JS errors')
 browser.close()
