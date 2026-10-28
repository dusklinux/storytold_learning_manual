# Field guide 08 — Frame rates, drop-frame timecode and media-compatibility math

**Read after:** L002, L013, L015 and L089. **Goal:** Keep timing and file formats conceptually separate.

## Timecode is an address system

Timecode `HH:MM:SS:FF` identifies a frame position using a frame-counting convention. The `FF` component denotes frames within a second, not decimal hundredths. At 25 fps, `00:00:03:24` is one frame before `00:00:04:00`. If a 25 fps clip contains 250 frames, nominal duration is 10 seconds. An edit boundary must be interpreted using the actual sequence frame rate.

**29.97 fps** is shorthand for approximately **30000/1001** frames per second. **Drop-frame timecode** does not remove real video frames. It omits selected timecode *numbers* to keep displayed time addresses aligned more closely with elapsed clock time. At 29.97 DF, frame labels `:00` and `:01` are skipped at the start of each minute except every tenth minute. Thus some apparently missing codes are intentional; the picture is continuous. 23.976, 29.97 and 59.94 require care with exact rational rates, particularly in long-form calculations.

## Constant versus variable frame cadence

Constant-frame-rate media uses a stable cadence. Phone screen recordings or mobile captures can have variable presentation timestamps; the nominal “30 fps” label might summarize a changing actual cadence. A variable-frame-rate recording can create sync drift, confusing timecode navigation or inconsistent decode. When problems occur, investigate a **constant-frame-rate transcode** that preserves intended playback duration, then relink/replace correctly and test sync. Do not randomly “interpret” frame rate to force a sync solution.

## Media layers you can inspect

| Layer | Example | Why it matters |
|---|---|---|
| Container | MP4 | Stores encoded streams and timing/metadata |
| Video codec | H.264/AVC | Dictates decoding, hardware support, bitrate and compression characteristics |
| Pixel format | 4:2:0, 10-bit | Affects chroma detail, precision and GPU support |
| Color metadata | Rec.709 or Log/transfer tag | Helps define signal interpretation; may be incomplete/wrong |
| Audio codec | AAC or PCM | Affects file size, compatibility and processing loss |
| Sample rate | 48,000 samples/s | Affects audio-clock relationship and delivery convention |
| GOP structure | All-intra vs long-GOP | Affects seek, edit responsiveness and file size |

A high-quality 4:2:2 10-bit HEVC file can be harder for a particular GPU to decode than a larger intraframe proxy. Hardware support is a matrix of exact profile/bit-depth/chroma/driver/device; “my GPU supports HEVC” is not enough detail.

## One technical worksheet

Given a 25 fps sequence containing 500 frames of picture, one 48 kHz stereo PCM audio stream and a planned H.264 delivery:

1. Picture duration: `500 / 25 = 20 seconds`.
2. Expected samples per audio channel in a perfect 20-second output: `48,000 × 20 = 960,000`.
3. A hypothetical 8 Mb/s average video stream for 20 seconds: `8,000,000 × 20 / 8 = 20,000,000 bytes` (before audio and overhead).
4. Actual final file size differs due to the audio codec, encoder rate control and wrapper overhead.
5. Check the **rendered export** for real duration, audio channel assignment and black/missing frames.

**Mastery:** Distinguish physical frame loss from drop-frame *numbering*, nominal rates from exact rational frame rates, and a wrapper extension from the codec and color signal inside it.
