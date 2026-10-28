# After Effects 26.5 — Windows Complete Learning Manual

**Application lessons:** After Effects **26.5 on Windows only**, default English keyboard. **Reading:** open the offline HTML or Markdown on Linux or Windows; export/import browser progress to move between systems.

> Version accuracy: This edition teaches stable 26.5, including the modern 26.0–26.5 tools. Features labeled Beta remain separate. Current Adobe Help pages can mix both. No claim is made that this package reproduces every parameter of every native, bundled or third-party effect.

## Table of contents

- [Step-by-step curriculum](#step-by-step-curriculum)
- [Deep topic reference](#deep-topic-reference)
- [Practical recipes](#practical-recipes)
- [Effects encyclopedia](#effects-encyclopedia)
- [Windows shortcuts](#windows-shortcuts)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [Sources and version restrictions](#sources-and-version-restrictions)


---

## Learning ladder and readiness checks

### START — Orientation

**Learn:** Build and navigate a correctly saved composition, understand sources and place layers precisely.

**Before moving on:** From a blank project, recreate a 4-second two-card edit, relink a source and identify Position versus Anchor Point.

**Practice:** Create a small working scene from solids, text and one imported source.

### FOUNDATIONS — Animation and compositing basics

**Learn:** Animate deliberately and understand how paths, mattes, text, precomps and effects change the image.

**Before moving on:** Build a 4-second title reveal with at least two eased properties, a track matte, a named precomp, and a deliberate effect order.

**Practice:** Try the loading-ring, text-window and logo-reveal recipes.

### INTERMEDIATE — Real footage and production craft

**Learn:** Work with sound, keying, tracking, 3D space, color and basic controller expressions.

**Before moving on:** Complete a short moving-footage composite, inspect every frame for track drift or alpha errors, and link a visible property to a controller.

**Practice:** Try a Keylight, a point track, and an audio-reactive exercise.

### ADVANCED — Reusable and complex systems

**Learn:** Make data-driven templates, control 3D/model interactions, use Puppet and native particle tools, and automate repetitive edits safely.

**Before moving on:** Create one editable template with independent instances plus a separate reproducible procedural/3D or scripted experiment.

**Practice:** Try the reusable lower third, JSON scoreboard or particle-burst recipes.

### DELIVERY — Render, preserve and troubleshoot

**Learn:** Export verified deliverables, collect all dependencies, compare cold/warm previews and isolate errors systematically.

**Before moving on:** Render a review and an alpha-capable master, reopen a collected project from another path, and resolve one deliberate failure.

**Practice:** Try the transparent-master and handoff-test recipes.

### CAPSTONE — Independent final production

**Learn:** Combine learned skills into an original, reviewable, portable 10-second sequence.

**Before moving on:** Deliver an independently checked 10-second composition with source files, project backup and an explanation of every major animation choice.

**Practice:** Build the final integrated-sequence recipe without step-by-step imitation.


---

## Lesson index

1. [01 · Install, identify and prepare AE 26.5](#lesson-install)
2. [02 · Understand projects, comps, layers and pixels](#lesson-logic)
3. [03 · Import and inspect footage correctly](#lesson-assets)
4. [04 · Read time, frames, trims and the work area](#lesson-timing)
5. [05 · Anchor, Position, Scale and parenting](#lesson-transform)
6. [06 · Create and remove keyframes safely](#lesson-keys)
7. [07 · Design motion with the Graph Editor](#lesson-easing)
8. [08 · Draw shapes and parametric shape operators](#lesson-paths)
9. [09 · Understand masks and alpha](#lesson-masks)
10. [10 · Use track mattes and blend modes](#lesson-mattes)
11. [11 · Precompositions, nested time and render order](#lesson-precomp)
12. [12 · Typography and animated text selectors](#lesson-text)
13. [13 · Learn effects, order and adjustment layers](#lesson-effects)
14. [14 · Quick Apply, guides and effect organization](#lesson-modern-operations)
15. [15 · Blur, glow, noise and depth maps](#lesson-blur)
16. [16 · Time remap, speed, loops and motion blur](#lesson-timefx)
17. [17 · Audio levels, waveform and reactive graphics](#lesson-audio)
18. [18 · Green/blue-screen compositing](#lesson-keying)
19. [19 · Track a moving point and stabilize motion](#lesson-tracking)
20. [20 · Roto Brush, Refine Edge and mask tracking](#lesson-roto)
21. [21 · Paint, clone and Content-Aware Fill](#lesson-paint)
22. [22 · 2.5D parallax, cameras and lights](#lesson-camera)
23. [23 · Camera tracking and screen replacement](#lesson-3dtrack)
24. [24 · Color correction, working space and alpha](#lesson-color)
25. [25 · Expressions: build a repeatable controller](#lesson-expressions)
26. [26 · Object Matte with frame-by-frame quality control](#lesson-object-selection)
27. [27 · SVG and variable-font motion](#lesson-modern-type)
28. [28 · Curl Noise, Unmult and audio dynamics](#lesson-flow-alpha)
29. [29 · Data-driven text and graphics](#lesson-data)
30. [30 · Essential Properties and MOGRT delivery](#lesson-templates)
31. [31 · Native 3D models, environments and renderers](#lesson-advanced3d)
32. [32 · Puppet rigging and deformation](#lesson-puppet)
33. [33 · Native particle and simulation systems](#lesson-particles)
34. [34 · ExtendScript, scripts and batch workflow](#lesson-automation)
35. [35 · Native mesh materials and an Advanced 3D rack focus](#lesson-mesh-focus)
36. [36 · Render Queue, codecs, alpha and audio](#lesson-render)
37. [37 · Backups, Collect Files and team handoff](#lesson-collect)
38. [38 · Performance, memory, cache and proxies](#lesson-performance)
39. [39 · Diagnose broken results systematically](#lesson-debug)
40. [40 · Complete project: 10-second motion graphics composite](#lesson-capstone)

## Step-by-step curriculum

<a id="lesson-install"></a>
### 01 · Install, identify and prepare AE 26.5

**Stage:** START
**Why:** Use the specified 26.5 stable build on Windows, with a reproducible workspace and no accidental version mismatch.

1. Open Creative Cloud Desktop on Windows. Locate After Effects and check the installed version through Help → About After Effects. The target is 26.5 stable (September 2026). Beta is a separate installation; its tools are not automatically part of stable.
2. Before a large project, compare your Windows version, CPU architecture, RAM, GPU/driver and free storage with Adobe’s 26.5 requirements. AVX2 is required for supported Intel/AMD systems; Windows on Arm has its own supported Snapdragon hardware. A Windows VM must expose the required CPU/GPU capabilities; successful launch alone does not establish 3D performance.
3. Start AE and identify Project, Composition viewer, Timeline, Effect Controls, Effects & Presets, Properties, Preview and Render Queue panels. Hover any panel and tap the backtick key (`) to maximize/restore it.
4. Choose Window → Workspace, select a standard layout and use Reset to Saved Layout if panels are lost. Use Edit → Preferences to configure auto-save, disk cache and available memory without starving Windows.
5. Create a dedicated folder such as D:\AE_Learning\01_First_Project. Reserve an Assets subfolder, an Output subfolder and a project backup folder. Avoid relying on temporary Downloads files.
6. Open Edit → Keyboard Shortcuts (Ctrl+Alt+') to verify bindings on your installed version and keyboard layout. Save a custom preset only if you intentionally change a shortcut.

**Do it yourself:** Break and restore a workspace layout, then find the Timeline and Effects & Presets in under 30 seconds.

**Self-check:**
- [ ] I can verify 26.5 and locate every central panel.
- [ ] I have an organized Windows project folder.
- [ ] I know where the shortcut editor is.

**Common mistakes:**
- Adobe Help can mix stable and Beta features; confirm the release label before using a new command.
- Do not delete the disk-cache folder while AE is actively writing to it.

**Related deep dives:** [The Windows After Effects interface](#topic-interface), [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow), [RAM, disk cache and preview rate](#topic-performance), [Folders, naming and backup policy](#topic-project-management)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history), [Adobe: After Effects 26.x system requirements](https://helpx.adobe.com/after-effects/desktop/get-started/technical-requirements/system-requirements.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html), [Adobe: memory and storage](https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html)

<a id="lesson-logic"></a>
### 02 · Understand projects, comps, layers and pixels

**Stage:** START
**Why:** Build a correct mental model before memorizing commands.

1. A .aep project is a container of references, compositions, settings and animation; imported images and video normally remain external files. Save Project is not the same as Collect Files or render.
2. Create a 1920×1080, 24 fps, 8-second composition with Ctrl+N. Name it 01_LAB. Distinguish composition size, frame rate, duration, pixel aspect ratio and background color; the comp background is not automatically an opaque render layer.
3. Create a blue solid (Ctrl+Y), a text layer (Ctrl+T in an appropriate context), and an empty shape layer (Layer → New → Shape Layer). Stack order determines which pixels cover which in ordinary 2D.
4. Select the blue layer: P=Position, S=Scale, R=Rotation, T=Opacity, A=Anchor Point. Use Shift+P to add Position while other properties are displayed, and U for animated properties.
5. Toggle a layer eye, shy, solo, lock, effects (fx), motion blur and 3D switch. Explain how hiding an entire layer differs from bypassing just its effects. F4 changes switches/modes columns.
6. Learn the vocabulary: footage item vs footage layer, source vs instance, composition vs precomposition, property vs keyframe, mask vs shape, alpha channel vs opacity, effect vs shape operator.

**Do it yourself:** Duplicate the blue solid layer twice; assign each instance a different Opacity. Observe that all three layers refer to the same Solid Footage source in the Project panel.

**Self-check:**
- [ ] I can describe the project/comp/layer hierarchy.
- [ ] I can distinguish source items from instances.
- [ ] I can reveal five transform properties.

**Common mistakes:**
- Pressing a stopwatch that is already active removes its keyframes.
- A background color setting does not add opaque pixels to your output.

**Related deep dives:** [The Windows After Effects interface](#topic-interface), [Composition, layer and project hierarchy](#topic-layer-anatomy), [Coordinates, anchor points and transforms](#topic-coordinates), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-assets"></a>
### 03 · Import and inspect footage correctly

**Stage:** START
**Why:** Learn what AE assumes when interpreting each media asset.

1. Use Ctrl+I to import a PNG with alpha, a JPG, a short constant-frame-rate video, a WAV file and—when available—an image sequence. Check whether the source is a file, sequence or folder.
2. Double-click footage in Project to open its Footage panel. Compare footage time and frame dimensions with those of your composition. Drag footage into a comp; inspect scaling and frame-rate behavior.
3. Right-click footage → Interpret Footage → Main. Identify frame rate assumption, field order, pixel aspect ratio and alpha interpretation (straight vs premultiplied); note color options separately.
4. For an image sequence, select the first frame and use the sequence checkbox only when intended. Verify that frames were numbered without gaps and their order is correct.
5. Replace a selected layer’s source by Alt-dragging a different source from Project onto the layer. Confirm transform animation and effects remain in place. Distinguish replacing a layer source from replacing a Project item globally.
6. Make an Assets folder in Project, sort sources and keep originals on disk. If Windows drive letters or source folders change, use Replace Footage to relink the existing Project item; importing the same file again creates a separate item and may leave broken layer references unresolved.

**Do it yourself:** Import a square logo and a wide logo, replace the first with the second using Alt-drag, and observe how the same Scale value affects each.

**Self-check:**
- [ ] I can interpret footage and verify source frame rates.
- [ ] I can replace footage without losing a layer animation.
- [ ] I know where a missing-file reference points.

**Common mistakes:**
- Variable-frame-rate recordings can cause erratic time or audio sync; use a constant-frame-rate transcode when needed.
- Premultiplied alpha interpreted as straight can cause a dark fringe.

**Related deep dives:** [Import formats, sequences and linked files](#topic-import-media), [Alpha, straight RGB and premultiplication](#topic-alpha), [Footage frame rate, alpha and pixel aspect](#topic-footage-interpretation), [Missing media, absolute paths and Windows storage](#topic-file-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-timing"></a>
### 04 · Read time, frames, trims and the work area

**Stage:** START
**Why:** The difference between layer time, source time and comp time prevents silent editing errors.

1. In the Timeline, place the current-time indicator (CTI) at exactly 00:00:02:00 at 24 fps. Use Page Up/Page Down to step frames; Shift+Page Up/Down steps ten frames. Read timecode as hours:minutes:seconds:frames.
2. Use B and N to set an intentionally short work area. Start/stop Preview with Space; observe the Preview panel options. The work area is a range for preview/render control, not a change to source duration.
3. With CTI at 1 second, select a footage layer and press [ to shift its entire layer bar so the In point meets CTI. Next move CTI to 2 seconds, press Alt+[ to trim the In point without moving the entire layer. Undo twice and compare layer Start Time, In point and source frames.
4. Use Alt+] to trim the out point, Ctrl+Shift+D to split, Ctrl+D to duplicate, and I/O to jump to a selected layer’s in/out points. Practice knowing which commands change the source span.
5. Move the Timeline zoom using = / - on the main keyboard. Toggle full-span/single-frame viewing with ;. View one exact source frame, then locate it after shifting the layer.
6. Set marker(s) to plan beats. A composition marker differs from a layer marker; both differ from a keyframe. Save an experiment copy before drastic trimming.

**Do it yourself:** Build a 4-second card transition that changes from a blue card to a red card at exactly 48 frames.

**Self-check:**
- [ ] I can step to a specific frame.
- [ ] I know the distinction between moving, trimming and splitting.
- [ ] I can define a work area.

**Common mistakes:**
- At 24 fps, :23 is the last frame within a numbered second; :24 is not an in-second frame.
- The main keyboard 0 and numpad 0 may do different things.

**Related deep dives:** [FPS, timecode and frame alignment](#topic-frames), [Layer bounds, work areas and markers](#topic-timeline), [Footage source time vs comp time](#topic-source-time)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-transform"></a>
### 05 · Anchor, Position, Scale and parenting

**Stage:** START
**Why:** Spatial transforms are predictable once you understand coordinate spaces.

1. Draw a 200×200 rectangle in a Shape Layer. Press P to inspect the comp-space Position of the shape layer’s anchor; press A to inspect its layer-space Anchor Point (which may not coincide with the rectangle’s own group center). Changing one is not the same as changing the other.
2. Move the anchor with the Pan Behind tool (Y). Rotate with R; notice where rotation occurs. To center the anchor within content, test Ctrl+Alt+Home and compare the result with Ctrl+Home, which centers the layer’s anchor in the comp.
3. Create a Null Object (Ctrl+Alt+Shift+Y). Parent the shape and text to the null using the Parent & Link pick whip. Move, scale and rotate the null; then inspect each child’s local transform.
4. Unparent one child and watch its on-screen pose if AE compensates its transform. Explain why parenting does not mean copying Position keyframes or merging layers.
5. For a 3D layer, Position has three dimensions and rotation/orientation differs from the 2D case. Do not introduce a camera yet; use the 3D switch only for a controlled experiment.
6. Build a single controller named CTRL_RIG, and do not put unrelated effects on it. Label layers clearly and lock controllers when their position is correct.

**Do it yourself:** Animate the null in a circle while rotating an independently animated child around its own pivot.

**Self-check:**
- [ ] I can tell anchor and position apart.
- [ ] I can parent two layers to a null.
- [ ] I can explain local vs comp coordinates.

**Common mistakes:**
- Changing a child parent can alter coordinate interpretation.
- Centering a layer and centering its anchor are different commands.

**Related deep dives:** [Coordinates, anchor points and transforms](#topic-coordinates), [Parenting, nulls and reusable rigs](#topic-parenting), [2.5D layers and spatial depth](#topic-3d-intro)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-keys"></a>
### 06 · Create and remove keyframes safely

**Stage:** FOUNDATIONS
**Why:** Animate one number correctly before adding complex rigs.

1. Add a Position keyframe at time 0 by clicking the stopwatch once. Move to 1 second and drag the object to a new Position. Inspect the two diamonds in the Timeline.
2. Return to time 0, reveal Opacity with T, set it to 100 and click its stopwatch to create the first Opacity keyframe. Then move to 2 seconds and change Opacity to 0 to create the second key. Without that first keyframe, the change at 2 seconds would simply set a constant value rather than a fade.
3. Select only one keyframe and press Delete. Rebuild it. To remove all Position keys, click the active stopwatch: observe that every keyframe vanishes and the current value is retained. Undo immediately.
4. Use U to show only animated properties, UU to show all properties modified from defaults, and K/J to jump visible keyframes/markers.
5. Use Alt+Shift+P or Alt+Shift+T to add/remove a key at CTI on the appropriate property; this does not toggle the whole property’s animation stopwatch.
6. Copy two selected Position keyframes, place CTI elsewhere and paste. Note that the first pasted key usually aligns with CTI. Use a separate duplicate layer to compare variations.

**Do it yourself:** Animate a circle from x=200 to x=1720 in exactly 2 seconds, then fade it in for the first 12 frames.

**Self-check:**
- [ ] I can create, move and remove a single keyframe.
- [ ] I understand the dangerous stopwatch toggle.
- [ ] I can show only animated properties.

**Common mistakes:**
- Auto-keyframing can enable animation for new properties automatically; leave it off while learning.
- Deleting one key is not the same as deactivating the stopwatch.

**Related deep dives:** [Keyframes and interpolation](#topic-keyframes), [Layer bounds, work areas and markers](#topic-timeline)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-easing"></a>
### 07 · Design motion with the Graph Editor

**Stage:** FOUNDATIONS
**Why:** Good animation depends on velocity and spacing, not just destinations.

1. Create Position keyframes 0 and 1 second, 800 pixels apart. Set both Linear, preview, and notice constant perceived speed on a straight path.
2. Select both keys and press F9 (Easy Ease). Use Shift+F3 to open the Graph Editor. Locate Speed Graph and Value Graph modes; for Position, choosing Separate Dimensions changes the way you can edit curves.
3. In Speed Graph, make the object accelerate quickly and decelerate gently. Preview and compare. Inspect motion-path dots: dense dots represent smaller distance per sample and hence slower motion.
4. Make a third middle Position key; separate spatial path curvature (trajectory) from the time interpolation (velocity). A curved path can move at constant speed, and a straight path can ease.
5. Use Easy Ease In/Out intentionally. For a stepped stop-motion look, test Toggle Hold Keyframe. Observe that Hold is not the same as a slow Bézier curve.
6. Open Keyframe Velocity (Ctrl+Shift+K) when numerical influence is necessary. Save a tiny file containing three clearly named easing examples.

**Do it yourself:** Make three identical circles travel 500 px with linear, ease-out and overshoot movement; render a side-by-side comparison.

**Self-check:**
- [ ] I can explain speed vs value graphs.
- [ ] I can make linear, eased and hold movement.
- [ ] I understand spatial vs temporal curves.

**Common mistakes:**
- Tweaking spatial Bézier handles changes the path rather than temporal easing.
- Position Separate Dimensions removes the unified motion path representation.

**Related deep dives:** [Value Graph, Speed Graph and easing](#topic-graph-editor), [Keyframes and interpolation](#topic-keyframes), [Timing and design principles for readable motion](#topic-motion-design)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-paths"></a>
### 08 · Draw shapes and parametric shape operators

**Stage:** FOUNDATIONS
**Why:** Distinguish vector geometry, paths, styles and per-group transformations.

1. Deselect all layers and use Q to draw a rectangle. It creates a Shape Layer. Expand Contents → Rectangle → Rectangle Path, Fill, Stroke, and the shape group’s Transform; compare with the layer’s separate Transform group.
2. Make an Ellipse and a Polystar with the Q tool cycle. Change parametric Size, Roundness, Points and radii. Do not convert to Bézier until you actually need manual vertices.
3. Use Contents → Add → Trim Paths and animate End from 0 to 100 on a stroked path. Set Start and Offset to explore moving a dash around a loop.
4. Use Repeater to create repeated copies of a group. Find Copies, Offset and Transform: Repeater → Position, Rotation, Scale. Explain why changing original geometry affects every repeated instance.
5. Explore Offset Paths, Pucker & Bloat, Zig Zag, Twist and Wiggle Paths one at a time. Turn each operator off and on to isolate its effect.
6. Convert a duplicated parametric path to Bézier; move a vertex with Pen/Selection tools. Try a closed filled shape and an open stroked path to compare filling behavior.

**Do it yourself:** Make a rotating loading indicator consisting of twelve repeated ticks and a Trim Paths ring.

**Self-check:**
- [ ] I can locate group Transform vs layer Transform.
- [ ] I can animate Trim Paths and Repeater.
- [ ] I can choose parametric vs Bézier geometry.

**Common mistakes:**
- An empty Shape Layer has no visible pixels.
- Shape operators are not in the Effect Controls effects list.

**Related deep dives:** [Parametric shapes vs Bézier paths](#topic-shapes), [Masks, shape paths and motion paths](#topic-paths), [Shape strokes, Trim Paths and Write-on](#topic-strokes)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-masks"></a>
### 09 · Understand masks and alpha

**Stage:** FOUNDATIONS
**Why:** Transparency has several independent sources, each suited to different work.

1. Add a photograph to a comp. Select the photograph and draw a rectangle: it normally creates a mask on the selected layer. Deselect and draw another rectangle: it creates a shape layer. Check the toolbar mask/shape mode.
2. Press MM to reveal mask groups. For each mask test Mode Add, Subtract, Intersect and None, then change Feather, Expansion and Opacity and invert the mask.
3. Animate Mask Path over several frames to follow a moving subject. Make simple wide shapes first; excessive vertices are harder to stabilize and maintain.
4. Set a high feather value, then change layer Opacity separately. Inspect the Alpha channel via Alt+4. A transparent pixel can still have RGB values; alpha determines coverage.
5. Draw two masks on the same layer; test which mode is used and whether the order changes results. Enable/disable masks independently without deleting their path keys.
6. Precompose masked imagery and compare the look with and without Collapse Transformations in a controlled vector/precomp case; do not assume the switch is a free quality upgrade.

**Do it yourself:** Cut a circular window into a photo and animate the window to follow a bouncing ball.

**Self-check:**
- [ ] I can create a mask on a selected layer.
- [ ] I can adjust feather, expansion and modes.
- [ ] I can inspect actual alpha separately.

**Common mistakes:**
- An animated mask is not a motion-tracked mask until you track it.
- High feather is not a cure for poor matte edges.

**Related deep dives:** [Mask modes and feathering](#topic-masks), [Alpha, straight RGB and premultiplication](#topic-alpha), [Alpha/luma track mattes](#topic-mattes)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-mattes"></a>
### 10 · Use track mattes and blend modes

**Stage:** FOUNDATIONS
**Why:** Mattes let one layer control visibility of another without drawing directly on the target.

1. Create a text layer above a video layer. In the video layer’s TrkMat column select the text layer as its matte source. Modern AE track mattes can refer to another layer without that matte being directly above the target.
2. Test Alpha Matte versus Alpha Inverted Matte. Then use a luminance gradient and select Luma Matte versus Luma Inverted Matte. Identify what white, black and grey mean in each mode.
3. Try a transparent red-to-blue shape as a matte and inspect why its alpha can be constant although its luminance varies dramatically. Convert to grayscale for a predictable luma test.
4. Use F4 to reveal Switches/Modes where necessary. Compare Normal, Multiply, Screen, Add and Overlay on the same footage with two test layers.
5. Precompose only when the matte has to become a reusable source or when an effect must operate after the matte. A simple matte relationship does not automatically require a precomp.
6. Render to a format supporting alpha and verify transparency over a checkerboard outside AE. A matte preview on black is not proof that alpha was exported.

**Do it yourself:** Make a 3-second title reveal in which video is visible only inside moving letters.

**Self-check:**
- [ ] I can choose alpha vs luma matte.
- [ ] I can invert either matte.
- [ ] I can demonstrate an actual transparent export.

**Common mistakes:**
- Screen blend mode against black does not create real alpha.
- Layer opacity and track-matte coverage multiply in the final composite.

**Related deep dives:** [Alpha/luma track mattes](#topic-mattes), [Layer blend modes and compositing](#topic-blending), [Alpha, straight RGB and premultiplication](#topic-alpha), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-precomp"></a>
### 11 · Precompositions, nested time and render order

**Stage:** FOUNDATIONS
**Why:** Precomps organize work, but also change which operations happen first.

1. Select three animated layers and precompose with Ctrl+Shift+C. Name the new comp 02_ICON_UNIT; with multiple selected layers After Effects uses Move all attributes into the new composition. To compare with Leave all attributes, make a separate single-layer footage/solid test (not a shape or text layer), precompose it, and inspect both dialog choices.
2. Open the precomp and note the inner time, duration, and layer layout. Return to the master comp and alter the precomp layer transform. Inspect whether the inner animation still plays as intended.
3. Apply Gaussian Blur to a shape, then precompose with different attribute settings; compare effect-before-transform with effect-after-transform. Render order is the reason precomposing can change an effect’s appearance.
4. In a duplicated test comp, toggle Collapse Transformations on the nested comp. Observe changed transformations, masks, 3D interactions and effect results rather than universally enabling the switch.
5. Use Time Remapping and an Essential Property only after the nested comp behaves consistently. Name instances uniquely when they need different controls.
6. Add a short marker on master comp corresponding to a specific event inside the precomp. Document any shifted inner start times and audio synchronization.

**Do it yourself:** Build a lower-third as its own comp, duplicate it twice in a master comp and vary scale/timing without editing the internal artwork.

**Self-check:**
- [ ] I can precompose with an intentional attribute choice.
- [ ] I can explain a changed blur after precomposition.
- [ ] I can locate inner vs outer time.

**Common mistakes:**
- Collapse Transformations is not a generic quality switch.
- Precompose can change how adjustment layers, 3D and effects interact.

**Related deep dives:** [Precomposition and nested timeline logic](#topic-precomp), [Effect and transform evaluation order](#topic-render-order), [Essential Properties as instance controls](#topic-essential-properties)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: Precomposing, nesting, and pre-rendering](https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html)

<a id="lesson-text"></a>
### 12 · Typography and animated text selectors

**Stage:** FOUNDATIONS
**Why:** Type in motion is a system of characters, paragraphs, layout and animation selectors.

1. Use Ctrl+T to create point text with a click and paragraph text by dragging a text box. Test different wrapping, alignment, font weight and paragraph settings in Character/Paragraph.
2. Make two headings with consistent font family and sizes; use tracking and leading intentionally. Use native text rather than rasterizing type when you need accessibility and later wording changes.
3. Expand Text → Animate → Position and add an Opacity animator. Open Range Selector → Advanced; compare Based On Characters, Characters Excluding Spaces, Words and Lines.
4. Animate Range Selector Offset from -100% to 100% to sweep a reveal. Compare Smoothness 0 to 100 and different selector shapes for stepped vs continuous entrances.
5. Use Text → Path Options when appropriate to put characters along a mask path. A text-on-path system is different from converting text to outlines.
6. Create two text layers, apply only a few font and style changes, and test 25.4+ copy/paste text formatting where available. Verify the paste action in the text editing context.

**Do it yourself:** Make a 5-second kinetic typography card with per-word emphasis, clean baseline and a safe screen margin.

**Self-check:**
- [ ] I can distinguish point and paragraph text.
- [ ] I can animate words and letters separately.
- [ ] I can use Range Selector Offset.

**Common mistakes:**
- Per-character expressions added in 25.0 are different from variable-font axis animation introduced in 26.0.
- Using the same keybindings while editing text can trigger text editing commands instead of layer shortcuts.

**Related deep dives:** [Point/box text, metrics and typography](#topic-text), [Text animators and selectors](#topic-text-animator), [Kinetic typography and text clarity](#topic-type-design)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-effects"></a>
### 13 · Learn effects, order and adjustment layers

**Stage:** FOUNDATIONS
**Why:** Effects compute images in sequence, and the order is part of the design.

1. Create a solid with Fractal Noise; apply Levels, Tint, Turbulent Displace and Glow in that order. Duplicate the layer and reorder Glow before Levels. Compare the different result.
2. Open Effect Controls with F3. Rename each effect instance by its purpose. Toggle its fx switch; note that disabling an effect is nondestructive while Ctrl+Shift+E removes all effects from selected layers.
3. Make an Adjustment Layer (Ctrl+Alt+Y) and apply Curves. Put it above two footage layers; toggle layer order and note which lower pixels it modifies.
4. Compare an effect applied to a footage layer, the same effect on a precomp, and an effect on an adjustment layer. They do not use identical inputs in all cases.
5. Press Ctrl+Enter to open Quick Apply. Search e:glow, p: for presets or m: for menu commands; Enter applies the selected result. Use Effect → Manage Effects if an installed effect is disabled.
6. Test effect compatibility at 8, 16 and 32 bpc in Project Settings. An effect may process fewer bit depths or be CPU-only; check supported modes for the actual installed 26.5 effect.

**Do it yourself:** Build a cloudy glow effect with at least four effects; save an Animation Preset for reuse.

**Self-check:**
- [ ] I can rearrange effects to change render results.
- [ ] I understand adjustment layers.
- [ ] I can distinguish bypass from deletion.

**Common mistakes:**
- In Quick Apply, Ctrl+Enter applies to a new layer and Ctrl+Alt+Enter to a new adjustment layer; outside it Ctrl+Enter opens the launcher.
- An effect called a 3D effect does not necessarily create an actual 3D layer.

**Related deep dives:** [The effect stack and control surfaces](#topic-effect-order), [Effects, presets and compatibility](#topic-effects), [Adjustment layers and global looks](#topic-adjustment-effects), [Quick Apply: effects, presets and commands](#topic-quick-apply), [Effect labels, masks and reusable presets](#topic-effect-labels)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html), [Adobe: Effect masks, opacity and animation presets](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html), [Adobe: Quick Apply](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/quick-apply.html)

<a id="lesson-modern-operations"></a>
### 14 · Quick Apply, guides and effect organization

**Stage:** FOUNDATIONS
**Why:** Use the current interface to locate operations and build consistent layouts.

1. Create a duplicate of your title comp. Press Ctrl+Enter, type e:glow and apply the result to the intended layer with Enter; F3 opens its controls.
2. Reopen Quick Apply and inspect p: and m: results. On a disposable comp try Ctrl+Alt+Enter inside the launcher to create an adjustment layer, then compare which pixels change.
3. Rename effect instances by purpose and give them distinct color labels using the gray swatch beside each effect name. Bypass one fx switch and compare before deleting anything.
4. Show rulers with Ctrl+R. Add a 50% vertical guide and a 100-pixel right-edge guide via Edit Guide; change a duplicate composition’s width and compare.
5. Lock guides independently from pinning. Export a .guides file and import it into another view, checking units, colors and reference edges in the destination.
6. Choose an effect you use often and save a deliberate Animation Preset. Apply it to a duplicate at a known playhead time and inspect the added properties and keys.

**Do it yourself:** Build landscape and portrait title variants with the same intended margins; explain which artwork still needs repositioning.

**Self-check:**
- [ ] I can use Quick Apply result modifiers.
- [ ] I can explain fixed versus percentage margins.
- [ ] I can distinguish effect labels from processing.

**Common mistakes:**
- Guides do not reposition layers automatically.
- A preset can add keyframes at CTI and change an existing setup.

**Related deep dives:** [Quick Apply: effects, presets and commands](#topic-quick-apply), [26.5 guides: pixels, percent, edge pinning and color](#topic-responsive-guides), [Effect labels, masks and reusable presets](#topic-effect-labels), [Snapshots, clipboard frames and rendered stills](#topic-clipboard-frame)

**Sources:** [Adobe: Quick Apply](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/quick-apply.html), [Adobe: Guide creation and management](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html), [Adobe: Effect Controls and instance labels](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html)

<a id="lesson-blur"></a>
### 15 · Blur, glow, noise and depth maps

**Stage:** INTERMEDIATE
**Why:** Understand the purpose of blur and procedural textures instead of applying random presets.

1. Place Gaussian Blur on a photographic layer. Increase Blurriness and compare Repeat Edge Pixels on/off around the boundaries.
2. On a duplicate, use Camera Lens Blur and configure lens properties. Compare computational cost and appearance with a Gaussian Blur of similar apparent radius.
3. Generate a grayscale Fractal Noise texture on another layer. Use Displacement Map to warp a checkerboard; inspect map source channel, Max Horizontal/Vertical Displacement and map resolution.
4. Try Compound Blur or Camera Lens Blur with a blur/depth map and feathered transitions. A depth map controls *where* blurring occurs; it is not the same as overall lens bokeh settings.
5. Make a glow source by isolating bright pixels through Levels, then apply Glow with intentional Threshold, Radius and Intensity. Note why adding glow to a full-bright white rectangle washes out the whole scene.
6. Animate Fractal Noise Evolution and Offset Turbulence. Use it as a texture, matte, displacement driver or blend overlay, checking noise aliasing at final resolution.

**Do it yourself:** Build a heat-haze transition using Fractal Noise as an animated Displacement Map.

**Self-check:**
- [ ] I can choose ordinary vs lens-like blur.
- [ ] I can use a grayscale map to deform or blur.
- [ ] I can keep a glow controllable.

**Common mistakes:**
- Curl Noise is available in 26.5 for flowing procedural textures; compare it with Fractal Noise rather than treating them as identical.
- Too much glow can destroy edge contrast and alpha quality.

**Related deep dives:** [Gaussian, lens and map-driven blur](#topic-blur), [Fractal/Turbulent Noise and displacement](#topic-procedural), [Displacement, depth and faux 3D](#topic-depth-maps), [Curl Noise: a flowing texture experiment](#topic-curl-noise)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html), [Adobe: Noise, grain and Curl Noise](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html)

<a id="lesson-timefx"></a>
### 16 · Time remap, speed, loops and motion blur

**Stage:** INTERMEDIATE
**Why:** Temporal sampling affects motion even when no transform changes.

1. Put a clip in a comp. Compare Time Stretch, Time-Reverse Layer (Ctrl+Alt+R), and Time Remapping (Ctrl+Alt+T). Record which changes source speed and which changes the timing of layer keyframes.
2. Enable Time Remapping on a duplicate and add a middle keyframe to speed up one segment and slow down another. Inspect interpolation: smooth time remapping can freeze or reverse segments.
3. For looping source playback, locate the final valid source frame and the default end-time key. Remove or adjust the problematic end key before adding loopOut('cycle') to Time Remap if required.
4. Use Posterize Time on a duplicate to create a stepped frame-rate aesthetic. Distinguish it from changing the *composition* frame rate.
5. Animate a fast-moving shape. Toggle its Motion Blur switch and the comp’s master Motion Blur switch. Adjust shutter angle and shutter phase under comp Advanced settings; judge at full speed.
6. Compare native motion blur with CC Force Motion Blur or Pixel Motion Blur where available. Third-party/plugins and frame interpolation may need substantially more rendering time.

**Do it yourself:** Create three 2-second strips: smooth moving circle, 12-fps posterized circle and motion-blurred circle.

**Self-check:**
- [ ] I can reverse footage and remap it.
- [ ] I can loop without an extra flash at the seam.
- [ ] I can enable both motion blur switches.

**Common mistakes:**
- Motion blur is not added just because a layer has Position keyframes.
- Time Remap source duration endpoints can be off by one visible frame.

**Related deep dives:** [Time remapping, reversal and loops](#topic-time-remap), [Frame-rate conversion and temporal sampling](#topic-frame-rate), [Native motion blur and shutter settings](#topic-motion-blur)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-audio"></a>
### 17 · Audio levels, waveform and reactive graphics

**Stage:** INTERMEDIATE
**Why:** AE can synchronize and drive animation from audio, but is not a full DAW.

1. Import a WAV with predictable beats. Press L for Audio Levels and LL (two quick taps) for its waveform; use numpad decimal for audio-only preview on a standard keyboard.
2. Set clear timeline markers at beats. Trim and reposition sound without accidentally offsetting its start relative to animated elements; use the Info panel if needed.
3. Select audio → Animation → Keyframe Assistant → Convert Audio to Keyframes. Inspect the resulting Audio Amplitude null and Both Channels Slider keyframes.
4. On a shape’s Scale, Alt+click the stopwatch and use a simple expression driven by the slider. For example: a=thisComp.layer('Audio Amplitude').effect('Both Channels')('Slider'); [100+a*2,100+a*2];.
5. Smooth noisy values with the smooth() expression when needed or keyframe smoothing, and clamp extreme peaks. Build a minimum scale so silence does not collapse the graphic.
6. Export a preview and listen to it. Audio playback from the computer can differ from a final encoded render; check that audio output is explicitly enabled in the Output Module.

**Do it yourself:** Animate a 5-bar equalizer-like display using five linked or differently remapped audio amplitude values.

**Self-check:**
- [ ] I can reveal an audio waveform.
- [ ] I can convert audio to control keys.
- [ ] I can make a shape pulse to audio.

**Common mistakes:**
- Audio amplitude generated by the assistant is a numerical representation, not a beat classifier.
- An audio effect can modify the sound, not just a visible waveform.

**Related deep dives:** [Audio preview, sync and output](#topic-audio), [Convert Audio to Keyframes workflow](#topic-audio-reactive), [Expression evaluation and safe syntax](#topic-expressions)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-keying"></a>
### 18 · Green/blue-screen compositing

**Stage:** INTERMEDIATE
**Why:** Professional keying separates core opacity, edge detail and spill removal.

1. Import evenly lit green-screen footage. Put a contrasting background beneath it, then apply Keylight (1.2) to the footage.
2. Pick a representative green Screen Colour away from hair/skin. Switch Keylight View to Screen Matte. Adjust Clip Black and Clip White moderately to establish opaque subject and clean background.
3. Inspect fine hair and semi-transparent material. Use Screen Shrink/Grow and Screen Softness carefully; extreme crushing loses legitimate edge detail.
4. Add Key Cleaner and Advanced Spill Suppressor after Keylight when useful. Compare suppression modes and check green reflections in grey or skin regions.
5. Use a garbage mask to eliminate off-screen gear and nonuniform regions before or alongside keying. Use separate inside and edge mattes for challenging footage rather than forcing one setting for every region.
6. Check the keyed subject against black, white, saturated grey and final intended background. Add light wrap/grade if visually needed, but keep a clean premultiplied edge.

**Do it yourself:** Produce a 5-second talking-head composite against a still photograph, with stable hair edges.

**Self-check:**
- [ ] I can read the Keylight screen matte.
- [ ] I can distinguish matte cleanup from spill suppression.
- [ ] I can inspect alpha on four backgrounds.

**Common mistakes:**
- Cranking Clip Black/White removes real fine detail.
- Luma matte does not automatically replace chroma keying.

**Related deep dives:** [Keylight, spill and edge recovery](#topic-keying), [Alpha, straight RGB and premultiplication](#topic-alpha), [Layer-based compositing and image order](#topic-compositing)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-tracking"></a>
### 19 · Track a moving point and stabilize motion

**Stage:** INTERMEDIATE
**Why:** Tracking turns observations in footage into reusable transformations.

1. Select a footage layer and open Window → Tracker. Choose Track Motion. Start with a high-contrast feature that does not rotate out of view; define Feature and Search Regions.
2. Track forward in small portions and inspect drift. Set the Attach Point thoughtfully; the feature region may move while the attachment stays separately positioned.
3. Create a Null, set Edit Target to that Null, and Apply the tracking data. Parent a graphic to the null rather than pasting tracking keys into every child.
4. Enable rotation and scale tracking by using two tracking points when the footage supports stable features. Know that point trackers cannot inherently solve full perspective deformation.
5. Use Stabilize Motion on a duplicate; note how the image edges move and why you may need scaling/cropping or synthesis for blank edges.
6. For planar surfaces and perspective replacement, open bundled Mocha AE, track a plane, then send corner-pin data back into AE. Verify the exact Mocha integration commands in the installed plugin version.

**Do it yourself:** Track a moving label onto a high-contrast point on a recorded object for 3 seconds.

**Self-check:**
- [ ] I can apply a point track to a Null.
- [ ] I can detect and repair track drift.
- [ ] I can distinguish point tracking from planar tracking.

**Common mistakes:**
- A successful tracker preview can still drift after an occlusion.
- Warp Stabilizer is not a simple replacement for perspective planar tracking.

**Related deep dives:** [Point tracking, attach points and drift](#topic-point-tracking), [Mocha AE planar tracking](#topic-mocha), [Warp Stabilizer and camera motion](#topic-stabilization)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-roto"></a>
### 20 · Roto Brush, Refine Edge and mask tracking

**Stage:** INTERMEDIATE
**Why:** Extract moving subjects without the 2026 Object Matte feature.

1. Duplicate a video layer and open that layer in the Layer panel, not only the Composition panel. Activate Roto Brush (Alt+W) and create foreground strokes where the intended subject has recognizable edges.
2. Use Alt with the brush, where supported, to subtract incorrectly selected regions. Identify the base frame and propagate forward/backward through a manageable span.
3. Scrub the full span and repair frames that drift, especially fast-moving hands, occlusions and hair. Use Refine Edge on semitransparent detail only after the main segmentation is stable.
4. Adjust Reduce Chatter, Feather, Shift Edge and Decontaminate Edge Colors as warranted, then Freeze propagation for the span. Keep the source footage available; Freeze is not the same as rendering a permanent matte file.
5. Use Mask Tracking on an appropriately drawn mask for rigid, easy-to-follow objects. If motion is complex, consider manual correction or a separate point/planar track.
6. Pre-render a clean RGBA intermediate when editing further becomes slow; verify that the output format actually retains an alpha channel.

**Do it yourself:** Cut a person out of an indoor clip and place a moving procedural texture behind the subject.

**Self-check:**
- [ ] I can roto a 2-second moving subject.
- [ ] I understand propagation and Freeze.
- [ ] I can choose mask tracking vs Roto Brush.

**Common mistakes:**
- Object Matte is also available; compare subject selection with brush-guided roto and mask tracking.
- Freezing a roto span does not replace checking every frame.

**Related deep dives:** [Roto Brush and Refine Edge alongside Object Matte](#topic-roto), [Alpha, straight RGB and premultiplication](#topic-alpha), [Tracked masks vs hand-roto](#topic-mask-tracking)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-paint"></a>
### 21 · Paint, clone and Content-Aware Fill

**Stage:** INTERMEDIATE
**Why:** Moving from an obvious brush stroke to credible invisible repair requires temporal checking.

1. Double-click footage to work in the Layer panel. Use Brush, Clone Stamp and Eraser there; the same tool is not just a normal Comp-view shape brush.
2. Set a Clone Stamp sampling point with Alt+click. Paint a small patch on a duplicate and test source alignment and stroke duration modes in the Paint panel.
3. Make a simple repair with painting, then preview over time. A correction that matches one frame can slide or flicker after motion unless properly tracked or the paint is adjusted.
4. Use a mask around an unwanted object, follow it with keyframes or tracking, and open Window → Content-Aware Fill. Select the appropriate Fill Method and Range, then Generate Fill Layer.
5. For a difficult frame, create a reference frame in Photoshop (when available) or a suitable still-image editor; fill the defect and return the reference to AE. Manage source paths and regenerated fills.
6. Evaluate repeated textures, camera motion, shadows and occlusion. Sometimes a clean plate plus planar tracking is more reliable than automated Fill.

**Do it yourself:** Remove a small stationary sticker from a 2-second shot with a moving handheld camera.

**Self-check:**
- [ ] I can clone a small detail.
- [ ] I can generate a Content-Aware Fill layer.
- [ ] I know when to use a tracked clean plate.

**Common mistakes:**
- Brush/Clone Stamp stroke duration matters.
- Content-Aware Fill may hallucinate repetition or change a texture over time.

**Related deep dives:** [Brush and Clone Stamp in Layer panel](#topic-paint), [Content-Aware Fill video cleanup](#topic-content-aware-fill), [Mask modes and feathering](#topic-masks)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-camera"></a>
### 22 · 2.5D parallax, cameras and lights

**Stage:** INTERMEDIATE
**Why:** AE 3D layers exist in 3D space, but not every 3D-looking effect behaves as scene geometry.

1. Turn on 3D switches for several photos or shape layers and separate them in Z depth. Create a Camera (Ctrl+Alt+Shift+C). Distinguish 1-node and 2-node camera behavior, point of interest, zoom and field of view.
2. Create a Camera orbit Null and parent the camera to it for controlled moves, or animate camera Position/Point Of Interest intentionally. Use multiple views to check that foreground and background have the desired depth separation.
3. Add a Light (Ctrl+Alt+Shift+L) and test Material Options on 3D layers. Understand Accepts Lights/Shadows and limitations of the selected 3D renderer.
4. Switch Project Settings/Composition Advanced 3D renderer only intentionally; Classic 3D, Cinema 4D and Advanced 3D do not have identical feature sets. Test native 3D models where supported.
5. In After Effects 26.5, select multiple 3D layers to use the shared/single 3D transform gizmo; also inspect View → Default Camera Settings for the new default camera controls.
6. For camera depth of field, use Advanced 3D’s in-engine DOF (available since 26.3) and inspect Camera Options focus and aperture. A 2D Camera Lens Blur map is a different workflow.

**Do it yourself:** Create a 6-second dolly move through three cut-out images at different Z positions, avoiding obvious image edges.

**Self-check:**
- [ ] I can make a 3-layer parallax scene.
- [ ] I can distinguish renderers and camera types.
- [ ] I can locate shared gizmo controls.

**Common mistakes:**
- 2D effects like CC Sphere or 3D Channel effects do not become scene geometry by naming alone.
- Advanced 3D renderer feature support differs from Classic 3D.

**Related deep dives:** [2.5D layers and spatial depth](#topic-3d-intro), [Camera nodes, POI and projection](#topic-cameras), [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers), [GLTF/GLB/OBJ/FBX and environment lights](#topic-3d-models)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history), [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="lesson-3dtrack"></a>
### 23 · Camera tracking and screen replacement

**Stage:** INTERMEDIATE
**Why:** Choose a scene-solving tool based on camera motion rather than the look of the final effect.

1. Use a shot with real parallax: camera moves through a room rather than only rotating from one point. Apply 3D Camera Tracker and allow Analysis/Solving to finish.
2. Inspect the track points and locate a plausible horizontal plane. Target a triad and create a Solid/Camera or Text/Camera. Check the solved graphic over all frames, not only the initial one.
3. If the solve is unstable, inspect fast pans, rolling shutter, motion blur, zoom changes, focal length and low-parallax shots. Trim and stabilize the analysis source where justified.
4. For a planar phone screen, compare Mocha AE corner pin or built-in perspective tracker. Use a high-contrast planar patch, not an assumption that a 3D camera solve will always be superior.
5. Track a sign or poster, then apply Corner Pin/CC Power Pin to the replacement screen. Control the insert’s color, noise and motion blur to match the plate.
6. Export a diagnostic video showing the tracker points or a checkerboard overlaid on the final surface; a drifting corner is easier to catch with a grid than with a textured replacement.

**Do it yourself:** Replace a moving phone screen with a checkerboard, then with a custom animated interface.

**Self-check:**
- [ ] I can solve a simple parallax clip.
- [ ] I can choose a planar track for a screen.
- [ ] I can check perspective replacement on every frame.

**Common mistakes:**
- 3D Camera Tracker will not solve every low-parallax or heavily blurred clip.
- Screen corner tracking is not equivalent to full-scene camera recovery.

**Related deep dives:** [3D Camera Tracker and solved scenes](#topic-camera-tracker), [Mocha AE planar tracking](#topic-mocha), [Corner Pin and perspective insertion](#topic-perspective)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-color"></a>
### 24 · Color correction, working space and alpha

**Stage:** INTERMEDIATE
**Why:** Correct color requires keeping separate input interpretation, working-space math, display, and output.

1. In File → Project Settings → Color, compare color-managed versus unmanaged workflows in a small 8/16/32-bpc experiment. Choose an intentional Working Color Space for the target delivery.
2. Inspect an imported image’s Interpret Footage color settings. When necessary, assign the right input profile; assigning a profile changes interpretation and is not the same thing as changing RGB values with an effect.
3. Use Lumetri Color, Curves and Levels on a test image. Correct exposure/contrast/white balance first, then make a look. View histograms or scopes where available and compare to a controlled reference.
4. Understand straight vs premultiplied alpha and RGB in transparent pixels. Remove Color Matting when necessary; a matte halo is not always fixed by globally sharpening an image.
5. For an OCIO/ACES workflow, open Project Settings → Color, select OCIO color managed, choose ACES 2.0 CG v4.0 or Studio v4.0, and explicitly set input, working, display and output spaces. Test a short render before changing an established project’s configuration.
6. Export a tagged test image/video and compare the rendered file in a color-managed viewer. Different Windows video apps may apply different display transforms; check metadata, not just eye judgment.

**Do it yourself:** Grade the same PNG to neutral in an 8-bpc unmanaged project and a 16-bpc color-managed project; document the differences.

**Self-check:**
- [ ] I know input vs working vs display vs output space.
- [ ] I can explain 8/16/32 bpc.
- [ ] I can test alpha against light/dark backgrounds.

**Common mistakes:**
- Increasing bpc does not restore clipped source data.
- Changing an existing project’s ACES configuration can change its appearance; preserve a known-good copy and compare renders.

**Related deep dives:** [RGB, color profiles and grade order](#topic-color), [8/16/32 bpc and floating point](#topic-color-depth), [OCIO/ACES 2.0 in a 26.5 project](#topic-ocio), [Alpha, straight RGB and premultiplication](#topic-alpha)

**Sources:** [Adobe: color management](https://helpx.adobe.com/after-effects/desktop/adjust-colors/color-management/color-management.html), [Adobe: OpenColorIO and ACES](https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="lesson-expressions"></a>
### 25 · Expressions: build a repeatable controller

**Stage:** INTERMEDIATE
**Why:** Expressions compute property values; learn safe interfaces before writing complex JavaScript.

1. Create a Null named CTRL. Apply Effect → Expression Controls → Slider Control, rename it Speed. On another layer’s Rotation, Alt+click its stopwatch once and enter time*thisComp.layer('CTRL').effect('Speed')('Slider');.
2. Set Speed to 0, 90 and -45; verify that the graphic stops, rotates clockwise and counterclockwise. Your expression needs a numeric output because Rotation expects a scalar.
3. On a 2D Position property, enter wiggle(1,20); and compare with value+[Math.sin(time*2)*20,0];. Distinguish nondeterministic-looking wiggle from smooth periodic motion.
4. Make a 2D Scale expression using [100,100] or [s,s], not a lone scalar. Learn value, time, thisComp, thisLayer, framesToTime(), ease(), linear(), clamp(), loopOut().
5. Create two expression-linked layers using the pick whip rather than manually typing names, then rename a controller and inspect references. Handle missing effects or source layer changes carefully.
6. Toggle an expression off without deleting it. Use Animation → Keyframe Assistant → Convert Expression to Keyframes to bake a copy when needed for portability or delivery.

**Do it yourself:** Build one Null with Speed, Amount and Color Control driving a three-layer animated indicator.

**Self-check:**
- [ ] I can create a slider-controlled rotation.
- [ ] I can return the correct value dimension.
- [ ] I can disable vs delete an expression.

**Common mistakes:**
- Expressions are not general browser JavaScript; DOM/HTML APIs are unavailable.
- An expression controller can introduce a fragile dependency on its layer name.

**Related deep dives:** [Expression evaluation and safe syntax](#topic-expressions), [JavaScript-like expressions, coordinates and values](#topic-expression-language), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls), [Copyable expression building blocks](#topic-expression-examples), [Modern dropdown labels, key lookup and range mapping](#topic-expression-lookup)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html), [Adobe: understanding expression language](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-basics/expression-language.html)

<a id="lesson-object-selection"></a>
### 26 · Object Matte with frame-by-frame quality control

**Stage:** INTERMEDIATE
**Why:** Use the current selection workflow and verify its cached propagation.

1. Choose a two-second shot with a clear subject and preserve the original footage. Double-click the layer into Layer panel and choose the Object Matte toolbar tool.
2. Hover the subject and click to select; correct the base frame using Quick Selection or Selection Brush. Use Refine Edge for appropriate hair detail.
3. Propagate across the intended range; inspect occlusions, hands and fast turns. Correct failed frames instead of assuming a green cache bar proves accuracy.
4. Freeze the reviewed result and return to Composition. Compare it over black, white and saturated backgrounds, inspecting alpha as well as RGB.
5. Save and reopen a test project. Compare 26.5 disk-cached propagation, then render an alpha-capable short master; retain source media and the project separately.
6. Use the isolated layer as an Alpha Matte for a separate animated texture. Verify it follows the silhouette without unnecessarily showing the matte as an independent layer.

**Do it yourself:** Compare Object Matte and brush-guided roto on the same difficult turn and keep the cleaner result.

**Self-check:**
- [ ] I can select and refine an object.
- [ ] I can judge matte stability across frames.
- [ ] I can distinguish disk-cached analysis from a final RGBA export.

**Common mistakes:**
- Ctrl+W is documented ambiguously; choose the toolbar or verify the installed editor.
- A cache is not an asset backup.

**Related deep dives:** [Object Matte: select, propagate, refine and cache](#topic-object-matte), [Roto Brush and Refine Edge alongside Object Matte](#topic-roto), [Alpha/luma track mattes](#topic-mattes)

**Sources:** [Adobe: AI-powered Object Matte](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-modern-type"></a>
### 27 · SVG and variable-font motion

**Stage:** INTERMEDIATE
**Why:** Bring editable vectors into a current typography workflow.

1. Import samples/badge.svg as footage and again as a composition. Compare source linkage, editable Contents and the rendered appearance.
2. If Illustrator is available, enable Include SVG Code in its Clipboard Handling preferences, copy outlined vector art and paste into an active AE comp. Inspect fills and grouping.
3. Create a text layer using an installed variable font. Expand Text → Animate → Variable Font Axes and choose an axis that the font actually supports.
4. Create an initial axis keyframe at time zero, move 24 frames and change the value within its supported range. Add a Range Selector for character timing.
5. Compare Variable Font Spacing modes and long/short text strings. Use native shapes or text layers deliberately; editable SVG geometry is not editable Illustrator text.
6. Render a 48-frame sample and inspect sharpness, glyph spacing and line wrapping. Record the exact font family/file needed for handoff.

**Do it yourself:** Make a two-second badge reveal with a weight change and a Trim Paths accent.

**Self-check:**
- [ ] I can choose editable SVG or linked footage.
- [ ] I can animate an available variable-font axis.
- [ ] I can verify typography dependencies.

**Common mistakes:**
- Use a variable font, not merely a static family with several weights.
- SVG text clipboard conversion is not supported by the stable shape route.

**Related deep dives:** [SVG file import and vector clipboard transfer](#topic-svg-workflow), [Animate variable-font axes and spacing](#topic-variable-fonts), [Text animators and selectors](#topic-text-animator)

**Sources:** [Adobe: SVG import and clipboard transfer](https://helpx.adobe.com/after-effects/desktop/import-files/import-svg-files/import-svg-files.html), [Adobe: Working with Variable Font Axes](https://helpx.adobe.com/after-effects/desktop/variable-font-axes/work-with-variable-font-axes/working-with-variable-font-axes.html)

<a id="lesson-flow-alpha"></a>
### 28 · Curl Noise, Unmult and audio dynamics

**Stage:** INTERMEDIATE
**Why:** Use current native effects for texture, alpha and sound.

1. Create a comp-sized solid, open Quick Apply and apply e:curl noise. Start with Internal input and compare Scale and Swirl separately.
2. Animate a short texture using the intended Evolution/motion controls. Colorize with Tint or Tritone and inspect aliasing at Full resolution.
3. Precompose the texture and use it as a luma matte on another layer. Confirm whether the consuming effect/matte samples the stage you intended.
4. On a suitable black-backed element apply Unmult, choose its background mode and inspect alpha. Tune level/softness and test over dark and bright backgrounds.
5. On a duplicate audio layer try Compressor, Gate and Distortion one at a time. Compare bypass at similar loudness and preserve spoken word endings.
6. Render a short review with audio and an alpha-capable element separately. Reimport to verify the channel behavior and listen to the processed sound.

**Do it yourself:** Build an abstract flowing title transition and document the purpose of each effect in its stack.

**Self-check:**
- [ ] I can distinguish a procedural texture from a fluid simulation.
- [ ] I can create real alpha from an appropriate backing.
- [ ] I can compare processed audio without confusing loudness with quality.

**Common mistakes:**
- Unmult may remove genuine foreground black/white without a protective matte.
- Gate does not remove room noise underneath speech.

**Related deep dives:** [Curl Noise: a flowing texture experiment](#topic-curl-noise), [Unmult: convert a black or white backing into alpha](#topic-unmult), [Compressor, Gate and Distortion in 26.5](#topic-audio-dynamics)

**Sources:** [Adobe: Noise, grain and Curl Noise](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html), [Adobe: Keying and Unmult](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html), [Adobe: Audio effects](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/audio-effects.html)

<a id="lesson-data"></a>
### 29 · Data-driven text and graphics

**Stage:** ADVANCED
**Why:** Separate content from animation so recurring work is faster to update.

1. Create a small UTF-8 CSV or TSV with name, score and color columns. Import it as data through File → Import and inspect its accessible data properties.
2. For JSON use footage('stats.json').sourceData.score. For CSV/TSV add the data item to a test comp, expand Data and pick-whip the intended cell; inspect its generated dataValue path and compare against the table before building row logic.
3. Create a Score text layer and set Source Text from a suitable string expression. Format numbers deliberately with Math.round(), toFixed() or String() where appropriate.
4. Build a background rectangle sized to text with sourceRectAtTime(); add horizontal and vertical padding, and inspect left/top offsets to avoid misalignment.
5. Try importing a small JSON object as footage and reading a nested key by expression using footage('filename.json').sourceData. Keep field names stable and check for missing keys.
6. Make a reusable template with editable content and named controls. Document what changes without touching timeline keys.

**Do it yourself:** Make a three-slide statistics board generated from a CSV, each with an auto-sized number card.

**Self-check:**
- [ ] I can import one data file.
- [ ] I can link text to a value.
- [ ] I can keep animated layout working after the string changes.

**Common mistakes:**
- Imported data schema paths are easy to misaddress: inspect the data structure.
- SourceText may contain formatted objects; test with the target 26.5 JavaScript expression engine.

**Related deep dives:** [CSV, JSON and AE data inputs](#topic-data), [Expression evaluation and safe syntax](#topic-expressions), [sourceRectAtTime and dynamic card padding](#topic-auto-layout)

**Sources:** [Adobe: Data-driven animations](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/data-driven-animation/data-driven-animations.html), [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="lesson-templates"></a>
### 30 · Essential Properties and MOGRT delivery

**Stage:** ADVANCED
**Why:** Build assets that another editor can adjust without breaking a controlled design.

1. Create a child comp containing a title, subtitle, color plate and simple entrance animation. Open Window → Essential Graphics and select the correct master composition.
2. Expose editable Source Text, key color controls and a Slider into Essential Graphics. Rename controls clearly, group when appropriate and provide default values.
3. Nest the child comp twice; inspect Essential Properties for each instance. Change one instance’s title and color while retaining the original child comp and other instance.
4. Test protected regions for intro/outro timing when building a reusable MOGRT, then stretch a middle region in a deliberately long test comp. Check that animation does not overlap unexpectedly.
5. Export a Motion Graphics Template (.mogrt) and choose the correct destination; use a video preview where supported. Verify third-party fonts/plugins or expression dependencies.
6. Open or install the MOGRT in a compatible Adobe workflow where available; test exposed controls, resolution and duration. Retain the original .aep and assets as source of truth.

**Do it yourself:** Make a lower-third MOGRT with name, role, primary color and adjustable hold duration.

**Self-check:**
- [ ] I can expose one editable text property.
- [ ] I can customize two comp instances.
- [ ] I know the distinction between a .mogrt and an .aep.

**Common mistakes:**
- MOGRT export cannot magically package every third-party dependency.
- Essential Properties are instance overrides, not a replacement for all original animation data.

**Related deep dives:** [Essential Properties as instance controls](#topic-essential-properties), [Motion Graphics templates and protected timing](#topic-mogrt), [Precomposition and nested timeline logic](#topic-precomp)

**Sources:** [Adobe: create Motion Graphics templates](https://helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html)

<a id="lesson-advanced3d"></a>
### 31 · Native 3D models, environments and renderers

**Stage:** ADVANCED
**Why:** Combine imported models with native meshes and supported materials in Advanced 3D.

1. Import a supported GLB/GLTF/OBJ or FBX model appropriate to your project. Inspect scale, axes, texture material paths and animation playback.
2. Create a 3D composition using the Advanced 3D renderer. Add an environment light or HDRI for reflections and test an animated environment light (introduced in 25.2).
3. Check each model’s Material Options, Accepts Lights, Shadows and shadow-catcher workflow. Compare quality/performance options and confirm the actual render, not only Fast Draft.
4. Use the shared single 3D gizmo on multiple selected 3D layers (25.6 feature) to transform as a group visually. Learn that it changes individual layers; it is not necessarily a persistent parent rig.
5. Change View → Default Camera Settings (25.6) to adjust the way default/custom views behave. Save a test and inspect composition views before and after.
6. Create a native mesh with the Parametric Mesh tool or Layer → New. Adjust Mesh Options and material roughness/metallic controls; import an SBSAR material to compare. Keep this separate from Beta-only materials on 3D text/shapes.

**Do it yourself:** Build an 8-second product turntable using a supported 3D model and a controlled camera orbit.

**Self-check:**
- [ ] I can import one model and light it.
- [ ] I can test an environment light.
- [ ] I can compare imported models and native meshes.

**Common mistakes:**
- 3D model and material import support varies by format/renderer.
- An emissive-looking material does not illuminate nearby geometry; use an actual light for that.

**Related deep dives:** [GLTF/GLB/OBJ/FBX and environment lights](#topic-3d-models), [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers), [Camera nodes, POI and projection](#topic-cameras), [Native parametric meshes and material appearance](#topic-parametric-meshes), [Substance SBSAR and real mesh displacement](#topic-substance-materials)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history), [Adobe: Create parametric meshes](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html), [Adobe: Apply Substance 3D materials](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/apply-substance-3d-materials.html)

<a id="lesson-puppet"></a>
### 32 · Puppet rigging and deformation

**Stage:** ADVANCED
**Why:** Animate flexible artwork without cutting it into dozens of rigid pieces.

1. Import a transparent character or ribbon. Duplicate the source and apply Puppet pins to a clean alpha layer while in the relevant Puppet tool mode.
2. Add pins to stable regions first: base/shoulder, elbow and tip. Move a single pin over time and inspect how the mesh deforms between pins.
3. Explore Overlap and Starch tools to control drawing order and rigidity in supported Puppet modes. Place pins where the mesh should bend and where it should resist stretching.
4. Reduce pin counts until you can understand every pin. An over-constrained mesh creates awkward hard bends or almost no visible motion.
5. Precompose when the Puppet effect needs to move with a separate rigid transform. Compare deform-then-scale with scale-then-deform in your hierarchy.
6. Render a seamless 2-second loop; inspect pin intersections and anti-aliased alpha edges at every extreme.

**Do it yourself:** Make a waving flag or cartoon arm bend while its base remains fixed.

**Self-check:**
- [ ] I can make a simple Puppet mesh.
- [ ] I can set stiffness/overlap deliberately.
- [ ] I can animate a clean loop.

**Common mistakes:**
- Puppet is a deformation tool, not skeletal 3D rigging by itself.
- Tiny transparent holes can distort a mesh unexpectedly.

**Related deep dives:** [Puppet deformation and mesh setup](#topic-puppet), [Alpha, straight RGB and premultiplication](#topic-alpha), [Precomposition and nested timeline logic](#topic-precomp)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-particles"></a>
### 33 · Native particle and simulation systems

**Stage:** ADVANCED
**Why:** Learn particle emitters, lifetimes and physics controls through measurable experiments.

1. Apply CC Particle World to a solid. Find Producer Position and Radius, Birth Rate, Longevity, Particle Type, Velocity, Gravity and Resistance controls.
2. Set Birth Rate low and Longevity short. Measure how many visible particles appear at once; rough steady count depends on rate × lifetime, though frame integration and fade settings affect the rendered result.
3. Make a second particle system using CC Particle Systems II. Compare available controls and rendering performance instead of assuming both systems are interchangeable.
4. Try CC Rainfall or CC Snowfall and then Foam or CC Bubbles. Understand emitter-based versus image-distortion-based animation.
5. Precompose particle sources when layering glow, blur and mattes. Test whether effect order changes source/particle size or the glow of particles.
6. Make a 5-second rain field that respects foreground occlusion via track matte and includes variation in size, velocity and blur.

**Do it yourself:** Create a burst that emits for 12 frames, falls under gravity and fades within 3 seconds.

**Self-check:**
- [ ] I can control birth rate and lifetime.
- [ ] I can compare native particle tools.
- [ ] I can matte particles behind an object.

**Common mistakes:**
- Particle count is not simply Birth Rate without accounting for particle lifetime.
- Some CC effects expose controls in normalized coordinates, not comp pixels.

**Related deep dives:** [Particles, emitters and simulation](#topic-particles), [Other simulation and stylize effects](#topic-simulations), [Effects, presets and compatibility](#topic-effects)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-automation"></a>
### 34 · ExtendScript, scripts and batch workflow

**Stage:** ADVANCED
**Why:** Understand which tasks need property expressions and which need application automation.

1. Distinguish expressions (a formula on a property, evaluated over time) from ExtendScript/JSX scripts (commands that build or edit project objects). A property expression cannot import and rename 200 files or create arbitrary layers.
2. Learn the project object model at a high level: app.project, items, compositions, layers, properties, keyframes, and render queue items. Keep automation scripts narrowly scoped.
3. Create a reversible experiment: a simple JSX script run through File → Scripts → Run Script File that makes a named solid and saves no files automatically. Review permissions/prefs relevant to scripts before running.
4. Use undo groups around edits and test on a copy. Always guard the selected item type and active composition before dereferencing it.
5. For external data, prefer explicit JSON/CSV inputs, deterministic naming and a record of generated assets. Do not put sensitive information inside easily shared project expressions.
6. Try a batch task such as renaming layers with a prefix or setting comp frame rates only after manually checking the intended targets. Compare before/after project structure.

**Do it yourself:** Write a short JSX script that enumerates comp names and reports them, without changing the project.

**Self-check:**
- [ ] I can distinguish JSX scripts from expressions.
- [ ] I can describe project item vs layer objects.
- [ ] I can test scripts safely on a copy.

**Common mistakes:**
- Scripts can alter a project or access files; only run code you understand and trust.
- An expression’s JavaScript support is not the same as a script’s API.

**Related deep dives:** [ExtendScript and project automation](#topic-scripting), [Expression evaluation and safe syntax](#topic-expressions), [Folders, naming and backup policy](#topic-project-management), [Copyable expression building blocks](#topic-expression-examples)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="lesson-mesh-focus"></a>
### 35 · Native mesh materials and an Advanced 3D rack focus

**Stage:** ADVANCED
**Why:** Combine stable geometry, material and camera tools in one controlled scene.

1. Create a new comp using Advanced 3D. Add a cube and sphere using the Parametric Mesh tool or Layer → New, placing them at different camera distances.
2. Adjust Mesh Options and contrasting Roughness/Metallic material values. Use a real light/environment and compare highlights with camera movement.
3. If an SBSAR is available, import and apply it to a supported mesh. Test modest material displacement on the mesh, checking silhouette and rendering cost.
4. Create a camera, enable Depth of Field and focus the near object. Adjust Aperture and Blur Level, then keyframe Focus Distance toward the far object.
5. Render a 48-frame test in Active Camera. Check focus at the first, middle and final frame and compare Full-quality output with the interactive preview.
6. Collect the test project and dependencies. Keep materials on 3D text/shapes and animated layers as material inputs out of this stable-only exercise; those are separate Beta capabilities.

**Do it yourself:** Create a product-style orbit with one controlled rack focus and a written material/dependency list.

**Self-check:**
- [ ] I can create native geometry.
- [ ] I can distinguish displacement from a 2D warp.
- [ ] I can render-check a camera focus change.

**Common mistakes:**
- Emission appearance does not illuminate nearby geometry.
- A flat CC Sphere effect is not the mesh created here.

**Related deep dives:** [Native parametric meshes and material appearance](#topic-parametric-meshes), [Substance SBSAR and real mesh displacement](#topic-substance-materials), [Advanced 3D in-engine depth of field](#topic-advanced-dof)

**Sources:** [Adobe: Create parametric meshes](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html), [Adobe: Apply Substance 3D materials](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/apply-substance-3d-materials.html), [Adobe: Modify materials and displacement](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/modify-materials-properties-of-3d-layers.html), [Adobe: Advanced 3D in-engine depth of field](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-3d-scene-depth-data/enable-in_engine-depth-of-field-in-advanced-3d.html)

<a id="lesson-render"></a>
### 36 · Render Queue, codecs, alpha and audio

**Stage:** DELIVERY
**Why:** Choose the output to match its downstream use and verify what the render actually contains.

1. Save your project. Select the final composition and use Ctrl+Shift+/ to add it to Render Queue. Inspect Render Settings, Output Module, and Output To separately.
2. Set a working review output, such as an H.264 MP4 where the installed 26.5 encoder and selected output route support it. Alternatively queue an Adobe Media Encoder output using Ctrl+Alt+M. Do not rely on one codec for every delivery.
3. For a master or intermediate, choose a high-quality suitable codec such as ProRes or DNxHR (where available), or an image sequence. Specify bit depth, frame rate, color tagging and audio as intended.
4. For transparency, use a format/codecs that support alpha, select RGB+Alpha, and specify Straight or Premultiplied according to downstream requirements. Standard H.264 MP4 generally does not carry normal AE RGBA transparency.
5. Render only intended work area or entire comp explicitly. Check that the final frame, 100% resolution, high-quality sampling and motion blur correspond to your delivery requirements.
6. Open the rendered output in a separate player/editor. Count frames, inspect audio sync, color, alpha and first/last frame. A successful Render Queue status does not certify the file is correct.

**Do it yourself:** Deliver one MP4 review, one transparent master or PNG sequence, and a written export checklist.

**Self-check:**
- [ ] I can export a review movie and an RGBA master.
- [ ] I can distinguish render settings vs output module.
- [ ] I can inspect a render externally.

**Common mistakes:**
- Choosing RGB+Alpha does nothing if the selected codec/container cannot carry an alpha channel.
- Rendered H.264 export is not the same as saving an editable project.

**Related deep dives:** [Render Queue decisions and preflight](#topic-export), [Containers, codecs, sequences and masters](#topic-codecs), [Alpha, straight RGB and premultiplication](#topic-alpha), [Audio preview, sync and output](#topic-audio)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-collect"></a>
### 37 · Backups, Collect Files and team handoff

**Stage:** DELIVERY
**Why:** Keep a project reproducible after assets move or the original editor is unavailable.

1. Save the working .aep, then use File → Dependencies → Collect Files to gather used sources into a package. Read the available options and select a dedicated collection folder.
2. Relocate/copy the collected folder to a different Windows path or drive letter, open the collected .aep and verify it uses collected assets rather than the old disk locations.
3. Audit installed fonts, effects, scripts, external 3D textures, render destinations, proxies and dynamically linked dependencies. Collect Files is not a guarantee of third-party plugin portability.
4. Generate an explicit README listing AE version 26.5, frame rates, render settings, color management, input dependencies, licensed assets and any known limitations.
5. Use versioned project saves such as Project_v001.aep and Increment and Save; maintain automated backups where configured. Restore a backup before trusting the process.
6. Consider making a high-quality pre-render or flattened proof video for reviewers who cannot open AE. Keep editable project and rendered approval media separate.

**Do it yourself:** Move the collected package to a different drive/path and re-open all comps without missing-file dialogs.

**Self-check:**
- [ ] I can collect and reopen a project from a new path.
- [ ] I have a dependency manifest.
- [ ] I can restore a previous project version.

**Common mistakes:**
- Collect Files does not bundle Adobe subscription licenses or every installed plugin.
- An .aep file by itself often cannot reproduce a project.

**Related deep dives:** [Folders, naming and backup policy](#topic-project-management), [Collect Files and portability](#topic-collect-files), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-performance"></a>
### 38 · Performance, memory, cache and proxies

**Stage:** DELIVERY
**Why:** Optimize the actual bottleneck instead of deleting caches reflexively.

1. Save a slow experiment project. Time a cold preview and a repeated warm preview over the same work area before changing settings.
2. Set viewer resolution Half or Quarter for fast interaction when appropriate; note that changing view quality does not automatically guarantee a full-resolution final render.
3. Inspect Edit → Preferences → Memory & Performance and Disk Cache settings. Reserve adequate RAM for Windows, choose a fast drive with spare capacity, and understand that purging invalidates useful cached frames.
4. Compare one CPU-bound procedural effect, GPU-accelerated effect, and codec-decoding bottleneck. Watch whether performance changes when an effect switch is turned off.
5. Use proxy footage or pre-renders for expensive sources and comps when appropriate. Keep a clear replacement/restore path so that final output uses the intended sources.
6. Check Multi-Frame Rendering and limitations of plugins. For a pathological project, disable suspect third-party effects one at a time and test safe startup rather than assuming the GPU always causes slowdowns.

**Do it yourself:** Create a before/after timing sheet for a 5-second heavy effects comp with two controlled optimization changes.

**Self-check:**
- [ ] I can separate first render from cached preview.
- [ ] I can find RAM and disk-cache settings.
- [ ] I can make a measurable performance comparison.

**Common mistakes:**
- Clearing the disk cache can make a project slower temporarily.
- A faster SSD does not cure an expensive single-frame effect algorithm.

**Related deep dives:** [RAM, disk cache and preview rate](#topic-performance), [Cache levels, purging and invalidation](#topic-cache), [Proxies, pre-renders and fast preview](#topic-proxies)

**Sources:** [Adobe: memory and storage](https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html), [Adobe: multi-frame rendering](https://helpx.adobe.com/after-effects/desktop/render-and-export/multi-frame-rendering/multi-frame-rendering.html)

<a id="lesson-debug"></a>
### 39 · Diagnose broken results systematically

**Stage:** DELIVERY
**Why:** Identify whether a problem is source, interpretation, transform, matte, effect, render or environment.

1. When the Comp viewer is black, check active comp, time, layer In/Out, eye, solo, opacity, mask, matte, blend mode and viewer channel before touching effects.
2. If the result is different after precomposing, compare render order, collapse transformations, effect stacks, adjustment layer scope and color management.
3. If preview is frozen, disable Caps Lock, inspect Preview settings and work area, then confirm a frame has been rendered. Restart only after a simple reproducible check.
4. If an effect is missing, inspect Effect Manager, plugin installation, 8/16/32-bpc support and whether it is stable in 26.5 or Beta-only. Replace unsupported features rather than inventing a hidden menu.
5. If output differs from Comp viewer, compare Render Settings, Output Module, output color space, channel selection, renderer and file playback transform.
6. Create a reduced reproducible .aep by duplicating the comp and removing half of its layers/effects, repeatedly narrowing the issue. Save before deleting or purging.

**Do it yourself:** Intentionally hide a layer with a matte and an effect, then diagnose the failure in a fixed checklist without random clicking.

**Self-check:**
- [ ] I can isolate a black-frame cause.
- [ ] I can compare viewer/render settings.
- [ ] I can build a minimal reproduction.

**Common mistakes:**
- A render queue completion message means the job finished, not that visual, alpha or audio QC passed.
- Caps Lock can inhibit viewer updates.

**Related deep dives:** [A structured debug decision tree](#topic-diagnostics), [Missing plugins, effects and unsupported version](#topic-missing-effects), [Alpha, straight RGB and premultiplication](#topic-alpha), [RGB, color profiles and grade order](#topic-color)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="lesson-capstone"></a>
### 40 · Complete project: 10-second motion graphics composite

**Stage:** CAPSTONE
**Why:** Combine foundations, animation, keying, data, effects, sound and export into a repeatable deliverable.

1. Create a clearly labeled 1920×1080 24 fps comp called FINAL_10S. Import or generate a 10-second background, a branded shape/title, and short WAV music/sound effects; keep the source files in project Assets.
2. Build a 2-second introductory title. Use a masked or matted reveal, controlled easing, and motion blur. Keep typography clear and safe from frame edges.
3. At 2–6 seconds, animate a set of three cards with a Null controller and either a text animator or template-driven properties. Make their timing editable without rebuilding the graphic.
4. Add a short compositing moment: tracked corner-pin insert, a keyed subject or a clean roto. Do not fake one if source footage is unavailable; use a self-generated shape/matte demonstration and document the substitution.
5. At 6–9 seconds, finish a procedural transition using Fractal Noise, Displacement Map or Glow. Audio should enter and leave cleanly, and the last second should contain a readable final message.
6. Audit at Full resolution: typography, alpha edges, layer order, no one-frame flash, camera position, color and clipping. Render a review movie and an archival-quality master; collect project files and write a delivery note.

**Do it yourself:** Grade yourself: can you rebuild 80% of the sequence from scratch with your own footage and no tutorial?

**Self-check:**
- [ ] I can deliver a complete timeline.
- [ ] My project reopens without missing assets.
- [ ] I can explain every element and effect in the render.

**Common mistakes:**
- Do not judge a project only by rendered appearance; reproducibility and clean dependencies matter.
- Use the stable 26.5 feature set throughout and document dependencies.

**Related deep dives:** [Repeatable production and QC workflow](#topic-workflow), [Final self-assessment and future practice](#topic-capstone), [Render Queue decisions and preflight](#topic-export), [Folders, naming and backup policy](#topic-project-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

---

## Deep topic index

- [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow)
- [Earlier 25.6 features retained in 26.5](#topic-25-6-features)
- [The Windows After Effects interface](#topic-interface)
- [Composition, layer and project hierarchy](#topic-layer-anatomy)
- [Folders, naming and backup policy](#topic-project-management)
- [Import formats, sequences and linked files](#topic-import-media)
- [Footage frame rate, alpha and pixel aspect](#topic-footage-interpretation)
- [FPS, timecode and frame alignment](#topic-frames)
- [Layer bounds, work areas and markers](#topic-timeline)
- [Coordinates, anchor points and transforms](#topic-coordinates)
- [Parenting, nulls and reusable rigs](#topic-parenting)
- [Keyframes and interpolation](#topic-keyframes)
- [Value Graph, Speed Graph and easing](#topic-graph-editor)
- [Timing and design principles for readable motion](#topic-motion-design)
- [Parametric shapes vs Bézier paths](#topic-shapes)
- [Masks, shape paths and motion paths](#topic-paths)
- [Shape strokes, Trim Paths and Write-on](#topic-strokes)
- [Mask modes and feathering](#topic-masks)
- [Alpha, straight RGB and premultiplication](#topic-alpha)
- [Alpha/luma track mattes](#topic-mattes)
- [Layer blend modes and compositing](#topic-blending)
- [Effect and transform evaluation order](#topic-render-order)
- [Precomposition and nested timeline logic](#topic-precomp)
- [The effect stack and control surfaces](#topic-effect-order)
- [Effects, presets and compatibility](#topic-effects)
- [Adjustment layers and global looks](#topic-adjustment-effects)
- [Gaussian, lens and map-driven blur](#topic-blur)
- [Fractal/Turbulent Noise and displacement](#topic-procedural)
- [Displacement, depth and faux 3D](#topic-depth-maps)
- [Time remapping, reversal and loops](#topic-time-remap)
- [Native motion blur and shutter settings](#topic-motion-blur)
- [Point/box text, metrics and typography](#topic-text)
- [Text animators and selectors](#topic-text-animator)
- [Kinetic typography and text clarity](#topic-type-design)
- [Audio preview, sync and output](#topic-audio)
- [Convert Audio to Keyframes workflow](#topic-audio-reactive)
- [Keylight, spill and edge recovery](#topic-keying)
- [Roto Brush and Refine Edge alongside Object Matte](#topic-roto)
- [Point tracking, attach points and drift](#topic-point-tracking)
- [Mocha AE planar tracking](#topic-mocha)
- [Warp Stabilizer and camera motion](#topic-stabilization)
- [Tracked masks vs hand-roto](#topic-mask-tracking)
- [Brush and Clone Stamp in Layer panel](#topic-paint)
- [Content-Aware Fill video cleanup](#topic-content-aware-fill)
- [2.5D layers and spatial depth](#topic-3d-intro)
- [Camera nodes, POI and projection](#topic-cameras)
- [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers)
- [GLTF/GLB/OBJ/FBX and environment lights](#topic-3d-models)
- [3D Camera Tracker and solved scenes](#topic-camera-tracker)
- [Corner Pin and perspective insertion](#topic-perspective)
- [RGB, color profiles and grade order](#topic-color)
- [8/16/32 bpc and floating point](#topic-color-depth)
- [OCIO/ACES 2.0 in a 26.5 project](#topic-ocio)
- [Expression evaluation and safe syntax](#topic-expressions)
- [JavaScript-like expressions, coordinates and values](#topic-expression-language)
- [Sliders, points, angles, colors and dropdowns](#topic-expression-controls)
- [CSV, JSON and AE data inputs](#topic-data)
- [sourceRectAtTime and dynamic card padding](#topic-auto-layout)
- [Essential Properties as instance controls](#topic-essential-properties)
- [Motion Graphics templates and protected timing](#topic-mogrt)
- [Puppet deformation and mesh setup](#topic-puppet)
- [Particles, emitters and simulation](#topic-particles)
- [Other simulation and stylize effects](#topic-simulations)
- [Render Queue decisions and preflight](#topic-export)
- [Containers, codecs, sequences and masters](#topic-codecs)
- [Collect Files and portability](#topic-collect-files)
- [RAM, disk cache and preview rate](#topic-performance)
- [Cache levels, purging and invalidation](#topic-cache)
- [Proxies, pre-renders and fast preview](#topic-proxies)
- [A structured debug decision tree](#topic-diagnostics)
- [Missing plugins, effects and unsupported version](#topic-missing-effects)
- [ExtendScript and project automation](#topic-scripting)
- [Missing media, absolute paths and Windows storage](#topic-file-management)
- [Repeatable production and QC workflow](#topic-workflow)
- [Final self-assessment and future practice](#topic-capstone)
- [What changed through 26.5](#topic-release-26-5)
- [Quick Apply: effects, presets and commands](#topic-quick-apply)
- [Object Matte: select, propagate, refine and cache](#topic-object-matte)
- [26.5 guides: pixels, percent, edge pinning and color](#topic-responsive-guides)
- [Effect labels, masks and reusable presets](#topic-effect-labels)
- [Quick Offset versus Proportional Scrubbing](#topic-proportional-scrubbing)
- [SVG file import and vector clipboard transfer](#topic-svg-workflow)
- [Animate variable-font axes and spacing](#topic-variable-fonts)
- [Native parametric meshes and material appearance](#topic-parametric-meshes)
- [Substance SBSAR and real mesh displacement](#topic-substance-materials)
- [Advanced 3D in-engine depth of field](#topic-advanced-dof)
- [Curl Noise: a flowing texture experiment](#topic-curl-noise)
- [Unmult: convert a black or white backing into alpha](#topic-unmult)
- [Compressor, Gate and Distortion in 26.5](#topic-audio-dynamics)
- [Snapshots, clipboard frames and rendered stills](#topic-clipboard-frame)
- [Native null controllers for points and paths](#topic-native-null-controllers)
- [Composition Profiler, ROI and compressed cache](#topic-profiler)
- [Stable versus Beta: read newer tutorials critically](#topic-beta-watchlist)
- [Copyable expression building blocks](#topic-expression-examples)
- [Modern dropdown labels, key lookup and range mapping](#topic-expression-lookup)
- [Text outlines, Layer Styles and source editability](#topic-outline-styles)
- [360-degree imagery and seam-aware effects](#topic-immersive)
- [Footage source time vs comp time](#topic-source-time)
- [Frame-rate conversion and temporal sampling](#topic-frame-rate)
- [Layer-based compositing and image order](#topic-compositing)

## Deep topic reference

<a id="topic-version-workflow"></a>
### Version discipline: 26.5 stable and a separate Beta

*Foundations* — Use the September 2026 stable release and recognize the boundary of its feature set.

**Identify**

Check Help → About After Effects for 26.5. This guide’s research date is 2026-10-28; it does not assume features from a rolling Beta page ship in stable.

**Modern tools**

26.0–26.3 added native meshes/materials, variable-font axes, SVG workflows, Unmult/audio effects, Quick Apply, Object Matte, Proportional Scrubbing, Curl Noise, clipboard frame capture and Advanced 3D DOF. They are all within this edition’s target.

**26.5 improvements**

Responsive guides, Object Matte disk caching, effect labels/modernized controls and ACES 2.0 configurations are included. Read the dedicated topics for the actual operations and limits.

**Beta boundary**

Contour Paint, De-esser, AI Assistant, layers as 3D material inputs, materials on 3D text/shapes, editable Illustrator-text conversion, Quick Set Anchor and generalized Alt-drag duplication are listed on Adobe’s Beta page. Do not build a stable-only handoff around them.

**Experiment:** Find the installed version, open Quick Apply, then explain why a Beta tutorial may expose different controls.

**Pitfalls:** Stable mesh-specific Alt-drag behavior does not establish general layer duplication support.

**Related topics:** [The Windows After Effects interface](#topic-interface), [What changed through 26.5](#topic-release-26-5), [Stable versus Beta: read newer tutorials critically](#topic-beta-watchlist)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe: What is new through 26.5](https://helpx.adobe.com/after-effects/desktop/what-s-new/whats-new.html), [Adobe: After Effects Beta (separate from stable)](https://helpx.adobe.com/after-effects/desktop/what-s-new/after-effects-beta.html)

<a id="topic-25-6-features"></a>
### Earlier 25.6 features retained in 26.5

*Foundations* — Earlier improvements retained in 26.5; the durable topic ID also preserves existing links.

**Shared 3D gizmo**

Select multiple 3D layers and use a single viewport gizmo to position, rotate and scale multiple selected layers. It reduces visual clutter; it does not replace Parenting or create a persistent Group object.

**Default camera settings**

View menu allows modifying default-camera behavior for appropriate views. Use this to control perspective when no explicit camera is used or when viewing a custom view, but record the change in a training project.

**Interface and fixes**

Tip of the Day appears when an appropriate viewer is empty/reloaded. Timelines can be closed to the left or right, and 25.6 fixes a large group of project, export and stability defects.

**GPU boundary**

Adobe’s 25.x requirements specify that After Effects 25.6 requires OpenCL 2.0 where OpenCL is applicable, removing support for 1.2 or older. Hardware compatibility matters more than incidental new tool names.

**Experiment:** Make a two-layer 3D scene and operate the joint gizmo, then parent both layers to a Null and describe the difference.

**Related topics:** [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow), [2.5D layers and spatial depth](#topic-3d-intro)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe: After Effects 26.x system requirements](https://helpx.adobe.com/after-effects/desktop/get-started/technical-requirements/system-requirements.html)

<a id="topic-interface"></a>
### The Windows After Effects interface

*Foundations* — Know the difference between each panel and where focus lives.

**Project and composition**

The Project panel stores footage, comps and folders. Composition viewer shows a rendered view of one composition at a given time, with guides and on-canvas controls. Double-clicking footage opens the Footage panel; double-clicking a footage layer can open the Layer panel.

**Timeline and Effects**

Timeline hosts layers, track mattes, time spans, properties, expressions, keyframes and graph curves. Effect Controls displays the selected layer’s effect stack; Effects & Presets is a catalog/search area for available effects and animation presets.

**Focused shortcuts**

A key can mean something else in text editing, painting, a 3D view or a render queue. Ctrl+D duplicates the current selected object in the active context. Click the intended panel and verify selection before using a destructive command.

**Recover layouts**

Use the Window → Workspace menu, reset layouts, hover a panel and press backtick to maximize it. F4 reveals alternate Timeline Switches/Modes columns. Use panel tabs and viewer locks to compare related comps.

**Experiment:** Use only keyboard and workspace menus to locate Project, Preview, Character, Render Queue and Composition panels in 60 seconds.

**Pitfalls:** A gray blank panel may be a viewer without an open item, not a failed render.

**Related topics:** [Composition, layer and project hierarchy](#topic-layer-anatomy), [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow)

**Sources:** [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-layer-anatomy"></a>
### Composition, layer and project hierarchy

*Foundations* — Understand nested composition references and editable source instances.

**Files are not embedded automatically**

An .aep project points to sources and stores transformations and project data. Two layers can reference one source item, and two comps can nest the same precomp; changing the nested original impacts both copies unless overridden.

**What lives on a layer**

A layer has In/Out, transform, masks, effects, blending mode, mattes, switches, parenting, keyframes and other type-specific properties. Effects modify generated pixel data; they are not identical to a shape layer’s Contents operators.

**Comp settings affect interpretation**

Composition FPS defines its frame grid; resolution and pixel aspect determine the render canvas. The footage source has its own interpretation, while the comp layer instance has its own transform and time placement.

**Experiment:** Build two comps sharing a precomp, then alter the shared precomp artwork and observe both.

**Pitfalls:** Do not assume deleting a layer will delete its Project footage source.

**Related topics:** [Precomposition and nested timeline logic](#topic-precomp), [Import formats, sequences and linked files](#topic-import-media), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-project-management"></a>
### Folders, naming and backup policy

*Foundations* — Organize projects so someone else can rebuild them.

**On disk vs Project panel**

A Project folder is metadata inside .aep, not necessarily an OS directory. Keep named Windows folders for Assets, Renders, Cache if desired, Archive and Collected. Backups should be saved outside the active working folder where feasible.

**Naming schemes**

Give comps distinctive prefixes (FINAL_, SCENE_, PRE_, CTRL_) and avoid duplicate or confusing names for controllers used in expressions. Label colors aid navigation but must not be the only source of meaning.

**Reproducibility**

Use File → Dependencies → Collect Files for used source material; also list external fonts, plugins, LUTs, environment assets and scripts. Never claim Collect Files packages plugin binaries or licenses.

**Experiment:** Open an .aep from a moved Collect Files directory after severing access to its original Assets path.

**Pitfalls:** Save As is not identical to Increment and Save or Collect Files.

**Related topics:** [Collect Files and portability](#topic-collect-files), [Missing plugins, effects and unsupported version](#topic-missing-effects)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-import-media"></a>
### Import formats, sequences and linked files

*Foundations* — Always inspect time, channels, format and external dependencies.

**Footage vs layer**

Importing creates a footage item in Project. Dragging it into a composition creates a layer instance with its own in point, transform and effects. Deleting an instance does not necessarily delete the source item.

**Sequence and alpha**

Numbered images can become one time-based sequence. Check whether alpha is straight or premultiplied; a premultiplied RGB fringe should not be interpreted as an image with independent straight edge colors.

**Dynamic links and layered PSD/AI**

Where supported, import a layered image as Composition — Retain Layer Sizes to keep logical layers. Inspect the anchor and coordinate placement after the import. Dynamic Link/Photoshop/Illustrator updates need the original source app/assets.

**Experiment:** Import a five-frame PNG sequence and then import one frame as still; explain the difference.

**Pitfalls:** A media path under Downloads can disappear even if .aep continues to exist.

**Related topics:** [Footage frame rate, alpha and pixel aspect](#topic-footage-interpretation), [Missing media, absolute paths and Windows storage](#topic-file-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-footage-interpretation"></a>
### Footage frame rate, alpha and pixel aspect

*Foundations* — Bad interpretation can invalidate an otherwise perfect composite.

**Frame rates**

When footage is interpreted at a different FPS, it may run faster/slower. Time stretch and frame blending are different from reinterpretation. Variable-frame-rate recordings may need transcoding to constant frame rate.

**Alpha types**

Straight/unmatted pixels encode RGB independently of alpha. Premultiplied/matted pixels were already mixed against a matte color; interpreting them incorrectly often creates dark/light halos.

**Pixel aspect and fields**

A non-square pixel interpretation scales geometry, not just final output dimensions. Interlaced fields and separated-fields options matter for legacy broadcast material and can cause combing if interpreted wrong.

**Experiment:** Take an RGBA still, intentionally choose incorrect alpha interpretation, then restore a clean edge.

**Pitfalls:** Changing footage interpretation can affect every use of that footage item.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [FPS, timecode and frame alignment](#topic-frames)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-frames"></a>
### FPS, timecode and frame alignment

*Foundations* — Work in frame counts to avoid off-by-one visual errors.

**Timecode**

In a 24-fps non-drop-frame composition, 00:00:01:12 means 1.5 seconds. Frames within a second run 00 through 23. The display mode can also show frames rather than timecode.

**Layer sampling**

Source footage at 30 fps inside a 24-fps comp is sampled at the comp frame grid, potentially repeating/dropping frames or using blending. Audio is time-based and should be inspected independently of visual frame matching.

**Useful arithmetic**

Duration seconds = frames / fps. 72 frames at 24 fps = 3 seconds; 100 frames at 25 fps = 4 seconds. Use the guide’s frame calculator to explore rates and offsets.

**Experiment:** Make a four-second comp at 25 fps and label frames 0, 24, 25 and 99. Frame 100 is the exclusive duration boundary, not a visible frame inside that comp.

**Pitfalls:** Drop-frame timecode applies to appropriate broadcast rates; do not use its punctuation as a universal frame-count formula.

**Related topics:** [Layer bounds, work areas and markers](#topic-timeline), [Footage source time vs comp time](#topic-source-time)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-timeline"></a>
### Layer bounds, work areas and markers

*Foundations* — A timeline is several overlapping time systems.

**Three positions**

The composition playhead indicates comp time; the layer’s bar shows In/Out times in that comp; footage source time indicates which source frame is used. A precomp also has its own inner timeline.

**Move versus trim**

[ and ] reposition entire selected layers to CTI using their In/Out references; Alt+[ and Alt+] trim at CTI. Ctrl+Shift+D splits. These are not equivalent to moving animation keyframes only.

**Markers and work area**

B/N set work area ends for local preview/render planning. Main keyboard digits may navigate numbered comp markers, while numpad keys can select layers or start a preview depending on focus.

**Experiment:** Use one video clip to demonstrate a shift, a trim, a split and a work-area change, and label each in a separate comp.

**Pitfalls:** Changing the work area does not necessarily change comp duration.

**Related topics:** [Footage source time vs comp time](#topic-source-time), [FPS, timecode and frame alignment](#topic-frames)

**Sources:** [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-coordinates"></a>
### Coordinates, anchor points and transforms

*Foundations* — Be precise about which point and which coordinate system each value uses.

**Anchor versus position**

Anchor is in the layer’s own coordinate system; Position specifies the anchor in parent/comp coordinates. Moving an anchor can appear to shift the image unless AE compensates its Position when using Pan Behind.

**Transform nesting**

A shape group has its own Transform inside Contents, plus the layer Transform. A child layer uses parent-space Position; a 3D layer can have X/Y/Z and Orientation as well as Rotation values.

**Converting positions**

Expressions provide toComp(), fromComp(), toWorld(), fromWorld() and related methods for correct cross-coordinate conversion. A direct Position link is only straightforward when both properties share the same coordinate context.

**Experiment:** Find the same corner of a shape before/after parenting and explain why its displayed Position values differ.

**Pitfalls:** A shape rectangle size is not the same property as layer Scale.

**Related topics:** [Parenting, nulls and reusable rigs](#topic-parenting), [Expression evaluation and safe syntax](#topic-expressions)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-parenting"></a>
### Parenting, nulls and reusable rigs

*Foundations* — Use simple controllers to coordinate several layers safely.

**Parent-child relationships**

A child inherits transforms from its parent but retains independent local animation. Parent to a Null for a clean control layer rather than applying identical Position keyframes to every object.

**Controllers**

Use descriptive names and Expression Controls for user-facing parameters. Parent a child only once in a hierarchy; avoid creating circular dependencies through expressions.

**Rig safety**

Duplicate a rig and check whether expressions reference the duplicated or original controls. Essential Properties are often more suitable for controlled per-instance variation than unstructured cross-comp expressions.

**Experiment:** Build a three-layer clock where the root null travels while a hand rotates independently.

**Pitfalls:** Parenting a 3D child to a 2D null can have unexpected coordinate behavior; test and document.

**Related topics:** [Coordinates, anchor points and transforms](#topic-coordinates), [Essential Properties as instance controls](#topic-essential-properties)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-keyframes"></a>
### Keyframes and interpolation

*Animation* — A keyframe stores a property value at a specific time.

**Recording properties**

Enable the stopwatch when you mean to animate. At a new time, editing the value creates an additional key. Changing a static value before enabling a stopwatch does not record a time history.

**Interpolation**

Linear changes at uniform numeric rate, Hold jumps, Bézier allows easing. Rotation angle and 2D Position follow different units, so similar graphs can still produce different perceived motion.

**Keyframe housekeeping**

U reveals keyed properties, J/K navigate visible time events, and Ctrl+Shift+K opens velocity controls. Ctrl-click in a keyframe view is contextual; learn the specific mode before editing.

**Experiment:** Make the same 0-to-100 opacity transition with Linear, Hold and Easy Ease.

**Pitfalls:** Clicking the active stopwatch deletes all animation for that property.

**Related topics:** [Value Graph, Speed Graph and easing](#topic-graph-editor), [Timing and design principles for readable motion](#topic-motion-design)

**Sources:** [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-graph-editor"></a>
### Value Graph, Speed Graph and easing

*Animation* — Control velocity and rhythm separately from endpoint positions.

**Speed vs value**

A Value Graph plots the property value over time. A Speed Graph plots the rate of change. A flat speed graph can correspond to a sloped linear position value graph.

**Influence and handles**

Temporal Bézier handles control easing at keys. At a given duration, sharper influence usually shifts which portions of the journey happen quickly versus slowly. The path can remain straight.

**Spatial keys**

Position motion paths have separate spatial Bézier interpolation; a curved trajectory does not guarantee ease. Rove Across Time can redistribute intermediate spatial keys but not arbitrary hold or non-spatial properties.

**Experiment:** Animate three identical dots to the same endpoint with different arrival timing and explain the change in speed graph.

**Pitfalls:** Do not make a curved spatial path when you only need easing.

**Related topics:** [Keyframes and interpolation](#topic-keyframes), [Timing and design principles for readable motion](#topic-motion-design)

**Sources:** [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-motion-design"></a>
### Timing and design principles for readable motion

*Animation* — Make movement communicate hierarchy, not merely demonstrate tools.

**Pose and hold**

Allow time for reading after a title enters. Motion that never stops is often harder to follow; a clean hold creates hierarchy and reduces attention fatigue.

**Overlap and anticipation**

Offset related layer animation by a few frames using measured timing, not arbitrary random delays. For a 24-fps comp, 6 frames = 0.25 seconds; choose offsets based on readability.

**Consistent motion language**

Keep easing, direction, acceleration and stagger rules reusable across a project. Test at full playback speed and also frame by frame for collisions.

**Experiment:** Build a 3-card entrance with 5-frame staggers and consistent ease-out shapes.

**Pitfalls:** Excess overshoot can look like accidental jitter rather than controlled energy.

**Related topics:** [Value Graph, Speed Graph and easing](#topic-graph-editor), [Parametric shapes vs Bézier paths](#topic-shapes)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-shapes"></a>
### Parametric shapes vs Bézier paths

*Animation* — Use the least complicated editable geometry for each job.

**Shape structure**

Shape Layer → Contents contains groups. Each group may contain path, fill, stroke, group transform and operators; the layer has its own Transform independently.

**Keep parameters live**

Rectangle Path Size and Roundness allow reusable UI-like cards. Polystar Path lets you animate point count and radii. Converting to Bézier gives vertex freedom but sacrifices simple parametric controls.

**Operators**

Trim Paths draws strokes; Repeater duplicates source shapes; Offset Paths grows/shrinks outlines; Pucker & Bloat distorts forms. They operate in Contents, not standard effects stack.

**Experiment:** Construct a shape-based progress ring, then change its size without redrawing vertices.

**Pitfalls:** A filled closed path revealed with Trim Paths may not behave like a stroked outline.

**Related topics:** [Masks, shape paths and motion paths](#topic-paths), [Shape strokes, Trim Paths and Write-on](#topic-strokes)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-paths"></a>
### Masks, shape paths and motion paths

*Animation* — Three different kinds of path can look visually similar.

**Mask path**

A mask path defines visible pixels and has Mode, Feather, Opacity and Expansion. Mask Path keyframes animate that outline, not the layer Position itself.

**Shape path**

A Shape Path defines fill/stroke geometry and can be a live parametric outline or a vertex-editable Bézier curve. It can be copied between compatible path properties in many situations.

**Motion path**

A Position property with spatial animation creates a trajectory whose dots represent temporal samples. Its vertices and handles change spatial travel, while keyframes/Graph Editor define timing.

**Experiment:** Make one letter follow a mask path while a separate shape traces a closed path via Trim Paths.

**Pitfalls:** Do not assume two visually similar paths have interchangeable parameter types.

**Related topics:** [Mask modes and feathering](#topic-masks), [Value Graph, Speed Graph and easing](#topic-graph-editor)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-strokes"></a>
### Shape strokes, Trim Paths and Write-on

*Animation* — Choose between drawing geometry and painting pixels.

**Stroke types**

Shape Stroke is vector line styling inside a Shape Layer. The Stroke effect can reveal a mask path on footage or a solid. Write-on uses paint-like accumulation and has its own timing controls.

**Dashed paths**

A shape stroke can have dashes, caps, joins and taper depending on the shape controls. Trim Paths Start/End define the visible portion of a path, while Offset rotates this visible window.

**Compositing**

To make a tracked outline, first track/animate the path, then generate a stroke, then optionally add Glow. Use a solid or precomp so the stroke has enough output dimensions when necessary.

**Experiment:** Draw a six-stroke icon and animate strokes in a deliberate order.

**Pitfalls:** Do not use a high-feather mask in place of a designed stroke.

**Related topics:** [Parametric shapes vs Bézier paths](#topic-shapes), [Brush and Clone Stamp in Layer panel](#topic-paint)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-masks"></a>
### Mask modes and feathering

*Compositing* — Masks edit layer transparency while preserving source pixels.

**Mode logic**

Add reveals, Subtract removes, Intersect retains shared area. Inverted changes interpretation. With multiple masks, compositing behavior depends on mode, ordering and the layer’s alpha.

**Edge controls**

Feather produces a soft transition, Expansion dilates/erodes region borders and Mask Opacity scales contribution. Variable/per-vertex feathering can handle nonuniform boundaries.

**Animated masks**

With a selected mask path stopwatch, edit vertices over time. Fewer stable vertices generally track better than dozens of imprecise ones.

**Experiment:** Draw two masks: one additive and one subtractive, then isolate the overlap.

**Pitfalls:** If masks are invisible, check View → Show Layer Controls; it does not change pixels.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Tracked masks vs hand-roto](#topic-mask-tracking)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-alpha"></a>
### Alpha, straight RGB and premultiplication

*Compositing* — Transparency is separate from visible RGB even when pixels look black.

**Representation**

An RGBA pixel stores red, green, blue and alpha. Alpha=0 need not force RGB=0 in all representations. In straight alpha, RGB is often intended unmultiplied; premultiplied RGB already contains transparency/color matte interaction.

**Artifacts**

Dark outlines on translucent edges commonly result from misinterpreted alpha or resampling a matte-color-contaminated source. Inspect straight RGB and alpha separately before adding choker/blur.

**Delivery**

A codec/container must carry an alpha plane, and the output module must export RGB+Alpha correctly. Many MP4 H.264 workflows do not carry ordinary RGBA transparency.

**Experiment:** Create a white semi-transparent circle over black, export and test its edge over magenta.

**Pitfalls:** Using Screen blending for black-backed particles is not identical to producing alpha for downstream editors.

**Related topics:** [Alpha/luma track mattes](#topic-mattes), [Render Queue decisions and preflight](#topic-export), [Footage frame rate, alpha and pixel aspect](#topic-footage-interpretation)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-mattes"></a>
### Alpha/luma track mattes

*Compositing* — An independent matte layer controls another layer’s visibility.

**Alpha matte**

Visible matte alpha determines the target’s coverage. A red opaque matte and blue opaque matte cover equally if both have full alpha.

**Luma matte**

Luminance of a matte determines visibility. Black gives none and white gives full coverage; mid-gray gives partial coverage. Color gradients can behave unlike alpha-only gradients.

**Flexible setup**

Modern track mattes let the target reference an appropriate other layer in the comp. One matte may be reused in more than one place; keep the source named and be aware of comp boundaries.

**Experiment:** Use a checkerboard, a full-alpha red rectangle and a grayscale gradient to compare alpha and luma mattes.

**Pitfalls:** A mask on the footage and a matte sourced from a different layer are not identical workflows.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Layer blend modes and compositing](#topic-blending)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-blending"></a>
### Layer blend modes and compositing

*Compositing* — Blend math changes RGB interaction with layers beneath.

**Ordinary compositing**

Normal combines pixels by alpha. Multiply darkens based on RGB product; Screen generally lightens; Add sums channels and can clip or exceed normal ranges in high-bit-depth projects.

**Order matters**

A blend mode acts on a layer relative to what has been composited below it. Reordering layers often changes the look, even when no keyframes change.

**Alpha does not follow automatically**

Screening a black-background explosion may visually hide black but does not magically reconstruct fully useful alpha. Check the deliverable’s requirements.

**Experiment:** Composite a bright flare onto black footage with Screen, then try a true RGBA flare and compare downstream alpha.

**Pitfalls:** Blend modes can behave differently under linear-light color management.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-render-order"></a>
### Effect and transform evaluation order

*Compositing* — The order of pixel processing explains why precomps can change results.

**Processing chain**

A simplified layer flow considers source, masks and effects, transformations, layer styles and compositing. Actual order can vary with layer type, 3D renderer and continuously rasterized/precomp settings.

**Precompose effects**

Moving effects inside versus leaving them outside a precomp can shift which pixels are processed at what scale/geometry. Use two simple controls to prove the cause.

**Adjustments and nested comps**

An adjustment layer affects pixels composited beneath it inside its active group/context. Nesting can change what image it receives and where it is calculated.

**Experiment:** Apply a 20-pixel blur to a 100×100 square, scale 500%, then swap where blur and scale occur.

**Pitfalls:** Collapse Transformations can change rendering; it should not be turned on reflexively.

**Related topics:** [Precomposition and nested timeline logic](#topic-precomp), [The effect stack and control surfaces](#topic-effect-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-precomp"></a>
### Precomposition and nested timeline logic

*Compositing* — A precomp is a composition used as a layer in another comp.

**Two contexts**

Inner composition time, resolution, frame rate, layer transforms and effects can all differ from the outer master comp. Time Remapping on outer precomp changes sampled inner time.

**Move attributes choice**

When precomposing, whether attributes move into the new comp changes how/where an effect is evaluated. Test with one blur and one transform rather than memorizing the dialog without context.

**Maintainable nesting**

Keep comp hierarchies shallow enough to inspect. Prefix names, write purposeful notes and avoid accidentally creating expression dependencies across unstable names.

**Experiment:** Build a comp of an animated icon, use it twice, and override only one instance’s timing.

**Pitfalls:** Do not assume outer frames and inner frames line up without checking frame-rate and start-time behavior.

**Related topics:** [Effect and transform evaluation order](#topic-render-order), [Essential Properties as instance controls](#topic-essential-properties)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-effect-order"></a>
### The effect stack and control surfaces

*Effects* — Each effect consumes the prior rendered result in its layer context.

**Processing order**

Fractal Noise → Levels → Glow does not necessarily match Fractal Noise → Glow → Levels. The first can threshold which regions glow; the second can recolor/clamp the already glowing output.

**Effect Controls**

Use F3 to inspect, rename and reorder effect instances. The fx switch bypasses individual effects and the layer fx switch bypasses effects as a set; deleting all effects is destructive.

**Scope**

A blur on a source layer differs from a blur on a precomp or an adjustment layer. Effect operating bounds, alpha and precomp render order can change the visible result.

**Experiment:** Reverse two effects on a duplicate layer and explain the changed pixels.

**Pitfalls:** Do not treat a property expression as an image effect.

**Related topics:** [Effects, presets and compatibility](#topic-effects), [Adjustment layers and global looks](#topic-adjustment-effects)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-effects"></a>
### Effects, presets and compatibility

*Effects* — Read the difference between native effects, bundled plugins and third-party plugins.

**Find capabilities**

Effects & Presets lists installed effects and presets. Different AE releases can add/remove or deprecate items. The Adobe Effect List reports GPU, Multi-Frame Rendering and bpc support for many named effects, but is a rolling document.

**Predesigned animation**

Presets may create multiple effects, text animators or keyframes. Apply them to a disposable layer and inspect what changed before using them on a production layer.

**Manage failures**

If an effect is missing, investigate Effect Manager, plugin licensing, paths, bit depth and OS support. A disabled or obsolete effect can still appear on old layers.

**Experiment:** Apply one animation preset to a temporary text layer, inspect every parameter it added, then rebuild its visual behavior manually.

**Pitfalls:** An effect may render on CPU even in a GPU-capable composition.

**Related topics:** [The effect stack and control surfaces](#topic-effect-order), [Missing plugins, effects and unsupported version](#topic-missing-effects)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-adjustment-effects"></a>
### Adjustment layers and global looks

*Effects* — Place finishing looks intentionally in a layer stack.

**What they sample**

Adjustment layers take the composite below within their scope and process it through effects. Use them to keep repeated color/grain/blur calculations under control.

**Limiting scope**

Trim adjustment In/Out, use masks or mattes, or nest intended layers into a precomp so only that result receives the change.

**Adjustment vs solid**

A solid with an effect is still an ordinary image source unless effect/composite settings cause it to act differently. An adjustment layer is a special processing layer.

**Experiment:** Apply Curves to only one card via an adjustment layer mask and compare to a directly applied effect.

**Pitfalls:** If the adjustment layer is at the bottom of the comp, it cannot affect layers above it as expected.

**Related topics:** [Layer blend modes and compositing](#topic-blending), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-blur"></a>
### Gaussian, lens and map-driven blur

*Effects* — Pick a blur that expresses the actual desired motion/depth.

**Ordinary blur**

Gaussian Blur is predictable and often economical. Directional Blur resembles linear streaking; Radial Blur simulates radial spin/zoom; Unsharp Mask enhances edges rather than smoothing.

**Lens look**

Camera Lens Blur can shape bokeh highlights and blur-map-dependent focus. It may be more expensive than a Gaussian blur; test representative shots and settings.

**Blur a matte vs blur an image**

Softening a mask/matte edge preserves subject detail differently from blurring the subject RGB itself. Use the channel viewer to see what data changed.

**Experiment:** Create an alpha matte with a 20-pixel soft edge, compare against a 20-pixel Gaussian blur on the actual footage.

**Pitfalls:** Overblurred matte edges can produce transparent halos with colored source pixels.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Displacement, depth and faux 3D](#topic-depth-maps)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-procedural"></a>
### Fractal/Turbulent Noise and displacement

*Effects* — Generate repeatable organic texture and use it as a controlled signal.

**Noise generator**

Fractal Noise exposes a procedural field. Contrast, Brightness, Scale, Complexity and Evolution/Offset Turbulence change pattern appearance and motion.

**Signal map**

Convert noise to useful grayscale and plug into Displacement Map, Compound Blur or matte controls. The map does not need to look beautiful as a layer; its luminance/channel relationship is the important factor.

**Animation loops**

Looping Evolution might not produce a seamless visual loop unless cycling and offset settings are chosen correctly. Check first and last frame against each other.

**Experiment:** Make 3 kinds of noise with identical Evolution speed but different Scale and use each as a Displacement Map.

**Pitfalls:** Curl Noise, introduced in 26.3, is available in 26.5; its flow controls differ from Fractal Noise.

**Related topics:** [Displacement, depth and faux 3D](#topic-depth-maps), [Effects, presets and compatibility](#topic-effects)

**Sources:** [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-depth-maps"></a>
### Displacement, depth and faux 3D

*Effects* — Depth maps encode local differences but do not automatically turn an image into geometry.

**Grayscale meaning**

A depth map typically uses light/dark values to represent a chosen near/far ordering. It is only meaningful when an effect interprets those values with a known range and channel.

**2D parallax**

Use separately cut foreground/background layers, Z positions and a moving camera for actual AE 2.5D parallax. A displacement map instead repositions pixels inside a layer.

**Map quality**

Soft gradients can create smooth wipes or depth-based blur. Abrupt low-resolution boundaries cause distortion and halos; feather the map before it is sampled.

**Experiment:** Create a grayscale radial gradient and use it as a blur map, then as a displacement map; compare interpretations.

**Pitfalls:** Camera Lens Blur on a map is not Advanced 3D camera depth of field.

**Related topics:** [Fractal/Turbulent Noise and displacement](#topic-procedural), [Camera nodes, POI and projection](#topic-cameras)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-time-remap"></a>
### Time remapping, reversal and loops

*Animation* — Resampling a source in time is different from moving keys along a comp timeline.

**Source-clock changes**

Time Remap keys map comp time to source time. A hold segment samples one source frame repeatedly; a descending segment can reverse the footage.

**Layer vs keyframe reversal**

Time-Reverse Layer reverses the layer source playback; Time-Reverse Keyframes reverses timing of selected animation keys. Use deliberately named test duplicates.

**Loop frames**

Keep the full N-frame source duration. Use an initial (0,0) remap key, a last-valid-frame key at ((N-1)*d,(N-1)*d) with outgoing Hold, and a cycle-boundary key at (N*d,0). loopOut('cycle') then repeats that full interval; simply deleting the duration endpoint can shorten the cycle. Check source/comp rates and trim offsets.

**Experiment:** Render a 2-second clip as forward, reverse, freeze and looping examples.

**Pitfalls:** Video source frames may be interpolated differently depending on frame blending settings.

**Related topics:** [FPS, timecode and frame alignment](#topic-frames), [Native motion blur and shutter settings](#topic-motion-blur)

**Sources:** [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-motion-blur"></a>
### Native motion blur and shutter settings

*Animation* — Motion blur communicates movement between discrete frames.

**Two switches**

Layer Motion Blur switch must be enabled, and the comp master Motion Blur must also be on. Some source/effect types require separate blur solutions.

**Shutter angle**

Larger shutter angle generally creates longer smears relative to frame interval. Shutter phase changes the sampling timing relative to the frame center.

**Evaluate carefully**

Check blur at final frame rate and Full-quality rendering, not only in a low-resolution interactive preview. Camera/3D motion may need renderer-compatible blur.

**Experiment:** Render the same fast-moving square with motion blur off, modest shutter, and long shutter.

**Pitfalls:** Motion blur cannot repair extremely poor source motion tracking.

**Related topics:** [Time remapping, reversal and loops](#topic-time-remap), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-text"></a>
### Point/box text, metrics and typography

*Text & data* — Readable type depends on spacing and consistent layout.

**Text modes**

Point text grows as you type; paragraph text wraps inside a bounding box. Baseline shift, leading, kerning, tracking and paragraph alignment are distinct tools.

**Design rules**

Build with type hierarchy, padding and safe areas. Validate font availability, substitution behavior and variable dimensions of different language strings.

**Editable workflows**

Preserve editable text for templates and handoff. Only convert text to shapes when vertex-specific path animation or flattening is truly required; a shape conversion is no longer a normal editable text string.

**Experiment:** Fit three differently sized names into one title-card layout without manual per-name repositioning.

**Pitfalls:** Style controls and font metrics can change between installed font versions.

**Related topics:** [Text animators and selectors](#topic-text-animator), [sourceRectAtTime and dynamic card padding](#topic-auto-layout)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-text-animator"></a>
### Text animators and selectors

*Text & data* — Text animation has selectors inside the text layer hierarchy.

**Animator vs source**

Source Text defines content. Text → Animate adds a group of animated properties that apply to selected characters, words or lines. The layer Transform moves all characters together.

**Range selector**

Start, End, Offset and Advanced selectors determine which text is affected. Shape, Smoothness and Based On modes can create scans, typewriter-like reveals or per-word emphasis.

**Expression selector**

A custom selector can provide per-character weight values. Use it only when Range or Wiggly Selector cannot express the motion and maintain it carefully.

**Experiment:** Animate each word in a heading by changing only Based On and a range selector’s Offset.

**Pitfalls:** Variable Font Axes are available in 26.5; use a genuinely variable font and check its supported axes.

**Related topics:** [Point/box text, metrics and typography](#topic-text), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls)

**Sources:** [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-type-design"></a>
### Kinetic typography and text clarity

*Text & data* — Text animation is meaningful only when it stays legible.

**Sequence hierarchy**

Decide which line is primary and which is secondary. Do not animate every word with equal force; use emphasis selectively.

**Spacing and contrast**

Monitor text at target playback size, on a phone-sized viewer when applicable. Check antialiasing, safe zones and contrast on busy plates.

**Time constraints**

Estimate reading time and keep titles visible long enough to understand. Faster keyframes do not automatically make a better design.

**Experiment:** Make an 8-second quote with 2-second line holds, one emphasized word per line, and a consistent baseline.

**Pitfalls:** Scale bounces can produce text shimmer at small final sizes.

**Related topics:** [Point/box text, metrics and typography](#topic-text), [Timing and design principles for readable motion](#topic-motion-design)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-audio"></a>
### Audio preview, sync and output

*Audio* — Work with sound deliberately even when AE is not the main editing app.

**Layers and waveforms**

L reveals levels; LL reveals waveform. Preview shortcuts differ by normal keyboard and numeric keypad. Set markers to real audible onsets instead of guessing from peaks.

**Sync**

Layer shifting, Time Stretch and frame-rate interpretation can all affect where sound aligns with motion. Video footage with variable frame rate can create sync trouble and may need preprocessing.

**Final QC**

Enable audio in the export path and listen to the rendered file. Verify beginning/end fades, clipping and the intended channel mix, not just a loud waveform in Timeline.

**Experiment:** Synchronize three shape pops to audible beats and export with checked audio sync.

**Pitfalls:** After Effects audio tools do not replace a full multitrack audio editing/mixing environment.

**Related topics:** [Convert Audio to Keyframes workflow](#topic-audio-reactive), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-audio-reactive"></a>
### Convert Audio to Keyframes workflow

*Audio* — Use an audio amplitude slider to drive numeric properties.

**Generate amplitude**

Use Animation → Keyframe Assistant → Convert Audio to Keyframes. The generated Null holds Left, Right and Both Channels Slider keyframes.

**Map scale**

On Scale, reference Both Channels with an expression and map/clamp it into an appropriate scale range. Use `[s,s]` for 2D scale output, not a bare number.

**Noise control**

Raw amplitude changes rapidly; smooth it or drive sparse pulses to avoid uncomfortable shaking. Add an envelope/falloff rather than directly following every sample.

**Experiment:** Make a circle pulse between 100% and 135% based on a short drum loop.

**Pitfalls:** Volume level curves do not identify rhythm genre or musical beat positions automatically.

**Related topics:** [Audio preview, sync and output](#topic-audio), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-keying"></a>
### Keylight, spill and edge recovery

*Compositing* — Clean keying has separate stages with distinct failure modes.

**Source stage**

Even lighting and sufficient chroma separation reduce the work of keying. Add a garbage matte so the keyer only processes the relevant area.

**Alpha stage**

Keylight Screen Matte lets you inspect and refine the core silhouette. Avoid clipping all hair detail for a perfectly black background.

**Edge stage**

Key Cleaner, Advanced Spill Suppressor, subtle edge color correction and selective blur improve integration. Test against multiple backgrounds and moving frames.

**Experiment:** Key a person over a dark and a light background, then adjust edges until both look acceptable.

**Pitfalls:** Green spill suppression is a color correction problem, not only alpha thresholding.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Mask modes and feathering](#topic-masks)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-roto"></a>
### Roto Brush and Refine Edge alongside Object Matte

*Compositing* — Choose brush-guided propagation when it gives better control than object selection.

**Layer viewer**

Roto Brush strokes are made on a layer in the Layer panel, not drawn as a Composition viewer shape. The initial base frame guides propagation across nearby frames.

**Propagation and correction**

Inspect forward/backward spans, repair slips and use Refine Edge for wispy hair. Freeze after corrections and render check the entire selection range.

**Tool choice**

For a rigid object, a tracked mask or Mocha planar mask may be more efficient than broad Roto Brush propagation. Choose based on edge topology and motion.

**Experiment:** Roto a walking person for two seconds without any abrupt matte popping.

**Pitfalls:** Object Matte is available; choose its toolbar tool for object selection, and use brush/refine tools for corrections.

**Related topics:** [Tracked masks vs hand-roto](#topic-mask-tracking), [Brush and Clone Stamp in Layer panel](#topic-paint)

**Sources:** [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-point-tracking"></a>
### Point tracking, attach points and drift

*Tracking & 3D* — Understand what one or two tracked features can and cannot tell you.

**Feature region**

Contains visual detail the tracker matches across frames. Search region defines where it is allowed to search. Attach Point is the actual point used to transfer the solved motion.

**Motion types**

One point provides translation, two points can model more of rotation and scale. Perspective corner changes require an appropriate perspective/planar tracking workflow.

**Review**

Watch each tracked frame for drift. Reducing motion blur, tracking in segments or choosing a more stable high-contrast target can improve results.

**Experiment:** Attach a 30×30 crosshair to a moving shirt button and keep it aligned for 60 frames.

**Pitfalls:** A search region that is too small will lose a fast-moving feature.

**Related topics:** [Mocha AE planar tracking](#topic-mocha), [Warp Stabilizer and camera motion](#topic-stabilization)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-mocha"></a>
### Mocha AE planar tracking

*Tracking & 3D* — Planar trackers follow a textured surface rather than one point.

**Planar region**

Define a useful plane, follow stable texture and manage occlusion. Mocha surface corners are not the same thing as the drawn tracking spline.

**Export/copy**

Use the bundled Mocha AE integration’s supported transfer path to Corner Pin or transform data. Check exact plugin UI for the installed Mocha build.

**Limits**

A bent cloth or independently moving object is not one stable plane. Break up the track or choose Roto Brush/manual work rather than forcing a single planar solve.

**Experiment:** Track a poster on a wall and apply a four-corner grid in AE.

**Pitfalls:** Warp Stabilizer, 3D Camera Tracker and Mocha each solve different geometric problems.

**Related topics:** [Point tracking, attach points and drift](#topic-point-tracking), [Corner Pin and perspective insertion](#topic-perspective)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-stabilization"></a>
### Warp Stabilizer and camera motion

*Tracking & 3D* — Smooth shaky footage without destroying the composition.

**What it analyzes**

Warp Stabilizer attempts to estimate unwanted motion and compensate it. Method and Smoothness control how aggressive that compensation is.

**Border strategy**

Stabilization often needs crop, scale or synthesized edge pixels; excessive smoothness can distort straight lines. Choose the least invasive method that solves the visible problem.

**Competing tasks**

A shot may first need a camera/point track before stabilization, or the shot may be stabilized only for a masking pass. Preserve an unchanged source for audit.

**Experiment:** Stabilize a ten-second handheld pan and check vertical edges for rubbery warping.

**Pitfalls:** Do not assume every pan is unwanted motion.

**Related topics:** [Point tracking, attach points and drift](#topic-point-tracking), [2.5D layers and spatial depth](#topic-3d-intro)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-mask-tracking"></a>
### Tracked masks vs hand-roto

*Tracking & 3D* — Automating vertices is useful only with deliberate quality review.

**Best candidates**

Select a mask on trackable footage/precomp, then use Animation → Track Mask or Mask Path analyze buttons directly in Timeline. Choose the motion method and analyze forward/backward. Solids, shapes, text and adjustment layers do not supply trackable footage; use roto for deforming hair.

**Key cleanup**

Adjust path vertices only where visibly necessary, avoid unnecessary topology changes, and feather in a stable way over time.

**Fallback**

Point/planar trackers can drive a mask transform while a few manual keys adjust localized shape changes.

**Experiment:** Track a moving oval badge for three seconds and correct at least one deliberately induced drift.

**Pitfalls:** Mask tracking does not infer hidden objects behind an occlusion perfectly.

**Related topics:** [Mask modes and feathering](#topic-masks), [Roto Brush and Refine Edge alongside Object Matte](#topic-roto)

**Sources:** [Adobe: Mask Tracking](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-mask/rigid-mask-tracking.html)

<a id="topic-paint"></a>
### Brush and Clone Stamp in Layer panel

*Compositing* — Painting has source-time and stroke-duration behavior.

**Context**

Select a suitable painting tool and work in Layer viewer. Source paint layers and Brush/Clone behavior depend on the Layer panel, Paint and Brushes controls.

**Temporal strokes**

Paint On Transparent and stroke Duration choices determine when and where marks appear. A fixed still frame repair may not remain aligned in later frames.

**Clone source**

Alt+click chooses a clone sampling source. Use small patches, animate/track where necessary and evaluate temporal texture consistency.

**Experiment:** Clone out a one-frame blemish, then expand the correction to ten frames with correct alignment.

**Pitfalls:** Painting directly on a composited final view is not identical to editing a footage source.

**Related topics:** [Content-Aware Fill video cleanup](#topic-content-aware-fill), [Alpha, straight RGB and premultiplication](#topic-alpha)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-content-aware-fill"></a>
### Content-Aware Fill video cleanup

*Compositing* — Generate candidate replacement pixels after identifying the actual missing region.

**Define hole**

Use a tracked/animated mask to specify the region that needs replacement; ensure the correct alpha relationship before opening the Content-Aware Fill panel.

**Method and reference**

Choose the fill method suitable for the motion/texture. Reference Frames can give a clean example when automatic reconstruction struggles.

**Inspect variation**

Review every frame, watching warping, repetition and unwanted edge seams. A tracked clean plate or a more modest crop may be a better answer.

**Experiment:** Remove a small object and render a frame-by-frame contact sheet to catch flicker.

**Pitfalls:** A good single still frame does not validate a fill over time.

**Related topics:** [Brush and Clone Stamp in Layer panel](#topic-paint), [Tracked masks vs hand-roto](#topic-mask-tracking)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-3d-intro"></a>
### 2.5D layers and spatial depth

*Tracking & 3D* — Position flat layers in 3D space to create depth cues.

**Z depth**

2D layers occupy the comp plane; 3D layers add Z depth, orientation and material interactions. Move layers by different amounts in Z and view from a moving camera to create parallax.

**Separate planes**

A flattened photograph with all scene depth painted into one raster image cannot magically reveal hidden background behind foreground objects. Cut layers or create suitable gaps and patches.

**Lighting and renderers**

A 3D layer may accept lights/shadows depending on the renderer and its material settings. Use simple flat colors to diagnose shadows before importing textured assets.

**Experiment:** Build a three-plane parallax shot and check visibility of edges at both camera extremes.

**Pitfalls:** 3D enabled layers are not automatically volumetric objects.

**Related topics:** [Camera nodes, POI and projection](#topic-cameras), [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-cameras"></a>
### Camera nodes, POI and projection

*Tracking & 3D* — Move a camera with intention and inspect results in multiple views.

**One- and two-node cameras**

A one-node camera can be easier to orient directly. A two-node camera also has a Point of Interest; changing Position without considering POI can produce unexpected aiming changes.

**Zoom and depth**

Camera Zoom and focal length influence framing/perspective, while changing Z distances alters parallax. Do not confuse moving a flat layer closer with scaling it in 2D.

**Orbit rig**

Parent a camera to a Null positioned near the desired pivot for repeatable orbital movement. When editing camera POI, verify how parent transforms interact.

**Experiment:** Build one dolly and one orbit move and label which parameters changed.

**Pitfalls:** Default Camera is a special view concept, distinct from an explicit camera layer.

**Related topics:** [2.5D layers and spatial depth](#topic-3d-intro), [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-3d-renderers"></a>
### Classic 3D, Advanced 3D and Cinema 4D

*Tracking & 3D* — Renderer choice defines the 3D features that actually calculate.

**Capabilities differ**

Advanced 3D supports imported models and advanced shading/material interactions, whereas Classic 3D and Cinema 4D renderer contexts serve different layer/geometry feature combinations.

**Performance modes**

Draft 3D and viewer preview modes trade interactivity for fidelity. Final frames need a deliberate check under the intended renderer and quality settings.

**Current capabilities**

26.5 includes native parametric meshes, Substance materials and in-engine depth of field. Test effect, shadow and transparency behavior in the chosen renderer before committing a project.

**Experiment:** Put a native 3D layer in a simple comp and compare which renderer controls are enabled in each mode.

**Pitfalls:** Render-time behavior can differ significantly from the viewport fast-preview display.

**Related topics:** [GLTF/GLB/OBJ/FBX and environment lights](#topic-3d-models), [Camera nodes, POI and projection](#topic-cameras)

**Sources:** [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-3d-models"></a>
### GLTF/GLB/OBJ/FBX and environment lights

*Tracking & 3D* — Use imported assets with predictable materials and scale.

**Model import**

24.x introduced model import and Advanced 3D. 25.2 expanded FBX support and animated environment lights. Check exact supported features and texture naming on the files you actually import.

**Geometry vs layer**

A 3D model layer is a scene object; ordinary 2D effects are not equivalent to editing its mesh/material internals. Use 3D-specific controls and renderer options.

**Materials and lighting**

Use an HDR environment where appropriate, control exposure and orientation, and test shadow reception/casting. A model with missing UV textures may appear uniformly shaded or magenta/default.

**Experiment:** Import a simple neutral cube/GLB, light it, and record size, rotation and texture dependencies.

**Pitfalls:** Substance SBSAR materials work with models and parametric meshes; layers as material sources and materials on text/shapes remain on the Beta watchlist.

**Related topics:** [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers), [RGB, color profiles and grade order](#topic-color)

**Sources:** [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-camera-tracker"></a>
### 3D Camera Tracker and solved scenes

*Tracking & 3D* — Recover a camera path only when footage contains enough useful 3D information.

**Analysis quality**

Good parallax and stable texture help the solve. Rotational-only motion, zoom, rolling shutter and motion blur may weaken results.

**Ground plane**

Choose tracked points that define a meaningful plane. Use a target region to create camera/solid/text and verify the object adheres across the whole shot.

**Failed solves**

Re-evaluate source quality, shot length and lens behavior. For one planar screen replacement, Mocha may be more direct than a full 3D camera solve.

**Experiment:** Track a short handheld room movement, create a ground-plane solid and watch it over 100 frames.

**Pitfalls:** A solver can produce apparently plausible 3D points while failing the intended insert.

**Related topics:** [Corner Pin and perspective insertion](#topic-perspective), [Mocha AE planar tracking](#topic-mocha)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-perspective"></a>
### Corner Pin and perspective insertion

*Tracking & 3D* — A four-corner mapping targets planar surfaces.

**Planar geometry**

A surface defined by four tracked corners can accept an animated screen or sign; corner ordering and transform calibration are critical.

**Matching**

Add appropriate edge softness, brightness, surface tint, noise, source blur and movement to integrate replacement media.

**Diagnose drift**

Use a visible checkerboard or clear colored corners to spot track errors before replacing with a complex UI or text.

**Experiment:** Insert a 640×360 checkerboard onto a moving four-corner plane without visible slippage.

**Pitfalls:** Perspective warp is not the same as a rigid layer transform with Position/Scale/Rotation.

**Related topics:** [Mocha AE planar tracking](#topic-mocha), [Point tracking, attach points and drift](#topic-point-tracking)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-color"></a>
### RGB, color profiles and grade order

*Color & delivery* — Keep image corrections separate from color-science transforms.

**Correction then look**

Balance exposure, white point, contrast and saturation consistently before adding a style look. Shot matching becomes harder if each clip begins with arbitrary creative LUTs.

**Managed project**

ICC workflows convert source profiles into a designated working space; OCIO workflows use configured transforms. If working space is None, color management is not working as it would in a managed comp.

**Viewer vs file**

Display color management transforms a working image to the monitor; a rendered output transform targets delivery. These need not use the same profile/transform.

**Experiment:** Export a small test chart as unmanaged and Rec.709-managed files and inspect metadata and appearance.

**Pitfalls:** Do not assume that turning monitor color management off edits the pixel values.

**Related topics:** [OCIO/ACES 2.0 in a 26.5 project](#topic-ocio), [8/16/32 bpc and floating point](#topic-color-depth)

**Sources:** [Adobe: color management](https://helpx.adobe.com/after-effects/desktop/adjust-colors/color-management/color-management.html)

<a id="topic-color-depth"></a>
### 8/16/32 bpc and floating point

*Color & delivery* — Project math precision differs from codec or source bit depth.

**Precision**

8 bpc uses integer-like limited steps; 16 bpc provides finer channel precision; 32 bpc floating point supports values outside the display 0..1 range and is common for HDR/linear-light pipelines.

**No recovered highlights**

Changing a clipped 8-bit source to 32 bpc preserves further calculations but cannot restore highlights already clipped in the recording.

**Effect support**

Individual effects may have different 8/16/32 support. Verify through installed effect behavior and Adobe effect documentation before claiming that one effect is universal.

**Experiment:** Apply several Curves operations to a gradient in 8 bpc and 16 bpc and compare visible banding.

**Pitfalls:** 32-bpc floating point project settings alone do not mean the H.264 output becomes 32-bit floating point.

**Related topics:** [RGB, color profiles and grade order](#topic-color), [Effects, presets and compatibility](#topic-effects)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-ocio"></a>
### OCIO/ACES 2.0 in a 26.5 project

*Color & delivery* — Configure input, scene-linear working space, display and render output deliberately.

**Color engine**

Project Settings → Color includes Adobe color managed and OpenColorIO-managed options in supported builds; choose the appropriate engine for the production pipeline.

**Config and transforms**

ACEScg is a working-space concept, not an output display transform. In OCIO choose configuration, source interpretation, working color space, viewing and output correctly.

**26.5 configuration**

OCIO 2.5.1 includes ACES 2.0 CG v4.0 and Studio v4.0. Choose a pipeline-approved configuration, set a suitable scene-linear working space, and set the Output Module color space independently from the viewer.

**Experiment:** Take one sRGB PNG, interpret it correctly in OCIO and export a Rec.709 display-targeted sample.

**Pitfalls:** Do not accidentally apply a display transform twice, once in an effect and again at output.

**Related topics:** [RGB, color profiles and grade order](#topic-color), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: OpenColorIO and ACES](https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-expressions"></a>
### Expression evaluation and safe syntax

*Expressions & data* — A property expression returns one calculated value at each time.

**Value vs action**

A property expression is computed as the composition renders. It changes a property value; it cannot arbitrarily add layers or save files.

**Functions**

Use time, value, wiggle(), ease(), linear(), clamp(), loopOut(), valueAtTime(), sourceRectAtTime(), toComp() and matching property types. On Position return a 2D/3D array as appropriate.

**Selection and errors**

Alt+click a stopwatch to create/remove an expression; the expression enable/disable switch is safer for temporary comparisons. Enable expression errors and resolve missing referenced effects or layers.

**Experiment:** Link one shape’s Rotation to another shape’s Position X coordinate via a scale mapping.

**Pitfalls:** A pasted expression can silently refer to the wrong composition when copied across comps.

**Related topics:** [JavaScript-like expressions, coordinates and values](#topic-expression-language), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html), [Adobe: understanding expression language](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-basics/expression-language.html)

<a id="topic-expression-language"></a>
### JavaScript-like expressions, coordinates and values

*Expressions & data* — Learn syntax, evaluation, and data dimensions rather than memorizing snippets.

**Types**

Numbers, arrays and strings differ. A 2D Scale returns `[x,y]`, Opacity returns one number, and Source Text can return a string or a compatible text style object.

**Property chain**

`thisComp.layer('NAME').transform.position` targets a concrete layer in current comp. `effect('Slider Control')('Slider')` reads a specific effect control; effect renaming changes the referenced path.

**Timing**

`time` is seconds, `framesToTime(n)` converts frames at context rate, and `posterizeTime()` alters expression sampling. `loopOut()` normally requires suitable keyed motion.

**Experiment:** Build a scale pulse driven by a Slider and toggle the slider from 0 to 100.

**Pitfalls:** Variables declared inside an expression are not globally stored between frames.

**Related topics:** [Expression evaluation and safe syntax](#topic-expressions), [sourceRectAtTime and dynamic card padding](#topic-auto-layout)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-expression-controls"></a>
### Sliders, points, angles, colors and dropdowns

*Expressions & data* — Expose deliberate rig parameters on a named Null.

**Control interfaces**

Expression Controls include Slider, Angle, Point, Color and other types. A readable named Slider like Swing Degrees is much easier to tune than hardcoded numbers across 12 expressions.

**Reference correctly**

Use the pick whip to generate exact effect/property paths. If a control is deleted or renamed unexpectedly, expressions can error and freeze or use fallback behavior.

**Defaults and ranges**

Although a Slider can store a large range, clamp incoming values in expressions when out-of-range results would cause negative size or absurd motion.

**Experiment:** Make a master controller with Spin, Radius, Tint and Pause, then wire three layers.

**Pitfalls:** A Slider is not automatically constrained to 0..100; clamp explicitly when required.

**Related topics:** [Expression evaluation and safe syntax](#topic-expressions), [Essential Properties as instance controls](#topic-essential-properties)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-data"></a>
### CSV, JSON and AE data inputs

*Expressions & data* — Make content replaceable while preserving animation structure.

**Formats**

CSV/TSV are suitable for flat tables and JSON for structured objects. A successful import does not guarantee the expression path to every nested field is what you assumed.

**Reference models**

`footage('file.json').sourceData` accesses JSON-like imported data; CSV/TSV may expose properties and dataValue access. Use the pick whip and inspect the actual imported shape.

**Failure modes**

Missing fields, wrong numeric types, commas in unquoted CSV fields and unexpected localized separators can break a template. Validate test rows including long names and zeros.

**Experiment:** Render three number cards from a short three-row data file.

**Pitfalls:** Do not bake confidential contact information into broadly shared MOGRTs without permission.

**Related topics:** [sourceRectAtTime and dynamic card padding](#topic-auto-layout), [Motion Graphics templates and protected timing](#topic-mogrt)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-auto-layout"></a>
### sourceRectAtTime and dynamic card padding

*Expressions & data* — Text changes require layout that uses current bounds rather than fixed-width guessing.

**Bounds**

`sourceRectAtTime(time,false)` returns a text layer’s current layout bounds including left/top offsets. `width` and `height` are useful for a rectangular background size.

**Alignment**

The text bounding rectangle may be offset relative to anchor/Position. Align background and text in a shared coordinate context, or transform bounds with coordinate-conversion methods.

**Padding**

Add independent horizontal and vertical padding; test long, short and empty text. Set a reasonable maximum width or word wrapping to protect design.

**Experiment:** Build one name badge that gracefully handles a two-letter name and a 30-character name.

**Pitfalls:** sourceRectAtTime does not automatically reposition a background around the text anchor.

**Related topics:** [Point/box text, metrics and typography](#topic-text), [Expression evaluation and safe syntax](#topic-expressions)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-essential-properties"></a>
### Essential Properties as instance controls

*Templates* — Different nested instances can expose and override selected controls.

**Master source**

Expose useful properties through Essential Graphics from an appropriate master comp; nested instances show the overrides as Essential Properties.

**Individual versions**

A reusable lower-third can use one source comp twice while individual instances have different title and color without altering shared internal animation.

**Maintainability**

Keep exposed properties few and well named. If required properties are missing or expressions refer elsewhere, the template can be difficult to customize.

**Experiment:** Make two instances of a one-source badge and change the name and color independently.

**Pitfalls:** An override in one instance is not a permanent edit to the original source.

**Related topics:** [Motion Graphics templates and protected timing](#topic-mogrt), [Precomposition and nested timeline logic](#topic-precomp)

**Sources:** [Adobe: create Motion Graphics templates](https://helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html)

<a id="topic-mogrt"></a>
### Motion Graphics templates and protected timing

*Templates* — A .mogrt is a controlled reusable package, not merely an .aep saved under another extension.

**Interface design**

Expose controls editors actually need: text, colors, durations and a few positions. Test user error cases and descriptive names before publishing.

**Timing**

Protected Regions allow selected intro/outro sections to remain unchanged when a motion graphics template is retimed. Inspect transitions at minimum/maximum intended durations.

**Dependencies**

Font installations, licensed plugins and expressions can affect an exported template. Verify compatibility with the target editing application where possible.

**Experiment:** Create a 4-second MOGRT with intro, body and outro that maintains its intro/outro in an 8-second test.

**Pitfalls:** A render or media proxy does not preserve MOGRT editability.

**Related topics:** [Essential Properties as instance controls](#topic-essential-properties), [Collect Files and portability](#topic-collect-files)

**Sources:** [Adobe: create Motion Graphics templates](https://helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html)

<a id="topic-puppet"></a>
### Puppet deformation and mesh setup

*Effects* — Use pinned deformable geometry for flexible illustration and cutout work.

**Pins and triangles**

Pin positions deform an underlying mesh, which is generated according to source alpha and tool settings. Put stable pins at joints/support points, not one pin per pixel.

**Rig controls**

Overlap determines which portions move in front/behind in relevant puppet modes; Starch stiffens a region. Test with a flat fill and no extra glow/blur to see deformation clearly.

**Looping**

For a 2-second cycle, match first/last pin poses and smooth speed. Test outlines at each extreme for holes or crumpled triangles.

**Experiment:** Rig an arm with shoulder, elbow and wrist pins; make a clean wave.

**Pitfalls:** A Puppet effect is not an automatic bone solver with awareness of anatomy.

**Related topics:** [Parametric shapes vs Bézier paths](#topic-shapes), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-particles"></a>
### Particles, emitters and simulation

*Effects* — Keep rate, lifespan, force and size separate.

**Population**

Approximate live particle count at steady state = rate × lifetime, with caveats for frame sampling and survival settings. Changing Longevity and Birth Rate together can double-count a desired density.

**Movement**

Initial velocity, Gravity, Resistance and emitter position define trajectories. Explore physics controls one at a time, keeping all others constant.

**Integration**

A particle effect usually renders into the source layer’s context. For multiple depths, duplicate/precompose particle elements and use masks, mattes and lighting/glow appropriately.

**Experiment:** Build one spark emitter lasting 0.5 seconds with 2 seconds of fading particles.

**Pitfalls:** Many native particle effects are 2.5D images, not real shaded 3D particles.

**Related topics:** [Effects, presets and compatibility](#topic-effects), [The effect stack and control surfaces](#topic-effect-order)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-simulations"></a>
### Other simulation and stylize effects

*Effects* — Effects may generate pixels, distort existing pixels or simulate pseudo-physics.

**Families**

Shatter and CC Pixel Polly break pixels into chunks; CC Ball Action makes a point/ball grid; Foam/CC Bubbles generate liquid/bubble impressions; Turbulent Displace warps the existing source.

**Use by goal**

Choose a particle emitter for autonomous moving pieces, Displacement Map for controlled deformation, and a texture/pixelation effect for stylized source conversion.

**Parameter discovery**

Find each effect’s exact 26.5 parameter list in installed Effect Controls and Adobe effect-specific documentation. The guide cannot truthfully specify parameters for every bundled/third-party revision.

**Experiment:** Recreate the same stylized logo breakdown using Shatter and CC Pixel Polly; compare limitations.

**Pitfalls:** Effects can be visually similar but have different layer size, sampling or cache behaviors.

**Related topics:** [Particles, emitters and simulation](#topic-particles), [Fractal/Turbulent Noise and displacement](#topic-procedural)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)

<a id="topic-export"></a>
### Render Queue decisions and preflight

*Color & delivery* — Choose deliverable-first settings and verify the resulting asset.

**Choose output**

H.264 review media differs from editing mezzanine or RGBA master. Decide dimensions, frame rate, color space, audio, alpha and destination before opening Output Module.

**Render Settings**

Quality, resolution, frame blending, motion blur and time span are render decisions. Output Module chooses container, codec, channels, depth, audio, file path and color conversion.

**Verification**

Inspect the first, middle and last frames; play the complete audio; check output resolution, fps, file size and alpha in an external consumer. Record the settings with the deliverable.

**Experiment:** Deliver three variants of the same comp and document why each is appropriate.

**Pitfalls:** Do not rely on an MP4 H.264 file for transparency.

**Related topics:** [Containers, codecs, sequences and masters](#topic-codecs), [Alpha, straight RGB and premultiplication](#topic-alpha), [RGB, color profiles and grade order](#topic-color)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-codecs"></a>
### Containers, codecs, sequences and masters

*Color & delivery* — Understand what the extension can and cannot promise.

**Container vs codec**

An .mp4 or .mov container can hold specific encoded video and metadata depending on the selected codec. ProRes/DNxHR/PNG/EXR differ in compression, color bit depth and alpha support.

**Image sequences**

A numbered PNG/EXR sequence preserves individual frames and may be resilient to interrupted renders, at the cost of many files and more management. Verify channel and color settings.

**Review vs mezzanine**

A small H.264 review is convenient; a high-quality intra-frame master or sequence is better for multiple rounds of effects/grading where supported by the pipeline.

**Experiment:** Render one 5-second RGBA element as a PNG sequence and confirm it recomposites cleanly in a fresh comp.

**Pitfalls:** Setting alpha in an output module cannot add a channel that a format lacks.

**Related topics:** [Render Queue decisions and preflight](#topic-export), [Alpha, straight RGB and premultiplication](#topic-alpha)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-collect-files"></a>
### Collect Files and portability

*Color & delivery* — An independently openable archive is the real deliverable test.

**Collection**

File → Dependencies → Collect Files copies referenced sources under chosen options and prepares a project. Confirm which proxies, unused items and plugin dependencies are included or omitted.

**Missing files**

Use Replace Footage and search folders to relink. Record stable relative subdirectories and verify no source still points to the old workstation.

**Team handoff**

Attach a README, screenshot/proof render and font/plugin list. Embed licensed third-party files only where your license permits.

**Experiment:** Reopen the collected copy with the original media drive disconnected.

**Pitfalls:** A linked external Photoshop/Illustrator asset can be missing even when the project opens.

**Related topics:** [Folders, naming and backup policy](#topic-project-management), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-performance"></a>
### RAM, disk cache and preview rate

*Troubleshooting* — Decide whether the bottleneck is decoding, rendering, memory or output.

**Cold vs warm preview**

The first pass calculates and caches frames. A replay may be far faster; changing a property can invalidate cached regions. Time only like-for-like comparisons.

**RAM and cache**

Memory preferences reserve RAM for other apps. Disk cache stores reusable intermediate frames on local storage; purging makes cached work disappear and may make the next playback slower.

**Multiframe**

When effects/plugins and resources permit, multi-frame rendering can render independent frames in parallel. Its gain depends on the shot, CPU, GPU, memory and media constraints.

**Experiment:** Time two previews before/after turning off an expensive effect; record whether the change helps cold and warm runs.

**Pitfalls:** Do not blindly assign all RAM to AE at Windows’ expense.

**Related topics:** [Cache levels, purging and invalidation](#topic-cache), [Proxies, pre-renders and fast preview](#topic-proxies)

**Sources:** [Adobe: memory and storage](https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html), [Adobe: multi-frame rendering](https://helpx.adobe.com/after-effects/desktop/render-and-export/multi-frame-rendering/multi-frame-rendering.html)

<a id="topic-cache"></a>
### Cache levels, purging and invalidation

*Troubleshooting* — A cached preview is reused work, not a permanently rendered file.

**Viewer vs memory**

Green/blue cache indicators and preview panels tell you about cached ranges and conditions. Preview may re-render after color/render setting changes even when footage is unchanged.

**Disk vs RAM**

RAM cached frames are short-lived; persistent disk cache may survive a restart for eligible intermediates. The exact behavior depends on source/effect and cache settings.

**When to purge**

Purge only for a diagnostic reason, corruption or disk management; capture a baseline first. Running out of free disk space can produce errors unrelated to the actual comp design.

**Experiment:** Change only one Glow parameter and observe which frames need rerendering.

**Pitfalls:** A preview cache does not substitute for a verified final exported master.

**Related topics:** [RAM, disk cache and preview rate](#topic-performance), [A structured debug decision tree](#topic-diagnostics)

**Sources:** [Adobe: memory and storage](https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html)

<a id="topic-proxies"></a>
### Proxies, pre-renders and fast preview

*Troubleshooting* — Substitute cheaper pixels while retaining an exact source of truth.

**Footage proxies**

Assign a lower resolution/quality proxy to complicated sources and clearly indicate which file is active. Some export paths may use source or proxy depending on settings.

**Pre-render**

For a computationally expensive nested composition, generate a high-quality render, then substitute it for iteration. Keep original comps and a versioned render path.

**Final review**

Before delivery verify source/proxy switch and any downsampled raster effect resolutions. A Quarter view is a performance choice, not proof of final sharpness.

**Experiment:** Produce a small proxy of a 4K clip, edit a 1080 comp, and verify which frames use proxy vs original.

**Pitfalls:** A proxy can hide scaling or codec artifacts that appear in the full-quality source.

**Related topics:** [RAM, disk cache and preview rate](#topic-performance), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-diagnostics"></a>
### A structured debug decision tree

*Troubleshooting* — Reduce a failure to one reproducible cause.

**Picture missing**

Check active viewer, comp time, video switch, In/Out span, alpha, mask, matte, opacity, solo/shy, 3D camera, effect stack and codec decoding.

**Picture incorrect**

Compare ungraded sources, then source interpretation, effect order, color working/display/output transforms, precomp switches and full-quality render.

**Performance failure**

Test a short work area, one expensive layer, one plugin at a time and a different source codec. Do not diagnose a whole project only from the CPU/GPU model name.

**Experiment:** Take a deliberately broken comp and identify the exact stage that makes it wrong.

**Pitfalls:** Multiple small causes can compound; one switch may not solve everything.

**Related topics:** [Missing plugins, effects and unsupported version](#topic-missing-effects), [Cache levels, purging and invalidation](#topic-cache)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-missing-effects"></a>
### Missing plugins, effects and unsupported version

*Troubleshooting* — A project can load without having the effect that produced a previous render.

**Diagnose source**

Check built-in Effects & Presets, Effect Manager, installed add-on version, licensing, Windows-only plugin paths and whether the effect debuted in 26.x.

**Avoid false fixes**

A missing plugin is not repaired by renaming an arbitrary different effect. Preserve the original project, replace intentionally, and compare the new render against a reference.

**Compatibility**

32-bpc, GPU acceleration, renderers and external plugin versions vary. Some old effects are marked Obsolete but may load older compositions for compatibility.

**Experiment:** Simulate missing effect by disabling one installed effect instance, save a test and document the visual fallback.

**Pitfalls:** Saving for an earlier release does not back-port unsupported native effects or mesh/material features.

**Related topics:** [A structured debug decision tree](#topic-diagnostics), [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow)

**Sources:** [Adobe: effect list and capabilities](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-scripting"></a>
### ExtendScript and project automation

*Advanced* — Build deterministic and reversible changes from scripts.

**Object hierarchy**

JSX/ExtendScript scripts use the AE scripting API: application, project, items, compositions, layers, properties and render queue. This differs from time-evaluated expressions.

**Safety**

Use try/finally/undo groups, validate active project/item types and test on a versioned copy. Avoid unreviewed scripts from unknown sources.

**Repeatability**

Use explicit comp names, prefixes and logs. Keep external input CSV/JSON stable and back up files before automatic relinking, renaming or rendering.

**Experiment:** Write a no-op JSX report listing current comp names and save its result outside the source .aep.

**Pitfalls:** JSX scripting is distinct from modern browser JavaScript modules or Node package installs.

**Related topics:** [Expression evaluation and safe syntax](#topic-expressions), [Folders, naming and backup policy](#topic-project-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-file-management"></a>
### Missing media, absolute paths and Windows storage

*Troubleshooting* — Drive letters and renamed folders can silently disrupt a project.

**Paths**

If imported files move on disk, AE’s Project items can become missing. Relink footage from Project with Replace Footage, and inspect affected duplicates/sequences.

**Cache vs original**

Disk cache is disposable processed data; imported source assets are not. Do not delete Assets because AE cached a preview.

**Pack and transfer**

Collect Files with source folders, then test the collected copy by opening it from a different folder. Include any external audio, fonts, 3D textures and LUT references.

**Experiment:** Rename an asset folder in Windows Explorer, observe the missing footage, and relink correctly.

**Pitfalls:** A project opened successfully can still have one or more missing media items.

**Related topics:** [Collect Files and portability](#topic-collect-files), [Folders, naming and backup policy](#topic-project-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-workflow"></a>
### Repeatable production and QC workflow

*Capstone* — Tie the individual skills into a dependable result.

**Define output first**

Agree on resolution, FPS, duration, codec, color, audio, alpha and revision rules before building layered animation. This determines composition settings and source requirements.

**Build in passes**

Block the story and timing, then implement graphics and track/roto, then add color, simulation and audio, finally handle render settings and QC.

**Review every layer of delivery**

A clean .aep, collected assets, fonts/plugins manifest, proof render and verified master are separate deliverables. Keep revision notes and a known-good prior version.

**Experiment:** Create a one-page checklist you can apply to any new client motion graphics job.

**Pitfalls:** A single green check mark in Render Queue is not complete quality assurance.

**Related topics:** [Final self-assessment and future practice](#topic-capstone), [Render Queue decisions and preflight](#topic-export), [Folders, naming and backup policy](#topic-project-management)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-capstone"></a>
### Final self-assessment and future practice

*Capstone* — Demonstrate independent ability rather than recall of one memorized recipe.

**Foundations**

Build and animate a three-layer shape composition without referring to menus. If you need the guide, identify the exact missing concept rather than rewatching unrelated tutorials.

**Compositing and effects**

Make one alpha matte, one chroma key/rotoscope, one procedural transition, a controller-based rig and a correctly managed render.

**Maintenance**

Reopen a collected project on a different path, diagnose one deliberately missing source, and explain why later-version shortcuts do not apply in your installed build.

**Experiment:** Complete the final lesson, then modify three visual decisions without following the original exact steps.

**Pitfalls:** A certificate is not meaningful without repeatable hands-on work.

**Related topics:** [Repeatable production and QC workflow](#topic-workflow), [A structured debug decision tree](#topic-diagnostics)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-release-26-5"></a>
### What changed through 26.5

*Foundations* — Locate modern tools without relearning the foundations.

**2026 foundation**

26.0 introduced native parametric meshes, Substance materials, variable-font axis animation, Unmult and Compressor/Gate/Distortion. SVG import was subsequently expanded; use current 26.5 import controls instead of an older workaround.

**Faster operations**

26.2 added Quick Apply, Object Matte, material displacement and Proportional Scrubbing. 26.3 added Curl Noise, Advanced 3D depth of field, improved Mask Tracker, vector clipboard transfer and Copy Frame to Clipboard.

**Current release**

26.5 improves guide placement, effect-instance labels, Effect Controls and Object Matte caching, and bundles ACES 2.0 via OCIO 2.5.1. These changes affect organization, reuse and color as well as visible imagery.

**Experiment:** Open one tool from each release family, then choose one that improves your own project.

**Pitfalls:** A feature-history date and a later expanded workflow are different facts.

**Related topics:** [Quick Apply: effects, presets and commands](#topic-quick-apply), [Object Matte: select, propagate, refine and cache](#topic-object-matte), [26.5 guides: pixels, percent, edge pinning and color](#topic-responsive-guides), [OCIO/ACES 2.0 in a 26.5 project](#topic-ocio), [Stable versus Beta: read newer tutorials critically](#topic-beta-watchlist)

**Sources:** [Adobe: After Effects release notes (26.5, September 2026)](https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html), [Adobe: What is new through 26.5](https://helpx.adobe.com/after-effects/desktop/what-s-new/whats-new.html), [Adobe-maintained After Effects feature history](https://github.com/AdobeDocs/after-effects-feature-history)

<a id="topic-quick-apply"></a>
### Quick Apply: effects, presets and commands

*Effects* — Find the operation by name, with a deliberate target.

**Open and filter**

Select the intended layer(s), press Ctrl+Enter or use Edit → Quick Apply. Prefix e: for effects, p: for presets or m: for menu commands. Choose the matching result and press Enter.

**New layers**

Inside the dialog, Ctrl+Enter applies the selected effect/preset to a new solid or layer; Ctrl+Alt+Enter creates an adjustment layer. Read the modifier hints for that result. Creating an adjustment changes which underlying pixels are processed.

**Inspect**

F3 opens Effect Controls. Check preset-added keys at the playhead, remove only unwanted properties and undo if it affected the wrong selection. A command result can act on the project rather than the selected layer.

**Experiment:** Apply Glow to a selected shape, then apply it to a new adjustment layer and explain the changed scope.

**Pitfalls:** Ctrl+Enter opens the dialog outside it, but applies to a new layer while inside it.

**Related topics:** [The effect stack and control surfaces](#topic-effect-order), [Adjustment layers and global looks](#topic-adjustment-effects)

**Sources:** [Adobe: Quick Apply](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/quick-apply.html)

<a id="topic-object-matte"></a>
### Object Matte: select, propagate, refine and cache

*Compositing* — Extract an object, then judge the matte across time.

**Base selection**

Double-click the footage layer to open Layer panel. Choose Object Matte from the toolbar, hover a clear subject and click. Use rectangle/lasso or Quick Selection and Selection Brush to correct included/excluded areas; Refine Edge helps hair.

**Propagation**

Advance through the required span, inspecting occlusions and pose changes. Correct errors, then Freeze from the Layer panel once the span is ready. Check the result over contrasting backgrounds before using it as a track matte.

**Persistence**

26.5 stores propagation on disk for reuse after reopening. Keep disk space available. Cached analysis and a saved project are different from an exported alpha master; changing the selection can require more propagation.

**Shortcut conflict**

Adobe’s Object Matte page lists Ctrl+W, while the general shortcut reference assigns Ctrl+W to Close. Use the toolbar or verify/remap the command in the installed editor; the documents do not establish a reliable focus rule.

**Experiment:** Isolate two seconds of a moving subject, inspect every frame, save/reopen and compare the matte before export.

**Pitfalls:** Disk caching does not certify an edge or replace footage/project backups.

**Related topics:** [Roto Brush and Refine Edge alongside Object Matte](#topic-roto), [Tracked masks vs hand-roto](#topic-mask-tracking), [Alpha/luma track mattes](#topic-mattes)

**Sources:** [Adobe: AI-powered Object Matte](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html), [Adobe: After Effects keyboard shortcuts reference](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)

<a id="topic-responsive-guides"></a>
### 26.5 guides: pixels, percent, edge pinning and color

*Animation* — Design margins that remain meaningful as the canvas changes.

**Placement**

In the intended viewer show rulers (Ctrl+R), drag out a guide, then right-click → Edit Guide. Set orientation, pixel/percent units, reference edge and color. View → Add Guide provides numeric placement directly.

**Responsive reference**

Use a percentage for proportional position, or a pixel offset from right/bottom for a fixed opposite-edge margin. During dragging, Alt changes units and Ctrl toggles pinning. Pinning changes the reference; locking (Ctrl+Alt+Shift+;) prevents movement.

**Reuse and scope**

Guides belong to the active view; they do not automatically reposition artwork or render into a movie. Export/import with View → Export Guides / Import Guides. Adobe’s page retains contradictory old import notes after its explicit 26.5 preservation statement: verify a round trip in the actual destination build.

**Experiment:** Set a 50% vertical guide and a 100-pixel right margin; change a duplicate comp’s width and compare their positions.

**Pitfalls:** Guides, guide layers and grid overlays are different; none is an automatic layout rig.

**Related topics:** [Coordinates, anchor points and transforms](#topic-coordinates), [sourceRectAtTime and dynamic card padding](#topic-auto-layout)

**Sources:** [Adobe: Guide creation and management](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html)

<a id="topic-effect-labels"></a>
### Effect labels, masks and reusable presets

*Effects* — Keep long stacks readable while controlling each effect’s scope.

**Organization**

26.5 modernizes Effect Controls and allows a color label on an individual effect instance. Select the gray label swatch beside the effect name and choose a color; use a purpose-based name. Colors organize controls; they do not change pixels or combine effects into one calculation.

**Local contribution**

Draw a mask, set Mode=None when it should not cut layer alpha, then expand the effect in Timeline → Compositing Options and add a Mask Reference. Tune mask feather and Effect Opacity, watching effect support and render order.

**Reuse**

Select the intended effects/properties and use Animation → Save Animation Preset for an .ffx. A preset stores selected settings/keys, not fonts, footage or plug-in installers. Apply on a duplicate at a known CTI and inspect changes.

**Experiment:** Make a masked Curves correction, name/color its effect, save the preset and test it on a duplicate layer.

**Pitfalls:** A Timeline layer label and an Effect Controls instance label are independent.

**Related topics:** [The effect stack and control surfaces](#topic-effect-order), [Mask modes and feathering](#topic-masks), [Effects, presets and compatibility](#topic-effects)

**Sources:** [Adobe: Effect Controls and instance labels](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html), [Adobe: Effect masks, opacity and animation presets](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html)

<a id="topic-proportional-scrubbing"></a>
### Quick Offset versus Proportional Scrubbing

*Animation* — Distribute either time or numeric changes without confusing the gestures.

**Time**

Select layer bars or keys in the intended order. Ctrl+Alt-drag in Timeline uses Quick Offset to spread timing. The first selection anchors the distribution; a layer offset carries its internal animation with it.

**Values**

For Proportional Scrubbing, select layers/properties in order, then Ctrl+Alt-drag the property hot text. The first gets zero added change, the last the full change and intermediate selections fractions. Three layers and a 120-pixel change receive offsets 0, 60, 120; unequal initial positions need not become equal final spacing.

**Group boundaries**

Shift+[ aligns the earliest In of the selection to CTI, Shift+] the latest Out, preserving relative timing. Alt+Shift brackets adjust the corresponding boundary group. Ordinary brackets instead use each layer’s own boundary. Check source handles when extending footage.

**Experiment:** With three initially aligned cards compare a 120-pixel proportional change with a timing offset; undo between trials.

**Pitfalls:** Ctrl+Alt is the same modifier family, but dragging bars and dragging hot text perform different operations.

**Related topics:** [Layer bounds, work areas and markers](#topic-timeline), [Keyframes and interpolation](#topic-keyframes), [Timing and design principles for readable motion](#topic-motion-design)

**Sources:** [Adobe: Proportional Scrubbing](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/proportional-scrubbing-in-timeline.html), [Adobe: Selecting and arranging layers](https://helpx.adobe.com/after-effects/desktop/work-with-layers/select-and-arrange-layers/selecting-arranging-layers.html)

<a id="topic-svg-workflow"></a>
### SVG file import and vector clipboard transfer

*Animation* — Choose source linkage or editable geometry intentionally.

**File route**

Use File → Import → File and choose SVG footage or composition as appropriate. A composition provides editable vector layers; footage behaves as a source item. Compare imported fills, gradients, strokes, grouping and bounds before animation.

**Clipboard route**

In Illustrator enable Edit → Preferences → Clipboard Handling → Include SVG Code. Copy artwork, then Ctrl+V in AE to add editable shapes. With no selected comp, a composition can be created. Other apps must actually put SVG data on the clipboard; copying XML as plain text is different.

**Text and fidelity**

Outline SVG text before this paste route, retaining the editable original elsewhere. Stable editable shape import does not establish editable Illustrator-text conversion, which remains Beta. Compare appearance at enlarged scale and inspect individual groups.

**Experiment:** Import samples/badge.svg as footage and as a composition; recolor one shape and explain which source stays linked.

**Pitfalls:** SVG text and every browser SVG filter are not guaranteed to transfer as editable AE objects.

**Related topics:** [Parametric shapes vs Bézier paths](#topic-shapes), [Import formats, sequences and linked files](#topic-import-media), [Stable versus Beta: read newer tutorials critically](#topic-beta-watchlist)

**Sources:** [Adobe: SVG import and clipboard transfer](https://helpx.adobe.com/after-effects/desktop/import-files/import-svg-files/import-svg-files.html)

<a id="topic-variable-fonts"></a>
### Animate variable-font axes and spacing

*Text & data* — Animate genuine font variation while keeping the text editable.

**Prerequisite**

Use a variable font whose installed file exposes axes such as Weight, Width or Slant. Multiple static font weights alone are not a variable font. The font filter can help locate variable families.

**Animate**

Expand the text layer, choose Animate → Variable Font Axes → the supported axis. Enable its stopwatch, move CTI and set another value within that font’s range. Use the Range Selector for character/word subsets.

**Layout**

Text → More Options → Variable Font Spacing controls compensation during axis changes. Compare spacing modes, multiline wrapping and the same font on the rendering machine. Width animation and layer Scale produce different letter shapes and spacing behavior.

**Experiment:** Animate one word’s Weight over 24 frames and use a selector to send the change across characters.

**Pitfalls:** A missing axis is usually a font capability issue; do not invent unsupported axis limits.

**Related topics:** [Point/box text, metrics and typography](#topic-text), [Text animators and selectors](#topic-text-animator), [sourceRectAtTime and dynamic card padding](#topic-auto-layout)

**Sources:** [Adobe: Working with Variable Font Axes](https://helpx.adobe.com/after-effects/desktop/variable-font-axes/work-with-variable-font-axes/working-with-variable-font-axes.html)

<a id="topic-parametric-meshes"></a>
### Native parametric meshes and material appearance

*Tracking & 3D* — Build simple real geometry instead of using a sphere image effect.

**Create**

Use Advanced 3D and the Parametric Mesh toolbar tool or Layer → New to create a primitive. Inspect Mesh Options, supported Bevel Options and material assignment. Ctrl draws from center, Shift constrains proportions while drawing.

**Appearance**

Change Base Color, Roughness and Metallic, then compare lighting at the same camera pose. Material Emission changes appearance but does not illuminate neighboring objects; use a light for illumination.

**Geometry**

Mesh controls change scene geometry. CC Sphere instead renders a sphere-like image from layer pixels. Choose a native mesh for perspective/lighting interactions and keep geometry detail appropriate to the visible result.

**Experiment:** Create a cube and sphere with contrasting roughness, orbit a camera and identify which highlights follow the environment.

**Pitfalls:** A native mesh and an extruded text/shape layer are different object types.

**Related topics:** [Classic 3D, Advanced 3D and Cinema 4D](#topic-3d-renderers), [Substance SBSAR and real mesh displacement](#topic-substance-materials), [Advanced 3D in-engine depth of field](#topic-advanced-dof)

**Sources:** [Adobe: Create parametric meshes](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html)

<a id="topic-substance-materials"></a>
### Substance SBSAR and real mesh displacement

*Tracking & 3D* — Separate surface shading from geometric displacement.

**Assign**

Import an .sbsar material, apply it to a supported model or parametric mesh and inspect its exposed controls. Keep the SBSAR file and texture dependencies with the project. A material preset can expose different controls from another material.

**Height**

Use the supported displacement controls on a parametric mesh with a suitable height input. Increase displacement modestly and inspect silhouette, surface detail and rendering cost. A bump/normal appearance does not necessarily change the silhouette; displacement can.

**Stable boundary**

26.5 supports this mesh/model workflow. Animated layers as material inputs and Substance assignment to 3D text/shapes are separately listed Beta features. A missing material after reopening may require Reload Footage; compare Adobe known issues before rebuilding the scene.

**Experiment:** Compare a textured primitive with displacement off/on under identical camera/light settings and document dependencies.

**Pitfalls:** A 2D Displacement Map effect remaps pixels; it does not create this geometry.

**Related topics:** [Native parametric meshes and material appearance](#topic-parametric-meshes), [GLTF/GLB/OBJ/FBX and environment lights](#topic-3d-models)

**Sources:** [Adobe: Apply Substance 3D materials](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/apply-substance-3d-materials.html), [Adobe: Modify materials and displacement](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/modify-materials-properties-of-3d-layers.html), [Adobe: Known issues by affected release](https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/known-issues-after-effects.html)

<a id="topic-advanced-dof"></a>
### Advanced 3D in-engine depth of field

*Tracking & 3D* — Focus an actual 3D scene using camera distance.

**Scene setup**

Choose Advanced 3D in Composition Settings and create a camera with objects at visibly different distances. Enable Camera Options → Depth of Field. Inspect the scene in Active Camera, not only a custom view.

**Focus**

Set Focus Distance to the intended object depth; adjust Aperture and Blur Level for the desired amount. Animate focus between objects and inspect edge quality at Full resolution. Render a short sample because interactive quality can differ.

**Distinctions**

This in-engine capability arrived in 26.3. Camera Lens Blur uses a 2D grayscale blur map; the older Depth of Field effect needs suitable depth data. Neither is automatically a scene-camera DOF switch. More blur cannot reveal an occluded object.

**Experiment:** Rack focus between a near cube and far sphere over 48 frames, then compare the first/middle/last rendered frames.

**Pitfalls:** An f-stop/aperture change in a simulated scene does not guarantee photographic exposure changes.

**Related topics:** [Camera nodes, POI and projection](#topic-cameras), [Native parametric meshes and material appearance](#topic-parametric-meshes), [Displacement, depth and faux 3D](#topic-depth-maps)

**Sources:** [Adobe: Advanced 3D in-engine depth of field](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-3d-scene-depth-data/enable-in_engine-depth-of-field-in-advanced-3d.html)

<a id="topic-curl-noise"></a>
### Curl Noise: a flowing texture experiment

*Effects* — Control structure separately from motion and color.

**Start**

Create a comp-sized solid and Quick Apply e:curl noise. Begin with Internal input. Compare spatial Scale and Swirl before adding color; a large preview area makes pattern changes easier to judge.

**Motion**

Speed/Direction drift the input; Evolution changes its state; Turbulence Speed changes temporal activity. Inspect Input Noise, Curl Generation and Final Render to isolate the stage creating a result. Flow sampling controls affect continuity and cost.

**Use**

Tint or Tritone can colorize the rendered field. Precompose when using it as a Displacement Map source or luma matte, and choose the appropriate sampled layer stage. For a loop, stop unrelated drift, cycle the intended controls and test the join; Evolution alone does not guarantee a seamless loop.

**Experiment:** Make two four-second textures with identical color but different scale/flow, then use one as a matte.

**Pitfalls:** This is procedural texture rather than a fluid solver with collision-aware smoke.

**Related topics:** [Fractal/Turbulent Noise and displacement](#topic-procedural), [The effect stack and control surfaces](#topic-effect-order), [Displacement, depth and faux 3D](#topic-depth-maps)

**Sources:** [Adobe: Noise, grain and Curl Noise](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html)

<a id="topic-unmult"></a>
### Unmult: convert a black or white backing into alpha

*Compositing* — Build transparency that can travel to another application.

**Input**

Use a suitable black- or white-backed element. Apply Unmult through Quick Apply or Keying. Choose the Background Color mode; inspect alpha separately using Alt+4.

**Edges**

Tune the corresponding level, Softness and Remove Color Matting. Judge semitransparent edges over dark and light backgrounds. Protect genuine black/white foreground regions with another matte if they must survive.

**Output**

A Screen blend can visually hide black over one background while leaving different alpha semantics. For reusable assets, render to an alpha-capable format with RGB+Alpha, then reimport and inspect both color and transparency.

**Experiment:** Unmult a black-backed light element and recompose its RGBA export over gray and magenta.

**Pitfalls:** Removing a background cannot reconstruct foreground color information destroyed in the source.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Keylight, spill and edge recovery](#topic-keying), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: Keying and Unmult](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html)

<a id="topic-audio-dynamics"></a>
### Compressor, Gate and Distortion in 26.5

*Audio* — Treat loudness, pauses and saturation as separate tasks.

**Dynamics**

Compressor reduces louder passages above a threshold; adjust Ratio, Attack and Release, then match bypass loudness before judging. A louder result is not automatically cleaner.

**Pauses**

Gate attenuates below threshold. Set it relative to the actual noise floor and tune Hold/Release to preserve word endings. It does not remove noise mixed under active speech.

**Sound design**

Distortion changes timbre. Start with low Drive and modest Mix, compensate output Volume and check peaks in the rendered audio. Resolution/downsampling make intentional digital degradation. De-esser remains Beta at this cutoff; do not expect it in stable.

**Experiment:** Process samples/pulse.wav and a recorded phrase on duplicates, level-match bypass and compare a rendered WAV.

**Pitfalls:** An audio effect does not generate a visual waveform or automatically detect musical beats.

**Related topics:** [Audio preview, sync and output](#topic-audio), [Convert Audio to Keyframes workflow](#topic-audio-reactive), [Stable versus Beta: read newer tutorials critically](#topic-beta-watchlist)

**Sources:** [Adobe: Audio effects](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/audio-effects.html)

<a id="topic-clipboard-frame"></a>
### Snapshots, clipboard frames and rendered stills

*Foundations* — Choose an inspection image or a controlled production still.

**Internal comparison**

Viewer snapshots use Shift+F5 through Shift+F8 to store, F5 through F8 to compare. These are temporary comparison aids, not asset exports.

**Clipboard**

Activate Composition, Layer or Footage and use Ctrl+Alt+Shift+F5 after the frame renders. Transparency Grid affects whether alpha is preserved for a supporting destination. The copy reflects viewing/color-management transforms; receiving apps choose a supported clipboard format.

**Production**

Ctrl+Alt+S queues a still through Render Queue. Choose channels, precision and output color deliberately for production; do not treat a clipboard screenshot as an unmanaged scene-linear EXR.

**Experiment:** Copy a translucent shape with the transparency grid on/off and compare with an RGB+Alpha still render.

**Pitfalls:** Destination clipboard support can differ even when AE supplies transparency.

**Related topics:** [RGB, color profiles and grade order](#topic-color), [Alpha, straight RGB and premultiplication](#topic-alpha), [Render Queue decisions and preflight](#topic-export)

**Sources:** [Adobe: Copy Frame to Clipboard](https://helpx.adobe.com/after-effects/desktop/view-and-preview/copy-frames/copy-frame-to-clipboard.html)

<a id="topic-native-null-controllers"></a>
### Native null controllers for points and paths

*Expressions & data* — Use maintained menu commands when a path needs reusable controls.

**Point properties**

Select a positional property or effect point and use Layer → Create → Null Controllers for Positional Points. Selecting a layer alone targets Position. Animate the generated null and inspect expression/Layer Control links.

**Path direction**

For a selected Path, Null Controllers for Path Points lets nulls drive vertices; Nulls Following Path Points does the reverse; Null Tracing Along Path creates a traveling control. These commands are also available through Animation → Keyframe Assistant.

**Rigs**

Use the JavaScript expression engine and distinct names. Shape-group skew/nonuniform scale or separating Position dimensions after linking can need repair. The older Create Nulls From Paths script panel has related operations under different labels.

**Experiment:** Create an arrow following a curved path with Null Tracing Along Path and change the path afterward.

**Pitfalls:** Select the actual property, not only the layer, for path-specific commands.

**Related topics:** [Masks, shape paths and motion paths](#topic-paths), [Parenting, nulls and reusable rigs](#topic-parenting), [Expression evaluation and safe syntax](#topic-expressions)

**Sources:** [Adobe: Native null controllers](https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/null-controllers/create-nulls-for-positional-properties-and-paths.html)

<a id="topic-profiler"></a>
### Composition Profiler, ROI and compressed cache

*Troubleshooting* — Measure the operation you intend to accelerate.

**Timings**

Enable the Timeline Render Time column using its snail icon or column menu. Expand a layer to compare effects/masks. Cached readings can include retrieval and carry an asterisk; compare the same frame, resolution and cache state.

**Area**

ROI restricts preview work. Crop Comp to Region of Interest changes the canvas; Output Module cropping changes the delivered area. These operations have different consequences. Turn ROI off for final whole-frame review.

**Storage**

Lossless compressed disk frames trade cache storage and processing without lossy export changes. Preferences → Disk → Disk Cache → Enable Compressed Frames (Lossless) controls it. Diagnose specific failures before disabling it; the known crash notice names 26.0/26.2, not a blanket 26.5 defect.

**Experiment:** Measure cold/warm timings for a short Glow stack and compare an ROI preview without changing delivery settings.

**Pitfalls:** Do not report cache replay timing as uncached final-render throughput.

**Related topics:** [RAM, disk cache and preview rate](#topic-performance), [Cache levels, purging and invalidation](#topic-cache), [Proxies, pre-renders and fast preview](#topic-proxies)

**Sources:** [Adobe: Composition Profiler](https://helpx.adobe.com/after-effects/desktop/work-with-compositions/composition-profiler/composition-profiler.html), [Adobe: Lossless compressed playback](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/lossless-compressed-playback.html), [Adobe: Known issues by affected release](https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/known-issues-after-effects.html), [Adobe: Previewing and Region of Interest](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/previewing.html)

<a id="topic-beta-watchlist"></a>
### Stable versus Beta: read newer tutorials critically

*Foundations* — Keep the 26.5 offline guide usable without Beta-only commands.

**Cutoff**

Adobe’s Beta page checked 2026-10-28 was updated October 7. It separately lists Contour Paint, De-esser, AI Assistant, animated layers as material inputs and Substance materials on 3D text/shapes.

**More experimental tools**

Editable Illustrator-text conversion, Quick Set Anchor, broader viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save are on that list. Their appearance in the shared documentation sidebar is not release evidence.

**Project decision**

Use stable alternatives for a 26.5 handoff: shape outlines, ordinary anchor controls, Ctrl+D, supported mesh materials and standard save/backup workflows. If you deliberately use Beta elsewhere, document that separate dependency and provide a compatible render.

**Experiment:** Identify one tutorial using a Beta feature and explain a stable 26.5 way to achieve a comparable result.

**Pitfalls:** Mesh-specific Alt-drag in stable documentation does not prove generalized viewer duplication is stable.

**Related topics:** [Version discipline: 26.5 stable and a separate Beta](#topic-version-workflow), [What changed through 26.5](#topic-release-26-5)

**Sources:** [Adobe: After Effects Beta (separate from stable)](https://helpx.adobe.com/after-effects/desktop/what-s-new/after-effects-beta.html)

<a id="topic-expression-examples"></a>
### Copyable expression building blocks

*Expressions & data* — Use complete references, correct dimensions and an inspectable coordinate system.

**Scalar and vector**

On Rotation, `time*90;` produces 90 degrees per second. On 2D Scale use `s=100+Math.sin(time*2)*10; [s,s];`. Put expressions on the intended property; an array and a scalar are not interchangeable.

**Measured text card**

For a simple background shape in the same untransformed context as a text layer named CAPTION, use `r=thisComp.layer("CAPTION").sourceRectAtTime(time,false); [r.width+40,r.height+24];` on Rectangle Path Size. Its group Position also needs `[r.left+r.width/2,r.top+r.height/2]` relative to the text origin; parent/align origins deliberately before linking. Size alone does not center the card.

**Coordinate conversion**

For a 2D follower’s Position, use `src=thisComp.layer("LEADER"); p=src.toComp(src.anchorPoint); hasParent ? parent.fromComp(p) : p;`. Inspect parent spaces and the returned dimensions; a 3D rig may require world-space methods instead.

**Controller**

On Rotation use `time*thisComp.layer("CTRL").effect("Speed")("Slider");` after creating and naming the null/slider. Use the expression pick whip for exact references and expose controls rather than duplicating constants.

**Experiment:** Build a labeled rotating badge with auto-sized text backing, then parent the rig and test the coordinate links.

**Pitfalls:** The displayed expression is evaluated per property; it cannot create layers as a JSX script would.

**Related topics:** [Expression evaluation and safe syntax](#topic-expressions), [sourceRectAtTime and dynamic card padding](#topic-auto-layout), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-expression-lookup"></a>
### Modern dropdown labels, key lookup and range mapping

*Expressions & data* — Read a configured control without maintaining duplicate label lists.

**Dropdown**

An eligible dropdown property exposes .text for its current label, .items for its label array and .textAtTime(t) for a sampled label. On Source Text, `thisComp.layer("CTRL").effect("Choice")("Menu").text;` needs an actual renamed dropdown control. Menu values are one-based; .items arrays are zero-based. Use numeric indices for portable logic because labels can be localized.

**Key lookup**

nextKey(t) returns the later key or the last at the end. previousKey(t) returns a key at/before time or the first before the start. Check numKeys before querying an empty property or marker stream; J/K are unrelated UI navigation.

**Range behavior**

linear(x,a,b,c,d) holds endpoint output values outside the input range; ease also holds its endpoints. For deliberate scalar extrapolation write the arithmetic explicitly, for example `20+(value/100)*180;`. Validate zero input spans in reusable rigs.

**Experiment:** Drive a text label from a named Dropdown Menu Control and compare the current label with one sampled a second earlier.

**Pitfalls:** String matching can fail after localization or renamed choices; numeric logic can remain stable.

**Related topics:** [JavaScript-like expressions, coordinates and values](#topic-expression-language), [Sliders, points, angles, colors and dropdowns](#topic-expression-controls), [CSV, JSON and AE data inputs](#topic-data)

**Sources:** [Adobe: expression language reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html)

<a id="topic-outline-styles"></a>
### Text outlines, Layer Styles and source editability

*Text & data* — Choose geometry conversion separately from live text and effect outlines.

**Outlines**

Select a text layer and use Layer → Create → Create Shapes From Text or Create Masks From Text. Keep the original text: generated outlines do not update when wording changes. Inspect holes in compound letters before animating vertices.

**Styles**

Layer → Layer Styles includes shadow, glow, bevel, overlay and Stroke options. These are Timeline style properties with their own render behavior, rather than ordinary Effect Controls instances.

**Stroke choices**

A style Stroke follows visible layer content; Generate → Stroke follows a mask path; a shape Stroke styles its geometry. Use shape Trim Paths for a designed line reveal, a mask Stroke for mask-based writing and a style for a silhouette outline.

**Experiment:** Compare the three Stroke approaches on duplicated artwork and record which remains editable as text.

**Pitfalls:** Converting artwork to paths sacrifices source-string editability; retain a source version.

**Related topics:** [Point/box text, metrics and typography](#topic-text), [Parametric shapes vs Bézier paths](#topic-shapes), [Shape strokes, Trim Paths and Write-on](#topic-strokes)

**Sources:** [Adobe: Create masks and outlines](https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/work-with-masks/create-masks.html), [Adobe: Blending modes and Layer Styles](https://helpx.adobe.com/after-effects/desktop/work-with-layers/work-with-layer-blending-modes/blending-modes-layer-styles.html)

<a id="topic-immersive"></a>
### 360-degree imagery and seam-aware effects

*Effects* — Convert between spherical panoramas and a normal viewer intentionally.

**Projection**

Use suitable equirectangular source imagery. VR Sphere to Plane makes a rectilinear view; VR Plane to Sphere puts planar imagery into a spherical projection. These work with appropriate still or moving sources.

**Seams**

Use immersive-aware effects for work across panorama seams, then inspect the full wrap rather than only a center viewport. Ordinary planar blur/distortion can create a discontinuity at the edge.

**Workflow**

Use VR Comp Editor or a deliberate nested-comp setup where available, retaining source projection and destination dimensions. CC Environment is another environment-mapping effect, not a stills-only counterpart to video-only VR effects.

**Experiment:** Project a panorama to a normal frame, animate the view and inspect a seam-spanning effect in the wrapped source.

**Pitfalls:** A spherical projection is not editable geometric scene depth.

**Related topics:** [2.5D layers and spatial depth](#topic-3d-intro), [Effects, presets and compatibility](#topic-effects)

**Sources:** [Adobe: Immersive video effects](https://helpx.adobe.com/after-effects/desktop/immersive-video-and-vr/immersive-video-effects/vr-effects.html)

<a id="topic-source-time"></a>
### Footage source time vs comp time

*Foundations* — Which source frame appears depends on interpretation, layer start, time stretch and remapping.

**Comp clock**

The timeline CTI measures time in the active composition. A source clip's first visible frame may be offset if the layer has an adjusted start time, In/Out or stretch.

**Remapped clock**

Time Remap keys specify the source timestamp to sample at a comp time. A reverse or freeze segment changes footage source sampling without moving the layer bar.

**Nested clocks**

A precomp layer samples an inner composition time; frame rates may differ, and fractional times can be involved. Always compare displayed source and comp frame counts.

**Experiment:** Make a clip show its original second 3 at comp second 1 without modifying the original media.

**Pitfalls:** Source time must not be confused with keyframe timing.

**Related topics:** [Time remapping, reversal and loops](#topic-time-remap), [Layer bounds, work areas and markers](#topic-timeline)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-frame-rate"></a>
### Frame-rate conversion and temporal sampling

*Foundations* — Source FPS, composition FPS and output FPS are separate choices.

**Source interpretation**

Interpret Footage defines assumed source rate for certain media. Changing this is not the same as placing a 30-fps clip in a 24-fps comp.

**Sampling**

Compositions evaluate frames at their own FPS and may repeat/drop/blend sources if frame rates differ. Frame blending and pixel motion can interpolate but may create artifacts.

**Delivery**

Choose an output frame rate intentionally and verify final frame count, audio sync and timecode before handoff.

**Experiment:** Put a 30-fps clip into a 24-fps comp and compare frame blending off vs on during a fast pan.

**Pitfalls:** Frame rate changes can make keyframe rhythms appear different at playback.

**Related topics:** [FPS, timecode and frame alignment](#topic-frames), [Time remapping, reversal and loops](#topic-time-remap)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

<a id="topic-compositing"></a>
### Layer-based compositing and image order

*Compositing* — Layers, alpha, mattes, blending and effects work together to produce pixels.

**Stack model**

In ordinary 2D, higher layers cover lower layers depending on their opacity, alpha and blending mode. An adjustment layer uses composited lower pixels as its image input.

**Opacity pipeline**

Source alpha, masks, effects and track matte controls can combine to set final coverage. Inspect RGB and alpha separately to find errors.

**Organizing passes**

For demanding shots, work on source cleanup, segmentation/keying, track integration, grade, then finishing grain/sharpness. Nest only when it clarifies render order.

**Experiment:** Build three overlapping colored shapes and explain precisely which pixels contribute at the center.

**Pitfalls:** Blending two layers visually is not necessarily equivalent to creating alpha for downstream use.

**Related topics:** [Alpha, straight RGB and premultiplication](#topic-alpha), [Layer blend modes and compositing](#topic-blending), [Effect and transform evaluation order](#topic-render-order)

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

---

## Practical recipes

### 01 · Animated loading ring with Trim Paths

**Animation · Beginner · Suggested after lesson 08** — Make a ring that draws itself without raster effects.

1. Draw a shape ellipse with Fill set to None and Stroke to a visible color/width.
2. Inside Contents add Trim Paths and animate End from 0 to 100 over 16 frames.
3. For a spinning partial ring, set Start/End to reveal one arc, then animate Offset.
4. Add a Repeater or a second ring for additional visual structure, without unnecessary plugins.
5. Preview at target size to check line cap and antialiasing.

**Verify:** Ring draws cleanly and is readable at one quarter of comp size.
**If it fails:** A fill may hide the open stroke if left enabled.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 02 · Handwriting from a traced mask

**Animation · Beginner · Suggested after lesson 09** — Use the Stroke effect to reveal a line.

1. Place scanned writing on a comp-sized solid or duplicated image as an image guide.
2. Draw one or several mask paths along the visible pen stroke in the correct order.
3. Apply Generate → Stroke, choose the mask(s) and Paint Style appropriate to the reveal.
4. Animate End from 0 to 100 over the intended write-on duration.
5. Use a white reveal matte or controlled Alpha Matte to reveal a separate textured ink layer when needed.

**Verify:** Strokes appear in a plausible writing order and do not reveal undesired connecting lines.
**If it fails:** Stroke operates along masks, while Trim Paths operates on shape contents.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 03 · Logo reveal using a matte

**Compositing · Beginner · Suggested after lesson 10** — Animated shape reveals a graphic without destroying its pixels.

1. Create a 1920×1080 24-fps composition and center a logo PNG with transparency.
2. Create a white rounded rectangle as a fixed reveal window covering the logo’s final position. Position the logo entirely outside the window at the start.
3. On the logo layer select the rectangle as an Alpha Matte source; use F4 if the TrkMat column is hidden.
4. Animate the logo into its final position inside the stationary matte over 20 frames. Ease the entrance and inspect alpha; the full final logo must remain inside the window.
5. Place a second copy of the logo at low opacity underneath for a tasteful ghost trail, only if readability improves.

**Verify:** The logo is never visibly stretched and is fully revealed by frame 20.
**If it fails:** If the entire rectangle renders, verify it is functioning as a matte source and that matte settings reference the intended layer.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 04 · Footage visible through moving text

**Compositing · Beginner · Suggested after lesson 12** — Use letters as an alpha matte.

1. Create a new composition containing video and a large text heading on separate layers.
2. Place the text as the source of the footage layer track matte (Alpha Matte).
3. Animate the text’s Position or scale so the visible video window moves across the frame.
4. Add a background solid below the video. Fade the matte text after a hold while keeping the background visible.
5. Test Alpha Inverted Matte and compare which parts of the footage show.

**Verify:** Footage is visible inside the glyphs only, without black squares.
**If it fails:** Do not mistake Screen blending for a matte.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 05 · Responsive title layout

**Animation · Beginner · Suggested after lesson 14** — Keep proportional and fixed margins distinct.

1. Duplicate a title comp before modifying its dimensions.
2. Show rulers, then add a vertical 50% guide using View → Add Guide.
3. Add a vertical 100-pixel guide referenced from the right and a horizontal bottom margin.
4. Change the duplicate’s aspect ratio and inspect guide positions; reposition artwork deliberately.
5. Export/import .guides into the other comp and verify colors, units and edges rather than assuming a round trip.

**Verify:** Center and fixed-margin guides retain their intended meanings; text is still inside the delivery frame.
**If it fails:** Guides are view-specific and do not animate or reposition layers.

**Sources:** [Adobe: Guide creation and management](https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html)

### 06 · Procedural cloud transition

**Effects · Intermediate · Suggested after lesson 15** — Combine noise, Levels and a matte reveal.

1. Create a solid with Fractal Noise and animate its Evolution/Offset Turbulence.
2. Use Levels to increase contrast so it evolves into a thresholded black/white matte.
3. Apply the resulting precomp as a Luma Matte to reveal the new scene over the old.
4. Animate Levels Input Black/White to turn a partial cloudy mask into full coverage.
5. Test consistency at full frame dimensions and inspect whether the mask reverses unintentionally.

**Verify:** Transition ends with completely visible second shot and no remaining first-shot pixels.
**If it fails:** If both pictures vanish, the luma matte direction may be inverted.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 07 · Depth-map-driven selective focus

**Effects · Intermediate · Suggested after lesson 15** — Blur one region more than another.

1. Make a grayscale gradient with bright values in intended blurred regions.
2. Apply Camera Lens Blur to a duplicate of the footage and select the depth/blur map.
3. Tune Radius and map interpretation until background blur is stronger than the subject.
4. Feather the map and inspect the transition around the subject silhouette.
5. Compare to a global Gaussian Blur and evaluate render cost.

**Verify:** Subject retains detail while distant region falls out of focus gradually.
**If it fails:** This uses a 2D blur map; for actual scene focus use the separate Advanced 3D camera DOF workflow.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 08 · Heat haze with Displacement Map

**Effects · Intermediate · Suggested after lesson 15** — Distort pixels using animated grayscale noise.

1. Make a comp-sized solid, apply Fractal Noise, choose a broad smooth scale and reduce contrast.
2. Animate Offset Turbulence slowly to make the map drift; precompose it as MAP_HEAT.
3. Apply Displacement Map to the target footage, point it to MAP_HEAT and adjust displacement strengths modestly.
4. Mask the effect region or use a matte so heat haze appears near a specific source.
5. Add small blur/color variation only where necessary; compare map on/off over time.

**Verify:** The background bends believably without an obvious repeating noise tile.
**If it fails:** A color noise map may need channel selection to avoid chaotic displacement.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 09 · Make a seamless time-remapped loop

**Animation · Intermediate · Suggested after lesson 16** — Avoid a one-frame black or phantom-frame flash.

1. Import a visibly seamless 2-second clip into a 6-second comp.
2. Enable Time Remapping and inspect initial keyframes, especially end-duration key.
3. For a source with N frames and frame duration d, keep the initial key at (0,0). Add a key at ((N-1)*d,(N-1)*d) and make its outgoing interpolation Hold. At the cycle boundary N*d set Time Remap to 0, replacing the default beyond-source value.
4. Add `loopOut('cycle')` on Time Remap, extend the layer to six seconds and compare repeated cycles frame by frame. The loop duration stays N*d, including the final source frame’s interval.
5. Check final frame and audio timing; Time Remap does not guarantee an inherently nonseamless source becomes seamless.

**Verify:** No unexpected blank, duplicate or jump frame at loop boundaries.
**If it fails:** A mathematical loop cannot conceal mismatched first/last source artwork.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 10 · Staggered cards using Quick Offset

**Animation · Intermediate · Suggested after lesson 16** — A 25.4+ timeline technique to spread entrances in time.

1. Create five shape cards stacked at the same center, each with a 10-frame Position entrance.
2. Select the intended layers in sequence, making sure selection order matches desired timing.
3. Hold Ctrl+Alt and drag the selected layer bars (Quick Offset) to distribute the group over time.
4. Inspect the earliest and latest start times; trim unwanted overlaps if necessary.
5. Preview and compare with manually offsetting keyframes only.

**Verify:** Entrances are staggered without changing each layer’s internal animation.
**If it fails:** Quick Offset changes timing. Proportional Scrubbing changes property values; Shift+[ or Shift+] moves a staggered layer selection as a group.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 11 · Animate to beats with markers

**Audio · Intermediate · Suggested after lesson 17** — Create rhythmic transitions without automatic beat-detection claims.

1. Import and listen to a clean WAV on Timeline; show waveform with LL.
2. Add comp markers manually at the actual beat transients.
3. Align keyframe entrances 2 frames before a beat or exactly on beat depending on intended impact.
4. Use F9 and Graph Editor to make 6-frame ease-out impacts and longer holds.
5. Export and listen to rendered sound, checking whether markers match perceptual onsets.

**Verify:** Every impact is perceptually synchronized in the exported movie.
**If it fails:** Waveform peak amplitude is not always the perceived musical beat.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 12 · Beat-reactive pulse

**Audio · Intermediate · Suggested after lesson 17** — Drive scale from audio-derived keyframes.

1. Import an audio file and use Convert Audio to Keyframes.
2. Select a logo and add a 2D Scale expression referencing Audio Amplitude → Both Channels Slider.
3. Use `a=thisComp.layer("Audio Amplitude").effect("Both Channels")("Slider"); s=100+Math.min(20,a*1.5); [s,s];` on 2D Scale, verifying names against your generated controller.
4. Preview with sound and observe peak reactions; smooth or cap peaks where needed.
5. Add a 10-frame opacity fade and export an audio-enabled review file.

**Verify:** Logo scales gently with the sound and never collapses during quiet segments.
**If it fails:** Array dimensionality errors cause red expression warnings.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 13 · Keylight clean screen composite

**Compositing · Intermediate · Suggested after lesson 18** — Isolate a foreground subject cleanly.

1. Place evenly lit green-screen footage above a neutral background.
2. Apply Keylight (1.2); pick a green patch as Screen Colour.
3. Select Screen Matte view, tune Clip Black and Clip White gently, then return to Final Result.
4. Add garbage mask, Key Cleaner and Advanced Spill Suppressor where useful.
5. Check edges over black, white and saturated backgrounds, and verify 10 consecutive frames.

**Verify:** Subject retains hair details without a green line or black halo.
**If it fails:** A crushed Screen Matte can erase semitransparent hair.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 14 · Tracked glowing outline

**Compositing · Intermediate · Suggested after lesson 19** — Build glow from a clean traced contour.

1. Create or track a mask path following the subject with as few stable vertices as possible.
2. Apply Generate → Stroke to a comp-sized solid and configure the path and width.
3. Precompose the stroke layer, duplicate it, blur one copy and add Glow to a duplicate.
4. Use a clean sharp core stroke above the soft bloom; tune opacities and blend modes.
5. Check motion frame by frame for outline detachment and edge aliasing.

**Verify:** One sharp line remains visible inside the blur, and outline follows subject motion.
**If it fails:** A high blur on the only stroke layer produces a mushy and poorly defined outline.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 15 · Track a title onto moving footage

**Tracking & 3D · Intermediate · Suggested after lesson 19** — Convert tracked pixels into a Null animation.

1. Import a short shot with a stable high-contrast mark and create a comp from it.
2. In Tracker choose Track Motion and place Feature and Search Regions around the mark.
3. Track forward, correcting any drift frames. Create a Null and apply the tracking data to it.
4. Parent a title layer to the Null; position the text relative to the intended feature.
5. Add an outline/background to keep the title legible and preview each frame.

**Verify:** The text follows the mark accurately for the full intended shot.
**If it fails:** A drifting null needs tracker correction; smoothing the title keys alone is not an accurate fix.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 16 · Roto Brush character cut-out

**Compositing · Intermediate · Suggested after lesson 20** — Extract a moving person without a green screen.

1. Open the subject video in Layer panel and activate Roto Brush.
2. Mark foreground and remove unwanted selected regions, starting at a good base frame.
3. Propagate through a 2-second segment, fixing errors around hands and head.
4. Use Refine Edge for hair and tune matte edge controls modestly; Freeze the result.
5. Place a background layer behind the cutout and render-check the complete segment.

**Verify:** The subject is clean on at least two contrasting backgrounds.
**If it fails:** If propagation fails, compare Object Matte, Quick Selection and Refine Edge, inspect the base frame and correct occlusions.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 17 · Remove an object using Content-Aware Fill

**Compositing · Intermediate · Suggested after lesson 21** — Generate a repair while retaining original footage.

1. Duplicate the clip and draw a mask around the unwanted object.
2. Animate/track mask and set its mode to create the intended transparent hole.
3. Open Window → Content-Aware Fill and choose suitable range and Fill Method.
4. Generate Fill Layer; inspect every frame and try a reference frame if textures are inconsistent.
5. Render and compare to source, particularly near moving occlusions and boundaries.

**Verify:** Object disappears without visible temporal pattern or seams.
**If it fails:** Content-Aware Fill may give temporally unstable texture; a clean plate may work better.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 18 · Simple camera orbit rig

**Tracking & 3D · Intermediate · Suggested after lesson 22** — Use a Null as a stable camera pivot.

1. Create a comp with three 3D solids at different depths.
2. Create a 2-node camera and an appropriately positioned 3D Null.
3. Parent the camera to the Null and animate the Null’s Y rotation 0→30 degrees.
4. Adjust camera local Position so subject stays framed; verify target/Point of Interest behavior.
5. Render in the intended 3D renderer and compare to a Position-only camera move.

**Verify:** Subject remains readable while background layers show depth shift.
**If it fails:** Incorrect pivot placement can make a camera orbit resemble uncontrolled zoom.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 19 · Parallax from a still photograph

**Tracking & 3D · Intermediate · Suggested after lesson 22** — Cut source artwork into near/mid/far planes.

1. Prepare a background image and two transparent foreground cutouts from the same photo.
2. Import each as a layer, enable 3D and spread them apart on the Z axis while preserving intended screen placement.
3. Create a camera and make a short lateral dolly/arc that reveals a depth difference.
4. Extend hidden background under the foreground silhouette to prevent holes.
5. Add subtle light/blur in the appropriate renderer and preview both camera extremes.

**Verify:** The foreground moves more than background without revealing empty cutout edges.
**If it fails:** Scaling a single flat photograph is not real parallax.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 20 · Replace a moving sign/screen

**Tracking & 3D · Intermediate · Suggested after lesson 23** — Map a replacement layer into four moving corners.

1. Choose a shot of an almost planar screen or poster with visible texture.
2. Open bundled Mocha AE from the effect integration, draw a planar region and track the shot.
3. Set/verify a planar surface with the correct corner order; transfer corner pin data using the integration available in 26.5.
4. Place a bold checkerboard into the replacement comp and inspect alignment at each frame.
5. Replace the checkerboard with the desired screen contents; match blur, exposure and noise.

**Verify:** Checkerboard corners remain anchored and final insert has no glaring seams.
**If it fails:** Perspective slippage usually indicates an unstable plane or the wrong corner calibration.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 21 · ACES 2.0 input-to-output proof

**Color & delivery · Intermediate · Suggested after lesson 24** — Make every color transform explicit.

1. Duplicate a small test project and choose Project Settings → Color → OCIO color managed.
2. Choose the pipeline-appropriate ACES 2.0 CG v4.0 or Studio v4.0 configuration.
3. Interpret a known source correctly and choose a suitable scene-linear working space such as ACEScg.
4. Set a display transform for inspection and an independent Output Module output color space for delivery.
5. Render a short image sequence, reimport with the correct interpretation and compare to the reference without double-applying a display transform.

**Verify:** Source, working, display and output transforms are recorded and the reference comparison is consistent.
**If it fails:** Do not change an established project’s configuration in place without a known-good reference.

**Sources:** [Adobe: OpenColorIO and ACES](https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html)

### 22 · Controlled RGB channel split

**Effects · Intermediate · Suggested after lesson 24** — Make an aberration effect using channel routing.

1. Precompose a source with correct alpha, then duplicate it into three layers.
2. Apply Shift Channels so each copy isolates red, green or blue, and combine with Add where appropriate.
3. Offset red slightly left and blue slightly right, leaving green centered.
4. Use a mask/adjustment where the effect should occur, rather than displacing the whole frame continuously.
5. Check seams, alpha and color clipping at Full resolution.

**Verify:** Aberration appears near high-contrast edges without introducing a giant invisible background.
**If it fails:** With alpha artwork, additive recomposition can unintentionally alter transparency.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 23 · Texture inside an Object Matte subject

**Compositing · Intermediate · Suggested after lesson 26** — Separate semantic selection from texture animation.

1. Open suitable moving footage in Layer panel and select the Object Matte toolbar tool.
2. Click the subject, refine the base selection and propagate the required span.
3. Correct occlusions and edge errors, then Freeze and inspect the silhouette over contrasting colors.
4. Add an animated texture on a separate layer and assign the isolated subject as its Alpha Matte.
5. Animate the texture independently and render a short sample, checking alpha and the whole moving edge.

**Verify:** Texture follows the subject silhouette with no one-frame holes or unrelated background.
**If it fails:** Correct the source matte before trying to hide edge problems with Glow.

**Sources:** [Adobe: AI-powered Object Matte](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html)

### 24 · Editable variable-font emphasis

**Text & data · Intermediate · Suggested after lesson 27** — Change letterform weight instead of scaling the whole layer.

1. Create a short headline in an installed variable font.
2. Choose Text → Animate → Variable Font Axes and an axis present in that font.
3. Keyframe the axis at time zero and at one second using supported values.
4. Use the Range Selector to send emphasis across characters or words.
5. Compare spacing modes and render the result at delivery size; record the font dependency.

**Verify:** Text remains editable and readable without unexpected spacing or wrapping.
**If it fails:** A static font family does not expose variable axes.

**Sources:** [Adobe: Working with Variable Font Axes](https://helpx.adobe.com/after-effects/desktop/variable-font-axes/work-with-variable-font-axes/working-with-variable-font-axes.html)

### 25 · Flowing Curl Noise reveal

**Effects · Intermediate · Suggested after lesson 28** — Use a procedural field as a controllable matte.

1. Create a comp-sized solid and apply Curl Noise with Quick Apply.
2. Begin with Internal input and adjust Scale/Swirl while keeping color simple.
3. Animate one motion control, inspecting Input Noise versus Final Render.
4. Precompose the generated field and assign it as a Luma Matte to an incoming image.
5. Animate a contrast/brightness transition to finish at complete coverage, then inspect start/end frames and the rendered cut.

**Verify:** The incoming image ends fully visible with no residual old frame.
**If it fails:** A partially bright noise field alone will not reach opaque full coverage.

**Sources:** [Adobe: Noise, grain and Curl Noise](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html)

### 26 · Black-backed element to RGBA master

**Compositing · Intermediate · Suggested after lesson 28** — Deliver alpha instead of relying on a background-specific blend.

1. Import a suitable light/smoke element with a black background and retain a source copy.
2. Apply Unmult, choose Black and inspect Alpha with Alt+4.
3. Adjust Black Level and Softness, then inspect Remove Color Matting around translucent edges.
4. Test over dark gray, white and saturated backgrounds; protect foreground black where needed.
5. Export RGB+Alpha to a suitable format and reimport over a contrasting solid to verify color and coverage.

**Verify:** Rendered alpha works over more than one background without opaque black borders.
**If it fails:** Screen mode alone does not establish a reusable alpha master.

**Sources:** [Adobe: Keying and Unmult](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html)

### 27 · JSON-driven statistics title

**Expressions & data · Advanced · Suggested after lesson 29** — Load external numbers into Source Text.

1. Create a UTF-8 JSON file with a simple `{"team":"North","score":42}` object.
2. Import it into the project and create a Source Text expression using `footage('stats.json').sourceData.score` with a valid data path.
3. Convert the numerical result to a string, label it with a title and position it inside a shape card.
4. Use `sourceRectAtTime` to auto-size card background with 20 pixels of padding.
5. Change JSON to a longer team label and verify the design remains readable.

**Verify:** Values update after reloading external data and remain properly aligned.
**If it fails:** Always check JSON syntax and exact field names.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 28 · Reusable lower third with Essential Properties

**Templates · Advanced · Suggested after lesson 30** — Separate animation from editable name/role content.

1. Build a 1920×1080 child comp with two text layers and a shape-rectangle background.
2. Place all layers under a controller Null, then animate entrance over 10 frames and exit over 10 frames.
3. Open Essential Graphics, expose name text, role text and primary fill color with descriptive labels.
4. Nest the comp twice in a master; override the name/role independently using Essential Properties.
5. Export a MOGRT after checking typography bounds and protected regions when appropriate.

**Verify:** Two independent instances show different content with the same timing and art direction.
**If it fails:** If one instance unexpectedly changes both names, you edited the shared source rather than an override.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 29 · Puppet waving flag

**Animation · Advanced · Suggested after lesson 32** — A flexible loop from a static transparent flag.

1. Import a transparent flag shape and inspect its alpha edges.
2. Add Puppet pins at fixed pole edge and on two flowing sections of fabric.
3. Animate mid and tip pins across three poses over two seconds.
4. Use stiffness controls when necessary to avoid folding the pole itself.
5. Copy the first pose to the loop end and smooth all movements.

**Verify:** Flag waves smoothly and the pole edge stays visually stable.
**If it fails:** Too many pins fight each other and create crumpling.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 30 · Native particle burst

**Effects · Advanced · Suggested after lesson 33** — A measured CC Particle World experiment.

1. Apply CC Particle World to a suitable comp-sized solid.
2. Set Birth Rate to a low visible rate and key it to 0 after the first 12 frames.
3. Set Longevity to about 2 seconds; choose a particle style and initial velocity and gravity.
4. Adjust emitter position so particles emerge from the logo center.
5. Add gentle Glow after the particle effect and preview at actual playback speed.

**Verify:** No particles are born after the burst ends, but earlier particles die naturally.
**If it fails:** Birth Rate 0 stops new particles; it does not kill those already alive.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 31 · Native mesh rack focus

**Tracking & 3D · Advanced · Suggested after lesson 35** — Render a stable 26.5 geometry and focus study.

1. Create a comp with Advanced 3D and add two native meshes at different depths.
2. Set distinct roughness/metallic values and light them with a controlled environment or supported light.
3. Create a camera and enable Camera Options → Depth of Field.
4. Set focus to the near object, then animate Focus Distance to the far object over two seconds.
5. Render in Active Camera at Full quality and inspect near/far edges and the focus transition.

**Verify:** Focus travels between real scene objects with a predictable first/middle/final frame.
**If it fails:** A custom viewer is not the final Active Camera; do not confuse Camera Lens Blur with this scene render.

**Sources:** [Adobe: Create parametric meshes](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html), [Adobe: Advanced 3D in-engine depth of field](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-3d-scene-depth-data/enable-in_engine-depth-of-field-in-advanced-3d.html)

### 32 · Transparent master and color check

**Color & delivery · Advanced · Suggested after lesson 36** — Deliver usable compositing assets.

1. Make a 48-frame comp with a moving semi-transparent circle over an empty comp background.
2. Choose Render Queue Output Module format/codec supporting alpha; set RGB+Alpha and appropriate alpha interpretation.
3. Render a lossless/near-lossless master or numbered PNG sequence with intentional color settings.
4. Import the result into a fresh comp over dark blue and hot pink backgrounds; inspect edge transparency.
5. Render a separate H.264 review file with a solid background; label it as a non-alpha review.

**Verify:** The alpha master has transparent edges, and the MP4 review is correctly labeled.
**If it fails:** An .mp4 file may look like an alpha preview in AE but will not preserve ordinary transparency.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 33 · Collect Files handoff test

**Color & delivery · Advanced · Suggested after lesson 37** — Prove that your project is portable.

1. Save the final project with descriptive version and output names.
2. Choose File → Dependencies → Collect Files and create a fresh folder that contains the project and required footage.
3. Add a README of fonts, third-party effects, scripts, LUTs and manual configuration notes.
4. Move the collected folder to a different Windows directory and reopen its project file.
5. Render a tiny proof frame; confirm it matches the pre-collection output and uses the new source paths.

**Verify:** Project reopens from collected directory and produces identical proof frames.
**If it fails:** Collect Files does not install fonts or purchase plugin licenses.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

### 34 · Final 10-second integrated sequence

**Capstone · Advanced · Suggested after lesson 40** — Practice the entire production pipeline with one coherent composition.

1. Create a 24-fps 10-second comp and organized project folders; establish color and output format.
2. Make a two-second alpha-matte animated title with a readable hold.
3. Add a three-card stagger using controlled easing and a Null; build one reusable editable title element.
4. Place either a tracked element or roto/keyed person over a short plate; inspect edges in motion.
5. Add a procedural 2-second transition and final text, synchronize audio, then render MP4 and an appropriate master.
6. Collect Files, reopen the collected project and write a self-critique of three improvements.

**Verify:** Both render and portable project exist, with no one-frame flashes or missing media.
**If it fails:** A capstone is not complete until the collected source can be reopened.

**Sources:** [Adobe: After Effects documentation index](https://helpx.adobe.com/after-effects/desktop.html)

---

## Effects encyclopedia

Orientation directory of effects and expression controls, including compatibility-only effects. Exact installation and effect parameters must be checked in AE 26.5. Adobe’s online catalog is continually updated and can also describe Beta functionality; entries labeled obsolete should not be the default for new designs.

| Effect | Category | Purpose |
|---|---|---|
| Camera Lens Blur | Blur & Sharpen | Lens-like bokeh; can use Blur Map for local/depth-varying blur, including highlights and focus control. Heavier than simple blur. |
| Gaussian Blur | Blur & Sharpen | Smooth, conventional uniform blur. Fast and reliable; repeat edge pixels if borders appear. |
| Fast Box Blur | Blur & Sharpen | Efficient box approximation; useful in matte softening, textures and previews. |
| Directional Blur | Blur & Sharpen | Linear blur along an angle; simulated speed smear/trails. |
| CC Radial Blur | Blur & Sharpen | Radial directional or zoom-streak blur based on a center; useful for impact effects. |
| CC Radial Fast Blur | Blur & Sharpen | Faster radial-style effect; fewer/other controls than standard. |
| Radial Blur | Blur & Sharpen | Older rotational/zoom radial blur option; still useful in some looks, not automatically obsolete. |
| CC Vector Blur | Blur & Sharpen | Uses vectors/texture for stylized flow-like warping/blurring. |
| Compound Blur | Blur & Sharpen | Uses a secondary layer's brightness to change blur amount across the image. |
| Channel Blur | Blur & Sharpen | Independently blurs R/G/B/A channels; potential color fringes and alpha softening. |
| Bilateral Blur | Blur & Sharpen | Smooths regions while retaining prominent edges. |
| Smart Blur | Blur & Sharpen | Smooths relatively uniform regions but attempts to protect edges. |
| Sharpen | Blur & Sharpen | Basic edge enhancement; halos appear if overdone. |
| Unsharp Mask | Blur & Sharpen | Controlled edge contrast sharpening, Amount/Radius/Threshold. |
| Camera-Shake Deblur | Blur & Sharpen | Attempts to mitigate motion-induced camera blur; may create artifacts. |
| CC Cross Blur | Blur & Sharpen | Cross-shaped/anamorphic-style blur direction. |
| CC Composite | Channel / Matte | Composites the processed result against the layer's underlying original input inside one effect pipeline; try RGB-only/alpha and blend settings when nothing seems to happen. |
| Blend | Channel / Matte | Blends the current layer with another input layer. |
| Set Matte | Channel / Matte | Pull alpha or luminance from a specified source and inject it into effect pipeline. |
| Shift Channels | Channel / Matte | Route/copy individual channels; build simple RGB split/aberration effects. |
| Set Channels | Channel / Matte | Assemble output channels from multiple source channels/layers. |
| Channel Combiner | Channel / Matte | Converts/composes color channels, including channel-to-lightness conversions. |
| Invert | Channel / Matte | Invert color values or selected channels, including alpha where chosen. |
| Minimax | Channel / Matte | Grow/shrink bright or dark regions, useful for matte expansion/erosion. |
| Remove Color Matting | Channel / Matte | Correct halo caused by premultiplication against an unwanted matte color. |
| Calculations | Channel / Matte | Combine input layer channels and mathematical/compositing operations. |
| Solid Composite | Channel / Matte | Composites layer over specified solid color within the layer bounds; useful for creating black/white map backgrounds. |
| Mocha Shape | Matte | Workflow-specific Mocha-created masks/mattes if available. |
| Keylight (1.2) | Keying | General green/blue screen chroma key with detailed Screen Matte controls. |
| Key Cleaner | Keying | Recover/clean key edges, especially fine outlines. |
| Advanced Spill Suppressor | Keying | Remove undesirable green/blue color contamination on subject edges. |
| Linear Color Key | Keying | Remove specified RGB color/range; controlled simple key. |
| Color Difference Key | Keying | Difference-based blue/green keying. |
| Color Range | Keying | Target color range; sometimes useful for selections but can be noisy. |
| Difference Matte | Keying | Remove area resembling clean background reference. |
| Extract | Keying | Use luminance thresholds to isolate bright/dark regions. |
| Inner/Outer Key | Keying | Separate inner/outer edges for difficult mattes. |
| CC Simple Wire Removal | Keying | Remove linear cables/wires across footage. |
| Color Key | Obsolete / compatibility only | Obsolete. Retained for compatibility; not mandatory in modern key workflow. |
| Lumetri Color | Color Correction | Comprehensive familiar color grading (basic, curves, color wheels, HSL secondary, vignette where available). |
| Curves | Color Correction | Precise tonal/channel mapping, matte contrast, look creation. |
| Exposure | Color Correction | Adjust photographic exposure and tonal offset; useful in higher-bit-depth workflows. |
| Hue/Saturation | Color Correction | Target hue, saturation and lightness globally or ranges. |
| Black & White | Color Correction | Tonal monochrome conversion with channel weights. |
| Brightness & Contrast | Color Correction | Basic global correction; limited compared with Curves. |
| Vibrance | Color Correction | Prioritize less-saturated color areas over skin tones in many cases. |
| Selective Color | Color Correction | Fine color-group adjustment. |
| Channel Mixer | Color Correction | Change RGB output from channel mixtures, make custom grayscale. |
| Leave Color | Color Correction | Retain one selected hue while desaturating others. |
| Colorama | Color Correction | Map luminance/phase to customizable color palette. |
| Color Link | Color Correction | Match/link colors in layer-based workflows. |
| Color Stabilizer | Color Correction | Correct fluctuating color using sample areas. |
| Equalize | Color Correction | Redistribution of intensity histogram; stylized image contrast. |
| Photo Filter | Color Correction | Warm/cool photographic filter color. |
| Shadow/Highlight | Color Correction | Recover local dark/light detail; can flatten images. |
| Gamma/Pedestal/Gain | Color Correction | Channel/tonal control using photographic video parameters. |
| PS Arbitrary Map | Color Correction | Photoshop arbitrary-map transfer function. |
| Apply Color LUT | Utility | Apply LUT transform; must use appropriate input color space to avoid bad look/double transform. |
| Color Profile Converter | Utility | Convert between color-profile spaces; distinct from simply applying a look LUT. |
| Bezier Warp | Distort / Transform | Warp whole image using edge/corner Bézier mesh handles; useful for cloth/smoke edges. |
| Mesh Warp | Distort / Transform | Fine multi-cell deformation; more localized control. |
| Liquify | Distort / Transform | Brush deformation/mesh for facial distortions, fire, organic visuals. |
| Displacement Map | Distort / Transform | Another layer's brightness/color shifts pixels horizontally/vertically; depth-map illusion, water, ripples. |
| Transform | Distort / Transform | Effect-order-aware extra transform; better than moving an entire layer when you need transform between effects. |
| Turbulent Displace | Distort / Transform | Organic bubbling/wavy displacement; great for smoke, fire, animated drawn art. |
| Wave Warp | Distort / Transform | Directional sine-wave fabric/hair/flag/river motion; Pinning controls where waves are suppressed. |
| Warp | Distort / Transform | Preset-type arcs, bulges, flags, fisheye and other deformable shapes. |
| CC Bend It | Distort / Transform | Bend along points, fast for organic/tube bends. |
| CC Bender | Distort / Transform | Bend based on bounding region with different behavior/controls. |
| CC Blobbylize | Distort / Transform | Glossy melted/liquid-like blobby shapes; useful for fluid motion design. |
| CC Flo Motion | Distort / Transform | Localized distortions around two control points. |
| CC Griddler | Distort / Transform | Grid-based segmentation/deformation. |
| CC Lens | Distort / Transform | Bulging/refracting lens distortion. |
| CC Page Turn | Distort / Transform | Flip/curl page. |
| CC Power Pin | Distort / Transform | Pin four corners of footage to a changing quadrilateral; screen replacement. |
| Corner Pin | Distort / Transform | Four-corner pinning; simpler option, still valid, not universally obsolete. |
| CC Ripple Pulse | Distort / Transform | Dynamic ripples that usually need animated Pulse/Amplitude values. |
| CC Slant | Distort / Transform | Skew/slant geometry. |
| CC Tiler | Distort / Transform | Copies a layer in tiles for infinite-space visual patterns. |
| Mirror | Distort / Transform | Reflect content across adjustable line. |
| Offset | Distort / Transform | Wrap image as it moves; seamless scrolling backgrounds. |
| Optics Compensation | Distort / Transform | Fisheye / undistort lens geometry; Reverse Lens Distortion changes direction. |
| Polar Coordinates | Distort / Transform | Rectangle↔polar map (tunnels/planet rings/clock-like effects). |
| Reshape | Distort / Transform | Morph one drawn silhouette toward another using masks. |
| Ripple | Distort / Transform | Water-surface-style waves. |
| Rolling Shutter Repair | Distort / Transform | Correct skew/wobble artifacts from rolling-shutter cameras. |
| Twirl | Distort / Transform | Twist pixels around center. |
| Warp Stabilizer | Distort / Transform | Automatic image stabilization; separate from intentionally creative warp. |
| Detail-preserving Upscale | Distort / Transform | More edge-aware scaling than simple magnification; evaluate fine details/halos. |
| 4-Color Gradient | Generate | Four-point color interpolation, useful backgrounds. |
| Gradient Ramp | Generate | Linear/radial gradient from start to end control points. |
| Grid | Generate | Draw a grid, useful graphical background or to diagnose warp. |
| Lens Flare | Generate | Simulated flare based on a point in the frame. |
| Radio Waves | Generate | Expanding rings/ripples; great for motion graphics. |
| Scribble | Generate | Animated scribble lines in masked regions. |
| Stroke | Generate | Render one or more mask paths with animated Start/End; glows/outlined drawings. |
| Vegas | Generate | Animated outlines/highlights using mask/contour paths. |
| Write-on | Generate | Frame-accumulating paint-like writing. |
| Fractal Noise | Noise & Grain | Rich coherent noise. Animate Evolution/Offset Turbulence, transform for scale, use Evolution Options for cycle where supported. |
| Turbulent Noise | Noise & Grain | Related procedural pattern with different rendering/performance/features; not “always faster” in every project. |
| Noise | Noise & Grain | Pixel-level random texture/dither/grain. |
| Dust & Scratches | Noise & Grain | Remove small specks or produce painterly smoothing at high values. |
| Noise Alpha | Noise & Grain | Randomize transparency. |
| CC Particle World | Simulation | 3D-like particle generator with birth rate, producer, physics, particle type. |
| CC Particle Systems II | Simulation | Simpler particle bursts/trails. |
| Particle Playground | Simulation | Rich older multi-input particle system, more configuration. |
| CC Ball Action | Simulation | Turns input into grids of balls—great for scattering/reforming graphics. |
| CC Pixel Polly | Simulation | Shatters source pixels/regions as simulated chunks. |
| Shatter | Simulation | Break objects apart with forces/debris/camera. |
| CC Mr. Mercury | Simulation | Viscous liquid-like emitted blobs/droplets. |
| Foam | Simulation | Bubble simulation from flow/birth parameters. |
| CC Bubbles | Simulation | Floating/refractive bubbles sampling underlying image appearance. |
| CC Drizzle | Simulation | Droplet surface ripples. |
| CC Hair | Simulation | Bundled hair/strand simulation effect. |
| CC Scatterize | Simulation | Scatter/fragment look. |
| CC Star Burst | Simulation | Starfield/travel visual. |
| Card Dance | Simulation | Animate source as discrete cards driven by control map. |
| Caustics | Simulation | Light refraction patterns through water/glass simulation. |
| Wave World | Simulation | Generated simulated rippling water surfaces, usable as effect map. |
| Glow | Stylize | Bloom around bright areas; threshold/radius/intensity control. |
| Find Edges | Stylize | Outline high-contrast boundaries, optionally invert/colorize. |
| CC Vignette | Stylize | Dark/light edge vignette. |
| Roughen Edges | Stylize | Organic irregular alpha edge, strong for paper/smoke/mattes. |
| Mosaic | Stylize | Pixel-block mosaic. |
| Posterize | Stylize | Reduce color levels; not frame rate. |
| Strobe Light | Stylize | Timed flashes/strobes. |
| CC Force Motion Blur | Time | Extra blur samples for moving operations; cost may be high. |
| Pixel Motion Blur | Time | Optical flow-like blur between frames. |
| Posterize Time | Time | Lower sampling rate for stop-motion look. |
| Time Difference | Time | Highlights changes between frames. |
| Time Displacement | Time | Grayscale layer controls relative source time per pixel. |
| Timewarp | Time | Retimes source with frame interpolation. |
| 3D Channel Extract | 3D Channel | Extract supported depth or channel data from imported 3D render passes. |
| Cryptomatte | 3D Channel | Build anti-aliased object or material mattes from cryptomatte data in EXR sources. |
| Depth Matte | 3D Channel | Use depth-pass information to define transparency based on distance. |
| Depth of Field | 3D Channel | Use 3D-channel depth data to simulate optical defocus in a composited pass; not the 26.3 Advanced 3D renderer feature. |
| Extractor | 3D Channel | Extract supported image/channels from floating point render passes. |
| Fog 3D | 3D Channel | Use depth data to create depth-dependent haze. |
| ID Matte | 3D Channel | Isolate regions based on ID channels where present. |
| IDentifier | 3D Channel | Generate masks from supported ID-style 3D channels. |
| Backwards | Audio | Reverses the sound playing in a layer. |
| Bass & Treble | Audio | Change broad high and low frequency content. |
| Delay | Audio | Repeat and offset audio to make echoes. |
| Flange & Chorus | Audio | Create short modulated delays for widened/chorused sound. |
| High-Low Pass | Audio | Filter out low or high-frequency content. |
| Modulator | Audio | Change audio with time-varying modulation. |
| Parametric EQ | Audio | Set targeted boost/cut frequencies and bandwidth. |
| Reverb | Audio | Simulate acoustic reflections and room tails. |
| Stereo Mixer | Audio | Adjust stereo channel balance and routing. |
| Tone | Audio | Generate a simple test/audio tone. |
| Fill | Generate | Replace output pixels with selected solid color while respecting alpha. |
| Circle | Generate | Generate a configurable circular shape/effect. |
| Beam | Generate | Draw a beam between two adjustable points. |
| Advanced Lightning | Generate | Generate electrical branching patterns between points. |
| Audio Spectrum | Generate | Turn audio frequency energy into animated frequency bars/lines. |
| Audio Waveform | Generate | Draw the audio waveform as visible pixels. |
| CC Light Rays | Generate | Emit stylized rays from a source point. |
| CC Light Burst 2.5 | Generate | Simulate a radial burst of light. |
| CC Light Sweep | Generate | A moving specular highlight over existing pixels. |
| CC Threads | Generate | Generate thread-like organic motion. |
| CC Glue Gun | Generate | Produce organic liquid-like extrusions. |
| Paint Bucket | Generate | Fill pixels by a sampled color range. |
| Levels | Color Correction | Set input/output black, white and gamma response per channels. |
| Tint | Color Correction | Map black and white regions to two chosen colors. |
| Tritone | Color Correction | Map shadows, midtones and highlights to three colors. |
| Auto Color | Color Correction | Estimate image-wide automatic channel balancing. |
| Auto Contrast | Color Correction | Adjust tonal contrast automatically. |
| Auto Levels | Color Correction | Set channel levels automatically. |
| Change Color | Color Correction | Alter a sampled color within a controllable tolerance. |
| Change to Color | Color Correction | Replace a selected color while retaining selected image variations. |
| Color Balance | Color Correction | Adjust channel balance and tonal colors. |
| Color Balance (HLS) | Color Correction | Adjust hue, lightness and saturation globally. |
| CC Color Neutralizer | Color Correction | Neutralize color casts using its controls. |
| CC Color Offset | Color Correction | Offset image color channels. |
| CC Toner | Color Correction | Map tone values to a set of colors. |
| CC Kernel | Color Correction | Apply a convolution kernel to image channels; inspect changes on an edge/grid test. |
| CC Sphere | Perspective | Map a 2D image around a sphere with shading controls; it does not create true 3D geometry. |
| CC Cylinder | Perspective | Wrap a 2D image on a faux cylinder. |
| Drop Shadow | Perspective | Cast a simple offset/blurred 2D shadow from layer alpha. |
| Radial Shadow | Perspective | Project a shadow away from a point source. |
| Bevel Alpha | Perspective | Give alpha edges a beveled light look. |
| Bevel Edges | Perspective | Relief on image edges. |
| CC Glass | Stylize | Use a bump map to create refractive/glass-like surface texture. |
| CC Spotlight | Perspective | Simulate a 2D spotlight effect. |
| Linear Wipe | Transition | Reveal one image in a straight advancing line. |
| Radial Wipe | Transition | Radial clock-like wipe with a center. |
| Venetian Blinds | Transition | Alternating bands with angle and completion. |
| Gradient Wipe | Transition | Transition through the luminance of a chosen gradient map. |
| Block Dissolve | Transition | Reveal or hide an image in random blocks. |
| Card Wipe | Transition | Flip or transform a grid of image cards. |
| CC Jaws | Transition | Jaw-like geometric wipe. |
| CC Grid Wipe | Transition | Reveal over a grid pattern. |
| CC Scale Wipe | Transition | Transition by scaling pattern. |
| CC Light Wipe | Transition | Wipe with lighting-like boundary glow. |
| CC Glass Wipe | Transition | Distort and reveal with glass-like refraction. |
| CC Twister | Transition | Spiral/twist transition. |
| CC Image Wipe | Transition | Reveal based on an image source. |
| Magnify | Distort / Transform | Enlarge a local region, like a moving lens. |
| Spherize | Distort / Transform | Warp pixels around a center into spherical distortion. |
| CC Smear | Distort / Transform | Smear pixels around source/target points. |
| CC Split | Distort / Transform | Split and separate part of an image. |
| CC Split 2 | Distort / Transform | Second variant of an image splitting distortion. |
| CC Kaleida | Stylize | Create kaleidoscopic repeated reflection. |
| Add Grain | Noise & Grain | Add controllable film-like grain using sampled or chosen settings. |
| Match Grain | Noise & Grain | Match grain texture to a sampled source. |
| Remove Grain | Noise & Grain | Reduce film grain and noise while preserving some details. |
| Median | Noise & Grain | Median neighborhood filter for noise reduction/stylization. |
| Noise HLS | Noise & Grain | Add noise in hue/lightness/saturation terms. |
| Noise HLS Auto | Noise & Grain | Automatically vary hue/lightness/saturation noise. |
| Median (Legacy) | Noise & Grain | Older median filter kept for older projects. |
| Matte Choker | Matte | Reduce/expand an alpha matte with detail-sensitive parameters. |
| Simple Choker | Matte | Quick alpha-edge shrink/grow. |
| Refine Hard Matte | Matte | Improve hard-edge matte contours. |
| Refine Soft Matte | Matte | Improve translucent and soft matte edges. |
| CC Burn Film | Stylize | Simulate old film burn marks. |
| CC Plastic | Stylize | Relief/plastic appearance using source luminance as surface information. |
| Emboss | Stylize | Convert edges into a relief-like rendered surface. |
| Color Emboss | Stylize | Emboss detail while retaining source colors. |
| Motion Tile | Stylize | Repeat and mirror pixels beyond layer edges. |
| CC RepeTile | Stylize | Repeat pixels outside layer dimensions. |
| Threshold | Stylize | Reduce an image into black/white based on brightness. |
| Scatter | Stylize | Distribute pixels randomly by an amount. |
| CC Threshold | Stylize | High-contrast threshold visual effect. |
| Cineon Converter | Utility | Convert to/from supported Cineon log film-style encodings. |
| HDR Compander | Utility | Compress/expand HDR-like pixel dynamic range for certain pipelines. |
| Grow Bounds | Utility | Expand a layer effect buffer before later processing. |
| 3D Point Control | Expression Controls | User-facing X/Y/Z controller; link an expression to its 3D value for reusable rigs. |
| Angle Control | Expression Controls | Single angle property that an expression can read from a controller layer. |
| Checkbox Control | Expression Controls | Boolean-like 0/1 property for on/off choices in expressions. |
| Color Control | Expression Controls | Choose an RGBA color for other expressions or effect settings. |
| Dropdown Menu Control | Expression Controls | Named menu options for expression-driven choices; check item indexes and names. |
| Layer Control | Expression Controls | Store a reference to a specific project layer for expression links. |
| Point Control | Expression Controls | Two-dimensional XY control, useful for center and position-driven expressions. |
| Slider Control | Expression Controls | Single numeric parameter for shared animation control; rename the control for clarity. |
| CC Rainfall | Simulation | Procedural animated rainfall with controls for amount, size, speed and variation. |
| CC Snowfall | Simulation | Procedural animated snow; adjust particle visibility and movement carefully. |
| 3D Camera Tracker | Perspective | Analyzes a moving shot and solves a 3D camera/track points for scene integration. |
| 3D Glasses | Perspective | Combines stereo left/right views for stereoscopic displays and preview workflows. |
| CC Environment | Perspective | Maps an image around a scene or object; belongs to the Perspective effects family. |
| Cell Pattern | Generate | Generates cellular structures; useful for procedural maps and organic transitions. |
| Checkerboard | Generate | Generates a configurable checkerboard with cell and color controls. |
| Ellipse | Generate | Creates an adjustable elliptical region without a separate shape layer. |
| Eyedropper Fill | Generate | Fills a layer using a sampled source color. |
| Fractal | Generate | Generates a fractal design; distinct from Fractal Noise in Noise & Grain. |
| Brush Strokes | Stylize | Stylizes the picture as short brush marks, with controllable direction and length. |
| Cartoon | Stylize | Simplifies tonal detail and enhances edges to achieve a stylized illustrated result. |
| CC Block Load | Stylize | Creates block-based moving pixel patterns and digital transitions. |
| CC HexTile | Stylize | Applies a hexagonal tile/kaleidoscopic arrangement. |
| CC Mr. Smoothie | Stylize | Smooths/stylizes the source into large shaped color regions. |
| CC Threshold RGB | Stylize | Thresholds component channels independently for unusual posterized/color effects. |
| Texturize | Stylize | Uses one layer as a texture map to alter another layer’s perceived relief. |
| CC Wide Time | Time | Blends a range of temporal samples to create time-based motion trails. |
| Echo | Time | Accumulates frames at temporal offsets; useful for trails and layered motion. |
| Numbers | Text | Legacy effect for generating formatted numeric values; compare with modern text and expressions. |
| Timecode | Text | Generates a visible timecode readout on a layer for review/burn-ins. |
| CC Line Sweep | Transition | Line-like animated wipe with adjustable direction and edge behavior. |
| CC Radial ScaleWipe | Transition | Radial wipe distortion with scaling behavior. |
| CC WarpoMatic | Transition | Animated warped transition between two looks. |
| Iris Wipe | Transition | Opens or closes an iris-shaped reveal. |
| CC Overbrights | Utility | Helps visualize or handle values outside normal display range in high-dynamic-range work. |
| HDR Highlight Compression | Utility | Compresses high-range highlights for certain HDR processing pipelines. |
| Arithmetic | Channel | Arithmetic operations on image channels; use with care, especially at high bit depth. |
| Compound Arithmetic | Channel | Combines two images through channel arithmetic operations. |
| Bulge | Distort | Creates adjustable spherical magnification/distortion within the image. |
| Smear | Distort | Smears an image region using interactive path-like distortion. |
| VR Blur | Immersive Video | Blur tailored to 360°/VR imagery; mindful of equirectangular seams. |
| VR Chromatic Aberrations | Immersive Video | Spherical-aware channel separation for VR footage. |
| VR Color Gradients | Immersive Video | Gradients designed for 360° panoramic images. |
| VR Converter | Immersive Video | Converts or reorients 360°/VR projection formats. |
| VR De-Noise | Immersive Video | Reduces noise in spherical panoramic footage. |
| VR Digital Glitch | Immersive Video | Glitch artifacts within VR-friendly image transforms. |
| VR Fractal Noise | Immersive Video | Generates fractal noise across VR projections. |
| VR Glow | Immersive Video | Glow effect designed to respect 360° projections. |
| VR Plane to Sphere | Immersive Video | Projects a planar image onto a 360° sphere representation. |
| VR Rotate Sphere | Immersive Video | Reorients a spherical panorama. |
| VR Sharpen | Immersive Video | Sharpens VR imagery while addressing panoramic continuity. |
| VR Sphere to Plane | Immersive Video | Projects a section of spherical footage to a flat plane. |
| Basic 3D | Obsolete / compatibility only | Compatibility effect for old projects; prefer modern 3D layer workflows. |
| Basic Text | Obsolete / compatibility only | Legacy text-generation effect; use native Text layers for new designs. |
| Gaussian Blur (Legacy) | Obsolete / compatibility only | Legacy blur retained for project compatibility; prefer current Gaussian Blur. |
| Lightning | Obsolete / compatibility only | Old lightning generator; Advanced Lightning is the more capable common alternative. |
| Luma Key | Obsolete / compatibility only | Legacy luminance keyer; prefer modern keying and track-matte workflows. |
| Path Text | Obsolete / compatibility only | Legacy text-on-path effect; prefer native Text Path Options. |
| Reduce Interlace Flicker | Obsolete / compatibility only | Legacy filter for older interlaced footage; assess modern source handling first. |
| Spill Suppressor | Obsolete / compatibility only | Legacy spill removal; prefer Advanced Spill Suppressor when suitable. |
| Unmult | Keying | Create alpha from a black or white backing; set Background Color, level and Softness, then inspect translucent edges. |
| Curl Noise | Noise & Grain | Generate flowing 2D texture; separate scale/swirl from drift/evolution, then use it as imagery or a signal map. |
| Compressor | Audio | Reduce peaks above Threshold with Ratio and timing controls; compare bypass at matched loudness. |
| Gate | Audio | Attenuate quiet passages; tune Threshold, Hold and Release to preserve word endings. |
| Distortion | Audio | Drive/saturate sound, blend with Mix and compensate Volume; inspect clipping in rendered audio. |
| Object Matte | Tool-generated matte processing | Generated controls from the Object Matte tool; select/refine/propagate in Layer panel, then Freeze. Not a conventional generator applied to a solid. |
| Levels (Individual Controls) | Color Correction | Levels with separately addressable controls. |
| Broadcast Colors | Color Correction | Limit legacy broadcast signal ranges; use the deliverable’s actual specification. |
| Video Limiter | Color Correction | Constrain output levels according to delivery requirements. |
| Mocha AE | Boris FX Mocha | Bundled planar tracking integration; Mocha Pro is separate. |
| CINEWARE | CINEMA 4D integration | Render imported Cinema 4D scenes through its installed integration; separate from choosing the composition renderer. |
| OCIO File Transform | Color Correction | Apply a supported LUT/CDL through OCIO. |
| OCIO Color Space Transform | Color Correction | Convert configured input/output color spaces. |
| OCIO Display Transform | Color Correction | Apply a configured display/view transform; avoid duplicating the project output transform. |
| OCIO Look Transform | Color Correction | Apply a configured look with intentional input/output spaces. |

---

## Windows shortcuts

These are task-oriented Windows shortcuts, gestures and contextual actions. They can be remapped; panel focus matters. Confirm with Edit → Keyboard Shortcuts (`Ctrl+Alt+'`).

| Task | Windows binding / gesture | Context and note |
|---|---|---|
| New project | `Ctrl+Alt+N` | New, empty `.aep` |
| Open project | `Ctrl+O` | Open `.aep` / project |
| Open most recent project | `Ctrl+Alt+Shift+P` | Recents |
| Save project | `Ctrl+S` | Save often |
| Save As | `Ctrl+Shift+S` | Separate copy/name |
| Increment and Save | `Ctrl+Alt+Shift+S` | Versioned iterative save |
| New composition | `Ctrl+N` | A new scene and timeline |
| Composition Settings | `Ctrl+K` | Selected/active comp |
| New composition from selection | `Alt+\` | Selected footage/items |
| Project Settings | `Ctrl+Alt+Shift+K` | Color, renderer-related project controls |
| New folder in Project panel | `Ctrl+Alt+Shift+N` | Folder in project hierarchy |
| Import file/sequence | `Ctrl+I` | Choose asset |
| Import multiple files/sequences | `Ctrl+Alt+I` | Multi-file importer |
| Edit original source | `Ctrl+E` | Open associated app |
| New solid | `Ctrl+Y` | Color solid/blank canvas |
| Edit selected solid/light/camera/null/adjustment settings | `Ctrl+Shift+Y` | Type-specific settings |
| New adjustment layer | `Ctrl+Alt+Y` | Effects affect composited pixels below |
| New null object | `Ctrl+Alt+Shift+Y` | Parenting and controllers |
| New text layer | `Ctrl+Alt+Shift+T` | May be context-dependent while editing text |
| Precompose selection | `Ctrl+Shift+C` | Nest in child comp |
| Trim comp to work area | `Ctrl+Shift+X` | Changes composition duration |
| Work area from selected layer span, or full comp if none | `Ctrl+Alt+B` | Quick range reset |
| Add comp to Render Queue | `Ctrl+Shift+/` (main keyboard) | `/` is slash, not numpad divide |
| Add comp to Adobe Media Encoder | `Ctrl+Alt+M` | Encoding queue |
| Render current frame via Render Queue | `Ctrl+Alt+S` | Still frame |
| Keyboard Shortcut Editor | `Ctrl+Alt+'` | Remap a command |
| Preferences | `Ctrl+Alt+;` | Semicolon, not apostrophe |
| Purge all memory | `Ctrl+Alt+/` (Num) | Discards caches; may require recaching |
| Quit AE | `Ctrl+Q` | Save work first |
| Undo / Redo | `Ctrl+Z` / `Ctrl+Shift+Z` | Standard edit history |
| Select all / Deselect all | `Ctrl+A` / `F2` or `Ctrl+Shift+A` | Current active context |
| Rename selected item | `Enter` (main keyboard) | Selected layer, effect, comp, project folder, mask |
| Open selected item | `Enter` (Num) | Unlike main Enter |
| Duplicate selected item | `Ctrl+D` | Works on layer, mask, effect, property group, project items |
| Cut / Copy / Paste | `Ctrl+X` / `Ctrl+C` / `Ctrl+V` | Context-sensitive |
| Paste layers at current time | `Ctrl+Alt+V` | Timeline-specific paste |
| Open Composition Mini-Flowchart | `Tab` | Active composition and its hierarchy; Project Flowchart uses `Ctrl+F11`. |
| Project panel search | `Ctrl+F` with Project focus | With Timeline focus searches Timeline instead |
| Display source frame filename in Info panel | `Ctrl+Alt+E` | At current time |
| Stop running script | `Esc` | Interrupt execution where supported |
| Project panel | `Ctrl+0` |  |
| Render Queue panel | `Ctrl+Alt+0` |  |
| Tools panel | `Ctrl+1` |  |
| Info panel | `Ctrl+2` | Pixel samples, cursor coords and durations |
| Preview panel | `Ctrl+3` | Work area, frame skipping, audio |
| Audio panel | `Ctrl+4` |  |
| Effects & Presets | `Ctrl+5` |  |
| Character | `Ctrl+6` |  |
| Paragraph | `Ctrl+7` |  |
| Paint | `Ctrl+8` |  |
| Brushes | `Ctrl+9` |  |
| Effect Controls for selected layer | `F3` or `Ctrl+Shift+T` | Direct control panel |
| Project Flowchart | `Ctrl+F11` | Distinct from mini-flowchart |
| Assigned workspaces | `Shift+F10/F11/F12` | If workspace presets configured |
| Close all viewers of active type / active panel | `Ctrl+Shift+W` | Can close multiple timelines |
| Split a viewer (opposite lock state) | `Ctrl+Alt+Shift+N` | Lock one viewer for side-by-side comparisons |
| Maximize panel under mouse | `` ` `` | Grave/backtick above Tab; tap again to restore |
| Resize application window to fit screen | `Ctrl+\` | Not true OS-exclusive fullscreen |
| Move window to main monitor / fit | `Ctrl+Alt+\` |  |
| Switch focus between Comp and Timeline | `\` | No Ctrl |
| Previous/next open item in viewer | `Shift+,` / `Shift+.` |  |
| Previous/next panel in same frame | `Alt+Shift+,` / `Alt+Shift+.` |  |
| Show Switches/Modes columns | `F4` | Needed for matte and blending controls |
| Show/hide Parent column | `Shift+F4` | Parent & Link |
| Timeline search | `Ctrl+F` with Timeline focus | Type part of a property/effect/layer name |
| Expand/collapse selected layer completely | Ctrl + backtick (`Ctrl` + `` ` ``) | Backtick character |
| Expand nested property group recursively | `Ctrl+click` disclosure triangle | Contextual |
| Hide a visible property or group | `Alt+Shift+click` property/group name | Not Ctrl+Alt+Shift+click |
| Scroll top selected layer to top of timeline | `X` | Does not change stacking order |
| Toggle color display management in active view | `Shift+/` (Num) | Display only, not file conversion |
| Selection | `V` | Default move/selection |
| Hand | `H` | Pan viewer |
| Hand momentarily | Hold `Space` / middle mouse | During most drawing/editing |
| Zoom In | `Z` | Alt while active temporarily zooms out |
| Rotation | `W` | Rotate in viewer |
| Pan Behind (Anchor Point) | `Y` | Shift pivot while preserving visual placement |
| Rectangle/Rounded Rectangle/Ellipse/Polygon/Star | `Q` repeated | Cycle modes |
| Pen/Mask Feather | `G` repeated | Preferences can change cycling behavior |
| Horizontal/Vertical Type | `Ctrl+T` repeated | Activates text tool; text-area vs point-text depends on dragging/clicking |
| Brush/Clone Stamp/Eraser | `Ctrl+B` repeated | All paint *in Layer viewer* |
| Puppet tools | `Ctrl+P` repeated | Pin, starch, overlap etc. as available |
| Camera tools | `C` repeated | Camera context determines available tools |
| Temporarily use Selection from Pen | Hold `Ctrl` | With Pen selected |
| Temporarily edit path from Selection | Hold `Ctrl+Alt` over path | Can select/add/convert vertices |
| Temporarily duplicate shape | Hold `Alt` with selection tool | Shape context |
| Temporarily direct-select shape | Hold `Ctrl` with selection tool | Shape context |
| Use a single-letter tool temporarily | Hold its tool key, then release | Returns to the previous tool; tap to select it persistently. |
| Cycle tool variations | `Alt+click` tool icon | Some groups only |
| Go forward one frame | `Page Down` or `Ctrl+Right` | Not Alt+Right (moves keyframes) |
| Go backward one frame | `Page Up` or `Ctrl+Left` |  |
| Go ±10 frames | `Shift+Page Down/Up` or `Ctrl+Shift+Right/Left` |  |
| Beginning/end of composition | `Home` / `End` | Or `Ctrl+Alt+Left/Right` |
| Beginning/end of work area | `Shift+Home` / `Shift+End` |  |
| Next/previous visible timeline item | `K` / `J` | Visible keys/markers and work-area boundaries; Layer-view roto spans add relevant boundaries/base frames. |
| Layer in/out | `I` / `O` | With multiple layers: earliest In / latest Out. |
| Next/previous layer in/out (any layer) | `Ctrl+Alt+Shift+Right/Left` |  |
| Scroll Timeline to current time | `D` | Center current-time region |
| Jump to a particular time | `Alt+Shift+J` | Enter timecode/time |
| Work area start / end at playhead | `B` / `N` | Independent of layer in/out |
| Work area from selected layers / comp | `Ctrl+Alt+B` | Start/end bounds |
| Start/stop playback | `Space`, `Shift+Space` or `Num 0` | Preview panel controls caching/looping |
| Audio-only preview from playhead | `Num .` | Numpad decimal |
| Audio-only preview work area | `Alt+Num .` |  |
| Preview alternate-frame count | `Alt+Num 0` | Preview prefs govern count |
| Navigate keys/markers of selected layers/properties | `Shift+J` / `Shift+K` | Previous / next within the selection. |
| Snap playhead during a drag | `Shift+drag` CTI | Snaps to eligible keys/markers. |
| Manual audio scrubbing | `Ctrl+drag` current-time indicator | Audio scrub |
| Snapshot to slot 5–8 | `Shift+F5` … `Shift+F8` | Four snapshot slots |
| Display snapshot slot 5–8 | `F5` … `F8` | Compare frames |
| Purge snapshot slot 5–8 | `Ctrl+Shift+F5` … `Ctrl+Shift+F8` |  |
| Zoom Timeline IN/OUT | `=` / `-` (main keyboard) | Time magnification |
| Timeline magnification toggle | `;` | One-frame units ↔ composition extent |
| Show entire Timeline duration | `Shift+;` | Toggle previous view |
| Viewer zoom IN/OUT | `.` / `,` (main keyboard) | Not period = audio preview |
| Viewer at 100% | `/` (main keyboard) | Pixel-level review |
| Fit viewer to panel | `Shift+/` (main keyboard) | `?` on US layout |
| Fit viewer, cap at 100% | `Alt+/` (main keyboard) | Useful for quality review |
| Center comp in viewer | Double-click Hand tool |  |
| Stop viewer render while changing timeline | `Caps Lock` | Must turn OFF to judge visuals |
| Comp full/half/custom preview resolution | `Ctrl+J` / `Ctrl+Shift+J` / `Ctrl+Alt+J` | Resolution dropdown |
| Fast Previews: Off | `Ctrl+Alt+1` |  |
| Fast Previews: Adaptive Resolution | `Ctrl+Alt+2` |  |
| Fast Previews: Draft | `Ctrl+Alt+3` |  |
| Fast Previews: Fast Draft | `Ctrl+Alt+4` |  |
| Fast Previews: Wireframe | `Ctrl+Alt+5` |  |
| Mercury Transmit preview | `Num /` | External monitor output |
| Select next / previous layer in stack | `Ctrl+Down` / `Ctrl+Up` | Panel must be Timeline |
| Extend layer selection downward/upward | `Ctrl+Shift+Down` / `Ctrl+Shift+Up` |  |
| Select layer number 1–999 | Type its number on numpad | Fast entry for 2–3 digits |
| Add/remove numbered layer to selection | `Shift`+numpad number |  |
| Deselect layers | `F2` / `Ctrl+Shift+A` |  |
| Move selected layer backward/forward ONE layer in stack | `Ctrl+Alt+Down/Up` | Affects compositing order, not time |
| Move layer(s) to bottom/top of stack | `Ctrl+Alt+Shift+Down/Up` |  |
| Duplicate layers | `Ctrl+D` | Does not advance time |
| Move entire layer bar so IN starts at playhead | `[` | Preserves layer span |
| Move entire layer bar so OUT ends at playhead | `]` | Preserves layer span |
| Trim start to playhead | `Alt+[` | Does not move rest of layer |
| Trim end to playhead | `Alt+]` | Does not move rest of layer |
| Shift whole layer ±1 frame | `Alt+Page Up/Down` | Distinct from keyframe nudge |
| Shift whole layer ±10 frames | `Alt+Shift+Page Up/Down` |  |
| Move layer IN to start of comp | `Alt+Home` | Align full layer start |
| Move layer OUT to comp end | `Alt+End` | Align full layer end |
| Split at playhead | `Ctrl+Shift+D` | Splits selected layers; with none selected, splits all eligible layers. |
| Reverse layer(s) in time | `Ctrl+Alt+R` | Time → Time-Reverse Layer |
| Enable Time Remapping | `Ctrl+Alt+T` | Source-time keyframes; works with time-based layers, incl. footage/precomp |
| Precompose | `Ctrl+Shift+C` | Choosing *Move all attributes* vs *Leave all attributes* matters |
| Lock selected layers | `Ctrl+L` | Prevent accidental edits |
| Unlock all layers | `Ctrl+Shift+L` | Unlocks all, not a subset |
| Toggle selected layer's video switch | `Ctrl+Alt+Shift+V` | Eye, not effects switch |
| Disable other solo switches | `Alt+click` Solo | Efficient isolation |
| Toggle Switches/Modes | `F4` | Reveals TrkMat and blending mode |
| Cycle blending modes | `Shift+-` / `Shift+=` | Selected layers |
| Find in Timeline | `Ctrl+F` | Property/layer search |
| Show/hide Parent & Link column | `Shift+F4` |  |
| Quality: Best / Draft / Wireframe | `Ctrl+U` / `Ctrl+Shift+U` / `Ctrl+Alt+Shift+U` | Affects layer sampling/quality |
| Sampling: Bilinear / Bicubic | `Alt+B` / `Alt+Shift+B` | Visual resampling method |
| Quick Offset (25.4+) | Ctrl+Alt+drag selected layer bars or selected keyframes | Distributes them across time in selection order; first selection stays in place |
| Sequence Layers | `Animation → Keyframe Assistant → Sequence Layers` | Arrange sequentially; optionally overlap |
| Time-Reverse Keyframes | `Animation → Keyframe Assistant → Time-Reverse Keyframes` | Reverses selected keyframes, not source layer |
| Reverse Paste Keyframes | `Ctrl+Shift+V` | Paste previously copied keyframes in reverse order |
| Anchor Point / point of interest | `A` | Pivot |
| Position | `P` | Position in comp/parent space |
| Scale | `S` | x/y(/z) percentages |
| Rotation / Orientation | `R` | Z, plus 3D values if enabled |
| Opacity / light Intensity | `T` | Transparency |
| Audio Levels | `L` | dB gain |
| Audio waveform | `LL` | Drawn waveform |
| Time Remap | `RR` | Requires remapping enabled |
| Effect group | `E` | All applied effects |
| Expression-bearing properties | `EE` | Property with expression, enabled or modified |
| Keyframed properties | `U` | Properties with keyframes |
| Modified properties | `UU` | Changed-from-default settings, including effects |
| Masks | `MM` | All mask groups |
| Mask path | `M` | Paths only |
| Mask feather | `F` | Feather only |
| Mask opacity | `TT` | Opacity for masks |
| Material options (3D) | `AA` | Surface/material settings |
| Paint/Puppet/Roto strokes | `PP` | Deformation/paint details |
| Missing effects | `FF` | Locate unavailable effects |
| Selected properties/groups only | `SS` | Isolate selected parameters in timeline |
| Multiple sets of reveal shortcuts | `Shift+P` etc. | Add/remove without collapsing the rest |
| Add/remove keyframe on a revealable property at current time | `Alt+Shift+P/S/R/T/A` etc. | Does not require opening stopwatch; must have valid layer and property |
| Edit Position using numeric dialog | `Ctrl+Shift+P` | With selected layer, not text editing |
| Edit Rotation numeric dialog | `Ctrl+Shift+R` |  |
| Edit Opacity numeric dialog | `Ctrl+Shift+O` | O, not T |
| Auto-Orient dialog | `Ctrl+Alt+O` | Orient along path / toward camera |
| Move layers 1 viewer pixel | `Arrow keys` | Zoom-dependent composition-space increment |
| Move layers 10 viewer pixels | `Shift+Arrow keys` | Magnification matters |
| Move value at normal increments | Drag hot-text value | Numeric scrub |
| Move value 10× faster | `Shift+drag` hot-text |  |
| Move value 10× slower | `Ctrl+drag` hot-text | Fine adjustment |
| Center layer anchor position in comp view | `Ctrl+Home` | Changes Position; doesn't center anchor inside content |
| Center anchor point in visible layer content | `Ctrl+Alt+Home` | Changes anchor and compensates position |
| Reset Rotation to 0° | Double-click Rotation tool |  |
| Reset Scale to 100% | Double-click Selection tool |  |
| Rotate Z 1° / 10° | `Num +/-` / `Shift+Num +/-` | Selected layers |
| Scale +/−1% | `Ctrl+Num +/-` or `Alt+Num +/-` |  |
| Scale +/−10% | `Ctrl+Shift+Num +/-` or `Alt+Shift+Num +/-` |  |
| Opacity +/−1% | `Ctrl+Alt+Num +/-` |  |
| Opacity +/−10% | `Ctrl+Alt+Shift+Num +/-` |  |
| Constrain interactive rotation 15° | Hold `Shift` while using Rotation tool |  |
| Preserve aspect ratio when changing layer bounding-box size | Hold `Shift` while dragging handle | Behavior also depends on current transform modes |
| Fit layer by distortion to comp width and height | `Ctrl+Alt+F` | Can stretch image |
| Fit layer to comp width preserving ratio | `Ctrl+Alt+Shift+H` | H = horizontal |
| Fit layer to comp height preserving ratio | `Ctrl+Alt+Shift+G` | G = vertical mapped shortcut |
| Effects: disable selected layer's effects | Click timeline fx switch | Nondestructive disable |
| Effects: delete all on selected layer(s) | `Ctrl+Shift+E` | Destructive removal |
| Copy with property links | `Ctrl+Alt+C` (where exposed) / `Edit → Copy with Property Links` | Creates expressions referencing source property; test across comps |
| Copy Expression Only | `Edit → Copy Expression Only` | Assign custom key if desired; does not copy values |
| Add an expression to a selected property | `Alt+Shift+=` / Animation → Add Expression | Adobe-documented binding; verify your installed preset. Use the expression switch for temporary bypass. |
| Toggle expression editor for one property | `Alt+click` stopwatch | Can remove existing expression; prefer `=` switch to disable temporarily |
| Show Graph Editor | `Shift+F3` | Toggle timeline/graph |
| Add/remove keyframe at CTI | `Alt+Shift+P/S/R/T/A` etc. | Current property value |
| Go previous / next visible key | `J` / `K` | Also jumps timeline markers/bounds |
| Easy Ease | `F9` | Eases into *and* out of keyframe |
| Easy Ease In | `Shift+F9` | Slow into selected keyframe |
| Easy Ease Out | `Ctrl+Shift+F9` | Slow away from selected keyframe |
| Keyframe Velocity dialog | `Ctrl+Shift+K` | Precise speeds/influence |
| Keyframe Interpolation dialog | `Ctrl+Alt+K` | Temporal/spatial controls |
| Hold ↔ Auto Bézier method | `Ctrl+Alt+H` | Context-dependent selection |
| Linear ↔ Auto Bézier | `Ctrl+click` keyframe (layer bars) |  |
| Linear ↔ Hold | `Ctrl+Alt+click` keyframe (layer bars) | Different modifier from above |
| Nudge selected keyframes ±1 frame | `Alt+Left/Right` | Keyframes selected, not layer |
| Nudge selected keyframes ±10 frames | `Alt+Shift+Left/Right` |  |
| Select all keys on one property | Click property name | Timeline |
| Select all visible keyframes/properties | `Ctrl+Alt+A` | Only visible elements |
| Deselect keys/properties/groups | `Shift+F2` / `Ctrl+Alt+Shift+A` |  |
| Reverse pasted keyframes | `Ctrl+Shift+V` | First copy with `Ctrl+C` |
| Proportionally rescale a group of keyframes | `Alt+drag` first/last selected keyframe | Stretches timing around opposite boundary |
| Reverse keyframe sequence in its current span | Keyframe Assistant → Time-Reverse Keyframes | Preserve original placement range |
| Rove a spatial keyframe across time | Right-click keyframe → Rove Across Time | For middle spatial keys; optimizes speed along motion path |
| Change selected interpolation to Hold | Right-click keyframe → Toggle Hold Keyframe | Useful for stepped animation |
| Allow subframe keys (graph mode) | Graph Editor options → Allow Keyframes Between Frames | Usually leave off for frame-accurate video timing |
| Horizontal/vertical Type tool | `Ctrl+T` (cycle) |  |
| New text layer | `Ctrl+Alt+Shift+T` |  |
| Left / center / right align | `Ctrl+Shift+L/C/R` | Paragraph alignment |
| All Caps / Small Caps | `Ctrl+Shift+K` / `Ctrl+Alt+Shift+K` | Text selected |
| Superscript / Subscript | `Ctrl+Shift+=` / `Ctrl+Alt+Shift+=` |  |
| Reset horizontal / vertical text scale to 100% | `Ctrl+Shift+X` / `Ctrl+Alt+Shift+X` |  |
| Automatic leading | `Ctrl+Alt+Shift+A` |  |
| Reset tracking to zero | `Ctrl+Shift+Q` |  |
| Justify, last line left / right / force | `Ctrl+Shift+J` / `Ctrl+Alt+Shift+J` / `Ctrl+Shift+F` |  |
| Decrease/increase font size by 2 | `Ctrl+Shift+,` / `Ctrl+Shift+.` | Text selected |
| Decrease/increase font size by 10 | `Ctrl+Alt+Shift+,` / `Ctrl+Alt+Shift+.` |  |
| Increase/decrease leading by 2 | `Alt+Down/Up` | Between baselines |
| Leading by 10 | `Ctrl+Alt+Down/Up` |  |
| Baseline shift by 2 / 10 | `Alt+Shift+Down/Up` / `Ctrl+Alt+Shift+Down/Up` | Vertical text offset |
| Kerning/tracking by 20 / 100 units | `Alt+Left/Right` / `Ctrl+Alt+Left/Right` | 1/1000 em units |
| Toggle paragraph composer | `Ctrl+Alt+Shift+T` | Context matters; same keys may mean new text layer elsewhere |
| Move by character / word | `Left/Right` / `Ctrl+Left/Right` | Text caret in a text box |
| Move by line / paragraph | `Up/Down` / `Ctrl+Up/Down` |  |
| Extend selection by char / word | `Shift+Left/Right` / `Ctrl+Shift+Left/Right` |  |
| Extend text selection by line | `Shift+Up/Down` |  |
| Select to line start/end | `Shift+Home/End` |  |
| Select to text frame beginning/end | `Ctrl+Shift+Home/End` |  |
| Extend selection to click point | `Shift+click` |  |
| Select word/line/paragraph/all | Double/triple/quadruple/quintuple click Type tool | Contextual |
| Finish entering text | `Num Enter` | Main `Enter` generally inserts line break |
| New mask | `Ctrl+Shift+N` | On a valid selected layer |
| Select next/previous mask | Alt + backtick / Alt+Shift+backtick | Grave key above Tab |
| Select all vertices of mask | `Alt+click` mask |  |
| Free Transform mask points | Double-click mask with Selection tool, or select mask then `Ctrl+T` | Exit `Esc` |
| Scale from center in Free Transform | `Ctrl+drag` |  |
| Nudge vertices 1/10 pixel-at-view | `Arrow` / `Shift+Arrow` | Magnification-based |
| Toggle smooth ↔ corner mask point | `Ctrl+Alt+click` vertex |  |
| Create/redraw Bézier handle | `Ctrl+Alt+drag` vertex |  |
| Invert mask | `Ctrl+Shift+I` |  |
| Mask Feather dialog | `Ctrl+Shift+F` |  |
| Mask Shape dialog | `Ctrl+Shift+M` |  |
| Change closed-mask mode during drawing/editing | `A` Add; `S` Subtract; `D` Darken; `F` Difference; `I` Intersect; `L` Lighten; `N` None | Hold the mouse button during mask drawing/modification; see below. |
| Group shapes / Ungroup shapes | `Ctrl+G` / `Ctrl+Shift+G` | Selected shape groups |
| Free-transform shape Path | Select Path then `Ctrl+T` |  |
| Paint foreground/background swap | `X` | When paint tool active |
| Paint black/white default colors | `D` | In paint context; Timeline `D` scrolls to CTI |
| Paint foreground sample | `Alt+click` | In Layer viewer |
| Average 4×4 color sample | `Ctrl+Alt+click` | Paint tool active |
| Resize brush / change hardness | `Ctrl+drag` / begin `Ctrl+drag`, release Ctrl as dragging |  |
| Join stroke to prior paint stroke | Hold `Shift` at start of stroke |  |
| Clone Stamp source point | `Alt+click` | Set sample before painting |
| Paint opacity 10–90% | `Num 1–9` | Paint context, not layer select |
| Paint opacity 100% | `Num .` |  |
| Paint flow 10–90% | `Shift+Num 1–9` |  |
| Paint flow 100% | `Shift+Num .` |  |
| Move playhead by paint-stroke duration | `Ctrl+Page Up/Down` or `1/2` (main keyboard) | Paint context |
| Marker at CTI | `Num *` | Layer marker if layer selected; else composition marker |
| Marker with dialog | `Alt+Num *` |  |
| Set numbered comp marker 0–9 | `Shift+0–9` (main keyboard) |  |
| Jump to numbered comp marker | `0–9` (main keyboard) | Conflicts with number entry if text focused |
| Duration between two keys/markers in Info panel | `Alt+click` first and second |  |
| Remove marker | `Ctrl+click` marker |  |
| Change mask/track feature region ±1/10 | `Arrow` / `Shift+Arrow` | Tracking context |
| Move feature/search region but not attach point ±1/10 | `Alt+Arrow` / `Alt+Shift+Arrow` | Tracking context |
| New camera | `Ctrl+Alt+Shift+C` | Camera layer |
| New light | `Ctrl+Alt+Shift+L` | Light layer |
| Camera orbit/pan/dolly mode | `1` / `2` / `3` (main keyboard) | 3D-view camera controls |
| Universal / Position / Scale / Rotation gizmo | `V` / `4` / `5` / `6` (main keyboard) | 3D viewer context |
| Camera tool family | `C` repeated |  |
| 3D view 1 / 2 / 3 | `F10` / `F11` / `F12` | Defaults Front / Custom View 1 / Active Camera on Windows |
| Return previous 3D view | `Esc` | In view context |
| Camera look at selected 3D layers | `Ctrl+Alt+Shift+\` |  |
| With camera tool selected: look at selected | `F` |  |
| With camera tool selected: look at all | `Ctrl+Shift+F` |  |
| Turn Cast Shadows on/off on selected 3D layers | `Alt+Shift+C` |  |
| Import file | `Ctrl+I` |  |
| Import multiple | `Ctrl+Alt+I` |  |
| Add selected project item(s) to active comp | `Ctrl+/` (main keyboard) |  |
| Replace footage for selected layer(s) with selected project item | `Ctrl+Alt+/` (main keyboard) |  |
| Swap one layer's footage but preserve setup | `Alt+drag` Project item onto layer | Extremely useful |
| Interpret Footage | `Ctrl+Alt+G` | Source FPS, alpha, color, fields |
| Remember footage interpretation | `Ctrl+Alt+C` |  |
| Replace project footage item | `Ctrl+H` |  |
| Reload project footage item | `Ctrl+Alt+L` |  |
| Set footage proxy | `Ctrl+Alt+P` | Manage sources efficiently |
| Delete footage with no warning | `Ctrl+Backspace` | Dangerous; Project panel context |
| Double-click effect in Effects & Presets | Double-click | Applies to selected layers |
| Apply last used effect | `Ctrl+Alt+Shift+E` |  |
| Apply last used animation preset | `Ctrl+Alt+Shift+F` |  |
| Remove all effects from selected layers | `Ctrl+Shift+E` | Deletes them |
| Add current comp to Render Queue | `Ctrl+Shift+/` |  |
| Add current comp to AME | `Ctrl+Alt+M` |  |
| Save frame | `Ctrl+Alt+S` | Add frame to Render Queue |
| Duplicate Render Queue output item | `Ctrl+Shift+D` in Render Queue | In Timeline it instead splits layer |
| Show safe margins | `'` | Title/action safe zones |
| Show grid | `Ctrl+'` | Full grid |
| Show proportional grid | `Alt+'` | Large proportion reference |
| Show rulers | `Ctrl+R` | Drag rulers to create guides |
| Show guides | `Ctrl+;` | Semicolon |
| Snap to grid | `Ctrl+Shift+'` | Toggle |
| Snap to guides | `Ctrl+Shift+;` | Toggle |
| Lock/unlock guides | `Ctrl+Alt+Shift+;` | Keep guides safe |
| Hide/show mask paths, layer controls, bounding boxes | `Ctrl+Shift+H` | Doesn't alter render |
| Active Comp viewer options | `Ctrl+Alt+U` | Includes overlays |
| Show grayscale Red/Green/Blue/Alpha | `Alt+1/2/3/4` | Check matte contamination |
| Show tinted R/G/B channel | `Alt+Shift+1/2/3` |  |
| Show Straight RGB | `Alt+Shift+4` | Useful for premultiplication checks |
| Alpha boundary in Layer panel | `Alt+5` |  |
| Alpha overlay in Layer panel | `Alt+6` |  |
| Refine Edge X-ray | `Alt+X` | Edge/matte review |
| Extend an item selection in Project, Effect Controls or Render Queue | `Shift+Up/Down` | Adds adjacent items to the selection; Timeline layer selection uses `Ctrl+Shift+Up/Down`. |
| Change project calculation precision quickly | `Alt+click` the Project panel bit-depth indicator | Cycles project bpc; clicking without Alt opens Project Settings. |
| Reset preferences during application launch | Hold `Ctrl+Alt+Shift` while launching | Follow the reset prompt; use when diagnosing a preference problem, after preserving custom settings. |
| Activate a different view in a multi-view Comp panel | Middle-click that view | Changes active view without changing selected layers. |
| Return to the previously active related composition | `Shift+Esc` | Travels within the current nested-composition hierarchy. |
| Use the third configurable preview binding | `Shift+Num 0` | Has its own Preview-panel settings, alongside Space and Num 0. |
| Restore older RAM/standard preview configurations | `Alt+click` Reset in Preview | Changes preview bindings/settings; ordinary playback remains configurable. |
| Scrub video interactively | Drag CTI; `Alt+drag` according to Live Update setting | Preview updating depends on Live Update. Audio scrubbing uses `Ctrl+drag`. |
| Open footage itself for inspection | Double-click its Project-panel item | Opens the Footage viewer, separate from its layer instance. |
| Open a Timeline layer's source | `Alt+double-click` that layer | Footage sources open in Footage; a precomp layer opens in Layer rather than its source composition. |
| Stretch a layer to a new In/Out reference | `Ctrl+Shift+,` / `Ctrl+Alt+,` | Time-stretch boundary commands; source playback speed changes. Inspect the Time Stretch result. |
| Expand selected effects in Effect Controls | `Ctrl` + backtick | Same expansion principle as Timeline; click the intended panel first. |
| Erase only the latest paint stroke temporarily | Hold `Ctrl+Shift` with a paint tool | Temporary Eraser / Last Stroke Only behavior. |
| Reposition Clone Stamp overlay/sample relationship | `Alt+Shift+drag` using Clone Stamp | Edits Offset when aligned, Source Position when unaligned. |
| Recall one of five Clone Stamp presets | Main-keyboard `3`–`7` | Paint/Clone context; these digits have different meanings in camera or marker contexts. |
| Make a copy of a Clone Stamp preset | `Alt+click` its preset button in Paint | Duplicates settings for another paint setup. |
| Advance/rewind by the paint stroke duration | `Ctrl+Page Down/Up`, or main-keyboard `2/1` | Moves time by the configured Duration; it does not change Duration itself. |
| Text caret to start/end of current line | `Home` / `End` | Text editing only; Timeline uses these for time navigation. |
| Select all characters in one text layer | Double-click the text layer | Enters text editing with its text selected. |
| Vertical text: select adjacent characters | `Shift+Up/Down` | Vertical typography follows its writing direction. |
| Vertical text: select words | `Ctrl+Shift+Up/Down` | Word-sized text selection. |
| Vertical text: select adjacent lines | `Shift+Left/Right` | Extends selection across vertical text columns. |
| Vertical text: caret by character / line / word / paragraph | `Up/Down` / `Left/Right` / `Ctrl+Up/Down` / `Ctrl+Left/Right` | Direction differs from horizontal text. |
| Vertical text alignment: top / center / bottom | `Ctrl+Shift+L/C/R` | Same alignment chords as horizontal text, interpreted vertically. |
| Round a rectangle while drawing | `Up/Down` | Adjusts roundness; on polygon/star tools these keys adjust sides/points. |
| Set rectangle corners to sharp / maximum roundness while drawing | `Left/Right` | For polygons/stars, adjusts outer roundness instead. |
| Repeat a Render Queue item with the original output filename | `Ctrl+Shift+D` in Render Queue | Check destination before rendering; this duplicate keeps the same filename. |
| Select every key on a property's graph | `Alt+click` a segment | Selects the property’s keys. |
| Constrain box movement | `Shift+drag` inside box | Time-only or value-only movement. |
| Scale around the box anchor | `Ctrl+drag` a box handle | Expands/contracts around its pivot. |
| Adjust only one corner | `Alt+drag` a corner handle | Changes that corner. |
| Taper values across the selection | `Ctrl+Alt+drag` a handle | Changes an animation's amplitude progressively. |
| Raise/lower one side | `Ctrl+Alt+Shift+drag` a handle | Tilts the selected value pattern. |
| Compare two looks inside AE | `Shift+F5…F8`, then `F5…F8` | Viewer snapshots for comparison. |
| Save a still using output settings | `Ctrl+Alt+S` | Queues the current frame for rendering. |
| Quick Apply | Ctrl+Enter | Outside the dialog opens Edit → Quick Apply. Type e:, p: or m: to filter. |
| Apply selected Quick Apply result | Enter | Inside Quick Apply applies/runs the highlighted result on the intended selection. |
| Quick Apply on a new layer | Ctrl+Enter | Inside Quick Apply creates a new solid/layer for the selected effect or preset; read result modifier hints. |
| Quick Apply on a new adjustment layer | Ctrl+Alt+Enter | Inside Quick Apply; adjustment affects underlying composited layers. |
| Move staggered selection start to CTI | Shift+[ | Earliest selected In meets CTI; relative timing is preserved. |
| Move staggered selection end to CTI | Shift+] | Latest selected Out meets CTI; relative timing is preserved. |
| Trim relative selection In points | Alt+Shift+[ | Uses earliest selected In as reference; inspect source handles. |
| Trim relative selection Out points | Alt+Shift+] | Uses latest selected Out as reference; inspect source handles. |
| Proportional Scrubbing | Ctrl+Alt+drag property hot text | Distributes numerical change in selection order; not Quick Offset on bars/keys. |
| Toggle guide units while dragging | Alt during guide drag | 26.5: switch pixel/percent units. |
| Toggle guide reference while dragging | Ctrl during guide drag | 26.5: toggle pinning while retaining visual position; Lock Guides is separate. |
| Copy rendered frame to clipboard | Ctrl+Alt+Shift+F5 | Composition/Layer/Footage viewer. Display transform and Transparency Grid affect the copied result. |
| Object Matte tool | Toolbar; verify binding in installed editor | Adobe lists Ctrl+W but general shortcuts assign it to Close; use toolbar or verify/remap rather than guessing context. |

---

## Troubleshooting

| Symptom | Inspect | Corrective action |
|---|---|---|
| Nothing appears in the viewer | Layer eye, Solo, enabled comp, work area, layer in/out, opacity, blend modes, track matte, guide layer, 3D view, collapsed transformations, alpha, effects | Start by switching to Active Camera/Front as appropriate and temporarily bypass suspect mattes/effects. |
| Layer is black where it should be transparent | Transparency Grid is a *preview aid*; comp background color isn't alpha, solid-color source may be opaque | Toggle Transparency Grid and inspect Alpha channel, not simply black RGB. Choose output format with alpha if needed. |
| Background is black after export | Codec/container doesn't preserve alpha; transparency interpreted as black in player | Use ProRes 4444 or appropriate PNG/EXR sequence with RGB+Alpha and correct alpha interpretation. Standard H.264 MP4 doesn't export an alpha channel. |
| Matte isn't working | Track Matte source assignment, Alpha vs Luma, invert, source visibility, matte layer alpha/brightness | Select the matted layer, choose its matte source with pick whip/dropdown. Matte source may be elsewhere in layer stack. |
| Some effects appear missing | Effects & Presets search, installed plugin, effect hidden in Obsolete group, renderer or bit-depth limitations | Confirm exact effect name/category; inspect supported 8/16/32-bpc and GPU icons, then verify plugins. |
| Can't see keyframes | Property is collapsed, layer not selected, Timeline search filter, expression-only animation | `U` shows keyed properties; `UU` modified properties; `EE` expressions. Clear Timeline search. |
| `J/K` seems to skip keyframes | Relevant properties are not exposed | Reveal keyframes with `U` and clear search/filter. |
| Shortcut doesn't work | Wrong panel focus; text cursor active; laptop Fn mapping; OS intercept; custom shortcut | Click correct panel; press `Esc` to leave text edit; check Edit → Keyboard Shortcuts. |
| `G/Q` draws a mask instead of a shape | Existing footage/solid layer selected vs no layer selected; Tool Creates Shape/Mask setting | Deselect layers for a new shape layer; deliberately choose Shape or Mask mode. |
| Cannot edit parametric rectangle vertices | Procedural Rectangle Path rather than Bézier path | Convert shape path to Bézier Path, then select Path and vertex. Preserve parametric form if you still need width/corner sliders. |
| Path pasted into Position doesn't follow correctly | Wrong path/property selection; position separation; space transforms; dimensions | Copy actual Path property, paste on Position with playhead at desired time, inspect spatial path. |
| Auto-Orient flips or points the wrong way | Original artwork direction, tangent, parent transform, spatial path | Use Auto-Orient Along Path and rotate source art/precomp for desired leading direction. |
| 3D object is flat / no depth | 3D switch vs geometry extrusion, render engine, mesh type, camera/light | A 3D switch creates a plane; actual geometric depth requires supported geometry/renderer and property controls. |
| Light has no effect | Layer material settings, 3D renderer, light type, lighting switch or blend style | Verify compatible renderer and Accepts Lights/material properties. |
| Motion blur doesn't show | Layer motion-blur switch, comp master motion-blur switch, shutter angle, type of animation | Enable both switches and verify shutter angle/samples; FX blur may behave differently. |
| Roto Brush crawls or drifts | Propagation, segmentation boundary, view resolution, clip cuts, occlusion, strokes too broad | Work close to source/full resolution, make small corrections, propagate in short spans, refine and freeze. |
| Green-screen subject looks transparent | Too aggressive Clip Black/White, Shrink/Grow, despill, suppression | Inspect Keylight Screen Matte; aim for clean black background, white subject and sensible grey edges. |
| Roto/keyer edges have a halo | Premultiplied RGB contamination, poor despill, matte chatter, uncorrected edge colors | Check straight/premultiplied interpretation, use edge color decontamination/despill, slight blur/choke only if needed. |
| Animation seems to speed up unpredictably | Unequal keyframe timing, nonlinear Graph Editor easing, path distances, frame rate | Examine motion-path dots, timing, speed graph and roving keys. Equal time between keys ≠ constant spatial speed. |
| Keyframes won't move off frames | Timeline snapping / graph options | Graph Editor → Choose Graph Type and Options → Allow Keyframes Between Frames (when supported). Rendering still samples actual frame times. |
| Badly lagging preview | Large footage, many layers, effects, GPU memory, disk cache, insufficient RAM, compressed media | Start with 1/4 preview and shorter work area; disable heaviest effects; test transcoded sources; inspect cache/disk. |
| Audio drifts out of sync | Variable frame rate footage, interpretation mismatch, mixed sample rates, time stretching | Convert VFR footage to constant frame rate; confirm comp rate, audio 48 kHz where appropriate; inspect source timing. |
| Type animation breaks across machines | Missing font or font-axis support, font version mismatch, plugin effects | Package font/license details, verify exact font and open a test copy on target machine. |
| Render different from preview | Work area vs entire comp; proxy; guide layers; 3D/camera, output color/bit depth; motion blur/sample settings | Render a short test with the intended output module and compare RGB/alpha/color. |
| Render fails / hangs | Corrupt frame, GPU driver, unsupported plugin, insufficient disk space, bad source segment | Narrow to failing frame/time, disable suspected effect, render a short image sequence, review log, update plugin/driver responsibly. |
| After Effects will not launch on Windows | Check installed version, supported CPU/AVX2, required GPU API, permissions and plugin crashes. | Check the current 26.5 system requirements, driver and architecture; isolate third-party startup effects with supported diagnostics. |
| Older OpenCL 1.2 GPU fails | Verify 26.5 hardware requirements and installed GPU driver/OpenCL capabilities. | Use a supported GPU with the required API, not a workaround that disables GPU capability checks. |
| Cannot find Quick Apply | Check 26.5 stable, text/modal focus and a remapped shortcut. | Use Edit → Quick Apply or its Timeline icon; Ctrl+Enter opens it. Check installed Keyboard Shortcuts. |
| Cannot find Object Matte tool | Confirm 26.5 and open the footage layer in Layer panel. | Choose Object Matte from the toolbar. Adobe lists Ctrl+W, which conflicts with Close; verify locally rather than assuming a focus rule. |
| Cannot find native SVG shape import | Check import mode and whether you are importing a file or pasting clipboard SVG. | File → Import → File can import SVG as a composition or footage; Illustrator paste requires Include SVG Code. |
| Cannot find new Unmult or Curl Noise | Search e:unmult or e:curl noise in Quick Apply and inspect Effect → Manage Effects. | Confirm 26.5 stable and enabled native effects. Unmult handles black/white alpha; Curl Noise generates flowing texture. |
| Cannot find Audio Compressor/Gate/Distortion | Verify the selected audio layer and search the Audio effects category. | These effects are stable in 26.5. Test the processed rendered sound with an audio-enabled Output Module. |
| No new percentage-based guide controls | Confirm 26.5 and the active viewer; a guide is distinct from a grid line. | Right-click a guide → Edit Guide to set percent/pixel units, reference edge and color. |
| Cannot generate ACES 2.0 default configuration | Check Project Settings → Color → OCIO color managed and the installed version. | Choose ACES 2.0 CG v4.0 or Studio v4.0; specify input, working, display and output transforms. |
| Text editor shortcuts change layer behavior | Text cursor has focus, so Ctrl+Shift+K or letter keys act on text. | Exit text editing with a valid method, select Timeline panel, and try again. |
| Shape Layer created but nothing is visible | Empty Contents group, missing Fill/Stroke, hidden layer or path size 0. | Draw a path, enable Fill/Stroke, inspect Contents and layer visibility. |
| New rectangle is a mask instead of a shape | A valid existing image/solid layer was selected or toolbar mode is Tool Creates Mask. | Deselect layers or change toolbar mask/shape mode intentionally. |
| Rotating layer moves it in a strange circle | Anchor is far from intended rotation pivot. | Inspect A and P; use Y Pan Behind to move anchor while preserving apparent position. |
| Child jumps when parenting | Parent and child coordinate spaces or existing keyframes differ. | Inspect parent transforms and resulting local coordinates; undo and establish a clean rig hierarchy. |
| Imported image looks too small or too large | Footage and comp dimensions differ; non-square pixels or layer Scale may be involved. | Inspect footage pixels, comp pixels, pixel aspect ratio and fit-to-comp commands. |
| Pixel aspect looks squeezed | Non-square pixel interpretation or comp setting mismatch. | Correct Interpret Footage and composition pixel aspect ratio; verify intended final output. |
| Image sequence imports as one still | Sequence option not enabled or numbering not continuous. | Select the first frame and enable appropriate image-sequence import options. |
| Layer plays backward unexpectedly | Time-Reverse Layer or descending Time Remap curve. | Inspect Time Remap and selected layer time operations, then restore correct source order. |
| Loop has one blank or extra frame | Default last Time Remap key points to source duration after last visible frame. | Keep a full source-duration cycle: add a last-valid-frame key, hold it through the final interval, and set the cycle boundary key to source time zero. Inspect every seam. |
| Motion path appears curved but motion is uneven | Spatial path curvature and temporal easing are separate. | Review path geometry and Graph Editor speed; do not equate key spacing with constant travel. |
| Stroke / Trim Paths not visible | Confusing effect Stroke with shape Trim Paths or a hidden Fill/Stroke. | Inspect the intended mask or shape path, stroke width, Trim Paths Start/End and operator location. |
| Replaced source ruined apparent scale | New source dimensions differ while layer scale values were preserved. | Use replacement source at expected dimensions or deliberately adjust Scale/anchor. |
| Audio Amplitude expression red error | Wrong layer/effect name or scalar returned to vector property. | Pick whip to actual Slider; return [s,s] for 2D Scale. |
| Source text background does not fit | sourceRectAtTime width/height used without left/top offsets or coordinate conversion. | Use both dimensions and positional offsets in the same coordinate context. |
| FX renders differently with Collapse Transformations | Nested transform/render order was changed. | Disable switch temporarily and compare effects, layer masks and 3D interactions. |
| Glow looks washed out | Glow is applied to too much bright imagery or effect stack has wrong order. | Isolate highlights, adjust Threshold/Radius/Intensity, and compare precomp/stack order. |
| Screen replacement slips on camera movement | Tracker plane drift or incorrect Corner Pin surface. | Review original checkerboard on every frame, recalibrate plane and retrack if necessary. |
| Roto freezes halfway | Propagation range incomplete or erroneous Freeze state. | Review corrected base frame and full span, and unfreeze/refreeze safely as required. |
| Content-Aware Fill looks like repeated blotches | Missing clean reference or fill algorithm cannot reconstruct motion/texture. | Use a reference frame/clean plate, smaller mask, or alternative tracked patch. |
| Output looks washed out | Unintended color transform, output profile or double-applied LUT. | Audit source, working, display and output transforms and inspect metadata. |
| Export audio is absent | Audio layer muted or Render Queue/Output Module audio setting disabled. | Confirm layer Audio switch, export setting and resulting media audio track. |
| Export image sequence has missing frames | Render interruption, nonmatching numbering or wrong range. | Check continuous frame count, output directory and any render failures before assembling. |
| RGBA preview shows black in media player | Media player may ignore alpha even when alpha exists. | Import rendered result in AE or another alpha-aware consumer over a colored solid. |
| RAM cache fills instantly | High-res/32-bpc source, big comp and insufficient RAM. | Limit preview range/resolution, manage memory settings and use proxies/pre-renders. |
| Disk cache full | Cache drive low on space, quota small or large prior assets. | Move cache to a fast drive with room or purge deliberately while AE is idle. |
| Collect Files reopens with missing fonts | Font software is not bundled by Collect Files. | Install licensed fonts on target and record exact family/version in README. |
| One plugin works only on other PC | Plugin binary, GPU, licensing or CPU/OS differs. | Check Windows-compatible plugin version and authorized installation; pre-render a fallback when necessary. |
| Frame preview stops updating | Caps Lock, wrong viewer, cached frame issue or no valid current layer. | Turn Caps Lock off, select correct comp and time, then test on a single plain solid. |
| Custom keyboard preset conflicts | A Windows/app shortcut may intercept it or focus in another panel. | Check Edit → Keyboard Shortcuts, reset/rename mapping and test within intended panel. |
| MOGRT name edit changes all copies | Shared child source edited instead of instance Essential Property. | Expose text properly and use instance overrides on each nested copy. |
| Layer shadows do not appear | Unsupported renderer, 2D layer, Material Options or light settings. | Enable 3D/material options and use an appropriate light/renderer combination. |
| Final master not reproducible | Uncollected source, LUT, font, plugin or unrecorded settings. | Collect Files, document dependencies and rerender a test from the transferred package. |

---

## Glossary

| Term | Definition |
|---|---|
| 2.5D | Flat image layers positioned/oriented in a 3D coordinate space. |
| ACES | Academy Color Encoding System: a standardized scene-referred film/VFX color workflow. |
| ACES / OCIO | Managed color pipeline standards/configuration used in VFX and color-critical work. |
| ACES 2.0 | Color pipeline supported natively in 26.5 through OCIO 2.5.1 and bundled CG/Studio v4.0 configurations. |
| Adjustment layer | Special layer through which effects process underlying composited pixels. |
| Advanced 3D | After Effects renderer for supported imported 3D models and relevant material/lighting features. |
| AEP | Native After Effects project file storing editable compositions and source references rather than embedding every source file. |
| Alpha channel | Transparency; 0 = fully transparent; 1.0 as normalized alpha (or 255 in 8-bit alpha) = fully opaque. |
| Alpha Inverted Matte | Matte type that inverts alpha-derived transparency. |
| Alpha Matte | Matte type that derives target coverage from source alpha. |
| Alpha premultiplication | Whether RGB values already have transparency mathematically baked into the colors. |
| Anchor Point | Local pivot point for scaling/rotation. |
| Attach point | The point to which calculated motion data is applied. |
| Bezier path | Geometry or motion curve controlled by points and tangent handles. |
| Bit depth (bpc) | Processing precision per color channel; not equivalent to source codec's bit depth. |
| Camera solve | Estimated 3D camera motion reconstructed from analyzed footage. |
| Camera Zoom | AE camera projection parameter affecting framing/field of view. |
| Choker | Matte processing effect that contracts/expands or cleans alpha edges. |
| CICP | Codec/container color-encoding metadata describing characteristics such as primaries and transfer functions. |
| Collapse Transformations | Change how transformations are propagated through nested comps; can alter appearance and layer ordering behavior. |
| Collect Files | Project dependency action that copies linked assets into a transportable collected project folder. |
| Color transform / LUT | Map between encodings or looks; creative LUT ≠ necessarily a correct camera input transform. |
| Comp background color | Composition viewer's background preference; not automatically opaque pixels in output. |
| Composition | Canvas and frame-based timeline that combines several layers into a rendered result. |
| Composition Profiler | Diagnostic display to help identify computationally expensive layers or effects. |
| Continuous Rasterization | Related switch that causes eligible vector art to be rasterized at an appropriate scale, retaining sharper edges. |
| Continuously Rasterize | Re-render vector layers at the required effective resolution for sharp results when scaled; cannot restore detail to an arbitrary raster photo. |
| Corner Pin | Perspective effect mapping image corners to specified tracked points. |
| CTI / playhead | Current Time Indicator; the time whose frame is displayed/evaluated. |
| Curl Noise | Procedural 2D flowing texture effect introduced in 26.3. |
| Despill | Remove green/blue color contamination from a keyed object's edges. |
| Disk cache | Persisted reusable frame data stored on a disk; distinct from source assets and final renders. |
| Display transform | Conversion from a working scene/image to a viewing device's intended display rendering. |
| Draft quality | Faster approximate viewer/sampling quality when supported; verify final output. |
| Easy Ease | Keyframe assistant that creates a smooth transition into/out of a keyframe. |
| Effect Controls | Panel for one or more applied effect instances and their properties. |
| Effect Manager | Interface for managing effect availability/enablement in supported builds. |
| Effects & Presets | Searchable After Effects panel listing installed effects and animation presets. |
| Environment light | Illumination sampled from an image or environment in a supported 3D renderer. |
| Essential Graphics | AE interface used to expose properties for templates and nested instance editing. |
| Essential Properties | Exposed properties of a precomp that can be overridden per instance. |
| Expression | Scripted formula linked to a property, evaluated at render/preview time. |
| Expression Controls | Slider, Angle, Color, Point and related controls designed for linking rigs. |
| Expression Selector | Text Animator selector driven by a custom expression. |
| EXR | OpenEXR image format often used with floating-point channels and VFX passes. |
| ExtendScript | Adobe scripting dialect used in JSX automation of application/project structure. |
| Feature region | Tracking patch containing the visual detail being matched across frames. |
| Footage item | Media reference inside the Project panel; one item can appear in multiple compositions. |
| Footage panel | Viewer for opening an imported file's source frames, distinct from a composition view. |
| Frame blending | Method of blending/interpolating frames when source timing differs from the output frame grid. |
| Frame sampling / frame blending | Methods to choose/interpolate frames for different playback time; Pixel Motion can introduce warped artifacts. |
| Freeze Roto | Operation that freezes Roto Brush propagation for a selected span; not equivalent to exporting permanent alpha footage. |
| Garbage matte | Roughly exclude unwanted region before precise keying/rotoscoping. |
| Graph Editor | Speed or value graph for keyframes and interpolation. |
| Guide layer | Visible for internal composition work but generally excluded from its rendered parent-comp output (subject to context). |
| Guide pinning | A guide’s reference edge for responsive placement; different from locking against edits. |
| H.264 | Widely used distribution codec, typically used in MP4 without a normal alpha channel. |
| H.264 / H.265 (HEVC) | Common compressed delivery codecs; strong distribution options, not ideal for every compositing source. |
| Hold / linear / Bézier | Keyframe interpolation choices: jump, constant interval interpolation, or curved interpolation. |
| Hold interpolation | Value stays at a key's level until next key, then jumps. |
| In / Out point | Beginning and end of a layer's visible span. Do not confuse with the Work Area limits `B`/`N`. |
| Input profile | Definition used to interpret source color values correctly. |
| JSX | Common file extension for an After Effects ExtendScript script. |
| Kerning | Spacing between a selected pair of characters. |
| Keyframe | Stored property value (and interpolation/tangent information) at a specified time. |
| Layer panel | Viewer for a single layer's source/paint/roto context. |
| Leading | Vertical distance between baselines of neighboring text lines. |
| Linear interpolation | In-between values change at a uniform numerical rate between keys. |
| Linear light | Signal encoding in which a numerical pixel value corresponds approximately linearly to light intensity. |
| loopOut | Expression function continuing a keyed pattern after its last keyframe. |
| Luma | Perceived image brightness; used for brightness-dependent mattes/effects. |
| Luma Inverted Matte | Matte type that inverts luminance-derived transparency. |
| Luma Matte | Matte type that derives target coverage from matte image brightness. |
| LUT | Lookup table used for a color conversion or artistic look; its meaning depends on source/target spaces. |
| Mask | Alpha boundary applied to a layer, with mode, path, feather, expansion and opacity. |
| Mezzanine | High-quality intermediate media designed for additional editing/compositing. |
| MFR | Multi-Frame Rendering: calculating multiple frames concurrently when resources and effect support permit. |
| Missing Footage | Project warning that an imported source reference cannot currently be resolved on disk. |
| Mocha AE | Bundled planar tracking integration, with features distinct from separately licensed Mocha Pro. |
| MOGRT | Motion Graphics template for standardized motion elements in supporting apps. |
| Motion Graphics Template | A .mogrt package exposing user-facing controls for reusable motion assets. |
| Motion path | Visible spatial trajectory of a Position animation. |
| Motion path dots | Visual samples of successive frame positions, indicating relative frame-to-frame travel spacing. |
| Null object | Invisible transform controller layer commonly used for parenting and expression controls. |
| Object Matte | Object-selection and propagation workflow with disk caching in 26.5; distinct from ordinary vector masks. |
| OCIO | OpenColorIO color pipeline system used for managing color transforms. |
| Offset Paths | Shape modifier that expands/contracts an outline according to its parameters. |
| Output Module | Render Queue configuration of format, channels, color, audio and destination options. |
| Output transform | Color conversion applied when creating a final intended delivery file. |
| Paragraph text | Text object that flows/wraps inside a specified bounding box. |
| Parametric mesh | Native 3D geometry controlled by editable parameters in Advanced 3D. |
| Parametric shape | Geometry described by parameters such as size and roundness rather than custom vertex locations. |
| Parent | A layer whose transforms another layer inherits; shifts spatial relationship. |
| Pixel Motion | Optical-flow-based frame interpolation; may warp around occlusions. |
| Planar tracking | Solving the motion of a flat or approximately flat textured surface. |
| Point of Interest | Target point used by some camera/light layer orientation controls. |
| Point text | Text object that grows naturally from a clicked insertion point. |
| Point tracking | Tracking translation or additional simple motion from one/two visual features. |
| Precomp / nested comp | Composition inside another composition, with its own pixels, properties and timeline. |
| Precompose | Command to move selected layers into a new child composition. |
| Precomposition | A composition nested in another composition, with separate properties and timing. |
| Premultiplied alpha | Representation in which color channels have been mathematically mixed with transparency and possibly a matte color. |
| Proportional Scrubbing | Ctrl+Alt-drag property hot text to distribute a numerical change in selection order; distinct from timing offsets. |
| ProRes / DNxHR | Common higher-quality intraframe editing/intermediate codecs. |
| ProRes 4444 | A ProRes codec variant that can carry an alpha channel in compatible workflows. |
| Protected Region | Time section in a reusable motion template marked to retain its intended timing on stretch. |
| Proxy | Substituted lighter/alternative footage used to speed editing or manage media workflows. |
| Quick Apply | Ctrl+Enter launcher for effects, animation presets and menu commands; stable since 26.2. |
| Quick Offset | `Ctrl+Alt+drag` selected layers/keys to distribute across time. |
| RAM cache | Cached rendered frames stored in memory for reuse during compatible previews. |
| Range Selector | Text Animator selector that applies animated properties to a chosen portion of text. |
| Refine Edge | Rotoscoping refinement tool for wispy/semipermeable boundaries like hair. |
| Render Queue | AE's native output queue, including native H.264 output support in recent versions. |
| Renderer | Processing engine defining 3D interpretation, capabilities and available quality options. |
| Repeater | Shape Contents operator that creates repeated copies using instance transforms. |
| ROI | Region of Interest; viewing/rendering only a limited image region during preview when supported. |
| Roto Brush | Brush-assisted tool for propagating a foreground segmentation through video frames. |
| Roving keyframe | An intermediate spatial-motion key whose time can adjust to maintain a more consistent motion-speed relationship. |
| SBSAR | Substance material file with exposed procedural controls; keep it with project dependencies. |
| Scene-linear | Working space in which numeric light intensity is approximately linear; useful for physically sensible CGI compositing. |
| Search region | Tracking area within which a tracked feature is searched for in the next frame. |
| Shadow catcher | 3D surface/feature used to receive shadows for image integration. |
| Shape group | Container in Shape Layer Contents with paths, styles, modifiers and its own Transform properties. |
| Shutter angle | Motion-blur exposure proportion relative to frame interval. |
| Shutter phase | Temporal offset for the motion blur sampling window. |
| Shy layer | A layer marked for hidden display in the Timeline when the master Shy switch is active; not necessarily absent from rendering. |
| Single 3D gizmo | AE 25.6 multi-selection transformation control for several 3D layers. |
| Solid | Layer generated as a constant-color rectangular source, often used as a carrier for effects. |
| Solo | Layer switch that temporarily isolates one or more layers for viewing/rendering in the working context. |
| Source Text | Editable text content property of a text layer. |
| sourceRectAtTime | Expression method returning a layer's visible rectangle metrics used for dynamic layout. |
| Spatial Bezier | Curved trajectory path for Position, separate from timing/easing. |
| Spatial interpolation | How a Position path curves between locations. |
| Speed Graph | Graph Editor view of the rate at which a property changes over time. |
| Straight alpha | RGBA representation in which RGB is not preblended against a matte color. |
| Temporal Bezier | Value-easing curve controlled by time-related tangent handles. |
| Temporal interpolation | How a value moves between times/keys. |
| thisComp | Expression reference to the current composition. |
| thisLayer | Expression reference to the current evaluated layer. |
| Time Remapping | Keyframable mapping from composition time to source time. |
| Time Stretch | Source playback-duration adjustment of a layer. |
| Tip of the Day | AE 25.6 guidance shown in certain empty/reloaded viewer contexts. |
| Track Matte | Another layer drives the alpha/brightness mask of a target layer. |
| Tracking | General letterspacing across a selected run of text. |
| Trim Paths | Shape Contents operator that shows only a Start-to-End portion of an eligible path. |
| Unmult | Keying effect converting a suitable black/white backing into alpha with level and edge controls. |
| Value Graph | Graph Editor view of property value over time. |
| valueAtTime | Expression function sampling a property's value at a requested time. |
| Variable font axis | Continuous font-specific variation such as Weight or Width, animatable through text animators. |
| Warp Stabilizer | Stabilization effect using motion analysis and compensating transforms/warping. |
| wiggle | Expression function producing time-varying pseudorandom variation in a property. |
| Wiggly Selector | Text Animator selector that varies which characters receive animated properties. |
| Work Area | Selected time range for preview/export, independent of composition duration until trimmed. |
| Working color space | Common space in which images are processed and composited. |
| Z depth | Distance along the third spatial axis, controlling parallax and depth relationships. |

---

## Sources and version restrictions

Adobe documentation is rolling; release notes, feature-specific pages and feature history establish the stable 26.5 boundary. The guide includes original explanatory content; no Adobe images, proprietary plugin binaries or training videos are bundled.

- **Adobe: Immersive video effects** — https://helpx.adobe.com/after-effects/desktop/immersive-video-and-vr/immersive-video-effects/vr-effects.html — Rolling Adobe reference; distinguish stable controls from Beta.
- **Adobe: Blending modes and Layer Styles** — https://helpx.adobe.com/after-effects/desktop/work-with-layers/work-with-layer-blending-modes/blending-modes-layer-styles.html — Rolling Adobe reference; distinguish stable controls from Beta.
- **Adobe: Create masks and outlines** — https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/work-with-masks/create-masks.html — Rolling Adobe reference; distinguish stable controls from Beta.
- **Adobe: What is new through 26.5** — https://helpx.adobe.com/after-effects/desktop/what-s-new/whats-new.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: After Effects Beta (separate from stable)** — https://helpx.adobe.com/after-effects/desktop/what-s-new/after-effects-beta.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Known issues by affected release** — https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/known-issues-after-effects.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Quick Apply** — https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/quick-apply.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: AI-powered Object Matte** — https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Guide creation and management** — https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Effect Controls and instance labels** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Effect masks, opacity and animation presets** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Proportional Scrubbing** — https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/proportional-scrubbing-in-timeline.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Selecting and arranging layers** — https://helpx.adobe.com/after-effects/desktop/work-with-layers/select-and-arrange-layers/selecting-arranging-layers.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: SVG import and clipboard transfer** — https://helpx.adobe.com/after-effects/desktop/import-files/import-svg-files/import-svg-files.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Working with Variable Font Axes** — https://helpx.adobe.com/after-effects/desktop/variable-font-axes/work-with-variable-font-axes/working-with-variable-font-axes.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Create parametric meshes** — https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Apply Substance 3D materials** — https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/apply-substance-3d-materials.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Modify materials and displacement** — https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/modify-materials-properties-of-3d-layers.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Advanced 3D in-engine depth of field** — https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-3d-scene-depth-data/enable-in_engine-depth-of-field-in-advanced-3d.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Noise, grain and Curl Noise** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Keying and Unmult** — https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Audio effects** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/audio-effects.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Copy Frame to Clipboard** — https://helpx.adobe.com/after-effects/desktop/view-and-preview/copy-frames/copy-frame-to-clipboard.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Native null controllers** — https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/null-controllers/create-nulls-for-positional-properties-and-paths.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Composition Profiler** — https://helpx.adobe.com/after-effects/desktop/work-with-compositions/composition-profiler/composition-profiler.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Lossless compressed playback** — https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/lossless-compressed-playback.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Previewing and Region of Interest** — https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/previewing.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Effect Manager** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-manager.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Data-driven animations** — https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/data-driven-animation/data-driven-animations.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Native H.264 Render Queue output** — https://helpx.adobe.com/after-effects/desktop/render-and-export/export-h-264-from-the-after-effects/exporting-h264-from-the-after-effects-render-queue.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: Mask Tracking** — https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-mask/rigid-mask-tracking.html — Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.
- **Adobe: After Effects release notes (26.5, September 2026)** — https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html — Stable target: 26.5. Rechecked 2026-10-28; Beta remains separate.
- **Adobe-maintained After Effects feature history** — https://github.com/AdobeDocs/after-effects-feature-history — Historical introduction dates; current stable workflows target 26.5.
- **Adobe: fixed issues in After Effects** — https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/fixed-issues.html — Includes historical 25.6 fixes; document is rolling.
- **Adobe: After Effects 26.x system requirements** — https://helpx.adobe.com/after-effects/desktop/get-started/technical-requirements/system-requirements.html — Current Windows requirements applicable to 26.5; actual CPU/GPU architecture matters.
- **Adobe: After Effects keyboard shortcuts reference** — https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html — Rolling shortcut page; compare against 26.5 installed editor.
- **Adobe: After Effects documentation index** — https://helpx.adobe.com/after-effects/desktop.html — Rolling guide. Later-release features may appear.
- **Adobe: effect list and capabilities** — https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html — Rolling list; cross-check 26.5 installed Effects & Presets.
- **Adobe: expression language reference** — https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html — JavaScript-like expression syntax; rolling documentation.
- **Adobe: understanding expression language** — https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-basics/expression-language.html — Expressions evaluate properties; distinct from ExtendScript automation.
- **Adobe: color management** — https://helpx.adobe.com/after-effects/desktop/adjust-colors/color-management/color-management.html — ICC and OCIO pipelines; 26.5 bundles ACES 2.0 configurations.
- **Adobe: OpenColorIO and ACES** — https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html — 26.5 uses OCIO 2.5.1 with ACES 2.0 CG v4.0 and Studio v4.0.
- **Adobe: create Motion Graphics templates** — https://helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html — Essential Graphics/Properties/MOGRT general technique; rolling.
- **Adobe: memory and storage** — https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html — Cache behavior; preference nomenclature varies by version.
- **Adobe: multi-frame rendering** — https://helpx.adobe.com/after-effects/desktop/render-and-export/multi-frame-rendering/multi-frame-rendering.html — Multi-Frame Rendering predates 25.6.
- **Adobe: Precomposing, nesting, and pre-rendering** — https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html — Leave all attributes is not available for multiple layers, shape layers, or text layers; Adobe Help is rolling.
- **User-supplied AE Notes (26.5 starting point)** — (user supplied document) — Adapted as a topic inventory and terminology starting point; Stable 26.5 coverage seed; verify factual claims against Adobe sources.

### Stable 26.5 and Beta boundary

Stable workflows include Quick Apply, Object Matte with disk caching, parametric meshes, Substance materials, variable-font axes, SVG import/paste, Unmult, Curl Noise, Compressor/Gate/Distortion, Advanced 3D DOF, effect labels, responsive guides and bundled ACES 2.0.

Beta watchlist at the research cutoff: Contour Paint, De-esser, AI Assistant, layers as material sources, materials on 3D text/shapes, editable Illustrator text, Quick Set Anchor, generalized viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save.

**Limits:** The reader is browser-tested separately from the product instructions. No licensed Windows AE 26.5 installation was available to execute every lesson or verify every installed plug-in parameter. External fonts, codecs, materials and hardware can change results; verify final deliverables.
