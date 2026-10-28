"""Structural audit for generated Photoshop offline manual. Run from any directory."""
import sys,json,csv,re,collections,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'content/content.json').read_text(encoding='utf-8'))
fail=[]
def check(value,message):
 if not value:fail.append(message)
lessons=D['lessons'];ids={x['id'] for x in lessons};stages=D['stages']
check(len(ids)==len(lessons)==75,'75 unique lesson ids')
check(len(stages)==12,'12 stages')
check([x['id'] for x in lessons]==sorted(ids),'lessons ordered by id')
check(len(D['tools'])>=65,'tool reference count')
check(len(D['filters'])>=70,'filter reference count')
check(len(D['shortcuts'])>=60,'shortcuts count')
check(len(D['glossary'])>=140,'glossary count')
check(len(D['recipes'])>=25,'recipes count')
check(len(D['troubleshooting'])>=25,'troubleshooting count')
check(D['manifest']['photoshop_version']=='27.11','version number')
required=['id','stage','title','objective','prerequisites','concept','location','steps','expected','why','use','mistake','tip','practice','proof','connections','question','answers','correct','explanation','completion']
for x in lessons:
 check(all(x.get(key) not in ('',None,[]) or key in ('prerequisites','connections') for key in required),f'lesson required fields {x["id"]}')
 check(len(x['steps'])>=4,f'walkthrough {x["id"]}')
 check(len(x['answers'])==3 and x['correct'] in (0,1,2),f'quiz {x["id"]}')
 for k in ('prerequisites','connections'):
  check(set(x[k])<=ids,f'cross-reference {x["id"]}.{k}')
 for k in ('previous','next'):
  check(x[k] in ids or x[k] is None,f'nav {x["id"]}.{k}')
 for p in x['prerequisites']:
  check(next(i for i,v in enumerate(lessons) if v['id']==p)<next(i for i,v in enumerate(lessons) if v['id']==x['id']),f'prerequisite order {x["id"]}')
for i,s in enumerate(stages,1):
 check(s['id']==i and s['lessons'],f'stage {i}')
 check(all(next((l for l in lessons if l['id']==id and l['stage']==i),None) for id in s['lessons']),f'stage mapping {i}')
 check(all(s['project'].get(k) for k in ('title','brief','pass')),f'project rubric {i}')
for fam in ('tools','filters','glossary','troubleshooting'):
 for row in D[fam]:check(row['lesson'] in ids,f'{fam} lesson {row.get("title",row.get("term"))}')
for r in D['recipes']:check(all(lid in ids for lid in r['requires']),f'recipe prerequisite {r["title"]}')
for fam in ('tools','filters','glossary','recipes','troubleshooting'):
 arr=D[fam];check(len({r['id'] for r in arr})==len(arr),f'{fam} unique ids')
source=(ROOT/'assets/content.js').read_text(encoding='utf-8');check(source.startswith('"use strict";window.MANUAL_DATA='),'file-local JS bundle exists')
check(json.loads(source.split('=',1)[1].rstrip(' ;\n'))==D,'JS website data matches JSON')
for name,collection in [('TOOLS.csv',D['tools']),('FILTERS.csv',D['filters']),('SHORTCUTS.csv',D['shortcuts']),('GLOSSARY.csv',D['glossary']),('RECIPES.csv',D['recipes']),('TROUBLESHOOTING.csv',D['troubleshooting'])]:
 with (ROOT/'reference'/name).open(encoding='utf-8',newline='') as f:check(len(list(csv.DictReader(f)))==len(collection),f'csv row count {name}')
md=(ROOT/'ALL_CONTENT.md').read_text(encoding='utf-8');check(all(f'## {x["id"]} — {x["title"]}' in md for x in lessons),'Markdown contains all lesson headings')
check(all(r['title'] in md for r in D['tools']),'Markdown contains tool entries')
check(all(r['title'] in md for r in D['filters']),'Markdown contains filter entries')
check(all(r['term'] in md for r in D['glossary']),'Markdown contains glossary')
check(all(r['symptom'] in md for r in D['troubleshooting']),'Markdown contains troubleshooting')
check(all(r['title'] in md for r in D['recipes']),'Markdown contains recipes')
check(all(f'Stage {s["id"]}' in md for s in stages),'Markdown contains projects')
for name in ['index.html','assets/style.css','assets/app.js','assets/content.js','ALL_CONTENT.md','README.md','CURRICULUM.md','SOURCES.md','CHANGELOG.md','AUDIT.md','content/content.json','content/manifest.json']:
 check((ROOT/name).is_file(),f'missing {name}')
for name in ['mask-shapes.png','tone-gradient.png','color-palette.png','retouch-dots.png','perspective-room.png','transparent-sticker.png']:
 check((ROOT/'practice'/name).is_file(),f'missing practice/{name}')
for name in ['diagram-pixels.svg','diagram-mask.svg','diagram-composite.svg']:
 check((ROOT/'assets'/name).is_file(),f'missing diagram {name}')
# Source-side app has no runtime HTTP fetches, CDN links or remote imports.
app=(ROOT/'assets/app.js').read_text(encoding='utf-8');html=(ROOT/'index.html').read_text(encoding='utf-8')
check(not re.search(r'\bfetch\s*\(|\bXMLHttpRequest\s*\(|\bimport\s*\(',app),'App does not use network or dynamic imports')
check(not re.search(r'<(?:script|link)[^>]+(?:src|href)=["\']https?://',html,re.I),'HTML no remote assets')
check('data-action="export"' in app and 'importProgress' in app,'portable progress handlers')
check('state.theme' in app,'theme handler')
if fail:
 print('FAILED ('+str(len(fail))+'):');print('\n'.join('- '+x for x in fail));sys.exit(1)
print('PASS: 75 lessons, 12 stage rubrics, all linked references, quizzes, 6 CSV exports, JSON/JS/Markdown consistency, offline dependencies.')
print('Counts:',', '.join(f'{k}={len(D[k])}' for k in ['lessons','tools','filters','shortcuts','glossary','troubleshooting','recipes']))
