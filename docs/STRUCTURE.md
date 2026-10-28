# Structural analysis and integration contract

## Supplied projects

The source folders contained 137 files (47 Photoshop, 55 Premiere, 35 After Effects), with all original manifest entries matching their SHA-256 hashes. None of these supplied folders contained a `.git` directory or ZIP. The After Effects directory appears to be an exported working tree rather than a Git checkout. The original After Effects builder unconditionally created an archive containing its own sources, generated outputs, assets and tests; this explains the redundant ZIP in builds even though no ZIP existed in the supplied folder at inspection.

| Area | Photoshop | Premiere Pro | After Effects |
|---|---|---|---|
| Runtime | Inline data, CSS and reader; adjacent diagrams/images | Adjacent classic scripts and CSS | Inline data, CSS and reader; adjacent samples |
| Course | 12 stages / 75 lessons; independent completion and graded lesson quizzes | 14 stages / 105 lessons; practice checks, notes, completion, stage quizzes | 6 stages / 40 lessons; action-level progress, 100 deep topics, separate quiz |
| References | Stable IDs, dedicated entry pages; shortcuts previously opened whole catalog | Compound natural keys and exact catalog targets | Stable IDs, catalog target highlighting; glossary uses term keys |
| Reading | Light/dark, larger text, contrast, one-step reading | Light/dark, larger text, contrast, next-unchecked-step reading | Light, larger text, contrast, one-step reading |
| Persistence | Own strict versioned backup validator and storage key | Own strict backup validator; retains v1 format | Current and legacy edition validators; semantic reset of changed old actions |
| Content sources | Final reviewed JSON + author/reference/enrichment scripts | Final reviewed JSON + author/enrichment scripts + complete guide Markdown/HTML bundle | `content.py` + curated JSON seeds; deterministic builder |
| Portable exports | Full Markdown, curriculum, 6 CSVs, provenance and audit records | Full Markdown, curriculum, CSVs, 13 Markdown guides, provenance and audits | Full Markdown, JSON, 2 CSVs, provenance and audits |

The differences serve the curricula. Forcing all of them into one lesson schema would either discard specialist detail or require a large translation layer. The strongest common capabilities were already present in all three after their earlier comparative audits: focused reading, progress backups, offline references, source boundaries and practice material. Those were preserved, then connected by shared navigation, a larger search index and a library backup.

## Final architecture

The root is the sole normal entrance and Git project. A lightweight library controller owns app selection, URL history, search, key comparisons and library backups. It loads a reader only when opened. Each reader remains mounted after first use, so switching apps retains reading state even when local storage is unavailable. Unopened readers load in the background only when needed for a complete backup or import.

Readers run in ordinary local iframes. The shared bridge uses `postMessage`, checking the actual parent/child window, rather than reading another document’s DOM or storage. This matters because Firefox and Chromium apply different local-file origin rules. There is no `fetch`, JavaScript module loader, service worker or server assumption. Reader-to-library messages contain progress, modification time, navigation sequence, route and storage status, never the whole teaching database. There is one shared bridge implementation: it is embedded at build time into the self-contained readers and loaded directly by Premiere.

The root URL carries the selected manual and its native route (`#read/photoshop/lesson/s01l01`, for example). Internal reader links request parent navigation; the bridge replaces the child’s fragment instead of adding another joint history entry. Existing native routers still render their pages. Each parent request increments a per-reader navigation sequence, and stale replies or delayed commands cannot undo a newer Back/Forward request. Async page rendering also checks its generation before changing the visible page. The shared app selector resumes the last page; **Library** always returns to a choice. Direct entry links work after reloading or copying the URL. Root search has its own query URL.

Full-text search is derived from every included lesson, stage assignment, topic, reference, recipe, diagnostic and Premiere field guide. It keeps app IDs and native routes, ranks title matches first, counts all matches and paginates rendering. Search includes Premiere’s stage quizzes and the AE stage challenges as well as the main reference families. Search normalizes text once when its index is loaded. It does not load at the chooser. Photoshop now has dedicated numeric shortcut routes so both its own search and the combined search open the precise shortcut. Photoshop version-status results now highlight and focus their specific table row. No shortcut or version-status substance changed.

Key comparison groups only normalized key labels, stripping spaces/backticks and ignoring case. Original commands and contexts are shown verbatim. This permits useful comparisons without claiming that a key has the same meaning in all apps. There is deliberately no automatic cross-app lesson-equivalence claim.

## Progress contract

