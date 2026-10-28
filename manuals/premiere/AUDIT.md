# Third-pass comparison and final-release audit — 2026-10-28

The prior v2 audit appears below as a historical baseline. The **current v3 findings supersede its reference counts, search/navigation description and browser-test coverage**. Its Adobe-source technical caveats and native-application limitations remain applicable. See `COMPARATIVE_AUDIT.md` for the explicit reasons for adopting some design patterns from the supplied After Effects manual and rejecting app-specific material.

**Current edition:** Premiere 26.5.2 for Windows, researched October 28, 2026. Independent Adobe release-note check reconfirmed the September 2026 version 26.5.2 entry (Adobe release notes updated October 5, 2026). No October 29 future release assumed.

## Macro audit after cross-manual comparison

- **Preserved:** 14 monotonic stages, 105 stable-ID lessons, explicit backward prerequisite edges, 42 stage quiz questions with balanced correct positions, 13 substantial field guides, 10 professional capstone briefs, and the original media exercises. The 40-lesson/six-stage After Effects course architecture would be a regression for Premiere's existing detailed sequence; it was not imported.
- **Improved:** Searched effects/shortcuts/transitions/panels/glossary terms now have exact, focusable URLs; prior generic catalog landing pages meant searching a record did not reliably land on the answer. Reading settings now include large text, high contrast and single practice-step focus, with all steps present in print output.
- **Expanded for reference usability:** 107 glossary entries (previously 59), 37 symptom-first troubleshooting cases (previously 20), 30 practical workflow recipes (previously 20), all independently written for Premiere with valid prerequisite/related lesson IDs. All existing ids remain stable. Original 182 Windows shortcut, 145 effects, 91 transitions and 25 panel rows remain; matching an unrelated application's entry counts would be unjustified.
- **Portability and safety:** The same progress export schema stays backward-compatible. Import now validates every checked step, lesson, quiz index and note type/range before replacing data, and corrupted browser storage is distinct from blocked storage. Saved bookmark, quiz, notes and original checkmark IDs are unchanged.
- **Maintainability:** All newly authored reference entries are in `scripts/third_pass_library.py` and regenerated into the structured JSON/JS, Markdown and CSV representations. `MANIFEST.sha256` and standard-library verification/package scripts provide payload integrity and deterministic builds.

## Micro / software verification of the v3 reader

- Official Premiere release notes were rechecked against the dated September 26.5.2 entry. Adobe's shortcut documentation also confirms that a customized keyboard map must be inspected in **Edit > Keyboard Shortcuts**. The AE manual was never treated as evidence for Premiere-specific shortcuts, menus, effects or version features.
- The existing static validator and quality-regression script passed, and **the new Chromium regression passed 749 specific content routes**: 105 lessons, 14 stages, 30 recipes, 37 diagnostics, 13 guides and every individual entry in five catalog types (182 shortcuts, 145 effects, 91 transitions, 25 panels, 107 glossary records). Each exact entry rendered and was uniquely targetable.
- Browser interactions verified: global search into an exact Lumetri Color result; reference filter; quiz focus and answer selection; checkbox and progress state; three reading preferences; printing expands every lesson step; backward-compatible v2 JSON import; multiple malformed imports rejected without changing state; malformed writable storage vs blocked-storage fallback; export from an unsaved session; responsive 375 px and 768 px layouts; no remote network requests; and zero JavaScript page errors in the measured test.
- The repeated prior v2 Chromium smoke test also passed, including all 105 lesson routes and progress, bookmarks, note and mobile controls.
- **Important boundary:** Browser tests use the exact published local assets inlined as a same-page test harness, because this runtime blocks both `file://` and local HTTP navigation, including when attempted with Playwright. Simulated storage is not a native browser-origin persistence certificate. The site still uses only ordinary relative script/style links and no network runtime dependencies.
- All 61 extended structural checks and all 32 original qualitative-proxy checks passed after data regeneration. Following packaging, the archive-aware validator passed **66/66 checks**, while the validator in a fresh extraction passed **62/62**. The SHA-256 manifest verified **54 extracted payload files**, the ZIP held **55 files including the manifest**, CRC checking found no errors, and rebuilding the ZIP from unchanged inputs produced the **same SHA-256 digest**. This is package integrity testing, not Premiere application certification.

## Remaining risks / no false certification

