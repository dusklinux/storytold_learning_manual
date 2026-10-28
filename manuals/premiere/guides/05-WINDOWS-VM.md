# Field guide 05 — Premiere in a Windows virtual machine, manual on Linux

**Read after:** L005, L014, L097. **Goal:** Know what virtualization does and does not promise.

This manual is static local HTML, CSS and JavaScript. You can extract it and read it in an ordinary Linux browser while Premiere runs separately in Windows. **The editing application is Windows-only in this course**; no Linux menus or Linux-only editing workflows are presented.

Adobe's Windows system requirements describe supported native Windows hardware and software. A Windows VM having a nominally supported Windows version does **not** prove Premiere or a GPU path inside it is supported or fast. Hypervisors, virtual graphics adapters, remote-display layers and passthrough setups vary substantially. Verify with your installed Adobe build, your hypervisor, your physical GPU and your driver combination.

## A capability checklist

| Area | What to verify | If absent or weak |
|---|---|---|
| GPU adapter | Does the guest see a capable, supported physical GPU or only a virtual display adapter? | Use software paths where supported; avoid GPU-heavy effects and HDR grading assumptions |
| GPU passthrough | Is device passthrough correctly isolated, driver-installed and permitted by the host? | Don't assume a virtual 3D adapter equals dedicated video hardware |
| Hardware decode | Does the exact source codec, chroma format, bit depth and profile decode in hardware in this guest? | Create intraframe proxies or transcode; inspect CPU utilization and dropped frames |
| Hardware encode | Is encoder support actually exposed for the requested profile? | Use software export where available and allow more processing time |
| Memory | Is RAM reserved for guest, host and GPU, with adequate headroom? | Reduce concurrent apps, use proxies and smaller previews; avoid swapping |
| Storage | Are source, cache, previews and export on fast, reliably mounted volumes? | Prefer fast local guest-accessible storage; test shared-folder throughput |
| Audio | Is a stable output device and sample rate recognized in guest? | Check Windows audio device, Premiere hardware preferences and remote audio latency |
| Color | Is guest display pipeline accurately color-managed? | Avoid treating remote desktop/virtual display as a grading reference |
| Licensing | Does Creative Cloud activation work in guest? | License, connectivity and device policies are separate from this offline manual |

## Conservative setup

1. Confirm Premiere version and Windows guest build from their own About/System screens; record CPU/GPU/RAM/driver/hypervisor configuration.
2. Test a known 1080p25 sample MP4 in a **new empty project** before moving a real job into the VM.
3. Record playback smoothness with no effects, then with Lumetri and one scaled clip; note actual frame drops, not subjective “looks fast.”
4. Test Media Encoder/software export and playback of its exported result; measure wall-clock export time for a 15-second sample.
5. If decode is slow, make proxies from **originals**, enable them for editing, then verify masters reconnect correctly for final output.
6. Keep project files and source on stable paths. VM shared-folder remounts may change Windows paths; moving only the `.prproj` does not move camera originals.
7. Maintain a native Windows fallback when a client deadline or color-critical work makes VM uncertainties unacceptable.

## Cross-machine progress

The website may store completion, bookmarks, notes and quiz choices in browser-local storage. **That storage is not synced between Linux and Windows.** Use **Export progress** in the top bar to save a JSON file, copy that file between computers by your usual trusted method, and use **Import** in the other browser. Import replaces the current browser's study record after confirmation. If a browser blocks persistence on local files, export before closing the page. None of this requires a network connection.

**Mastery:** Report exactly which GPU/codec/acceleration functions are *observed* inside the guest, distinguish them from theoretical hardware support and demonstrate a successful archival export using original footage.
