# Field guide 04 — Export lab: codecs, containers, masters and quality control

**Read after:** L083–L090. **Goal:** Deliver the right file for the intended viewer, not merely click Export.

## Separate five independent properties

A **sequence** is an editing timebase and a list of instructions. A **preview render** stores temporary rendered frames that may speed playback; it is not automatically the final delivered file. An **export** constructs a new media file. A **container** (for example MP4, MOV or MXF) organizes tracks and metadata. A **codec** (for example H.264, HEVC, ProRes or DNxHR) defines the stream's representation. A codec may be supported in several containers, and a container does not guarantee a codec.

| Intended use | Typical starting point | Tradeoff to verify |
|---|---|---|
| Everyday web review | H.264 in MP4, appropriate audio | Broad compatibility and moderate size; compression artifacts at low rates |
| Smaller high-efficiency delivery | HEVC/H.265 if clients support it | May decode more slowly; hardware/bit-depth/rights support varies |
| High-quality interchange/master | A supported intraframe ProRes or DNxHR profile in appropriate wrapper | Large files; receiver must support chosen profile and exact alpha/color needs |
| Graphics with transparency | An alpha-capable codec or image sequence, with correctly configured alpha export | H.264 MP4 is not a general-purpose alpha delivery choice |
| Image sequence or VFX handoff | PNG/EXR or other supported image frames as specified by pipeline | Many files; frame numbering, color space and audio synchronization matter |
| Broadcast handoff | Exact broadcaster spec for wrapper, codec, channels, loudness and color | Never guess the requirement from “broadcast-quality” |

## Bitrate and size without fake precision

For a simple estimate, file size in bytes is approximately

`(video bitrate in bits/s + audio bitrate in bits/s) × seconds / 8`,

plus container overhead. For a **60-second** file with average 12 Mb/s video and 0.192 Mb/s audio: `(12,000,000 + 192,000) × 60 / 8 ≈ 91.4 MB`. VBR can move around an average/target, and the actual file can differ. A high bitrate does not recreate missing source detail; lower bitrate can be enough for low-motion/simple video but not a hard grainy concert.

**CBR** targets a steady data rate (depending on encoder implementation). **VBR** allocates more bits to complex moments and fewer to simple ones; quality and size depend on rate control mode and encoder. One-pass versus multi-pass, codec profile, reference frames, GOP length, hardware encoding, bit depth and motion complexity all matter. Hardware encoding can be fast but compatibility and visual results vary by card, codec, profile and driver.

## A repeatable deliverable process

1. Confirm required dimensions, frame rate, scan type, color space, codec, container, audio channels, loudness, maximum size and naming standard. For social destinations, confirm the *current* platform spec independently if the file is being delivered later than the guide date.
2. Review sequence settings and source frame rates; avoid accidental frame-rate conversions.
3. Save a milestone copy, remove disabled scratch tracks from export consideration, and set intended export range.
4. Choose a preset as a starting point; inspect every parameter against the brief rather than trusting the label.
5. Export a short 10–20-second difficult section first, with high motion, dialogue, titles and a fade if those are present.
6. Watch **the exported file**, not just the Program Monitor. Scrub first/middle/last frames and inspect black frames, audio dropouts, typo/caption position and color.
7. Inspect file properties (actual resolution/frame rate, codec profile, duration, audio sample rate, channels and bitrate). Check loudness with a suitable measurement tool when required.
8. Deliver the compressed viewing copy separately from the archival master; retain original source media and licenses.

## Failure isolation

- Export fails at one timecode: replace or temporarily disable one effect/transition in a **duplicate** sequence; check media corruption and plugins.
- Export is soft: compare source resolution, scaling algorithm, encoder bitrate and whether proxies/previews entered the export path.
- Video stutters but audio continues: check variable-frame-rate source, frame-rate mismatch or player decode capacity.
- Audio missing: inspect routing, track mute/solo, output channel mapping and whether the export includes audio.
- Color washed out: work through the four color pipeline decisions in field guide 03.
- File too large: compute bitrate budget first; do not solve size only by shrinking resolution if that breaks delivery requirements.

**Mastery:** Produce a documented web review MP4 and a separately specified high-quality master, verify both in an external player, and explain the tradeoff in your own words.
