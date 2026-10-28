# Dusky Adobe Manual

Three independent, researched Windows Adobe manuals in one offline learning library. Read on Linux while practicing in a Windows VM, or use the same folder on Windows.

**Open [index.html](index.html).** Choose Photoshop, Premiere Pro or After Effects. Use **Library** to return to the chooser, or the persistent app selector to switch manuals and return to your last page. The first launch shows the chooser; it never chooses an app for you.

No server, internet connection, package installation, Python, Node.js, Adobe login, CDN or remote font is needed to read. Keep the entire folder together. The project uses ordinary local HTML/CSS/JavaScript and works directly from `file://`. External source links are optional and require internet only if you open them.

| Manual | Preserved research target | Curriculum | Extra material |
|---|---|---|---|
| Photoshop | Windows 27.11 | 75 lessons / 12 stages | Tools, filters, recipes, quizzes, 6 practice images |
| Premiere Pro | Windows 26.5.2 | 105 lessons / 14 stages | Effects, transitions, 13 field guides, sample video/audio |
| After Effects | Windows 26.5 | 40 lessons / 6 stages | 100 topics, 34 recipes, effects/controls, expressions/data samples |

These are the supplied research snapshots dated **28 October 2026**, not automatic claims about the latest installed release. The integration preserves the teaching text and research boundaries. See each manual’s sources and historical audits for Adobe-specific evidence and limitations.

**Search all** searches 2,423 records across full lesson text, reference entries, quiz text, stage challenges and complete field-guide text. Exact title matches rank first; title abbreviations such as `gsblur` and `curvs` work alongside full-text queries. Matching title characters and literal excerpt matches are highlighted. Filter by app or entry type; results open the exact entry. Search is loaded only when needed. In the library, press **Ctrl+K** from any reader to search all manuals. Use **↓/↑** to select results, **Enter** to open, and **Escape** to return to the input (or clear it when already there). Native Tab navigation and each reader’s own search remain available. **Compare keys** groups the 680 documented Windows shortcut records by matching key label, with each command and context kept separate. Matching keys do not establish equivalent behavior.

**Progress** exports/imports all three records together, including checkmarks, quiz answers, bookmarks, Premiere notes and preferences. Each reader also accepts its existing single-manual backups. Import an old backup through **App progress**, then export a new library backup. All three records must validate before a library import replaces anything. Reading preferences can be applied to all readers from the shared settings page. A later individual adjustment remains saved; reloading does not reapply the global defaults.

Progress is local to your browser profile and this copy of the library; it does not sync between host and VM. Local-file storage rules vary. If storage is blocked, the open session retains all three readers when switching apps; export before closing. Moving the folder, switching browsers or opening the standalone reader can use different local storage. Export/import is the reliable transfer method. On reload, the newer dated record is used when both the library and reader have saved progress. This also protects newer reader progress if a library-store write failed. There is no live cross-tab synchronization; export/import remains the transfer method between browsers or machines.

Use **Print manual** while reading, or Ctrl+P while the manual has focus. It prints the active reader, whose print styles expand focused practice steps. Browser-menu printing of the outer library page prints the library page; use the dedicated button for a lesson. **Open standalone** opens the current entry in its original reader. Complete Markdown editions and CSV references remain in each manual directory.

The reader works offline; this does not change Adobe activation, cloud AI or service requirements. Adobe exercises and Windows GPU-pass-through behavior must be checked in the actual installed applications.

## Project layout

```text
index.html                 Shared entrance, navigation and offline library
assets/                    Shared styles, controller, message bridge, generated indexes
manuals/photoshop/         Photoshop teaching material, reader, practice assets and sources
manuals/premiere/          Premiere teaching material, reader, guides, media and sources
manuals/after-effects/     After Effects teaching material, reader, samples and sources
scripts/build.py           Dependency-free library build; generates no archives
scripts/validate.py        Checksums, content preservation, local assets and native checks
tests/browser_test.py      Every generated route and primary offline workflows
tests/second_pass.py       Delayed messages, failed storage/imports and recovery
tests/search_logic.cjs     Ranking, abbreviation, Unicode and full-text retention checks
tests/search_browser.py    Offline fuzzy-search keyboard and visual regressions
tests/test_build.py        One-pass source freshness, deterministic outputs and traversal
docs/STRUCTURE.md          Structural analysis, integration decisions and maintenance contract
docs/AUDIT.md              Initial integration review
docs/SECOND_PASS.md        Integration findings, fixes and verification limits
docs/SEARCH_AUDIT.md       Fuzzy-search design, macro/micro review and test evidence
docs/original-files.json   SHA-256 baseline of all 137 supplied files
MANIFEST.sha256            Checksums of the shipped project, including nested manifests
```

## Maintain and verify

Reading requires no development tools. Building uses **Python 3.15+ and its standard library**:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

The regular build compiles the reviewed Photoshop/Premiere JSON snapshots and After Effects’ maintained authored source. It does not run Photoshop/Premiere’s historical authoring or enrichment scripts, rewrite research, regenerate sample media or package ZIPs. Historical source definitions and original audits are retained for traceability. See [docs/STRUCTURE.md](docs/STRUCTURE.md) before editing content.

Optional browser QA requires the development-only `playwright` package and its Firefox browser, plus system Chromium on Linux:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/playwright install firefox
.venv/bin/python tests/browser_test.py --browser both --exhaustive
.venv/bin/python tests/second_pass.py --browser both
.venv/bin/python tests/search_browser.py
```

The browser test selects system Chromium when available; for Firefox it uses Playwright’s installed build. No browser download or test dependency is needed to read or rebuild. Run browser tests before publishing reader changes. `scripts/build.py` refreshes checksums after deliberate edits; `scripts/validate.py` checks them without modifying files. No archive, nested Git repository or generated cache belongs in the project.

This is an independent educational project, not an Adobe product. The original sources contain no project-wide license grant; this integration does not invent one. Original synthetic assets retain their supplied usage notes.

## Before wiping or changing computers

The GitHub repository contains the complete manual, generated offline readers, media and source. Browser-local learning progress is separate: use **Progress → Export all progress**, and keep the downloaded JSON somewhere that survives the wipe. Restore it through **Import library backup** afterward. The project does not automatically upload your progress or notes to GitHub.
