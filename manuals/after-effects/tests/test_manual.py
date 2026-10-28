"""Structural test suite. Run: python -m unittest discover -s tests -v"""
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import build
import validate


class ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = build.data()

    def test_schema_and_content_thresholds(self):
        self.assertTrue(build.validate(self.d))

    def test_windows_only(self):
        self.assertEqual(self.d['meta']['platform'], 'Windows')
        self.assertEqual(self.d['meta']['applicationVersion'], '26.5')
        for x in self.d['shortcuts']:
            self.assertNotIn('macos', x['key'].lower())
            self.assertNotIn('⌘', x['key'])

    def test_26_5_feature_boundary(self):
        names={x['name'] for x in self.d['effects']}
        self.assertTrue({'Unmult','Curl Noise','Compressor','Gate','Distortion'}<=names)
        self.assertFalse({'Contour Paint','De-esser'}&names)

    def test_lessons_have_measurable_outcomes(self):
        for x in self.d['chapters']:
            with self.subTest(x['id']):
                self.assertGreaterEqual(len(x['steps']),5)
                self.assertGreaterEqual(len(x['checks']),2)
                self.assertGreater(len(x['experiment']),20)
                self.assertGreater(len(x['why']),20)
                self.assertTrue(x['topics'])

    def test_topic_and_recipe_links(self):
        topics = {x['id'] for x in self.d['topics']}
        for x in self.d['chapters']:
            self.assertTrue(set(x['topics']) <= topics, x['id'])
        for x in self.d['topics']:
            self.assertGreaterEqual(len(x['sections']),3)
            self.assertTrue(set(x['related']) <= topics, x['id'])
        for x in self.d['recipes']:
            self.assertGreaterEqual(len(x['steps']),5)
            self.assertTrue(x['verify'])
            self.assertTrue(x['fail'])

    def test_unique_ids(self):
        for kind in ('chapters', 'topics', 'recipes', 'effects', 'shortcuts', 'troubleshooting', 'quiz'):
            ids=[x['id'] for x in self.d[kind]]
            self.assertEqual(len(ids),len(set(ids)),kind)

    def test_source_links_are_declared(self):
        for kind in ('chapters','topics','recipes'):
            for x in self.d[kind]:
                self.assertTrue(set(x['sources']) <= set(self.d['sources']), (kind,x['id']))

    def test_html_and_exports(self):
        result=validate.verify()
        self.assertEqual(len(result['chapters']),len(self.d['chapters']))

    def test_reference_contains_3d_render_color_expressions(self):
        haystack=' '.join(x['title'] for x in self.d['topics']).lower()
        for substring in ['expression','3d','color','render','shape','mask','tracking','typography','motion']:
            self.assertIn(substring,haystack)


if __name__=='__main__':unittest.main()
