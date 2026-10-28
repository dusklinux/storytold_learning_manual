#!/usr/bin/env python3
"""Validate the complete local library without modifying project files. Stdlib only."""
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import subprocess
import shutil
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import payload_files

# Reviewed changes are limited to UI integration and removal of archive generation.
EXCEPTIONS = {
    'photoshop': {'MANIFEST.sha256','README.md','assets/app.js','index.html'},
    'premiere': {'MANIFEST.sha256','README.md','app.js','guides.js','index.html'},
    'after-effects': {'MANIFEST.sha256','README.md','build.py','index.html','tests/test_26_5.py','tests/test_second_pass.py','tests/browser_check.py','validate.py','web/app.js'},
}


class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        for field in (['src'] if tag in {'script','img','video','audio','source','iframe'} else ['href'] if tag=='link' else []):
            if attrs.get(field):
                self.assets.append(attrs[field])


def run(command, cwd=ROOT):
    result=subprocess.run(command,cwd=cwd,text=True,capture_output=True)
    if result.returncode:
        print(result.stdout,result.stderr)
        raise AssertionError('Failed: '+' '.join(command))
    lines=result.stdout.strip().splitlines()
    print('PASS', ' '.join(command[1:]), '—', lines[-1] if lines else 'completed')


def main():
    assert not list(ROOT.rglob('*.zip')), 'Nested archive is redundant'
    baseline=json.loads((ROOT/'docs/original-files.json').read_text(encoding='utf-8'))
    unchanged=0
    for app,files in baseline.items():
        for name,digest in files.items():
            path=ROOT/'manuals'/app/name
            assert path.is_file(), f'Lost original file: {app}/{name}'
            if name not in EXCEPTIONS[app]:
                assert hashlib.sha256(path.read_bytes()).hexdigest()==digest, f'Authored material changed: {app}/{name}'
                unchanged+=1
    print(f'PASS {unchanged} original files byte-identical outside explicit integration exceptions')
    for base in [*(ROOT/'manuals'/app for app in baseline), ROOT]:
        expected={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in payload_files(base)}
        entries={}
        for line in (base/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
            digest,name=line.split('  ',1)
            assert name not in entries, 'Duplicate manifest entry'
            entries[name]=digest
        assert entries==expected, f'Manifest mismatch: {base}'
    print('PASS all four manifests match every payload, including unexpected-file checks')
    for app in baseline:
        base=ROOT/'manuals'/app
        if app=='photoshop':
            data=json.loads((base/'content/content.json').read_text(encoding='utf-8'))
            inline=(base/'index.html').read_text(encoding='utf-8')
            assert 'window.ManualAdapter' in inline and 'dusky-manual-v1' in inline
        elif app=='premiere':
            data=json.loads((base/'data/course.json').read_text(encoding='utf-8'))
            for guide in json.loads((base/'data/guides.json').read_text(encoding='utf-8')):
                assert (base/guide['filename']).read_text(encoding='utf-8')==guide['markdown']
        else:
            data=json.loads((base/'manual_data.json').read_text(encoding='utf-8'))
        assert data
    for path in [ROOT/'index.html',*(ROOT/'manuals'/app/'index.html' for app in baseline)]:
        parser=Resources();parser.feed(path.read_text(encoding='utf-8'))
        for value in parser.assets:
            url=urlsplit(value)
            assert url.scheme not in {'http','https','//'}, f'Remote runtime asset: {value}'
            if not url.scheme:
                assert (path.parent/unquote(url.path)).is_file(), f'Missing local resource: {value}'
    for path in [ROOT/'assets/library.js',ROOT/'assets/bridge.js']:
        source=path.read_text(encoding='utf-8')
        assert not re.search(r'\bfetch\s*\(|XMLHttpRequest|WebSocket|sendBeacon|serviceWorker|\bimport\s*\(',source)
    print('PASS all shipped HTML resources are local and resolve; no runtime network APIs')
    if shutil.which('node'):
        for name in ['library','bridge','catalog','search']:
            run(['node','--check',str(ROOT/'assets'/f'{name}.js')])
    else:
        print('SKIP JavaScript syntax checks: Node.js is an optional development dependency')
    run([sys.executable,'scripts/validate.py'], ROOT/'manuals/photoshop')
    run([sys.executable,'scripts/validate.py'], ROOT/'manuals/premiere')
    run([sys.executable,'validate.py'], ROOT/'manuals/after-effects')
    run([sys.executable,'-m','unittest','discover','-s','tests','-v'], ROOT/'manuals/after-effects')
    print('PASS library, preserved teaching material, native structural suites and JavaScript syntax')


if __name__=='__main__':
    main()
