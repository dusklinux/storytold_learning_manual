# Maintaining the Photoshop Field Manual (Windows, Photoshop 27.11)

This project uses **a single editorial source of truth**: `scripts/author.py`, `scripts/references.py`, `scripts/second_pass.py` and `scripts/build.py`. Do not edit generated `content/content.json`, `assets/content.js`, `ALL_CONTENT.md`, `CURRICULUM.md`, `SOURCES.md` or the CSVs independently; rebuilding will overwrite them.

- Preserve durable lesson IDs (`s01l01` … `s12...`) and the order of each lesson's completion checklist unless you deliberately migrate progress. Checks are saved as `lessonID:index`; changing their meanings requires an explicit migration, not silently reusing old checkboxes.
- Keep Photoshop Windows commands grounded in official Adobe desktop documentation for the verified release. Mark Beta, removed, cloud-dependent and conditional features explicitly. The included reference data is curated, not an extracted installed-command registry.
- `web/index.template.html` and `assets/style.css`/`assets/app.js` are the maintainable browser source. `scripts/build.py` embeds the CSS, data and app into `index.html` for `file://` portability. Keep all external images and diagrams in the package; using the index alone omits those visual assets.
- Maintain progress compatibility deliberately. Edition 1.2 imports earlier compatible 1.0/1.1 JSON exports for the same Photoshop 27.11 target. Import validates IDs and preferences, asks for confirmation, and never silently discards bad records. Local browser state remains under the existing `photoshop-manual-progress-v1` key, so updates in place do not lose it. Use an exported backup when moving folders or machines.
- Build uses Python 3 and Pillow for generated sample images. The browser reader itself needs no Python, Node.js, network, or server.

Run from the project directory:

```sh
python scripts/build.py
python scripts/validate.py
python scripts/audit_second_pass.py
node --check assets/app.js                # optional development check
python scripts/browser_test.py           # needs Playwright + Chromium; inline test
python scripts/browser_extended.py       # needs Playwright + Chromium; offline browser simulation
python scripts/check_manifest.py --write
python scripts/check_manifest.py --check
python scripts/package.py /path/to/output.zip
```

`file://` navigation is administrator-blocked in the publishing environment. Browser tests use the actual inline web reader in a controlled, offline Chromium page, **not** an unrestricted local-file launch. The product’s Photoshop GUI, third-party VM drivers and printer proofs were not executed in this publishing environment; these remain separate verification requirements.
