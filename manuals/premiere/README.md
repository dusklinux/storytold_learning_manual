> **Combined project:** open [the Dusky library](../../index.html) to choose or switch apps. This directory retains the supplied manual and its historical standalone documentation below. Use the [root build and maintenance instructions](../../docs/STRUCTURE.md); the library build generates no archives.

# Premiere, Explained — Windows edition · fully offline reading

**Release target:** Adobe Premiere desktop 26.5.2 for Windows, latest stable verified from Adobe's release notes on **October 28, 2026**. The requested October 29 research cutoff was still in the future. This is an independent learning manual, not a product of Adobe.

## Open the manual on Linux or Windows

1. Extract the **entire ZIP** to an ordinary folder, preserving `index.html`, `.js`, `.css`, `guides/`, `data/`, and the other directories. Do not run the site from inside the ZIP preview.
2. Open `index.html` in a current desktop browser (Chrome/Chromium, Firefox or Edge) by double-clicking, or use **Open File** from the browser. No local server, Python, Node, npm, Adobe login, web connection, installation or CDN is required for reading.
3. Choose **Start with lesson 1**. Follow stages 1–14, check off practice steps, complete the knowledge checks and open the separate reference sections when working.
4. When using Premiere, follow only the **Windows** menu paths and Windows keyboard shortcuts provided here. The browser manual can run on Linux while the editing application runs in a Windows VM or separate Windows computer.

The site loads **only adjacent local files** through normal `<script src>` and `<link rel=stylesheet>` references. It does **not** use `fetch()`, JavaScript modules, service workers, CDNs or remote fonts. External Adobe documentation is linked for provenance, but never needed to display core lessons, guides or reference entries. No browser add-on or local server is required.

## Navigate and learn

- **Learn:** 14 stages, **105 guided lessons**, **42 quiz questions** with saved answers, practice checkboxes, lesson completion, next/previous and clearly marked prerequisites.
- **Reference:** 182 Windows shortcut records, 145 video/audio effect entries (with Adobe-listed/legacy/obsolete/removed/unresolved classifications), 91 transitions, 25 panels/tools, 107 glossary entries, 30 workflow recipes and 37 symptom-based troubleshooting guides.
- **Field guides:** Thirteen long-form technical guides explaining editing geometry, audio, color, encoding, VM performance, AI services, capstone delivery, timecode and accessible captions.
- **Search:** Use the search bar or press `/` outside a text field. Search scans lessons and the reference databases, plus field-guide summaries. Search results now open the exact effect, shortcut, transition, glossary term or panel, not merely the top of its catalog.
- **Bookmarks and notes:** Use the bookmark button and the note box on lessons. Light/dark mode persists if browser storage is available. The **Reading & progress settings** page also offers larger text, higher contrast and one-step exercises; printing expands all practice steps.

## Move progress between Linux and Windows

Completion, quiz answers, bookmarks, checklist steps, notes and theme are saved **in this browser only** when the browser allows local storage. They **do not** sync between browsers, user accounts or computers. Click **Export progress** to download a `.json` file and **Import** on the other device. Exports from the earlier v2 manual remain importable with the same lesson IDs; new reading preferences default to off. Imports validate known lessons, exercise steps, quiz choices and note types before changing any state. Import explicitly **replaces** the destination browser's progress; retain your previous export if you might need to reverse the change. On smaller screens, export/import are also available in the sidebar.

Some browsers block or clear `localStorage` for `file://`. In that situation the app still works for the current page session, but you should export JSON **before closing** to keep your work. No cloud service or database is involved. Avoid importing JSON files from unknown sources, even though this app treats imported progress as text.

## Sample material and exercises

Original video patterns and synthetic audio are in `sample_media/`. See `sample_media/README.md` for their technical specifications and permissive educational-use notice. Realistic dialogue/interview lessons ask you to record your own authorized speech and footage; no commercial stock/media purchase is required. Some named optional Adobe ecosystem services are educational context only, not prerequisites.

## Technical boundaries

- **Adobe Premiere itself** requires its own compatible Windows environment, licensing and potentially Creative Cloud connectivity. The offline manual does not make cloud AI, online account services or Generative Media available offline.
- The exact release and some AI features are time-sensitive; 26.5.2 is a fixed research snapshot, not an automatically updating resource. Check `SOURCES.md`, `VERSION_AUDIT.md` and the site source desk.
- Standard shortcut layouts can be remapped and are context-dependent. Confirm active panel and **Edit > Keyboard Shortcuts** in your installation.
- A Windows VM may lack effective GPU acceleration, hardware decode/encode, calibrated video display or reliable shared storage. Start with `guides/05-WINDOWS-VM.md`.
- The effects database separates Adobe-listed active, Legacy, Obsolete, Removed, newer replacements and unresolved effects; neither Adobe documentation alone nor this environment establishes the complete installed 26.5.2 inventory or every effect parameter.

## Additional formats and maintenance

`ALL_CONTENT.md` contains the entire course, reference sections and the thirteen additional field guides in a portable text edition. `CURRICULUM.md` contains lesson order, required prerequisites, stage projects and skill bands. CSVs are independently sortable reference exports. `scripts/rebuild.py` regenerates the course database, Markdown and field-guide bundle from maintained source definitions; rebuilding requires Python and the `mistune` library, **but reading the shipped website requires neither**. `scripts/validate.py` performs static integrity checks; it needs only Python's standard library. `MANIFEST.sha256` authenticates all extracted files; verify it with `python scripts/check_manifest.py`. `scripts/package.py` reproducibly builds and checks a ZIP from maintained files. `COMPARATIVE_AUDIT.md` explains the design improvements borrowed from the supplied After Effects manual and what was deliberately excluded. Optional development-only Playwright tests can run `python scripts/comparative_browser_regression.py`.

## Test limits

Automated runtime UI tests were performed against an inlined copy of the published local HTML, CSS and JS with headless Chromium, including 749 content routes, adverse progress imports and reading preferences. The testing environment policy blocked navigation to both `file://` and localhost, so direct file URL behavior on actual Linux/Windows desktops was **not personally verified**. A Windows installation of Premiere and a real Windows browser were not available for execution testing. See `AUDIT.md` for precise coverage and residual issues.
