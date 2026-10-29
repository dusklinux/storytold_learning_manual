"""Regression checks for one-pass source freshness and deterministic offline builds."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build import catalogs, load, payload_files


class BuildTests(unittest.TestCase):
    def test_search_contains_previously_missing_teaching(self):
        _,records,keys=catalogs(load(ROOT/'manuals/photoshop/content/content.json'),load(ROOT/'manuals/premiere/data/course.json'),load(ROOT/'manuals/after-effects/manual_data.json'),load(ROOT/'manuals/premiere/data/guides.json'))
        self.assertEqual(len(keys),870)
        for quiz in load(ROOT/'manuals/premiere/data/course.json')['quizzes']:
            self.assertTrue(any(r['app']=='premiere' and quiz['question'] in r['body'] for r in records),quiz['id'])
        for stage in load(ROOT/'manuals/after-effects/manual_data.json')['stagePlan']:
            self.assertTrue(any(r['app']=='after-effects' and stage['gate'] in r['body'] for r in records),stage['phase'])

    def test_payload_prunes_development_trees(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'keep.txt').write_text('keep',encoding='utf-8')
            for name in ['.git','.venv','node_modules','test-results','__pycache__']:
                folder=root/name;folder.mkdir();(folder/'ignored.zip').write_bytes(b'ignored')
            (root/'directory-link').symlink_to(root/'.venv',target_is_directory=True)
            self.assertEqual([p.name for p in payload_files(root,include_archives=True)],['keep.txt'])

    def test_single_build_uses_new_after_effects_source(self):
        with tempfile.TemporaryDirectory(prefix='Adobe build regression ') as temporary:
            root=Path(temporary)/'manual'
            shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__','.venv','node_modules','test-results'))
            content=root/'manuals/after-effects/content.py'
            original=content.read_text(encoding='utf-8')
            phrase='SECOND_PASS_SOURCE_FRESHNESS'
            self.assertIn('Use the specified 26.5 stable build',original)
            content.write_text(original.replace('Use the specified 26.5 stable build',phrase+' Use the specified 26.5 stable build',1),encoding='utf-8')
            result=subprocess.run([sys.executable,str(root/'scripts/build.py')],capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            for name in ['manuals/after-effects/manual_data.json','manuals/after-effects/index.html','assets/search.js']:
                self.assertIn(phrase,(root/name).read_text(encoding='utf-8'),name)
            before={p.relative_to(root):hashlib.sha256(p.read_bytes()).hexdigest() for p in payload_files(root)}
            result=subprocess.run([sys.executable,str(root/'scripts/build.py')],capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            after={p.relative_to(root):hashlib.sha256(p.read_bytes()).hexdigest() for p in payload_files(root)}
            self.assertEqual(before,after)
            self.assertFalse(list(root.rglob('*.zip')))


if __name__=='__main__':
    unittest.main()
