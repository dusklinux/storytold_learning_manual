"""Original AE 26.5 Windows learning material. No third-party content copied verbatim."""

SOURCES = {
 'immersive': {'title': 'Adobe: Immersive video effects', 'url': 'https://helpx.adobe.com/after-effects/desktop/immersive-video-and-vr/immersive-video-effects/vr-effects.html', 'kind': 'reference', 'note': 'Rolling Adobe reference; distinguish stable controls from Beta.'},
 'layer-styles': {'title': 'Adobe: Blending modes and Layer Styles', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-layers/work-with-layer-blending-modes/blending-modes-layer-styles.html', 'kind': 'reference', 'note': 'Rolling Adobe reference; distinguish stable controls from Beta.'},
 'text-outlines': {'title': 'Adobe: Create masks and outlines', 'url': 'https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/work-with-masks/create-masks.html', 'kind': 'reference', 'note': 'Rolling Adobe reference; distinguish stable controls from Beta.'},
 'whats-new': {'title': 'Adobe: What is new through 26.5', 'url': 'https://helpx.adobe.com/after-effects/desktop/what-s-new/whats-new.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'beta': {'title': 'Adobe: After Effects Beta (separate from stable)', 'url': 'https://helpx.adobe.com/after-effects/desktop/what-s-new/after-effects-beta.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'known-issues': {'title': 'Adobe: Known issues by affected release', 'url': 'https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/known-issues-after-effects.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'quick-apply': {'title': 'Adobe: Quick Apply', 'url': 'https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/quick-apply.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'object-matte': {'title': 'Adobe: AI-powered Object Matte', 'url': 'https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'guides': {'title': 'Adobe: Guide creation and management', 'url': 'https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/guide-creation-and-management.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'effect-controls': {'title': 'Adobe: Effect Controls and instance labels', 'url': 'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'effects-overview': {'title': 'Adobe: Effect masks, opacity and animation presets', 'url': 'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effects-animation-presets-overview.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'proportional': {'title': 'Adobe: Proportional Scrubbing', 'url': 'https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-keyframes/proportional-scrubbing-in-timeline.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'layers': {'title': 'Adobe: Selecting and arranging layers', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-layers/select-and-arrange-layers/selecting-arranging-layers.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'svg': {'title': 'Adobe: SVG import and clipboard transfer', 'url': 'https://helpx.adobe.com/after-effects/desktop/import-files/import-svg-files/import-svg-files.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'variable-fonts': {'title': 'Adobe: Working with Variable Font Axes', 'url': 'https://helpx.adobe.com/after-effects/desktop/variable-font-axes/work-with-variable-font-axes/working-with-variable-font-axes.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'meshes': {'title': 'Adobe: Create parametric meshes', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/create-parametric-meshes/working-with-parametric-meshes.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'substance': {'title': 'Adobe: Apply Substance 3D materials', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/apply-substance-3d-materials.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'material-properties': {'title': 'Adobe: Modify materials and displacement', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-materials/modify-materials-properties-of-3d-layers.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'advanced-dof': {'title': 'Adobe: Advanced 3D in-engine depth of field', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/work-with-3d-scene-depth-data/enable-in_engine-depth-of-field-in-advanced-3d.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'noise': {'title': 'Adobe: Noise, grain and Curl Noise', 'url': 'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'keying-effects': {'title': 'Adobe: Keying and Unmult', 'url': 'https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'audio-effects': {'title': 'Adobe: Audio effects', 'url': 'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/audio-effects.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'copy-frame': {'title': 'Adobe: Copy Frame to Clipboard', 'url': 'https://helpx.adobe.com/after-effects/desktop/view-and-preview/copy-frames/copy-frame-to-clipboard.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'null-controllers': {'title': 'Adobe: Native null controllers', 'url': 'https://helpx.adobe.com/after-effects/desktop/drawing-painting-and-paths/null-controllers/create-nulls-for-positional-properties-and-paths.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'profiler': {'title': 'Adobe: Composition Profiler', 'url': 'https://helpx.adobe.com/after-effects/desktop/work-with-compositions/composition-profiler/composition-profiler.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'compressed-cache': {'title': 'Adobe: Lossless compressed playback', 'url': 'https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/lossless-compressed-playback.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'preview': {'title': 'Adobe: Previewing and Region of Interest', 'url': 'https://helpx.adobe.com/after-effects/desktop/view-and-preview/preview-video-and-audio/previewing.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'effect-manager': {'title': 'Adobe: Effect Manager', 'url': 'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-manager.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'data': {'title': 'Adobe: Data-driven animations', 'url': 'https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/data-driven-animation/data-driven-animations.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'h264': {'title': 'Adobe: Native H.264 Render Queue output', 'url': 'https://helpx.adobe.com/after-effects/desktop/render-and-export/export-h-264-from-the-after-effects/exporting-h264-from-the-after-effects-render-queue.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'mask-tracking': {'title': 'Adobe: Mask Tracking', 'url': 'https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-mask/rigid-mask-tracking.html', 'kind': 'reference', 'note': 'Stable 26.5 reference; rolling page, Beta labels still apply. See AUDIT.md for research evidence.'},
 'release': {'title':'Adobe: After Effects release notes (26.5, September 2026)', 'url':'https://helpx.adobe.com/after-effects/desktop/what-s-new/release-notes-after-effects.html','kind':'version','note':'Stable target: 26.5. Rechecked 2026-10-28; Beta remains separate.'},
 'history': {'title':'Adobe-maintained After Effects feature history','url':'https://github.com/AdobeDocs/after-effects-feature-history','kind':'version','note':'Historical introduction dates; current stable workflows target 26.5.'},
 'fixes': {'title':'Adobe: fixed issues in After Effects','url':'https://helpx.adobe.com/after-effects/desktop/troubleshooting/fixed-and-known-issues/fixed-issues.html','kind':'version','note':'Includes historical 25.6 fixes; document is rolling.'},
 'requirements': {'title':'Adobe: After Effects 26.x system requirements','url':'https://helpx.adobe.com/after-effects/desktop/get-started/technical-requirements/system-requirements.html','kind':'version','note':'Current Windows requirements applicable to 26.5; actual CPU/GPU architecture matters.'},
 'shortcuts': {'title':'Adobe: After Effects keyboard shortcuts reference','url':'https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html','kind':'reference','note':'Rolling shortcut page; compare against 26.5 installed editor.'},
 'help': {'title':'Adobe: After Effects documentation index','url':'https://helpx.adobe.com/after-effects/desktop.html','kind':'reference','note':'Rolling guide. Later-release features may appear.'},
 'effects': {'title':'Adobe: effect list and capabilities','url':'https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html','kind':'reference','note':'Rolling list; cross-check 26.5 installed Effects & Presets.'},
 'expressions': {'title':'Adobe: expression language reference','url':'https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html','kind':'reference','note':'JavaScript-like expression syntax; rolling documentation.'},
 'expressions-basics': {'title':'Adobe: understanding expression language','url':'https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-basics/expression-language.html','kind':'reference','note':'Expressions evaluate properties; distinct from ExtendScript automation.'},
 'color': {'title':'Adobe: color management','url':'https://helpx.adobe.com/after-effects/desktop/adjust-colors/color-management/color-management.html','kind':'reference','note':'ICC and OCIO pipelines; 26.5 bundles ACES 2.0 configurations.'},
 'ocio': {'title':'Adobe: OpenColorIO and ACES','url':'https://helpx.adobe.com/after-effects/desktop/adjust-colors/opencolorio-and-aces-color-management/opencolorio-aces-color-management.html','kind':'reference','note':'26.5 uses OCIO 2.5.1 with ACES 2.0 CG v4.0 and Studio v4.0.'},
 'mogrt': {'title':'Adobe: create Motion Graphics templates','url':'https://helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html','kind':'reference','note':'Essential Graphics/Properties/MOGRT general technique; rolling.'},
 'memory': {'title':'Adobe: memory and storage','url':'https://helpx.adobe.com/after-effects/desktop/memory-storage-performance/memory-and-storage/memory-storage1.html','kind':'reference','note':'Cache behavior; preference nomenclature varies by version.'},
 'multiframe': {'title':'Adobe: multi-frame rendering','url':'https://helpx.adobe.com/after-effects/desktop/render-and-export/multi-frame-rendering/multi-frame-rendering.html','kind':'reference','note':'Multi-Frame Rendering predates 25.6.'},
 'precompose': {'title':'Adobe: Precomposing, nesting, and pre-rendering','url':'https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html','kind':'reference','note':'Leave all attributes is not available for multiple layers, shape layers, or text layers; Adobe Help is rolling.'},
 'user-notes': {'title':'User-supplied AE Notes (26.5 starting point)','url':'','kind':'user material','note':'Adapted as a topic inventory and terminology starting point; Stable 26.5 coverage seed; verify factual claims against Adobe sources.'},
}

# Chapters progress IDs are permanent. Keep stable when editing exercises.
CHAPTERS=[]
def lesson(id,title,phase,why,steps,check,experiment='',pitfalls='',topics='',sources='help shortcuts',optional=False,diagram='layers'):
    CHAPTERS.append(dict(id=id,title=title,phase=phase,why=why,
      steps=[s.strip() for s in steps.strip().split('\n') if s.strip()],
      checks=[s.strip() for s in check.split('|') if s.strip()],
      experiment=experiment, pitfalls=[s.strip() for s in pitfalls.split('|') if s.strip()],
      topics=topics.split(),sources=sources.split(),optional=optional,diagram=diagram))

lesson('install','01 · Install, identify and prepare AE 26.5','START',
'Use the specified 26.5 stable build on Windows, with a reproducible workspace and no accidental version mismatch.', '''
Open Creative Cloud Desktop on Windows. Locate After Effects and check the installed version through Help → About After Effects. The target is 26.5 stable (September 2026). Beta is a separate installation; its tools are not automatically part of stable.
Before a large project, compare your Windows version, CPU architecture, RAM, GPU/driver and free storage with Adobe’s 26.5 requirements. AVX2 is required for supported Intel/AMD systems; Windows on Arm has its own supported Snapdragon hardware. A Windows VM must expose the required CPU/GPU capabilities; successful launch alone does not establish 3D performance.
Start AE and identify Project, Composition viewer, Timeline, Effect Controls, Effects & Presets, Properties, Preview and Render Queue panels. Hover any panel and tap the backtick key (`) to maximize/restore it.
Choose Window → Workspace, select a standard layout and use Reset to Saved Layout if panels are lost. Use Edit → Preferences to configure auto-save, disk cache and available memory without starving Windows.
Create a dedicated folder such as D:\\AE_Learning\\01_First_Project. Reserve an Assets subfolder, an Output subfolder and a project backup folder. Avoid relying on temporary Downloads files.
Open Edit → Keyboard Shortcuts (Ctrl+Alt+') to verify bindings on your installed version and keyboard layout. Save a custom preset only if you intentionally change a shortcut.
''', 'I can verify 26.5 and locate every central panel.|I have an organized Windows project folder.|I know where the shortcut editor is.',
'Break and restore a workspace layout, then find the Timeline and Effects & Presets in under 30 seconds.',
'Adobe Help can mix stable and Beta features; confirm the release label before using a new command.|Do not delete the disk-cache folder while AE is actively writing to it.',
'interface version-workflow performance project-management', 'release history requirements shortcuts memory',diagram='screen')

lesson('logic','02 · Understand projects, comps, layers and pixels','START',
'Build a correct mental model before memorizing commands.', '''
A .aep project is a container of references, compositions, settings and animation; imported images and video normally remain external files. Save Project is not the same as Collect Files or render.
Create a 1920×1080, 24 fps, 8-second composition with Ctrl+N. Name it 01_LAB. Distinguish composition size, frame rate, duration, pixel aspect ratio and background color; the comp background is not automatically an opaque render layer.
Create a blue solid (Ctrl+Y), a text layer (Ctrl+T in an appropriate context), and an empty shape layer (Layer → New → Shape Layer). Stack order determines which pixels cover which in ordinary 2D.
Select the blue layer: P=Position, S=Scale, R=Rotation, T=Opacity, A=Anchor Point. Use Shift+P to add Position while other properties are displayed, and U for animated properties.
Toggle a layer eye, shy, solo, lock, effects (fx), motion blur and 3D switch. Explain how hiding an entire layer differs from bypassing just its effects. F4 changes switches/modes columns.
Learn the vocabulary: footage item vs footage layer, source vs instance, composition vs precomposition, property vs keyframe, mask vs shape, alpha channel vs opacity, effect vs shape operator.
''', 'I can describe the project/comp/layer hierarchy.|I can distinguish source items from instances.|I can reveal five transform properties.',
'Duplicate the blue solid layer twice; assign each instance a different Opacity. Observe that all three layers refer to the same Solid Footage source in the Project panel.',
'Pressing a stopwatch that is already active removes its keyframes.|A background color setting does not add opaque pixels to your output.',
'interface layer-anatomy coordinates render-order',diagram='layers')

lesson('assets','03 · Import and inspect footage correctly','START',
'Learn what AE assumes when interpreting each media asset.', '''
Use Ctrl+I to import a PNG with alpha, a JPG, a short constant-frame-rate video, a WAV file and—when available—an image sequence. Check whether the source is a file, sequence or folder.
Double-click footage in Project to open its Footage panel. Compare footage time and frame dimensions with those of your composition. Drag footage into a comp; inspect scaling and frame-rate behavior.
Right-click footage → Interpret Footage → Main. Identify frame rate assumption, field order, pixel aspect ratio and alpha interpretation (straight vs premultiplied); note color options separately.
For an image sequence, select the first frame and use the sequence checkbox only when intended. Verify that frames were numbered without gaps and their order is correct.
Replace a selected layer’s source by Alt-dragging a different source from Project onto the layer. Confirm transform animation and effects remain in place. Distinguish replacing a layer source from replacing a Project item globally.
Make an Assets folder in Project, sort sources and keep originals on disk. If Windows drive letters or source folders change, use Replace Footage to relink the existing Project item; importing the same file again creates a separate item and may leave broken layer references unresolved.
''', 'I can interpret footage and verify source frame rates.|I can replace footage without losing a layer animation.|I know where a missing-file reference points.',
'Import a square logo and a wide logo, replace the first with the second using Alt-drag, and observe how the same Scale value affects each.',
'Variable-frame-rate recordings can cause erratic time or audio sync; use a constant-frame-rate transcode when needed.|Premultiplied alpha interpreted as straight can cause a dark fringe.',
'import-media alpha footage-interpretation file-management',diagram='layers')

lesson('timing','04 · Read time, frames, trims and the work area','START',
'The difference between layer time, source time and comp time prevents silent editing errors.', '''
In the Timeline, place the current-time indicator (CTI) at exactly 00:00:02:00 at 24 fps. Use Page Up/Page Down to step frames; Shift+Page Up/Down steps ten frames. Read timecode as hours:minutes:seconds:frames.
Use B and N to set an intentionally short work area. Start/stop Preview with Space; observe the Preview panel options. The work area is a range for preview/render control, not a change to source duration.
With CTI at 1 second, select a footage layer and press [ to shift its entire layer bar so the In point meets CTI. Next move CTI to 2 seconds, press Alt+[ to trim the In point without moving the entire layer. Undo twice and compare layer Start Time, In point and source frames.
Use Alt+] to trim the out point, Ctrl+Shift+D to split, Ctrl+D to duplicate, and I/O to jump to a selected layer’s in/out points. Practice knowing which commands change the source span.
Move the Timeline zoom using = / - on the main keyboard. Toggle full-span/single-frame viewing with ;. View one exact source frame, then locate it after shifting the layer.
Set marker(s) to plan beats. A composition marker differs from a layer marker; both differ from a keyframe. Save an experiment copy before drastic trimming.
''', 'I can step to a specific frame.|I know the distinction between moving, trimming and splitting.|I can define a work area.',
'Build a 4-second card transition that changes from a blue card to a red card at exactly 48 frames.',
'At 24 fps, :23 is the last frame within a numbered second; :24 is not an in-second frame.|The main keyboard 0 and numpad 0 may do different things.',
'frames timeline source-time',diagram='timeline')

lesson('transform','05 · Anchor, Position, Scale and parenting','START',
'Spatial transforms are predictable once you understand coordinate spaces.', '''
Draw a 200×200 rectangle in a Shape Layer. Press P to inspect the comp-space Position of the shape layer’s anchor; press A to inspect its layer-space Anchor Point (which may not coincide with the rectangle’s own group center). Changing one is not the same as changing the other.
Move the anchor with the Pan Behind tool (Y). Rotate with R; notice where rotation occurs. To center the anchor within content, test Ctrl+Alt+Home and compare the result with Ctrl+Home, which centers the layer’s anchor in the comp.
Create a Null Object (Ctrl+Alt+Shift+Y). Parent the shape and text to the null using the Parent & Link pick whip. Move, scale and rotate the null; then inspect each child’s local transform.
Unparent one child and watch its on-screen pose if AE compensates its transform. Explain why parenting does not mean copying Position keyframes or merging layers.
For a 3D layer, Position has three dimensions and rotation/orientation differs from the 2D case. Do not introduce a camera yet; use the 3D switch only for a controlled experiment.
Build a single controller named CTRL_RIG, and do not put unrelated effects on it. Label layers clearly and lock controllers when their position is correct.
''', 'I can tell anchor and position apart.|I can parent two layers to a null.|I can explain local vs comp coordinates.',
'Animate the null in a circle while rotating an independently animated child around its own pivot.',
'Changing a child parent can alter coordinate interpretation.|Centering a layer and centering its anchor are different commands.',
'coordinates parenting 3d-intro',diagram='coordinates')

lesson('keys','06 · Create and remove keyframes safely','FOUNDATIONS',
'Animate one number correctly before adding complex rigs.', '''
Add a Position keyframe at time 0 by clicking the stopwatch once. Move to 1 second and drag the object to a new Position. Inspect the two diamonds in the Timeline.
Return to time 0, reveal Opacity with T, set it to 100 and click its stopwatch to create the first Opacity keyframe. Then move to 2 seconds and change Opacity to 0 to create the second key. Without that first keyframe, the change at 2 seconds would simply set a constant value rather than a fade.
Select only one keyframe and press Delete. Rebuild it. To remove all Position keys, click the active stopwatch: observe that every keyframe vanishes and the current value is retained. Undo immediately.
Use U to show only animated properties, UU to show all properties modified from defaults, and K/J to jump visible keyframes/markers.
Use Alt+Shift+P or Alt+Shift+T to add/remove a key at CTI on the appropriate property; this does not toggle the whole property’s animation stopwatch.
Copy two selected Position keyframes, place CTI elsewhere and paste. Note that the first pasted key usually aligns with CTI. Use a separate duplicate layer to compare variations.
''', 'I can create, move and remove a single keyframe.|I understand the dangerous stopwatch toggle.|I can show only animated properties.',
'Animate a circle from x=200 to x=1720 in exactly 2 seconds, then fade it in for the first 12 frames.',
'Auto-keyframing can enable animation for new properties automatically; leave it off while learning.|Deleting one key is not the same as deactivating the stopwatch.',
'keyframes timeline',diagram='timeline')

lesson('easing','07 · Design motion with the Graph Editor','FOUNDATIONS',
'Good animation depends on velocity and spacing, not just destinations.', '''
Create Position keyframes 0 and 1 second, 800 pixels apart. Set both Linear, preview, and notice constant perceived speed on a straight path.
Select both keys and press F9 (Easy Ease). Use Shift+F3 to open the Graph Editor. Locate Speed Graph and Value Graph modes; for Position, choosing Separate Dimensions changes the way you can edit curves.
In Speed Graph, make the object accelerate quickly and decelerate gently. Preview and compare. Inspect motion-path dots: dense dots represent smaller distance per sample and hence slower motion.
Make a third middle Position key; separate spatial path curvature (trajectory) from the time interpolation (velocity). A curved path can move at constant speed, and a straight path can ease.
Use Easy Ease In/Out intentionally. For a stepped stop-motion look, test Toggle Hold Keyframe. Observe that Hold is not the same as a slow Bézier curve.
Open Keyframe Velocity (Ctrl+Shift+K) when numerical influence is necessary. Save a tiny file containing three clearly named easing examples.
''', 'I can explain speed vs value graphs.|I can make linear, eased and hold movement.|I understand spatial vs temporal curves.',
'Make three identical circles travel 500 px with linear, ease-out and overshoot movement; render a side-by-side comparison.',
'Tweaking spatial Bézier handles changes the path rather than temporal easing.|Position Separate Dimensions removes the unified motion path representation.',
'graph-editor keyframes motion-design',diagram='graph')

lesson('paths','08 · Draw shapes and parametric shape operators','FOUNDATIONS',
'Distinguish vector geometry, paths, styles and per-group transformations.', '''
Deselect all layers and use Q to draw a rectangle. It creates a Shape Layer. Expand Contents → Rectangle → Rectangle Path, Fill, Stroke, and the shape group’s Transform; compare with the layer’s separate Transform group.
Make an Ellipse and a Polystar with the Q tool cycle. Change parametric Size, Roundness, Points and radii. Do not convert to Bézier until you actually need manual vertices.
Use Contents → Add → Trim Paths and animate End from 0 to 100 on a stroked path. Set Start and Offset to explore moving a dash around a loop.
Use Repeater to create repeated copies of a group. Find Copies, Offset and Transform: Repeater → Position, Rotation, Scale. Explain why changing original geometry affects every repeated instance.
Explore Offset Paths, Pucker & Bloat, Zig Zag, Twist and Wiggle Paths one at a time. Turn each operator off and on to isolate its effect.
Convert a duplicated parametric path to Bézier; move a vertex with Pen/Selection tools. Try a closed filled shape and an open stroked path to compare filling behavior.
''', 'I can locate group Transform vs layer Transform.|I can animate Trim Paths and Repeater.|I can choose parametric vs Bézier geometry.',
'Make a rotating loading indicator consisting of twelve repeated ticks and a Trim Paths ring.',
'An empty Shape Layer has no visible pixels.|Shape operators are not in the Effect Controls effects list.',
'shapes paths strokes',diagram='layers')

lesson('masks','09 · Understand masks and alpha','FOUNDATIONS',
'Transparency has several independent sources, each suited to different work.', '''
Add a photograph to a comp. Select the photograph and draw a rectangle: it normally creates a mask on the selected layer. Deselect and draw another rectangle: it creates a shape layer. Check the toolbar mask/shape mode.
Press MM to reveal mask groups. For each mask test Mode Add, Subtract, Intersect and None, then change Feather, Expansion and Opacity and invert the mask.
Animate Mask Path over several frames to follow a moving subject. Make simple wide shapes first; excessive vertices are harder to stabilize and maintain.
Set a high feather value, then change layer Opacity separately. Inspect the Alpha channel via Alt+4. A transparent pixel can still have RGB values; alpha determines coverage.
Draw two masks on the same layer; test which mode is used and whether the order changes results. Enable/disable masks independently without deleting their path keys.
Precompose masked imagery and compare the look with and without Collapse Transformations in a controlled vector/precomp case; do not assume the switch is a free quality upgrade.
''', 'I can create a mask on a selected layer.|I can adjust feather, expansion and modes.|I can inspect actual alpha separately.',
'Cut a circular window into a photo and animate the window to follow a bouncing ball.',
'An animated mask is not a motion-tracked mask until you track it.|High feather is not a cure for poor matte edges.',
'masks alpha mattes',diagram='alpha')

lesson('mattes','10 · Use track mattes and blend modes','FOUNDATIONS',
'Mattes let one layer control visibility of another without drawing directly on the target.', '''
Create a text layer above a video layer. In the video layer’s TrkMat column select the text layer as its matte source. Modern AE track mattes can refer to another layer without that matte being directly above the target.
Test Alpha Matte versus Alpha Inverted Matte. Then use a luminance gradient and select Luma Matte versus Luma Inverted Matte. Identify what white, black and grey mean in each mode.
Try a transparent red-to-blue shape as a matte and inspect why its alpha can be constant although its luminance varies dramatically. Convert to grayscale for a predictable luma test.
Use F4 to reveal Switches/Modes where necessary. Compare Normal, Multiply, Screen, Add and Overlay on the same footage with two test layers.
Precompose only when the matte has to become a reusable source or when an effect must operate after the matte. A simple matte relationship does not automatically require a precomp.
Render to a format supporting alpha and verify transparency over a checkerboard outside AE. A matte preview on black is not proof that alpha was exported.
''', 'I can choose alpha vs luma matte.|I can invert either matte.|I can demonstrate an actual transparent export.',
'Make a 3-second title reveal in which video is visible only inside moving letters.',
'Screen blend mode against black does not create real alpha.|Layer opacity and track-matte coverage multiply in the final composite.',
'mattes blending alpha export',diagram='alpha')

lesson('precomp','11 · Precompositions, nested time and render order','FOUNDATIONS',
'Precomps organize work, but also change which operations happen first.', '''
Select three animated layers and precompose with Ctrl+Shift+C. Name the new comp 02_ICON_UNIT; with multiple selected layers After Effects uses Move all attributes into the new composition. To compare with Leave all attributes, make a separate single-layer footage/solid test (not a shape or text layer), precompose it, and inspect both dialog choices.
Open the precomp and note the inner time, duration, and layer layout. Return to the master comp and alter the precomp layer transform. Inspect whether the inner animation still plays as intended.
Apply Gaussian Blur to a shape, then precompose with different attribute settings; compare effect-before-transform with effect-after-transform. Render order is the reason precomposing can change an effect’s appearance.
In a duplicated test comp, toggle Collapse Transformations on the nested comp. Observe changed transformations, masks, 3D interactions and effect results rather than universally enabling the switch.
Use Time Remapping and an Essential Property only after the nested comp behaves consistently. Name instances uniquely when they need different controls.
Add a short marker on master comp corresponding to a specific event inside the precomp. Document any shifted inner start times and audio synchronization.
''', 'I can precompose with an intentional attribute choice.|I can explain a changed blur after precomposition.|I can locate inner vs outer time.',
'Build a lower-third as its own comp, duplicate it twice in a master comp and vary scale/timing without editing the internal artwork.',
'Collapse Transformations is not a generic quality switch.|Precompose can change how adjustment layers, 3D and effects interact.',
'precomp render-order essential-properties','help precompose',diagram='layers')

lesson('text','12 · Typography and animated text selectors','FOUNDATIONS',
'Type in motion is a system of characters, paragraphs, layout and animation selectors.', '''
Use Ctrl+T to create point text with a click and paragraph text by dragging a text box. Test different wrapping, alignment, font weight and paragraph settings in Character/Paragraph.
Make two headings with consistent font family and sizes; use tracking and leading intentionally. Use native text rather than rasterizing type when you need accessibility and later wording changes.
Expand Text → Animate → Position and add an Opacity animator. Open Range Selector → Advanced; compare Based On Characters, Characters Excluding Spaces, Words and Lines.
Animate Range Selector Offset from -100% to 100% to sweep a reveal. Compare Smoothness 0 to 100 and different selector shapes for stepped vs continuous entrances.
Use Text → Path Options when appropriate to put characters along a mask path. A text-on-path system is different from converting text to outlines.
Create two text layers, apply only a few font and style changes, and test 25.4+ copy/paste text formatting where available. Verify the paste action in the text editing context.
''', 'I can distinguish point and paragraph text.|I can animate words and letters separately.|I can use Range Selector Offset.',
'Make a 5-second kinetic typography card with per-word emphasis, clean baseline and a safe screen margin.',
'Per-character expressions added in 25.0 are different from variable-font axis animation introduced in 26.0.|Using the same keybindings while editing text can trigger text editing commands instead of layer shortcuts.',
'text text-animator type-design',diagram='layers')

lesson('effects','13 · Learn effects, order and adjustment layers','FOUNDATIONS',
'Effects compute images in sequence, and the order is part of the design.', '''
Create a solid with Fractal Noise; apply Levels, Tint, Turbulent Displace and Glow in that order. Duplicate the layer and reorder Glow before Levels. Compare the different result.
Open Effect Controls with F3. Rename each effect instance by its purpose. Toggle its fx switch; note that disabling an effect is nondestructive while Ctrl+Shift+E removes all effects from selected layers.
Make an Adjustment Layer (Ctrl+Alt+Y) and apply Curves. Put it above two footage layers; toggle layer order and note which lower pixels it modifies.
Compare an effect applied to a footage layer, the same effect on a precomp, and an effect on an adjustment layer. They do not use identical inputs in all cases.
Press Ctrl+Enter to open Quick Apply. Search e:glow, p: for presets or m: for menu commands; Enter applies the selected result. Use Effect → Manage Effects if an installed effect is disabled.
Test effect compatibility at 8, 16 and 32 bpc in Project Settings. An effect may process fewer bit depths or be CPU-only; check supported modes for the actual installed 26.5 effect.
''', 'I can rearrange effects to change render results.|I understand adjustment layers.|I can distinguish bypass from deletion.',
'Build a cloudy glow effect with at least four effects; save an Animation Preset for reuse.',
'In Quick Apply, Ctrl+Enter applies to a new layer and Ctrl+Alt+Enter to a new adjustment layer; outside it Ctrl+Enter opens the launcher.|An effect called a 3D effect does not necessarily create an actual 3D layer.',
'effect-order effects adjustment-effects quick-apply effect-labels','effects effects-overview quick-apply',diagram='effects')

lesson('blur','14 · Blur, glow, noise and depth maps','INTERMEDIATE',
'Understand the purpose of blur and procedural textures instead of applying random presets.', '''
Place Gaussian Blur on a photographic layer. Increase Blurriness and compare Repeat Edge Pixels on/off around the boundaries.
On a duplicate, use Camera Lens Blur and configure lens properties. Compare computational cost and appearance with a Gaussian Blur of similar apparent radius.
Generate a grayscale Fractal Noise texture on another layer. Use Displacement Map to warp a checkerboard; inspect map source channel, Max Horizontal/Vertical Displacement and map resolution.
Try Compound Blur or Camera Lens Blur with a blur/depth map and feathered transitions. A depth map controls *where* blurring occurs; it is not the same as overall lens bokeh settings.
Make a glow source by isolating bright pixels through Levels, then apply Glow with intentional Threshold, Radius and Intensity. Note why adding glow to a full-bright white rectangle washes out the whole scene.
Animate Fractal Noise Evolution and Offset Turbulence. Use it as a texture, matte, displacement driver or blend overlay, checking noise aliasing at final resolution.
''', 'I can choose ordinary vs lens-like blur.|I can use a grayscale map to deform or blur.|I can keep a glow controllable.',
'Build a heat-haze transition using Fractal Noise as an animated Displacement Map.',
'Curl Noise is available in 26.5 for flowing procedural textures; compare it with Fractal Noise rather than treating them as identical.|Too much glow can destroy edge contrast and alpha quality.',
'blur procedural depth-maps curl-noise','effects noise',diagram='effects')

lesson('timefx','15 · Time remap, speed, loops and motion blur','INTERMEDIATE',
'Temporal sampling affects motion even when no transform changes.', '''
Put a clip in a comp. Compare Time Stretch, Time-Reverse Layer (Ctrl+Alt+R), and Time Remapping (Ctrl+Alt+T). Record which changes source speed and which changes the timing of layer keyframes.
Enable Time Remapping on a duplicate and add a middle keyframe to speed up one segment and slow down another. Inspect interpolation: smooth time remapping can freeze or reverse segments.
For looping source playback, locate the final valid source frame and the default end-time key. Remove or adjust the problematic end key before adding loopOut('cycle') to Time Remap if required.
Use Posterize Time on a duplicate to create a stepped frame-rate aesthetic. Distinguish it from changing the *composition* frame rate.
Animate a fast-moving shape. Toggle its Motion Blur switch and the comp’s master Motion Blur switch. Adjust shutter angle and shutter phase under comp Advanced settings; judge at full speed.
Compare native motion blur with CC Force Motion Blur or Pixel Motion Blur where available. Third-party/plugins and frame interpolation may need substantially more rendering time.
''', 'I can reverse footage and remap it.|I can loop without an extra flash at the seam.|I can enable both motion blur switches.',
'Create three 2-second strips: smooth moving circle, 12-fps posterized circle and motion-blurred circle.',
'Motion blur is not added just because a layer has Position keyframes.|Time Remap source duration endpoints can be off by one visible frame.',
'time-remap frame-rate motion-blur',diagram='timeline')

lesson('audio','16 · Audio levels, waveform and reactive graphics','INTERMEDIATE',
'AE can synchronize and drive animation from audio, but is not a full DAW.', '''
Import a WAV with predictable beats. Press L for Audio Levels and LL (two quick taps) for its waveform; use numpad decimal for audio-only preview on a standard keyboard.
Set clear timeline markers at beats. Trim and reposition sound without accidentally offsetting its start relative to animated elements; use the Info panel if needed.
Select audio → Animation → Keyframe Assistant → Convert Audio to Keyframes. Inspect the resulting Audio Amplitude null and Both Channels Slider keyframes.
On a shape’s Scale, Alt+click the stopwatch and use a simple expression driven by the slider. For example: a=thisComp.layer('Audio Amplitude').effect('Both Channels')('Slider'); [100+a*2,100+a*2];.
Smooth noisy values with the smooth() expression when needed or keyframe smoothing, and clamp extreme peaks. Build a minimum scale so silence does not collapse the graphic.
Export a preview and listen to it. Audio playback from the computer can differ from a final encoded render; check that audio output is explicitly enabled in the Output Module.
''', 'I can reveal an audio waveform.|I can convert audio to control keys.|I can make a shape pulse to audio.',
'Animate a 5-bar equalizer-like display using five linked or differently remapped audio amplitude values.',
'Audio amplitude generated by the assistant is a numerical representation, not a beat classifier.|An audio effect can modify the sound, not just a visible waveform.',
'audio audio-reactive expressions',diagram='timeline')

lesson('keying','17 · Green/blue-screen compositing','INTERMEDIATE',
'Professional keying separates core opacity, edge detail and spill removal.', '''
Import evenly lit green-screen footage. Put a contrasting background beneath it, then apply Keylight (1.2) to the footage.
Pick a representative green Screen Colour away from hair/skin. Switch Keylight View to Screen Matte. Adjust Clip Black and Clip White moderately to establish opaque subject and clean background.
Inspect fine hair and semi-transparent material. Use Screen Shrink/Grow and Screen Softness carefully; extreme crushing loses legitimate edge detail.
Add Key Cleaner and Advanced Spill Suppressor after Keylight when useful. Compare suppression modes and check green reflections in grey or skin regions.
Use a garbage mask to eliminate off-screen gear and nonuniform regions before or alongside keying. Use separate inside and edge mattes for challenging footage rather than forcing one setting for every region.
Check the keyed subject against black, white, saturated grey and final intended background. Add light wrap/grade if visually needed, but keep a clean premultiplied edge.
''', 'I can read the Keylight screen matte.|I can distinguish matte cleanup from spill suppression.|I can inspect alpha on four backgrounds.',
'Produce a 5-second talking-head composite against a still photograph, with stable hair edges.',
'Cranking Clip Black/White removes real fine detail.|Luma matte does not automatically replace chroma keying.',
'keying alpha compositing',diagram='alpha')

lesson('tracking','18 · Track a moving point and stabilize motion','INTERMEDIATE',
'Tracking turns observations in footage into reusable transformations.', '''
Select a footage layer and open Window → Tracker. Choose Track Motion. Start with a high-contrast feature that does not rotate out of view; define Feature and Search Regions.
Track forward in small portions and inspect drift. Set the Attach Point thoughtfully; the feature region may move while the attachment stays separately positioned.
Create a Null, set Edit Target to that Null, and Apply the tracking data. Parent a graphic to the null rather than pasting tracking keys into every child.
Enable rotation and scale tracking by using two tracking points when the footage supports stable features. Know that point trackers cannot inherently solve full perspective deformation.
Use Stabilize Motion on a duplicate; note how the image edges move and why you may need scaling/cropping or synthesis for blank edges.
For planar surfaces and perspective replacement, open bundled Mocha AE, track a plane, then send corner-pin data back into AE. Verify the exact Mocha integration commands in the installed plugin version.
''', 'I can apply a point track to a Null.|I can detect and repair track drift.|I can distinguish point tracking from planar tracking.',
'Track a moving label onto a high-contrast point on a recorded object for 3 seconds.',
'A successful tracker preview can still drift after an occlusion.|Warp Stabilizer is not a simple replacement for perspective planar tracking.',
'point-tracking mocha stabilization',diagram='coordinates')

lesson('roto','19 · Roto Brush, Refine Edge and mask tracking','INTERMEDIATE',
'Extract moving subjects without the 2026 Object Matte feature.', '''
Duplicate a video layer and open that layer in the Layer panel, not only the Composition panel. Activate Roto Brush (Alt+W) and create foreground strokes where the intended subject has recognizable edges.
Use Alt with the brush, where supported, to subtract incorrectly selected regions. Identify the base frame and propagate forward/backward through a manageable span.
Scrub the full span and repair frames that drift, especially fast-moving hands, occlusions and hair. Use Refine Edge on semitransparent detail only after the main segmentation is stable.
Adjust Reduce Chatter, Feather, Shift Edge and Decontaminate Edge Colors as warranted, then Freeze propagation for the span. Keep the source footage available; Freeze is not the same as rendering a permanent matte file.
Use Mask Tracking on an appropriately drawn mask for rigid, easy-to-follow objects. If motion is complex, consider manual correction or a separate point/planar track.
Pre-render a clean RGBA intermediate when editing further becomes slow; verify that the output format actually retains an alpha channel.
''', 'I can roto a 2-second moving subject.|I understand propagation and Freeze.|I can choose mask tracking vs Roto Brush.',
'Cut a person out of an indoor clip and place a moving procedural texture behind the subject.',
'Object Matte is also available; compare subject selection with brush-guided roto and mask tracking.|Freezing a roto span does not replace checking every frame.',
'roto alpha mask-tracking',diagram='alpha')

lesson('paint','20 · Paint, clone and Content-Aware Fill','INTERMEDIATE',
'Moving from an obvious brush stroke to credible invisible repair requires temporal checking.', '''
Double-click footage to work in the Layer panel. Use Brush, Clone Stamp and Eraser there; the same tool is not just a normal Comp-view shape brush.
Set a Clone Stamp sampling point with Alt+click. Paint a small patch on a duplicate and test source alignment and stroke duration modes in the Paint panel.
Make a simple repair with painting, then preview over time. A correction that matches one frame can slide or flicker after motion unless properly tracked or the paint is adjusted.
Use a mask around an unwanted object, follow it with keyframes or tracking, and open Window → Content-Aware Fill. Select the appropriate Fill Method and Range, then Generate Fill Layer.
For a difficult frame, create a reference frame in Photoshop (when available) or a suitable still-image editor; fill the defect and return the reference to AE. Manage source paths and regenerated fills.
Evaluate repeated textures, camera motion, shadows and occlusion. Sometimes a clean plate plus planar tracking is more reliable than automated Fill.
''', 'I can clone a small detail.|I can generate a Content-Aware Fill layer.|I know when to use a tracked clean plate.',
'Remove a small stationary sticker from a 2-second shot with a moving handheld camera.',
'Brush/Clone Stamp stroke duration matters.|Content-Aware Fill may hallucinate repetition or change a texture over time.',
'paint content-aware-fill masks',diagram='layers')

lesson('camera','21 · 2.5D parallax, cameras and lights','INTERMEDIATE',
'AE 3D layers exist in 3D space, but not every 3D-looking effect behaves as scene geometry.', '''
Turn on 3D switches for several photos or shape layers and separate them in Z depth. Create a Camera (Ctrl+Alt+Shift+C). Distinguish 1-node and 2-node camera behavior, point of interest, zoom and field of view.
Create a Camera orbit Null and parent the camera to it for controlled moves, or animate camera Position/Point Of Interest intentionally. Use multiple views to check that foreground and background have the desired depth separation.
Add a Light (Ctrl+Alt+Shift+L) and test Material Options on 3D layers. Understand Accepts Lights/Shadows and limitations of the selected 3D renderer.
Switch Project Settings/Composition Advanced 3D renderer only intentionally; Classic 3D, Cinema 4D and Advanced 3D do not have identical feature sets. Test native 3D models where supported.
In After Effects 26.5, select multiple 3D layers to use the shared/single 3D transform gizmo; also inspect View → Default Camera Settings for the new default camera controls.
For camera depth of field, use Advanced 3D’s in-engine DOF (available since 26.3) and inspect Camera Options focus and aperture. A 2D Camera Lens Blur map is a different workflow.
''', 'I can make a 3-layer parallax scene.|I can distinguish renderers and camera types.|I can locate shared gizmo controls.',
'Create a 6-second dolly move through three cut-out images at different Z positions, avoiding obvious image edges.',
'2D effects like CC Sphere or 3D Channel effects do not become scene geometry by naming alone.|Advanced 3D renderer feature support differs from Classic 3D.',
'3d-intro cameras 3d-renderers 3d-models', 'release history help',diagram='coordinates')

lesson('3dtrack','22 · Camera tracking and screen replacement','INTERMEDIATE',
'Choose a scene-solving tool based on camera motion rather than the look of the final effect.', '''
Use a shot with real parallax: camera moves through a room rather than only rotating from one point. Apply 3D Camera Tracker and allow Analysis/Solving to finish.
Inspect the track points and locate a plausible horizontal plane. Target a triad and create a Solid/Camera or Text/Camera. Check the solved graphic over all frames, not only the initial one.
If the solve is unstable, inspect fast pans, rolling shutter, motion blur, zoom changes, focal length and low-parallax shots. Trim and stabilize the analysis source where justified.
For a planar phone screen, compare Mocha AE corner pin or built-in perspective tracker. Use a high-contrast planar patch, not an assumption that a 3D camera solve will always be superior.
Track a sign or poster, then apply Corner Pin/CC Power Pin to the replacement screen. Control the insert’s color, noise and motion blur to match the plate.
Export a diagnostic video showing the tracker points or a checkerboard overlaid on the final surface; a drifting corner is easier to catch with a grid than with a textured replacement.
''','I can solve a simple parallax clip.|I can choose a planar track for a screen.|I can check perspective replacement on every frame.',
'Replace a moving phone screen with a checkerboard, then with a custom animated interface.',
'3D Camera Tracker will not solve every low-parallax or heavily blurred clip.|Screen corner tracking is not equivalent to full-scene camera recovery.',
'camera-tracker mocha perspective',diagram='coordinates')

lesson('color','23 · Color correction, working space and alpha','INTERMEDIATE',
'Correct color requires keeping separate input interpretation, working-space math, display, and output.', '''
In File → Project Settings → Color, compare color-managed versus unmanaged workflows in a small 8/16/32-bpc experiment. Choose an intentional Working Color Space for the target delivery.
Inspect an imported image’s Interpret Footage color settings. When necessary, assign the right input profile; assigning a profile changes interpretation and is not the same thing as changing RGB values with an effect.
Use Lumetri Color, Curves and Levels on a test image. Correct exposure/contrast/white balance first, then make a look. View histograms or scopes where available and compare to a controlled reference.
Understand straight vs premultiplied alpha and RGB in transparent pixels. Remove Color Matting when necessary; a matte halo is not always fixed by globally sharpening an image.
For an OCIO/ACES workflow, open Project Settings → Color, select OCIO color managed, choose ACES 2.0 CG v4.0 or Studio v4.0, and explicitly set input, working, display and output spaces. Test a short render before changing an established project’s configuration.
Export a tagged test image/video and compare the rendered file in a color-managed viewer. Different Windows video apps may apply different display transforms; check metadata, not just eye judgment.
''','I know input vs working vs display vs output space.|I can explain 8/16/32 bpc.|I can test alpha against light/dark backgrounds.',
'Grade the same PNG to neutral in an 8-bpc unmanaged project and a 16-bpc color-managed project; document the differences.',
'Increasing bpc does not restore clipped source data.|Changing an existing project’s ACES configuration can change its appearance; preserve a known-good copy and compare renders.',
'color color-depth ocio alpha', 'color ocio history',diagram='effects')

lesson('expressions','24 · Expressions: build a repeatable controller','INTERMEDIATE',
'Expressions compute property values; learn safe interfaces before writing complex JavaScript.', '''
Create a Null named CTRL. Apply Effect → Expression Controls → Slider Control, rename it Speed. On another layer’s Rotation, Alt+click its stopwatch once and enter time*thisComp.layer('CTRL').effect('Speed')('Slider');.
Set Speed to 0, 90 and -45; verify that the graphic stops, rotates clockwise and counterclockwise. Your expression needs a numeric output because Rotation expects a scalar.
On a 2D Position property, enter wiggle(1,20); and compare with value+[Math.sin(time*2)*20,0];. Distinguish nondeterministic-looking wiggle from smooth periodic motion.
Make a 2D Scale expression using [100,100] or [s,s], not a lone scalar. Learn value, time, thisComp, thisLayer, framesToTime(), ease(), linear(), clamp(), loopOut().
Create two expression-linked layers using the pick whip rather than manually typing names, then rename a controller and inspect references. Handle missing effects or source layer changes carefully.
Toggle an expression off without deleting it. Use Animation → Keyframe Assistant → Convert Expression to Keyframes to bake a copy when needed for portability or delivery.
''', 'I can create a slider-controlled rotation.|I can return the correct value dimension.|I can disable vs delete an expression.',
'Build one Null with Speed, Amount and Color Control driving a three-layer animated indicator.',
'Expressions are not general browser JavaScript; DOM/HTML APIs are unavailable.|An expression controller can introduce a fragile dependency on its layer name.',
'expressions expression-language expression-controls expression-examples expression-lookup', 'expressions expressions-basics',diagram='layers')

lesson('data','25 · Data-driven text and graphics','ADVANCED',
'Separate content from animation so recurring work is faster to update.', '''
Create a small UTF-8 CSV or TSV with name, score and color columns. Import it as data through File → Import and inspect its accessible data properties.
For JSON use footage('stats.json').sourceData.score. For CSV/TSV add the data item to a test comp, expand Data and pick-whip the intended cell; inspect its generated dataValue path and compare against the table before building row logic.
Create a Score text layer and set Source Text from a suitable string expression. Format numbers deliberately with Math.round(), toFixed() or String() where appropriate.
Build a background rectangle sized to text with sourceRectAtTime(); add horizontal and vertical padding, and inspect left/top offsets to avoid misalignment.
Try importing a small JSON object as footage and reading a nested key by expression using footage('filename.json').sourceData. Keep field names stable and check for missing keys.
Make a reusable template with editable content and named controls. Document what changes without touching timeline keys.
''','I can import one data file.|I can link text to a value.|I can keep animated layout working after the string changes.',
'Make a three-slide statistics board generated from a CSV, each with an auto-sized number card.',
'Imported data schema paths are easy to misaddress: inspect the data structure.|SourceText may contain formatted objects; test with the target 26.5 JavaScript expression engine.',
'data expressions auto-layout','data expressions',diagram='layers')

lesson('templates','26 · Essential Properties and MOGRT delivery','ADVANCED',
'Build assets that another editor can adjust without breaking a controlled design.', '''
Create a child comp containing a title, subtitle, color plate and simple entrance animation. Open Window → Essential Graphics and select the correct master composition.
Expose editable Source Text, key color controls and a Slider into Essential Graphics. Rename controls clearly, group when appropriate and provide default values.
Nest the child comp twice; inspect Essential Properties for each instance. Change one instance’s title and color while retaining the original child comp and other instance.
Test protected regions for intro/outro timing when building a reusable MOGRT, then stretch a middle region in a deliberately long test comp. Check that animation does not overlap unexpectedly.
Export a Motion Graphics Template (.mogrt) and choose the correct destination; use a video preview where supported. Verify third-party fonts/plugins or expression dependencies.
Open or install the MOGRT in a compatible Adobe workflow where available; test exposed controls, resolution and duration. Retain the original .aep and assets as source of truth.
''','I can expose one editable text property.|I can customize two comp instances.|I know the distinction between a .mogrt and an .aep.',
'Make a lower-third MOGRT with name, role, primary color and adjustable hold duration.',
'MOGRT export cannot magically package every third-party dependency.|Essential Properties are instance overrides, not a replacement for all original animation data.',
'essential-properties mogrt precomp', 'mogrt',diagram='layers')

lesson('advanced3d','27 · Native 3D models, environments and renderers','ADVANCED',
'Combine imported models with native meshes and supported materials in Advanced 3D.', '''
Import a supported GLB/GLTF/OBJ or FBX model appropriate to your project. Inspect scale, axes, texture material paths and animation playback.
Create a 3D composition using the Advanced 3D renderer. Add an environment light or HDRI for reflections and test an animated environment light (introduced in 25.2).
Check each model’s Material Options, Accepts Lights, Shadows and shadow-catcher workflow. Compare quality/performance options and confirm the actual render, not only Fast Draft.
Use the shared single 3D gizmo on multiple selected 3D layers (25.6 feature) to transform as a group visually. Learn that it changes individual layers; it is not necessarily a persistent parent rig.
Change View → Default Camera Settings (25.6) to adjust the way default/custom views behave. Save a test and inspect composition views before and after.
Create a native mesh with the Parametric Mesh tool or Layer → New. Adjust Mesh Options and material roughness/metallic controls; import an SBSAR material to compare. Keep this separate from Beta-only materials on 3D text/shapes.
''','I can import one model and light it.|I can test an environment light.|I can compare imported models and native meshes.',
'Build an 8-second product turntable using a supported 3D model and a controlled camera orbit.',
'3D model and material import support varies by format/renderer.|An emissive-looking material does not illuminate nearby geometry; use an actual light for that.',
'3d-models 3d-renderers cameras parametric-meshes substance-materials', 'release history meshes substance',diagram='coordinates')

lesson('puppet','28 · Puppet rigging and deformation','ADVANCED',
'Animate flexible artwork without cutting it into dozens of rigid pieces.', '''
Import a transparent character or ribbon. Duplicate the source and apply Puppet pins to a clean alpha layer while in the relevant Puppet tool mode.
Add pins to stable regions first: base/shoulder, elbow and tip. Move a single pin over time and inspect how the mesh deforms between pins.
Explore Overlap and Starch tools to control drawing order and rigidity in supported Puppet modes. Place pins where the mesh should bend and where it should resist stretching.
Reduce pin counts until you can understand every pin. An over-constrained mesh creates awkward hard bends or almost no visible motion.
Precompose when the Puppet effect needs to move with a separate rigid transform. Compare deform-then-scale with scale-then-deform in your hierarchy.
Render a seamless 2-second loop; inspect pin intersections and anti-aliased alpha edges at every extreme.
''','I can make a simple Puppet mesh.|I can set stiffness/overlap deliberately.|I can animate a clean loop.',
'Make a waving flag or cartoon arm bend while its base remains fixed.',
'Puppet is a deformation tool, not skeletal 3D rigging by itself.|Tiny transparent holes can distort a mesh unexpectedly.',
'puppet alpha precomp',diagram='layers')

lesson('particles','29 · Native particle and simulation systems','ADVANCED',
'Learn particle emitters, lifetimes and physics controls through measurable experiments.', '''
Apply CC Particle World to a solid. Find Producer Position and Radius, Birth Rate, Longevity, Particle Type, Velocity, Gravity and Resistance controls.
Set Birth Rate low and Longevity short. Measure how many visible particles appear at once; rough steady count depends on rate × lifetime, though frame integration and fade settings affect the rendered result.
Make a second particle system using CC Particle Systems II. Compare available controls and rendering performance instead of assuming both systems are interchangeable.
Try CC Rainfall or CC Snowfall and then Foam or CC Bubbles. Understand emitter-based versus image-distortion-based animation.
Precompose particle sources when layering glow, blur and mattes. Test whether effect order changes source/particle size or the glow of particles.
Make a 5-second rain field that respects foreground occlusion via track matte and includes variation in size, velocity and blur.
''','I can control birth rate and lifetime.|I can compare native particle tools.|I can matte particles behind an object.',
'Create a burst that emits for 12 frames, falls under gravity and fades within 3 seconds.',
'Particle count is not simply Birth Rate without accounting for particle lifetime.|Some CC effects expose controls in normalized coordinates, not comp pixels.',
'particles simulations effects',diagram='effects')

lesson('render','30 · Render Queue, codecs, alpha and audio','DELIVERY',
'Choose the output to match its downstream use and verify what the render actually contains.', '''
Save your project. Select the final composition and use Ctrl+Shift+/ to add it to Render Queue. Inspect Render Settings, Output Module, and Output To separately.
Set a working review output, such as an H.264 MP4 where the installed 26.5 encoder and selected output route support it. Alternatively queue an Adobe Media Encoder output using Ctrl+Alt+M. Do not rely on one codec for every delivery.
For a master or intermediate, choose a high-quality suitable codec such as ProRes or DNxHR (where available), or an image sequence. Specify bit depth, frame rate, color tagging and audio as intended.
For transparency, use a format/codecs that support alpha, select RGB+Alpha, and specify Straight or Premultiplied according to downstream requirements. Standard H.264 MP4 generally does not carry normal AE RGBA transparency.
Render only intended work area or entire comp explicitly. Check that the final frame, 100% resolution, high-quality sampling and motion blur correspond to your delivery requirements.
Open the rendered output in a separate player/editor. Count frames, inspect audio sync, color, alpha and first/last frame. A successful Render Queue status does not certify the file is correct.
''','I can export a review movie and an RGBA master.|I can distinguish render settings vs output module.|I can inspect a render externally.',
'Deliver one MP4 review, one transparent master or PNG sequence, and a written export checklist.',
'Choosing RGB+Alpha does nothing if the selected codec/container cannot carry an alpha channel.|Rendered H.264 export is not the same as saving an editable project.',
'export codecs alpha audio',diagram='timeline')

lesson('collect','31 · Backups, Collect Files and team handoff','DELIVERY',
'Keep a project reproducible after assets move or the original editor is unavailable.', '''
Save the working .aep, then use File → Dependencies → Collect Files to gather used sources into a package. Read the available options and select a dedicated collection folder.
Relocate/copy the collected folder to a different Windows path or drive letter, open the collected .aep and verify it uses collected assets rather than the old disk locations.
Audit installed fonts, effects, scripts, external 3D textures, render destinations, proxies and dynamically linked dependencies. Collect Files is not a guarantee of third-party plugin portability.
Generate an explicit README listing AE version 26.5, frame rates, render settings, color management, input dependencies, licensed assets and any known limitations.
Use versioned project saves such as Project_v001.aep and Increment and Save; maintain automated backups where configured. Restore a backup before trusting the process.
Consider making a high-quality pre-render or flattened proof video for reviewers who cannot open AE. Keep editable project and rendered approval media separate.
''','I can collect and reopen a project from a new path.|I have a dependency manifest.|I can restore a previous project version.',
'Move the collected package to a different drive/path and re-open all comps without missing-file dialogs.',
'Collect Files does not bundle Adobe subscription licenses or every installed plugin.|An .aep file by itself often cannot reproduce a project.',
'project-management collect-files export',diagram='layers')

lesson('performance','32 · Performance, memory, cache and proxies','DELIVERY',
'Optimize the actual bottleneck instead of deleting caches reflexively.', '''
Save a slow experiment project. Time a cold preview and a repeated warm preview over the same work area before changing settings.
Set viewer resolution Half or Quarter for fast interaction when appropriate; note that changing view quality does not automatically guarantee a full-resolution final render.
Inspect Edit → Preferences → Memory & Performance and Disk Cache settings. Reserve adequate RAM for Windows, choose a fast drive with spare capacity, and understand that purging invalidates useful cached frames.
Compare one CPU-bound procedural effect, GPU-accelerated effect, and codec-decoding bottleneck. Watch whether performance changes when an effect switch is turned off.
Use proxy footage or pre-renders for expensive sources and comps when appropriate. Keep a clear replacement/restore path so that final output uses the intended sources.
Check Multi-Frame Rendering and limitations of plugins. For a pathological project, disable suspect third-party effects one at a time and test safe startup rather than assuming the GPU always causes slowdowns.
''','I can separate first render from cached preview.|I can find RAM and disk-cache settings.|I can make a measurable performance comparison.',
'Create a before/after timing sheet for a 5-second heavy effects comp with two controlled optimization changes.',
'Clearing the disk cache can make a project slower temporarily.|A faster SSD does not cure an expensive single-frame effect algorithm.',
'performance cache proxies', 'memory multiframe',diagram='effects')

lesson('debug','33 · Diagnose broken results systematically','DELIVERY',
'Identify whether a problem is source, interpretation, transform, matte, effect, render or environment.', '''
When the Comp viewer is black, check active comp, time, layer In/Out, eye, solo, opacity, mask, matte, blend mode and viewer channel before touching effects.
If the result is different after precomposing, compare render order, collapse transformations, effect stacks, adjustment layer scope and color management.
If preview is frozen, disable Caps Lock, inspect Preview settings and work area, then confirm a frame has been rendered. Restart only after a simple reproducible check.
If an effect is missing, inspect Effect Manager, plugin installation, 8/16/32-bpc support and whether it is stable in 26.5 or Beta-only. Replace unsupported features rather than inventing a hidden menu.
If output differs from Comp viewer, compare Render Settings, Output Module, output color space, channel selection, renderer and file playback transform.
Create a reduced reproducible .aep by duplicating the comp and removing half of its layers/effects, repeatedly narrowing the issue. Save before deleting or purging.
''','I can isolate a black-frame cause.|I can compare viewer/render settings.|I can build a minimal reproduction.',
'Intentionally hide a layer with a matte and an effect, then diagnose the failure in a fixed checklist without random clicking.',
'A render queue completion message means the job finished, not that visual, alpha or audio QC passed.|Caps Lock can inhibit viewer updates.',
'diagnostics missing-effects alpha color',diagram='screen')

lesson('automation','34 · ExtendScript, scripts and batch workflow','ADVANCED',
'Understand which tasks need property expressions and which need application automation.', '''
Distinguish expressions (a formula on a property, evaluated over time) from ExtendScript/JSX scripts (commands that build or edit project objects). A property expression cannot import and rename 200 files or create arbitrary layers.
Learn the project object model at a high level: app.project, items, compositions, layers, properties, keyframes, and render queue items. Keep automation scripts narrowly scoped.
Create a reversible experiment: a simple JSX script run through File → Scripts → Run Script File that makes a named solid and saves no files automatically. Review permissions/prefs relevant to scripts before running.
Use undo groups around edits and test on a copy. Always guard the selected item type and active composition before dereferencing it.
For external data, prefer explicit JSON/CSV inputs, deterministic naming and a record of generated assets. Do not put sensitive information inside easily shared project expressions.
Try a batch task such as renaming layers with a prefix or setting comp frame rates only after manually checking the intended targets. Compare before/after project structure.
''','I can distinguish JSX scripts from expressions.|I can describe project item vs layer objects.|I can test scripts safely on a copy.',
'Write a short JSX script that enumerates comp names and reports them, without changing the project.',
'Scripts can alter a project or access files; only run code you understand and trust.|An expression’s JavaScript support is not the same as a script’s API.',
'scripting expressions project-management expression-examples','help expressions',diagram='layers')

lesson('capstone','35 · Complete project: 10-second motion graphics composite','CAPSTONE',
'Combine foundations, animation, keying, data, effects, sound and export into a repeatable deliverable.', '''
Create a clearly labeled 1920×1080 24 fps comp called FINAL_10S. Import or generate a 10-second background, a branded shape/title, and short WAV music/sound effects; keep the source files in project Assets.
Build a 2-second introductory title. Use a masked or matted reveal, controlled easing, and motion blur. Keep typography clear and safe from frame edges.
At 2–6 seconds, animate a set of three cards with a Null controller and either a text animator or template-driven properties. Make their timing editable without rebuilding the graphic.
Add a short compositing moment: tracked corner-pin insert, a keyed subject or a clean roto. Do not fake one if source footage is unavailable; use a self-generated shape/matte demonstration and document the substitution.
At 6–9 seconds, finish a procedural transition using Fractal Noise, Displacement Map or Glow. Audio should enter and leave cleanly, and the last second should contain a readable final message.
Audit at Full resolution: typography, alpha edges, layer order, no one-frame flash, camera position, color and clipping. Render a review movie and an archival-quality master; collect project files and write a delivery note.
''','I can deliver a complete timeline.|My project reopens without missing assets.|I can explain every element and effect in the render.',
'Grade yourself: can you rebuild 80% of the sequence from scratch with your own footage and no tutorial?',
'Do not judge a project only by rendered appearance; reproducibility and clean dependencies matter.|Use the stable 26.5 feature set throughout and document dependencies.',
'workflow capstone export project-management',diagram='timeline')


lesson('modern-operations','00 · Quick Apply, guides and effect organization','FOUNDATIONS',
'Use the current interface to locate operations and build consistent layouts.', '''
Create a duplicate of your title comp. Press Ctrl+Enter, type e:glow and apply the result to the intended layer with Enter; F3 opens its controls.
Reopen Quick Apply and inspect p: and m: results. On a disposable comp try Ctrl+Alt+Enter inside the launcher to create an adjustment layer, then compare which pixels change.
Rename effect instances by purpose and give them distinct color labels using the gray swatch beside each effect name. Bypass one fx switch and compare before deleting anything.
Show rulers with Ctrl+R. Add a 50% vertical guide and a 100-pixel right-edge guide via Edit Guide; change a duplicate composition’s width and compare.
Lock guides independently from pinning. Export a .guides file and import it into another view, checking units, colors and reference edges in the destination.
Choose an effect you use often and save a deliberate Animation Preset. Apply it to a duplicate at a known playhead time and inspect the added properties and keys.
''','I can use Quick Apply result modifiers.|I can explain fixed versus percentage margins.|I can distinguish effect labels from processing.',
'Build landscape and portrait title variants with the same intended margins; explain which artwork still needs repositioning.',
'Guides do not reposition layers automatically.|A preset can add keyframes at CTI and change an existing setup.',
'quick-apply responsive-guides effect-labels clipboard-frame','quick-apply guides effect-controls',diagram='screen')

lesson('object-selection','00 · Object Matte with frame-by-frame quality control','INTERMEDIATE',
'Use the current selection workflow and verify its cached propagation.', '''
Choose a two-second shot with a clear subject and preserve the original footage. Double-click the layer into Layer panel and choose the Object Matte toolbar tool.
Hover the subject and click to select; correct the base frame using Quick Selection or Selection Brush. Use Refine Edge for appropriate hair detail.
Propagate across the intended range; inspect occlusions, hands and fast turns. Correct failed frames instead of assuming a green cache bar proves accuracy.
Freeze the reviewed result and return to Composition. Compare it over black, white and saturated backgrounds, inspecting alpha as well as RGB.
Save and reopen a test project. Compare 26.5 disk-cached propagation, then render an alpha-capable short master; retain source media and the project separately.
Use the isolated layer as an Alpha Matte for a separate animated texture. Verify it follows the silhouette without unnecessarily showing the matte as an independent layer.
''','I can select and refine an object.|I can judge matte stability across frames.|I can distinguish disk-cached analysis from a final RGBA export.',
'Compare Object Matte and brush-guided roto on the same difficult turn and keep the cleaner result.',
'Ctrl+W is documented ambiguously; choose the toolbar or verify the installed editor.|A cache is not an asset backup.',
'object-matte roto mattes','object-matte shortcuts',diagram='alpha')

lesson('modern-type','00 · SVG and variable-font motion','INTERMEDIATE',
'Bring editable vectors into a current typography workflow.', '''
Import samples/badge.svg as footage and again as a composition. Compare source linkage, editable Contents and the rendered appearance.
If Illustrator is available, enable Include SVG Code in its Clipboard Handling preferences, copy outlined vector art and paste into an active AE comp. Inspect fills and grouping.
Create a text layer using an installed variable font. Expand Text → Animate → Variable Font Axes and choose an axis that the font actually supports.
Create an initial axis keyframe at time zero, move 24 frames and change the value within its supported range. Add a Range Selector for character timing.
Compare Variable Font Spacing modes and long/short text strings. Use native shapes or text layers deliberately; editable SVG geometry is not editable Illustrator text.
Render a 48-frame sample and inspect sharpness, glyph spacing and line wrapping. Record the exact font family/file needed for handoff.
''','I can choose editable SVG or linked footage.|I can animate an available variable-font axis.|I can verify typography dependencies.',
'Make a two-second badge reveal with a weight change and a Trim Paths accent.',
'Use a variable font, not merely a static family with several weights.|SVG text clipboard conversion is not supported by the stable shape route.',
'svg-workflow variable-fonts text-animator','svg variable-fonts',diagram='layers')

lesson('flow-alpha','00 · Curl Noise, Unmult and audio dynamics','INTERMEDIATE',
'Use current native effects for texture, alpha and sound.', '''
Create a comp-sized solid, open Quick Apply and apply e:curl noise. Start with Internal input and compare Scale and Swirl separately.
Animate a short texture using the intended Evolution/motion controls. Colorize with Tint or Tritone and inspect aliasing at Full resolution.
Precompose the texture and use it as a luma matte on another layer. Confirm whether the consuming effect/matte samples the stage you intended.
On a suitable black-backed element apply Unmult, choose its background mode and inspect alpha. Tune level/softness and test over dark and bright backgrounds.
On a duplicate audio layer try Compressor, Gate and Distortion one at a time. Compare bypass at similar loudness and preserve spoken word endings.
Render a short review with audio and an alpha-capable element separately. Reimport to verify the channel behavior and listen to the processed sound.
''','I can distinguish a procedural texture from a fluid simulation.|I can create real alpha from an appropriate backing.|I can compare processed audio without confusing loudness with quality.',
'Build an abstract flowing title transition and document the purpose of each effect in its stack.',
'Unmult may remove genuine foreground black/white without a protective matte.|Gate does not remove room noise underneath speech.',
'curl-noise unmult audio-dynamics','noise keying-effects audio-effects',diagram='effects')

lesson('mesh-focus','00 · Native mesh materials and an Advanced 3D rack focus','ADVANCED',
'Combine stable geometry, material and camera tools in one controlled scene.', '''
Create a new comp using Advanced 3D. Add a cube and sphere using the Parametric Mesh tool or Layer → New, placing them at different camera distances.
Adjust Mesh Options and contrasting Roughness/Metallic material values. Use a real light/environment and compare highlights with camera movement.
If an SBSAR is available, import and apply it to a supported mesh. Test modest material displacement on the mesh, checking silhouette and rendering cost.
Create a camera, enable Depth of Field and focus the near object. Adjust Aperture and Blur Level, then keyframe Focus Distance toward the far object.
Render a 48-frame test in Active Camera. Check focus at the first, middle and final frame and compare Full-quality output with the interactive preview.
Collect the test project and dependencies. Keep materials on 3D text/shapes and animated layers as material inputs out of this stable-only exercise; those are separate Beta capabilities.
''','I can create native geometry.|I can distinguish displacement from a 2D warp.|I can render-check a camera focus change.',
'Create a product-style orbit with one controlled rack focus and a written material/dependency list.',
'Emission appearance does not illuminate nearby geometry.|A flat CC Sphere effect is not the mesh created here.',
'parametric-meshes substance-materials advanced-dof','meshes substance material-properties advanced-dof',diagram='coordinates')

# Stable chapter IDs are also saved progress keys. Keep IDs while sorting the learning ladder.
_PHASE_ORDER={'START':0,'FOUNDATIONS':1,'INTERMEDIATE':2,'ADVANCED':3,'DELIVERY':4,'CAPSTONE':5}
CHAPTERS.sort(key=lambda c:_PHASE_ORDER[c['phase']])
for number,chapter in enumerate(CHAPTERS,1):
    chapter['title']=f"{number:02d} · "+chapter['title'].split(' · ',1)[1]

# This roadmap is advice and readiness criteria, not artificial locking of lessons.
STAGE_PLAN=[
 {'phase':'START','name':'Orientation','objective':'Build and navigate a correctly saved composition, understand sources and place layers precisely.','gate':'From a blank project, recreate a 4-second two-card edit, relink a source and identify Position versus Anchor Point.','practice':'Create a small working scene from solids, text and one imported source.'},
 {'phase':'FOUNDATIONS','name':'Animation and compositing basics','objective':'Animate deliberately and understand how paths, mattes, text, precomps and effects change the image.','gate':'Build a 4-second title reveal with at least two eased properties, a track matte, a named precomp, and a deliberate effect order.','practice':'Try the loading-ring, text-window and logo-reveal recipes.'},
 {'phase':'INTERMEDIATE','name':'Real footage and production craft','objective':'Work with sound, keying, tracking, 3D space, color and basic controller expressions.','gate':'Complete a short moving-footage composite, inspect every frame for track drift or alpha errors, and link a visible property to a controller.','practice':'Try a Keylight, a point track, and an audio-reactive exercise.'},
 {'phase':'ADVANCED','name':'Reusable and complex systems','objective':'Make data-driven templates, control 3D/model interactions, use Puppet and native particle tools, and automate repetitive edits safely.','gate':'Create one editable template with independent instances plus a separate reproducible procedural/3D or scripted experiment.','practice':'Try the reusable lower third, JSON scoreboard or particle-burst recipes.'},
 {'phase':'DELIVERY','name':'Render, preserve and troubleshoot','objective':'Export verified deliverables, collect all dependencies, compare cold/warm previews and isolate errors systematically.','gate':'Render a review and an alpha-capable master, reopen a collected project from another path, and resolve one deliberate failure.','practice':'Try the transparent-master and handoff-test recipes.'},
 {'phase':'CAPSTONE','name':'Independent final production','objective':'Combine learned skills into an original, reviewable, portable 10-second sequence.','gate':'Deliver an independently checked 10-second composition with source files, project backup and an explanation of every major animation choice.','practice':'Build the final integrated-sequence recipe without step-by-step imitation.'},
]

TOPICS=[]
def topic(id,title,category,summary,section_text,exercise='',pitfall='',related='',sources='help'):
    sections=[]
    for s in section_text.strip().split('\n'):
        if '::' in s:
            name,body=s.split('::',1)
            sections.append(dict(title=name.strip(),text=body.strip()))
    TOPICS.append(dict(id=id,title=title,category=category,summary=summary,
        sections=sections,experiment=exercise,pitfalls=[v.strip() for v in pitfall.split('|') if v.strip()],
        related=related.split(),sources=sources.split()))

topic('version-workflow','Version discipline: 26.5 stable and a separate Beta','Foundations','Use the September 2026 stable release and recognize the boundary of its feature set.', '''
Identify::Check Help → About After Effects for 26.5. This guide’s research date is 2026-10-28; it does not assume features from a rolling Beta page ship in stable.
Modern tools::26.0–26.3 added native meshes/materials, variable-font axes, SVG workflows, Unmult/audio effects, Quick Apply, Object Matte, Proportional Scrubbing, Curl Noise, clipboard frame capture and Advanced 3D DOF. They are all within this edition’s target.
26.5 improvements::Responsive guides, Object Matte disk caching, effect labels/modernized controls and ACES 2.0 configurations are included. Read the dedicated topics for the actual operations and limits.
Beta boundary::Contour Paint, De-esser, AI Assistant, layers as 3D material inputs, materials on 3D text/shapes, editable Illustrator-text conversion, Quick Set Anchor and generalized Alt-drag duplication are listed on Adobe’s Beta page. Do not build a stable-only handoff around them.
''','Find the installed version, open Quick Apply, then explain why a Beta tutorial may expose different controls.','Stable mesh-specific Alt-drag behavior does not establish general layer duplication support.','interface release-26-5 beta-watchlist','release whats-new beta')

topic('25-6-features','Earlier 25.6 features retained in 26.5','Foundations','Earlier improvements retained in 26.5; the durable topic ID also preserves existing links.', '''
Shared 3D gizmo::Select multiple 3D layers and use a single viewport gizmo to position, rotate and scale multiple selected layers. It reduces visual clutter; it does not replace Parenting or create a persistent Group object.
Default camera settings::View menu allows modifying default-camera behavior for appropriate views. Use this to control perspective when no explicit camera is used or when viewing a custom view, but record the change in a training project.
Interface and fixes::Tip of the Day appears when an appropriate viewer is empty/reloaded. Timelines can be closed to the left or right, and 25.6 fixes a large group of project, export and stability defects.
GPU boundary::Adobe’s 25.x requirements specify that After Effects 25.6 requires OpenCL 2.0 where OpenCL is applicable, removing support for 1.2 or older. Hardware compatibility matters more than incidental new tool names.
''','Make a two-layer 3D scene and operate the joint gizmo, then parent both layers to a Null and describe the difference.','','version-workflow 3d-intro','release requirements')

topic('interface','The Windows After Effects interface','Foundations','Know the difference between each panel and where focus lives.', '''
Project and composition::The Project panel stores footage, comps and folders. Composition viewer shows a rendered view of one composition at a given time, with guides and on-canvas controls. Double-clicking footage opens the Footage panel; double-clicking a footage layer can open the Layer panel.
Timeline and Effects::Timeline hosts layers, track mattes, time spans, properties, expressions, keyframes and graph curves. Effect Controls displays the selected layer’s effect stack; Effects & Presets is a catalog/search area for available effects and animation presets.
Focused shortcuts::A key can mean something else in text editing, painting, a 3D view or a render queue. Ctrl+D duplicates the current selected object in the active context. Click the intended panel and verify selection before using a destructive command.
Recover layouts::Use the Window → Workspace menu, reset layouts, hover a panel and press backtick to maximize it. F4 reveals alternate Timeline Switches/Modes columns. Use panel tabs and viewer locks to compare related comps.
''','Use only keyboard and workspace menus to locate Project, Preview, Character, Render Queue and Composition panels in 60 seconds.','A gray blank panel may be a viewer without an open item, not a failed render.','layer-anatomy version-workflow','shortcuts')

topic('layer-anatomy','Composition, layer and project hierarchy','Foundations','Understand nested composition references and editable source instances.', '''
Files are not embedded automatically::An .aep project points to sources and stores transformations and project data. Two layers can reference one source item, and two comps can nest the same precomp; changing the nested original impacts both copies unless overridden.
What lives on a layer::A layer has In/Out, transform, masks, effects, blending mode, mattes, switches, parenting, keyframes and other type-specific properties. Effects modify generated pixel data; they are not identical to a shape layer’s Contents operators.
Comp settings affect interpretation::Composition FPS defines its frame grid; resolution and pixel aspect determine the render canvas. The footage source has its own interpretation, while the comp layer instance has its own transform and time placement.
''','Build two comps sharing a precomp, then alter the shared precomp artwork and observe both.','Do not assume deleting a layer will delete its Project footage source.','precomp import-media render-order','help')

topic('project-management','Folders, naming and backup policy','Foundations','Organize projects so someone else can rebuild them.', '''
On disk vs Project panel::A Project folder is metadata inside .aep, not necessarily an OS directory. Keep named Windows folders for Assets, Renders, Cache if desired, Archive and Collected. Backups should be saved outside the active working folder where feasible.
Naming schemes::Give comps distinctive prefixes (FINAL_, SCENE_, PRE_, CTRL_) and avoid duplicate or confusing names for controllers used in expressions. Label colors aid navigation but must not be the only source of meaning.
Reproducibility::Use File → Dependencies → Collect Files for used source material; also list external fonts, plugins, LUTs, environment assets and scripts. Never claim Collect Files packages plugin binaries or licenses.
''','Open an .aep from a moved Collect Files directory after severing access to its original Assets path.','Save As is not identical to Increment and Save or Collect Files.','collect-files missing-effects','help')

topic('import-media','Import formats, sequences and linked files','Foundations','Always inspect time, channels, format and external dependencies.', '''
Footage vs layer::Importing creates a footage item in Project. Dragging it into a composition creates a layer instance with its own in point, transform and effects. Deleting an instance does not necessarily delete the source item.
Sequence and alpha::Numbered images can become one time-based sequence. Check whether alpha is straight or premultiplied; a premultiplied RGB fringe should not be interpreted as an image with independent straight edge colors.
Dynamic links and layered PSD/AI::Where supported, import a layered image as Composition — Retain Layer Sizes to keep logical layers. Inspect the anchor and coordinate placement after the import. Dynamic Link/Photoshop/Illustrator updates need the original source app/assets.
''','Import a five-frame PNG sequence and then import one frame as still; explain the difference.','A media path under Downloads can disappear even if .aep continues to exist.','footage-interpretation file-management','help')

topic('footage-interpretation','Footage frame rate, alpha and pixel aspect','Foundations','Bad interpretation can invalidate an otherwise perfect composite.', '''
Frame rates::When footage is interpreted at a different FPS, it may run faster/slower. Time stretch and frame blending are different from reinterpretation. Variable-frame-rate recordings may need transcoding to constant frame rate.
Alpha types::Straight/unmatted pixels encode RGB independently of alpha. Premultiplied/matted pixels were already mixed against a matte color; interpreting them incorrectly often creates dark/light halos.
Pixel aspect and fields::A non-square pixel interpretation scales geometry, not just final output dimensions. Interlaced fields and separated-fields options matter for legacy broadcast material and can cause combing if interpreted wrong.
''','Take an RGBA still, intentionally choose incorrect alpha interpretation, then restore a clean edge.','Changing footage interpretation can affect every use of that footage item.','alpha frames','help')

topic('frames','FPS, timecode and frame alignment','Foundations','Work in frame counts to avoid off-by-one visual errors.', '''
Timecode::In a 24-fps non-drop-frame composition, 00:00:01:12 means 1.5 seconds. Frames within a second run 00 through 23. The display mode can also show frames rather than timecode.
Layer sampling::Source footage at 30 fps inside a 24-fps comp is sampled at the comp frame grid, potentially repeating/dropping frames or using blending. Audio is time-based and should be inspected independently of visual frame matching.
Useful arithmetic::Duration seconds = frames / fps. 72 frames at 24 fps = 3 seconds; 100 frames at 25 fps = 4 seconds. Use the guide’s frame calculator to explore rates and offsets.
''','Make a four-second comp at 25 fps and label frames 0, 24, 25 and 99. Frame 100 is the exclusive duration boundary, not a visible frame inside that comp.','Drop-frame timecode applies to appropriate broadcast rates; do not use its punctuation as a universal frame-count formula.','timeline source-time','help')

topic('timeline','Layer bounds, work areas and markers','Foundations','A timeline is several overlapping time systems.', '''
Three positions::The composition playhead indicates comp time; the layer’s bar shows In/Out times in that comp; footage source time indicates which source frame is used. A precomp also has its own inner timeline.
Move versus trim::[ and ] reposition entire selected layers to CTI using their In/Out references; Alt+[ and Alt+] trim at CTI. Ctrl+Shift+D splits. These are not equivalent to moving animation keyframes only.
Markers and work area::B/N set work area ends for local preview/render planning. Main keyboard digits may navigate numbered comp markers, while numpad keys can select layers or start a preview depending on focus.
''','Use one video clip to demonstrate a shift, a trim, a split and a work-area change, and label each in a separate comp.','Changing the work area does not necessarily change comp duration.','source-time frames','shortcuts')

topic('coordinates','Coordinates, anchor points and transforms','Foundations','Be precise about which point and which coordinate system each value uses.', '''
Anchor versus position::Anchor is in the layer’s own coordinate system; Position specifies the anchor in parent/comp coordinates. Moving an anchor can appear to shift the image unless AE compensates its Position when using Pan Behind.
Transform nesting::A shape group has its own Transform inside Contents, plus the layer Transform. A child layer uses parent-space Position; a 3D layer can have X/Y/Z and Orientation as well as Rotation values.
Converting positions::Expressions provide toComp(), fromComp(), toWorld(), fromWorld() and related methods for correct cross-coordinate conversion. A direct Position link is only straightforward when both properties share the same coordinate context.
''','Find the same corner of a shape before/after parenting and explain why its displayed Position values differ.','A shape rectangle size is not the same property as layer Scale.','parenting expressions','expressions')

topic('parenting','Parenting, nulls and reusable rigs','Foundations','Use simple controllers to coordinate several layers safely.', '''
Parent-child relationships::A child inherits transforms from its parent but retains independent local animation. Parent to a Null for a clean control layer rather than applying identical Position keyframes to every object.
Controllers::Use descriptive names and Expression Controls for user-facing parameters. Parent a child only once in a hierarchy; avoid creating circular dependencies through expressions.
Rig safety::Duplicate a rig and check whether expressions reference the duplicated or original controls. Essential Properties are often more suitable for controlled per-instance variation than unstructured cross-comp expressions.
''','Build a three-layer clock where the root null travels while a hand rotates independently.','Parenting a 3D child to a 2D null can have unexpected coordinate behavior; test and document.','coordinates essential-properties','help')

topic('keyframes','Keyframes and interpolation','Animation','A keyframe stores a property value at a specific time.', '''
Recording properties::Enable the stopwatch when you mean to animate. At a new time, editing the value creates an additional key. Changing a static value before enabling a stopwatch does not record a time history.
Interpolation::Linear changes at uniform numeric rate, Hold jumps, Bézier allows easing. Rotation angle and 2D Position follow different units, so similar graphs can still produce different perceived motion.
Keyframe housekeeping::U reveals keyed properties, J/K navigate visible time events, and Ctrl+Shift+K opens velocity controls. Ctrl-click in a keyframe view is contextual; learn the specific mode before editing.
''','Make the same 0-to-100 opacity transition with Linear, Hold and Easy Ease.','Clicking the active stopwatch deletes all animation for that property.','graph-editor motion-design','shortcuts')

topic('graph-editor','Value Graph, Speed Graph and easing','Animation','Control velocity and rhythm separately from endpoint positions.', '''
Speed vs value::A Value Graph plots the property value over time. A Speed Graph plots the rate of change. A flat speed graph can correspond to a sloped linear position value graph.
Influence and handles::Temporal Bézier handles control easing at keys. At a given duration, sharper influence usually shifts which portions of the journey happen quickly versus slowly. The path can remain straight.
Spatial keys::Position motion paths have separate spatial Bézier interpolation; a curved trajectory does not guarantee ease. Rove Across Time can redistribute intermediate spatial keys but not arbitrary hold or non-spatial properties.
''','Animate three identical dots to the same endpoint with different arrival timing and explain the change in speed graph.','Do not make a curved spatial path when you only need easing.','keyframes motion-design','shortcuts')

topic('motion-design','Timing and design principles for readable motion','Animation','Make movement communicate hierarchy, not merely demonstrate tools.', '''
Pose and hold::Allow time for reading after a title enters. Motion that never stops is often harder to follow; a clean hold creates hierarchy and reduces attention fatigue.
Overlap and anticipation::Offset related layer animation by a few frames using measured timing, not arbitrary random delays. For a 24-fps comp, 6 frames = 0.25 seconds; choose offsets based on readability.
Consistent motion language::Keep easing, direction, acceleration and stagger rules reusable across a project. Test at full playback speed and also frame by frame for collisions.
''','Build a 3-card entrance with 5-frame staggers and consistent ease-out shapes.','Excess overshoot can look like accidental jitter rather than controlled energy.','graph-editor shapes','help')

topic('shapes','Parametric shapes vs Bézier paths','Animation','Use the least complicated editable geometry for each job.', '''
Shape structure::Shape Layer → Contents contains groups. Each group may contain path, fill, stroke, group transform and operators; the layer has its own Transform independently.
Keep parameters live::Rectangle Path Size and Roundness allow reusable UI-like cards. Polystar Path lets you animate point count and radii. Converting to Bézier gives vertex freedom but sacrifices simple parametric controls.
Operators::Trim Paths draws strokes; Repeater duplicates source shapes; Offset Paths grows/shrinks outlines; Pucker & Bloat distorts forms. They operate in Contents, not standard effects stack.
''','Construct a shape-based progress ring, then change its size without redrawing vertices.','A filled closed path revealed with Trim Paths may not behave like a stroked outline.','paths strokes','help')

topic('paths','Masks, shape paths and motion paths','Animation','Three different kinds of path can look visually similar.', '''
Mask path::A mask path defines visible pixels and has Mode, Feather, Opacity and Expansion. Mask Path keyframes animate that outline, not the layer Position itself.
Shape path::A Shape Path defines fill/stroke geometry and can be a live parametric outline or a vertex-editable Bézier curve. It can be copied between compatible path properties in many situations.
Motion path::A Position property with spatial animation creates a trajectory whose dots represent temporal samples. Its vertices and handles change spatial travel, while keyframes/Graph Editor define timing.
''','Make one letter follow a mask path while a separate shape traces a closed path via Trim Paths.','Do not assume two visually similar paths have interchangeable parameter types.','masks graph-editor','help')

topic('strokes','Shape strokes, Trim Paths and Write-on','Animation','Choose between drawing geometry and painting pixels.', '''
Stroke types::Shape Stroke is vector line styling inside a Shape Layer. The Stroke effect can reveal a mask path on footage or a solid. Write-on uses paint-like accumulation and has its own timing controls.
Dashed paths::A shape stroke can have dashes, caps, joins and taper depending on the shape controls. Trim Paths Start/End define the visible portion of a path, while Offset rotates this visible window.
Compositing::To make a tracked outline, first track/animate the path, then generate a stroke, then optionally add Glow. Use a solid or precomp so the stroke has enough output dimensions when necessary.
''','Draw a six-stroke icon and animate strokes in a deliberate order.','Do not use a high-feather mask in place of a designed stroke.','shapes paint','help')

topic('masks','Mask modes and feathering','Compositing','Masks edit layer transparency while preserving source pixels.', '''
Mode logic::Add reveals, Subtract removes, Intersect retains shared area. Inverted changes interpretation. With multiple masks, compositing behavior depends on mode, ordering and the layer’s alpha.
Edge controls::Feather produces a soft transition, Expansion dilates/erodes region borders and Mask Opacity scales contribution. Variable/per-vertex feathering can handle nonuniform boundaries.
Animated masks::With a selected mask path stopwatch, edit vertices over time. Fewer stable vertices generally track better than dozens of imprecise ones.
''','Draw two masks: one additive and one subtractive, then isolate the overlap.','If masks are invisible, check View → Show Layer Controls; it does not change pixels.','alpha mask-tracking','help')

topic('alpha','Alpha, straight RGB and premultiplication','Compositing','Transparency is separate from visible RGB even when pixels look black.', '''
Representation::An RGBA pixel stores red, green, blue and alpha. Alpha=0 need not force RGB=0 in all representations. In straight alpha, RGB is often intended unmultiplied; premultiplied RGB already contains transparency/color matte interaction.
Artifacts::Dark outlines on translucent edges commonly result from misinterpreted alpha or resampling a matte-color-contaminated source. Inspect straight RGB and alpha separately before adding choker/blur.
Delivery::A codec/container must carry an alpha plane, and the output module must export RGB+Alpha correctly. Many MP4 H.264 workflows do not carry ordinary RGBA transparency.
''','Create a white semi-transparent circle over black, export and test its edge over magenta.','Using Screen blending for black-backed particles is not identical to producing alpha for downstream editors.','mattes export footage-interpretation','help')

topic('mattes','Alpha/luma track mattes','Compositing','An independent matte layer controls another layer’s visibility.', '''
Alpha matte::Visible matte alpha determines the target’s coverage. A red opaque matte and blue opaque matte cover equally if both have full alpha.
Luma matte::Luminance of a matte determines visibility. Black gives none and white gives full coverage; mid-gray gives partial coverage. Color gradients can behave unlike alpha-only gradients.
Flexible setup::Modern track mattes let the target reference an appropriate other layer in the comp. One matte may be reused in more than one place; keep the source named and be aware of comp boundaries.
''','Use a checkerboard, a full-alpha red rectangle and a grayscale gradient to compare alpha and luma mattes.','A mask on the footage and a matte sourced from a different layer are not identical workflows.','alpha blending','help')

topic('blending','Layer blend modes and compositing','Compositing','Blend math changes RGB interaction with layers beneath.', '''
Ordinary compositing::Normal combines pixels by alpha. Multiply darkens based on RGB product; Screen generally lightens; Add sums channels and can clip or exceed normal ranges in high-bit-depth projects.
Order matters::A blend mode acts on a layer relative to what has been composited below it. Reordering layers often changes the look, even when no keyframes change.
Alpha does not follow automatically::Screening a black-background explosion may visually hide black but does not magically reconstruct fully useful alpha. Check the deliverable’s requirements.
''','Composite a bright flare onto black footage with Screen, then try a true RGBA flare and compare downstream alpha.','Blend modes can behave differently under linear-light color management.','alpha render-order','help')

topic('render-order','Effect and transform evaluation order','Compositing','The order of pixel processing explains why precomps can change results.', '''
Processing chain::A simplified layer flow considers source, masks and effects, transformations, layer styles and compositing. Actual order can vary with layer type, 3D renderer and continuously rasterized/precomp settings.
Precompose effects::Moving effects inside versus leaving them outside a precomp can shift which pixels are processed at what scale/geometry. Use two simple controls to prove the cause.
Adjustments and nested comps::An adjustment layer affects pixels composited beneath it inside its active group/context. Nesting can change what image it receives and where it is calculated.
''','Apply a 20-pixel blur to a 100×100 square, scale 500%, then swap where blur and scale occur.','Collapse Transformations can change rendering; it should not be turned on reflexively.','precomp effect-order','help')

topic('precomp','Precomposition and nested timeline logic','Compositing','A precomp is a composition used as a layer in another comp.', '''
Two contexts::Inner composition time, resolution, frame rate, layer transforms and effects can all differ from the outer master comp. Time Remapping on outer precomp changes sampled inner time.
Move attributes choice::When precomposing, whether attributes move into the new comp changes how/where an effect is evaluated. Test with one blur and one transform rather than memorizing the dialog without context.
Maintainable nesting::Keep comp hierarchies shallow enough to inspect. Prefix names, write purposeful notes and avoid accidentally creating expression dependencies across unstable names.
''','Build a comp of an animated icon, use it twice, and override only one instance’s timing.','Do not assume outer frames and inner frames line up without checking frame-rate and start-time behavior.','render-order essential-properties','help')

topic('effect-order','The effect stack and control surfaces','Effects','Each effect consumes the prior rendered result in its layer context.', '''
Processing order::Fractal Noise → Levels → Glow does not necessarily match Fractal Noise → Glow → Levels. The first can threshold which regions glow; the second can recolor/clamp the already glowing output.
Effect Controls::Use F3 to inspect, rename and reorder effect instances. The fx switch bypasses individual effects and the layer fx switch bypasses effects as a set; deleting all effects is destructive.
Scope::A blur on a source layer differs from a blur on a precomp or an adjustment layer. Effect operating bounds, alpha and precomp render order can change the visible result.
''','Reverse two effects on a duplicate layer and explain the changed pixels.','Do not treat a property expression as an image effect.','effects adjustment-effects','effects')

topic('effects','Effects, presets and compatibility','Effects','Read the difference between native effects, bundled plugins and third-party plugins.', '''
Find capabilities::Effects & Presets lists installed effects and presets. Different AE releases can add/remove or deprecate items. The Adobe Effect List reports GPU, Multi-Frame Rendering and bpc support for many named effects, but is a rolling document.
Predesigned animation::Presets may create multiple effects, text animators or keyframes. Apply them to a disposable layer and inspect what changed before using them on a production layer.
Manage failures::If an effect is missing, investigate Effect Manager, plugin licensing, paths, bit depth and OS support. A disabled or obsolete effect can still appear on old layers.
''','Apply one animation preset to a temporary text layer, inspect every parameter it added, then rebuild its visual behavior manually.','An effect may render on CPU even in a GPU-capable composition.','effect-order missing-effects','effects')

topic('adjustment-effects','Adjustment layers and global looks','Effects','Place finishing looks intentionally in a layer stack.', '''
What they sample::Adjustment layers take the composite below within their scope and process it through effects. Use them to keep repeated color/grain/blur calculations under control.
Limiting scope::Trim adjustment In/Out, use masks or mattes, or nest intended layers into a precomp so only that result receives the change.
Adjustment vs solid::A solid with an effect is still an ordinary image source unless effect/composite settings cause it to act differently. An adjustment layer is a special processing layer.
''','Apply Curves to only one card via an adjustment layer mask and compare to a directly applied effect.','If the adjustment layer is at the bottom of the comp, it cannot affect layers above it as expected.','blending render-order','help')

topic('blur','Gaussian, lens and map-driven blur','Effects','Pick a blur that expresses the actual desired motion/depth.', '''
Ordinary blur::Gaussian Blur is predictable and often economical. Directional Blur resembles linear streaking; Radial Blur simulates radial spin/zoom; Unsharp Mask enhances edges rather than smoothing.
Lens look::Camera Lens Blur can shape bokeh highlights and blur-map-dependent focus. It may be more expensive than a Gaussian blur; test representative shots and settings.
Blur a matte vs blur an image::Softening a mask/matte edge preserves subject detail differently from blurring the subject RGB itself. Use the channel viewer to see what data changed.
''','Create an alpha matte with a 20-pixel soft edge, compare against a 20-pixel Gaussian blur on the actual footage.','Overblurred matte edges can produce transparent halos with colored source pixels.','alpha depth-maps','effects')

topic('procedural','Fractal/Turbulent Noise and displacement','Effects','Generate repeatable organic texture and use it as a controlled signal.', '''
Noise generator::Fractal Noise exposes a procedural field. Contrast, Brightness, Scale, Complexity and Evolution/Offset Turbulence change pattern appearance and motion.
Signal map::Convert noise to useful grayscale and plug into Displacement Map, Compound Blur or matte controls. The map does not need to look beautiful as a layer; its luminance/channel relationship is the important factor.
Animation loops::Looping Evolution might not produce a seamless visual loop unless cycling and offset settings are chosen correctly. Check first and last frame against each other.
''','Make 3 kinds of noise with identical Evolution speed but different Scale and use each as a Displacement Map.','Curl Noise, introduced in 26.3, is available in 26.5; its flow controls differ from Fractal Noise.','depth-maps effects','history')

topic('depth-maps','Displacement, depth and faux 3D','Effects','Depth maps encode local differences but do not automatically turn an image into geometry.', '''
Grayscale meaning::A depth map typically uses light/dark values to represent a chosen near/far ordering. It is only meaningful when an effect interprets those values with a known range and channel.
2D parallax::Use separately cut foreground/background layers, Z positions and a moving camera for actual AE 2.5D parallax. A displacement map instead repositions pixels inside a layer.
Map quality::Soft gradients can create smooth wipes or depth-based blur. Abrupt low-resolution boundaries cause distortion and halos; feather the map before it is sampled.
''','Create a grayscale radial gradient and use it as a blur map, then as a displacement map; compare interpretations.','Camera Lens Blur on a map is not Advanced 3D camera depth of field.','procedural cameras','help')

topic('time-remap','Time remapping, reversal and loops','Animation','Resampling a source in time is different from moving keys along a comp timeline.', '''
Source-clock changes::Time Remap keys map comp time to source time. A hold segment samples one source frame repeatedly; a descending segment can reverse the footage.
Layer vs keyframe reversal::Time-Reverse Layer reverses the layer source playback; Time-Reverse Keyframes reverses timing of selected animation keys. Use deliberately named test duplicates.
Loop frames::Keep the full N-frame source duration. Use an initial (0,0) remap key, a last-valid-frame key at ((N-1)*d,(N-1)*d) with outgoing Hold, and a cycle-boundary key at (N*d,0). loopOut('cycle') then repeats that full interval; simply deleting the duration endpoint can shorten the cycle. Check source/comp rates and trim offsets.
''','Render a 2-second clip as forward, reverse, freeze and looping examples.','Video source frames may be interpolated differently depending on frame blending settings.','frames motion-blur','shortcuts')

topic('motion-blur','Native motion blur and shutter settings','Animation','Motion blur communicates movement between discrete frames.', '''
Two switches::Layer Motion Blur switch must be enabled, and the comp master Motion Blur must also be on. Some source/effect types require separate blur solutions.
Shutter angle::Larger shutter angle generally creates longer smears relative to frame interval. Shutter phase changes the sampling timing relative to the frame center.
Evaluate carefully::Check blur at final frame rate and Full-quality rendering, not only in a low-resolution interactive preview. Camera/3D motion may need renderer-compatible blur.
''','Render the same fast-moving square with motion blur off, modest shutter, and long shutter.','Motion blur cannot repair extremely poor source motion tracking.','time-remap export','help')

topic('text','Point/box text, metrics and typography','Text & data','Readable type depends on spacing and consistent layout.', '''
Text modes::Point text grows as you type; paragraph text wraps inside a bounding box. Baseline shift, leading, kerning, tracking and paragraph alignment are distinct tools.
Design rules::Build with type hierarchy, padding and safe areas. Validate font availability, substitution behavior and variable dimensions of different language strings.
Editable workflows::Preserve editable text for templates and handoff. Only convert text to shapes when vertex-specific path animation or flattening is truly required; a shape conversion is no longer a normal editable text string.
''','Fit three differently sized names into one title-card layout without manual per-name repositioning.','Style controls and font metrics can change between installed font versions.','text-animator auto-layout','help')

topic('text-animator','Text animators and selectors','Text & data','Text animation has selectors inside the text layer hierarchy.', '''
Animator vs source::Source Text defines content. Text → Animate adds a group of animated properties that apply to selected characters, words or lines. The layer Transform moves all characters together.
Range selector::Start, End, Offset and Advanced selectors determine which text is affected. Shape, Smoothness and Based On modes can create scans, typewriter-like reveals or per-word emphasis.
Expression selector::A custom selector can provide per-character weight values. Use it only when Range or Wiggly Selector cannot express the motion and maintain it carefully.
''','Animate each word in a heading by changing only Based On and a range selector’s Offset.','Variable Font Axes are available in 26.5; use a genuinely variable font and check its supported axes.','text expression-controls','history')

topic('type-design','Kinetic typography and text clarity','Text & data','Text animation is meaningful only when it stays legible.', '''
Sequence hierarchy::Decide which line is primary and which is secondary. Do not animate every word with equal force; use emphasis selectively.
Spacing and contrast::Monitor text at target playback size, on a phone-sized viewer when applicable. Check antialiasing, safe zones and contrast on busy plates.
Time constraints::Estimate reading time and keep titles visible long enough to understand. Faster keyframes do not automatically make a better design.
''','Make an 8-second quote with 2-second line holds, one emphasized word per line, and a consistent baseline.','Scale bounces can produce text shimmer at small final sizes.','text motion-design','help')

topic('audio','Audio preview, sync and output','Audio','Work with sound deliberately even when AE is not the main editing app.', '''
Layers and waveforms::L reveals levels; LL reveals waveform. Preview shortcuts differ by normal keyboard and numeric keypad. Set markers to real audible onsets instead of guessing from peaks.
Sync::Layer shifting, Time Stretch and frame-rate interpretation can all affect where sound aligns with motion. Video footage with variable frame rate can create sync trouble and may need preprocessing.
Final QC::Enable audio in the export path and listen to the rendered file. Verify beginning/end fades, clipping and the intended channel mix, not just a loud waveform in Timeline.
''','Synchronize three shape pops to audible beats and export with checked audio sync.','After Effects audio tools do not replace a full multitrack audio editing/mixing environment.','audio-reactive export','help')

topic('audio-reactive','Convert Audio to Keyframes workflow','Audio','Use an audio amplitude slider to drive numeric properties.', '''
Generate amplitude::Use Animation → Keyframe Assistant → Convert Audio to Keyframes. The generated Null holds Left, Right and Both Channels Slider keyframes.
Map scale::On Scale, reference Both Channels with an expression and map/clamp it into an appropriate scale range. Use `[s,s]` for 2D scale output, not a bare number.
Noise control::Raw amplitude changes rapidly; smooth it or drive sparse pulses to avoid uncomfortable shaking. Add an envelope/falloff rather than directly following every sample.
''','Make a circle pulse between 100% and 135% based on a short drum loop.','Volume level curves do not identify rhythm genre or musical beat positions automatically.','audio expression-controls','expressions')

topic('keying','Keylight, spill and edge recovery','Compositing','Clean keying has separate stages with distinct failure modes.', '''
Source stage::Even lighting and sufficient chroma separation reduce the work of keying. Add a garbage matte so the keyer only processes the relevant area.
Alpha stage::Keylight Screen Matte lets you inspect and refine the core silhouette. Avoid clipping all hair detail for a perfectly black background.
Edge stage::Key Cleaner, Advanced Spill Suppressor, subtle edge color correction and selective blur improve integration. Test against multiple backgrounds and moving frames.
''','Key a person over a dark and a light background, then adjust edges until both look acceptable.','Green spill suppression is a color correction problem, not only alpha thresholding.','alpha masks','help')

topic('roto','Roto Brush and Refine Edge alongside Object Matte','Compositing','Choose brush-guided propagation when it gives better control than object selection.', '''
Layer viewer::Roto Brush strokes are made on a layer in the Layer panel, not drawn as a Composition viewer shape. The initial base frame guides propagation across nearby frames.
Propagation and correction::Inspect forward/backward spans, repair slips and use Refine Edge for wispy hair. Freeze after corrections and render check the entire selection range.
Tool choice::For a rigid object, a tracked mask or Mocha planar mask may be more efficient than broad Roto Brush propagation. Choose based on edge topology and motion.
''','Roto a walking person for two seconds without any abrupt matte popping.','Object Matte is available; choose its toolbar tool for object selection, and use brush/refine tools for corrections.','mask-tracking paint','history')

topic('point-tracking','Point tracking, attach points and drift','Tracking & 3D','Understand what one or two tracked features can and cannot tell you.', '''
Feature region::Contains visual detail the tracker matches across frames. Search region defines where it is allowed to search. Attach Point is the actual point used to transfer the solved motion.
Motion types::One point provides translation, two points can model more of rotation and scale. Perspective corner changes require an appropriate perspective/planar tracking workflow.
Review::Watch each tracked frame for drift. Reducing motion blur, tracking in segments or choosing a more stable high-contrast target can improve results.
''','Attach a 30×30 crosshair to a moving shirt button and keep it aligned for 60 frames.','A search region that is too small will lose a fast-moving feature.','mocha stabilization','help')

topic('mocha','Mocha AE planar tracking','Tracking & 3D','Planar trackers follow a textured surface rather than one point.', '''
Planar region::Define a useful plane, follow stable texture and manage occlusion. Mocha surface corners are not the same thing as the drawn tracking spline.
Export/copy::Use the bundled Mocha AE integration’s supported transfer path to Corner Pin or transform data. Check exact plugin UI for the installed Mocha build.
Limits::A bent cloth or independently moving object is not one stable plane. Break up the track or choose Roto Brush/manual work rather than forcing a single planar solve.
''','Track a poster on a wall and apply a four-corner grid in AE.','Warp Stabilizer, 3D Camera Tracker and Mocha each solve different geometric problems.','point-tracking perspective','help')

topic('stabilization','Warp Stabilizer and camera motion','Tracking & 3D','Smooth shaky footage without destroying the composition.', '''
What it analyzes::Warp Stabilizer attempts to estimate unwanted motion and compensate it. Method and Smoothness control how aggressive that compensation is.
Border strategy::Stabilization often needs crop, scale or synthesized edge pixels; excessive smoothness can distort straight lines. Choose the least invasive method that solves the visible problem.
Competing tasks::A shot may first need a camera/point track before stabilization, or the shot may be stabilized only for a masking pass. Preserve an unchanged source for audit.
''','Stabilize a ten-second handheld pan and check vertical edges for rubbery warping.','Do not assume every pan is unwanted motion.','point-tracking 3d-intro','help')

topic('mask-tracking','Tracked masks vs hand-roto','Tracking & 3D','Automating vertices is useful only with deliberate quality review.', '''
Best candidates::Select a mask on trackable footage/precomp, then use Animation → Track Mask or Mask Path analyze buttons directly in Timeline. Choose the motion method and analyze forward/backward. Solids, shapes, text and adjustment layers do not supply trackable footage; use roto for deforming hair.
Key cleanup::Adjust path vertices only where visibly necessary, avoid unnecessary topology changes, and feather in a stable way over time.
Fallback::Point/planar trackers can drive a mask transform while a few manual keys adjust localized shape changes.
''','Track a moving oval badge for three seconds and correct at least one deliberately induced drift.','Mask tracking does not infer hidden objects behind an occlusion perfectly.','masks roto','mask-tracking')

topic('paint','Brush and Clone Stamp in Layer panel','Compositing','Painting has source-time and stroke-duration behavior.', '''
Context::Select a suitable painting tool and work in Layer viewer. Source paint layers and Brush/Clone behavior depend on the Layer panel, Paint and Brushes controls.
Temporal strokes::Paint On Transparent and stroke Duration choices determine when and where marks appear. A fixed still frame repair may not remain aligned in later frames.
Clone source::Alt+click chooses a clone sampling source. Use small patches, animate/track where necessary and evaluate temporal texture consistency.
''','Clone out a one-frame blemish, then expand the correction to ten frames with correct alignment.','Painting directly on a composited final view is not identical to editing a footage source.','content-aware-fill alpha','help')

topic('content-aware-fill','Content-Aware Fill video cleanup','Compositing','Generate candidate replacement pixels after identifying the actual missing region.', '''
Define hole::Use a tracked/animated mask to specify the region that needs replacement; ensure the correct alpha relationship before opening the Content-Aware Fill panel.
Method and reference::Choose the fill method suitable for the motion/texture. Reference Frames can give a clean example when automatic reconstruction struggles.
Inspect variation::Review every frame, watching warping, repetition and unwanted edge seams. A tracked clean plate or a more modest crop may be a better answer.
''','Remove a small object and render a frame-by-frame contact sheet to catch flicker.','A good single still frame does not validate a fill over time.','paint mask-tracking','help')

topic('3d-intro','2.5D layers and spatial depth','Tracking & 3D','Position flat layers in 3D space to create depth cues.', '''
Z depth::2D layers occupy the comp plane; 3D layers add Z depth, orientation and material interactions. Move layers by different amounts in Z and view from a moving camera to create parallax.
Separate planes::A flattened photograph with all scene depth painted into one raster image cannot magically reveal hidden background behind foreground objects. Cut layers or create suitable gaps and patches.
Lighting and renderers::A 3D layer may accept lights/shadows depending on the renderer and its material settings. Use simple flat colors to diagnose shadows before importing textured assets.
''','Build a three-plane parallax shot and check visibility of edges at both camera extremes.','3D enabled layers are not automatically volumetric objects.','cameras 3d-renderers','help')

topic('cameras','Camera nodes, POI and projection','Tracking & 3D','Move a camera with intention and inspect results in multiple views.', '''
One- and two-node cameras::A one-node camera can be easier to orient directly. A two-node camera also has a Point of Interest; changing Position without considering POI can produce unexpected aiming changes.
Zoom and depth::Camera Zoom and focal length influence framing/perspective, while changing Z distances alters parallax. Do not confuse moving a flat layer closer with scaling it in 2D.
Orbit rig::Parent a camera to a Null positioned near the desired pivot for repeatable orbital movement. When editing camera POI, verify how parent transforms interact.
''','Build one dolly and one orbit move and label which parameters changed.','Default Camera is a special view concept, distinct from an explicit camera layer.','3d-intro 3d-renderers','help')

topic('3d-renderers','Classic 3D, Advanced 3D and Cinema 4D','Tracking & 3D','Renderer choice defines the 3D features that actually calculate.', '''
Capabilities differ::Advanced 3D supports imported models and advanced shading/material interactions, whereas Classic 3D and Cinema 4D renderer contexts serve different layer/geometry feature combinations.
Performance modes::Draft 3D and viewer preview modes trade interactivity for fidelity. Final frames need a deliberate check under the intended renderer and quality settings.
Current capabilities::26.5 includes native parametric meshes, Substance materials and in-engine depth of field. Test effect, shadow and transparency behavior in the chosen renderer before committing a project.
''','Put a native 3D layer in a simple comp and compare which renderer controls are enabled in each mode.','Render-time behavior can differ significantly from the viewport fast-preview display.','3d-models cameras','history')

topic('3d-models','GLTF/GLB/OBJ/FBX and environment lights','Tracking & 3D','Use imported assets with predictable materials and scale.', '''
Model import::24.x introduced model import and Advanced 3D. 25.2 expanded FBX support and animated environment lights. Check exact supported features and texture naming on the files you actually import.
Geometry vs layer::A 3D model layer is a scene object; ordinary 2D effects are not equivalent to editing its mesh/material internals. Use 3D-specific controls and renderer options.
Materials and lighting::Use an HDR environment where appropriate, control exposure and orientation, and test shadow reception/casting. A model with missing UV textures may appear uniformly shaded or magenta/default.
''','Import a simple neutral cube/GLB, light it, and record size, rotation and texture dependencies.','Substance SBSAR materials work with models and parametric meshes; layers as material sources and materials on text/shapes remain on the Beta watchlist.','3d-renderers color','history')

topic('camera-tracker','3D Camera Tracker and solved scenes','Tracking & 3D','Recover a camera path only when footage contains enough useful 3D information.', '''
Analysis quality::Good parallax and stable texture help the solve. Rotational-only motion, zoom, rolling shutter and motion blur may weaken results.
Ground plane::Choose tracked points that define a meaningful plane. Use a target region to create camera/solid/text and verify the object adheres across the whole shot.
Failed solves::Re-evaluate source quality, shot length and lens behavior. For one planar screen replacement, Mocha may be more direct than a full 3D camera solve.
''','Track a short handheld room movement, create a ground-plane solid and watch it over 100 frames.','A solver can produce apparently plausible 3D points while failing the intended insert.','perspective mocha','help')

topic('perspective','Corner Pin and perspective insertion','Tracking & 3D','A four-corner mapping targets planar surfaces.', '''
Planar geometry::A surface defined by four tracked corners can accept an animated screen or sign; corner ordering and transform calibration are critical.
Matching::Add appropriate edge softness, brightness, surface tint, noise, source blur and movement to integrate replacement media.
Diagnose drift::Use a visible checkerboard or clear colored corners to spot track errors before replacing with a complex UI or text.
''','Insert a 640×360 checkerboard onto a moving four-corner plane without visible slippage.','Perspective warp is not the same as a rigid layer transform with Position/Scale/Rotation.','mocha point-tracking','help')

topic('color','RGB, color profiles and grade order','Color & delivery','Keep image corrections separate from color-science transforms.', '''
Correction then look::Balance exposure, white point, contrast and saturation consistently before adding a style look. Shot matching becomes harder if each clip begins with arbitrary creative LUTs.
Managed project::ICC workflows convert source profiles into a designated working space; OCIO workflows use configured transforms. If working space is None, color management is not working as it would in a managed comp.
Viewer vs file::Display color management transforms a working image to the monitor; a rendered output transform targets delivery. These need not use the same profile/transform.
''','Export a small test chart as unmanaged and Rec.709-managed files and inspect metadata and appearance.','Do not assume that turning monitor color management off edits the pixel values.','ocio color-depth','color')

topic('color-depth','8/16/32 bpc and floating point','Color & delivery','Project math precision differs from codec or source bit depth.', '''
Precision::8 bpc uses integer-like limited steps; 16 bpc provides finer channel precision; 32 bpc floating point supports values outside the display 0..1 range and is common for HDR/linear-light pipelines.
No recovered highlights::Changing a clipped 8-bit source to 32 bpc preserves further calculations but cannot restore highlights already clipped in the recording.
Effect support::Individual effects may have different 8/16/32 support. Verify through installed effect behavior and Adobe effect documentation before claiming that one effect is universal.
''','Apply several Curves operations to a gradient in 8 bpc and 16 bpc and compare visible banding.','32-bpc floating point project settings alone do not mean the H.264 output becomes 32-bit floating point.','color effects','effects')

topic('ocio','OCIO/ACES 2.0 in a 26.5 project','Color & delivery','Configure input, scene-linear working space, display and render output deliberately.', '''
Color engine::Project Settings → Color includes Adobe color managed and OpenColorIO-managed options in supported builds; choose the appropriate engine for the production pipeline.
Config and transforms::ACEScg is a working-space concept, not an output display transform. In OCIO choose configuration, source interpretation, working color space, viewing and output correctly.
26.5 configuration::OCIO 2.5.1 includes ACES 2.0 CG v4.0 and Studio v4.0. Choose a pipeline-approved configuration, set a suitable scene-linear working space, and set the Output Module color space independently from the viewer.
''','Take one sRGB PNG, interpret it correctly in OCIO and export a Rec.709 display-targeted sample.','Do not accidentally apply a display transform twice, once in an effect and again at output.','color export','ocio history')

topic('expressions','Expression evaluation and safe syntax','Expressions & data','A property expression returns one calculated value at each time.', '''
Value vs action::A property expression is computed as the composition renders. It changes a property value; it cannot arbitrarily add layers or save files.
Functions::Use time, value, wiggle(), ease(), linear(), clamp(), loopOut(), valueAtTime(), sourceRectAtTime(), toComp() and matching property types. On Position return a 2D/3D array as appropriate.
Selection and errors::Alt+click a stopwatch to create/remove an expression; the expression enable/disable switch is safer for temporary comparisons. Enable expression errors and resolve missing referenced effects or layers.
''','Link one shape’s Rotation to another shape’s Position X coordinate via a scale mapping.','A pasted expression can silently refer to the wrong composition when copied across comps.','expression-language expression-controls','expressions expressions-basics')

topic('expression-language','JavaScript-like expressions, coordinates and values','Expressions & data','Learn syntax, evaluation, and data dimensions rather than memorizing snippets.', '''
Types::Numbers, arrays and strings differ. A 2D Scale returns `[x,y]`, Opacity returns one number, and Source Text can return a string or a compatible text style object.
Property chain::`thisComp.layer('NAME').transform.position` targets a concrete layer in current comp. `effect('Slider Control')('Slider')` reads a specific effect control; effect renaming changes the referenced path.
Timing::`time` is seconds, `framesToTime(n)` converts frames at context rate, and `posterizeTime()` alters expression sampling. `loopOut()` normally requires suitable keyed motion.
''','Build a scale pulse driven by a Slider and toggle the slider from 0 to 100.','Variables declared inside an expression are not globally stored between frames.','expressions auto-layout','expressions')

topic('expression-controls','Sliders, points, angles, colors and dropdowns','Expressions & data','Expose deliberate rig parameters on a named Null.', '''
Control interfaces::Expression Controls include Slider, Angle, Point, Color and other types. A readable named Slider like Swing Degrees is much easier to tune than hardcoded numbers across 12 expressions.
Reference correctly::Use the pick whip to generate exact effect/property paths. If a control is deleted or renamed unexpectedly, expressions can error and freeze or use fallback behavior.
Defaults and ranges::Although a Slider can store a large range, clamp incoming values in expressions when out-of-range results would cause negative size or absurd motion.
''','Make a master controller with Spin, Radius, Tint and Pause, then wire three layers.','A Slider is not automatically constrained to 0..100; clamp explicitly when required.','expressions essential-properties','expressions')

topic('data','CSV, JSON and AE data inputs','Expressions & data','Make content replaceable while preserving animation structure.', '''
Formats::CSV/TSV are suitable for flat tables and JSON for structured objects. A successful import does not guarantee the expression path to every nested field is what you assumed.
Reference models::`footage('file.json').sourceData` accesses JSON-like imported data; CSV/TSV may expose properties and dataValue access. Use the pick whip and inspect the actual imported shape.
Failure modes::Missing fields, wrong numeric types, commas in unquoted CSV fields and unexpected localized separators can break a template. Validate test rows including long names and zeros.
''','Render three number cards from a short three-row data file.','Do not bake confidential contact information into broadly shared MOGRTs without permission.','auto-layout mogrt','expressions')

topic('auto-layout','sourceRectAtTime and dynamic card padding','Expressions & data','Text changes require layout that uses current bounds rather than fixed-width guessing.', '''
Bounds::`sourceRectAtTime(time,false)` returns a text layer’s current layout bounds including left/top offsets. `width` and `height` are useful for a rectangular background size.
Alignment::The text bounding rectangle may be offset relative to anchor/Position. Align background and text in a shared coordinate context, or transform bounds with coordinate-conversion methods.
Padding::Add independent horizontal and vertical padding; test long, short and empty text. Set a reasonable maximum width or word wrapping to protect design.
''','Build one name badge that gracefully handles a two-letter name and a 30-character name.','sourceRectAtTime does not automatically reposition a background around the text anchor.','text expressions','expressions')

topic('essential-properties','Essential Properties as instance controls','Templates','Different nested instances can expose and override selected controls.', '''
Master source::Expose useful properties through Essential Graphics from an appropriate master comp; nested instances show the overrides as Essential Properties.
Individual versions::A reusable lower-third can use one source comp twice while individual instances have different title and color without altering shared internal animation.
Maintainability::Keep exposed properties few and well named. If required properties are missing or expressions refer elsewhere, the template can be difficult to customize.
''','Make two instances of a one-source badge and change the name and color independently.','An override in one instance is not a permanent edit to the original source.','mogrt precomp','mogrt')

topic('mogrt','Motion Graphics templates and protected timing','Templates','A .mogrt is a controlled reusable package, not merely an .aep saved under another extension.', '''
Interface design::Expose controls editors actually need: text, colors, durations and a few positions. Test user error cases and descriptive names before publishing.
Timing::Protected Regions allow selected intro/outro sections to remain unchanged when a motion graphics template is retimed. Inspect transitions at minimum/maximum intended durations.
Dependencies::Font installations, licensed plugins and expressions can affect an exported template. Verify compatibility with the target editing application where possible.
''','Create a 4-second MOGRT with intro, body and outro that maintains its intro/outro in an 8-second test.','A render or media proxy does not preserve MOGRT editability.','essential-properties collect-files','mogrt')

topic('puppet','Puppet deformation and mesh setup','Effects','Use pinned deformable geometry for flexible illustration and cutout work.', '''
Pins and triangles::Pin positions deform an underlying mesh, which is generated according to source alpha and tool settings. Put stable pins at joints/support points, not one pin per pixel.
Rig controls::Overlap determines which portions move in front/behind in relevant puppet modes; Starch stiffens a region. Test with a flat fill and no extra glow/blur to see deformation clearly.
Looping::For a 2-second cycle, match first/last pin poses and smooth speed. Test outlines at each extreme for holes or crumpled triangles.
''','Rig an arm with shoulder, elbow and wrist pins; make a clean wave.','A Puppet effect is not an automatic bone solver with awareness of anatomy.','shapes render-order','help')

topic('particles','Particles, emitters and simulation','Effects','Keep rate, lifespan, force and size separate.', '''
Population::Approximate live particle count at steady state = rate × lifetime, with caveats for frame sampling and survival settings. Changing Longevity and Birth Rate together can double-count a desired density.
Movement::Initial velocity, Gravity, Resistance and emitter position define trajectories. Explore physics controls one at a time, keeping all others constant.
Integration::A particle effect usually renders into the source layer’s context. For multiple depths, duplicate/precompose particle elements and use masks, mattes and lighting/glow appropriately.
''','Build one spark emitter lasting 0.5 seconds with 2 seconds of fading particles.','Many native particle effects are 2.5D images, not real shaded 3D particles.','effects effect-order','effects')

topic('simulations','Other simulation and stylize effects','Effects','Effects may generate pixels, distort existing pixels or simulate pseudo-physics.', '''
Families::Shatter and CC Pixel Polly break pixels into chunks; CC Ball Action makes a point/ball grid; Foam/CC Bubbles generate liquid/bubble impressions; Turbulent Displace warps the existing source.
Use by goal::Choose a particle emitter for autonomous moving pieces, Displacement Map for controlled deformation, and a texture/pixelation effect for stylized source conversion.
Parameter discovery::Find each effect’s exact 26.5 parameter list in installed Effect Controls and Adobe effect-specific documentation. The guide cannot truthfully specify parameters for every bundled/third-party revision.
''','Recreate the same stylized logo breakdown using Shatter and CC Pixel Polly; compare limitations.','Effects can be visually similar but have different layer size, sampling or cache behaviors.','particles procedural','effects')

topic('export','Render Queue decisions and preflight','Color & delivery','Choose deliverable-first settings and verify the resulting asset.', '''
Choose output::H.264 review media differs from editing mezzanine or RGBA master. Decide dimensions, frame rate, color space, audio, alpha and destination before opening Output Module.
Render Settings::Quality, resolution, frame blending, motion blur and time span are render decisions. Output Module chooses container, codec, channels, depth, audio, file path and color conversion.
Verification::Inspect the first, middle and last frames; play the complete audio; check output resolution, fps, file size and alpha in an external consumer. Record the settings with the deliverable.
''','Deliver three variants of the same comp and document why each is appropriate.','Do not rely on an MP4 H.264 file for transparency.','codecs alpha color','help')

topic('codecs','Containers, codecs, sequences and masters','Color & delivery','Understand what the extension can and cannot promise.', '''
Container vs codec::An .mp4 or .mov container can hold specific encoded video and metadata depending on the selected codec. ProRes/DNxHR/PNG/EXR differ in compression, color bit depth and alpha support.
Image sequences::A numbered PNG/EXR sequence preserves individual frames and may be resilient to interrupted renders, at the cost of many files and more management. Verify channel and color settings.
Review vs mezzanine::A small H.264 review is convenient; a high-quality intra-frame master or sequence is better for multiple rounds of effects/grading where supported by the pipeline.
''','Render one 5-second RGBA element as a PNG sequence and confirm it recomposites cleanly in a fresh comp.','Setting alpha in an output module cannot add a channel that a format lacks.','export alpha','help')

topic('collect-files','Collect Files and portability','Color & delivery','An independently openable archive is the real deliverable test.', '''
Collection::File → Dependencies → Collect Files copies referenced sources under chosen options and prepares a project. Confirm which proxies, unused items and plugin dependencies are included or omitted.
Missing files::Use Replace Footage and search folders to relink. Record stable relative subdirectories and verify no source still points to the old workstation.
Team handoff::Attach a README, screenshot/proof render and font/plugin list. Embed licensed third-party files only where your license permits.
''','Reopen the collected copy with the original media drive disconnected.','A linked external Photoshop/Illustrator asset can be missing even when the project opens.','project-management export','help')

topic('performance','RAM, disk cache and preview rate','Troubleshooting','Decide whether the bottleneck is decoding, rendering, memory or output.', '''
Cold vs warm preview::The first pass calculates and caches frames. A replay may be far faster; changing a property can invalidate cached regions. Time only like-for-like comparisons.
RAM and cache::Memory preferences reserve RAM for other apps. Disk cache stores reusable intermediate frames on local storage; purging makes cached work disappear and may make the next playback slower.
Multiframe::When effects/plugins and resources permit, multi-frame rendering can render independent frames in parallel. Its gain depends on the shot, CPU, GPU, memory and media constraints.
''','Time two previews before/after turning off an expensive effect; record whether the change helps cold and warm runs.','Do not blindly assign all RAM to AE at Windows’ expense.','cache proxies','memory multiframe')

topic('cache','Cache levels, purging and invalidation','Troubleshooting','A cached preview is reused work, not a permanently rendered file.', '''
Viewer vs memory::Green/blue cache indicators and preview panels tell you about cached ranges and conditions. Preview may re-render after color/render setting changes even when footage is unchanged.
Disk vs RAM::RAM cached frames are short-lived; persistent disk cache may survive a restart for eligible intermediates. The exact behavior depends on source/effect and cache settings.
When to purge::Purge only for a diagnostic reason, corruption or disk management; capture a baseline first. Running out of free disk space can produce errors unrelated to the actual comp design.
''','Change only one Glow parameter and observe which frames need rerendering.','A preview cache does not substitute for a verified final exported master.','performance diagnostics','memory')

topic('proxies','Proxies, pre-renders and fast preview','Troubleshooting','Substitute cheaper pixels while retaining an exact source of truth.', '''
Footage proxies::Assign a lower resolution/quality proxy to complicated sources and clearly indicate which file is active. Some export paths may use source or proxy depending on settings.
Pre-render::For a computationally expensive nested composition, generate a high-quality render, then substitute it for iteration. Keep original comps and a versioned render path.
Final review::Before delivery verify source/proxy switch and any downsampled raster effect resolutions. A Quarter view is a performance choice, not proof of final sharpness.
''','Produce a small proxy of a 4K clip, edit a 1080 comp, and verify which frames use proxy vs original.','A proxy can hide scaling or codec artifacts that appear in the full-quality source.','performance export','help')

topic('diagnostics','A structured debug decision tree','Troubleshooting','Reduce a failure to one reproducible cause.', '''
Picture missing::Check active viewer, comp time, video switch, In/Out span, alpha, mask, matte, opacity, solo/shy, 3D camera, effect stack and codec decoding.
Picture incorrect::Compare ungraded sources, then source interpretation, effect order, color working/display/output transforms, precomp switches and full-quality render.
Performance failure::Test a short work area, one expensive layer, one plugin at a time and a different source codec. Do not diagnose a whole project only from the CPU/GPU model name.
''','Take a deliberately broken comp and identify the exact stage that makes it wrong.','Multiple small causes can compound; one switch may not solve everything.','missing-effects cache','help')

topic('missing-effects','Missing plugins, effects and unsupported version','Troubleshooting','A project can load without having the effect that produced a previous render.', '''
Diagnose source::Check built-in Effects & Presets, Effect Manager, installed add-on version, licensing, Windows-only plugin paths and whether the effect debuted in 26.x.
Avoid false fixes::A missing plugin is not repaired by renaming an arbitrary different effect. Preserve the original project, replace intentionally, and compare the new render against a reference.
Compatibility::32-bpc, GPU acceleration, renderers and external plugin versions vary. Some old effects are marked Obsolete but may load older compositions for compatibility.
''','Simulate missing effect by disabling one installed effect instance, save a test and document the visual fallback.','Saving for an earlier release does not back-port unsupported native effects or mesh/material features.','diagnostics version-workflow','effects history')

topic('scripting','ExtendScript and project automation','Advanced','Build deterministic and reversible changes from scripts.', '''
Object hierarchy::JSX/ExtendScript scripts use the AE scripting API: application, project, items, compositions, layers, properties and render queue. This differs from time-evaluated expressions.
Safety::Use try/finally/undo groups, validate active project/item types and test on a versioned copy. Avoid unreviewed scripts from unknown sources.
Repeatability::Use explicit comp names, prefixes and logs. Keep external input CSV/JSON stable and back up files before automatic relinking, renaming or rendering.
''','Write a no-op JSX report listing current comp names and save its result outside the source .aep.','JSX scripting is distinct from modern browser JavaScript modules or Node package installs.','expressions project-management','help')

topic('file-management','Missing media, absolute paths and Windows storage','Troubleshooting','Drive letters and renamed folders can silently disrupt a project.', '''
Paths::If imported files move on disk, AE’s Project items can become missing. Relink footage from Project with Replace Footage, and inspect affected duplicates/sequences.
Cache vs original::Disk cache is disposable processed data; imported source assets are not. Do not delete Assets because AE cached a preview.
Pack and transfer::Collect Files with source folders, then test the collected copy by opening it from a different folder. Include any external audio, fonts, 3D textures and LUT references.
''','Rename an asset folder in Windows Explorer, observe the missing footage, and relink correctly.','A project opened successfully can still have one or more missing media items.','collect-files project-management','help')

topic('workflow','Repeatable production and QC workflow','Capstone','Tie the individual skills into a dependable result.', '''
Define output first::Agree on resolution, FPS, duration, codec, color, audio, alpha and revision rules before building layered animation. This determines composition settings and source requirements.
Build in passes::Block the story and timing, then implement graphics and track/roto, then add color, simulation and audio, finally handle render settings and QC.
Review every layer of delivery::A clean .aep, collected assets, fonts/plugins manifest, proof render and verified master are separate deliverables. Keep revision notes and a known-good prior version.
''','Create a one-page checklist you can apply to any new client motion graphics job.','A single green check mark in Render Queue is not complete quality assurance.','capstone export project-management','help')

topic('capstone','Final self-assessment and future practice','Capstone','Demonstrate independent ability rather than recall of one memorized recipe.', '''
Foundations::Build and animate a three-layer shape composition without referring to menus. If you need the guide, identify the exact missing concept rather than rewatching unrelated tutorials.
Compositing and effects::Make one alpha matte, one chroma key/rotoscope, one procedural transition, a controller-based rig and a correctly managed render.
Maintenance::Reopen a collected project on a different path, diagnose one deliberately missing source, and explain why later-version shortcuts do not apply in your installed build.
''','Complete the final lesson, then modify three visual decisions without following the original exact steps.','A certificate is not meaningful without repeatable hands-on work.','workflow diagnostics','help')

# Modern stable workflows, grouped by task rather than release-note order.
topic('release-26-5','What changed through 26.5','Foundations','Locate modern tools without relearning the foundations.', '''
2026 foundation::26.0 introduced native parametric meshes, Substance materials, variable-font axis animation, Unmult and Compressor/Gate/Distortion. SVG import was subsequently expanded; use current 26.5 import controls instead of an older workaround.
Faster operations::26.2 added Quick Apply, Object Matte, material displacement and Proportional Scrubbing. 26.3 added Curl Noise, Advanced 3D depth of field, improved Mask Tracker, vector clipboard transfer and Copy Frame to Clipboard.
Current release::26.5 improves guide placement, effect-instance labels, Effect Controls and Object Matte caching, and bundles ACES 2.0 via OCIO 2.5.1. These changes affect organization, reuse and color as well as visible imagery.
''','Open one tool from each release family, then choose one that improves your own project.','A feature-history date and a later expanded workflow are different facts.','quick-apply object-matte responsive-guides ocio beta-watchlist','release whats-new history')

topic('quick-apply','Quick Apply: effects, presets and commands','Effects','Find the operation by name, with a deliberate target.', '''
Open and filter::Select the intended layer(s), press Ctrl+Enter or use Edit → Quick Apply. Prefix e: for effects, p: for presets or m: for menu commands. Choose the matching result and press Enter.
New layers::Inside the dialog, Ctrl+Enter applies the selected effect/preset to a new solid or layer; Ctrl+Alt+Enter creates an adjustment layer. Read the modifier hints for that result. Creating an adjustment changes which underlying pixels are processed.
Inspect::F3 opens Effect Controls. Check preset-added keys at the playhead, remove only unwanted properties and undo if it affected the wrong selection. A command result can act on the project rather than the selected layer.
''','Apply Glow to a selected shape, then apply it to a new adjustment layer and explain the changed scope.','Ctrl+Enter opens the dialog outside it, but applies to a new layer while inside it.','effect-order adjustment-effects','quick-apply')

topic('object-matte','Object Matte: select, propagate, refine and cache','Compositing','Extract an object, then judge the matte across time.', '''
Base selection::Double-click the footage layer to open Layer panel. Choose Object Matte from the toolbar, hover a clear subject and click. Use rectangle/lasso or Quick Selection and Selection Brush to correct included/excluded areas; Refine Edge helps hair.
Propagation::Advance through the required span, inspecting occlusions and pose changes. Correct errors, then Freeze from the Layer panel once the span is ready. Check the result over contrasting backgrounds before using it as a track matte.
Persistence::26.5 stores propagation on disk for reuse after reopening. Keep disk space available. Cached analysis and a saved project are different from an exported alpha master; changing the selection can require more propagation.
Shortcut conflict::Adobe’s Object Matte page lists Ctrl+W, while the general shortcut reference assigns Ctrl+W to Close. Use the toolbar or verify/remap the command in the installed editor; the documents do not establish a reliable focus rule.
''','Isolate two seconds of a moving subject, inspect every frame, save/reopen and compare the matte before export.','Disk caching does not certify an edge or replace footage/project backups.','roto mask-tracking mattes','object-matte shortcuts')

topic('responsive-guides','26.5 guides: pixels, percent, edge pinning and color','Animation','Design margins that remain meaningful as the canvas changes.', '''
Placement::In the intended viewer show rulers (Ctrl+R), drag out a guide, then right-click → Edit Guide. Set orientation, pixel/percent units, reference edge and color. View → Add Guide provides numeric placement directly.
Responsive reference::Use a percentage for proportional position, or a pixel offset from right/bottom for a fixed opposite-edge margin. During dragging, Alt changes units and Ctrl toggles pinning. Pinning changes the reference; locking (Ctrl+Alt+Shift+;) prevents movement.
Reuse and scope::Guides belong to the active view; they do not automatically reposition artwork or render into a movie. Export/import with View → Export Guides / Import Guides. Adobe’s page retains contradictory old import notes after its explicit 26.5 preservation statement: verify a round trip in the actual destination build.
''','Set a 50% vertical guide and a 100-pixel right margin; change a duplicate comp’s width and compare their positions.','Guides, guide layers and grid overlays are different; none is an automatic layout rig.','coordinates auto-layout','guides')

topic('effect-labels','Effect labels, masks and reusable presets','Effects','Keep long stacks readable while controlling each effect’s scope.', '''
Organization::26.5 modernizes Effect Controls and allows a color label on an individual effect instance. Select the gray label swatch beside the effect name and choose a color; use a purpose-based name. Colors organize controls; they do not change pixels or combine effects into one calculation.
Local contribution::Draw a mask, set Mode=None when it should not cut layer alpha, then expand the effect in Timeline → Compositing Options and add a Mask Reference. Tune mask feather and Effect Opacity, watching effect support and render order.
Reuse::Select the intended effects/properties and use Animation → Save Animation Preset for an .ffx. A preset stores selected settings/keys, not fonts, footage or plug-in installers. Apply on a duplicate at a known CTI and inspect changes.
''','Make a masked Curves correction, name/color its effect, save the preset and test it on a duplicate layer.','A Timeline layer label and an Effect Controls instance label are independent.','effect-order masks effects','effect-controls effects-overview')

topic('proportional-scrubbing','Quick Offset versus Proportional Scrubbing','Animation','Distribute either time or numeric changes without confusing the gestures.', '''
Time::Select layer bars or keys in the intended order. Ctrl+Alt-drag in Timeline uses Quick Offset to spread timing. The first selection anchors the distribution; a layer offset carries its internal animation with it.
Values::For Proportional Scrubbing, select layers/properties in order, then Ctrl+Alt-drag the property hot text. The first gets zero added change, the last the full change and intermediate selections fractions. Three layers and a 120-pixel change receive offsets 0, 60, 120; unequal initial positions need not become equal final spacing.
Group boundaries::Shift+[ aligns the earliest In of the selection to CTI, Shift+] the latest Out, preserving relative timing. Alt+Shift brackets adjust the corresponding boundary group. Ordinary brackets instead use each layer’s own boundary. Check source handles when extending footage.
''','With three initially aligned cards compare a 120-pixel proportional change with a timing offset; undo between trials.','Ctrl+Alt is the same modifier family, but dragging bars and dragging hot text perform different operations.','timeline keyframes motion-design','proportional layers')

topic('svg-workflow','SVG file import and vector clipboard transfer','Animation','Choose source linkage or editable geometry intentionally.', '''
File route::Use File → Import → File and choose SVG footage or composition as appropriate. A composition provides editable vector layers; footage behaves as a source item. Compare imported fills, gradients, strokes, grouping and bounds before animation.
Clipboard route::In Illustrator enable Edit → Preferences → Clipboard Handling → Include SVG Code. Copy artwork, then Ctrl+V in AE to add editable shapes. With no selected comp, a composition can be created. Other apps must actually put SVG data on the clipboard; copying XML as plain text is different.
Text and fidelity::Outline SVG text before this paste route, retaining the editable original elsewhere. Stable editable shape import does not establish editable Illustrator-text conversion, which remains Beta. Compare appearance at enlarged scale and inspect individual groups.
''','Import samples/badge.svg as footage and as a composition; recolor one shape and explain which source stays linked.','SVG text and every browser SVG filter are not guaranteed to transfer as editable AE objects.','shapes import-media beta-watchlist','svg')

topic('variable-fonts','Animate variable-font axes and spacing','Text & data','Animate genuine font variation while keeping the text editable.', '''
Prerequisite::Use a variable font whose installed file exposes axes such as Weight, Width or Slant. Multiple static font weights alone are not a variable font. The font filter can help locate variable families.
Animate::Expand the text layer, choose Animate → Variable Font Axes → the supported axis. Enable its stopwatch, move CTI and set another value within that font’s range. Use the Range Selector for character/word subsets.
Layout::Text → More Options → Variable Font Spacing controls compensation during axis changes. Compare spacing modes, multiline wrapping and the same font on the rendering machine. Width animation and layer Scale produce different letter shapes and spacing behavior.
''','Animate one word’s Weight over 24 frames and use a selector to send the change across characters.','A missing axis is usually a font capability issue; do not invent unsupported axis limits.','text text-animator auto-layout','variable-fonts')

topic('parametric-meshes','Native parametric meshes and material appearance','Tracking & 3D','Build simple real geometry instead of using a sphere image effect.', '''
Create::Use Advanced 3D and the Parametric Mesh toolbar tool or Layer → New to create a primitive. Inspect Mesh Options, supported Bevel Options and material assignment. Ctrl draws from center, Shift constrains proportions while drawing.
Appearance::Change Base Color, Roughness and Metallic, then compare lighting at the same camera pose. Material Emission changes appearance but does not illuminate neighboring objects; use a light for illumination.
Geometry::Mesh controls change scene geometry. CC Sphere instead renders a sphere-like image from layer pixels. Choose a native mesh for perspective/lighting interactions and keep geometry detail appropriate to the visible result.
''','Create a cube and sphere with contrasting roughness, orbit a camera and identify which highlights follow the environment.','A native mesh and an extruded text/shape layer are different object types.','3d-renderers substance-materials advanced-dof','meshes')

topic('substance-materials','Substance SBSAR and real mesh displacement','Tracking & 3D','Separate surface shading from geometric displacement.', '''
Assign::Import an .sbsar material, apply it to a supported model or parametric mesh and inspect its exposed controls. Keep the SBSAR file and texture dependencies with the project. A material preset can expose different controls from another material.
Height::Use the supported displacement controls on a parametric mesh with a suitable height input. Increase displacement modestly and inspect silhouette, surface detail and rendering cost. A bump/normal appearance does not necessarily change the silhouette; displacement can.
Stable boundary::26.5 supports this mesh/model workflow. Animated layers as material inputs and Substance assignment to 3D text/shapes are separately listed Beta features. A missing material after reopening may require Reload Footage; compare Adobe known issues before rebuilding the scene.
''','Compare a textured primitive with displacement off/on under identical camera/light settings and document dependencies.','A 2D Displacement Map effect remaps pixels; it does not create this geometry.','parametric-meshes 3d-models','substance material-properties known-issues')

topic('advanced-dof','Advanced 3D in-engine depth of field','Tracking & 3D','Focus an actual 3D scene using camera distance.', '''
Scene setup::Choose Advanced 3D in Composition Settings and create a camera with objects at visibly different distances. Enable Camera Options → Depth of Field. Inspect the scene in Active Camera, not only a custom view.
Focus::Set Focus Distance to the intended object depth; adjust Aperture and Blur Level for the desired amount. Animate focus between objects and inspect edge quality at Full resolution. Render a short sample because interactive quality can differ.
Distinctions::This in-engine capability arrived in 26.3. Camera Lens Blur uses a 2D grayscale blur map; the older Depth of Field effect needs suitable depth data. Neither is automatically a scene-camera DOF switch. More blur cannot reveal an occluded object.
''','Rack focus between a near cube and far sphere over 48 frames, then compare the first/middle/last rendered frames.','An f-stop/aperture change in a simulated scene does not guarantee photographic exposure changes.','cameras parametric-meshes depth-maps','advanced-dof')

topic('curl-noise','Curl Noise: a flowing texture experiment','Effects','Control structure separately from motion and color.', '''
Start::Create a comp-sized solid and Quick Apply e:curl noise. Begin with Internal input. Compare spatial Scale and Swirl before adding color; a large preview area makes pattern changes easier to judge.
Motion::Speed/Direction drift the input; Evolution changes its state; Turbulence Speed changes temporal activity. Inspect Input Noise, Curl Generation and Final Render to isolate the stage creating a result. Flow sampling controls affect continuity and cost.
Use::Tint or Tritone can colorize the rendered field. Precompose when using it as a Displacement Map source or luma matte, and choose the appropriate sampled layer stage. For a loop, stop unrelated drift, cycle the intended controls and test the join; Evolution alone does not guarantee a seamless loop.
''','Make two four-second textures with identical color but different scale/flow, then use one as a matte.','This is procedural texture rather than a fluid solver with collision-aware smoke.','procedural effect-order depth-maps','noise')

topic('unmult','Unmult: convert a black or white backing into alpha','Compositing','Build transparency that can travel to another application.', '''
Input::Use a suitable black- or white-backed element. Apply Unmult through Quick Apply or Keying. Choose the Background Color mode; inspect alpha separately using Alt+4.
Edges::Tune the corresponding level, Softness and Remove Color Matting. Judge semitransparent edges over dark and light backgrounds. Protect genuine black/white foreground regions with another matte if they must survive.
Output::A Screen blend can visually hide black over one background while leaving different alpha semantics. For reusable assets, render to an alpha-capable format with RGB+Alpha, then reimport and inspect both color and transparency.
''','Unmult a black-backed light element and recompose its RGBA export over gray and magenta.','Removing a background cannot reconstruct foreground color information destroyed in the source.','alpha keying export','keying-effects')

topic('audio-dynamics','Compressor, Gate and Distortion in 26.5','Audio','Treat loudness, pauses and saturation as separate tasks.', '''
Dynamics::Compressor reduces louder passages above a threshold; adjust Ratio, Attack and Release, then match bypass loudness before judging. A louder result is not automatically cleaner.
Pauses::Gate attenuates below threshold. Set it relative to the actual noise floor and tune Hold/Release to preserve word endings. It does not remove noise mixed under active speech.
Sound design::Distortion changes timbre. Start with low Drive and modest Mix, compensate output Volume and check peaks in the rendered audio. Resolution/downsampling make intentional digital degradation. De-esser remains Beta at this cutoff; do not expect it in stable.
''','Process samples/pulse.wav and a recorded phrase on duplicates, level-match bypass and compare a rendered WAV.','An audio effect does not generate a visual waveform or automatically detect musical beats.','audio audio-reactive beta-watchlist','audio-effects')

topic('clipboard-frame','Snapshots, clipboard frames and rendered stills','Foundations','Choose an inspection image or a controlled production still.', '''
Internal comparison::Viewer snapshots use Shift+F5 through Shift+F8 to store, F5 through F8 to compare. These are temporary comparison aids, not asset exports.
Clipboard::Activate Composition, Layer or Footage and use Ctrl+Alt+Shift+F5 after the frame renders. Transparency Grid affects whether alpha is preserved for a supporting destination. The copy reflects viewing/color-management transforms; receiving apps choose a supported clipboard format.
Production::Ctrl+Alt+S queues a still through Render Queue. Choose channels, precision and output color deliberately for production; do not treat a clipboard screenshot as an unmanaged scene-linear EXR.
''','Copy a translucent shape with the transparency grid on/off and compare with an RGB+Alpha still render.','Destination clipboard support can differ even when AE supplies transparency.','color alpha export','copy-frame')

topic('native-null-controllers','Native null controllers for points and paths','Expressions & data','Use maintained menu commands when a path needs reusable controls.', '''
Point properties::Select a positional property or effect point and use Layer → Create → Null Controllers for Positional Points. Selecting a layer alone targets Position. Animate the generated null and inspect expression/Layer Control links.
Path direction::For a selected Path, Null Controllers for Path Points lets nulls drive vertices; Nulls Following Path Points does the reverse; Null Tracing Along Path creates a traveling control. These commands are also available through Animation → Keyframe Assistant.
Rigs::Use the JavaScript expression engine and distinct names. Shape-group skew/nonuniform scale or separating Position dimensions after linking can need repair. The older Create Nulls From Paths script panel has related operations under different labels.
''','Create an arrow following a curved path with Null Tracing Along Path and change the path afterward.','Select the actual property, not only the layer, for path-specific commands.','paths parenting expressions','null-controllers')

topic('profiler','Composition Profiler, ROI and compressed cache','Troubleshooting','Measure the operation you intend to accelerate.', '''
Timings::Enable the Timeline Render Time column using its snail icon or column menu. Expand a layer to compare effects/masks. Cached readings can include retrieval and carry an asterisk; compare the same frame, resolution and cache state.
Area::ROI restricts preview work. Crop Comp to Region of Interest changes the canvas; Output Module cropping changes the delivered area. These operations have different consequences. Turn ROI off for final whole-frame review.
Storage::Lossless compressed disk frames trade cache storage and processing without lossy export changes. Preferences → Disk → Disk Cache → Enable Compressed Frames (Lossless) controls it. Diagnose specific failures before disabling it; the known crash notice names 26.0/26.2, not a blanket 26.5 defect.
''','Measure cold/warm timings for a short Glow stack and compare an ROI preview without changing delivery settings.','Do not report cache replay timing as uncached final-render throughput.','performance cache proxies','profiler compressed-cache known-issues preview')

topic('beta-watchlist','Stable versus Beta: read newer tutorials critically','Foundations','Keep the 26.5 offline guide usable without Beta-only commands.', '''
Cutoff::Adobe’s Beta page checked 2026-10-28 was updated October 7. It separately lists Contour Paint, De-esser, AI Assistant, animated layers as material inputs and Substance materials on 3D text/shapes.
More experimental tools::Editable Illustrator-text conversion, Quick Set Anchor, broader viewer Alt-drag duplication, PNG compression selection, Account/Stock panels and enhanced Auto-Save are on that list. Their appearance in the shared documentation sidebar is not release evidence.
Project decision::Use stable alternatives for a 26.5 handoff: shape outlines, ordinary anchor controls, Ctrl+D, supported mesh materials and standard save/backup workflows. If you deliberately use Beta elsewhere, document that separate dependency and provide a compatible render.
''','Identify one tutorial using a Beta feature and explain a stable 26.5 way to achieve a comparable result.','Mesh-specific Alt-drag in stable documentation does not prove generalized viewer duplication is stable.','version-workflow release-26-5','beta')

topic('expression-examples','Copyable expression building blocks','Expressions & data','Use complete references, correct dimensions and an inspectable coordinate system.', '''
Scalar and vector::On Rotation, `time*90;` produces 90 degrees per second. On 2D Scale use `s=100+Math.sin(time*2)*10; [s,s];`. Put expressions on the intended property; an array and a scalar are not interchangeable.
Measured text card::For a simple background shape in the same untransformed context as a text layer named CAPTION, use `r=thisComp.layer("CAPTION").sourceRectAtTime(time,false); [r.width+40,r.height+24];` on Rectangle Path Size. Its group Position also needs `[r.left+r.width/2,r.top+r.height/2]` relative to the text origin; parent/align origins deliberately before linking. Size alone does not center the card.
Coordinate conversion::For a 2D follower’s Position, use `src=thisComp.layer("LEADER"); p=src.toComp(src.anchorPoint); hasParent ? parent.fromComp(p) : p;`. Inspect parent spaces and the returned dimensions; a 3D rig may require world-space methods instead.
Controller::On Rotation use `time*thisComp.layer("CTRL").effect("Speed")("Slider");` after creating and naming the null/slider. Use the expression pick whip for exact references and expose controls rather than duplicating constants.
''','Build a labeled rotating badge with auto-sized text backing, then parent the rig and test the coordinate links.','The displayed expression is evaluated per property; it cannot create layers as a JSX script would.','expressions auto-layout expression-controls','expressions')

topic('expression-lookup','Modern dropdown labels, key lookup and range mapping','Expressions & data','Read a configured control without maintaining duplicate label lists.', '''
Dropdown::An eligible dropdown property exposes .text for its current label, .items for its label array and .textAtTime(t) for a sampled label. On Source Text, `thisComp.layer("CTRL").effect("Choice")("Menu").text;` needs an actual renamed dropdown control. Menu values are one-based; .items arrays are zero-based. Use numeric indices for portable logic because labels can be localized.
Key lookup::nextKey(t) returns the later key or the last at the end. previousKey(t) returns a key at/before time or the first before the start. Check numKeys before querying an empty property or marker stream; J/K are unrelated UI navigation.
Range behavior::linear(x,a,b,c,d) holds endpoint output values outside the input range; ease also holds its endpoints. For deliberate scalar extrapolation write the arithmetic explicitly, for example `20+(value/100)*180;`. Validate zero input spans in reusable rigs.
''','Drive a text label from a named Dropdown Menu Control and compare the current label with one sampled a second earlier.','String matching can fail after localization or renamed choices; numeric logic can remain stable.','expression-language expression-controls data','expressions')

topic('outline-styles','Text outlines, Layer Styles and source editability','Text & data','Choose geometry conversion separately from live text and effect outlines.', '''
Outlines::Select a text layer and use Layer → Create → Create Shapes From Text or Create Masks From Text. Keep the original text: generated outlines do not update when wording changes. Inspect holes in compound letters before animating vertices.
Styles::Layer → Layer Styles includes shadow, glow, bevel, overlay and Stroke options. These are Timeline style properties with their own render behavior, rather than ordinary Effect Controls instances.
Stroke choices::A style Stroke follows visible layer content; Generate → Stroke follows a mask path; a shape Stroke styles its geometry. Use shape Trim Paths for a designed line reveal, a mask Stroke for mask-based writing and a style for a silhouette outline.
''','Compare the three Stroke approaches on duplicated artwork and record which remains editable as text.','Converting artwork to paths sacrifices source-string editability; retain a source version.','text shapes strokes','text-outlines layer-styles')

topic('immersive','360-degree imagery and seam-aware effects','Effects','Convert between spherical panoramas and a normal viewer intentionally.', '''
Projection::Use suitable equirectangular source imagery. VR Sphere to Plane makes a rectilinear view; VR Plane to Sphere puts planar imagery into a spherical projection. These work with appropriate still or moving sources.
Seams::Use immersive-aware effects for work across panorama seams, then inspect the full wrap rather than only a center viewport. Ordinary planar blur/distortion can create a discontinuity at the edge.
Workflow::Use VR Comp Editor or a deliberate nested-comp setup where available, retaining source projection and destination dimensions. CC Environment is another environment-mapping effect, not a stills-only counterpart to video-only VR effects.
''','Project a panorama to a normal frame, animate the view and inspect a seam-spanning effect in the wrapped source.','A spherical projection is not editable geometric scene depth.','3d-intro effects','immersive')

RECIPES=[]
def recipe(id,title,category,goal,steps,verify,fail,level='Intermediate',sources='help'):
 RECIPES.append(dict(id=id,title=title,category=category,goal=goal,steps=[s.strip() for s in steps.strip().split('\n') if s.strip()],verify=verify,fail=fail,level=level,sources=sources.split()))
recipe('logo-reveal','01 · Logo reveal using a matte','Compositing','Animated shape reveals a graphic without destroying its pixels.','''
Create a 1920×1080 24-fps composition and center a logo PNG with transparency.
Create a white rounded rectangle as a fixed reveal window covering the logo’s final position. Position the logo entirely outside the window at the start.
On the logo layer select the rectangle as an Alpha Matte source; use F4 if the TrkMat column is hidden.
Animate the logo into its final position inside the stationary matte over 20 frames. Ease the entrance and inspect alpha; the full final logo must remain inside the window.
Place a second copy of the logo at low opacity underneath for a tasteful ghost trail, only if readability improves.
''','The logo is never visibly stretched and is fully revealed by frame 20.','If the entire rectangle renders, verify it is functioning as a matte source and that matte settings reference the intended layer.','Beginner')
recipe('text-window','02 · Footage visible through moving text','Compositing','Use letters as an alpha matte.','''
Create a new composition containing video and a large text heading on separate layers.
Place the text as the source of the footage layer track matte (Alpha Matte).
Animate the text’s Position or scale so the visible video window moves across the frame.
Add a background solid below the video. Fade the matte text after a hold while keeping the background visible.
Test Alpha Inverted Matte and compare which parts of the footage show.
''','Footage is visible inside the glyphs only, without black squares.','Do not mistake Screen blending for a matte.','Beginner')
recipe('lower-third','03 · Reusable lower third with Essential Properties','Templates','Separate animation from editable name/role content.','''
Build a 1920×1080 child comp with two text layers and a shape-rectangle background.
Place all layers under a controller Null, then animate entrance over 10 frames and exit over 10 frames.
Open Essential Graphics, expose name text, role text and primary fill color with descriptive labels.
Nest the comp twice in a master; override the name/role independently using Essential Properties.
Export a MOGRT after checking typography bounds and protected regions when appropriate.
''','Two independent instances show different content with the same timing and art direction.','If one instance unexpectedly changes both names, you edited the shared source rather than an override.')
recipe('track-title','04 · Track a title onto moving footage','Tracking & 3D','Convert tracked pixels into a Null animation.','''
Import a short shot with a stable high-contrast mark and create a comp from it.
In Tracker choose Track Motion and place Feature and Search Regions around the mark.
Track forward, correcting any drift frames. Create a Null and apply the tracking data to it.
Parent a title layer to the Null; position the text relative to the intended feature.
Add an outline/background to keep the title legible and preview each frame.
''','The text follows the mark accurately for the full intended shot.','A drifting null needs tracker correction; smoothing the title keys alone is not an accurate fix.')
recipe('corner-pin','05 · Replace a moving sign/screen','Tracking & 3D','Map a replacement layer into four moving corners.','''
Choose a shot of an almost planar screen or poster with visible texture.
Open bundled Mocha AE from the effect integration, draw a planar region and track the shot.
Set/verify a planar surface with the correct corner order; transfer corner pin data using the integration available in 26.5.
Place a bold checkerboard into the replacement comp and inspect alignment at each frame.
Replace the checkerboard with the desired screen contents; match blur, exposure and noise.
''','Checkerboard corners remain anchored and final insert has no glaring seams.','Perspective slippage usually indicates an unstable plane or the wrong corner calibration.')
recipe('green-key','06 · Keylight clean screen composite','Compositing','Isolate a foreground subject cleanly.','''
Place evenly lit green-screen footage above a neutral background.
Apply Keylight (1.2); pick a green patch as Screen Colour.
Select Screen Matte view, tune Clip Black and Clip White gently, then return to Final Result.
Add garbage mask, Key Cleaner and Advanced Spill Suppressor where useful.
Check edges over black, white and saturated backgrounds, and verify 10 consecutive frames.
''','Subject retains hair details without a green line or black halo.','A crushed Screen Matte can erase semitransparent hair.')
recipe('roto-cutout','07 · Roto Brush character cut-out','Compositing','Extract a moving person without a green screen.','''
Open the subject video in Layer panel and activate Roto Brush.
Mark foreground and remove unwanted selected regions, starting at a good base frame.
Propagate through a 2-second segment, fixing errors around hands and head.
Use Refine Edge for hair and tune matte edge controls modestly; Freeze the result.
Place a background layer behind the cutout and render-check the complete segment.
''','The subject is clean on at least two contrasting backgrounds.','If propagation fails, compare Object Matte, Quick Selection and Refine Edge, inspect the base frame and correct occlusions.')
recipe('handwriting','08 · Handwriting from a traced mask','Animation','Use the Stroke effect to reveal a line.','''
Place scanned writing on a comp-sized solid or duplicated image as an image guide.
Draw one or several mask paths along the visible pen stroke in the correct order.
Apply Generate → Stroke, choose the mask(s) and Paint Style appropriate to the reveal.
Animate End from 0 to 100 over the intended write-on duration.
Use a white reveal matte or controlled Alpha Matte to reveal a separate textured ink layer when needed.
''','Strokes appear in a plausible writing order and do not reveal undesired connecting lines.','Stroke operates along masks, while Trim Paths operates on shape contents.')
recipe('stroke-icons','09 · Animated loading ring with Trim Paths','Animation','Make a ring that draws itself without raster effects.','''
Draw a shape ellipse with Fill set to None and Stroke to a visible color/width.
Inside Contents add Trim Paths and animate End from 0 to 100 over 16 frames.
For a spinning partial ring, set Start/End to reveal one arc, then animate Offset.
Add a Repeater or a second ring for additional visual structure, without unnecessary plugins.
Preview at target size to check line cap and antialiasing.
''','Ring draws cleanly and is readable at one quarter of comp size.','A fill may hide the open stroke if left enabled.','Beginner')
recipe('stagger','10 · Staggered cards using Quick Offset','Animation','A 25.4+ timeline technique to spread entrances in time.','''
Create five shape cards stacked at the same center, each with a 10-frame Position entrance.
Select the intended layers in sequence, making sure selection order matches desired timing.
Hold Ctrl+Alt and drag the selected layer bars (Quick Offset) to distribute the group over time.
Inspect the earliest and latest start times; trim unwanted overlaps if necessary.
Preview and compare with manually offsetting keyframes only.
''','Entrances are staggered without changing each layer’s internal animation.','Quick Offset changes timing. Proportional Scrubbing changes property values; Shift+[ or Shift+] moves a staggered layer selection as a group.')
recipe('logo-pulse','11 · Beat-reactive pulse','Audio','Drive scale from audio-derived keyframes.','''
Import an audio file and use Convert Audio to Keyframes.
Select a logo and add a 2D Scale expression referencing Audio Amplitude → Both Channels Slider.
Use `a=thisComp.layer("Audio Amplitude").effect("Both Channels")("Slider"); s=100+Math.min(20,a*1.5); [s,s];` on 2D Scale, verifying names against your generated controller.
Preview with sound and observe peak reactions; smooth or cap peaks where needed.
Add a 10-frame opacity fade and export an audio-enabled review file.
''','Logo scales gently with the sound and never collapses during quiet segments.','Array dimensionality errors cause red expression warnings.')
recipe('depth-dolly','12 · Parallax from a still photograph','Tracking & 3D','Cut source artwork into near/mid/far planes.','''
Prepare a background image and two transparent foreground cutouts from the same photo.
Import each as a layer, enable 3D and spread them apart on the Z axis while preserving intended screen placement.
Create a camera and make a short lateral dolly/arc that reveals a depth difference.
Extend hidden background under the foreground silhouette to prevent holes.
Add subtle light/blur in the appropriate renderer and preview both camera extremes.
''','The foreground moves more than background without revealing empty cutout edges.','Scaling a single flat photograph is not real parallax.')
recipe('camera-dolly','13 · Simple camera orbit rig','Tracking & 3D','Use a Null as a stable camera pivot.','''
Create a comp with three 3D solids at different depths.
Create a 2-node camera and an appropriately positioned 3D Null.
Parent the camera to the Null and animate the Null’s Y rotation 0→30 degrees.
Adjust camera local Position so subject stays framed; verify target/Point of Interest behavior.
Render in the intended 3D renderer and compare to a Position-only camera move.
''','Subject remains readable while background layers show depth shift.','Incorrect pivot placement can make a camera orbit resemble uncontrolled zoom.')
recipe('noise-warp','14 · Heat haze with Displacement Map','Effects','Distort pixels using animated grayscale noise.','''
Make a comp-sized solid, apply Fractal Noise, choose a broad smooth scale and reduce contrast.
Animate Offset Turbulence slowly to make the map drift; precompose it as MAP_HEAT.
Apply Displacement Map to the target footage, point it to MAP_HEAT and adjust displacement strengths modestly.
Mask the effect region or use a matte so heat haze appears near a specific source.
Add small blur/color variation only where necessary; compare map on/off over time.
''','The background bends believably without an obvious repeating noise tile.','A color noise map may need channel selection to avoid chaotic displacement.')
recipe('depth-focus','15 · Depth-map-driven selective focus','Effects','Blur one region more than another.','''
Make a grayscale gradient with bright values in intended blurred regions.
Apply Camera Lens Blur to a duplicate of the footage and select the depth/blur map.
Tune Radius and map interpretation until background blur is stronger than the subject.
Feather the map and inspect the transition around the subject silhouette.
Compare to a global Gaussian Blur and evaluate render cost.
''','Subject retains detail while distant region falls out of focus gradually.','This uses a 2D blur map; for actual scene focus use the separate Advanced 3D camera DOF workflow.')
recipe('glow-outline','16 · Tracked glowing outline','Compositing','Build glow from a clean traced contour.','''
Create or track a mask path following the subject with as few stable vertices as possible.
Apply Generate → Stroke to a comp-sized solid and configure the path and width.
Precompose the stroke layer, duplicate it, blur one copy and add Glow to a duplicate.
Use a clean sharp core stroke above the soft bloom; tune opacities and blend modes.
Check motion frame by frame for outline detachment and edge aliasing.
''','One sharp line remains visible inside the blur, and outline follows subject motion.','A high blur on the only stroke layer produces a mushy and poorly defined outline.')
recipe('cloud-transition','17 · Procedural cloud transition','Effects','Combine noise, Levels and a matte reveal.','''
Create a solid with Fractal Noise and animate its Evolution/Offset Turbulence.
Use Levels to increase contrast so it evolves into a thresholded black/white matte.
Apply the resulting precomp as a Luma Matte to reveal the new scene over the old.
Animate Levels Input Black/White to turn a partial cloudy mask into full coverage.
Test consistency at full frame dimensions and inspect whether the mask reverses unintentionally.
''','Transition ends with completely visible second shot and no remaining first-shot pixels.','If both pictures vanish, the luma matte direction may be inverted.')
recipe('rgb-split','18 · Controlled RGB channel split','Effects','Make an aberration effect using channel routing.','''
Precompose a source with correct alpha, then duplicate it into three layers.
Apply Shift Channels so each copy isolates red, green or blue, and combine with Add where appropriate.
Offset red slightly left and blue slightly right, leaving green centered.
Use a mask/adjustment where the effect should occur, rather than displacing the whole frame continuously.
Check seams, alpha and color clipping at Full resolution.
''','Aberration appears near high-contrast edges without introducing a giant invisible background.','With alpha artwork, additive recomposition can unintentionally alter transparency.')
recipe('particles-burst','19 · Native particle burst','Effects','A measured CC Particle World experiment.','''
Apply CC Particle World to a suitable comp-sized solid.
Set Birth Rate to a low visible rate and key it to 0 after the first 12 frames.
Set Longevity to about 2 seconds; choose a particle style and initial velocity and gravity.
Adjust emitter position so particles emerge from the logo center.
Add gentle Glow after the particle effect and preview at actual playback speed.
''','No particles are born after the burst ends, but earlier particles die naturally.','Birth Rate 0 stops new particles; it does not kill those already alive.')
recipe('puppet-wave','20 · Puppet waving flag','Animation','A flexible loop from a static transparent flag.','''
Import a transparent flag shape and inspect its alpha edges.
Add Puppet pins at fixed pole edge and on two flowing sections of fabric.
Animate mid and tip pins across three poses over two seconds.
Use stiffness controls when necessary to avoid folding the pole itself.
Copy the first pose to the loop end and smooth all movements.
''','Flag waves smoothly and the pole edge stays visually stable.','Too many pins fight each other and create crumpling.')
recipe('content-fill','21 · Remove an object using Content-Aware Fill','Compositing','Generate a repair while retaining original footage.','''
Duplicate the clip and draw a mask around the unwanted object.
Animate/track mask and set its mode to create the intended transparent hole.
Open Window → Content-Aware Fill and choose suitable range and Fill Method.
Generate Fill Layer; inspect every frame and try a reference frame if textures are inconsistent.
Render and compare to source, particularly near moving occlusions and boundaries.
''','Object disappears without visible temporal pattern or seams.','Content-Aware Fill may give temporally unstable texture; a clean plate may work better.')
recipe('audio-cues','22 · Animate to beats with markers','Audio','Create rhythmic transitions without automatic beat-detection claims.','''
Import and listen to a clean WAV on Timeline; show waveform with LL.
Add comp markers manually at the actual beat transients.
Align keyframe entrances 2 frames before a beat or exactly on beat depending on intended impact.
Use F9 and Graph Editor to make 6-frame ease-out impacts and longer holds.
Export and listen to rendered sound, checking whether markers match perceptual onsets.
''','Every impact is perceptually synchronized in the exported movie.','Waveform peak amplitude is not always the perceived musical beat.')
recipe('json-score','23 · JSON-driven statistics title','Expressions & data','Load external numbers into Source Text.','''
Create a UTF-8 JSON file with a simple `{"team":"North","score":42}` object.
Import it into the project and create a Source Text expression using `footage('stats.json').sourceData.score` with a valid data path.
Convert the numerical result to a string, label it with a title and position it inside a shape card.
Use `sourceRectAtTime` to auto-size card background with 20 pixels of padding.
Change JSON to a longer team label and verify the design remains readable.
''','Values update after reloading external data and remain properly aligned.','Always check JSON syntax and exact field names.')
recipe('loop-remap','24 · Make a seamless time-remapped loop','Animation','Avoid a one-frame black or phantom-frame flash.','''
Import a visibly seamless 2-second clip into a 6-second comp.
Enable Time Remapping and inspect initial keyframes, especially end-duration key.
For a source with N frames and frame duration d, keep the initial key at (0,0). Add a key at ((N-1)*d,(N-1)*d) and make its outgoing interpolation Hold. At the cycle boundary N*d set Time Remap to 0, replacing the default beyond-source value.
Add `loopOut('cycle')` on Time Remap, extend the layer to six seconds and compare repeated cycles frame by frame. The loop duration stays N*d, including the final source frame’s interval.
Check final frame and audio timing; Time Remap does not guarantee an inherently nonseamless source becomes seamless.
''','No unexpected blank, duplicate or jump frame at loop boundaries.','A mathematical loop cannot conceal mismatched first/last source artwork.')
recipe('alpha-delivery','25 · Transparent master and color check','Color & delivery','Deliver usable compositing assets.','''
Make a 48-frame comp with a moving semi-transparent circle over an empty comp background.
Choose Render Queue Output Module format/codec supporting alpha; set RGB+Alpha and appropriate alpha interpretation.
Render a lossless/near-lossless master or numbered PNG sequence with intentional color settings.
Import the result into a fresh comp over dark blue and hot pink backgrounds; inspect edge transparency.
Render a separate H.264 review file with a solid background; label it as a non-alpha review.
''','The alpha master has transparent edges, and the MP4 review is correctly labeled.','An .mp4 file may look like an alpha preview in AE but will not preserve ordinary transparency.')
recipe('project-handoff','26 · Collect Files handoff test','Color & delivery','Prove that your project is portable.','''
Save the final project with descriptive version and output names.
Choose File → Dependencies → Collect Files and create a fresh folder that contains the project and required footage.
Add a README of fonts, third-party effects, scripts, LUTs and manual configuration notes.
Move the collected folder to a different Windows directory and reopen its project file.
Render a tiny proof frame; confirm it matches the pre-collection output and uses the new source paths.
''','Project reopens from collected directory and produces identical proof frames.','Collect Files does not install fonts or purchase plugin licenses.')
recipe('capstone','27 · Final 10-second integrated sequence','Capstone','Practice the entire production pipeline with one coherent composition.','''
Create a 24-fps 10-second comp and organized project folders; establish color and output format.
Make a two-second alpha-matte animated title with a readable hold.
Add a three-card stagger using controlled easing and a Null; build one reusable editable title element.
Place either a tracked element or roto/keyed person over a short plate; inspect edges in motion.
Add a procedural 2-second transition and final text, synchronize audio, then render MP4 and an appropriate master.
Collect Files, reopen the collected project and write a self-critique of three improvements.
''','Both render and portable project exist, with no one-frame flashes or missing media.','A capstone is not complete until the collected source can be reopened.')

recipe('guide-layout','00 · Responsive title layout','Animation','Keep proportional and fixed margins distinct.','''
Duplicate a title comp before modifying its dimensions.
Show rulers, then add a vertical 50% guide using View → Add Guide.
Add a vertical 100-pixel guide referenced from the right and a horizontal bottom margin.
Change the duplicate’s aspect ratio and inspect guide positions; reposition artwork deliberately.
Export/import .guides into the other comp and verify colors, units and edges rather than assuming a round trip.
''','Center and fixed-margin guides retain their intended meanings; text is still inside the delivery frame.','Guides are view-specific and do not animate or reposition layers.','Beginner','guides')
recipe('object-texture','00 · Texture inside an Object Matte subject','Compositing','Separate semantic selection from texture animation.','''
Open suitable moving footage in Layer panel and select the Object Matte toolbar tool.
Click the subject, refine the base selection and propagate the required span.
Correct occlusions and edge errors, then Freeze and inspect the silhouette over contrasting colors.
Add an animated texture on a separate layer and assign the isolated subject as its Alpha Matte.
Animate the texture independently and render a short sample, checking alpha and the whole moving edge.
''','Texture follows the subject silhouette with no one-frame holes or unrelated background.','Correct the source matte before trying to hide edge problems with Glow.','Intermediate','object-matte')
recipe('font-axis','00 · Editable variable-font emphasis','Text & data','Change letterform weight instead of scaling the whole layer.','''
Create a short headline in an installed variable font.
Choose Text → Animate → Variable Font Axes and an axis present in that font.
Keyframe the axis at time zero and at one second using supported values.
Use the Range Selector to send emphasis across characters or words.
Compare spacing modes and render the result at delivery size; record the font dependency.
''','Text remains editable and readable without unexpected spacing or wrapping.','A static font family does not expose variable axes.','Intermediate','variable-fonts')
recipe('curl-matte','00 · Flowing Curl Noise reveal','Effects','Use a procedural field as a controllable matte.','''
Create a comp-sized solid and apply Curl Noise with Quick Apply.
Begin with Internal input and adjust Scale/Swirl while keeping color simple.
Animate one motion control, inspecting Input Noise versus Final Render.
Precompose the generated field and assign it as a Luma Matte to an incoming image.
Animate a contrast/brightness transition to finish at complete coverage, then inspect start/end frames and the rendered cut.
''','The incoming image ends fully visible with no residual old frame.','A partially bright noise field alone will not reach opaque full coverage.','Intermediate','noise')
recipe('unmult-master','00 · Black-backed element to RGBA master','Compositing','Deliver alpha instead of relying on a background-specific blend.','''
Import a suitable light/smoke element with a black background and retain a source copy.
Apply Unmult, choose Black and inspect Alpha with Alt+4.
Adjust Black Level and Softness, then inspect Remove Color Matting around translucent edges.
Test over dark gray, white and saturated backgrounds; protect foreground black where needed.
Export RGB+Alpha to a suitable format and reimport over a contrasting solid to verify color and coverage.
''','Rendered alpha works over more than one background without opaque black borders.','Screen mode alone does not establish a reusable alpha master.','Intermediate','keying-effects')
recipe('mesh-rack-focus','00 · Native mesh rack focus','Tracking & 3D','Render a stable 26.5 geometry and focus study.','''
Create a comp with Advanced 3D and add two native meshes at different depths.
Set distinct roughness/metallic values and light them with a controlled environment or supported light.
Create a camera and enable Camera Options → Depth of Field.
Set focus to the near object, then animate Focus Distance to the far object over two seconds.
Render in Active Camera at Full quality and inspect near/far edges and the focus transition.
''','Focus travels between real scene objects with a predictable first/middle/final frame.','A custom viewer is not the final Active Camera; do not confuse Camera Lens Blur with this scene render.','Advanced','meshes advanced-dof')
recipe('ocio-proof','00 · ACES 2.0 input-to-output proof','Color & delivery','Make every color transform explicit.','''
Duplicate a small test project and choose Project Settings → Color → OCIO color managed.
Choose the pipeline-appropriate ACES 2.0 CG v4.0 or Studio v4.0 configuration.
Interpret a known source correctly and choose a suitable scene-linear working space such as ACEScg.
Set a display transform for inspection and an independent Output Module output color space for delivery.
Render a short image sequence, reimport with the correct interpretation and compare to the reference without double-applying a display transform.
''','Source, working, display and output transforms are recorded and the reference comparison is consistent.','Do not change an established project’s configuration in place without a known-good reference.','Advanced','ocio')

ADDITIONAL_GLOSSARY = '''
Quick Apply :: Ctrl+Enter launcher for effects, animation presets and menu commands; stable since 26.2.
Object Matte :: Object-selection and propagation workflow with disk caching in 26.5; distinct from ordinary vector masks.
Proportional Scrubbing :: Ctrl+Alt-drag property hot text to distribute a numerical change in selection order; distinct from timing offsets.
Parametric mesh :: Native 3D geometry controlled by editable parameters in Advanced 3D.
SBSAR :: Substance material file with exposed procedural controls; keep it with project dependencies.
Variable font axis :: Continuous font-specific variation such as Weight or Width, animatable through text animators.
Unmult :: Keying effect converting a suitable black/white backing into alpha with level and edge controls.
Curl Noise :: Procedural 2D flowing texture effect introduced in 26.3.
Guide pinning :: A guide’s reference edge for responsive placement; different from locking against edits.
ACES 2.0 :: Color pipeline supported natively in 26.5 through OCIO 2.5.1 and bundled CG/Studio v4.0 configurations.

AEP :: Native After Effects project file storing editable compositions and source references rather than embedding every source file.
Footage item :: Media reference inside the Project panel; one item can appear in multiple compositions.
Footage panel :: Viewer for opening an imported file's source frames, distinct from a composition view.
Layer panel :: Viewer for a single layer's source/paint/roto context.
Composition :: Canvas and frame-based timeline that combines several layers into a rendered result.
Comp background color :: Composition viewer's background preference; not automatically opaque pixels in output.
Work area :: Timeline start/end region used for previews and certain renders, separate from comp duration.
Shy layer :: A layer marked for hidden display in the Timeline when the master Shy switch is active; not necessarily absent from rendering.
Solo :: Layer switch that temporarily isolates one or more layers for viewing/rendering in the working context.
Guide layer :: Layer used for design reference and normally omitted from parent-comp final render, depending on context.
Null object :: Invisible transform controller layer commonly used for parenting and expression controls.
Adjustment layer :: Special layer through which effects process underlying composited pixels.
Solid :: Layer generated as a constant-color rectangular source, often used as a carrier for effects.
Precomposition :: A composition nested in another composition, with separate properties and timing.
Precompose :: Command to move selected layers into a new child composition.
Collapse Transformations :: Nested-comp switch that alters how inner transforms and some rendering steps combine with the outer composition.
Continuous Rasterization :: Related switch that causes eligible vector art to be rasterized at an appropriate scale, retaining sharper edges.
Shape group :: Container in Shape Layer Contents with paths, styles, modifiers and its own Transform properties.
Parametric shape :: Geometry described by parameters such as size and roundness rather than custom vertex locations.
Bezier path :: Geometry or motion curve controlled by points and tangent handles.
Trim Paths :: Shape Contents operator that shows only a Start-to-End portion of an eligible path.
Repeater :: Shape Contents operator that creates repeated copies using instance transforms.
Offset Paths :: Shape modifier that expands/contracts an outline according to its parameters.
Mask :: Alpha boundary applied to a layer, with mode, path, feather, expansion and opacity.
Garbage matte :: Coarse mask removing obviously unwanted image regions before precise keying or roto.
Track matte :: Layer-based source of alpha/luma transparency for a target layer.
Alpha Matte :: Matte type that derives target coverage from source alpha.
Luma Matte :: Matte type that derives target coverage from matte image brightness.
Alpha Inverted Matte :: Matte type that inverts alpha-derived transparency.
Luma Inverted Matte :: Matte type that inverts luminance-derived transparency.
Straight alpha :: RGBA representation in which RGB is not preblended against a matte color.
Premultiplied alpha :: Representation in which color channels have been mathematically mixed with transparency and possibly a matte color.
Despill :: Remove green/blue color contamination from a keyed object's edges.
Choker :: Matte processing effect that contracts/expands or cleans alpha edges.
Roto Brush :: Brush-assisted tool for propagating a foreground segmentation through video frames.
Refine Edge :: Rotoscoping refinement tool for wispy/semipermeable boundaries like hair.
Freeze Roto :: Operation that freezes Roto Brush propagation for a selected span; not equivalent to exporting permanent alpha footage.
Point tracking :: Tracking translation or additional simple motion from one/two visual features.
Feature region :: Tracking patch containing the visual detail being matched across frames.
Search region :: Tracking area within which a tracked feature is searched for in the next frame.
Attach point :: The point to which calculated motion data is applied.
Planar tracking :: Solving the motion of a flat or approximately flat textured surface.
Corner Pin :: Perspective effect mapping image corners to specified tracked points.
Warp Stabilizer :: Stabilization effect using motion analysis and compensating transforms/warping.
Camera solve :: Estimated 3D camera motion reconstructed from analyzed footage.
2.5D :: Flat image layers positioned/oriented in a 3D coordinate space.
Z depth :: Distance along the third spatial axis, controlling parallax and depth relationships.
Point of Interest :: Target point used by some camera/light layer orientation controls.
Camera Zoom :: AE camera projection parameter affecting framing/field of view.
Environment light :: Illumination sampled from an image or environment in a supported 3D renderer.
Shadow catcher :: 3D surface/feature used to receive shadows for image integration.
Advanced 3D :: After Effects renderer for supported imported 3D models and relevant material/lighting features.
Renderer :: Processing engine defining 3D interpretation, capabilities and available quality options.
MFR :: Multi-Frame Rendering: calculating multiple frames concurrently when resources and effect support permit.
RAM cache :: Cached rendered frames stored in memory for reuse during compatible previews.
Disk cache :: Persisted reusable frame data stored on a disk; distinct from source assets and final renders.
Proxy :: Substituted lighter/alternative footage used to speed editing or manage media workflows.
ROI :: Region of Interest, a restricted viewer-rendering area for inspecting part of a composition.
Composition Profiler :: Diagnostic display to help identify computationally expensive layers or effects.
Effects & Presets :: Searchable After Effects panel listing installed effects and animation presets.
Effect Controls :: Panel for one or more applied effect instances and their properties.
Effect Manager :: Interface for managing effect availability/enablement in supported builds.
Keyframe :: Stored property value (and interpolation/tangent information) at a specified time.
Linear interpolation :: In-between values change at a uniform numerical rate between keys.
Hold interpolation :: Value stays at a key's level until next key, then jumps.
Temporal Bezier :: Value-easing curve controlled by time-related tangent handles.
Spatial Bezier :: Curved trajectory path for Position, separate from timing/easing.
Easy Ease :: Keyframe assistant that creates a smooth transition into/out of a keyframe.
Roving keyframe :: Spatial keyframe allowed to vary its time automatically while following the motion path.
Value Graph :: Graph Editor view of property value over time.
Speed Graph :: Graph Editor view of the rate at which a property changes over time.
Motion path :: Visible spatial trajectory of a Position animation.
Time Remapping :: Keyframable mapping from composition time to source time.
Time Stretch :: Source playback-duration adjustment of a layer.
Frame blending :: Method of blending/interpolating frames when source timing differs from the output frame grid.
Pixel Motion :: Optical-flow-based frame interpolation; may warp around occlusions.
Shutter angle :: Motion-blur exposure proportion relative to frame interval.
Shutter phase :: Temporal offset for the motion blur sampling window.
Source Text :: Editable text content property of a text layer.
Point text :: Text object that grows naturally from a clicked insertion point.
Paragraph text :: Text object that flows/wraps inside a specified bounding box.
Leading :: Vertical distance between baselines of neighboring text lines.
Kerning :: Spacing between a selected pair of characters.
Tracking :: General letterspacing across a selected run of text.
Range Selector :: Text Animator selector that applies animated properties to a chosen portion of text.
Wiggly Selector :: Text Animator selector that varies which characters receive animated properties.
Expression Selector :: Text Animator selector driven by a custom expression.
Expression :: JavaScript-like formula that calculates a property value at evaluation time.
Expression Controls :: Slider, Angle, Color, Point and related controls designed for linking rigs.
ExtendScript :: Adobe scripting dialect used in JSX automation of application/project structure.
JSX :: Common file extension for an After Effects ExtendScript script.
sourceRectAtTime :: Expression method returning a layer's visible rectangle metrics used for dynamic layout.
thisComp :: Expression reference to the current composition.
thisLayer :: Expression reference to the current evaluated layer.
loopOut :: Expression function continuing a keyed pattern after its last keyframe.
valueAtTime :: Expression function sampling a property's value at a requested time.
wiggle :: Expression function producing time-varying pseudorandom variation in a property.
OCIO :: OpenColorIO color pipeline system used for managing color transforms.
ACES :: Academy Color Encoding System: a standardized scene-referred film/VFX color workflow.
Working color space :: Common space in which images are processed and composited.
Display transform :: Conversion from a working scene/image to a viewing device's intended display rendering.
Output transform :: Color conversion applied when creating a final intended delivery file.
Input profile :: Definition used to interpret source color values correctly.
Linear light :: Signal encoding in which a numerical pixel value corresponds approximately linearly to light intensity.
CICP :: Codec/container color-encoding metadata describing characteristics such as primaries and transfer functions.
LUT :: Lookup table used for a color conversion or artistic look; its meaning depends on source/target spaces.
EXR :: OpenEXR image format often used with floating-point channels and VFX passes.
Mezzanine :: High-quality intermediate media designed for additional editing/compositing.
H.264 :: Widely used distribution codec, typically used in MP4 without a normal alpha channel.
ProRes 4444 :: A ProRes codec variant that can carry an alpha channel in compatible workflows.
Output Module :: Render Queue configuration of format, channels, color, audio and destination options.
Motion Graphics Template :: A .mogrt package exposing user-facing controls for reusable motion assets.
Essential Graphics :: AE interface used to expose properties for templates and nested instance editing.
Essential Properties :: Nested comp instance controls/overrides for exposed source properties.
Protected Region :: Time section in a reusable motion template marked to retain its intended timing on stretch.
Collect Files :: Project dependency action that copies linked assets into a transportable collected project folder.
Missing Footage :: Project warning that an imported source reference cannot currently be resolved on disk.
Quick Offset :: Ctrl+Alt-drag selected layer bars or keyframes to stagger timings; added by After Effects 25.4.
Single 3D gizmo :: AE 25.6 multi-selection transformation control for several 3D layers.
Tip of the Day :: AE 25.6 guidance shown in certain empty/reloaded viewer contexts.
'''

ADDITIONAL_TROUBLE = [
 ('After Effects will not launch on Windows','Check installed version, supported CPU/AVX2, required GPU API, permissions and plugin crashes.','Check the current 26.5 system requirements, driver and architecture; isolate third-party startup effects with supported diagnostics.'),
 ('Older OpenCL 1.2 GPU fails','Verify 26.5 hardware requirements and installed GPU driver/OpenCL capabilities.','Use a supported GPU with the required API, not a workaround that disables GPU capability checks.'),
 ('Cannot find Quick Apply', 'Check 26.5 stable, text/modal focus and a remapped shortcut.', 'Use Edit → Quick Apply or its Timeline icon; Ctrl+Enter opens it. Check installed Keyboard Shortcuts.'),
 ('Cannot find Object Matte tool', 'Confirm 26.5 and open the footage layer in Layer panel.', 'Choose Object Matte from the toolbar. Adobe lists Ctrl+W, which conflicts with Close; verify locally rather than assuming a focus rule.'),
 ('Cannot find native SVG shape import', 'Check import mode and whether you are importing a file or pasting clipboard SVG.', 'File → Import → File can import SVG as a composition or footage; Illustrator paste requires Include SVG Code.'),
 ('Cannot find new Unmult or Curl Noise', 'Search e:unmult or e:curl noise in Quick Apply and inspect Effect → Manage Effects.', 'Confirm 26.5 stable and enabled native effects. Unmult handles black/white alpha; Curl Noise generates flowing texture.'),
 ('Cannot find Audio Compressor/Gate/Distortion', 'Verify the selected audio layer and search the Audio effects category.', 'These effects are stable in 26.5. Test the processed rendered sound with an audio-enabled Output Module.'),
 ('No new percentage-based guide controls', 'Confirm 26.5 and the active viewer; a guide is distinct from a grid line.', 'Right-click a guide → Edit Guide to set percent/pixel units, reference edge and color.'),
 ('Cannot generate ACES 2.0 default configuration', 'Check Project Settings → Color → OCIO color managed and the installed version.', 'Choose ACES 2.0 CG v4.0 or Studio v4.0; specify input, working, display and output transforms.'),
 ('Text editor shortcuts change layer behavior','Text cursor has focus, so Ctrl+Shift+K or letter keys act on text.','Exit text editing with a valid method, select Timeline panel, and try again.'),
 ('Shape Layer created but nothing is visible','Empty Contents group, missing Fill/Stroke, hidden layer or path size 0.','Draw a path, enable Fill/Stroke, inspect Contents and layer visibility.'),
 ('New rectangle is a mask instead of a shape','A valid existing image/solid layer was selected or toolbar mode is Tool Creates Mask.','Deselect layers or change toolbar mask/shape mode intentionally.'),
 ('Rotating layer moves it in a strange circle','Anchor is far from intended rotation pivot.','Inspect A and P; use Y Pan Behind to move anchor while preserving apparent position.'),
 ('Child jumps when parenting','Parent and child coordinate spaces or existing keyframes differ.','Inspect parent transforms and resulting local coordinates; undo and establish a clean rig hierarchy.'),
 ('Imported image looks too small or too large','Footage and comp dimensions differ; non-square pixels or layer Scale may be involved.','Inspect footage pixels, comp pixels, pixel aspect ratio and fit-to-comp commands.'),
 ('Pixel aspect looks squeezed','Non-square pixel interpretation or comp setting mismatch.','Correct Interpret Footage and composition pixel aspect ratio; verify intended final output.'),
 ('Image sequence imports as one still','Sequence option not enabled or numbering not continuous.','Select the first frame and enable appropriate image-sequence import options.'),
 ('Layer plays backward unexpectedly','Time-Reverse Layer or descending Time Remap curve.','Inspect Time Remap and selected layer time operations, then restore correct source order.'),
 ('Loop has one blank or extra frame','Default last Time Remap key points to source duration after last visible frame.','Keep a full source-duration cycle: add a last-valid-frame key, hold it through the final interval, and set the cycle boundary key to source time zero. Inspect every seam.'),
 ('Motion path appears curved but motion is uneven','Spatial path curvature and temporal easing are separate.','Review path geometry and Graph Editor speed; do not equate key spacing with constant travel.'),
 ('Stroke / Trim Paths not visible','Confusing effect Stroke with shape Trim Paths or a hidden Fill/Stroke.','Inspect the intended mask or shape path, stroke width, Trim Paths Start/End and operator location.'),
 ('Replaced source ruined apparent scale','New source dimensions differ while layer scale values were preserved.','Use replacement source at expected dimensions or deliberately adjust Scale/anchor.'),
 ('Audio Amplitude expression red error','Wrong layer/effect name or scalar returned to vector property.','Pick whip to actual Slider; return [s,s] for 2D Scale.'),
 ('Source text background does not fit','sourceRectAtTime width/height used without left/top offsets or coordinate conversion.','Use both dimensions and positional offsets in the same coordinate context.'),
 ('FX renders differently with Collapse Transformations','Nested transform/render order was changed.','Disable switch temporarily and compare effects, layer masks and 3D interactions.'),
 ('Glow looks washed out','Glow is applied to too much bright imagery or effect stack has wrong order.','Isolate highlights, adjust Threshold/Radius/Intensity, and compare precomp/stack order.'),
 ('Screen replacement slips on camera movement','Tracker plane drift or incorrect Corner Pin surface.','Review original checkerboard on every frame, recalibrate plane and retrack if necessary.'),
 ('Roto freezes halfway','Propagation range incomplete or erroneous Freeze state.','Review corrected base frame and full span, and unfreeze/refreeze safely as required.'),
 ('Content-Aware Fill looks like repeated blotches','Missing clean reference or fill algorithm cannot reconstruct motion/texture.','Use a reference frame/clean plate, smaller mask, or alternative tracked patch.'),
 ('Output looks washed out','Unintended color transform, output profile or double-applied LUT.','Audit source, working, display and output transforms and inspect metadata.'),
 ('Export audio is absent','Audio layer muted or Render Queue/Output Module audio setting disabled.','Confirm layer Audio switch, export setting and resulting media audio track.'),
 ('Export image sequence has missing frames','Render interruption, nonmatching numbering or wrong range.','Check continuous frame count, output directory and any render failures before assembling.'),
 ('RGBA preview shows black in media player','Media player may ignore alpha even when alpha exists.','Import rendered result in AE or another alpha-aware consumer over a colored solid.'),
 ('RAM cache fills instantly','High-res/32-bpc source, big comp and insufficient RAM.','Limit preview range/resolution, manage memory settings and use proxies/pre-renders.'),
 ('Disk cache full','Cache drive low on space, quota small or large prior assets.','Move cache to a fast drive with room or purge deliberately while AE is idle.'),
 ('Collect Files reopens with missing fonts','Font software is not bundled by Collect Files.','Install licensed fonts on target and record exact family/version in README.'),
 ('One plugin works only on other PC','Plugin binary, GPU, licensing or CPU/OS differs.','Check Windows-compatible plugin version and authorized installation; pre-render a fallback when necessary.'),
 ('Frame preview stops updating','Caps Lock, wrong viewer, cached frame issue or no valid current layer.','Turn Caps Lock off, select correct comp and time, then test on a single plain solid.'),
 ('Custom keyboard preset conflicts','A Windows/app shortcut may intercept it or focus in another panel.','Check Edit → Keyboard Shortcuts, reset/rename mapping and test within intended panel.'),
 ('MOGRT name edit changes all copies','Shared child source edited instead of instance Essential Property.','Expose text properly and use instance overrides on each nested copy.'),
 ('Layer shadows do not appear','Unsupported renderer, 2D layer, Material Options or light settings.','Enable 3D/material options and use an appropriate light/renderer combination.'),
 ('Final master not reproducible','Uncollected source, LUT, font, plugin or unrecorded settings.','Collect Files, document dependencies and rerender a test from the transferred package.')
]


# Recipes become available as optional practice once their prerequisite concept has been learned.
RECIPE_AFTER={'guide-layout':'modern-operations','object-texture':'object-selection','font-axis':'modern-type','curl-matte':'flow-alpha','unmult-master':'flow-alpha','mesh-rack-focus':'mesh-focus','ocio-proof':'color','logo-reveal': 'mattes', 'text-window': 'text', 'lower-third': 'templates', 'track-title': 'tracking', 'corner-pin': '3dtrack', 'green-key': 'keying', 'roto-cutout': 'roto', 'handwriting': 'masks', 'stroke-icons': 'paths', 'stagger': 'timefx', 'logo-pulse': 'audio', 'depth-dolly': 'camera', 'camera-dolly': 'camera', 'noise-warp': 'blur', 'depth-focus': 'blur', 'glow-outline': 'tracking', 'cloud-transition': 'blur', 'rgb-split': 'color', 'particles-burst': 'particles', 'puppet-wave': 'puppet', 'content-fill': 'paint', 'audio-cues': 'audio', 'json-score': 'data', 'loop-remap': 'timefx', 'alpha-delivery': 'render', 'project-handoff': 'collect', 'capstone': 'capstone'}
for r in RECIPES:
 r['afterLesson']=next(i for i,c in enumerate(CHAPTERS,1) if c['id']==RECIPE_AFTER[r['id']])
 r['level']=('Beginner' if CHAPTERS[r['afterLesson']-1]['phase'] in ('START','FOUNDATIONS') else 'Intermediate' if CHAPTERS[r['afterLesson']-1]['phase']=='INTERMEDIATE' else 'Advanced')
RECIPES.sort(key=lambda r:(r['afterLesson'],r['id']))
for i,r in enumerate(RECIPES,1):
 r['title']=f"{i:02d} · "+r['title'].split(' · ',1)[1]

QUIZ = [
 ('Which file is the editable After Effects project?',['.mp4','.aep','.png','.wav'],1,'The .aep stores compositions and references to other assets.'),
 ('Which launcher searches effects, presets and menu commands in 26.5?',['Quick Offset','Effects & Presets','Quick Apply','Precompose'],2,'Ctrl+Enter opens Quick Apply; e:, p: and m: narrow its result types.'),
 ('What does the layer Anchor Point define?',['Delivery frame rate','Local transform pivot','Source duration','Color space'],1,'Anchor is the pivot in layer coordinates.'),
 ('What does pressing U show on a selected animated layer?',['Only used keyframed properties','Audio levels','Undo history','All matte sources'],0,'U reveals animation-keyed properties.'),
 ('Which shortcut trims selected layer IN at playhead?',['[','Alt+[','Shift+[','Ctrl+['],1,'Alt+[ trims; [ shifts the layer.'),
 ('At 24 fps, how many frames are in 2 seconds?',['24','36','48','60'],2,'Frames = seconds × FPS.'),
 ('Which setting defines a composition frame grid?',['Preview zoom','Project folder','Composition frame rate','Layer blend mode'],2,'The comp FPS determines output sample times.'),
 ('What does a Hold keyframe do?',['Changes alpha mode','Maintains value until next key','Adds blur','Scales the footage'],1,'Hold interpolation jumps rather than smoothly interpolates.'),
 ('Which graph shows the numerical rate of change?',['Value Graph','Speed Graph','Waveform','Histogram'],1,'Speed Graph is rate per unit time.'),
 ('How do you animate a shape outline drawing on?',['Trim Paths','Gaussian Blur','Time Remap','Set Matte'],0,'Trim Paths is a Shape Contents operator.'),
 ('Which is a parametric shape property?',['Rectangle Path Roundness','Mask Track Matte','Output Module','Footage Proxy'],0,'Rectangle Path preserves editable size and roundness.'),
 ('What controls alpha coverage from another layer?',['Track Matte','Timeline Marker','Keyframe Assistant','Viewer Resolution'],0,'A matte source drives visibility of its target.'),
 ('How does a Luma Matte differ from Alpha Matte?',['It adds motion blur','It uses brightness','It changes FPS','It is always inverted'],1,'Luma uses brightness; alpha uses transparency.'),
 ('Which view is most helpful for matte quality?',['Alpha channel','Only RGB full color','File Info','Effects & Presets'],0,'Inspect alpha as a grayscale channel.'),
 ('What happens if you click an active stopwatch?',['Makes one extra key','Opens preferences','Removes property keyframes','Adds a null'],2,'It removes all property animation and keeps a current value.'),
 ('What is a purpose of a Null?',['Encoding video','Parenting controller','Converting RGB','Importing audio'],1,'Nulls are invisible transform/control layers.'),
 ('Which operation changes nested render order?',['Precompose','Rename','Timeline zoom','Info panel'],0,'Precompose can move effect/transform stages to another context.'),
 ('What is an Adjustment Layer?',['A global file proxy','An effect processor for composited pixels below','An audio file','An export-only effect'],1,'It applies effects to underlying composited layers within context.'),
 ('Which tool offers object-based subject selection in 26.5?',['Roto Brush','Mocha AE','Object Matte','Keylight'],2,'Object Matte debuted in 26.2.'),
 ('Why track a checkerboard before final screen replacement?',['Better font loading','Easier to spot corner drift','Automatic audio sync','Uses less storage'],1,'Distinct grid corners expose perspective tracking errors.'),
 ('Which tool is best suited to a planar moving sign?',['Mocha AE planar tracker','Only Gaussian Blur','Levels','Audio Spectrum'],0,'Mocha tracks planar surfaces for corner-pin results.'),
 ('What does Roto Brush Freeze do?',['Renders final MP4','Locks propagated segmentation for range','Changes footage FPS','Converts masks to shape'],1,'Freeze caches propagation, not final media delivery.'),
 ('What does 32-bpc float provide?',['More source detail than recorded','Larger color/math headroom','Automatic 10-bit codec','Faster all effects'],1,'Floating-point working precision can preserve extended values; it cannot recover clipped source.'),
 ('Which came to AE with version 25.6?',['Curl Noise','Single 3D gizmo','Object Matte','Variable-font axis animation'],1,'Single 3D gizmo across selected 3D layers is 25.6.'),
 ('Which is a 26.5-only upgrade?',['Native ACES 2.0 bundled support','OCIO color engine existence','8-bpc projects','RGB channels'],0,'Bundled OCIO 2.5.1/ACES 2.0 support was introduced in 26.5.'),
 ('Which type can carry normal AE RGBA alpha more reliably?',['Standard H.264 MP4','ProRes 4444 or suitable PNG sequence','MP3','WAV'],1,'Use a codec/format and output module that actually supports RGB+Alpha.'),
 ('What is the difference between Output Module and Render Settings?',['They are identical','Codec/channels vs render quality/time options','Timeline only vs Project only','Neither affects export'],1,'Output Module handles file options; Render Settings govern rendering.'),
 ('Why use sourceRectAtTime for text cards?',['It tracks a camera','It measures changing text bounds','It creates sound','It exports JPEG'],1,'Text bounds support auto-sized backgrounds.'),
 ('What does `loopOut("cycle")` normally repeat?',['Entire project','A suitable animated property keyframe cycle','All audio','Imported fonts'],1,'loopOut is property-oriented and depends on meaningful keyed animation.'),
 ('What is the safer debugging first step for a slow comp?',['Purge every cache repeatedly','Measure a short cold/warm preview and isolate effects','Reinstall Windows','Turn off all render quality forever'],1,'Measure actual bottlenecks before deleting caches or replacing hardware.'),
 ('What does Collect Files not promise to include?',['Referenced source footage','A copy of the project','Third-party plug-in licenses and fonts','Project folders'],2,'Fonts and plugins require separate handoff checks.'),
 ('How can you verify a render is correct?',['Only see green Render Queue status','Open output separately and check frames/audio/alpha','Assume preset is correct','Count layer names'],1,'Independent playback/reimport verifies the deliverable.'),
 ('How do expressions differ from scripts?',['Expressions drive individual property values, scripts edit projects','Both work only in HTML','Expressions install plugins','Scripts cannot see layer names'],0,'Expressions are time-evaluated formulas; scripts automate the application.'),
 ('Which frame is frame :23 at 24 fps?',['Last frame in that numbered second','First frame in next second','Two seconds','Impossible at 24 fps'],0,'Frames inside a second range from :00 through :23.'),
 ('How many 25-fps frames correspond to 4 seconds?',['24','96','100','125'],2,'25×4=100 frames.'),
]

topic('source-time','Footage source time vs comp time','Foundations','Which source frame appears depends on interpretation, layer start, time stretch and remapping.', '''
Comp clock::The timeline CTI measures time in the active composition. A source clip's first visible frame may be offset if the layer has an adjusted start time, In/Out or stretch.
Remapped clock::Time Remap keys specify the source timestamp to sample at a comp time. A reverse or freeze segment changes footage source sampling without moving the layer bar.
Nested clocks::A precomp layer samples an inner composition time; frame rates may differ, and fractional times can be involved. Always compare displayed source and comp frame counts.
''','Make a clip show its original second 3 at comp second 1 without modifying the original media.','Source time must not be confused with keyframe timing.','time-remap timeline','help')

topic('frame-rate','Frame-rate conversion and temporal sampling','Foundations','Source FPS, composition FPS and output FPS are separate choices.', '''
Source interpretation::Interpret Footage defines assumed source rate for certain media. Changing this is not the same as placing a 30-fps clip in a 24-fps comp.
Sampling::Compositions evaluate frames at their own FPS and may repeat/drop/blend sources if frame rates differ. Frame blending and pixel motion can interpolate but may create artifacts.
Delivery::Choose an output frame rate intentionally and verify final frame count, audio sync and timecode before handoff.
''','Put a 30-fps clip into a 24-fps comp and compare frame blending off vs on during a fast pan.','Frame rate changes can make keyframe rhythms appear different at playback.','frames time-remap','help')

topic('compositing','Layer-based compositing and image order','Compositing','Layers, alpha, mattes, blending and effects work together to produce pixels.', '''
Stack model::In ordinary 2D, higher layers cover lower layers depending on their opacity, alpha and blending mode. An adjustment layer uses composited lower pixels as its image input.
Opacity pipeline::Source alpha, masks, effects and track matte controls can combine to set final coverage. Inspect RGB and alpha separately to find errors.
Organizing passes::For demanding shots, work on source cleanup, segmentation/keying, track integration, grade, then finishing grain/sharpness. Nest only when it clarifies render order.
''','Build three overlapping colored shapes and explain precisely which pixels contribute at the center.','Blending two layers visually is not necessarily equivalent to creating alpha for downstream use.','alpha blending render-order','help')
