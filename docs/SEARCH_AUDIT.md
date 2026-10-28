# Offline fuzzy-search implementation and audit

This review covers the new search interaction and its effect on the existing learning library. The researched Adobe teaching content, lesson IDs, progress schemas, 2,423 indexed records and 680 shortcut records are unchanged.

## Overall organization and learning flow

The shared search is a reference desk across the three specialist learning paths. It preserves app/type filters, precise entry links and full-text lookup while adding title abbreviations. It does not change curriculum order, prerequisites, readiness challenges or quizzes. Each result names its app and type; the reader still provides context, related lessons and source boundaries.

The existing stage maps, diagrams, exercise assets and practice tools remain in place. No speculative concept diagram was added: the inspected need was faster retrieval and clearer navigation, already served by the shared entrance, authored curriculum and links. The original readers retain their own search controls; Ctrl+K opens the shared fuzzy search while reading inside the library.

## Matching and interaction

`assets/matcher.js` is a small, dependency-free browser script loaded alongside the local search index only when search/comparison is opened. It does not invoke installed fzf, launch a helper, contact a service, use a CDN, or require a server. Ordinary file URLs remain supported.

Matching combines exact full-text tokens with ordered title subsequences. Exact titles and title phrases rank first, then stronger title-token/abbreviation matches, then body/context matches. A fuzzy match must have at least three characters and a reasonably compact span; body text is never scanned for arbitrary loose subsequences. All query tokens must match. These rules avoid burying a precise reference beneath coincidental matches across a long lesson. Stable tie-breaking keeps equal matches in authored index order.

Examples tested against the actual data include `gsblur` → Gaussian Blur, `gausian blur` → Gaussian Blur and `curvs` → Curves. This supports abbreviations and missing letters; it does not promise arbitrary misspellings, transpositions or fzf's exact algorithm/query syntax. Exact substring tokens still search complete lessons, references, quizzes and field guides.

Text is normalized once for matching. Unicode title positions are mapped back to the original characters for highlighting, including accented letters and surrogate pairs. Rendering escapes text before adding highlight elements; it never treats a query as HTML. Literal body matches are highlighted in the excerpt, while title subsequences show their matched characters. Original display text is preserved.

Search uses native links and inputs, with added keyboard behavior:

- Ctrl+K opens/focuses shared search from the library or any embedded manual.
- From the search field, Down selects the first result, Up the last, and Enter opens the first result.
- Within results, Up/Down move through visible links; Up from the first returns to the input. Home/End select the first/last visible link.
- Escape returns to the input; when already there, it clears the query. Native Tab/Enter behavior remains available.
- Show more results moves focus to the first newly revealed result, retaining a usable keyboard reading position.

Search is a full page, not a modal or an ARIA listbox. Native link semantics and Tab order remain intact. IME composition does not activate the result-navigation shortcuts. URL/query restoration, app/type filtering, pagination and empty/no-match states are retained.

## Detailed review and fixes

The lazy loader loads the matcher and index together, reports missing local files and permits retry without adding network dependencies. Existing render-generation checks prevent an old load from replacing a newer page. Search normalizes its index once and renders at most 40 results initially; excerpts are computed once per rendered result.

Cross-frame testing exposed two integration issues: Firefox needed the parent workspace activated before focusing the search field after a reader shortcut, and global preferences changed during reader initialization could be missed. Both are corrected. A delayed-initial-snapshot fixture verifies the preference request is applied once the reader becomes ready. Existing navigation sequences, persistence reconciliation and backup validation remain in use. Tests of hidden readers use timer polling rather than animation-frame polling, since browsers can suspend animation frames in hidden documents.

The matcher logic suite checks actual-library ranking, application/type filters, exact/full-text retention, Unicode normalization/highlighting, empty queries and absent matches. Browser tests exercise real offline file URLs, character highlights, query-to-entry keyboard navigation, Ctrl+K inside a reader, Escape, filters, pagination/focus, query restoration, text escaping and 320/375/768 px widths. No failed assets, HTTP(S) requests or JavaScript errors were observed in the dedicated search tests in Chromium and Firefox.

The full library route/interaction sweep and the second-pass recovery suite are rerun to detect effects on learning progress, imports, settings, navigation, printing and storage-denied sessions. Final results are recorded below before publication.

## Measurements and verification

Observed development tools: Python 3.15.1, Node 26.12.1, Chromium 156.0.8078.47 and Playwright's Firefox 157.0 with Playwright 1.64.1. These are development observations, not new runtime installations or package requirements for reading.

- Matcher fixture over all 2,423 records: approximately 1.96 ms median / 2.51 ms maximum across 45 warm mixed queries in Node.
- Real browser query plus synchronous result DOM updates, 30 warm mixed queries: Chromium median 5.4 ms / maximum 22.5 ms; Firefox median 4.0 ms / maximum 11 ms. These exclude paint and are not cold-start or slow-device guarantees.
- Search browser tests: pass in Chromium and Firefox with networking disabled, including the delayed-preference fixture.
- Core source/manifest/export validators and build regressions: pass; all protected original teaching material remains byte-identical.
- Complete library sweep: all 2,423 routes passed in each of Chromium and Firefox, with zero JavaScript errors or HTTP(S) requests.
- State-recovery regression suite: pass in Chromium and Firefox.

The change adds functionality, so no overall speedup over the previous exact-only search is claimed. The matcher and full index remain lazy-loaded. There is no runtime package manager or operating-system search dependency.

## Backup and limits

The repository contains the ready-to-open reader, sources, generated data, original teaching formats, diagrams, sample media and tests. A fresh checkout is checked before delivery. Browser-local progress and personal notes are not repository files: export them using Progress → Export all progress and save the JSON outside the laptop before wiping it. Import that backup after restoring the repository. Nothing silently uploads browser data to GitHub.

This audit covers reader behavior and preservation, not execution of every Adobe exercise in licensed Windows applications. Existing product-version and research boundaries remain unchanged. The matching rules are intentionally bounded and do not guarantee that every abbreviation or typing error produces the desired result; app/type filters and exact full-text queries remain available.