These remain **open** despite the passing tests: actual Premiere 26.5.2 use on a licensed Windows machine; keyboard conflicts under installed/custom keysets; complete installed effect/parameter inventory; per-codec and GPU-accelerated encoding; VM passthrough; live cloud/AI entitlements; direct `file://` Linux and Windows browser tests; comprehensive screen-reader/WCAG review. Reference membership and Adobe documentation are not the same as executing every workflow. No source-backed command or effect was imported from After Effects merely because both applications use similar language.

**Result:** The After Effects archive contributed several valuable generic educational/software design improvements. The v3 package is materially better than v2 while preserving its Premiere-specific progression and source cautions; perfection or exhaustive native-app certification is not claimed.

---

# Independent second-pass macro, micro and software audit

**Research snapshot:** October 28, 2026. **Windows editing target:** Adobe Premiere desktop 26.5.2, confirmed in Adobe release notes last updated October 5, 2026. The user-requested October 29 research cutoff had not yet occurred. **Manual edition:** 2.0. **Disposition:** ready for offline study subject to the unverified installed-application and `file://` constraints below. An independently executed Premiere 26.5.2 Windows seat was **not** available.

## Executive findings and corrections

The original archive was not exhaustive despite passing its static build checks. This second pass was a **corrective audit**, not just a reapproval.

| Finding in original archive | Severity | Correction in edition 2.0 |
|---|---|---|
| All 42 quiz correct answers were stored at option A | High | Distributed correct options approximately evenly: 11 A, 11 B, 10 C, 10 D. Caught and removed an additional **display-layer rotation** that otherwise placed every visible correct answer last. Added regression test of displayed answer positions. |
| Several applied Stage 14 briefs depended on all preceding expert lessons | Medium | Assigned independently appropriate prerequisites for L097–L104; full capstone L105 remains integrative. |
| Generic playback verification appended to 76 exercises including non-playback subjects | Medium | Replaced universal step with 14 stage-specific observation procedures and explicitly authored critical beginner/export exercises. |
| All lessons asked readers to deliberately trigger an error, including some with destructive implications | High | Reworded 105 review tests as safe thought experiments plus reversible practice; original media must remain intact. |
| Technical deep dives confused L083 preview rendering with codec/container and L085 codec families with preview rendering | High | Moved explanations to their correct lessons; added a distinct container/codec discussion to L084. |
| The effect list was mainly uncertain older names and lacked new categorized releases | High | Expanded to **145 effects**: Adobe 26.0 active family, Legacy, Obsolete, Removed, later 26.2–26.5 replacements, audio reference, unresolved entries. Added explanatory purpose text for formerly blank/generic active rows; this is **not** a claim that the installed 26.5.2 Effects panel was inspected. |
| Transition database lacked current 26.0 reference families | Medium | Expanded to **91 transitions** with documented family and migration status; distinguish legacy and removed entries. |
| 123 shortcuts only; missing official Windows panel/navigation entries | Medium | **182** documented rows, including Adobe’s January 7, 2026 default Windows table and distinct playback documentation. Scope/focus noted. Unknown or blank commands were **not** guessed. |
| Search indexed a missing `exercise` property instead of lesson steps | Medium | Search now indexes lesson step text, concepts, deeper explanations and Windows UI descriptions. |
| Glossary was not strictly alphabetized, and many added effects lacked meaningful categories/descriptions | Medium | Alphabetized glossary; mapped active video effects to Adobe's published panel families; improved individual descriptions. |
| Short research guides omitted detailed status/keyboard and production QC procedures | Medium | Expanded from 9 to **13** field guides, including effect migration, shortcut practice, QC pipeline and verification protocols. |

## Macro educational architecture — 14-stage review

