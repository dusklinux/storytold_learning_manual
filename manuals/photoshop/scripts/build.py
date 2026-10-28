"""Build static, offline Photoshop 27.11 learning system from authored Python data.
Usage: python scripts/build.py; no network, package manager or JS toolchain required.
"""
from pathlib import Path
import json,csv,random,re,hashlib,datetime,html
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from author import LESSONS,STAGES
from references import TOOLS,FILTERS,SHORTCUTS,GLOSSARY,TROUBLE,RECIPES
ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'reference'; CONTENT=ROOT/'content'; ASSETS=ROOT/'assets'; PR=ROOT/'practice'
VER='27.11'; DATE='2026-10-28'
SRC=[
 ('Adobe Photoshop desktop release notes','https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html','Last updated Oct 5, 2026. September 2026 version 27.11; recent feature changes in 27.6–27.11.'),
 ('Adobe Photoshop security bulletin APSB26-158','https://www.adobe.com/trust/security/products/photoshop/apsb26-158.html','Published Oct 13, 2026. Photoshop 2026 fixed/updated at 27.11, and LTS branch 26.11.8; confirms patch baseline.'),
 ('Adobe supported Photoshop versions','https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/photoshop-supported-versions.html','Sep 28, 2026. Stable current 27.x and prior 26.x; Help > About Photoshop on Windows.'),
 ('Adobe desktop technical requirements','https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/adobe-photoshop-on-desktop-technical-requirements.html','Sep 9, 2026. Windows requirements for 27.x; CPU/RAM/GPU/DirectX/scratch/internet.'),
 ('Adobe View keyboard shortcuts','https://helpx.adobe.com/photoshop/desktop/get-started/settings-and-preferences/view-keyboard-shortcuts.html','Sep 8, 2026. Edit > Keyboard Shortcuts and Ctrl+Alt+Shift+K; shortcut override verification method.'),
 ('Adobe filter effects reference','https://helpx.adobe.com/photoshop/desktop/effects-filters/blur-sharpen-filters/filter-effects-reference.html','Oct 4, 2026. Blur, sharpen, sketch and other filter classifications and bit-depth caveats.'),
 ('Adobe filters overview','https://helpx.adobe.com/photoshop/desktop/effects-filters/get-started-with-filters/filters-overview.html','Feb 23, 2026. Categories, Smart Filter compatibility and filter restrictions.'),
 ('Adobe Filter Gallery overview','https://helpx.adobe.com/photoshop/desktop/effects-filters/get-started-with-filters/filter-gallery.html','Current Adobe gallery descriptions and category explanations.'),
 ('Adobe Adjust image lighting with Light','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/adjust-image-lighting-with-light.html','Sep 9, 2026. Light adjustment layer introduced in 27.10 and six controls.'),
 ('Adobe adjust image color and tone','https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/adjust-image-color-and-tone.html','Sep 30, 2026. Adjustment layers versus Camera Raw and mask behavior.'),
 ('Adobe Generative Fill desktop','https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/edit-images-with-generative-fill.html','Sep 2026. Selection-based generative edits, model picker and output variations.'),
 ('Adobe generative AI overview','https://helpx.adobe.com/photoshop/desktop/generative-ai/generative-ai-features-overview.html','May 20, 2026. Cloud generative features and credits.'),
 ('Adobe generative troubleshooting','https://helpx.adobe.com/photoshop/kb/troubleshoot-generative-ai-features.html','Mode/bit-depth/selection, account/internet and credits requirements may constrain Generative Fill.'),
 ('Adobe on-device Remove model release evidence','https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html','May 2026 feature update: Remove local model after download and hardware check.'),
 ('Adobe filters troubleshooting','https://helpx.adobe.com/photoshop/desktop/troubleshoot/tool-feature-issues/filters-and-effects-errors.html','Oct 4, 2026. Filter limitations; GPU and mode diagnostics.'),
 ('Adobe Shake Reduction removal notice','https://helpx.adobe.com/photoshop/using/reduce-camera-shake-induced-blurring.html','May 2023. Adobe confirms removal starting with Photoshop 23.3 (April 2022); legacy only in 27.11.'),
 ('Adobe Topaz AI Sharpen and AI Denoise','https://helpx.adobe.com/in/photoshop/desktop/effects-filters/artistic-stylize-filters/enhance-images-with-generative-ai-filters.html','December 2025. Filter > AI Sharpen / Filter > AI Denoise, premium usage credits, 56 MP file limit and active-layer replacement.'),
 ('Adobe GPU setup','https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/enable-photoshop-to-use-the-graphics-processor.html','Feb 23, 2026. Edit > Preferences > Performance on Windows.'),
 ('Adobe Camera Raw introduction','https://helpx.adobe.com/camera-raw/desktop/get-started/overview-and-setup/introduction-camera-raw.html','Sep 29, 2026. RAW processing, metadata sidecars and Smart Object workflow.'),
 ('Adobe Camera Raw installer','https://helpx.adobe.com/camera-raw/desktop/troubleshoot/camera-raw-plug-in-installer.html','Sep 29, 2026. Lists Camera Raw 18.7 installer; plug-in version may vary from Photoshop.'),
 ('Adobe camera raw GPU troubleshooting','https://helpx.adobe.com/camera-raw/desktop/troubleshoot/acr-gpu-faq.html','GPU compatibility and guest/driver diagnostics.'),
 ('Adobe Photoshop preset file locations','https://helpx.adobe.com/photoshop/desktop/apply-painting-techniques/brushes-presets/photoshop-presets-locations.html','Legacy 3D removed; Save for Web legacy hidden since 23.0 according to current Adobe note.'),
 ('Adobe Add layer masks','https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/add-layer-masks.html','Dec 2025. Reveal and hide selections and mask gestures on Windows.'),
 ('Adobe linked Smart Objects','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/create-linked-smart-objects.html','Feb 23, 2026. File > Place Linked and linked layer icon.'),
 ('Adobe Smart Objects overview','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/smart-objects-overview-and-benefits.html','Feb 23, 2026. Editable transforms/filters, embedded versus linked, and painting limits.'),
 ('Adobe package linked Smart Objects','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/package-linked-smart-objects.html','Feb 23, 2026. File > Package; include linked assets for portable delivery.'),
 ('Adobe Remove objects tool','https://helpx.adobe.com/photoshop/desktop/repair-retouch/remove-objects-fill-space/remove-unwanted-objects-and-distractions.html','Aug 18, 2026. Remove Tool processing modes including Device and Cloud.'),
 ('Adobe Remove Tool hardware requirements','https://helpx.adobe.com/photoshop/desktop/repair-retouch/remove-objects-fill-space/remove-tool-minimum-and-recommended-hardware-requirements.html','Aug 18, 2026. On-device model requirements may substantially exceed normal Photoshop minimum.'),
 ('Adobe combine images','https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/transform-manipulate-reshape/combine-images-in-photoshop.html','Sep 28, 2026. Object Selection, masks and compositing workflow.'),
 ('Adobe Batch-process files','https://helpx.adobe.com/photoshop/desktop/automate-tasks/process-a-batch-of-files/batch-process-files.html','Feb 23, 2026. File > Automate > Batch, Actions and source/destination safeguards.'),
 ('Adobe keyboard shortcut troubleshooting','https://helpx.adobe.com/photoshop/desktop/troubleshoot/tool-feature-issues/keyboard-shortcuts-not-working.html','Shortcut conflicts and resets; observed behavior may depend on customization.'),
 ('Adobe compare desktop/web functionality','https://helpx.adobe.com/photoshop/web/get-set-up/learn-the-basics/compare-photoshop-web-and-desktop-features.html','Broad desktop tool family corroboration; web features must not be mistaken for desktop instructions.'),
 ('Adobe Photoshop Beta product update','https://community.adobe.com/product-updates','Oct 15, 2026 modernized toolbar UI explicitly Beta; excluded from stable instructions.')]

