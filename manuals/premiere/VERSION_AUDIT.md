# Release-specific feature and compatibility audit

**Target:** Adobe Premiere desktop **26.5.2** for **Windows**. Research date **2026-10-28**. Adobe release notes current then and last updated October 5, 2026; future October 29 publication cannot be verified yet.

## Version-specific release matrix

| Subject | Version | Stable by audit | Notes |
|---|---|---|---|
| Stable release | 26.5.2 | Yes | Sept 2026 patch, release notes updated Oct 5 2026; latest verified as Oct 28 |
| Generative Media Tool | 26.5 | Yes, service-dependent | Timeline video/SFX generation; connection, account, credits/model vary |
| Paper Edit | 26.5 | Yes | Transcript selections create sequence |
| Object Mask smoothing | 26.5 | Yes | Improved smoothing controls; verify edges throughout |
| Object Mask tool | 26.0 | Yes | AI selection/tracking supported; asset/processor conditions apply |
| Single-word captions | 26.3 | Yes | Style/export behavior is caption-workflow dependent |
| Sequence Index | 26.2 | Yes | Searchable timeline index |
| Film Impact-powered modern effects | 26.2 | Yes, per component | Includes Channel Blur, Gradient, Noise and 3D Spinback/Slide |
| Generative Extend expanded footage | 26.5 | Yes, service-dependent | 360p–4K UHD etc per Adobe release summary; check individual constraints |
| ProRes RAW native controls | 26.5 | Yes, format-dependent | Camera/hardware/driver restrictions |
| Hardware 4:2:2 10-bit AVC/HEVC MXF NVIDIA Blackwell | 26.5 | Yes, hardware-dependent | Do not generalize to older GPUs or VM virtual adapters |
| AI Assistant | Beta | No | Explicitly excluded from stable curriculum, appendix only |
| Premiere 27.0 | Future/upcoming as verified Oct 28 | No | Adobe community announced planned Windows requirements; no stable release verified |
| Essential Graphics Edit workflow | Legacy | Not as older tutorials teach | Use modern Properties panel for many graphic edits |
| Effects catalogue | 26.0–26.5.2 | Adobe taxonomy cross-checked; installed inventory untested | Separates active, Legacy, Obsolete, Removed, new replacements and unresolved names in exported data. Exact installed controls require a Windows Premiere test. |
| 26.0 effects removal/legacy migration | 26.0 | Yes | Modern named effects replace or coexist with historical plug-ins; old removed variants may fail to render in legacy projects. |
| Windows shortcut audit | 26.0–26.5.2 | Reference verified; live UI untested | Expanded Adobe default keyboard table, plus separate Adobe playback J/K/L verification; conflicts explicitly panel-scoped. |

## Stable-release teaching decisions

- Teach current **Properties panel** workflow for many graphics operations and annotate older Essential Graphics tutorials as historical.
- Include **Paper Edit** and the **Generative Media Tool** as 26.5 features, with explicit transcript/service constraints.
- Include Object Masking, generative extension and AI assistance as *reviewable tools*, not infallible one-click outputs.
- Keep Premiere 27.0 and AI Assistant outside mandatory 26.5.2 stable-release lessons.
- Verify all Windows shortcuts by active panel context and `Edit > Keyboard Shortcuts` when installed.
- Treat export color, codec profile and source hardware compatibility as coupled technical specifications, not one-size-fits-all presets.

## Requirements and offline boundary

Adobe’s current Windows technical requirements for this release list Windows 11 **24H2** as minimum. Full GPU acceleration, H.264/HEVC hardware decode/encode and newer chroma/bit-depth profiles depend on actual hardware and drivers. A Windows guest in Linux is not guaranteed to expose the host’s GPU, encoder or calibrated output; see `guides/05-WINDOWS-VM.md`.

The **HTML course** runs entirely from bundled local files. **Premiere activation**, many AI model calls, cloud collaboration, asset stores and credits/payment services are separate and may require online services, login or an additional plan. Adobe Media Encoder, After Effects, Audition and Photoshop are companion software; the guide describes their role without assuming they are owned.

## High-risk claims awaiting in-application confirmation

- Complete patch-specific installed effect/transition inventory, and exact Premiere support for some legacy audio effect names.
- Every individual shortcut when default shortcuts have been changed or an unexpected panel has focus.
- Exact UI details in rolling cloud product updates or account-gated experiments.
- Guest-GPU decode/encode with Blackwell, HEVC 4:2:2 or RAW without checking supported profiles.
- Current online credit pricing or available third-party AI models; service contracts can change.

These uncertainties are marked openly in data, lessons, CSVs, field guides and the final audit.
