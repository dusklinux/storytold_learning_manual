#!/usr/bin/env python3
"""Compile the offline library from checked-in content; Python 3.15+, stdlib only.
This does not run the historical authoring/enrichment scripts or create archives.
"""
import hashlib
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def plain(value):
    if isinstance(value, dict):
        return ' '.join(plain(v) for k, v in value.items() if k not in {'html', 'sources', 'source', 'ref_tags'})
    if isinstance(value, list):
        return ' '.join(map(plain, value))
    return str(value) if value is not None else ''


def payload_files(base):
    return [p for p in sorted(base.rglob('*')) if p.is_file() and not any(part in {'.git', '__pycache__', '.venv', 'node_modules', 'test-results'} for part in p.relative_to(base).parts) and p.suffix not in {'.pyc', '.zip'} and p != base / 'MANIFEST.sha256' and p.name != '.DS_Store']


def manifest(base):
    (base / 'MANIFEST.sha256').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(base).as_posix()}\n' for p in payload_files(base)), encoding='utf-8')


def main():
    ps = ROOT / 'manuals/photoshop'
    pr = ROOT / 'manuals/premiere'
    ae = ROOT / 'manuals/after-effects'
    photoshop = load(ps / 'content/content.json')
    premiere = load(pr / 'data/course.json')
    after = load(ae / 'manual_data.json')
    guides = load(pr / 'data/guides.json')

    # Keep Photoshop self-contained; images/diagrams stay adjacent for exercises.
    source = '"use strict";window.MANUAL_DATA=' + compact(photoshop) + ';\n'
    (ps / 'assets/content.js').write_text(source, encoding='utf-8')
    template = (ps / 'web/index.template.html').read_text(encoding='utf-8')
    template = template.replace('  <link rel="stylesheet" href="assets/style.css">', '<style>' + (ps / 'assets/style.css').read_text(encoding='utf-8') + '</style>')
    for name in ('content', 'app'):
        template = template.replace(f'  <script defer src="assets/{name}.js"></script>', '')
    template = template.replace('</body>', '<script>' + source + '</script><script>' + (ps / 'assets/app.js').read_text(encoding='utf-8') + '</script><script>' + (ROOT / 'assets/bridge.js').read_text(encoding='utf-8') + '</script>\n</body>')
    (ps / 'index.html').write_text(template, encoding='utf-8')
    # After Effects' original builder remains responsible for its authored outputs.
    import subprocess
    import sys
    subprocess.run([sys.executable, str(ae / 'build.py')], check=True)
    (pr / 'data.js').write_text('window.PREMIERE_MANUAL = ' + compact(premiere) + ';\n', encoding='utf-8')
    (pr / 'guides.js').write_text('window.PREMIERE_GUIDES = ' + compact([{k: v for k, v in g.items() if k != 'markdown'} for g in guides]) + ';\n', encoding='utf-8')

    manuals = [
        dict(id='photoshop', name='Photoshop', mark='Ps', version=photoshop['manifest']['photoshop_version'], lessons=len(photoshop['lessons']), stages=len(photoshop['stages']), home='home', start='lesson/' + photoshop['lessons'][0]['id'], settings='progress', color='#17658b', bg='#e6f3fb', description='Build images with intention. Understand pixels, selections, layers, masks, retouching and production.', highlights=[f"{len(photoshop['tools'])} tools · {len(photoshop['filters'])} filters", f"{len(photoshop['shortcuts'])} Windows shortcuts", '6 original practice images']),
        dict(id='premiere', name='Premiere Pro', mark='Pr', version=premiere['meta']['version'], lessons=len(premiere['lessons']), stages=len(premiere['stages']), home='overview', start='lesson/' + premiere['lessons'][0]['id'], settings='settings', color='#6257a8', bg='#f0edff', description='Shape a story in time. Learn precise editing, audio, color, captions and reliable delivery.', highlights=[f"{len(premiere['effects'])} effects · {len(premiere['transitions'])} transitions", f"{len(premiere['shortcuts'])} Windows shortcuts", f'{len(guides)} technical field guides + sample media']),
        dict(id='after-effects', name='After Effects', mark='Ae', version=after['meta']['applicationVersion'], lessons=len(after['chapters']), stages=len(after['stagePlan']), home='home', start='lesson/' + after['chapters'][0]['id'], settings='settings', color='#7c5297', bg='#f4eaf9', description='Make the invisible mechanics visible. Learn animation, compositing, motion design and rendering.', highlights=[f"{len(after['topics'])} deep topics · {len(after['recipes'])} recipes", f"{len(after['effects'])} effect/control records", f"{len(after['shortcuts'])} Windows shortcuts + practice assets"]),
    ]
    records = []
    keys = []

    def add(app, kind, title, route, record):
        text = re.sub(r'\s+', ' ', plain(record)).strip()
        records.append(dict(app=app, kind=kind, title=title, route=route, body=text))

    for x in photoshop['stages']:
        add('photoshop', 'Stage', x['title'], f"stage/{x['id']}", x)
    for x in photoshop['lessons']:
        add('photoshop', 'Lesson', x['title'], 'lesson/' + x['id'], x)
    for kind in ('tools', 'filters', 'glossary', 'troubleshooting', 'recipes'):
        for x in photoshop[kind]:
            add('photoshop', {'tools':'Tool','filters':'Filter','glossary':'Term','troubleshooting':'Troubleshooting','recipes':'Recipe'}[kind], x.get('title') or x.get('term') or x['symptom'], 'ref/' + kind + '/' + x['id'], x)
    for i, x in enumerate(photoshop['shortcuts']):
        route = f'shortcut/{i}'
        add('photoshop', 'Shortcut', x['action'], route, x)
        keys.append(dict(app='photoshop', key=x['keys'], action=x['action'], context=x['context'] + ' · ' + x['note'], route=route))
    for x in photoshop['changes']:
        add('photoshop', 'Version', x['feature'], 'changes', x)
    for x in premiere['stages']:
        add('premiere', 'Stage', x['title'], f"stage/{x['id']}", x)
    for kind in ('lessons', 'recipes', 'troubleshooting'):
        for x in premiere[kind]:
            route = {'lessons':'lesson','recipes':'recipe','troubleshooting':'trouble'}[kind] + '/' + x['id']
            add('premiere', {'lessons':'Lesson','recipes':'Recipe','troubleshooting':'Troubleshooting'}[kind], x['title'], route, x)
    from urllib.parse import quote
    for kind, fields in {'shortcuts':['command','windows','context'], 'effects':['kind','name'], 'transitions':['category','name'], 'panels':['name'], 'glossary':['term']}.items():
        for x in premiere[kind]:
            token = ' | '.join(x[f] for f in fields)
            route = 'ref/' + kind + '/' + quote(token, safe="~()*!.'-_")
            add('premiere', {'shortcuts':'Shortcut','effects':'Effect','transitions':'Transition','panels':'Panel','glossary':'Term'}[kind], x.get('command') or x.get('name') or x['term'], route, x)
            if kind == 'shortcuts':
                keys.append(dict(app='premiere', key=x['windows'], action=x['command'], context=x['context'] + ' · ' + x['status'], route=route))
    for x in guides:
        add('premiere', 'Field guide', x['title'], 'guide/' + x['id'], x)
    for kind in ('chapters', 'topics', 'recipes', 'effects', 'shortcuts', 'troubleshooting', 'glossary'):
        for x in after[kind]:
            segment = {'chapters':'lesson','topics':'topic','recipes':'recipe','effects':'effects','shortcuts':'shortcuts','troubleshooting':'troubleshoot','glossary':'glossary'}[kind]
            route = segment + '/' + (quote(x['term'], safe="~()*!.'-_") if kind == 'glossary' else x['id'])
            add('after-effects', {'chapters':'Lesson','topics':'Topic','recipes':'Recipe','effects':'Effect','shortcuts':'Shortcut','troubleshooting':'Troubleshooting','glossary':'Term'}[kind], x.get('title') or x.get('name') or x.get('action') or x.get('symptom') or x['term'], route, x)
            if kind == 'shortcuts':
                keys.append(dict(app='after-effects', key=x['key'].replace('`', ''), action=x['action'], context=x['detail'] + ' · ' + x['verification'], route=route))
    add('after-effects', 'Quiz', 'Knowledge checks', 'quiz', after['quiz'])
    (ROOT / 'assets/catalog.js').write_text('window.LIBRARY_MANUALS=' + compact(manuals) + ';\n', encoding='utf-8')
    (ROOT / 'assets/search.js').write_text('window.LIBRARY_SEARCH=' + compact(records) + ';\nwindow.LIBRARY_KEYS=' + compact(keys) + ';\n', encoding='utf-8')
    # Per-manual and top-level manifests are refreshed only after all outputs exist.
    for base in (ps, pr, ae):
        manifest(base)
    manifest(ROOT)
    print(f'Library: {sum(m["lessons"] for m in manuals)} lessons, {len(records)} searchable records, {len(keys)} shortcut records. No archives generated.')


if __name__ == '__main__':
    main()
