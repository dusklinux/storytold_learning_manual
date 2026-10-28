#!/usr/bin/env python3
"""Deterministic, dependency-free builder for the AE 26.5 Windows offline field manual."""
import argparse,csv,io,json,pathlib
import content
ROOT=pathlib.Path(__file__).resolve().parent
EDITION=2
VERSION='26.5'


def read_json(path):return json.loads(path.read_text(encoding='utf-8'))
def data():
 shortcuts=read_json(ROOT/'data/shortcuts_seed.json')
 effects=read_json(ROOT/'data/effects_seed.json')
 problems=read_json(ROOT/'data/troubleshooting_seed.json')
 start=len(problems)
 problems.extend({'id':f'trouble-{i+start+1:03}','symptom':s,'checks':c,'fix':f} for i,(s,c,f) in enumerate(content.ADDITIONAL_TROUBLE))
 glossary=read_json(ROOT/'data/glossary_seed.json')
 for line in content.ADDITIONAL_GLOSSARY.strip().splitlines():
  if ' :: ' in line:
   t,defn=line.split(' :: ',1)
   if t.lower() not in {x['term'].lower() for x in glossary}:glossary.append({'term':t,'definition':defn})
 glossary.sort(key=lambda x:x['term'].lower())
 quiz=[{'id':f'q-{i+1:03}','question':q,'options':opts,'correct':a,'explanation':why} for i,(q,opts,a,why) in enumerate(content.QUIZ)]
 return {'meta':{'name':'After Effects 26.5 — Windows Complete Learning Manual', 'application':'Adobe After Effects','applicationVersion':'26.5','platform':'Windows','readerPlatforms':['Linux','Windows'],'keyboard':'Default English layout','manualEdition':EDITION,'released':'2026-09','guideResearchCutoff':'2026-10-28','offline':True,'provenance':'Adobe 26.5 release notes, current requirements, feature-specific Adobe documentation and user-supplied topic inventory'},
  'stagePlan':content.STAGE_PLAN,'chapters':content.CHAPTERS,'topics':content.TOPICS,'recipes':content.RECIPES,'effects':effects,'shortcuts':shortcuts,'troubleshooting':problems,'glossary':glossary,'quiz':quiz,'sources':content.SOURCES}


def validate(d):
 assert d['meta']['applicationVersion']=='26.5'
 for plural,key in [('chapters','id'),('topics','id'),('recipes','id'),('effects','id'),('shortcuts','id'),('troubleshooting','id'),('quiz','id')]:
  seq=d[plural];assert len(seq)==len(set(str(v[key]) for v in seq)),f'duplicate IDs in {plural}'
 topicset={x['id'] for x in d['topics']}
 for ch in d['chapters']:
  assert len(ch['steps'])>=5, f"Lesson must have actionable content: {ch['id']}"
  assert len(ch['checks'])>=2 and ch['experiment']
  assert all(k in topicset for k in ch['topics']), ('Missing topics',ch['id'],set(ch['topics'])-topicset)
  assert all(k in d['sources'] for k in ch['sources'])
 assert [v['phase'] for v in d['stagePlan']]==list(dict.fromkeys(c['phase'] for c in d['chapters']))
 assert all(1<=r['afterLesson']<=len(d['chapters']) for r in d['recipes'])
 assert all(a['afterLesson']<=b['afterLesson'] for a,b in zip(d['recipes'],d['recipes'][1:]))
 for t in d['topics']:
  assert len(t['sections'])>=3 and len(t['experiment'])>=30,('Shallow topic',t['id'])
  assert all(k in topicset for k in t['related']),('Missing topic relation',t['id'],set(t['related'])-topicset)
  assert all(k in d['sources'] for k in t['sources'])
 for r in d['recipes']:
  assert len(r['steps'])>=5 and r['verify'] and r['fail']
  assert all(k in d['sources'] for k in r['sources'])
 for x in d['quiz']:assert len(x['options'])==4 and 0<=x['correct']<4
 names={x['name'].casefold() for x in d['effects']}
 assert {'unmult','curl noise','compressor','gate','distortion'}<=names
 assert not {'contour paint','de-esser'}&names, 'Beta-only effects in stable directory'
 for kind in ('effects','shortcuts'):
  assert all(x['source'] in d['sources'] for x in d[kind]), ('Missing reference source',kind)
 assert not any('macos' in x['key'].lower() for x in d['shortcuts'])
 assert len(d['chapters'])>=30 and len(d['topics'])>=70 and len(d['effects'])>=200
 assert len(d['shortcuts'])>=300 and len(d['recipes'])>=25
 return True


