# Field guide 01 — Editing geometry: source time, sequence time and four trims

**Read after:** L016–L025. **Goal:** Predict an edit before touching the mouse.

## Three coordinate systems

A **source file** contains frames. Its frame 250 is frame 250 regardless of which sequence uses it. A **source selection** is a pair of boundaries, In and Out. A **sequence** is a new time axis containing instances that reference parts of source media. The **playhead** addresses sequence time; the Source Monitor playhead addresses source time. One source may appear in a sequence ten times without ten copies of the underlying file.

For simple constant-speed clips with matching rates, the mapping is:

`source frame = source in + (sequence frame - instance start)`.

For example, if B uses source frames 50–99 and starts at sequence frame 100, the viewer sees B source frame 62 at sequence frame 112. The camera file has not changed. At 25 fps a 50-frame selection lasts 2 seconds. Speed effects, reverse motion, remapping and mismatched frame rates change this mapping; do not apply the simple formula blindly.

## A shared example

Start with `A[0–99] | B[50–149] | C[0–99]`, all 25 fps. Three segments use 100 frames each, a 300-frame sequence (12 seconds). The notation is inclusive for explanation only: Premiere In/Out semantics and edit points should be checked with the frame display when executing.

| Operation | What changes | What is deliberately preserved | Predictable consequence |
|---|---|---|---|
| **Ripple trim** B's left edge 25 frames later | B loses its first 25 used source frames; following clips shift earlier | Earlier A untouched; remaining C source range stays the same | Sequence becomes 25 frames shorter if no locks or other constraints stop the ripple |
| **Rolling edit** A/B boundary 25 frames later | A extends 25 source frames and B starts 25 source frames later | Combined A+B timeline duration; positions of material after B | Requires handles; whole sequence duration stays constant |
| **Slip** B's selected source range 25 frames later | B uses `[75–174]` instead of `[50–149]` | B's timeline position, both edges, overall duration, A and C | Content within B changes without moving its timeline boundaries |
| **Slide** B 25 frames later | B's sequence position moves later and adjacent A/C boundaries compensate | B's source In/Out and duration; overall sequence duration | Requires usable adjacent handles; A and C durations change |

When performing a roll or slide, available source handles may limit how far you can move. Track locks, sync locks, linked selection, multi-track compositions, and transition handles change what is legally editable. **Undo and inspect the full sequence**, not just the active clip.

## Insert versus overwrite

Given `A | B` and an incoming two-second C:

- **Insert** between A and B: `A | C | B`; eligible following material shifts by two seconds. Sequence grows by two seconds.
- **Overwrite** at B's first frame: `A | C | ...B`; incoming frames replace the corresponding destination interval. If B has enough duration, total sequence duration need not change.

**Source patching** chooses which incoming source streams are mapped to timeline destinations (for example incoming video to V2, audio to A1). **Track targeting** influences many sequence commands and navigation; targeting a track does not automatically replace source patching. Check the timeline header controls before inserting. Both types of control can be customized.

## J-cuts and L-cuts without mystique

A J-cut starts the incoming shot's audio before its picture. An L-cut keeps the outgoing shot's audio playing after its picture changes. They're not special video effects; they're intentional differences in audio and picture edit positions. Separate or unlink only the appropriate media, preserve synchronization reference, and listen across the boundary. A one-second lead-in is not automatically better than an eight-frame lead-in: editorial context decides.

## Practice drill

1. Duplicate a short practice sequence so the original can be restored.
2. Build three five-second clips A, B and C on V1 (and associated audio if useful).
3. Record the original sequence end time and B's source In/Out.
4. Ripple the end of A one second shorter; record the new sequence end and position of C.
5. Undo. Roll the A/B boundary one second later; check sequence duration and A/B source ranges.
6. Undo. Slip B one second later; check its timeline boundaries and source range.
7. Undo. Slide B one second later; check A/C durations and B's source range.
8. Explain every difference without saying only which button you clicked.

**Mastery:** You can predict total sequence duration, clip position, and source-frame choices for all four edits, including the effect of missing handles or track locks. See L018, L021–L025 and the diagram controls in the corresponding lessons.