| Stage | Reason for placement | Audited competence target |
|---|---|---|
| 1. First principles | Introduces source files, sequences, frames and the Windows application before operations | Paper timeline and correct frame rollover |
| 2. Project/media | Teaches import references, folder stability, proxies and formats before editing | Find, relink and organize stable source media |
| 3. Source → timeline | Separates Source/Program Monitor, patching, targeting and basic insert/overwrite | Produce a first cut and inspect duration |
| 4. Precision | Requires source/sequence mental model before trims or speed effects | Distinguish ripple/roll/slip/slide, handles and total duration |
| 5. Story | Builds editorial judgment only after stable manipulation | Explain why shots, reaction cuts, J/L edits and rhythm serve a story |
| 6. Audio | Introduces dBFS, gain, channel, mix, LUFS, effects and acceptance | Listen with matched levels and inspect measured output |
| 7. Visual effects/motion | Teaches keyframes and parameters after basic timeline | Compare bypass, effect order, masking and motion |
| 8. Color | Explains transforms, scopes and Rec.709 before creative look | Normalize sources and independently QC output color |
| 9. Graphics/captions | Uses current Properties-oriented editing and exported caption checks | Produce clear branded title, transcript and subtitle outputs |
| 10. Advanced media | Depends on sync, trim, audio and established media organization | Multicam/proxy/Productions handoff with originals preserved |
| 11. Assisted/AI | Separates stable features from Beta, service terms and consent | Evaluate automation critically and record cloud/credit dependencies |
| 12. Export | Builds on sequence, color and mix; distinguishes previews from final streams | Produce verified delivery master and receiver-compatible file |
| 13. Maintenance | Introduces reversible diagnostics after understanding the workflow | Diagnose cache/GPU/VM/relink/codec issues without harming originals |
| 14. Applied practice | Independent projects reuse selected prerequisites; capstone integrates all | Deliver editable archive, exported video, captions and QC evidence |

**Graph check:** 105 lesson IDs are unique and ordered, every prerequisite points backward to an existing lesson, every lesson belongs to exactly one stage, and every stage has its own quiz and practical challenge. The first basic export does not require advanced lessons. There are still judgment-dependent curriculum questions a program cannot settle (for example, whether a particular learner needs more practice with audio or Log workflows).

## Micro-level factual and technical review

**Release and feature status.** Adobe’s 26.5.2 dated release note is used as the patch anchor. New graphics/Properties workflows, Paper Edit, Generative Media, Object Mask and service-dependent automation are discussed with release limits. Beta/upcoming functionality and deprecated UI are isolated in an appendix. Features that use Adobe services can require internet access, credits, licensed account permissions or additional applications; the website's offline operation must not be conflated with those prerequisites.

**Shortcuts (182 rows).** Primary comparison source: [Adobe Windows default keyboard shortcuts](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html), dated **January 7, 2026**; playback J/K/L/Space separately documented by Adobe. The table includes menu shortcuts, project/timeline/panel-specific actions, workspaces, graphics, markers, captions, audio controls and navigation. It explicitly distinguishes context conflicts (for example `Ctrl+L`, `Ctrl+R`, `Backspace` and `Shift+O`), default versus user-custom mappings and 26.5.2 seat verification. Adobe's scraped table displays the **Maximize Frame** key as an incomplete blank; no key was fabricated for it. Some Adobe text describes graphic-position nudges as “frames”; the guide flags that wording instead of converting a spatial control into a temporal claim. **No actual presses against installed Windows Premiere were tested.**

**Effects and transitions.** Primary source: [Adobe’s 26.0 effect/transition migration table](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html), last updated February 25, 2026; supplemented by modern effect, audio effect and 26.2–26.5 release documents. 145 entries consist of **107 video and 38 audio**; 91 transition entries are separately classified. Counts by effect verification label in this build: **87** listed as active in the 26.0 video taxonomy; **7** documented 26.2–26.5 replacements; **5** Legacy; **2** Obsolete; **3** Removed; **29** named in Adobe's current audio effects reference with exact Premiere controls untested; **9** audio names not conclusively established; **2** unresolved video names; **1** modern effect with exact label requiring installed confirmation. The audio reference includes text referring to related Adobe audio workflows, so membership in that page is **not** equivalent to test evidence of a specific native Premiere 26.5.2 processor. Family-level controls or source characteristics are sometimes provided instead of invented precision. Entries explicitly marked Removed must not be treated as executable modern steps. The catalog cannot honestly be certified as a complete installed-panel inventory without running Premiere and comparing exact controls/plugins.

**High-risk conceptual distinctions reviewed:** project reference versus source file versus clip instance; source patching versus timeline targeting; insert versus overwrite; ripple versus rolling; slip versus slide; source gain versus instance automation versus track fader; dBFS versus LUFS/true peak; input color transform versus creative LUT; Log/SDR/HDR and monitor color-management paths; preview render versus media export; codec versus container; constant versus variable frame rate and bitrate; drop-frame label numbering versus video frame loss; proxy representation versus camera master; sequence settings versus delivery settings. The guides contain deeper examples and test protocols. These checks are source-level review, not 105 independent live application trials.