Each reader exposes a small `ManualAdapter`: ID, home route, state getter, existing validation, state replacement, progress summary, storage status and reading preferences. Source-side save/render hooks notify the shared bridge; notifications coalesce in a microtask. Library state writes are debounced and flushed on page exit. The existing manual schemas and progress IDs are unchanged.

The library keeps a snapshot per app. The shared bridge stores a small modification-time marker beside each reader’s existing storage key. When reopening, it compares that marker with the library snapshot and uses the newer record, so an old aggregate cannot erase newer reader progress after a failed aggregate write. Existing states and backup schemas are unchanged; old undated records retain the original initialization behavior until edited. A complete backup declares the library format/schema and each app’s target version, state and last route. Existing strict validators check all three states before any replacement. Exports explicitly request fresh state from every reader. A failed replacement triggers rollback to the prior session records and routes. Import/export and global preference writes are serialized while a backup operation is pending; the UI shows persistent backup status. Invalid saved library state falls back to the reader’s own valid local record. Old single-manual backups continue through the original reader-specific import paths, including AE 25.6 migration.

Shared preferences explicitly apply large text, contrast and one-step mode to all three readers. App-specific controls and themes remain available. Saved per-app choices take precedence over initialization defaults; explicit Apply to all still updates all three readers. There is no fake overall completion percentage: Photoshop/Premiere count completed lessons; AE counts completed actions. Their summaries retain the correct units.

Storage remains browser-local. A moved folder, another browser or a standalone reader can have a different record. Export/import is the supported transfer path; it works when local storage is denied. The suite retains initialized readers in memory, not in a cloud account.

## Build and editing rules

`python3 scripts/build.py` is the project build. It uses the standard library and creates no ZIP. It does not install dependencies or contact the network.

| Material | Edit source | Result |
|---|---|---|
| Library UI/protocol | Root `index.html`, `assets/library.*`, `assets/bridge.js` | Shared entrance and reader integration |
| Photoshop teaching | `manuals/photoshop/content/content.json` | Browser data and root search are compiled from this reviewed snapshot |
| Photoshop reader | `manuals/photoshop/assets/app.js`, `assets/style.css`, `web/index.template.html` | Inlined `manuals/photoshop/index.html` |
| Premiere teaching | `manuals/premiere/data/course.json`, reviewed `data/guides.json` and matching `guides/*.md` | Adjacent browser data bundles and root search |
| Premiere reader | `manuals/premiere/app.js`, `style.css`, `index.html` | Direct local reader; no inlining needed |
| AE teaching | `manuals/after-effects/content.py`, `data/*_seed.json` | Original deterministic builder generates JSON, HTML, Markdown and CSVs |
| AE reader | `manuals/after-effects/web/*` | Embedded reader and shared bridge |

The Photoshop/Premiere historical authoring, enrichment and packaging scripts are retained for provenance and deliberate research maintenance. They can overwrite reviewed snapshots, README/audit records, text exports or media. They are not part of the routine library build. If deliberately updating teaching content, synchronize Markdown/CSV exports and author definitions, review the substantive diff, then update the content-preservation baseline only for the reviewed changes. Do not blindly run the enrichment scripts as an installation step.

`docs/original-files.json` records the initial hashes. The integration validator protects teaching sources, structured snapshots, seeds, Markdown editions, CSV exports, research/audit documents and sample media against accidental changes. Its explicit integration exception list covers only reader code, templates, build/validation/test updates and per-manual integration README notes. Existing HTML/data bundles may change byte formatting while their decoded JSON must still equal the preserved canonical snapshots. Generated root indexes must rebuild identically.

The old AE archive generator and archive-dependent tests were removed; they were replaced with no-archive and deterministic-output tests. The shared indexes are generated only after the AE authored source has been rebuilt, so one build updates both the reader and cross-app search. Validation independently regenerates expected catalogs from current data and compares them to the shipped bundles; checksums alone are not treated as proof of source consistency. Development directories are pruned during file traversal. Per-manual manifests and the root manifest are regenerated at the end of a successful library build. The root manifest includes the nested manifests, excludes Git metadata, development caches and itself, and detects unexpected project files as well as changed files.

Historical per-manual audit documents describe earlier editions and earlier testing environments. The root integration audit is the current source for this combined project’s verification evidence. No source folder was edited in place, and no existing progress was silently copied from another path/browser.

The current second-pass findings and evidence are in [SECOND_PASS.md](SECOND_PASS.md). The original integration report remains as a record of the first pass.
