"""Independently check source outputs, curriculum graph, technical regressions and ZIP safety.
Does not replace hands-on verification against installed Adobe Photoshop.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,csv,re,hashlib,zipfile,sys,html.parser
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'content/content.json').read_text())
results=[]
def audit(label,yes,details=''):
 results.append((label,bool(yes),str(details)))
 print(('PASS' if yes else 'FAIL'),label,details)

lessons=D['lessons'];ids=[l['id'] for l in lessons];position={x:i for i,x in enumerate(ids)}
audit('lesson identifiers unique',len(set(ids))==75,len(ids))
audit('stage assignments contiguous',sorted(Counter(l['stage'] for l in lessons).keys())==list(range(1,13)))
audit('stage content/IDs match exactly', all(set(s['lessons'])=={x['id'] for x in lessons if x['stage']==s['id']} for s in D['stages']))
audit('bidirectional previous/next',all(l['previous']==(ids[i-1] if i else None) and l['next']==(ids[i+1] if i<len(ids)-1 else None) for i,l in enumerate(lessons)))
audit('all pedagogical dependencies earlier',all(p in position and position[p]<position[l['id']] for l in lessons for p in l['prerequisites']))
audit('cross-stage dependencies present',sum(any(next(y['stage'] for y in lessons if y['id']==p)<l['stage'] for p in l['prerequisites']) for l in lessons)>=11)
audit('lesson walkthroughs substantive',all(len(l['steps'])>=4 and len(l['concept'])>=90 and len(l['why'])>=40 and len(l['practice'])>=35 and len(l['proof'])>=30 for l in lessons))
audit('lesson exams unique prompts',len({l['question'].lower() for l in lessons})==len(lessons))
audit('no quiz uses duplicate options',all(len(set(a.lower() for a in l['answers']))==3 for l in lessons))
audit('lesson objectives/practice/criteria nonempty',all(l['objective'] and l['practice'] and l['proof'] and l['tip'] and l['mistake'] and l['use'] for l in lessons))
audit('stage projects all independent',len({s['project']['title'] for s in D['stages']})==12)
for cat in ('tools','filters','glossary','recipes','troubleshooting'):
 arr=D[cat];audit(cat+' IDs unique',len({x['id'] for x in arr})==len(arr),len(arr))
 audit(cat+' references valid',all(all(t in position for t in (r['requires'] if cat=='recipes' else [r['lesson']])) for r in arr))
 audit(cat+' labels not duplicated',len({x.get('title',x.get('term',x.get('symptom',''))).lower() for x in arr})==len(arr))
audit('all tools have specific toolbar group location',all(x['location'].startswith('Toolbar > ') and 'tool group' in x['location'] and len(x['location'])>50 for x in D['tools']))
audit('filters without generic locations',not any('inspect the live menu' in x['location'] for x in D['filters']),sum('inspect the live menu' in x['location'] for x in D['filters']))
audit('no old R assigned to retouch tools',not any(x['shortcut']=='R' for x in D['tools'] if x['title'] in ('Blur','Smudge','Sharpen')))
audit('no old K assigned to retouch tools',not any(x['shortcut']=='K' for x in D['tools'] if x['title'] in ('Blur','Smudge','Sharpen')))
audit('Frame retains K; Rotate View R',next(x['shortcut'] for x in D['tools'] if x['title']=='Frame')=='K' and next(x['shortcut'] for x in D['tools'] if x['title']=='Rotate View')=='R')
audit('Quick Mask location corrected','Select > Edit in Quick Mask Mode' not in D['lessons'][next(i for i,l in enumerate(lessons) if l['id']=='s03l05')]['location'])
audit('Shake Reduction marked removed in 23.3',all('REMOVED' in x['location'] and '23.3' in x['status'] for x in D['filters'] if x['title']=='Shake Reduction'))
audit('Adobe partner AI filter paths conditional',all(x['location'].startswith('Filter > AI ') and 'credits' in x['location'] for x in D['filters'] if x['title'] in ('AI Sharpen (Topaz)','AI Denoise (Topaz)')))
audit('Perspective Warp correctly under Edit',next(x['location'] for x in D['filters'] if x['title']=='Perspective Warp')=='Edit > Perspective Warp')
audit('no obsolete F shortcut duplicate',not any(x['action']=='Full screen menus varies' for x in D['shortcuts']))
audit('shortcut action and context nonempty',all(x['keys'] and x['action'] and x['context'] and x['note'] for x in D['shortcuts']),len(D['shortcuts']))
audit('Windows-only keyboard directions',not any('command+' in x['keys'].lower() or 'option+' in x['keys'].lower() for x in D['shortcuts']))
filelist=['index.html','assets/content.js','assets/app.js','assets/style.css','ALL_CONTENT.md','CURRICULUM.md','README.md','SOURCES.md','CHANGELOG.md','AUDIT.md','AUDIT_SECOND_PASS.md','content/content.json','content/manifest.json','reference/TOOLS.csv','reference/FILTERS.csv','reference/SHORTCUTS.csv','reference/GLOSSARY.csv','reference/RECIPES.csv','reference/TROUBLESHOOTING.csv']
audit('required project files present',all((ROOT/x).exists() for x in filelist))
js=(ROOT/'assets/content.js').read_text();audit('website bundled JSON exactly matches source',json.loads(js.split('=',1)[1].rstrip(' ;\n'))==D)
audit('manifest equals embedded manifest',json.loads((ROOT/'content/manifest.json').read_text())==D['manifest'])
for cat,filename in [('tools','TOOLS.csv'),('filters','FILTERS.csv'),('shortcuts','SHORTCUTS.csv'),('glossary','GLOSSARY.csv'),('recipes','RECIPES.csv'),('troubleshooting','TROUBLESHOOTING.csv')]:
 with (ROOT/'reference'/filename).open(newline='') as f:rows=list(csv.DictReader(f))
 audit(filename+' row counts match',len(rows)==len(D[cat]))
md=(ROOT/'ALL_CONTENT.md').read_text()
audit('all lessons present in Markdown',all(f'## {l["id"]} — {l["title"]}' in md for l in lessons))
audit('all shortcuts present in Markdown',all(f'### {s["action"]}' in md for s in D['shortcuts']))
audit('all recipes present in Markdown',all(f'### {r["title"]}' in md for r in D['recipes']))
audit('no browser network API',not re.search(r'\bfetch\s*\(|\bXMLHttpRequest\s*\(|\bimport\s*\(', (ROOT/'assets/app.js').read_text()))
audit('skip link interception',all(x in (ROOT/'assets/app.js').read_text() for x in ('#skip-link','tabindex="-1"')))
for file in (ROOT/'practice').glob('*.png'):
 with Image.open(file) as im:
  im.verify()
audit('sample image PNGs decoded',len(list((ROOT/'practice').glob('*.png')))==6)
# Search index coverage is deterministic: app.js iterates every root family.
app=(ROOT/'assets/app.js').read_text()
audit('all reference libraries included in search',"const families=['tools','filters','shortcuts','glossary','recipes','troubleshooting']" in app and 'families.forEach(f=>D[f].forEach' in app)
audit('progress import/export exists',all(x in app for x in ('importProgress(file)','exportProgress()','state.bookmarks','state.completed')))
if len(sys.argv)>1 and sys.argv[1].endswith('.zip'):
 with zipfile.ZipFile(sys.argv[1]) as z:
  bad=z.testzip();names=z.namelist()
  audit('ZIP CRC validity',bad is None)
  audit('ZIP path safe',all(not n.startswith('/') and '..' not in Path(n).parts for n in names))
  audit('ZIP contains all required files',all('Photoshop_Field_Manual/'+x in names for x in filelist))
passed=sum(1 for _,ok,_ in results if ok)
print(f'\nRESULT: {passed}/{len(results)} checks passed')
if passed!=len(results):sys.exit(1)
