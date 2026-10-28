"""Release conversion, semantic progress preservation and portable rebuild regressions."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import wave
import build

ROOT=Path(__file__).resolve().parents[1]


class EditionTests(unittest.TestCase):
    def test_legacy_lesson_keys_still_represent_original_actions(self):
        legacy=json.loads((ROOT/'tests/legacy_progress.json').read_text(encoding='utf-8'))
        chapters={c['id']:c for c in build.data()['chapters']}
        for key,count in legacy['steps'].items():
            self.assertIn(key,chapters)
            self.assertEqual(len(chapters[key]['steps']),count)
        self.assertEqual(chapters['keys']['steps'][1].count('first Opacity keyframe'),1)
        self.assertIn('stationary matte',next(r for r in build.data()['recipes'] if r['id']=='logo-reveal')['steps'][3])

    def test_modern_workflows_link_to_specific_primary_sources(self):
        data=build.data()
        for key in ('quick-apply','object-matte','responsive-guides','variable-fonts','parametric-meshes','advanced-dof','curl-noise','unmult','beta-watchlist'):
            topic=next(t for t in data['topics'] if t['id']==key)
            self.assertTrue(all(data['sources'][s]['url'].startswith('https://helpx.adobe.com/') for s in topic['sources']))
        self.assertIn('ACES 2.0',str(next(t for t in data['topics'] if t['id']=='ocio')))

    def test_samples_have_known_dimensions_and_data(self):
        self.assertEqual(json.loads((ROOT/'samples/stats.json').read_text(encoding='utf-8')),{'team':'North','score':42})
        with wave.open(str(ROOT/'samples/pulse.wav')) as audio:
            self.assertEqual((audio.getframerate(),audio.getnframes(),audio.getnchannels(),audio.getsampwidth()),(48000,192000,1,2))

    def test_rebuild_preserves_authored_data(self):
        with tempfile.TemporaryDirectory() as temp:
            target=Path(temp)
            result=subprocess.run([sys.executable,str(ROOT/'build.py'),'--output-dir',str(target)],text=True,capture_output=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            for name in ('index.html','manual_data.json','ALL_CONTENT.md','shortcuts.csv','effects.csv'):
                self.assertEqual((target/name).read_bytes(),(ROOT/name).read_bytes(),name)
            self.assertFalse(list(target.glob('*.zip')))


if __name__=='__main__':unittest.main()
