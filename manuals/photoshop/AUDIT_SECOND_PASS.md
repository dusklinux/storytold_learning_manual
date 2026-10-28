# Independent second-pass publication audit — edition 1.1.0

**Date:** October 28, 2026. **Product:** Photoshop 2026 for Windows, release 27.11 (latest verified stable feature version). **Scope:** all packaged educational content, project exports, reference catalogs and offline reader code. This is a desk/documentation and browser audit **without access to a live Windows Photoshop 27.11 installation**. It cannot certify operation of every command in the actual application, and it is not a test of every possible Photoshop option.

## Executive judgment

The package is a coherent, locally bundled 12-stage learning course with 75 lessons, exercises, stage integration projects, quizzes and searchable reference tables. The initial edition was not error-free. The second pass found several real defects: a wrong R shortcut for Blur/Sharpen/Smudge, a collision with historical K assignments, a non-existent Quick Mask menu path, several generic filter paths (including Perspective Warp being under **Edit**, not **Filter**), a missing Adjustment Brush entry, tool locations that were generic rather than group-specific, an incorrectly available legacy Shake Reduction filter, imprecise AI service paths, insufficient cross-stage prerequisite declarations, a duplicate pseudo-tool entry, and a skip-navigation link incompatible with the website's hash-router. Corrections are applied **at the shared source generator level**, not only in one export. The fundamental curriculum order remains sound.

## Corrective change log with evidence

| Severity | Finding | Correction | Evidence category |
|---|---|---|---|
| High | R incorrectly assigned to the Blur/Sharpen/Smudge tool group, conflicting with Rotate View | Removed R; explicitly state Blur group lacks a reliable current default | Adobe Rotate View tool documentation; current Photoshop Training Channel 2026 desktop shortcut guide |
| High | Historical older reference assigns K to Blur tools, but current K belongs to Frame | K stays with Frame; old Blur K not recommended | Current shortcut documentation/expert 2026 audit; Adobe shortcut editor is final authority |
| High | `Select > Edit in Quick Mask Mode` appeared as if a menu command | Replace with Quick Mask button or Q; Select > Save Selection remains valid | Adobe Quick Mask desktop page |
| High | Generic location for Edit > Perspective Warp and 16 other filter/workspace entries | Explicit paths for 15 available native entries; two partner-AI service items still use conditional location | Adobe filter/Smart Filter docs and conventional Windows UI paths; conditional items flagged |
| Medium | Stage references used only immediate predecessor, omitting important cross-stage foundations | Added explicit earlier prerequisites to complex editing, color, compositing, production and final review lessons | Curriculum dependency analysis |
| Medium | Missing Adjustment Brush and wrong Selection Brush keyboard grouping; Artboard shortcut omitted | Added Adjustment Brush; Selection Brush L; Artboard V | Adobe historic references plus current 2026 expert Photoshop reference; verify customized toolbar |
| Medium | Tool encyclopedia used the same broad “Toolbar” location for all tools | Added 71 identifiable toolbar group locations, with customization caveat | Tool taxonomy / keyboard group audit |
| Medium | Duplicate pseudo-entry “Color Sampler and measuring tools” used as if a distinct tool | Removed; retained actual Color Sampler, Ruler, Note and Count tools | Editor structure audit |
| Medium | `file://` app skip navigation caused a `#main` hash that router treats as an invalid content route | Intercept skip link, focus main without altering route, restore focus on route change | DOM/browser functional design review |
| Medium | Several imprecise paths for Camera Raw, Quick Export, account status | Clarified Open/Camera Raw Filter/Export preferences, separated external Creative Cloud account | Official Adobe desktop help and menu discipline |
| High | Shake Reduction incorrectly presented as an available Filter > Sharpen command | Explicitly mark REMOVED since Photoshop 23.3; historical listing only | Adobe official removal notice, May 2023 |
| Medium | AI Sharpen/Denoise needed exact conditional menu paths and destructive behavior caveats | Filter > AI Sharpen / AI Denoise; premium/credit requirement, current-layer operation | Adobe 2025–2026 Topaz AI help |
| Low | Entry coverage gaps in shortcuts, glossary and recipes | Expanded to 112 contextual shortcuts, 155 glossary definitions and 40 recipes | Curated, conditional references; legacy shortcut evidence not claimed as live-validated |

