"""Final pass regression checks: sequence, instruction-level fixes, version and portability."""
import json
import pathlib
import re
import unittest
from collections import Counter

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'manual_data.json').read_text('utf8'))
PHASES=['START','FOUNDATIONS','INTERMEDIATE','ADVANCED','DELIVERY','CAPSTONE']

class FinalPassChecks(unittest.TestCase):
 def test_strict_increasing_stage_structure(self):
  stages=list(dict.fromkeys(ch['phase'] for ch in DATA['chapters']))
  self.assertEqual(stages,PHASES)
  self.assertEqual([s['phase'] for s in DATA['stagePlan']],PHASES)
  self.assertEqual(Counter(ch['phase'] for ch in DATA['chapters']),Counter({'START':5,'FOUNDATIONS':9,'INTERMEDIATE':14,'ADVANCED':7,'DELIVERY':4,'CAPSTONE':1}))
  self.assertEqual(DATA['chapters'][-1]['id'],'capstone')

 def test_chapter_numbers_and_stage_challenges(self):
  for ix,ch in enumerate(DATA['chapters'],1):
   self.assertTrue(ch['title'].startswith(f'{ix:02} · '),(ix,ch['title']))
  for stage in DATA['stagePlan']:
   for key in ('name','objective','gate','practice'):
    self.assertGreater(len(stage[key]),35 if key!='name' else 5)

 def test_recipe_hill_and_consistent_labels(self):
  levels={'Beginner':0,'Intermediate':1,'Advanced':2}
  prev=0
  for ix,r in enumerate(DATA['recipes'],1):
   self.assertTrue(r['title'].startswith(f'{ix:02} · '))
   self.assertGreaterEqual(r['afterLesson'],prev)
   self.assertIn(r['level'],levels)
   phase=DATA['chapters'][r['afterLesson']-1]['phase']
   self.assertEqual(levels[r['level']],0 if phase in ('START','FOUNDATIONS') else 1 if phase=='INTERMEDIATE' else 2)
   prev=r['afterLesson']
  required={'handwriting':9,'text-window':12,'stagger':16,'glow-outline':19,'rgb-split':24,'capstone':40}
  self.assertTrue(all(next(r['afterLesson'] for r in DATA['recipes'] if r['id']==key)==num for key,num in required.items()))

 def test_corrected_steps(self):
  c={x['id']:x for x in DATA['chapters']}
  self.assertIn('solid layer',c['logic']['experiment'])
  self.assertIn('Next move CTI to 2 seconds',c['timing']['steps'][2])
  self.assertIn('multiple selected layers',c['precomp']['steps'][0])
  self.assertIn('single-layer footage/solid',c['precomp']['steps'][0])
  self.assertIn('first Opacity keyframe',c['keys']['steps'][1])
  self.assertEqual(len(c['precomp']['steps']),6)
  self.assertTrue({'precompose','help'}<=set(c['precomp']['sources']))

 def test_installed_app_not_reader_os(self):
  self.assertEqual(DATA['meta']['platform'],'Windows')
  self.assertEqual(DATA['meta']['readerPlatforms'],['Linux','Windows'])
  html=(ROOT/'index.html').read_text('utf8')
  self.assertIn('stageRoadmap',html)
  self.assertIn('file://',html)
  self.assertNotRegex(html,r'<script\s+[^>]*src=')
  self.assertNotRegex(html,r'<iframe\b')

 def test_verifiable_version_boundary(self):
  self.assertEqual(DATA['meta']['applicationVersion'],'26.5')
  self.assertIn('release-notes',DATA['sources']['release']['url'])
  self.assertIn('Leave all attributes',DATA['sources']['precompose']['note'])
  self.assertFalse(any('Stylize, Time & Transition'==fx['category'] for fx in DATA['effects']))
  self.assertTrue({'Unmult','Curl Noise'}<={fx['name'] for fx in DATA['effects']})

 def test_exported_markdown_roadmap_and_recipe_mapping(self):
  md=(ROOT/'ALL_CONTENT.md').read_text('utf8')
  self.assertIn('Learning ladder and readiness checks',md)
  for s in DATA['stagePlan']: self.assertIn(s['gate'],md)
  for r in DATA['recipes']:self.assertIn(f"Suggested after lesson {r['afterLesson']:02d}",md)

if __name__=='__main__': unittest.main()
