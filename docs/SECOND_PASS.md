# Comprehensive second-pass review

Reviewed 28 October 2026, starting from clean commit `ebbea2e`. This is the current integration review; [AUDIT.md](AUDIT.md) retains the earlier pass. The second pass found real defects despite the first pass’s successful route sweep. Those earlier results established route reachability, not complete correctness of every state transition.

## Findings and changes

| Area | Before | Corrected behavior and evidence |
|---|---|---|
| One-pass builds | Shared indexes read AE JSON before its source builder ran. An authored change could appear in AE immediately and reach shared search only on a second build. | AE is rebuilt before its JSON is read for shared indexes. A copied-source fixture changes an actual lesson paragraph and verifies new JSON, HTML and search after one build, then verifies an identical repeat build. |
| Reading preferences | Initialization reapplied global preferences over each saved reader state. Individual changes and imported preferences could revert after reload. | Existing reader state retains its own settings. Explicit Apply to all still updates every reader; global settings initialize a reader with no library snapshot. Divergent settings survive bundle import and reload. |
| Fresh backups | Export depended on asynchronously cached notifications. | Export asks each reader for its current state and receives an explicit reply before creating the backup. A fixture suppresses automatic notifications and still exports the latest completion. |
| Import recovery | Backup actions could overlap, rollback used cached state, and restored routes were not sent to readers. | Backup actions serialize; pre-import state is freshly read; replacement and rollback restore both state and route. A deliberately failing third reader demonstrates recovery after another reader has already changed. Cancellation preserves the current record. |
| Back/Forward | Late child messages could undo a newer parent request. | Each request carries a per-reader navigation sequence. Stale replies and delayed commands are ignored. A fixture deliberately delays the next-lesson command until after Back and verifies both URLs remain on the previous lesson. |
| Failed persistence | A later library-store failure was silent. On reload an older aggregate could replace newer successfully saved reader progress. | Write failures update visible status and request an export. A small, separate modification-time marker lets initialization retain the newer saved record. A fixture fails only aggregate writes, saves a new native completion, reloads and verifies the completion remains. Existing backup/state schemas are unchanged. |
| Reader recovery | A timed-out reader left a permanently rejected cached promise; its late error could replace a newer library page. | Failed, uninitialized frames are removed so opening can retry. Rendering checks its generation before writing errors or content. A timeout fixture returns to the chooser before failure, then successfully reopens the reader. |
| Query/history consistency | The empty search URL could retain an earlier query. A delayed query update could run after navigating away. | Query text is derived from the current URL; route changes cancel pending URL updates. Empty-query and navigate-away regressions pass. Search keyboard focus waits for the index/render to finish. |
| Standalone links | Programmatic native search/filter routes updated the root URL without updating Open standalone. | The standalone link follows acknowledged reader routes, including AE’s replaceState-based search. |
| Skip navigation | Focusing only the frame did not focus its reading content; focusing only the child content was insufficient in Firefox. | The parent activates the frame, then the bridge focuses its main element. Keyboard activation is exercised in both browsers. |
| Search coverage | The 42 Premiere quiz questions and six AE readiness-challenge paragraphs were absent from shared search. Photoshop version results opened the whole table. | All 48 teaching units are indexed. Premiere quizzes attach to their stage; the AE learning-path record includes all stages/challenges. Photoshop version routes focus/highlight the specific row. The library now has 2,423 records, with the original 680 shortcut records. |
| Narrow screens | The root navigation overflowed a 320 px viewport: measured document width was 368 px. | Narrow navigation spacing and text wrapping were corrected. Tests cover 320, 375 and 768 px, including the three native readers and large/contrast/focused reading. |
| Validation depth | Checksums could be fresh even with stale shared indexes. Photoshop CSV checks primarily checked counts. | Validation regenerates expected catalogs from canonical data, verifies complete shared bundles, checks every quiz/challenge and compares every Photoshop CSV field. Browser sweeps check the expected entry title and exact targets as well as route existence. |
| Development files | File traversal entered ignored development trees; archive detection could mistake development fixtures for shipped archives. | Tree walking prunes Git, environments, dependencies, caches and test artifacts. Directory symlinks are not treated as regular payload files. A fixture includes ignored archives and a directory symlink. |

## Preservation and source review

All 137 original file paths remain. **118 files outside 19 explicit integration exceptions remain byte-identical to the supplied originals.** The additional exception in this pass is Photoshop’s stylesheet for the focused version-status row. The canonical teaching JSON, AE authored teaching source/seeds, original authoring definitions, full Markdown editions, curricula, CSV exports, research/audit records and practice assets were not rewritten. The original input folders were not edited.