## MACRO evaluation

| Audit dimension | Finding |
|---|---|
| Curriculum completeness | All twelve requested major stages represented; 75 original lesson topics and one integrated project in each stage; missing content is not hidden as placeholders. |
| Prerequisite graph | Sequence remains acyclic; additional explicit cross-stage prerequisites were inserted for Smart Filters, masking, color, compositing and production. Validated by script. |
| Learning load | Each lesson supplies a conceptual rationale, at least 4 procedural steps, expected result, common failure, practice and a quiz. Advanced work has prerequisites and stage synthesis projects. Some lessons remain **short** relative to a comprehensive textbook chapter. |
| Skill coverage | Raster/vector, color, layers, masks, selections, editable corrections, retouch, painting, type, shape paths, RAW/color profiles, composites, automation, output, performance, VM support and AI/offline constraints are present. |
| Reference taxonomy | Tool/filter/shortcut/glossary/troubleshooting/recipe collections distinguished from lessons and indexed by browser search. Some rare subcommands and settings are necessarily not listed. |
| Progression/gating | No artificial lesson locks; progress, checklists, quizzes, stage completion and bookmarks are optional, client-side. |
| Exercise accessibility | Six original synthetic assets are bundled, but portrait/RAW/print exercises naturally still require an owned portrait/camera RAW file or printer profile; these are not included. |
| Navigation | Sidebar, stage pages, breadcrumbs, previous/next, search and reference deep links exist; skip-to-content route issue corrected. |
| Reproducibility | `scripts/build.py`, `scripts/second_pass.py` and references source generate JSON, JavaScript bundle, CSV, Markdown and documentation; no Node build required to consume website. |
| Version separation | 27.11 desktop feature branch distinguished from LTS 26.x, Beta tools, legacy/removed features, cloud-dependent AI and hardware-limited on-device AI. |

## MICRO verification and evidence classification

**Checked against official Adobe pages dated on or before October 28, 2026:** desktop stable release number, version notes, shortcut editor location, Quick Mask editing, mask gestures, Smart Filter model and exclusions, adjustment layer/Smart Object fundamentals, export paths, GPU setup, Camera Raw concepts, large-document rules, and filters' mode restrictions. Checked selected shortcuts against a contemporary 2026 expert reference where current Adobe default-key tables were not published in an updated itemized HTML version. The installer itself, user-assigned shortcuts, graphics drivers and cloud entitlement were not available for direct observation.

**Shortcut consistency:** Every nonblank key record has a context/warning. The tool roster and shortcut table no longer disagree about R/K and Selection Brush. Context-dependent gestures are separate from global commands. Export/older panel shortcuts are supplied as historically documented and should be verified in the installed `Edit > Keyboard Shortcuts` dialog; listed shortcuts are not a guarantee that every user retains defaults. Double meanings such as `Ctrl+J` for duplication versus selection-to-layer are intentional and have explicit scopes.

**Filters:** The inventory explains 81 entries (including the historical, removed Shake Reduction filter) and includes mode/GPU caveats. In particular, Lens Blur, Tree, Flame and Vanishing Point are not promised as Smart Filters. Adobe documents Filter > AI Sharpen and Filter > AI Denoise, but these are conditional premium services with credit and eligibility requirements. Adobe confirms both operate on the active layer without creating a new layer; preserve a duplicate first. Adobe confirms Shake Reduction was removed in Photoshop 23.3, so its entry now explicitly states it is historical and unavailable in 27.11. The inventory is curated rather than a binary-extracted complete filter registry, and filter behavior can vary by document mode/bit depth.

**Numerical and color correctness:** Core examples were reviewed for dimension arithmetic (e.g. 2400 px at 300 PPI = 8 inches), mask black/white semantics, resampling versus physical print density, working PSD versus delivery PNG/JPEG, color management conversion and practical print proofing. Sample values are pedagogical, not universal correction targets. Print profiles and GPU/VM behavior must be checked on actual target hardware.

**Research boundary:** The initial day of the 27.11 release is not firmly established. Adobe's 2026-10-13 security bulletin names 27.11, but a finer 27.11.x build cannot be certified. The requested October 29 cutoff was not reached at research time (Oct 28). Do not infer October 29 updates.

