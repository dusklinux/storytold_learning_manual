# Integration audit — Dusky Adobe Manual

> Historical first-pass report. See [SECOND_PASS.md](SECOND_PASS.md) for the current review, later defects found, fixes and validation.

Review date: 28 October 2026. This report covers the combined reader, structure, preservation and offline behavior. The supplied manuals’ Adobe research and earlier audits are retained in their own directories; they are historical evidence, not a claim that this integration reran every Adobe exercise.

## Macro review

The project has one normal entrance, one Git repository, one shared navigation/search/backup layer and three specialist curricula. Opening the root file asks which app to read. Returning to the library or switching apps does not require browsing folders. A direct lesson URL selects the right reader. Each manual retains its meaningful differences: Photoshop image exercises, Premiere editing geometry/field guides and notes, AE action progress, topics, recipes, expression/data samples and legacy progress migration.

No teaching schema was flattened into a lowest-common-denominator lesson format. All original research sources, full text editions, curricula, CSV exports, practice media, authoring definitions and audit records remain. Canonical teaching files are checked against the original SHA-256 baseline. No substantive Adobe instruction was rewritten during integration, and matching shortcut labels do not create unsupported equivalence claims.

The full project remains a plain local folder. There are no runtime packages, remote resources, modules, service workers, API keys, accounts or server requirements. Root search is an adjacent classic script, loaded on demand. The message bridge avoids assumptions about shared origins or shared storage between local files. The supplied AE folder had no actual ZIP or `.git`; its old builder unconditionally generated a redundant self-containing ZIP. That generator and archive-dependent tests were removed. There are zero nested archives and zero nested Git directories in the combined project.

The app chooser and per-reader wrappers were visually inspected at desktop and narrow widths. The specialist readers deliberately retain their existing presentation, with one persistent library header and consistent switching/progress controls. This gives a single project without putting research-specific reader rewrites at risk.

## Micro review

| Area | What was checked | Result |
|---|---|---|
| Content preservation | All 137 original paths remain; 119 files outside 18 explicit reader/build/test/documentation exceptions hash-match the source. JSON, seeds, CSVs, complete Markdown, source definitions, practice assets and historical research/audits are unchanged. | Pass |
| Curriculum | Existing Photoshop validator; Premiere’s 62 structural checks; AE’s 29 unit tests. Unique IDs, stage membership, prerequisites, lesson links, topic/recipe relations, quiz answer bounds and exported formats. | Pass |
| Generated reader data | Photoshop JSON equals browser bundle; Premiere JSON equals data/guide bundles; AE authored data equals JSON and embedded HTML. | Pass |
| Search | 2,422 records; all 220 lessons, 100 AE topics, 13 complete Premiere field guides, stages/assignments and reference records. App/type filters, title ranking, pagination, empty results and exact entry links. | Pass |
| Keyboard comparison | All 680 original records; exact normalized key grouping; original app/action/context shown; precise shortcut links. | Pass |
| URL/history | Initial chooser, direct entry, internal links, one Back/Forward step per native link, app resume and return to chooser. Child-route messages cannot overwrite a newer parent request while it is pending. | Pass |
| Progress | Completion/checks/bookmarks/notes, all-reader preferences, persistence after reload, export/download, valid replacement and rejection before partial replacement. Original format validators remain authoritative. | Pass |
| Offline/storage | Real `file://` sessions with networking disabled. Storage-denied sessions retain initialized readers across app switches and export all three records. | Pass |
| Print | Dedicated message to the active reader; Ctrl+P forwarding; native print styles expand focused actions. Browser-menu printing of the outer library remains library-page printing. | Pass for forwarding/styles; physical printer output not tested |
| Responsive/accessibility | 375 and 768 px suite layouts, native large-text/contrast/focused reading, keyboard controls, focusable skip controls and correctly named frames. | Pass for automated/visual checks; no screen-reader certification |
| Build | Repeated dependency-free build produces identical payload hashes. Root/per-manual manifests include all shipped files and detect unexpected files. No archive creation. | Pass |
| Git structure | One root repository targeting `dusklinux/dusky_adobe_manual`; no nested repository metadata or archives. | Pass |

## Browser evidence

