# Field guide 03 — A reliable color pipeline from camera signal to delivered file

**Read after:** L055–L061. **Goal:** Distinguish technical interpretation from creative appearance.

## The four separate decisions

1. **Identify camera input.** Determine source color gamut, transfer function, bit depth and whether media is standard video, Log or RAW. The filename extension alone is not enough.
2. **Choose working/output intent.** Establish SDR Rec.709 or a justified HDR specification early, and confirm the actual sequence color-management settings in this Premiere version.
3. **Normalize the input.** Apply the correct supported input interpretation/transform where necessary, avoiding a second transform to already normalized media.
4. **Grade creatively and deliver.** Balance white point, exposure, contrast and skin tones across shots, then export with coherent target metadata; view the actual output under controlled conditions.

A camera Log encoding is deliberately flat looking when viewed without its intended transform. Applying random creative LUTs until the image “pops” is not equivalent to choosing the correct camera input transform. A **technical LUT/transform** maps signals into a working/display space. A **creative LUT** changes appearance. Creative grading may happen before or after specific transforms depending on the intentional pipeline; the critical point is to know what signals the operation expects.

## SDR and HDR essentials

**Rec.709** describes a widely used HDTV color system, but real output appearance also depends on transfer functions, display calibration, operating-system display management and video-player interpretation. “HDR” is not just brighter SDR: an HDR pipeline involves appropriate source dynamic range, working/output transfer functions, bit depth, compatible monitors and metadata. Do not assume a normal 8-bit monitor accurately previews an HDR grade.

**Scopes are measurement tools, not taste meters.** A waveform helps compare luma distribution, RGB parade helps identify channel imbalances, vectorscope helps evaluate hue/saturation tendencies. None guarantees a perfectly matching image without lighting, viewing conditions and content judgment. Skin tones occupy a family of hues, not a magic line to which every complexion should be forced.

## Why exported color can differ

Before blaming an encoder, check these variables separately:

- Source interpretation: was Log or RAW recognized and transformed correctly?
- Sequence working color space and tone mapping: is the sequence SDR while footage was HDR?
- Export settings: what color tag, bit depth and codec were actually written?
- GPU/display monitoring: was the display calibrated and was color management enabled?
- Player differences: is an external viewer applying its own transfer conversion or metadata interpretation?
- Comparison method: are you comparing the same frame at the same brightness and display configuration?

Do a **short 10-second test export** with a neutral gray/skin reference and two difficult highlights. Reimport it into Premiere, check scopes/metadata, compare in another managed application, and write down the settings. Reimport comparison is informative but not proof that every external viewer will match.

## Color correction drill

1. Pick a 15-second cut containing three camera angles; include a neutral wall/object.
2. Inspect footage interpretation and sequence color options before touching creative sliders.
3. Normalize each input as appropriate for its camera specification.
4. Correct white balance and exposure first; compare scopes and visual continuity at cuts.
5. Match contrast and saturation conservatively; look for clipped highlights and crushed shadows.
6. Add a gentle creative look, then toggle the look off to verify the underlying corrections are still sound.
7. Export a short SDR review, noting codec, color settings, display conditions and any player discrepancy.

**Mastery:** Explain why a wrong input transform, creative LUT, export color tag and uncalibrated viewer are four different potential causes of a mismatch. See L055–L061 and the export guide.