# Stage projects provide measurable synthesis without gating navigation.
PROJECTS=[
 ('Pixel field guide','Create a labeled 800 × 600 PSD comparing raster marks, vector shapes, PPI and zoom; keep two versions.','Show 100% and 400% views; correctly distinguish pixel count from print density.'),
 ('Editable six-tile layout','Build six organized shape/text layers, two groups, clear alignment and transparent PNG output.','Grid spacing consistent within 4 px; PSD layers remain editable.'),
 ('Edge isolation studio','Extract three objects using color range, object selection and a Pen/vector mask; test on dark/light backgrounds.','Three separately toggled masks; no major hard fringe at 100%.'),
 ('Reversible visual treatment','Create an original PSD plus three looks using Curves, Smart Filters, Blend If and named layer styles.','Each look toggles independently; master pixels untouched.'),
 ('Careful restoration','Repair a damaged practice image, showing healing, cloning, dodge/burn and an annotated before/after.','No major repeated textures; source copy preserved.'),
 ('Limited-palette artwork','Paint a five-layer scene and a swatch board using fixed and dynamics brushes, gradient and value hierarchy.','Scene reads at 10% view; colors can be recreated from swatches.'),
 ('Typographic poster','Create a 1200 × 1600 poster with two type sizes, correct tracking/leading, 3 vector shapes and a Bézier icon.','Editable live text; consistent 64 px margins; no overflow.'),
 ('Color-managed portrait and print proof','Prepare a neutral and creative grade, inspect histogram, record output profile and native print size.','No accidental clipping; ICC assumptions documented.'),
 ('Multi-plane photo composite','Composite subject, floor, sky and graphic insert with perspective, shadows, haze and selective color adjustments.','No floating object; coherent key-light direction and mask boundaries.'),
 ('Production export bundle','Build a reusable template, export three sizes and run/test one Action against 3 different source files.','Correct filenames/sizes; zero overwritten sources.'),
 ('Technical incident report','Audit your own system and run a safe VM-or-native GPU, memory, scratch, account/offline diagnostic.','Document contains exact observed GPU, vRAM, Photoshop version and unknowns.'),
 ('Complete campaign brief','Produce three-format advertisement, an optional advanced photo restoration, editable PSD, proof images and change log.','Target 85%+ final rubric; no critical source loss or missing linked assets.')]

