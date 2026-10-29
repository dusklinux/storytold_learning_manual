#!/usr/bin/env python3
"""Validate exported offline manual in-place; no dependencies."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from html.parser import HTMLParser

import build

ROOT = Path(__file__).resolve().parent


class EmbeddedDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.gather = False
        self.embedded = []
        self.script_types = []
        self.external_assets = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'script':
            self.script_types.append(a.get('type', 'inline'))
            self.gather = a.get('id') == 'guideData'
            if a.get('src'): self.external_assets.append(a['src'])
        if tag == 'link' and a.get('rel') in ('stylesheet', 'preload') and a.get('href'):
            self.external_assets.append(a['href'])
        if tag in ('iframe', 'img', 'video', 'audio', 'source') and a.get('src'):
            self.external_assets.append(a['src'])

    def handle_data(self, value):
        if self.gather:
            self.embedded.append(value)

    def handle_endtag(self, tag):
        if tag == 'script': self.gather = False


def verify(root=ROOT):
    written = json.loads((root / 'manual_data.json').read_text(encoding='utf8'))
    build.validate(written)
    expected = build.data()
    assert written == expected, 'Generated JSON does not match current authored data; run build.py'

    html = (root / 'index.html').read_text(encoding='utf8')
    parser = EmbeddedDataParser()
    parser.feed(html)
    assert not parser.external_assets, 'HTML contains an external resource request'
    assert parser.script_types.count('application/json') == 1
    assert json.loads(''.join(parser.embedded)) == written, 'Embedded data differs from JSON export'
    assert '<style>' in html and '</style>' in html, 'CSS not embedded'
    assert 'function render(' in html and 'function searchPage(' in html, 'App script missing'
    assert 'http-equiv="refresh"' not in html
    assert not re.search(r'<\s*(?:script|link)[^>]+\b(?:src|href)\s*=\s*[\'\"]https?://', html, re.I)
    assert '__CSS__' not in html and '__JS__' not in html and '__DATA__' not in html

    manual = (root / 'ALL_CONTENT.md').read_text(encoding='utf8')
    assert manual.startswith('# After Effects 26.5')
    for chapter in written['chapters']:
        assert chapter['title'] in manual
    assert '## Effects encyclopedia' in manual
    assert '## Windows shortcuts' in manual
    assert '### Stable 26.5 and Beta boundary' in manual

    for filename, entity_type in [('shortcuts.csv', 'shortcuts'), ('effects.csv', 'effects')]:
        with (root / filename).open(encoding='utf8', newline='') as f:
            rows = list(csv.DictReader(f))
            assert len(rows) == len(written[entity_type]), (filename, len(rows), len(written[entity_type]))
            assert [x['id'] for x in rows] == [x['id'] for x in written[entity_type]]

    # Verify the portable SHA-256 manifest against the files in the current build.
    manifest=(root/'MANIFEST.sha256').read_text(encoding='utf8').splitlines()
    assert len(manifest)>15 and len(manifest)==len(set(manifest))
    for line in manifest:
        digest, name = line.split('  ',1)
        assert len(digest)==64 and (root/name).is_file(), name
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest, name

    return written


if __name__ == '__main__':
    try:
        found = verify()
    except Exception as exc:
        print('FAILED:', repr(exc), file=sys.stderr)
        sys.exit(1)
    print('VALIDATED: After Effects 26.5 & EffectCraft offline manual')
    print('Content:', ', '.join(f'{k}={len(found[k])}' for k in ('chapters','topics','recipes','effects','shortcuts','troubleshooting','glossary','quiz')))
    print('Offline HTML, JSON, CSVs, Markdown contents are consistent.')