def source_markdown(d, ids):
 return ', '.join(f"[{d['sources'][k]['title']}]({d['sources'][k]['url']})" if d['sources'][k]['url'] else d['sources'][k]['title'] for k in ids)


def md(s):return str(s).replace('\r',' ').strip()
def markdown(d):
 out=[f"# {d['meta']['name']}",
  '', '**Application lessons:** After Effects **26.5 on Windows only**, default English keyboard. **Reading:** open the offline HTML or Markdown on Linux or Windows; export/import browser progress to move between systems.',
  '', '> Version accuracy: This edition teaches stable 26.5, including the modern 26.0–26.5 tools. Features labeled Beta remain separate. Current Adobe Help pages can mix both. No claim is made that this package reproduces every parameter of every native, bundled or third-party effect.',
  '', '## Table of contents','',
  '- [Step-by-step curriculum](#step-by-step-curriculum)','- [Deep topic reference](#deep-topic-reference)','- [Practical recipes](#practical-recipes)','- [Effects encyclopedia](#effects-encyclopedia)','- [Windows shortcuts](#windows-shortcuts)','- [Troubleshooting](#troubleshooting)','- [Glossary](#glossary)','- [Sources and version restrictions](#sources-and-version-restrictions)','',
  '', '---','', '## Learning ladder and readiness checks',''] + [f"### {stage['phase']} — {stage['name']}\n\n**Learn:** {stage['objective']}\n\n**Before moving on:** {stage['gate']}\n\n**Practice:** {stage['practice']}\n" for stage in d['stagePlan']] + ['','---','', '## Lesson index',''] + [f"{i}. [{ch['title']}](#lesson-{ch['id']})" for i,ch in enumerate(d['chapters'],1)] + ['', '## Step-by-step curriculum','']
 for i,ch in enumerate(d['chapters'],1):
  out += [f"<a id=\"lesson-{ch['id']}\"></a>",f"### {md(ch['title'])}",'',f"**Stage:** {ch['phase']}",f"**Why:** {ch['why']}",'']
  out += [f'{j}. {md(step)}' for j,step in enumerate(ch['steps'],1)]
  out += ['','**Do it yourself:** '+ch['experiment'],'', '**Self-check:**']+[f'- [ ] {v}' for v in ch['checks']]
  if ch['pitfalls']:out += ['','**Common mistakes:**']+[f'- {v}' for v in ch['pitfalls']]
  out += ['','**Related deep dives:** '+', '.join(f"[{next(t['title'] for t in d['topics'] if t['id']==k)}](#topic-{k})" for k in ch['topics']),'','**Sources:** '+source_markdown(d,ch['sources']),'']
 out+=['---','','## Deep topic index',''] + [f"- [{t['title']}](#topic-{t['id']})" for t in d['topics']] + ['', '## Deep topic reference','']
 for t in d['topics']:
  out += [f"<a id=\"topic-{t['id']}\"></a>",f"### {t['title']}",'',f"*{t['category']}* — {t['summary']}",'']
  for sec in t['sections']:out += [f"**{sec['title']}**",'',sec['text'],'']
  out += ['**Experiment:** '+t['experiment'],'']
  if t['pitfalls']:out += ['**Pitfalls:** '+'; '.join(t['pitfalls']),'']
  out += ['**Related topics:** '+', '.join(f"[{next(x['title'] for x in d['topics'] if x['id']==k)}](#topic-{k})" for k in t['related']),'','**Sources:** '+source_markdown(d,t['sources']),'']
 out+=['---','','## Practical recipes','']
 for r in d['recipes']:
  out += [f"### {r['title']}",'',f"**{r['category']} · {r['level']} · Suggested after lesson {r['afterLesson']:02d}** — {r['goal']}",'']
  out += [f"{j}. {step}" for j,step in enumerate(r['steps'],1)]
  out += ['',f"**Verify:** {r['verify']}",f"**If it fails:** {r['fail']}",'','**Sources:** '+source_markdown(d,r['sources']),'']
 out+=['---','','## Effects encyclopedia','',
  'Orientation directory of effects and expression controls, including compatibility-only effects. Exact installation and effect parameters must be checked in AE 26.5. Adobe’s online catalog is continually updated and can also describe Beta functionality; entries labeled obsolete should not be the default for new designs.','',
  '| Effect | Category | Purpose |','|---|---|---|']
 for fx in d['effects']:out.append('| '+ ' | '.join(md(fx.get(k,'')).replace('|','\\|') for k in ['name','category','summary'])+' |')
 out+=['','---','','## Windows shortcuts','',
 'These are task-oriented Windows shortcuts, gestures and contextual actions. They can be remapped; panel focus matters. Confirm with Edit → Keyboard Shortcuts (`Ctrl+Alt+\'`).','',
 '| Task | Windows binding / gesture | Context and note |','|---|---|---|']
 for k in d['shortcuts']:out.append('| '+' | '.join(md(k.get(x,'')).replace('|','\\|') for x in ['action','key','detail'])+' |')
 out+=['','---','','## Troubleshooting','', '| Symptom | Inspect | Corrective action |','|---|---|---|']
 for t in d['troubleshooting']:out.append('| '+' | '.join(md(t.get(x,'')).replace('|','\\|') for x in ['symptom','checks','fix'])+' |')
 out+=['','---','','## Glossary','', '| Term | Definition |','|---|---|']
 for t in d['glossary']:out.append('| '+' | '.join(md(t.get(x,'')).replace('|','\\|') for x in ['term','definition'])+' |')
 out+=['','---','','## Sources and version restrictions','',
 'Adobe documentation is rolling; release notes, feature-specific pages and feature history establish the stable 26.5 boundary. The guide includes original explanatory content; no Adobe images, proprietary plugin binaries or training videos are bundled.','']
 for k,s in d['sources'].items():out.append(f"- **{s['title']}** — {s['url'] or '(user supplied document)'} — {s['note']}")
 out+=['','### Stable 26.5 and Beta boundary','',
 'Stable workflows include Quick Apply, Object Matte with disk caching, parametric meshes, Substance materials, variable-font axes, SVG import/paste, Unmult, Curl Noise, Compressor/Gate/Distortion, Advanced 3D DOF, effect labels, responsive guides and bundled ACES 2.0.',
 '', 'Beta watchlist at the research cutoff: Contour Paint, De-esser, AI Assistant, layers as material sources, materials on 3D text/shapes, editable Illustrator text, Quick Set Anchor, generalized viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save.',
 '', '**Limits:** The reader is browser-tested separately from the product instructions. No licensed Windows AE 26.5 installation was available to execute every lesson or verify every installed plug-in parameter. External fonts, codecs, materials and hardware can change results; verify final deliverables.','']
 return '\n'.join(out)


