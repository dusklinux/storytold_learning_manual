# Field guide 06 — AI-assisted editing in the verified stable release

**Read after:** L076–L082. **Goal:** Use automation with clear provenance and truthful offline expectations.

This guide uses Adobe Premiere **26.5.2** as the latest stable version verified on **2026-10-28**. The requested research date of October 29, 2026, had not yet occurred. Later updates, account-specific controls or cloud service changes may differ. The following is a **capability map**, not a promise that all features run in every installed seat.

| Capability | Stable-release status by Oct 28 research | Important boundary |
|---|---|---|
| Transcription and text-based editing | Established desktop functionality | Language/model support, download and connectivity may be configuration-dependent |
| **Paper Edit** | Added in 26.5 | Build a sequence from transcript selections; verify edits and speaker/context carefully |
| **Generative Media Tool** | Added in 26.5 | Adobe service, supported model, account eligibility and potentially credits required; not an offline operation |
| **Generative Extend** | Stable in current product, expanded availability in 26.5 | Generated frames/audio may require remote processing, supported media constraints and generative credits |
| **Object Masking** and smoothing | Stable, with smoothing enhancements in 26.5 | Inspect edges, occlusion, temporal drift and performance on actual footage |
| **Enhance Speech** | Supported Adobe audio workflow | Quality is input-dependent; verify current processing requirements in your installed version |
| Automatic Reframe, scene detection, captions | Established assisted workflows | Always review crop, cut points, spelling and reading speed |
| **AI Assistant** | Beta/not established as 26.5.2 stable | Not taught as a stable required step in this course |
| Premiere 27.0 | Future/upcoming as researched | Do not attribute announced changes to stable 26.5.2 |

The exact naming and UI location of a fast-changing service can move between updates. Verify using Adobe's live current documentation **when online**, but this course remains usable offline for concept study. A feature being installed does not necessarily mean cloud generation is possible while offline; a connection and service entitlements can be separate constraints from application launch.

## Responsible generated-media procedure

1. Choose a task such as extending a shot for a transition where generated content is appropriate, rather than covering essential documentary evidence.
2. Work in a duplicate sequence and preserve a record of the original source extent.
3. Confirm whether the action calls a remote model and what service terms, limits, credit costs and copyright/client approval apply to your account.
4. Generate only appropriate content and compare the added frames with adjacent source, paying attention to hands, text, logos, geometry, motion and continuity.
5. Check audio artifacts, resolution, color changes, duration and whether the generated result is approved for the intended client context.
6. Keep source, generated results and editorial decisions distinguishable in bins, naming and delivery documentation.

## Text-assisted editing checks

A transcript helps locate candidate cuts but is not authoritative: false words, speaker confusion, overlapping dialogue, abrupt cuts and context changes occur. Verify critical claims by listening to source recordings, viewing edit boundaries and checking whether picture continuity still works. For subtitles, correct the text and timing manually and check readability, especially where one-word caption styles create high visual density.

**Mastery:** Identify which AI operation is available offline, requires services or remains beta; describe its failure modes; and provide a human-reviewed export rather than relying on the automated preview alone.
