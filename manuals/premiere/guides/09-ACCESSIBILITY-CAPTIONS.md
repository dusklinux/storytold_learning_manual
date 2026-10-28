# Field guide 09 — Titles, captions, transcripts and accessible review

**Read after:** L062–L068. **Goal:** Know which text artifact your audience and client actually needs.

A **title/graphic** is visual design inside the picture. A **transcript** is a text representation of spoken language, usually with timestamps or speaker information; it can support Paper Edit and text-based editing. A **caption track** contains timed text intended to be read alongside audio. **Open/burned-in captions** are permanently visible in image pixels; **closed/selectable captions or subtitle files** can often be toggled in compatible players or platforms. The precise terminology and support depend on the delivery format and player.

## Practical distinctions

| Requirement | Appropriate starting workflow | Necessary check |
|---|---|---|
| Names and lower thirds | Text/graphics and current Properties panel | Safe area, contrast, spelling, timing and brand consistency |
| Readable speech captions | Transcript review → timed caption segments | Accuracy, speaker attribution, line breaks and reading rate |
| Selectable subtitle sidecar | Export requested SRT or compatible sidecar format | Frame rate/timebase, encoding, exact beginning/ending and platform ingestion |
| Burned-in visual captions | Render captions into the video only when specified | They cannot be disabled, and visual placement affects reframe |
| Localization | Separately proofread translations and timings | Do not mistake machine translation for human language review |

In current Premiere documentation, many title-editing controls live in the **Properties** panel, not in the historical Essential Graphics Edit panel shown in old videos. Check the installed build rather than applying outdated UI steps from screenshots.

## Accessibility is practical

Use sufficient luminance contrast over moving backgrounds; a short drop shadow or unobtrusive backing shape can help. Avoid forcing a viewer to read large blocks while a complex visual action occurs. Keep text inside the delivery's safe composition area, including vertical reframes and smartphone UI overlays. Identify speakers when needed, and represent meaningful non-speech sounds if the caption standard calls for it.

Automatic transcript/caption tools are draft assistants, not final proofreaders. Common errors include names, specialized terms, numerals, homophones, speaker overlaps, sound effects and phrase boundaries. A one-word-per-caption creative style may be visually trendy but can harm readability in some contexts. Client specification and audience take priority over the style preset.

## Repeatable exercise

1. Record 30 seconds of narration yourself or obtain consented speech.
2. Generate a transcript using a supported workflow. If unavailable offline, transcribe manually.
3. Correct every word by listening to the original, paying attention to names and punctuation.
4. Create caption segments with intentional phrase grouping and timing; watch playback at 1×.
5. Design one lower third using the Properties panel, checking margins in a 16:9 and 9:16 mockup.
6. Export a caption sidecar and an optional caption-burned review. Confirm which is actually required by the brief.
7. Reopen the SRT in a plain text editor and check first/last cues, UTF-8 characters and a random middle cue.

**Mastery:** Explain the differences among graphics, transcripts, captions, SRT sidecars, and burned-in text; demonstrate a proofread accessible delivery instead of trusting automated text blindly.
