# Photoshop Field Manual — Windows Edition

**Verified Photoshop version:** 27.11 (September 2026 release, confirmed by Adobe Oct 13 security bulletin). Research checked 2026-10-28; the Oct 29 requested cutoff had not yet occurred.

## Start reading offline

1. Extract this entire ZIP to a normal folder on Linux or Windows; retain subfolders.
2. Double-click `index.html` or open it as a local `file://` URL in a modern Chromium, Firefox or Edge browser.
3. Choose **Start learning**. Use the sidebar to browse 12 stages, or **Search** to locate tools, filters, concepts, recipes and troubleshooting.
4. Complete a lesson after checking its exercise; quiz answers are revealed when you check them. Progress is informative, never a lock. In **Progress & transfer**, choose larger text, high contrast or one-step walkthrough reading.
5. Use **Export progress** and **Import progress** to carry a JSON file between browsers or machines. Import validates the backup, checks the Photoshop target version and asks for confirmation before replacing the current record. There is no automatic sync; local storage policies vary and can be disabled for `file://`.

The site requires **no internet, web server, Node.js, CDN, cloud font or online script**. The learning data, styles and reader code are embedded into `index.html`; there are no separate scripts to load. All core lessons and references work when local storage is disabled, but your progress may not persist; export JSON regularly. Source URLs are optional external reading, not runtime requirements.

## Photoshop setup (Windows only)

Install the Adobe Creative Cloud desktop app and Photoshop 2026 27.11 through your Adobe account; confirm Windows Photoshop version via **Help > About Photoshop**. Official minimums for 27.x: supported Windows builds, 8 GB RAM, Intel/AMD AVX2-compatible CPU, and DirectX 12 feature level 12_0 with suitable VRAM; Adobe recommends 16 GB+ RAM, SSD/scratch capacity and more GPU memory for high-resolution work. See `SOURCES.md` for precise specifications. Adobe activation and certain subscriptions/services require connectivity.

Using Photoshop in a Windows VM while reading on Linux requires the **Windows guest** to present an adequate GPU/driver. Host Linux graphics acceleration alone proves nothing about guest DirectX compatibility. Check **Help > System Info** and **Edit > Preferences > Performance** inside the guest; fallback or missing GPU features are common with virtual adapters. Adobe support for an entire VM configuration is not implied.

## Structure

- `index.html` — self-contained offline reader with inline CSS/JavaScript/data; `web/index.template.html` and `assets/*` — editable build inputs, diagrams and assets.
- `content/content.json` — structured canonical content; `scripts/author.py`, `scripts/references.py` and `scripts/second_pass.py` are editable authoring source.
- `ALL_CONTENT.md` — full reading edition generated from the same data.
- `CURRICULUM.md` — all stages, prerequisites, stage-end assignments.
- `reference/*.csv` — filter, tool, shortcut, glossary, recipe and diagnostic exports.
- `practice/*.png` — original synthetic exercise assets, no external license dependency.
- `SOURCES.md`, `AUDIT.md`, `AUDIT_CROSS_MANUAL.md`, `AUDIT_SECOND_PASS.md`, `AUDIT_INITIAL_1.0.0.md`, `CHANGELOG.md` — research, comparative and earlier audits, and revision history.
- `scripts/build.py` — rebuild derived content (requires Python and Pillow for samples); `scripts/validate.py` and `scripts/audit_second_pass.py` — structural/content checks; `scripts/browser_test.py`, `scripts/browser_extended.py` — optional Playwright/Chromium tests; `scripts/check_manifest.py`, `scripts/package.py` — checksum and reproducible ZIP tooling; `MAINTENANCE.md` — authoring and progress-data contract.

The SHA-256 manifest (`MANIFEST.sha256`) can be checked with `python scripts/check_manifest.py --check` after extraction. The bundled reader can be used without Python.

This project includes 75 lesson modules, 71 tool entries, 81 filter entries, 230 shortcut entries, 155 glossary terms, 30 troubleshooting cases, 40 recipes, 12 stage projects and 75 graded quiz prompts.

## Teaching and accuracy notes

The manual focuses on stable workflows, not unverified 'every possible' control. Some rare, version-specific, legacy or model-dependent features are identified as such. Do not treat the site as legal advice about licensing, authorization or representation; use images you own or have permission to edit. For updates to 27.11, consult Adobe's official documentation once online. No Photoshop desktop was available for direct GUI validation during publishing; see `AUDIT.md`.