## Executed automated validations

- `python scripts/validate.py` checks baseline schemas, ordering, cross-references, generated files, 6 CSV exports and no network requests.
- `python scripts/audit_second_pass.py` performs additional independent checks of bidirectional navigation, cross-stage graph, completeness, unique quiz prompts and options, actual tool IDs, filter locations, shortcut collisions, local assets, generated manifest consistency and progress/search code presence.
- `python scripts/browser_test.py` exercises search, quizzes, lesson completion, transfer, bookmarking, theme and mobile layout in a real headless Chromium DOM with offline networking.
- Direct local-file navigation through managed Chromium remains blocked by an administrator restriction in the test host. The browser test uses inline injection of the **same** CSS/data/app bytes, so local `file://` asset resolution and native Linux/Windows deployment were **not** directly proven. This limitation is an environment restriction, not a diagnosed code failure. There is no server or network dependency in the project.
- A live Photoshop 27.11 Windows interactive click-by-click test, real printer proof, real GPU passthrough VM test and individual raw-camera support test were **not performed**.

## Known residual weaknesses / further specialist work

1. Lessons are generally concise modules (mostly four to five steps), not exhaustive long-form chapters about every dialog option. They are a strong progressive foundation and reference, not a literal enumeration of every Photoshop mode.
2. Some user-selected fonts, image-mode combinations, model entitlements, localized UI, GPU capabilities and Windows/VM behaviors cannot be validated offline or without target hardware.
3. The comprehensive default shortcut list needs an export from **a clean 27.11 Photoshop installation** to certify every command; the old Adobe reference and modern Photoshop conflict on a few assignments.
4. Availability of Topaz partner-model/AI services, pricing, subscriptions and account credits is time-sensitive and region/plan-dependent. This guide labels such functions as conditional.
5. Adobe’s official system requirements do not guarantee adequate virtual graphics acceleration; real guest DirectX and drivers need native testing.
6. Test assets intentionally use shapes/gradients, so exercises involving hair, faces, real RAW sensor data and physical print proofs require the learner's rights-cleared materials.
7. An independent typographic copy edit, live accessibility audit using assistive technology and full functional test on real Windows/Firefox browsers have not been performed.

## Principal sources used in this second pass

- Adobe official Camera Shake Reduction removal: https://helpx.adobe.com/photoshop/using/reduce-camera-shake-induced-blurring.html
- Adobe Topaz AI Sharpen/Denoise paths and limitations: https://helpx.adobe.com/in/photoshop/desktop/effects-filters/artistic-stylize-filters/enhance-images-with-generative-ai-filters.html
- Adobe desktop Photoshop release notes: https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html
- Adobe View keyboard shortcuts (2026): https://helpx.adobe.com/photoshop/desktop/get-started/settings-and-preferences/view-keyboard-shortcuts.html
- Adobe Rotate View tool: https://helpx.adobe.com/in/photoshop/using/tool-techniques/rotate-view-tool.html
- Adobe Quick Mask mode: https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/create-a-temporary-quick-mask.html
- Adobe Smart Filters: https://helpx.adobe.com/photoshop/desktop/effects-filters/smart-filters/apply-and-manage-smart-filters.html
- Adobe filters overview: https://helpx.adobe.com/photoshop/desktop/effects-filters/get-started-with-filters/filters-overview.html
- Adobe layer masks: https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/add-layer-masks.html
- Adobe large documents: https://helpx.adobe.com/photoshop/desktop/save-and-export/save-files/save-large-documents.html
- Adobe desktop current shortcut expert cross-check: https://photoshoptrainingchannel.com/photoshop-keyboard-shortcuts/
- Historic Adobe Education shortcut listing (used with version caveat): https://cdn.edex.adobe.com/v3/uploads/resourceFile/2023/c0c1aaee-43e8-4c03-9b2c-aaec2c3d9285/08d7c4a0-c2ba-4d6a-8fa2-396d2d99c346.pdf

**Quality statement:** The delivered revision is materially improved and passes automated structural/UI checks, but it would be false to call its every command and default shortcut exhaustively verified without a Windows Photoshop 27.11 installation. Treat the above residuals as open validation boundaries, not suppressed defects.
