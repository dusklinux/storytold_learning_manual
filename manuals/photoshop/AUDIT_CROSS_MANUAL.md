# Cross-manual comparative audit — Photoshop Field Manual 1.2.0

**Audit performed:** October 28, 2026. **Target:** Photoshop 2026 desktop **27.11 on Windows**, English default keyboard. **Reader target:** Linux and Windows offline browsers. **Reference inspected:** the user-supplied `ae_manual-main.zip` After Effects 26.5 manual. This is an independent comparison of the educational and software-design patterns, not a transfer of After Effects content or an Adobe certification.

## Conclusion

**A selective upgrade was warranted.** The Photoshop course already follows a more granular Photoshop-specific beginner-to-expert curriculum (12 stages / 75 lessons), with stable references and source-based generation. Replacing it with After Effects' six-stage organization, 40 lessons or domain-specific effects/shortcuts would be inappropriate. However, the supplied project demonstrated materially better backup hygiene, learner reading preferences, single-file delivery, maintenance handoff, checksum packaging and stronger edge-case testing. Those patterns were adapted, implemented, and regression-tested.

The entire Photoshop domain data collection (stages, lessons, tools, filters, shortcuts, glossary, troubleshooting, recipes, version changes and sources) compares **equal field-for-field to edition 1.1.0**. Only the edition metadata and the reader/packaging/audit implementation have changed. No After Effects tool, effect, keyboard command, concept explanation or application-specific instruction was imported.

## MACRO — structure, pedagogy and coverage

| Dimension | Photoshop finding | Reference-manual pattern | Decision / action |
|---|---|---|---|
| Stage progression | 12 dependency-ordered Photoshop stages, 75 lessons, 12 synthesis projects | After Effects has six stages and 40 guided chapters | **Retain Photoshop structure.** Different creative applications need different learning prerequisites. |
| Lesson substance | Objectives, prerequisites, concepts, precise Windows locations, at least four steps, expected outcomes, causes, practice, rubrics, quizzes and links | After Effects separates 100 deep explanatory topics from 40 walkthroughs | Retain Photoshop lesson/reference division. Deeper long-form dialog-by-dialog coverage is a known future editorial enhancement, not something to duplicate from unrelated topics. |
| References | 71 tools, 81 filter/effect rows, 112 context-qualified Windows shortcut entries, 155 glossary items, 30 troubleshooting entries, 40 recipes | After Effects has 300 AE effects, 386 AE shortcut/gesture rows, 67 troubleshooting cases, 34 recipes | **Do not copy counts or AE shortcuts.** Photoshop-specific reference correctness matters more than numerical parity. |
| Version discipline | 27.11 baseline; Beta, conditional AI and removed filters separated | AE manual explicitly distinguishes 26.5 stable and Beta | Retained Photoshop version policy and prior evidence. |
| Reader portability | Previously loaded local JavaScript files with no runtime network requests | AE embeds its code and data into a single HTML document | **Adopted single self-contained `index.html`** for data/style/app; practice images and diagrams remain separately included. |
| Progress transfers | Previous import validated outer schema but silently filtered unknown IDs and invalid checklist keys | AE validates imports before replacing state | **Adopted strict, all-or-nothing validation, exact known IDs, matching Photoshop version and edition allowlist, explicit replacement confirmation.** |
| Existing learner data | Persistent key `photoshop-manual-progress-v1`, schema 1 | AE has explicit edition migration contract | Preserved storage key and schema. Editions 1.0.0/1.1.0/1.2.0 targeting 27.11 can be imported; existing stored records are normalized conservatively. |
| Reading comfort | Themes and responsive layout | AE has large-text, high-contrast and one-step view | **Added all three**, plus full-step print rendering and focus retention on key controls. |
| Reproducible build | Shared Python authoring source, CSV/Markdown/JS exports, validation | AE has handoff, tests, checksum manifest, reproducible ZIP | **Added** `MAINTENANCE.md`, `scripts/check_manifest.py`, `scripts/package.py`, and expanded offline-browser tests. |
| Source traceability | 33 dated Photoshop source records and prior source-by-claim second-pass audit | AE has source notes attached to individual topics | Did not fabricate per-entry citations. Granular documentation coverage remains a separate source-verification task. |
| Practice assets | Six original raster exercises, plus simple offline diagrams | AE includes WAV, SVG, JSON and CSV for AE tasks | Kept Photoshop-specific assets. Real portraits, camera RAWs and licensed photographic assets are not replaceable with AE samples. |

## MICRO — code, data and behavior

### Findings fixed in this edition