stages=[]
for i,(title,desc) in enumerate(STAGES,1):
 ids=[x['id'] for x in LESSONS if x['stage']==i]
 stages.append(dict(id=i,title=title,description=desc,lessons=ids,project={'title':PROJECTS[i-1][0],'brief':PROJECTS[i-1][1],'pass':PROJECTS[i-1][2]}))
for k,x in enumerate(LESSONS):
 x['next']=LESSONS[k+1]['id'] if k+1<len(LESSONS) else None
 x['previous']=LESSONS[k-1]['id'] if k else None
 x['connections']=[v for v in [x['next'],LESSONS[max(0,k-5)]['id'] if k>=5 else None] if v]
 # Change fixed-position answer ordering for genuine assessments.
 shift=(k*7+2)%3
 ans=x['answers'];x['answers']=ans[shift:]+ans[:shift];x['correct']=(x['correct']-shift)%3
 x['completion']=[x['proof'],'Explain why this workflow is appropriate rather than a destructive alternative.']

SPECIAL=[
 dict(feature='Light adjustment layer',status='stable',introduced='27.10 (August 2026)',meaning='Exposure, Contrast, Highlights, Shadows, Whites and Blacks on live adjustment layer.'),
 dict(feature='Enhance edge',status='stable',introduced='27.11 (September 2026)',meaning='AI-powered selection edge refinement; cloud/model conditions need current in-app check.'),
 dict(feature='GPT Image 2 model',status='online model option',introduced='27.11 (September 2026)',meaning='Available for Generate Image/Prompt to edit as listed in release notes; entitlement/model list may change.'),
 dict(feature='On-device Remove Tool model',status='stable, conditional',introduced='27.7 (May 2026)',meaning='Downloadable local model on supported hardware; not the same as all generative features working offline.'),
 dict(feature='Generative Fill / Generate Image / Harmonize',status='online/service',introduced='features of stable release',meaning='Account, service, generative credits and sometimes model picker required.'),
 dict(feature='AI Assisted Editor',status='Beta',introduced='27.10 (August 2026)',meaning='Explicit Beta; not required curriculum and not treated as stable.'),
 dict(feature='Modernized Toolbar and Tool Options',status='Beta',introduced='Oct 15, 2026 Beta announcement',meaning='Not assumed in the 27.11 stable UI.'),
 dict(feature='Dynamic Text along shapes/paths',status='stable',introduced='27.6/27.10 (2026)',meaning='Newer controls; ordinary editable path text taught as universal prerequisite.'),
 dict(feature='Save As format customization',status='stable',introduced='27.10 (August 2026)',meaning='Show, hide and reorder formats in Save As and Save a Copy dialogs.'),
 dict(feature='Recent document presets management',status='stable',introduced='27.11 (September 2026)',meaning='Rename/delete Recents in New Document dialog.'),
 dict(feature='3D legacy tools',status='removed',introduced='legacy, removed before 27.11',meaning='Do not use old 3D tutorials as current Photoshop production commands.'),
 dict(feature='Save for Web',status='legacy / hidden by default',introduced='older workflow',meaning='Use Export As in modern workflow; historical recipes may mention Save for Web.'),
 dict(feature='LTS maintenance branch',status='separate version',introduced='26.11.8 as of Oct 13, 2026',meaning='Not same as current feature branch 27.11.'),
 dict(feature='Camera Raw',status='separately versioned plugin',introduced='18.7 installer listed Sep 2026',meaning='Check Help > About Plug-In > Camera Raw; do not confuse with Photoshop version.')]

# Mark risk-specific entries instead of asserting unavailable tools exist.
for t in TOOLS:
 t['id']='tool-'+re.sub('[^a-z0-9]+','-',t['title'].lower()).strip('-')
 t['location']='Toolbar (expand matching tool group; use Edit > Toolbar if hidden)'
 t['status']='Legacy workflow' if 'legacy' in t['family'].lower() else 'Tool family; inspect toolbar configuration'
