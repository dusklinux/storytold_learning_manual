# Field guide 12 — End-to-end professional edit, compliance and QC pipeline

## Define delivery before production

A professional workflow begins with a **delivery specification**, not with a codec preset. Ask the receiver for picture dimensions, exact frame rate, color space/transfer, desired bit depth/profile, audio channel order/sample rate, loudness or true-peak thresholds, subtitle format, aspect versions, maximum file size, deadline and permitted media rights. If the receiver provides only a social-platform name, treat presets as starting points rather than a formal contract.

## Stage gates

| Gate | Check | Proof |
|---|---|---|
| 1. Intake | Source files copied safely, rights recorded, codec/fps/audio formats inventoried | Source manifest and backup count |
| 2. Project structure | Stable Windows paths, bins, autosave and scratch plan | Reopen project without relinking |
| 3. Assembly | Narrative beginning/middle/end, selected takes, stable source references | Rough-cut review file |
| 4. Picture lock | J/L cuts, continuity, handles, approved story and exact duration | Locked edit version and change log |
| 5. Sound finish | Noise repair is mild; clip gain before track mix; meters verify delivery | Integrated loudness report and listening log |
| 6. Image finish | Input interpretation and sequence management verified; scopes and shot match | Color QC stills and reference monitor notes |
| 7. Text finish | Graphics safe, spelling correct, caption timing accurate | Subtitle proofreading pass |
| 8. Export | Correct container/codec/frame rate/pixel aspect/caption mode | Independently played encoded files and metadata |
| 9. Handoff | Receiver can extract, relink and open project; asset rights included | Archive restoration test |

## High-risk distinctions to explain before working

**Sequence versus export.** A 1080p sequence can be exported at 4K, but upscaling cannot recover native detail. A 4K sequence can be exported at 1080p while requiring appropriate downscaling. Sequence settings and export settings are independent decisions.

**Codec versus container.** H.264/H.265 are codecs; MP4/MOV are containers. A MOV is not inherently archival; it depends on the stream codec, profile, bit depth, color metadata, audio and long-term decoding environment.

**Proxies versus masters.** Proxies speed interactive editing. Confirm online originals before making the approved delivery, and avoid exporting lower-resolution proxy imagery accidentally.

**Loudness versus peak.** Integrated LUFS approximates overall perceived loudness; sample peak dBFS and true peak measure different risks. Do not satisfy one by ignoring the others. Never invent a universal streaming loudness requirement—specifications vary by receiver.

**Color.** A Log camera clip must be interpreted against its actual camera transfer/gamut. A display-referred creative LUT is not a reliable substitute for an input transform. After export, compare on known-managed viewing paths and document display differences.

**Captions.** “Burn-in” is drawn into video pixels; a sidecar such as SRT supplies text/timing but generally cannot reproduce rich styling. Embedding into a video container is format/profile constrained; verify the specific receiver/player.

## Five failure-injection tests

1. **Offline media:** rename a copy of a media directory and verify relinking; restore original paths afterward.
2. **Unsupported decoder:** transcode a duplicate of problematic compressed footage to a supported editing codec and compare behavior while preserving original source.
3. **Broken color:** deliberately assign incorrect input color settings in a test copy; compare scopes and identify the cause rather than compensating with saturation alone.
4. **Caption mismatch:** export SRT and burn-in as separate controlled tests; view the SRT in a media player to understand style loss.
5. **Damaged handoff:** move the archive to a new directory and reopen the project. If source references fail, the package is not yet finished.

## Receipt-quality handoff manifest

Record: delivery ID; Windows Premiere patch; project file version; sequence names; original folder layout; count of media files; proxy/media dependencies; footage/music/fonts/LUT licenses; required plug-ins; export format and encoder; dimensions; frame rate; color primaries/transfer; bit depth; audio channels, sample rate, integrated loudness/peak values; caption file(s); checksums where required; reviewer/date; and any exception.

**Final acceptance:** all deliverables open in independent playback, start/end are correct, speech is intelligible, music isn't accidentally clipped, captions match text and timing, picture contains no unintended black frames or bad masks, and the project can be recovered from the delivered archive.

## Using the included practice media

The bundled samples are original, generated media for technical exercises. They cannot substitute for filmed conversations, emotional performance or complex production footage. For narrative capstones, record your own authorized interview/action shots; do not import copyrighted commercial videos or music without permission.
