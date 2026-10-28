# Field guide 13 — Version verification, technical uncertainty and reproducible testing

## What a passing test does and does not establish

An automated lesson-ID check proves that references resolve. A browser DOM test proves that **tested controls operated in that browser test context**. Neither proves that a 26.5.2 feature exists in an installed Windows copy. A dated Adobe release note proves that Adobe documented a capability for the release; it does not prove account eligibility, credit pricing, source-format compatibility or GPU behavior on a specific Windows VM.

Use four confidence levels:

1. **Adobe-published current:** release note or current Adobe help identifies the feature/name/command and release or category.
2. **Adobe-published historical/Legacy/Obsolete/Removed:** archival or migration reference; should not be taught as an ordinary current effect.
3. **In-app reproducible:** exact Windows build and keyboard preset tested, with before/after media and a recorded procedure. **Not achieved by this manual's author in this environment.**
4. **Open hypothesis:** incomplete current catalog support, unsupported hardware profile, external account or plugin-dependent result; require further evidence.

## Patch-specific revalidation checklist

Record the installed version via Help > About Premiere (or the equivalent Help > About dialog visible in your seat), then compare:

- Release notes and hotfixes since 26.5.2.
- The available named video effects, audio effects and transitions within the Effects panel, including whether a row says Legacy.
- `Edit > Keyboard Shortcuts` command name, default key set and active context. If a key is user-customized, report that difference rather than changing the whole course.
- Properties, Text, Effect Controls, Export, Color and Audio panel locations.
- The complete media path/proxy path and the specific hardware decoding/encoding profiles used in the project.
- Cloud/AI feature's service status, account, entitlement, model and credit prompt before using it.
- Captions: transcript features, editable text, export burn-in/sidecar/embedding options.
- Installed plug-ins, font availability, LUT dependencies and hardware drivers.

## How to report a suspected manual error

Record the lesson/row ID, the exact statement, Adobe version and Windows build, current screenshot or menu label, chosen workspace/keyboard preset, precise reproduction steps, actual versus expected output and a current official source URL if possible. Mark the claim as **correct**, **context-sensitive**, **changed after publication**, **historical only**, or **unverified**. Avoid untraceable claims such as “Premiere always does this.”

## Explicitly untested here

This package was tested using published documentation, data integrity scripts, media probes and headless Chromium DOM interactions. The automation environment blocked `file://` top-level navigation. No unrestricted Linux/Windows file-origin browser run, native Windows keyboard-preset inspection, real Premiere export or Windows VM GPU passthrough test was available. These are residual deployment gates, not success claims.

## Source priorities

1. Adobe [release notes](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html) to establish stable version and chronology.
2. Adobe [default shortcuts](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html) for documented Windows keys.
3. Adobe [26.0 effect migration inventory](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html) plus [modern effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/effects.html) for currently named replacements.
4. Adobe [technical requirements](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-pro-technical-requirements.html) and media/codec documentation for support boundaries.
5. Real Windows installation and asset-specific test for final deployment validation.

A good manual explicitly distinguishes **what was researched**, **what was independently tested**, and **what a learner must verify on their seat**.