for f in FILTERS:
 f['id']='filter-'+re.sub('[^a-z0-9]+','-',f['title'].lower()).strip('-')
 f['location']=('Filter > Filter Gallery' if 'Filter Gallery' in f['family'] else ('Filter > '+f['family']+' > '+f['title'] if f['family'] in ('Blur','Sharpen','Noise','Distort','Pixelate','Render','Stylize') else 'Filter menu / associated filter workspace; inspect the live menu'))
 f['status']='Legacy / confirm in current menu' if 'Shake Reduction' in f['title'] else ('Service / check entitlement' if f['family'] in ('AI partner','Neural / AI') else 'Documented family; mode and GPU limits apply')
for section, items, titlefield in [('glossary',GLOSSARY,'term'),('troubleshooting',TROUBLE,'symptom'),('recipes',RECIPES,'title')]:
 for i,x in enumerate(items):x['id']=section[:-1]+'-'+re.sub('[^a-z0-9]+','-',x[titlefield].lower()).strip('-')

from second_pass import patch
patch(LESSONS, TOOLS, FILTERS, SHORTCUTS, GLOSSARY, TROUBLE, RECIPES)

DATA=dict(manifest=dict(project='Photoshop Field Manual: Windows Edition',edition='1.2.0',photoshop_version=VER,release='September 2026; exact day not established from consulted release notes',security_patch_evidence='Adobe October 13, 2026 APSB26-158: 27.11',verified_on=DATE,research_cutoff_requested='2026-10-29',scope='Photoshop 2026 stable desktop, Windows; offline reader Windows/Linux',lessons=len(LESSONS)),stages=stages,lessons=LESSONS,tools=TOOLS,filters=FILTERS,shortcuts=SHORTCUTS,glossary=GLOSSARY,troubleshooting=TROUBLE,recipes=RECIPES,changes=SPECIAL,sources=[{'title':a,'url':b,'evidence':c,'checked':DATE} for a,b,c in SRC])
CONTENT.joinpath('content.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ASSETS.joinpath('content.js').write_text('"use strict";window.MANUAL_DATA='+json.dumps(DATA,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';\n',encoding='utf-8')
CONTENT.joinpath('manifest.json').write_text(json.dumps(DATA['manifest'],indent=2)+'\n',encoding='utf-8')
# Offline reader is self-contained: data, CSS and application JS embedded at build-time.
# Assets remain individually authored and included for inspection, tests, and rebuilds.
TEMPLATE=(ROOT/'web/index.template.html').read_text(encoding='utf-8')
page=TEMPLATE.replace('  <link rel="stylesheet" href="assets/style.css">', '<style>\n'+(ASSETS/'style.css').read_text(encoding='utf-8')+'\n</style>')
page=page.replace('  <script defer src="assets/content.js"></script>', '')
page=page.replace('  <script defer src="assets/app.js"></script>', '')
# Inline scripts must execute after the body element they use (inline defer has no effect).
page=page.replace('</body>', '<script>\n'+(ASSETS/'content.js').read_text(encoding='utf-8')+'\n</script>\n<script>\n'+(ASSETS/'app.js').read_text(encoding='utf-8')+'\n</script>\n</body>')
ROOT.joinpath('index.html').write_text(page,encoding='utf-8')


def csvout(filename,cols,items):
 with (REF/filename).open('w',encoding='utf-8',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');wr.writeheader();wr.writerows(items)
csvout('TOOLS.csv',['id','title','family','location','shortcut','purpose','controls','use','caution','status','lesson'],TOOLS)
csvout('FILTERS.csv',['id','title','family','location','controls','effect','use','caution','status','lesson'],FILTERS)
csvout('SHORTCUTS.csv',['family','action','keys','context','note'],SHORTCUTS)
csvout('GLOSSARY.csv',['id','term','definition','lesson'],GLOSSARY)
csvout('TROUBLESHOOTING.csv',['id','symptom','cause','diagnosis','solution','warning','lesson'],TROUBLE)
csvout('RECIPES.csv',['id','title','requires','procedure','pass'],[{**r,'requires':', '.join(r['requires'])} for r in RECIPES])

def mdformat_lesson(l):
 s=next(st for st in stages if st['id']==l['stage'])
 return '\n'.join([f'## {l["id"]} — {l["title"]}',f'**Stage {l["stage"]}:** {s["title"]}  ',f'**Objective:** {l["objective"]}  ',f'**Prerequisites:** {", ".join(l["prerequisites"]) or "None"}',
  '### Concept and principle',l['concept'],'### Location (Windows)',l['location'],'### Walkthrough']+[f'{i}. {t}' for i,t in enumerate(l['steps'],1)]+['### Expected result',l['expected'],'### Why it works',l['why'],'### Practical application',l['use'],'### Common mistake and fix',l['mistake'],'### Efficiency tip',l['tip'],'### Independent exercise',l['practice'],'### Completion criteria',l['proof'],'### Knowledge check',l['question']]+[f'- {a}' for a in l['answers']]+[f'**Answer:** {l["answers"][l["correct"]]}. {l["explanation"]}', '### Connections','; '.join(l['connections']) or 'Final lesson.', ''])

md=['# Photoshop Field Manual — Windows Edition',f'Photoshop {VER}; researched {DATE}. Offline Linux/Windows reading; Photoshop directions are Windows only.','', 'The research cutoff requested was October 29, 2026, one day after verified execution date. No October 29 release is presumed.', '', '## How to use','Study stages in order, perform each exercise in Photoshop, then check its success criteria. The website contains navigation, searchable references and portable progress, all without networking. This Markdown edition is also fully readable offline.','']
for s in stages:
 md += [f'# Stage {s["id"]} — {s["title"]}',s['description'],'']
 md += [mdformat_lesson(l) for l in LESSONS if l['stage']==s['id']]
 p=s['project'];md += [f'## Stage {s["id"]} project — {p["title"]}',p['brief'],f'**Pass condition:** {p["pass"]}','']
md += ['# Reference encyclopedias','']
for heading,collection,fields in [('Tools',TOOLS,['purpose','location','shortcut','controls','use','caution','status','lesson']),('Filters',FILTERS,['effect','location','controls','use','caution','status','lesson']),('Windows shortcuts',SHORTCUTS,['family','keys','context','note']),('Concept glossary',GLOSSARY,['definition','lesson']),('Troubleshooting',TROUBLE,['cause','diagnosis','solution','warning','lesson']),('Professional recipes',RECIPES,['requires','procedure','pass'])]:
 md += [f'## {heading}','']
 for x in collection:
  name=x.get('title',x.get('term',x.get('symptom',x.get('action',''))))
  md += ['### '+name]
  for key in fields:
   val=x.get(key,''); val=', '.join(val) if isinstance(val,list) else val
   md += [f'**{key.replace("_"," ").capitalize()}:** {val}  ']
  md += ['']
md+=['# Version changes and limitations','']
for x in SPECIAL:md += [f'### {x["feature"]}',f'{x["status"]}; {x["introduced"]}. {x["meaning"]}','']
md+=['# Research sources','']
for a,b,c in SRC:md += [f'- {a}: {b} (checked {DATE}). {c}']
ROOT.joinpath('ALL_CONTENT.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

curr=['# Curriculum and dependencies','',f'75 sequential lessons across 12 stages; Photoshop {VER} (Windows).','', 'Lessons are indexed by stable identifiers. Default prerequisite: immediately prior lesson; earlier skills are explicitly reinforced at stages/projects. The website never locks navigation.','']
for s in stages:
 curr+= [f'## Stage {s["id"]}: {s["title"]}',s['description'],'']
 for id in s['lessons']:
  l=next(x for x in LESSONS if x['id']==id)
  curr += [f'- `{id}` {l["title"]} (requires {", ".join(l["prerequisites"]) or "none"})']
 curr+= [f'**Project:** {s["project"]["title"]} — {s["project"]["pass"]}','']
curr += ['## Cross-stage dependency map','', 'Pixels → dimensions → layers → selections → masks → adjustment layers/Smart Objects → retouch & brush foundations → paths/type → color/RAW → perspective/compositing → output automation → troubleshooting → capstones.','', 'Suggested revision: repeat masking after Stage 5; revisit Smart Filters after Stage 8; do a full export/preflight before Stage 12.']
ROOT.joinpath('CURRICULUM.md').write_text('\n'.join(curr)+'\n',encoding='utf-8')

source_md=['# SOURCES — verified baseline', '', f'**Research executed:** {DATE}. **Requested cutoff:** 2026-10-29 (future relative to execution). No later release has been assumed.', '',f'**Selected stable feature release:** Photoshop 2026 {VER}, labelled September 2026 in Adobe desktop release notes (updated Oct 5). Exact day of initial release not specified in the source. **Security patch confirmation:** Adobe APSB26-158, published Oct 13, lists updated Photoshop 2026 version 27.11; no finer 27.11.x patch was established. **Separate LTS:** 26.11.8.','', 'All sources below are official Adobe pages, read or checked online on October 28, 2026. The manual preserves URLs as references but does not load them while offline. Terminology may change under a later release or customized UI.','']
source_md += [f'{i}. **{a}** — {b}\n   - Reviewed: {DATE}. {c}' for i,(a,b,c) in enumerate(SRC,1)]
source_md+=['','## Evidence policy','- Release-specific additions and Beta status come from official release notes and Beta announcements.','- Ordinary long-standing tool workflows are corroborated by Photoshop desktop documentation and organized for education; not every individual control was exercised in Photoshop.','- Tool shortcut letters and common Windows commands are conservative reference values; the installed Edit > Keyboard Shortcuts dialog remains authoritative after customizations.','- Labels and offerings of cloud/AI models, credits and subscription entitlements can change without desktop version change.','- GPU hardware requirements are official; virtualization recommendations are practical diagnostic guidance, not official Adobe VM certification.','- Shortcut, tool/filter and operating-system support claims not independently simulated inside Photoshop are marked as requiring live-application verification in AUDIT.md.']
ROOT.joinpath('SOURCES.md').write_text('\n'.join(source_md)+'\n',encoding='utf-8')

readme=f'''# Photoshop Field Manual — Windows Edition

**Verified Photoshop version:** {VER} (September 2026 release, confirmed by Adobe Oct 13 security bulletin). Research checked {DATE}; the Oct 29 requested cutoff had not yet occurred.

## Start reading offline

1. Extract this entire ZIP to a normal folder on Linux or Windows; retain subfolders.
2. Double-click `index.html` or open it as a local `file://` URL in a modern Chromium, Firefox or Edge browser.
3. Choose **Start learning**. Use the sidebar to browse 12 stages, or **Search** to locate tools, filters, concepts, recipes and troubleshooting.
4. Complete a lesson after checking its exercise; quiz answers are revealed when you check them. Progress is informative, never a lock. In **Progress & transfer**, choose larger text, high contrast or one-step walkthrough reading.
5. Use **Export progress** and **Import progress** to carry a JSON file between browsers or machines. Import validates the backup, checks the Photoshop target version and asks for confirmation before replacing the current record. There is no automatic sync; local storage policies vary and can be disabled for `file://`.

The site requires **no internet, web server, Node.js, CDN, cloud font or online script**. The learning data, styles and reader code are embedded into `index.html`; there are no separate scripts to load. All core lessons and references work when local storage is disabled, but your progress may not persist; export JSON regularly. Source URLs are optional external reading, not runtime requirements.

## Photoshop setup (Windows only)

Install the Adobe Creative Cloud desktop app and Photoshop 2026 27.11 through your Adobe account; confirm Windows Photoshop version via **Help > About Photoshop**. Official minimums for 27.x: supported Windows builds, 8 GB RAM, Intel/AMD AVX2-compatible CPU, and DirectX 12 feature level 12_0 with suitable VRAM; Adobe recommends 16 GB+ RAM, SSD/scratch capacity and more GPU memory for high-resolution work. See `SOURCES.md` for precise specifications. Adobe activation and certain subscriptions/services require connectivity.

Using Photoshop in a Windows VM while reading on Linux requires the **Windows guest** to present an adequate GPU/driver. Host Linux graphics acceleration alone proves nothing about guest DirectX compatibility. Check **Help > System Info** and **Edit > Preferences > Performance** inside the guest; fallback or missing GPU features are common with virtual adapters. Adobe support for an entire VM configuration is not implied.

## Structure

- `index.html` — self-contained offline reader with inline CSS/JavaScript/data; `web/index.template.html` and `assets/*` — editable build inputs, diagrams and assets.
- `content/content.json` — structured canonical content; `scripts/author.py`, `scripts/references.py` and `scripts/second_pass.py` are editable authoring source.
- `ALL_CONTENT.md` — full reading edition generated from the same data.
- `CURRICULUM.md` — all stages, prerequisites, stage-end assignments.
- `reference/*.csv` — filter, tool, shortcut, glossary, recipe and diagnostic exports.
- `practice/*.png` — original synthetic exercise assets, no external license dependency.
- `SOURCES.md`, `AUDIT.md`, `AUDIT_CROSS_MANUAL.md`, `AUDIT_SECOND_PASS.md`, `AUDIT_INITIAL_1.0.0.md`, `CHANGELOG.md` — research, comparative and earlier audits, and revision history.
- `scripts/build.py` — rebuild derived content (requires Python and Pillow for samples); `scripts/validate.py` and `scripts/audit_second_pass.py` — structural/content checks; `scripts/browser_test.py`, `scripts/browser_extended.py` — optional Playwright/Chromium tests; `scripts/check_manifest.py`, `scripts/package.py` — checksum and reproducible ZIP tooling; `MAINTENANCE.md` — authoring and progress-data contract.

The SHA-256 manifest (`MANIFEST.sha256`) can be checked with `python scripts/check_manifest.py --check` after extraction. The bundled reader can be used without Python.

This project includes {len(LESSONS)} lesson modules, {len(TOOLS)} tool entries, {len(FILTERS)} filter entries, {len(SHORTCUTS)} shortcut entries, {len(GLOSSARY)} glossary terms, {len(TROUBLE)} troubleshooting cases, {len(RECIPES)} recipes, 12 stage projects and {len(LESSONS)} graded quiz prompts.

## Teaching and accuracy notes

The manual focuses on stable workflows, not unverified 'every possible' control. Some rare, version-specific, legacy or model-dependent features are identified as such. Do not treat the site as legal advice about licensing, authorization or representation; use images you own or have permission to edit. For updates to 27.11, consult Adobe's official documentation once online. No Photoshop desktop was available for direct GUI validation during publishing; see `AUDIT.md`.
'''
ROOT.joinpath('README.md').write_text(readme,encoding='utf-8')
ROOT.joinpath('CHANGELOG.md').write_text(f'''# CHANGELOG\n\n## 1.2.0 — {DATE} (cross-manual quality pass)

- Adapted relevant quality patterns from the supplied After Effects manual: strict version-aware progress backup validation, readable large-text and high-contrast settings, one-step lesson view with full print expansion, and deeper regression coverage.
- Added self-contained inline-data `index.html` to reduce local-file compatibility risks while retaining editable component source files and original practice resources.
- Added deterministic SHA-256 payload manifest, extra malformed-import and offline-browser validation, and a maintenance handoff.
- Retained all 75 Photoshop lessons and the curated 27.11-specific content; did not import After Effects technical instruction or shortcut records.

## 1.1.0 — {DATE} (second-pass audit)\n\n- Corrected modern shortcut conflicts: R rotates view; K selects Frame; Blur/Sharpen/Smudge have no current assigned default.\n- Corrected Quick Mask, Camera Raw, Quick Export, and conditional filter command locations.\n- Added Adjustment Brush and repaired tool-group references.\n- Added cross-stage dependencies, focused troubleshooting tips, reference recipes, glossary definitions and a contextual shortcut list.\n- Added second-pass structural checks and documented verification boundaries.\n- Corrected Shake Reduction: removed in Photoshop 23.3; made Filter > AI Sharpen/Denoise conditional service paths explicit.\n\n## 1.0.0 — {DATE}\n\n- Established Adobe-verified Photoshop 2026 27.11 baseline.\n- Authored {len(LESSONS)} progressive lessons and quizzes across 12 stages and project rubrics.\n- Published local-file HTML interface, search, bookmarks, progress export/import and references.\n- Curated technical encyclopedias and independent sample exercise images.\n- Generated Markdown/CSV editions from shared source and ran validation and offline browser checks.\n''',encoding='utf-8')

# Original, locally reproducible synthetic practice images; no outside images.
random.seed(1826)
font=None
try:font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',28)
except:font=ImageFont.load_default()
def save_img(name,im):im.save(PR/name,optimize=True)
# Masks and selections
im=Image.new('RGB',(1200,800),'#efedf4'); d=ImageDraw.Draw(im)
d.rectangle((0,625,1200,800),fill='#d8dce8');d.ellipse((100,125,570,625),fill='#e76d63');d.rounded_rectangle((500,200,1030,680),radius=72,fill='#1b8a91');d.polygon([(705,65),(1120,280),(830,545)],fill='#f4ba51');
for x in range(110,1100,100):d.line((x,690,x,740),fill='#a7adbb',width=3)
d.text((42,45),'Selection practice: shapes with distinct and overlapping edges',fill='#343a52',font=font);save_img('mask-shapes.png',im)
# Controlled tone test
im=Image.new('RGB',(1200,700));pix=im.load()
for x in range(1200):
 v=round(18+225*x/1199)
 for y in range(700):pix[x,y]=(v,v,min(255,round(v*.92+10)))
d=ImageDraw.Draw(im);d.rectangle((55,110,1145,580),outline='#abbacc',width=4)
for x in range(100,1150,100):d.line((x,100,x,590),fill='#546478',width=2)
d.text((80,35),'Tone ramp — inspect Levels, Curves, clipping and banding',fill='white',font=font);save_img('tone-gradient.png',im)
# Palette
im=Image.new('RGB',(1050,600),'#f4f1ec');d=ImageDraw.Draw(im)
colors=['#25465c','#e5ad4a','#db5a55','#8ab3a2','#6e6b88','#e9e3cf']
for i,c in enumerate(colors):
 x=40+(i%3)*345;y=90+(i//3)*235;d.rounded_rectangle((x,y,x+300,y+160),radius=18,fill=c);d.text((x+25,y+170),c,fill='#24303c',font=font)
d.text((40,20),'Sample these colors with Eyedropper (I)',fill='#27313c',font=font);save_img('color-palette.png',im)
# Retouch, textured gradient with deliberate spot-like defects
im=Image.new('RGB',(1200,800));pix=im.load();random.seed(2711)
for y in range(800):
 for x in range(1200):
  n=random.randint(-7,7);t=x/1200+0.35*y/800
  pix[x,y]=tuple(max(0,min(255,int(base+shift*t+n))) for base,shift in ((190,30),(161,28),(143,20)))
d=ImageDraw.Draw(im)
random.seed(77)
for i in range(45):
 x=random.randint(100,1100);y=random.randint(120,720);r=random.randint(4,11)
 d.ellipse((x-r,y-r,x+r,y+r),fill=random.choice(['#65514a','#b55957','#e7c5b1']))
d.text((35,25),'Synthetic retouching practice — deliberately added spots',fill='#2b2528',font=font)
save_img('retouch-dots.png',im)
# Perspective grid scene
im=Image.new('RGB',(1200,800),'#c9d6dc');d=ImageDraw.Draw(im)
d.rectangle((0,440,1200,800),fill='#a7b3ae');d.line((0,440,1200,440),fill='#697a8b',width=6)
for x in range(-800,2001,190):d.line((600,440,x,800),fill='#7c928a',width=3)
for y in (480,525,585,675,790):d.line((0,y,1200,y),fill='#849b91',width=3)
d.rounded_rectangle((420,220,790,650),radius=18,fill='#d9875b',outline='#5f4943',width=8)
d.text((40,26),'Synthetic perspective / composite practice',fill='#27313c',font=font);save_img('perspective-room.png',im)
# Transparent asset
im=Image.new('RGBA',(700,700),(0,0,0,0));d=ImageDraw.Draw(im)
d.ellipse((125,125,575,575),fill='#efbc67',outline='#343e54',width=24)
d.polygon([(350,190),(395,304),(515,315),(420,392),(447,515),(350,449),(253,515),(280,392),(185,315),(305,304)],fill='#304c67')
save_img('transparent-sticker.png',im)

# Three local explanatory diagrams, pure SVG and thus offline.
(ASSETS/'diagram-mask.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 180"><rect width="780" height="180" rx="12" fill="#eef3f6"/><g font-family="Arial" font-size="15" fill="#244056" text-anchor="middle"><text x="130" y="25">Original layer</text><text x="390" y="25">Mask coverage</text><text x="650" y="25">Visible result</text></g><rect x="40" y="45" width="180" height="110" rx="8" fill="#0a8197"/><circle cx="130" cy="100" r="46" fill="#efb55c"/><defs><linearGradient id="m"><stop stop-color="white"/><stop offset="1" stop-color="black"/></linearGradient><clipPath id="v"><rect x="560" y="45" width="180" height="110"/></clipPath></defs><rect x="300" y="45" width="180" height="110" rx="8" fill="url(#m)"/><g clip-path="url(#v)"><rect x="560" y="45" width="180" height="110" fill="#eef3f6"/><path d="M560 45 H650 Q720 100 650 155 H560 Z" fill="#0a8197"/><circle cx="650" cy="100" r="46" fill="#efb55c"/></g><g fill="#56717c" font-size="23" font-family="Arial"><text x="245" y="105">×</text><text x="507" y="105">=</text></g></svg>''',encoding='utf-8')
(ASSETS/'diagram-pixels.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 170"><rect width="780" height="170" rx="12" fill="#eef3f6"/><g font-family="Arial" font-size="17" fill="#264055"><text x="30" y="30">Raster samples (zoom reveals grid)</text><text x="425" y="30">Vector path (geometry is editable)</text></g><g stroke="#f4f6f8" stroke-width="2"><rect x="45" y="65" width="42" height="42" fill="#295675"/><rect x="88" y="65" width="42" height="42" fill="#295675"/><rect x="131" y="65" width="42" height="42" fill="#df8158"/><rect x="174" y="65" width="42" height="42" fill="#df8158"/><rect x="217" y="65" width="42" height="42" fill="#df8158"/><rect x="260" y="65" width="42" height="42" fill="#295675"/></g><path d="M425 135 C470 10 600 10 725 135" fill="none" stroke="#237e94" stroke-width="6"/><g fill="#e59d41" stroke="#f5f7f9" stroke-width="3"><circle cx="425" cy="135" r="8"/><circle cx="725" cy="135" r="8"/></g></svg>''',encoding='utf-8')
(ASSETS/'diagram-composite.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 210"><rect width="780" height="210" rx="12" fill="#eff3f5"/><path d="M40 90 H740 V185 H40Z" fill="#c8d4c7"/><path d="M40 90 H740" stroke="#75928e" stroke-width="3"/><path d="M100 185 L390 90 L680 185" stroke="#89a59d" stroke-width="2" fill="none"/><rect x="305" y="65" width="120" height="115" rx="11" fill="#d6875a"/><ellipse cx="365" cy="183" rx="89" ry="16" fill="#5d6863" opacity=".45"/><ellipse cx="367" cy="177" rx="58" ry="8" fill="#424744" opacity=".6"/><path d="M600 25 L550 80" stroke="#eab33c" stroke-width="6" stroke-linecap="round"/><path d="M550 80 L553 53 M550 80 L577 75" stroke="#eab33c" stroke-width="6" fill="none"/><g font-family="Arial" font-size="16" fill="#254458"><text x="46" y="33">Horizon</text><text x="450" y="30">Key light</text><text x="455" y="161">Cast shadow</text><text x="455" y="188">Contact shadow</text></g></svg>''',encoding='utf-8')
print('built',len(LESSONS),'lessons',len(TOOLS),'tools',len(FILTERS),'filters')
