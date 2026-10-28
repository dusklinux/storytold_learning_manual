# Publication audit — Photoshop Field Manual 1.2.0

**Revised:** October 28, 2026. **Target:** Photoshop 2026 27.11 on Windows. **Offline reader:** Linux and Windows.

The **current comparative and third-pass quality audit** is **[AUDIT_CROSS_MANUAL.md](AUDIT_CROSS_MANUAL.md)**. It records changes borrowed from the user-provided After Effects project, rejects irrelevant transfers, and reports additional browser and integrity tests.

The foundational macro and micro Photoshop accuracy audit for edition 1.1.0 is **[AUDIT_SECOND_PASS.md](AUDIT_SECOND_PASS.md)**. Read that report for all corrections, validated checks, the source evidence, and explicit remaining verification limits.

The original edition 1.0.0 audit is preserved as **[AUDIT_INITIAL_1.0.0.md](AUDIT_INITIAL_1.0.0.md)** for transparency. Its inventory counts and findings describe the **superseded 1.0.0 edition**, not the current distribution; do not use them as a specification for 1.2.0.

## Current publication inventory

- 12 curriculum stages, 75 sequential lessons and associated knowledge checks; 12 substantial stage projects.
- 71 tool entries; 81 effect/filter references (**including one historical, removed filter**); 112 Windows shortcut/gesture rows; 155 glossary concepts; 30 troubleshooting entries; 40 recipes.
- A self-contained offline HTML reader with search, bookmarks, progress, quizzes, validated JSON transfer and reading/contrast controls; full Markdown and six CSV reference exports.

## Verification boundary

Automated source consistency, reference checks and offline Chromium interaction tests pass. No native Photoshop installation was available for a full per-command 27.11 Windows GUI check; no Windows VM/GPU or printer integration test was possible. Browser testing executes actual Chromium DOM interactions in inline pages, including the complete generated index.html HTML, rather than directly opening file:// URLs, which are restricted by the managed test environment.

**Do not interpret this publication as proof that every shortcut, filter mode, menu route, hardware requirement, third-party/cloud service or localized UI state was exercised.** Confirm disputed shortcut assignments with Photoshop's own Edit > Keyboard Shortcuts on the intended installation.