1. **Progress import could silently discard invalid records.** Previously, `normalize()` dropped unknown lesson IDs, bookmarks and checklist entries on import. This could misleadingly report a successful transfer while losing evidence. The new `validateBackup()` rejects malformed records without replacing the current state. Valid backups require the Photoshop 27.11 target and a compatible edition. Import asks for confirmation.
2. **Bookmark validation was permissive.** It accepted routes merely starting with certain prefixes. The new reader checks against exact, existing lesson/stage/reference routes.
3. **Checklist validation was too permissive.** Previously it accepted any `lesson-id:index` key for a real lesson. Now it checks each actual checklist item's index.
4. **Reading accessibility omitted larger text, stronger contrast and paced steps.** These modes have been implemented and exported in progress files; the one-step view is expanded in print CSS.
5. **Inline-script initialization needed deliberate ordering.** During the build upgrade, embedding application scripts into the document head would have executed before the application root existed. The generator was corrected to insert them at the end of the body, and the actual final HTML is now directly tested.
6. **One-step CSS conflicted with the list's author-level display rules.** Hidden steps now explicitly use `display:none` on screen and `display:list-item` in print. A live Chromium regression proves both behaviors.
7. **Malformed hash paths could throw URI decoder errors.** Route decoding now fails safely to the not-found view instead of crashing navigation.
8. **Keyboard focus could be lost when rerendering after actions.** Progress, quiz, bookmark, theme, step and reading-preference controls now restore focus where appropriate.
9. **No full-bundle checksum verifier.** Added `MANIFEST.sha256`, an integrity-check command, a deterministic packager and extraction verification.

### Data integrity verified

- Structural validator: **passed**, checking all 75 lessons, 12 stages, references, prerequisites, quizzes, six CSV files and JSON/JavaScript/Markdown consistency.
- Additional second-pass validator: **55/55 checks passed**. It covers navigation, source order, shortcut collisions, filter locations and sample assets.
- Unchanged educational dataset: fields `stages`, `lessons`, `tools`, `filters`, `shortcuts`, `glossary`, `troubleshooting`, `recipes`, `changes` and `sources` are **byte-equivalent after JSON parsing** to the supplied 1.1.0 Photoshop ZIP. (Only `manifest.edition` changes.)
- JavaScript source passed `node --check`; self-contained HTML includes the exact generated CSS, content and application code and retains the text-only `ALL_CONTENT.md` fallback.
- Original Chromium interaction suite: **20 tests passed** under inline offline simulation.
- Extended Chromium suite: **16 groups passed**, encompassing all 12 stage routes, all 75 lesson routes, **377** reference detail routes, bad URLs, reading modes, print, checkboxes, quizzes, valid and invalid imports, old backups, search, blocked storage, mobile layouts and no unexpected HTTP requests or runtime errors.
- The output ZIP is built from sorted payload files with fixed timestamps; its SHA-256 manifest covers all shipped project files except itself. ZIP integrity and extraction checksum verification are conducted after packaging.

## Remaining uncertainties and explicit limits

- **No live Photoshop 27.11 GUI test was performed.** This comparison audits the software manual and carries forward edition 1.1's Adobe-source checking; it does not independently certify every tool location, keyboard binding, filter control, entitlement, AI model, GPU/VM behavior or written Photoshop procedure. A completely clean Windows Photoshop install with the shortcut editor would be needed to check every contextual binding.
- **Native `file://` navigation remains untestable in the managed publishing Chromium** (`ERR_BLOCKED_BY_ADMINISTRATOR`). Both suites execute actual JavaScript in Chromium with networking offline; the expanded suite executes the *generated, self-contained* HTML. This is stronger evidence for independence from local-script resolution, **not** a claim of unrestricted Windows/Linux browser interoperability. Local storage persistence across a real `file://` restart was likewise not demonstrated.
- Synthetic practice media cannot substitute for realistic portrait/RAW/print assets. Version-dependent cloud/partner AI entitlements and licensed Photoshop runtime require independent live verification.
- The 75 lessons are generally concise modules, not exhaustive control-by-control chapters. Filter and shortcut references are curated and context-qualified rather than a raw full software registry. This limitation predates the comparison and is not disguised by reference-manual entry counts.
- Individual Photoshop technical entries are not all annotated with direct per-entry Adobe source IDs; the dated `SOURCES.md` and earlier `AUDIT_SECOND_PASS.md` maintain the research provenance where established. No unverified provenance links were added merely to increase citation counts.
- Further real-world accessibility testing with assistive technology, actual Windows/Firefox local-file startup, native Photoshop lessons and GPU/print hardware could not be performed here.

## Quality assessment

**Go for offline self-study and curated reference use**, subject to these documented limitations. The reference comparison identified worthwhile improvements, which were actually implemented. The updated reader now has stronger safety and operational correctness than edition 1.1.0; the existing lesson content and shortcut references were deliberately left untouched rather than being silently altered with After Effects material.
