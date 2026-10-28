#!/usr/bin/env python3
"""Validate the complete local library without modifying project files. Stdlib only."""
from html.parser import HTMLParser
import hashlib
import csv
import json
from pathlib import Path
import re
import subprocess
import shutil
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import payload_files, catalogs, compact, load

# Reviewed changes are limited to UI integration and removal of archive generation.
EXCEPTIONS = {
    'photoshop': {'MANIFEST.sha256','README.md','assets/app.js','assets/style.css','index.html'},
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
    assert not any(p.suffix=='.zip' for p in payload_files(ROOT,include_archives=True)), 'Nested archive is redundant'
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
    ps=load(ROOT/'manuals/photoshop/content/content.json')
    pr=load(ROOT/'manuals/premiere/data/course.json')
    ae=load(ROOT/'manuals/after-effects/manual_data.json')
    guides=load(ROOT/'manuals/premiere/data/guides.json')
    inline=(ROOT/'manuals/photoshop/index.html').read_text(encoding='utf-8')
    assert 'window.ManualAdapter' in inline and 'dusky-manual-v1' in inline
    for guide in guides:
        assert (ROOT/'manuals/premiere'/guide['filename']).read_text(encoding='utf-8')==guide['markdown']
    manuals,records,keys=catalogs(ps,pr,ae,guides)
    assert (ROOT/'assets/catalog.js').read_text(encoding='utf-8')=='window.LIBRARY_MANUALS='+compact(manuals)+';\n', 'Stale library catalog'
    assert (ROOT/'assets/search.js').read_text(encoding='utf-8')=='window.LIBRARY_SEARCH='+compact(records)+';\nwindow.LIBRARY_KEYS='+compact(keys)+';\n', 'Stale shared search/key index'
    for q in pr['quizzes']:
        assert any(r['app']=='premiere' and r['route']==f"stage/{q['stage']}" and q['question'] in r['body'] for r in records), q['id']
    for stage in ae['stagePlan']:
        assert any(r['app']=='after-effects' and stage['gate'] in r['body'] for r in records), stage['phase']
    for family,name in {'tools':'TOOLS','filters':'FILTERS','shortcuts':'SHORTCUTS','glossary':'GLOSSARY','recipes':'RECIPES','troubleshooting':'TROUBLESHOOTING'}.items():
        with (ROOT/'manuals/photoshop/reference'/f'{name}.csv').open(encoding='utf-8',newline='') as stream:
            reader=csv.DictReader(stream);rows=list(reader)
        expected=[{k:(', '.join(x[k]) if k=='requires' else str(x.get(k,''))) for k in reader.fieldnames} for x in ps[family]]
        assert rows==expected, f'Photoshop CSV content differs: {name}'
    print(f'PASS {len(records)} search records, every Premiere quiz/AE stage challenge, {len(keys)} key contexts and all Photoshop CSV fields')
    for path in [ROOT/'index.html',*(ROOT/'manuals'/app/'index.html' for app in baseline)]:
        parser=Resources();parser.feed(path.read_text(encoding='utf-8'))
        for value in parser.assets:
            url=urlsplit(value)
            assert not url.netloc and url.scheme not in {'http','https'}, f'Remote runtime asset: {value}'
            if not url.scheme:
                assert (path.parent/unquote(url.path)).is_file(), f'Missing local resource: {value}'
    for path in [ROOT/'assets/library.js',ROOT/'assets/bridge.js']:
        source=path.read_text(encoding='utf-8')
        assert not re.search(r'\bfetch\s*\(|XMLHttpRequest|WebSocket|sendBeacon|serviceWorker|\bimport\s*\(',source)
    print('PASS all shipped HTML resources are local and resolve; no runtime network APIs')
    if shutil.which('node'):
        for name in ['library','bridge','catalog','search','matcher','vim']:
            run(['node','--check',str(ROOT/'assets'/f'{name}.js')])
        run(['node','tests/search_logic.cjs'])
    else:
        print('SKIP JavaScript syntax checks: Node.js is an optional development dependency')
    run([sys.executable,'scripts/validate.py'], ROOT/'manuals/photoshop')
    run([sys.executable,'scripts/validate.py'], ROOT/'manuals/premiere')
    run([sys.executable,'validate.py'], ROOT/'manuals/after-effects')
    run([sys.executable,'-m','unittest','discover','-s','tests','-v'], ROOT/'manuals/after-effects')
    run([sys.executable,'-m','unittest','discover','-s','tests','-p','test_build.py','-v'])
    print('PASS library, preserved teaching material and native structural suites')


if __name__=='__main__':
    main()