def csv_text(entries,fields):
 buffer=io.StringIO(newline='');w=csv.DictWriter(buffer,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(entries);return buffer.getvalue()


def build(outdir):
 outdir.mkdir(parents=True,exist_ok=True);d=data();validate(d)
 payload=json.dumps(d,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
 template=(ROOT/'web/template.html').read_text(encoding='utf-8')
 css=(ROOT/'web/styles.css').read_text(encoding='utf-8');js=(ROOT/'web/app.js').read_text(encoding='utf-8')
 html=template.replace('__CSS__',css).replace('__DATA__',payload).replace('__JS__',js)
 html=html.replace('</body>','<script>'+ (ROOT/'../../assets/vim.js').read_text(encoding='utf-8')+'</script><script>'+(ROOT/'../../assets/reading.js').read_text(encoding='utf-8')+'</script><script>'+(ROOT/'../../assets/shortcut-study.js').read_text(encoding='utf-8')+'</script><script>'+ (ROOT/'../../assets/bridge.js').read_text(encoding='utf-8')+'</script></body>')
 import sys
 sys.path.insert(0,str(ROOT/'../../scripts'))
 from palettes import reader_head
 html=html.replace('</head>',reader_head('after-effects')+'</head>')
 (outdir/'index.html').write_text(html,encoding='utf-8')
 (outdir/'manual_data.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (outdir/'ALL_CONTENT.md').write_text(markdown(d),encoding='utf-8')
 (outdir/'shortcuts.csv').write_text(csv_text(d['shortcuts'],['id','category','action','key','detail','source','verification']),encoding='utf-8')
 (outdir/'effects.csv').write_text(csv_text(d['effects'],['id','name','category','summary','version','source']),encoding='utf-8')
 print(f"Built {outdir/'index.html'} ({(outdir/'index.html').stat().st_size:,} bytes)")
 print('Counts:',{k:len(d[k]) for k in ['chapters','topics','recipes','effects','shortcuts','troubleshooting','glossary','quiz']})
 return d

if __name__=='__main__':
 parser=argparse.ArgumentParser(description='Rebuild After Effects 26.5 Windows offline manual (Python stdlib only).')
 parser.add_argument('--output-dir',type=pathlib.Path,default=ROOT,help='Where to write generated deliverables (defaults to project directory).')
 args=parser.parse_args();build(args.output_dir.resolve())
