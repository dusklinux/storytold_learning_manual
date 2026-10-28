# Publication audit — Photoshop Field Manual 1.0.0

**Audit date:** 2026-10-28  
**Research date:** 2026-10-28; the requested 2026-10-29 cutoff was not yet reached.  
**Target Photoshop:** Windows Photoshop 2026, stable release **27.11** (September 2026 in Adobe release notes; included as the updated version in Adobe's 2026-10-13 security bulletin).  
**Target reader:** Modern Linux/Windows web browser; static local `index.html`, no web server.

## Executive finding

This is a functional educational **edition**, not a certification that every Photoshop option and shortcut has been tested against a live installation. It provides a carefully sequenced 12-stage course with 75 authored lessons, 75 knowledge checks, 12 stage-end projects, sample artwork, and searchable reference collections. Source documents and an explicit version-status appendix are provided. See **Outstanding limitations** before relying on an obscure menu item or a changing online feature.

## Inventory and structural audit

| Check | Result | Evidence / scope |
|---|---|---|
| 12 stages and stage-end projects | PASS | One applied project and pass rubric per stage; advanced tasks appear after foundational lessons. |
| 75 lessons present and uniquely identified | PASS | `scripts/validate.py`; all IDs unique and staged. |
| Lesson components | PASS (structure) | Every lesson has objective, ordered prerequisites, conceptual model, Windows location, ≥4 walkthrough steps, expected result, explanation, application, mistakes, efficiency tip, independent exercise, evidence standard, skill checkboxes, related links and a three-option quiz. |
| Dependency graph | PASS (structural) | Every prerequisite points to a present earlier lesson. Cross-references, previous/next links and 12 stage assignments checked. |
| Reference library | PASS (structure) | 71 tools, 81 filters, 69 shortcuts, 148 glossary terms, 30 symptom-based troubleshooting topics, 30 recipes; every linked lesson exists. |
| Learning/reference integration | PASS | The same canonical content produces website search data, complete Markdown and CSV reference exports. |
| Progress and portability | PASS (browser simulation) | In-browser completion, knowledge check, bookmark, JSON download and JSON upload were exercised in Chromium. |
| Offline web architecture | PASS (static analysis + browser network observation) | Only relative local CSS/JS/images, no external fonts, CDNs, fetch, XMLHttpRequest, dynamic import or network requests for essential content. |
| Native `file://` browser navigation | **NOT TESTED SUCCESSFULLY** | Managed Chromium in the test environment returns `net::ERR_BLOCKED_BY_ADMINISTRATOR` for direct local navigation; inline simulation described below. |
| Photoshop desktop commands | **NOT DIRECTLY TESTED** | Photoshop was not installed or launched in a Windows desktop. Official Adobe documentation is the source of the release and many operations, but individual click paths and all permutations of UI settings were not exercised. |
| Full exhaustiveness across all optional features | **NOT CLAIMED** | The reference libraries cover major built-in families but do not certify every variant, plugin, obscure legacy option or combination of modes. |

## Software/browser test record

The test runner is `python scripts/browser_test.py`. It uses **real headless Chromium** with the browser network set offline. Because this environment's administrator URL blocklist denies direct `file://` navigation, the runner places the **unchanged locally authored application CSS, data JS and UI JS bytes** into one in-memory HTML document using Chromium's `set_content`; it then executes actual DOM, keyboard and download/upload interactions. This is a **real-browser UI test of the application logic**, but only an **inline-content simulation** of direct local-file loading. Asset paths for diagrams/images cannot be resolved from `about:blank`, so image loading was not visually verified in those screenshots. The original `index.html` uses relative URLs to bundled assets; a normal unmanaged local browser is the intended deployment environment.

Browser interaction checks passed:

1. Offline homepage render.
2. All 75 lesson links listed.
3. Lesson sections and guided steps shown.
4. Quiz selection and answer evaluation.
5. Completion state changes the UI.
6. Previous/next progression links.
7. Full-text search returns lesson and filter results.
8. Windows shortcut filtering.
9. Tool reference detail rendering.
10. Filter reference detail rendering.
11. Reference bookmarking and favorite state.
12. Bookmarked reference appears in progress collection.
13. Dark/light theme switching.
14. Portable JSON progress download and schema validation.
15. JSON progress import and restored completion.
16. `/` keyboard search navigation.
17. No runtime JavaScript exceptions or remote HTTP requests.
18. Mobile lesson layout rendering.
19. Mobile sidebar open/close.
20. Mobile horizontal-overflow check.

The harness reports 19 named UI tasks plus a separate no-error/no-network assertion. Screenshot files in `audit/screenshots/` are labeled **simulated** and are illustrative, not proof of local-file image rendering or a Windows Photoshop session.

## Content correctness checks and boundaries

- **Version control:** Adobe September 2026 release notes describe 27.11. The October 13, 2026 security bulletin lists 27.11 as the updated Photoshop 2026 version; the stable release's **exact original day and any 27.11.x point-build string were not established**. LTS 26.11.8 is a different branch and is not presented as the selected release. No release from October 29 or later is implied.
- **Recent features:** The Light adjustment layer, edge improvements, Remove processing mode distinctions and generative capabilities are treated according to their announced version and operational constraints; a Beta AI Assisted Editor and a Beta toolbar redesign are excluded from stable instructions. A changing AI model menu or plan/credit limit may supersede a screenshot or reference entry independently of the installed version.
- **Windows focus:** Photoshop instructions use Windows menu and preference routes; no macOS equivalent shortcuts are included. Shortcuts are accompanied by context notes and Adobe's **Edit > Keyboard Shortcuts** is identified as authoritative for installed/customized environments.
- **Destructive operations:** Lesson patterns favor duplicated sources, separate retouch layers, masks, Smart Objects, layered working PSDs and nondestructive adjustments. Some selection, filter, paint or flattening methods require mode-specific checks and are explicitly conditional.
- **Color and formats:** Lessons distinguish pixel dimensions versus print resolution, destructive resampling, RGB/CMYK, bit depth, color profiles, layered working files and delivery exports. Precision and display matching depend on the real color-managed hardware and a chosen printer/output workflow.
- **System and cloud:** Adobe's official GPU and OS minimums guide the Windows specification; a virtual machine is **not** promised the same capabilities as a supported physical host. Generative cloud features may require sign-in, subscription, usage credits and connectivity; device-side models may need an initial download and substantially greater GPU/system resources.
- **Completeness limits:** Reference entries are curated and structured, rather than automatically enumerated from Photoshop binaries. Menu labels, filter availability, keyboard overrides, Camera Raw version, regional cloud options, and obscure modes should be checked against the installed application's current Help/Settings and Adobe's linked official documentation.

## Macro curriculum audit

Sequence: pixels and interface → documents and layers → selection and masks → editable corrections → retouching → painting → vector/type design → photography and color → compositing → professional automation/exports → performance/diagnostics → capstones. The ordering ensures layers precede masks; masks and Smart Objects precede complex retouching and compositing; color fundamentals precede production soft-proofing. All lessons have predecessor references and are **not gated** by a quiz or artificial lock. Every stage has a practical deliverable and measurable pass standard.

The level of difficulty remains a judgment call: some learners will need extra practice on paths, color management and scripting before advancing. Stage projects provide that integration check. The written examples are deliberately reproducible without paid stock assets, but sophisticated portrait restoration and real-world print tests necessarily benefit from rights-cleared photographs and access to output hardware.

## Micro audit and residual risks

The structured audit catches missing lesson fields, invalid reference IDs, quiz shape errors, and export mismatches; it does **not** establish that a desktop command functions exactly as written on every GPU, language setting, image mode or subscription. The most important remaining tasks for a reader with Photoshop installed are: spot-check a representative lesson and shortcut in each stage, confirm the installed Photoshop build under **Help > About Photoshop**, verify GPU status under **Edit > Preferences > Performance**, and check that the actual Photoshop AI UI matches the applicable account/region. Record any differences before expanding the manual to later releases.

Potential uncertainty categories: user-customized toolbar/workspace, conflicting keyboard shortcuts, document mode and bit depth restrictions, optional plugin/component availability, legacy filters, temporary Adobe cloud model offerings, GPU-driver behavior (especially VM virtual adapters), unsupported graphics paths, local browser persistence policies and color-managed print outcomes.

## User acceptance checklist on Linux or Windows

1. Extract the ZIP and confirm `index.html`, `assets/`, `content/`, `practice/` and `reference/` are in the same root folder.
2. Disconnect the internet and open `index.html` directly as a file URL in a regular browser not subject to administrator URL blocking.
3. Confirm a stage, a lesson, the sample-art preview and a filter page open; use search and a quiz.
4. Complete/bookmark an item, export JSON, and import it into a second browser profile to demonstrate non-synchronizing portability.
5. Check the Dark theme and narrow-window sidebar. Test in your actual target Linux browser and Windows browser; browser-specific `file://` storage is not standardized.
6. In Photoshop for Windows, verify actual 27.11 build, a simple masks lesson, a Smart Filter, output color profile and GPU performance before relying on specialized operations.

## Commands to reproduce publisher checks

```text
python scripts/validate.py
python scripts/browser_test.py
node --check assets/app.js
```

The browser test additionally needs Playwright Python and a local Chromium executable in its current form; neither is needed to **read** the manual. The website requires no terminal commands, tools or installation once extracted.

## Publication decision

**Deliver as an openly qualified, offline-capable structured learning system.** Structural export, application logic and offline network checks pass. Direct `file://` access under this managed browser, cross-browser testing on a normal Linux/Windows device, live Photoshop UI verification, full exhaustive command validation, and real Windows-VM GPU certification remain outside the verified test coverage. This distinction is intentional: no missing test is represented as a success.
