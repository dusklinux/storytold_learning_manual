# Maintaining the After Effects 26.5 offline manual

The current user request explicitly supersedes the repository’s old 25.6 instructions. Target **26.5 stable, Windows, default English keyboard**. The reader runs offline on Linux and Windows. Do not revert the edition to 25.6 or remove modern stable tools.

Read `AUDIT.md` for source conflicts, live-product limits and verification evidence. Use Adobe’s release notes and feature-specific stable documentation; the shared Help sidebar includes Beta features.

## Authoring

- `content.py` contains sources, lessons, topics, recipes, roadmap, glossary additions, troubleshooting and quiz. Lesson and topic helpers keep authored sections consistent. Recipe prerequisites use durable chapter IDs; displayed numbers are derived after ordering.
- `data/*_seed.json` contains curated catalogs. Keep record IDs stable. New records append new IDs; correcting a name does not imply renumbering other entries.
- `web/template.html`, `web/styles.css`, `web/app.js` form the single HTML reader. No external scripts, styles, fonts, images or runtime requests. Source URLs are optional user-activated references.
- `samples/*` supplies original minimal assets, with explicit instructions and limits. Do not imply synthetic graphics validate photographic tracking, keying or Object Matte.
- `build.py` produces HTML, Markdown, JSON, CSVs, manifest and deterministic ZIP. Generated files must be rebuilt together.

## Progress contract

Current storage: `ae_26_5_windows_manual_progress_v2`, version `26.5`, edition 2. Legacy: `ae_25_6_windows_manual_progress_v1`, version `25.6`, edition 1. Keep the old record when migrating. `tests/legacy_progress.json` records original chapter IDs/action counts. Existing six action positions retain their meaning except explicitly reset installation, `effects:4`, `color:4` and `advanced3d:5`. Quiz index 1 changed and is reset. New lessons have new IDs and start unchecked. Changes to the meaning/order of completed actions require explicit migration, not just new headings.

Import validates before replacement and accepts only compatible versions/editions, known action IDs, true checks, valid quiz options and boolean preferences. Malformed/blocked local storage must not break reading. Export remains available without storage. One-step reading must still print all lesson actions.

## Stable/Beta distinctions

Include Quick Apply, Object Matte, Curl Noise, Unmult, Compressor/Gate/Distortion, native parametric meshes, SBSAR materials on supported models/meshes, mesh displacement, variable-font axes, SVG import/paste, Proportional Scrubbing, Advanced 3D DOF, clipboard frames, effect labels, guide improvements and bundled ACES 2.0.

Keep Beta-only Contour Paint, De-esser, AI Assistant, animated-layer material sources, materials on 3D text/shapes, editable Illustrator-text conversion, Quick Set Anchor, generalized viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save in the watchlist until stable release evidence changes. Stable mesh-specific duplication is a different scope.

## Verification

```sh
python3 build.py
python3 validate.py
python3 -m unittest discover -s tests -v
node --check web/app.js
node tests/browser_logic.cjs
python3 tests/browser_check.py --browser both
```

The browser runner needs Playwright and Chromium/Firefox; the reader and dependency-free tests do not. Python baseline: 3.15+. Optional browser imports are lazy so CLI help works without that dependency. Tests cover a real file URL offline, routes, exact record navigation, filters, focus, print, storage, migration, exports/imports, timing and mobile layout. ZIP extraction/rebuild must be byte-identical.

Do not equate these checks with executing the lessons in licensed Windows AE. Hardware, renderer, media, fonts, plug-ins, external apps and output validation remain a separate product test. Avoid unsupported 100% completeness/certification claims and invented performance scores.
