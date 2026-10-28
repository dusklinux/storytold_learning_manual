# Field guide 02 — Audio levels, loudness, repair and delivery

**Read after:** L038–L046. **Goal:** Understand the signal path, not memorize a target number.

## Audio as a sequence of stages

Audio arrives as samples in a clip, then passes through applicable clip-level controls/effects, track-level processing, routing and output mixing. **Clip gain** changes the signal before later volume and some downstream processing; **volume automation** is a time-varying level adjustment. Different places in the path give compressors and noise gates different signal levels, so the order can affect the outcome.

A good working order for dialogue is: select the right take → synchronize → remove clicks and edit boundaries → adjust gain and large level differences → cautious noise/speech repair → high-pass/EQ when justified → compression if needed → keyframe or automate phrases → mix against music/effects → meter → listen to the final exported file.

## dB, peaks and loudness

Decibels express **ratios**, not an absolute sound level by themselves. For amplitude:

`change in dB = 20 × log10(new amplitude / original amplitude)`.

A +6 dB change approximately doubles amplitude; −6 dB approximately halves it. In digital audio, **0 dBFS** is the nominal digital sample full-scale ceiling. A track can distort upstream of the master even when the final meter looks lower, so review gain staging throughout the chain. A limiter may control output peaks but cannot necessarily undo existing clipping.

**Peak level** tracks brief extremes. **Integrated loudness** in LUFS estimates perceived loudness over an entire programme using a standardized weighting and gating method. Loudness targets vary by platform, broadcaster, delivery agreement and content; there is no universal “make every export −14 LUFS” requirement. If a client specifies true-peak dBTP and integrated LUFS, verify both using an appropriate loudness tool and report actual measured values. Sample peaks do not guarantee intersample true peaks are safe.

| Symptom | Likely cause | Better first test |
|---|---|---|
| Voice buried under music | Music competing in same frequencies or level | Lower music during speech; compare at normal volume |
| Hiss becomes more obvious after compression | Noise floor was raised | Bypass compressor; address source noise before adding gain |
| Pumping or unnatural speech | Excessive repair/fast compression | Reduce processing; compare unprocessed source |
| Export clips despite a quiet timeline | Gain or loudness changes in output path; peak overs | Compare output file with meters; inspect output processing |
| Channels sound wrong | Mono/stereo mapping or unexpected channel assignment | Inspect Modify > Audio Channels and sequence routing |

## Dynamics in practical language

A compressor turns down signal above a chosen threshold by a ratio, often with attack/release timing. A 4:1 ratio is not a fixed −4 dB adjustment; for material 8 dB above threshold, it nominally leaves roughly 2 dB above threshold (6 dB reduction) before knee, timing, makeup gain and other variables. **Attack** controls how quickly compression responds; **release** controls recovery. **Noise reduction** estimates or separates noise; excessive amounts often create warbling, metallic artifacts or swallowed consonants.

## Build a measured dialogue-and-music example

1. Use self-recorded 20–30 seconds of speech. The included WAV examples are synthetic tones/ambience, **not human speech**.
2. Listen first at reasonable output volume; identify bad edits and obvious clipping.
3. Adjust clip gain so the voice has workable headroom; do not normalize every micro-syllable.
4. Use subtle EQ or repair only for an identified problem; bypass to compare.
5. Add a music track, lower it beneath speech, and automate an intentional rise only during a gap.
6. Use appropriate meters/loudness analysis, noting the delivery specification you are aiming for.
7. Export a 48 kHz audio-inclusive video; listen to the rendered file through headphones and speakers.
8. Keep a copy of unprocessed dialogue and a note of your output peak/loudness readings.

**Mastery:** Explain why clip gain, track volume, compressor threshold, sample peak, true peak and LUFS are not interchangeable. See L038–L045 and the symptom-oriented audio troubleshooting entries.
