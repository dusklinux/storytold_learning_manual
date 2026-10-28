# Research register and source limitations

**Edition 3.0 (comparative design review). Verification date: 2026-10-28.** The requested cutoff, October 29, is one day in the future; no later releases have been assumed. Version-specific claims are fixed to the Adobe Premiere desktop release **26.5.2 for Windows**.

## Official source register

| ID | Source / URL | Version relevance | Verified | Claim scope and notes |
|---|---|---|---|---|
| `release` | [Premiere desktop release notes](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html) | 26.5.2; latest release verified Oct 28 | 2026-10-28 | Official release notes last updated October 5 2026. |
| `new` | [What’s new in Premiere](https://helpx.adobe.com/premiere/desktop/whats-new/whats-new.html) | 26.5/26.x | 2026-10-28 | September 2026 features; patch fixes in release notes. |
| `home` | [Premiere desktop official help](https://helpx.adobe.com/premiere/desktop.html) | 26.x | 2026-10-28 | Navigation and entry point for current menus; broad source. |
| `keys` | [Default keyboard shortcuts](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html) | 26.x; doc Jan 2026 | 2026-10-28 | Adobe Windows shortcut tables; contextual conflicts possible. |
| `keycustom` | [Customize keyboard shortcuts](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/customize-keyboard-shortcuts.html) | 26.x | 2026-10-28 | See Edit > Keyboard Shortcuts; commands may be remapped. |
| `requirements` | [Technical requirements](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-pro-technical-requirements.html) | 26.5.2 | 2026-10-28 | Windows 11 24H2 minimum, hardware-specific acceleration, online activation. |
| `hardware` | [Hardware-accelerated decoding and encoding](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/hardware-accelerated-decoding-and-encoding.html) | 26.x | 2026-10-28 | Hardware capability depends on codec/profile/GPU/driver. |
| `formats` | [Supported file formats](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/supported-file-formats.html) | 26.x | 2026-10-28 | Codec/container support evolves. |
| `patching` | [Source patching](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/add-media-to-the-timeline-using-source-patching.html) | 26.x | 2026-10-28 | Destination for source insert and overwrite. |
| `targeting` | [Track targeting](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/work-with-clips-on-the-timeline-using-track-targeting.html) | 26.x | 2026-10-28 | Timeline targeting is not source patching. |
| `paper` | [Paper Edit](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/create-a-sequence-with-paper-edit.html) | 26.5+ | 2026-10-28 | New transcript selection assembly. |
| `effects` | [Modern Premiere effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/effects.html) | 26.2–26.5 | 2026-10-28 | GPU-accelerated modern effects including replacement Lens Flare and Channel Blur. |
| `transitions` | [Modern transitions](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/transitions.html) | 26.x | 2026-10-28 | Modern transition families. |
| `audio` | [Audio effects library](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/audio-effects-library.html) | 26.x | 2026-10-28 | Current list includes audio effects; defaults may be device-dependent. |
| `speech` | [Enhance Speech](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/enhance-speech.html) | 26.x | 2026-10-28 | Enhanced speech limitations and settings. |
| `color` | [Color grading overview](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/about-color-grading.html) | 26.x | 2026-10-28 | Color correction and grading overview. |
| `colorsettings` | [Color settings](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/color-settings.html) | 26.x | 2026-10-28 | Color interpretation and sequence output settings. |
| `productions` | [Productions](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/about-productions.html) | 26.x | 2026-10-28 | Shared production dependencies. |
| `issues` | [Known and fixed issues](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/known-and-fixed-issues.html) | 26.5 and later | 2026-10-28 | Issue table as of Oct 12 2026; not exhaustive. |
| `v27` | [Adobe community notice: upcoming v27.0 requirements](https://community.adobe.com/announcements-727/important-notice-upcoming-system-requirement-changes-in-v27-0-1639157) | 27.0 upcoming | 2026-10-28 | Future/beta, excluded from stable curriculum. |
| `effectchange` | [Effects and transitions changes in Premiere 26.0](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html) | 26.0; still relevant to 26.5.2 | 2026-10-28 | Authoritative active, Legacy, Obsolete and Removed inventories; later re-added effects tracked separately. |
| `playback` | [Play active sequence in Program Monitor](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-active-sequence-in-program-monitor.html) | 26.x | 2026-10-28 | Adobe explicitly documents Space, J, K and L playback controls. |
| `effectremove` | [Removed effects and transitions](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/effects-and-transitions-removed-from-adobe-premiere.html) | 26.x | 2026-10-28 | Explains obsolete/replaced effects behavior in existing projects. |

## Research ranking and cross-check method

1. Current Adobe release notes for version/patch and dated change claims.
2. Current Adobe help for workflows, terminology and UI; default keyboard command listing for shortcut rows.
3. Adobe system, supported-format, hardware and issue pages for environmental limitations.
4. The installed application would be the decisive check for panel layouts, applied effect names and user-remapped shortcuts; direct execution was not possible for this build.
5. The project distinguishes official stable support, legacy/obsolete/removed distinctions and unresolved entries, beta functionality and externally processed features rather than silently treating them as equivalents.

## Reconciliation and remaining conflicts

| Question | Resolution / confidence | Follow-up in Premiere |
|---|---|
| “Premiere” versus “Premiere Pro” | Adobe uses the shorter Premiere desktop branding on current documentation; “Premiere Pro” remains recognizable historical terminology | Check `Help > About Premiere` for installed build |
| 26.5.2 vs announced 27.0 | 26.5.2 latest stable verified on date; v27 listed as upcoming | Revisit Adobe release notes after Oct 28, 2026 |
| Old Essential Graphics tutorials | Modern Properties panel is primary for many selected graphics controls | Verify current Properties workflow and any workspace-specific differences |
| 26.x effects categorization | **145** video/audio rows: distinguish published active, modern replacements, Legacy, Obsolete, Removed and unresolved. No installed-seat inventory check | Test exact processing identity, controls and effect list in installed 26.5.2 |
| Windows shortcut default vs customized | **182** documented Windows rows; Adobe menu/panel table and separate playback reference. Local customization and focus affect results | Compare to `Edit > Keyboard Shortcuts` with the intended panel active |
| AI generation “offline” | Installed feature does not imply offline availability; service/credits/entitlements are separate requirements | Inspect current account dialog and Adobe service terms |
| GPU and VM support | Supported *native* system specs do not certify arbitrary hypervisor passthrough or 4:2:2 hardware support | Test actual guest GPU, decode and encoder separately |
| Premiere UI exact paths | Official docs were used, but no live application was available for final click-through validation | Validate workflow against installed Windows 26.5.2 |

## Why some sources do not prove every detail

Adobe often documents an effect category and selected examples rather than publishing a dated, machine-readable “complete installed effect inventory” tied to a particular patch. Old tutorials and legacy catalogs can include effects that were renamed, hidden, deprecated, bundled differently or require third-party products. The database’s `status` field is intentional and makes verification gaps visible.

All documentation URLs in this register are **references only**. The course itself never fetches data from these URLs and can be read with the internet disabled.