Test environment: Linux, Python 3.15.1, Node 26.12.1, system Chromium 156.0.8078.47, Playwright 1.64.1 and its Firefox 157.0. These are observed test versions, not runtime requirements for reading. No Windows Adobe installation was available.

- Combined Chromium sweep: **2,422/2,422** emitted catalog routes through the actual parent/reader message protocol; zero JavaScript errors and zero HTTP(S) requests. Interaction coverage includes Back/Forward, switching, global search with full guide text, exact shortcuts, key comparisons, global preferences, complete backups, rejection of a bad record, reload, focused printing, mobile widths and storage denial.
- Combined Firefox sweep: **2,422/2,422** catalog routes, the same offline integration interactions and blocked-storage checks; zero JavaScript errors and zero HTTP(S) requests. Default browser history limits were retained, with paced automation as described below.
- Original Photoshop extended suite: **16/16** grouped interaction assertions, including all lesson/stage/detail routes, quizzes, checklist/completion, old backups, malformed imports, reading/print behavior and mobile widths.
- Original Premiere comparative suite: **749/749** content routes, exact references, printing, preferences, progress compatibility, malformed/corrupt/blocked storage and responsive behavior; zero remote requests and JavaScript errors.
- Native AE browser suite: **1,094/1,094** routes in Chromium and Firefox, including calculators, quiz/step focus, exact searches, legacy progress migration, corruption, storage denial, mobile layouts and print styles; zero remote requests and JavaScript errors.

A final Chromium interaction rerun also passed 333 lesson/topic/guide routes with explicit print-button/Ctrl+P forwarding and a deliberately mixed valid/invalid import that proved no partial replacement. Portability checks rebuilt the project and opened each manual in both browsers from a relocated folder with spaces in its path; a corrupt library snapshot recovered to the reader’s valid record.

The Firefox sweep initially hit the browser’s default History API rate limit when automation attempted hundreds of parent/child navigations within seconds. A focused alternating-route fixture reproduced the console error. Test navigation is now paced within the default browser limits; browser preferences are unchanged. Root search URL updates are debounced. The relevant browser behavior is documented in [Mozilla’s navigation-rate-limit report](https://bugzilla.mozilla.org/show_bug.cgi?id=1944202) and [History API rate-limit discussion](https://bugzilla.mozilla.org/show_bug.cgi?id=1963333). This is test pacing, not a compatibility path in the reader.

## Efficiency observations

The chooser loads **36,202 bytes** of uncompressed HTML, CSS, controller, metadata and icon only. It loads neither the three readers nor the 1,491,634-byte full-text index until needed. Tests assert this lazy-loading behavior. Only one frame per app is created; initialized readers are retained to preserve session progress when storage is blocked. Native UI updates are coalesced before sending snapshots; library storage writes and search URL updates are debounced. Search normalizes text once and renders results in bounded batches.

A warm repeated build took approximately **0.41 s** on this development machine, with all **152** then-present payload files byte-identical between runs. That measurement preceded the final audit file, which adds a documentation payload; it is an informational observation, not a before/after speedup or cold-start benchmark. The final documented project contains 153 checksummed payload files; a final repeat build also preserved every payload hash. No runtime speed gain is claimed without a comparative benchmark.

## Remaining limits

The tests establish offline reader behavior on the tested Linux browsers. They do not establish that Adobe’s researched instructions are correct in every installed Windows build, that a GPU-passthrough VM meets every Adobe requirement, or that every effect/shortcut exists under a custom preset. The preserved research targets are snapshots, not live release checks. No direct Windows browser execution or licensed Photoshop/Premiere/After Effects exercise execution was performed.

Local storage can be denied, isolated or cleared, and standalone readers may use different storage. Backups are the supported way to move learning records between paths, browsers and machines. Original manual-specific exports remain importable inside their own reader. A full library backup contains learning state, not Adobe projects or source media.

The optional source links need internet when explicitly followed; reader content and included assets do not. Adobe activation and cloud/service-dependent features are separate from the offline manual. Print forwarding and print CSS are exercised, but no physical printer or every browser’s print dialog was tested. Historical authoring scripts are retained for maintenance provenance and are not invoked by the normal build.
