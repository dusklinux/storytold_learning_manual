#!/usr/bin/env python3
"""Second-pass independent qualitative-proxy gates; not a claim of semantic proof.
Run with `python scripts/deep_review.py` and include separate static and browser tests.
"""
from pathlib import Path
from collections import Counter
import json, subprocess, shutil, re, sys
R=Path(__file__).resolve().parent.parent
D=json.loads((R/'data/course.json').read_text(encoding='utf-8'))
G=json.loads((R/'data/guides.json').read_text(encoding='utf-8'))
L=D['lessons']; S=D['shortcuts']; F=D['effects']; T=D['transitions']; Q=D['quizzes']
results=[]
def check(label,pred):results.append((label,bool(pred)))
check('All lesson IDs L001–L105 contiguous', [x['id'] for x in L]==[f'L{i:03d}' for i in range(1,106)])
check('All 14 stage lesson groups nonempty',all(x['lessons'] and x['quiz'] for x in D['stages']))
check('All 105 lessons have >=3 exercise actions',all(len(x['steps'])>=3 for x in L))
check('All 105 lessons have expected outcomes & mastery',all(len(x['expected'])>12 and len(x['mastery'])>15 for x in L))
check('All 105 lessons have at least one error and corrective step',all(x['mistakes'] and x['fixes'] for x in L))
check('No unsafe intentional mistake reproduction',all('deliberately trigger' not in x['review_test'] for x in L))
check('No irrelevant universal playback exercise boilerplate',all('Compare before and after at normal playback' not in ' '.join(x['steps']) for x in L))
check('Film source file not modified in paper first lesson', 'without modifying originals' in L[0]['expected'])
check('Frame count example rollover 25fps', '00:00:04:00' in L[1]['deep_dive'] and '00:00:03:25 is invalid' in ' '.join(L[1]['steps']))
check('Preview rendering distinction on correct lesson', 'preview render files' in L[82]['deep_dive'] and 'ProRes' in L[84]['deep_dive'])
check('Patch vs targeting distinction in lesson L018', 'not the same switch' in L[17]['deep_dive'])
check('Independent applied project prerequisites',all('L096' not in x['prerequisites'] for x in L[96:104]))
check('All Q answer positions visually balanced',max(Counter(q['answer'] for q in Q).values())<=12 and 'function quizOrder(q){return [0,1,2,3];}' in (R/'app.js').read_text())
check('No extinct all-answers-A assessment bias',len(set(q['answer'] for q in Q))==4)
check('Full lesson exercises indexed in offline search',"x.steps.join(' ')" in (R/'app.js').read_text())
check('Alphabetically sorted glossary', [x['term'] for x in D['glossary']]==sorted([x['term'] for x in D['glossary']],key=str.casefold))
check('No duplicate video or audio effect name',len({(x['kind'],x['name']) for x in F})==len(F))
check('No duplicate transition name',len({x['name'] for x in T})==len(T))
check('Current video names assigned Adobe subject categories',not any(x['category'].startswith('Adobe 26.x active') for x in F))
check('No boilerplate active-effect descriptions',not any(x['purpose'].startswith('Adobe lists this as an active video effect') for x in F))
check('Effect classification includes active, Legacy, Obsolete, Removed, newer and unresolved',all(any(s in x['status'] for x in F) for s in ['active video','Legacy','Obsolete','Removed','replacement','Unresolved']))
check('Windows shortcut records document source and context',all(x['context'] and x['source'] and x['status'] for x in S))
check('No macOS key notation in Windows CSV',all(not any(k in x['windows'] for k in ['Cmd','Option','⌘','⌥']) for x in S))
check('Shortcut duplicates are context distinguishable',len({(x['windows'],x['command'],x['context']) for x in S})==len(S))
check('All bundled source links are HTTPS',all(x['url'].startswith('https://') for x in D['sources']))
check('All 13 field guide Markdown originals intact',all((R/x['filename']).read_text(encoding='utf-8')==x['markdown'] for x in G))
check('Progress JSON import has size bound', '2*1024*1024' in (R/'app.js').read_text())
check('Generated project documentation reflects 182 keys',all('182 Windows shortcut' in (R/n).read_text(encoding='utf-8') for n in ('README.md','CHANGELOG.md')))
check('Generated project documentation reflects 145 effects',all('145' in (R/n).read_text(encoding='utf-8') for n in ('README.md','SOURCES.md')))
# Verify local Markdown links in individual docs, not remote links or fragment-only anchors.
local=[]
for file in [R/'README.md',R/'CAPSTONE.md',*list((R/'guides').glob('*.md'))]:
 for url in re.findall(r'(?<!!)\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
  if '://' in url or url.startswith('#') or url.startswith('mailto:'):continue
  local.append((file,url.split('#')[0]))
check('Markdown local paths resolve',all((f.parent/path).exists() for f,path in local if path))
# Source metadata is a dated snapshot, not a future assumption.
check('No future research date in metadata',D['meta']['verified_on']=='2026-10-28' and '2026-10-28' in D['meta']['research_cutoff'])
# Native media probes are real (but do not establish import into Premiere).
ff=shutil.which('ffprobe')
if ff:
 videos=sorted((R/'sample_media').glob('*.mp4'))
 wavs=sorted((R/'sample_media').glob('*.wav'))
 good=True
 for p in videos+wavs:
  r=subprocess.run([ff,'-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)],text=True,capture_output=True)
  good=good and r.returncode==0 and float(r.stdout.strip() or '0')>0
 check('All five original practice media files demux with ffprobe',len(videos)==3 and len(wavs)==2 and good)
else:results.append(('All five original practice media files demux with ffprobe — NOT RUN',False))
for label,ok in results: print(('PASS' if ok else 'FAIL')+' '+label)
print(f'RESULT: {sum(ok for _,ok in results)}/{len(results)} passed')
sys.exit(0 if all(ok for _,ok in results) else 1)
