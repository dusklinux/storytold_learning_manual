> **Combined project:** open [the Dusky library](../../index.html) to choose or switch apps. This directory retains the supplied manual and its historical standalone documentation below. Use the [root build and maintenance instructions](../../docs/STRUCTURE.md); the library build generates no archives.

# After Effects 26.5 & EffectCraft for After Effects — Offline Learning Manual

Open **[index.html](index.html)** in Firefox, Chromium or Edge. The reader works on Linux and Windows, including directly from `file://`, with no server, installation or internet connection. The instructions target **After Effects 26.5 stable on Windows** and **EffectCraft on Linux**, default English keyboard. Research cutoff: **28 October 2026**.

This edition replaces the repository’s former 25.6 target. It includes modern stable tools rather than excluding the 26.x series. Adobe’s release notes identify 26.5 as the September 2026 release; Beta-only functionality has a separate watchlist.

## Start learning

1. Use **Step-by-step walkthrough**: 40 lessons through six stages, from your first composition to a collected, verified final project.
2. Perform each action in AE, then try the independent exercise and self-check. The checkboxes record your own progress; they do not inspect an AE project.
3. Open related **Deep topics** for explanations, or **Practical recipes** for a complete production task. Recipes link to their prerequisite lesson.
4. Use global search for lessons, topics, recipes, effects, shortcuts, troubleshooting and glossary. Reference search results open the matching entry.
5. Use **Progress & settings** for larger text, contrast, one-step reading and JSON backups. Export before moving between browsers, machines or a Linux host and Windows guest. File-URL browser storage may be isolated or blocked; an exported JSON is your portable backup.

**Read-only fallback:** [ALL_CONTENT.md](ALL_CONTENT.md) contains the written curriculum and reference with internal links and per-topic sources. Reading needs no Python or Node.js. For the portable download, extract `after_effects_26_5_windows_offline_manual.zip` and open its `index.html`.

## Coverage

- 40 ordered lessons, 100 explanatory topics and 34 practical recipes, with experiments, verification and recovery instructions.
- 300 effect/control records, 458 After Effects & EffectCraft shortcut/gesture records, 67 troubleshooting cases, 155 glossary terms and 35 quiz questions. Counts describe the authored directory, including legacy and tool-generated records, rather than every installed plug-in parameter.
- Quick Apply, Object Matte and disk caching, responsive guides, effect labels, Proportional Scrubbing, SVG import/paste, variable-font animation, native meshes, SBSAR materials/displacement, Advanced 3D camera DOF, Curl Noise, Unmult, modern audio effects and ACES 2.0.
- Rendering, alpha, color, sound, tracking, keying, brush-guided roto, MOGRTs, expressions/data, reusable rigs, performance diagnosis and portable project delivery.
- Original [practice assets](samples/README.md): SVG, JSON, CSV and a short PCM pulse track. Footage-based exercises still require appropriate footage; font/material exercises require those dependencies prepared before going offline.

Adobe pages can mix stable and Beta material. Contour Paint, De-esser, AI Assistant, broader material sources, editable Illustrator text and other Beta items are described separately, not taught as stable 26.5 requirements. The application has not been certified by executing every lesson in licensed Windows AE. See [AUDIT.md](AUDIT.md) for evidence and limits.

## Existing progress

Current exports use `manualVersion: "26.5"`, `edition: 2`. Old 25.6 edition-1 exports remain importable. On the same file location/browser, existing 25.6 local storage is migrated if no current record exists; its original record is retained. Unchanged lesson IDs and action positions are preserved. The installation lesson, changed Quick Apply/ACES/native-mesh actions and rewritten quiz question 2 are reset for review. New lessons start unchecked. Migration does not claim older completed exercises prove current-version proficiency.

## Files and rebuilding

| File | Purpose |
|---|---|
| `index.html`, `ALL_CONTENT.md` | Offline browser reader and Markdown reference |
| `manual_data.json`, `effects.csv`, `shortcuts.csv` | Structured exports |
| `content.py`, `data/*_seed.json` | Editable teaching material and reference records |
| `web/*` | Reader source embedded into the HTML |
| `build.py`, `validate.py`, `tests/*` | Reproducible build and regression checks |
| `MANIFEST.sha256` | Checksums of ZIP payload files; excludes itself and the ZIP |
| `data/source_checks.json` | HTTP source-retrieval record; status is not factual certification |
| `samples/*` | Original offline practice material and usage instructions |
| `AGENT_HANDOFF.md`, `AUDIT.md` | Maintenance instructions, findings and verification limits |

Development targets **Python 3.15+**. The normal build uses only its standard library and committed inputs; no network access is needed:

```sh
python3 build.py
python3 validate.py
python3 -m unittest discover -s tests -v
```

Use `python3 build.py --output-dir /path/to/output` for separate deliverables. The ZIP includes sources, assets and tests and can rebuild itself after extraction. Edit sources, then rebuild; generated HTML/JSON/Markdown/CSVs and checksums must agree. On Linux, check the extracted payload with `sha256sum -c MANIFEST.sha256`.

Optional JavaScript checks require Node.js:

```sh
node --check web/app.js
node tests/browser_logic.cjs
```

Real-browser checks use Playwright as a **development-only** dependency:

```sh
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium firefox
.venv/bin/python tests/browser_check.py --browser both
```

On Windows use `.venv\Scripts\python` / `.venv\Scripts\playwright`. The runner uses system Chromium on Linux when available, otherwise Playwright’s installed browser. It opens `file://` with networking disabled. `tools/check_sources.py` is an optional online HTTP provenance check; some Adobe requests return HTTP 403 in automation, so those responses cannot certify link health or content. `tools/curate_starter.py --notes PATH` reports note headings/table coverage without overwriting curated IDs.

The manual contains original explanations and optional public source links. It bundles no Adobe documentation pages, footage, fonts, plug-in binaries, telemetry or external runtime assets.
