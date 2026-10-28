#!/usr/bin/env python3
"""Produce project planning, source, and version registers from course.json."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parent.parent
D=json.loads((R/'data/course.json').read_text(encoding='utf-8'))
lessons={x['id']:x for x in D['lessons']}
L=['# Learning curriculum and prerequisite graph','',
'**Windows edition · Adobe Premiere 26.5.2 · verified October 28, 2026.**',
'','## The dependency structure','',
'Stages 1–3 make a safe first edit. Stage 4 teaches precision; Stage 5 teaches the reasons for cuts. Stages 6–9 finish sound, picture, effects and captions. Stages 10–11 scale and automate the workflow. Stage 12 covers delivery, Stage 13 diagnostics, and Stage 14 applies everything. Advanced concepts are not required to export a beginner’s first video.','',
'**Prerequisite edges:** The list below is the explicit directed graph; each `Lxxx ← Lyyy` means study `Lyyy` first. A lesson may also build on general knowledge from earlier stages. There are no prerequisites pointing forward, and all ids are unique.','',
'## Stage overview','',
'| Stage | Band | Name | Lessons | Objective |','|---:|---|---|---:|---|']
for s in D['stages']:
 L.append(f"| {s['id']} | {s['level']} | {s['title']} | {len(s['lessons'])} | {s['goal']} |")
L+=['','## All stages, lessons, and practice assessments','']
for s in D['stages']:
 L += [f"### Stage {s['id']}: {s['title']} — {s['level']}", '',f"**Thesis:** {s['thesis']}",'',f"**Goal:** {s['goal']}",'', '| ID | Lesson | Required prerequisites | Practice duration |','|---|---|---|---:|']
 for id in s['lessons']:
  t=lessons[id]
  L.append(f"| {id} | {t['title']} | {', '.join(t['prerequisites']) or 'None'} | {t['duration']} min |")
 L+=['',f"**Stage challenge:** {s['challenge']}",'',f"**Pass criteria:** {s['pass']}",'',f"**Assessment questions:** {', '.join(s['quiz'])}",'']
L+=['## Learning strategy','',
'- **First month:** Complete stages 1–4 before worrying about advanced effects; make frequent short exports and inspect output files.',
'- **Intermediate block:** Complete story, audio and effects stages 5–7 using your own short clips; review the same cut for editorial and sound flaws.',
'- **Advanced block:** Complete color, captions, professional media and AI stages 8–11 while checking which specific services work with your installed release.',
'- **Expert and delivery:** Stages 12–14 focus on tested output and reproducible handoff. Read the field guides after corresponding prerequisites.',
'- **Review exercise:** For each mastered technique, undo a practice edit and explain what changed in source frames, sequence position, duration and output.',
'','## Lesson prerequisite edges','']
L+= [f"- `{x['id']}` ← {', '.join('`'+a+'`' for a in x['prerequisites']) or 'none'}" for x in D['lessons']]
(R/'CURRICULUM.md').write_text('\n'.join(L)+'\n',encoding='utf-8')
S=['# Research register and source limitations','',
 '**Edition 3.0 (comparative design review). Verification date: 2026-10-28.** The requested cutoff, October 29, is one day in the future; no later releases have been assumed. Version-specific claims are fixed to the Adobe Premiere desktop release **26.5.2 for Windows**.','',
 '## Official source register','',
 '| ID | Source / URL | Version relevance | Verified | Claim scope and notes |','|---|---|---|---|---|']
for x in D['sources']:
 S.append(f"| `{x['id']}` | [{x['title']}]({x['url']}) | {x['version']} | {x['verified']} | {x['notes'].replace('|','/')} |")
S+=['','## Research ranking and cross-check method','',
 '1. Current Adobe release notes for version/patch and dated change claims.',
 '2. Current Adobe help for workflows, terminology and UI; default keyboard command listing for shortcut rows.',
 '3. Adobe system, supported-format, hardware and issue pages for environmental limitations.',
 '4. The installed application would be the decisive check for panel layouts, applied effect names and user-remapped shortcuts; direct execution was not possible for this build.',
 '5. The project distinguishes official stable support, legacy/obsolete/removed distinctions and unresolved entries, beta functionality and externally processed features rather than silently treating them as equivalents.',
 '', '## Reconciliation and remaining conflicts','',
 '| Question | Resolution / confidence | Follow-up in Premiere |','|---|---|']
S+= [
 '| “Premiere” versus “Premiere Pro” | Adobe uses the shorter Premiere desktop branding on current documentation; “Premiere Pro” remains recognizable historical terminology | Check `Help > About Premiere` for installed build |',
 '| 26.5.2 vs announced 27.0 | 26.5.2 latest stable verified on date; v27 listed as upcoming | Revisit Adobe release notes after Oct 28, 2026 |',
 '| Old Essential Graphics tutorials | Modern Properties panel is primary for many selected graphics controls | Verify current Properties workflow and any workspace-specific differences |',
 f'| 26.x effects categorization | **{len(D["effects"])}** video/audio rows: distinguish published active, modern replacements, Legacy, Obsolete, Removed and unresolved. No installed-seat inventory check | Test exact processing identity, controls and effect list in installed 26.5.2 |',
 f'| Windows shortcut default vs customized | **{len(D["shortcuts"])}** documented Windows rows; Adobe menu/panel table and separate playback reference. Local customization and focus affect results | Compare to `Edit > Keyboard Shortcuts` with the intended panel active |',
 '| AI generation “offline” | Installed feature does not imply offline availability; service/credits/entitlements are separate requirements | Inspect current account dialog and Adobe service terms |',
 '| GPU and VM support | Supported *native* system specs do not certify arbitrary hypervisor passthrough or 4:2:2 hardware support | Test actual guest GPU, decode and encoder separately |',
 '| Premiere UI exact paths | Official docs were used, but no live application was available for final click-through validation | Validate workflow against installed Windows 26.5.2 |'
 ]
S+=['','## Why some sources do not prove every detail','',
 'Adobe often documents an effect category and selected examples rather than publishing a dated, machine-readable “complete installed effect inventory” tied to a particular patch. Old tutorials and legacy catalogs can include effects that were renamed, hidden, deprecated, bundled differently or require third-party products. The database’s `status` field is intentional and makes verification gaps visible.',
 '', 'All documentation URLs in this register are **references only**. The course itself never fetches data from these URLs and can be read with the internet disabled.']
(R/'SOURCES.md').write_text('\n'.join(S)+'\n',encoding='utf-8')
V=['# Release-specific feature and compatibility audit','',
 '**Target:** Adobe Premiere desktop **26.5.2** for **Windows**. Research date **2026-10-28**. Adobe release notes current then and last updated October 5, 2026; future October 29 publication cannot be verified yet.','',
 '## Version-specific release matrix','',
 '| Subject | Version | Stable by audit | Notes |','|---|---|---|---|']
for r in D['version_audit']:
 V.append(f"| {r['topic']} | {r['version']} | {r['stable']} | {r['notes']} |")
V+=['','## Stable-release teaching decisions','',
 '- Teach current **Properties panel** workflow for many graphics operations and annotate older Essential Graphics tutorials as historical.',
 '- Include **Paper Edit** and the **Generative Media Tool** as 26.5 features, with explicit transcript/service constraints.',
 '- Include Object Masking, generative extension and AI assistance as *reviewable tools*, not infallible one-click outputs.',
 '- Keep Premiere 27.0 and AI Assistant outside mandatory 26.5.2 stable-release lessons.',
 '- Verify all Windows shortcuts by active panel context and `Edit > Keyboard Shortcuts` when installed.',
 '- Treat export color, codec profile and source hardware compatibility as coupled technical specifications, not one-size-fits-all presets.',
 '', '## Requirements and offline boundary','',
 'Adobe’s current Windows technical requirements for this release list Windows 11 **24H2** as minimum. Full GPU acceleration, H.264/HEVC hardware decode/encode and newer chroma/bit-depth profiles depend on actual hardware and drivers. A Windows guest in Linux is not guaranteed to expose the host’s GPU, encoder or calibrated output; see `guides/05-WINDOWS-VM.md`.',
 '', 'The **HTML course** runs entirely from bundled local files. **Premiere activation**, many AI model calls, cloud collaboration, asset stores and credits/payment services are separate and may require online services, login or an additional plan. Adobe Media Encoder, After Effects, Audition and Photoshop are companion software; the guide describes their role without assuming they are owned.',
 '', '## High-risk claims awaiting in-application confirmation','',
 '- Complete patch-specific installed effect/transition inventory, and exact Premiere support for some legacy audio effect names.',
 '- Every individual shortcut when default shortcuts have been changed or an unexpected panel has focus.',
 '- Exact UI details in rolling cloud product updates or account-gated experiments.',
 '- Guest-GPU decode/encode with Blackwell, HEVC 4:2:2 or RAW without checking supported profiles.',
 '- Current online credit pricing or available third-party AI models; service contracts can change.',
 '', 'These uncertainties are marked openly in data, lessons, CSVs, field guides and the final audit.']
(R/'VERSION_AUDIT.md').write_text('\n'.join(V)+'\n',encoding='utf-8')
B='''# Beta, upcoming, deprecated and historical reference (optional)

This appendix is **not** required to complete the stable Premiere 26.5.2 curriculum. It should never be used to invent features that were not established in the researched release.

## Upcoming or Beta

- **AI Assistant:** Adobe has described AI-assistant experiences outside the current stable course. Because the requested stable 26.5.2 workflows do not establish availability, it is *not* a required lesson. Confirm official Beta documentation, conditions and release status if exploring separately.
- **Premiere 27.0:** An Adobe community announcement referenced forthcoming requirements. The October 28, 2026 research did not establish 27.0 as a stable release. Do not assume announced features are already present.
- **Generative service controls:** Model availability, generation credit requirements and account eligibility can change independently of the desktop application patch. They are never guaranteed for a particular seat by this manual.

## Historical interface or effect advice

- **Essential Graphics editing panel:** Many older tutorials teach controls in a legacy panel. Current learning content emphasizes **Properties** for selected graphic edits. An older screenshot should be treated as a historical illustration, not a reliable navigation instruction.
- **Legacy effects:** A name found in a historical Premiere catalog is not automatically a built-in 26.5.2 effect. The included `EFFECTS.csv` distinguishes Adobe-listed active effects, modern replacements, Legacy, Obsolete, Removed and unresolved audio or video names. Do not use Removed entries as instructions; inspect the installed Effects panel before relying on any uncertain entry.
- **Third-party plugins:** An effect from a plugin suite, After Effects or another Adobe application is not a guaranteed native Premiere effect. Installed copies and licenses vary.
- **Older title and DVD-style workflows:** Avoid using out-of-date templates that assume now-retired UI panels or delivery formats without verifying their current compatibility.

## How to reassess a future release

1. Read Adobe's dated release notes and `What's New` documentation.
2. Record exact Windows patch/build and minimum OS requirements.
3. Review changed UI, removed effects, media formats, hardware decoder/encoder profiles and known issues.
4. Recheck default shortcuts and current panels in the target installation.
5. Update the structured course and source register, rebuild the website/Markdown/CSV exports, and rerun all validation.
'''
(R/'BETA_AND_HISTORICAL.md').write_text(B,encoding='utf-8')
(R/'CAPSTONE.md').write_text('''# Final capstone and professional quality gates

The full production brief is available as **field guide 07** in the offline website and at [`guides/07-CAPSTONE-PRODUCTION.md`](guides/07-CAPSTONE-PRODUCTION.md). Complete the applied practice projects **L097–L104** and the capstone **L105**.

**Deliver:** (1) a 2:30–3:30 minute coherent film, (2) a reviewed H.264 MP4 copy, (3) a receiver-specified high-quality master, (4) a proofread caption file if speech is present, (5) the original media and permissions/usage notes, (6) a relinkable project archive, and (7) a short quality-control report.

**Pass standard:** 80/100 in the field guide rubric, with no critical failure of media integrity, audio, caption compliance or final export playback. An independent viewer should be able to understand the story, and a second editor should be able to open and verify the archived project.

There are ten applied briefs in Stage 14: short dialogue, music montage, YouTube explainer, documentary interview, promotional advertisement, multicam performance, color/mix, subtitle/graphics packaging and the integrated capstone. No proprietary or externally licensed assets are bundled or demanded.
''',encoding='utf-8')
(R/'CHANGELOG.md').write_text('''# Project changelog

## 2.0 — October 28, 2026 · independent second-pass audit

- Re-audited structural progression and 105 lessons; repaired applied-project prerequisites and expanded conceptual self-tests.
- Corrected a serious assessment bias: all 42 prior quiz answers were at position A; now evenly distributed with answers preserved.
- Cross-checked 182 Windows shortcut entries against Adobe's January 2026 menu/panel shortcut table and separately documented playback operations, with focus caveats.
- Reclassified and expanded to 145 effects and 91 transitions with Adobe 26.0 Legacy/Obsolete/Removed distinctions and 26.2–26.5 replacements.
- Added four deep technical field guides (13 total), updated the offline reader and maintained synchronized Markdown/CSV/JS output.
- Tightened progress-file import size handling; reran structural, browser-DOM and archive tests.
- Documented unverified installed Windows Premiere and direct file URL behavior, with exact evidence boundaries.

## 1.0 — October 28, 2026

- Established the target as Adobe Premiere for Windows **26.5.2**, recording the unreached Oct 29 research cutoff.
- Authored 105 progressive lessons in 14 stages, with prerequisites, exercises, objective mastery checks and 42 stage quizzes.
- Built responsive standalone offline HTML/CSS/JS interface with full-text search, bookmarks, notes, completion state, light/dark themes, interactive edit diagrams and JSON progress export/import.
- Added 123 Windows shortcut records, 95 effects entries (including clearly marked uncertain candidates), 21 transitions, 25 panels, 59 glossary terms, 20 workflow recipes and 20 troubleshooting records.
- Added nine detailed technical field guides and bundled original synthetic practice media.
- Generated full Markdown course edition, CSV reference exports, research/source records, release audit and automated validation scripts.
- Performed DOM/browser interaction tests through Chromium with inlined local assets; direct file navigation was blocked by the test environment and is documented as unverified.
''',encoding='utf-8')
print('Created curriculum and documentary research files')