Every Python source file compiles, and every JavaScript reader/data bundle passes Node’s syntax check. The native structure validators check IDs, stage membership, prerequisites, references, quiz answer ranges, source relationships and export consistency. Photoshop’s independent content audit passes 55/55 checks; Premiere’s independent review passes 32/32 checks. These are structural/qualitative checks, not semantic proof of every Adobe statement.

A targeted live primary-source review corroborated the existing release targets: [Photoshop 27.11 release notes](https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html), [Premiere 26.5.2 release notes](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html), and [After Effects 26.5 release notes](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html). Sample Windows shortcut checks also agree with [Premiere’s default table](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html) and [After Effects’ shortcut reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html). This did not recertify every rolling Adobe page or every installed effect parameter. No unverified substantive correction was inserted into researched teaching text.

All local Markdown file links resolve. Every bundled SVG parses. The six practice PNGs decode in the original image audit, and Photoshop’s overview images load in both browser regression runs. ffprobe confirms all three supplied videos are H.264, 960×540, 25 fps, 175 frames / seven seconds, with no audio stream. The two Premiere WAVs are mono 48 kHz/16-bit PCM with 384,000 frames each; AE’s pulse is the same PCM layout with 192,000 frames. These match the supplied asset descriptions. This verifies the supplied media, not import/render results in Adobe.

## Verification record

Environment: Linux, Python 3.15.1, Node 26.12.1, Chromium 156.0.8078.47, Playwright 1.64.1 and its Firefox 157.0. Browser networking is disabled. Default Firefox navigation limits are retained; automated sweeps are paced within them.

| Check | Result |
|---|---|
| Core validation, manifests, exact source/index/CSV comparisons | Pass |
| Native AE structural regression | 29/29 pass |
| Build freshness/determinism/traversal regressions | 3/3 pass |
| Focused second-pass browser regressions | Chromium and Firefox pass; no JS errors, HTTP(S) requests or failed assets |
| Exhaustive combined reader sweep | Chromium and Firefox each 2,423/2,423 pass; expected-title/target checks and 320/375/768 px layouts included |
| Photoshop extended interactions | 16/16 grouped assertions pass |
| Premiere comparative browser regression | 749/749 routes and interaction checks pass |
| Native AE browser regression | Chromium and Firefox each 1,094/1,094 pass |
| All Python/JavaScript syntax and local Markdown file links | Pass |
| Native media metadata, original PNG audit and SVG parse | Pass |

The focused browser suite covers saved preferences, fresh export with delayed notifications, invalid/failed/cancelled replacement, rollback, query URLs, standalone links, keyboard focus, exact version rows, image decode, storage failure/reload, delayed navigation and timeout recovery. The main sweep adds quizzes/checks/notes/bookmarks, backup transfer, persistence, printing dispatch/styles, narrow screens and completely blocked storage. Source checksums alone are not used to assert that an interaction works.

## Efficiency and maintenance

The uncompressed entrance is about **38.8 KB**, compared with 36.2 KB in the first pass; the extra control logic handles demonstrated reliability failures. The **1,501,540-byte** full-text index and each reader still load only when needed. Snapshot notifications remain coalesced and aggregate writes remain debounced. Snapshot comparison now reuses its existing serialized state instead of serializing the whole state twice. A Node fixture with 105 notes of 20,000 characters (2,100,951 serialized bytes), 45 iterations per variant, measured median comparison work of 25.78 ms before and 12.86 ms after on this machine. This isolates serialization work; it is not a whole-reader latency or typing benchmark. Only a small timestamp marker is stored beside each reader’s existing learning record. No framework, runtime dependency, server, archive or online service was added.

Ignored development trees are pruned rather than scanned and filtered afterward. No before/after runtime speedup is claimed without comparative measurements. Repeated builds remain deterministic. New maintenance tests use a temporary copy when deliberately changing authored material, so the real course is never modified by a regression fixture.

Modification markers reconcile saved records at reader initialization, not continuously across open tabs and never across machines. Explicit imports replace state after confirmation, including when importing an older backup deliberately. Export/import is still the portable transfer path. With storage fully blocked, an open session and exported backups remain the available persistence mechanisms.

## Limits

This pass verifies the shipped reader and its integration on the tested Linux browsers, plus structural consistency, preservation and the targeted source/media checks above. It does not establish universal correctness of Adobe documentation, execute all exercises in licensed Windows Photoshop/Premiere/After Effects, test a physical printer, certify screen-reader behavior or validate every GPU-pass-through environment. There was no direct Windows browser execution. Unknown installed plug-ins, customized shortcut presets and service/account requirements remain governed by the original manuals’ scope notes.

The tests found and corrected concrete defects; the project is not described as mathematically perfect or completely certified. The remaining product-validation boundary is explicit rather than hidden behind a successful route count.
