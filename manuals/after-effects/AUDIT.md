# After Effects 26.5 manual audit

Audit date: **28 October 2026**. Target: **After Effects 26.5 stable, Windows, default English keyboard**. Reader: Linux/Windows offline browsers and Markdown viewers. This is independently authored instruction, not Adobe-certified training.

## Main finding and scope correction

The supplied local repository and GitHub HEAD (`51bd1f8`) targeted **25.6**, despite the requested **26.5** and the supplied 26.5 Markdown notes. Version metadata, lessons, catalogs, validation, README, maintenance policy, storage keys and progress exports all enforced the older target. Quick Apply, Object Matte, native meshes/materials, Unmult, new audio effects, variable-font axes, SVG workflows, Curl Noise, Advanced 3D DOF and ACES 2.0 were deliberately excluded or described as unavailable.

This edition corrects the target throughout. Adobe’s [release notes](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html) identify September 2026 version 26.5; [What’s New](https://helpx.adobe.com/after-effects/desktop/what-s-new/whats-new.html) documents the stable improvements. The historical 25.6 topic remains as earlier functionality retained in 26.5, with its durable ID preserved. The old security-patch discussion was removed from the version policy because it was irrelevant to the requested edition; this was a documentation/product audit, not a security audit.

The Factorio path was supplied in error and explicitly corrected to `/mnt/zram1/ae_manual`. The Factorio files and the personal Markdown note were not edited. The note was read as a coverage seed; its statements were compared with feature-specific Adobe references rather than imported uncritically.

## Coverage and teaching changes

| Area | Previous edition | Current edition |
|---|---|---|
| Target | 25.6, November 2025 | 26.5 stable, September 2026 |
| Lessons | 35 | 40, including 5 current-workflow lessons |
| Explanatory topics | 78 | 100 |
| Practical recipes | 27 | 34 |
| Effect/control records | 285 | 300 |
| Shortcut/gesture records | 373 | 386 |
| Glossary | 145 | 155 |
| Practice assets | None | Original SVG, JSON, CSV and PCM audio |

The six learning stages remain monotonic. Recipe prerequisites now use durable chapter IDs; lesson numbers are derived after ordering, so inserting a lesson cannot silently point a recipe at an unrelated prerequisite. Existing lesson IDs and six original action positions remain stable.

Modern workflows now include Quick Apply result modifiers, responsive guide units/reference edges, effect swatches and masked contributions, Object Matte correction/propagation/freeze/cache, Proportional Scrubbing versus Quick Offset, SVG file/clipboard routes, variable-font axes/spacing, native geometry/materials/displacement, actual Advanced 3D camera focus, Curl Noise, Unmult, Compressor/Gate/Distortion, ACES 2.0, native null controllers and clipboard frame capture. Added references cover expression examples, modern dropdown labels/key lookup, text outlines/Layer Styles and immersive effects.

Concrete instruction corrections include:

- The old logo-reveal recipe moved a fixed matte past the logo, potentially hiding it again. The logo now enters a stationary reveal window and remains fully covered at its final pose.
- A four-second 25-fps exercise asked for frame 100 as if it were inside the comp. Frames 0–99 are visible; 100 is the exclusive duration boundary.
- The loop recipe now preserves the full source-duration interval with an explicit last-valid-frame Hold and a boundary remap to zero. Merely deleting a default duration-end key can shorten a cycle. Source rate/trim offsets still require inspecting the actual render.
- Effects catalog corrected an unsupported `CC Color Balance` label to documented `CC Kernel`, and added missing Levels (Individual Controls), Broadcast Colors, Video Limiter, Mocha AE, CINEWARE and OCIO transforms.
- Placeholder audio expressions were replaced with full named references. CSV and JSON access paths are distinguished; table cells are inspected with the pick whip rather than guessed from nested JSON.
- Modern effect labels use the documented gray swatch beside each instance; the panel’s swatch/tint options affect organization rather than pixels.

The effect directory is an orientation reference. It includes obsolete compatibility effects and explicitly identified tool-generated processing; it does not claim all 300 records are ordinary drag-on generators or that every installed plug-in parameter is enumerated. CPU/GPU, bit depth and MFR support are independent; no unsupported blanket performance claims were added.

## Research and source conflicts

Primary references are linked per lesson/topic/recipe in HTML and Markdown, and recorded in `content.py → SOURCES`. Adobe’s general effect/keyboard tables predate some recent feature-specific pages, so a missing modern entry in a general table is not sufficient evidence of absence.

- **Stable/Beta:** Adobe’s [Beta page](https://helpx.adobe.com/after-effects/desktop/what-s-new/after-effects-beta.html), updated October 7, separately lists Contour Paint, De-esser, AI Assistant, animated-layer material sources, materials on 3D text/shapes, editable Illustrator text, Quick Set Anchor, generalized viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save. These remain a watchlist, not stable lesson prerequisites. Stable mesh-specific duplication has narrower scope.
- **Object Matte binding:** its [dedicated page](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html) lists Windows Ctrl+W, while the [general shortcuts](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html) use Ctrl+W for Close. No undocumented focus rule is invented. Use the toolbar or inspect/remap locally.
- **Guide import:** [guide documentation](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html) explicitly describes 26.5 preservation of colors, units and pins, followed by retained older statements about conversion. The guide teaches current behavior and requires a destination round trip for interchange.
- **Cache crashes:** the [known-issues page](https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/known-issues-after-effects.html) names 26.0/26.2 for the compressed-cache crash notice. It is not presented as proof that all 26.5 installations should disable compression. The listed 26.5 twirl-state issue is a different problem.
- **Color:** [OCIO documentation](https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html) confirms OCIO 2.5.1, ACES 2.0 CG v4.0 and Studio v4.0. Source interpretation, working space, display transform and output transform remain separate decisions.

`data/source_checks.json` distinguishes editorial web research from automated HTTP retrieval. The direct HTTP run received 403 for Adobe URLs, while GitHub history was retrievable. Those errors are preserved, not represented as broken links or successful validation. Web research retrieved the cited primary pages. Neither a successful HTTP status nor a search result certifies every procedure in the product.

## Reader reliability and progress

Search results now identify the exact effect/shortcut/problem/term and focus its entry. The skip link moves focus without routing away from the active lesson. Checking a step or quiz option restores keyboard focus after redraw. Reading options affect the small text used in lessons/catalogs. One-step view retains all actions in the DOM and prints the whole lesson.

Saved/imported progress is validated before use, including arrays versus objects, known step keys, quiz indices/options and preference types. Malformed state cannot be spread into the application. Imports replace progress only after validation and confirmation; failed reads are reported. Storage failures leave reading and JSON export available.

Current exports use version 26.5/edition 2. Old 25.6/edition-1 data is accepted and migrated; original browser storage is retained. The installation lesson, `effects:4` (new launcher operation), `color:4` (current ACES configuration), `advanced3d:5` (native mesh operation), and quiz index 1 need review and are reset. New lessons start unchecked. Other original action IDs retain their meaning. Moving the HTML to another path/browser may require explicit JSON import.

## Verification record and limits

The initial checkout had 25 structural tests: 23 passed, two failed because the documented ZIP was absent. Earlier audit text said browser testing was blocked. In this environment both system Chromium and Playwright Firefox launch successfully, so the revised reader has real offline browser coverage.

The regression suite covers generated data/embedded HTML/CSV consistency, version gates, sources and internal links, curriculum order, prerequisites, original progress keys, sample dimensions, manifest contents and archive extraction/rebuild identity. Node checks cover JavaScript syntax, simulated navigation, progress and malformed data. Real-browser checks use `file://` with networking disabled and cover every route/record, exact search results, filters, persistence, export/import, legacy migration, keyboard focus, printing, exact fractional-frame timing, 375/768-pixel layouts and corrupt/blocked storage. Final measured results are recorded below after the final run.

No licensed Windows AE 26.5 installation was available. The 240 authored actions and rendered examples were not exhaustively executed in the product. Synthetic assets do not validate photographic tracking, keying or Object Matte; those need suitable footage. External fonts, SBSARs, Mocha/Maxon components, codecs, hardware/VM GPU behavior and third-party extensions need their own installation/render checks. This audit does not claim parameter-level completeness for every effect, every scripting API or every possible production task.

### Final measured results

- **29/29** dependency-free structural/content/package tests passed, including extraction and byte-identical rebuild of the archive.
- **Chromium and Firefox: 1,094/1,094 offline routes each passed**, plus the functional checks above; **zero HTTP requests and zero JavaScript errors** in the browser run.
- JavaScript syntax and Node simulated navigation/progress/malformed-state checks passed. CLI help works without Playwright installed in the system interpreter.
- Desktop (1440 pixels) and mobile (375 pixels) screenshots inspected; automated layout checks passed at 375/768 pixels with normal and enlarged prose.
- Generated HTML, JSON, Markdown, CSVs and ZIP are consistent; `git diff --check` is clean. Performance throughput was not benchmarked, so no speedup is claimed.

These are reader/build results on Linux. They do not certify rendering, menus or every exercise inside Windows After Effects.
