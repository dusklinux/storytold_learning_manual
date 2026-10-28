#!/usr/bin/env python3
"""Offline project structural and cross-format validation. Python stdlib only.
Call from anywhere: python scripts/validate.py [optional archive.zip].
Does not claim UI click-through or application-side verification.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,csv,re,sys,zipfile,hashlib
ROOT=Path(__file__).resolve().parent.parent
errors=[]; checks=[]
def check(name,ok,detail=''):
 checks.append((name,'PASS' if ok else 'FAIL',detail))
 if not ok:errors.append(name+': '+detail)
required=['index.html','style.css','app.js','data.js','guides.js','data/course.json','data/guides.json','ALL_CONTENT.md','README.md','CURRICULUM.md','SOURCES.md','VERSION_AUDIT.md','BETA_AND_HISTORICAL.md','CHANGELOG.md','AUDIT.md','CAPSTONE.md','SHORTCUTS.csv','EFFECTS.csv','TRANSITIONS.csv','PANELS_AND_TOOLS.csv','GLOSSARY.csv','TROUBLESHOOTING.csv','scripts/build_content.py','scripts/build_guides.py','scripts/build_project_docs.py','scripts/rebuild.py','scripts/validate.py','sample_media/README.md']
check('required project files',all((ROOT/p).is_file() for p in required),', '.join(p for p in required if not (ROOT/p).is_file()))
D=json.loads((ROOT/'data/course.json').read_text(encoding='utf-8'))
G=json.loads((ROOT/'data/guides.json').read_text(encoding='utf-8'))
check('release metadata',D['meta']['version']=='26.5.2' and D['meta']['verified_on']=='2026-10-28')
check('stage quantity',len(D['stages'])==14,str(len(D['stages'])))
check('lesson quantity',len(D['lessons'])==105,str(len(D['lessons'])))
check('quiz quantity',len(D['quizzes'])==42,str(len(D['quizzes'])))
check('guides quantity',len(G)==13,str(len(G)))
check('unique stable identifiers',all(len({x['id'] for x in D[k]})==len(D[k]) for k in ['lessons','quizzes','stages','recipes','troubleshooting','sources']) and len({g['id'] for g in G})==len(G))
lessons={x['id']:x for x in D['lessons']};qs={x['id']:x for x in D['quizzes']};orders={x['id']:i for i,x in enumerate(D['lessons'])};stage_ids={s['id'] for s in D['stages']}
check('stage references',all(x['stage'] in stage_ids for x in D['lessons']) and all(set(s['lessons']).issubset(lessons) and set(s['quiz']).issubset(qs) for s in D['stages']))
check('each lesson exactly one stage',Counter(id for s in D['stages'] for id in s['lessons'])==Counter({id:1 for id in lessons}))
check('lesson prerequisite order and existence',all(p in lessons and orders[p]<orders[x['id']] for x in D['lessons'] for p in x['prerequisites']))
check('lesson links all resolve',all(z in lessons for x in D['lessons'] for z in x['related']))
check('complete lesson learning fields',all(all(x.get(k) for k in ['title','objective','concept','ui','steps','expected','why','use_cases','mistakes','fixes','tip','challenge','mastery']) for x in D['lessons']))
check('stage quiz references',all(q['stage']==s['id'] for s in D['stages'] for id in s['quiz'] for q in [qs[id]]))
check('quizzes answer bounds',all(0<=q['answer']<len(q['options']) and len(q['options'])==4 for q in D['quizzes']))
check('quiz correct answer positions balanced',max(Counter(q['answer'] for q in D['quizzes']).values())<=12)
check('every lesson has enriched explanation and adversarial self-test',all(len(x.get('deep_dive',''))>35 and len(x.get('review_test',''))>65 for x in D['lessons']))
check('optional stage-14 projects have domain prerequisites',all('L096' not in x['prerequisites'] for x in D['lessons'] if 97<=int(x['id'][1:])<=104))
source_ids={s['id'] for s in D['sources']}
check('all effect status classifications nonempty',all(e.get('status') and e.get('source') in source_ids for e in D['effects']))
check('transitions status/source classification',all(e.get('status') and e.get('source') in source_ids for e in D['transitions']))
check('shortcuts status/source classification',all(e.get('status') and e.get('source') in source_ids for e in D['shortcuts']))
check('shortcut value pairs no exact duplicates',len({(x['command'],x['windows'],x['context']) for x in D['shortcuts']})==len(D['shortcuts']))
check('no generic legacy-only effects labeled current',all(x['status'].startswith('Legacy') for x in D['effects'] if x['name'] in ('Crop','Ramp','Camera Blur','Replicate','Edge Feather') and x['kind']=='Video'))
check('recipe and trouble lesson links',all(all(id in lessons for id in r['prerequisites']) for r in D['recipes']) and all(t['lesson'] in lessons for t in D['troubleshooting']))
check('glossary lesson links',all(x['lesson'] in lessons for x in D['glossary']))
source_ids={s['id'] for s in D['sources']}
check('lesson source references',all(all(t in source_ids for t in x['ref_tags']) for x in D['lessons']))
check('sources have URLs and date',all(x['url'].startswith('https://') and x['verified']=='2026-10-28' for x in D['sources']))
check('every guide has local file and HTML',all((ROOT/g['filename']).is_file() and len(g['html'])>100 and len(g['markdown'])>400 for g in G))
check('guide Markdown matches source',all((ROOT/g['filename']).read_text(encoding='utf-8')==g['markdown'] for g in G))
for key,fn in [('shortcuts','SHORTCUTS.csv'),('effects','EFFECTS.csv'),('transitions','TRANSITIONS.csv'),('panels','PANELS_AND_TOOLS.csv'),('glossary','GLOSSARY.csv'),('troubleshooting','TROUBLESHOOTING.csv')]:
 with (ROOT/fn).open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
 check('CSV data match '+fn,rows==[{k:str(d.get(k,'')) for k in rows[0].keys()} for d in D[key]],str(len(rows))+' rows')
 check('CSV quantity '+fn,len(rows)==len(D[key]))
js=(ROOT/'data.js').read_text(encoding='utf-8')
check('JS course data equals JSON',json.loads(js.removeprefix('window.PREMIERE_MANUAL = ').strip().rstrip(';'))==D)
gs=(ROOT/'guides.js').read_text(encoding='utf-8')
jsG=json.loads(gs.removeprefix('window.PREMIERE_GUIDES = ').strip().rstrip(';'))
check('JS guide data equals JSON',all(jsG[i]['html']==G[i]['html'] and jsG[i]['id']==G[i]['id'] for i in range(len(G))))
M=(ROOT/'ALL_CONTENT.md').read_text(encoding='utf-8')
check('Markdown course coverage',all((x['id'] in M and x['title'] in M) for x in D['lessons']))
check('Markdown field guide coverage',all(g['markdown'].strip() in M for g in G))
check('Markdown research coverage','## Official research sources' in M and '## Version feature audit' in M)
html=(ROOT/'index.html').read_text(encoding='utf-8');css=(ROOT/'style.css').read_text(encoding='utf-8');app=(ROOT/'app.js').read_text(encoding='utf-8')
check('all local entrypoint assets',all((ROOT/p).is_file() for p in re.findall(r'(?:src|href)="([\w./-]+\.(?:css|js))"',html)))
check('no CDN or external dynamic requests',not any(re.search(pattern,html+'\n'+css+'\n'+app) for pattern in [r'@import\b',r'\bfetch\s*\(',r'XMLHttpRequest',r'<script[^>]*https?://',r'<link[^>]*https?://',r'new\s+WebSocket\s*\(']))
check('offline entrypoint scripts present',all(f'src="{n}"' in html for n in ['data.js','guides.js','app.js']))
check('progress schema and export/import functions',all(k in app for k in ['premiere-explained-progress-v1','function exportData()','async function importData(','state.complete','state.answers','state.bookmarks','state.notes']))
check('accessible skip control and responsive CSS','id="skipContent"' in html and "$('skipContent').addEventListener('click'" in app and '@media(max-width:880px)' in css)
check('synthetic sample media files',all((ROOT/'sample_media'/n).is_file() and (ROOT/'sample_media'/n).stat().st_size>1000 for n in ['SHOT_A_motion.mp4','SHOT_B_colorbars.mp4','SHOT_C_precision.mp4','AUDIO_A_original_tone.wav','AUDIO_B_original_room_noise.wav']))
# Cross-manual comparative audit extensions: actual entry coverage rather than padded counts.
check('third-pass reference sizes',len(D['glossary'])==107 and len(D['troubleshooting'])==37 and len(D['recipes'])==30)
check('new reference IDs contiguous and unique', [t['id'] for t in D['troubleshooting']]==[f'T{i:03}' for i in range(1,len(D['troubleshooting'])+1)] and [r['id'] for r in D['recipes']]==[f'R{i:03}' for i in range(1,len(D['recipes'])+1)])
check('compound deep-link keys unambiguous',all(len({tuple(str(r.get(k,'')) for k in fields) for r in D[type]})==len(D[type]) for type,fields in {'shortcuts':['command','windows','context'],'effects':['kind','name'],'transitions':['category','name'],'panels':['name'],'glossary':['term']}.items()))
check('all recipes have >=3 actions and existing prerequisites',all(len(r['steps'])>=3 and all(i in lessons for i in r['prerequisites']) for r in D['recipes']))
check('complete Markdown recipes and diagnostics',all(r['title'] in M for r in D['recipes']) and all(t['title'] in M for t in D['troubleshooting']))
check('complete Markdown glossary',all(g['term']+ '**:' in M for g in D['glossary']))
check('settings navigation / controls present', 'href="#settings"' in html and all(w in app and w in css for w in ['large-text','high-contrast','one-step']))
check('strict progress validation supports old exports', 'function normalizeProgress(obj)' in app and all(x in app for x in ['const checkIds=new Set','const quizzes=','Invalid lesson notes','result[k]=obj[k]===true']))
check('precise catalog links and focus',all(x in app for x in ['function refKey(','function refTarget(','function focusRefRecord()','.search-target']))
check('comparison audit and independent library', (ROOT/'COMPARATIVE_AUDIT.md').is_file() and (ROOT/'scripts/third_pass_library.py').is_file() and (ROOT/'scripts/comparative_browser_regression.py').is_file())
if (ROOT/'MANIFEST.sha256').is_file():
 manifest_rows=[line.partition('  ') for line in (ROOT/'MANIFEST.sha256').read_text().splitlines() if line.strip()]
 actual={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and p.name not in {'.DS_Store','MANIFEST.sha256'} and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.suffix!='.zip'}
 check('SHA256 manifest includes all released files and matches', all(sep=='  ' and actual.get(name)==digest for digest,sep,name in manifest_rows) and {row[2] for row in manifest_rows}==set(actual))
if len(sys.argv)>1:
 zpath=Path(sys.argv[1]);check('archive exists',zpath.is_file())
 if zpath.is_file():
  with zipfile.ZipFile(zpath) as z:
   check('ZIP CRC check',z.testzip() is None)
   names=set(z.namelist());check('ZIP required files',all('Premiere_Explained/'+p in names for p in required))
   check('ZIP root HTML matches on disk',z.read('Premiere_Explained/index.html')==(ROOT/'index.html').read_bytes())
print('\n'.join(f'{stat:4}  {name}'+(f' — {detail}' if detail else '') for name,stat,detail in checks))
print(f'\nRESULT: {len(checks)-len(errors)}/{len(checks)} passed; {len(errors)} failed')
sys.exit(1 if errors else 0)