**Practical coverage:** Every lesson has a named objective, explicit prerequisite, conceptual model, Windows work location, structured steps, expected result, diagnostic advice, mastery criterion, links, additional deep explanation and safe challenge. Synthetic MP4/WAV material supports editor basics; interviews, captions and dialogue exercises may require **user-recorded authorized footage**, not purchased commercial media. Stage 14 ends in a quality-control-driven, relinkable project and externally playable deliverables.

## Reference and website architecture

- The same structured course database generates the offline JavaScript data, CSV reference sheets, Markdown edition and stage graph. The 13 Markdown field guides are bundled into JavaScript for `file://`-friendly use without `fetch()` or module imports.
- The website has stage progress, collapsible navigation, searchable content, bookmarks, saved notes, quizzes, light/dark theme, previous/next navigation, keyboard skip link, responsive layout, diagrams and JSON progress transfer.
- Browser storage may not persist under every `file://` policy. Manual JSON export/import is the supported cross-machine workflow; no sync is claimed. Imported progress is a data file and is size-limited to 2 MB.
- The reference database has 182 shortcut entries, 145 effects, 91 transitions, 25 panels/tools, 59 alphabetized glossary entries, 20 recipes and 20 symptom diagnoses. These are **curated educational catalogs**, not a claim of all possible third-party plugins or every future UI command.

## Tests executed and outcomes

| Gate | Method | Result | Boundary |
|---|---|---|---|
| Static integrity | `python scripts/validate.py` | **51/51 passed** | Identifiers, prerequisites, JSON/JS/CSV/Markdown parity, sources, assets and local architecture |
| Second-pass regression | `python scripts/deep_review.py` | **32/32 passed** | Exercises, no unsafe boilerplate, quiz answer balance, terminology placement, glossary, ref classes, local Markdown paths, `ffprobe` sample-media decoding |
| Browser interactions | Playwright with headless Linux Chromium | **Passed** | All 105 lesson routes; search, reference filtering, editing diagrams, quiz correctness positions, completion, notes, bookmarks, light/dark, export/import, mobile sidebar; no JavaScript page errors |
| JavaScript syntax | `node --check app.js` | **Passed** | Syntax only, not a native application or browser-origin test |
| Original practice media | `ffprobe` on 3 MP4 + 2 WAV files | **Passed** | Container/stream readability only, not import into Premiere |
| Direct opening from `file://` | Restricted Linux browser environment | **Not executed** | Local environment blocked direct navigation; reader relies only on conventional relative bundled `<script>` and stylesheet links, but cross-platform origin policies remain unproven |
| Native Windows browser or Adobe Premiere | No Windows environment supplied | **Not executed** | Shortcut execution, exact menu labels, GPU/VM, effects controls and encoder availability require an installed-seat check |
| Archive CRC, traversal, extraction | Python ZIP integrity and fresh extraction | **Passed: CRC, safe paths, fresh extraction, embedded validator** | Record result with release ZIP before sharing |

## Outstanding risks — disclosed, not concealed

1. **Application-side verification:** Every shortcut and effect cannot be certified to exist or work identically in a specific Premiere 26.5.2 installation, customized keyboard set, hardware configuration or licensed account without operating the program. The table is backed by Adobe sources, but this is a documentation audit, not a full application test.
2. **`file://` origin restrictions:** The local asset architecture is offline-compatible by design; this environment's direct-file browser policy prevented definitive real Linux and Windows double-click tests. Local storage persistence is particularly browser-specific.
3. **Effects encyclopedia depth:** The reference now distinguishes migration and has useful descriptions, but effect-specific parameter ranges, every transition variant, third-party entitlements and all obscure legacy render paths are not independently inspected in Premiere.
4. **Educational depth:** All 105 lessons have executable learning structure and practical checks, but not every individual exercise can be guaranteed reproducible across every codec, workstation, camera, cloud service or VM. Refer to the release notes and version-audit caveats if an installed UI differs.
5. **Online AI and dynamic pricing/limits:** Accounts, credits and model options are external services, not guarantees tied to the desktop patch.
6. **Accessibility:** Keyboard focus/skip and responsive smoke testing passed; comprehensive screen-reader testing and independent WCAG conformance evaluation were not performed.

**Audit conclusion:** Corrected substantive assessment, curriculum, reference, lesson-safety and search defects; automated integrity and browser-interaction tests passed. The corrected package is suitable for structured offline learning and documented consultation, but the unresolved native-application and browser-origin checks prevent claiming exhaustive real-world verification of every factual or operational detail.
