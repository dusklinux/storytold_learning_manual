"""Research-grounded second pass: pedagogic improvements and Premiere 26.x category migration.
Only use explicitly documented Adobe category names. Later-installed-seat verification is a separate gate.
"""
from collections import Counter

ADOBE_KEYS='https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html'
ADOBE_EFF='https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html'
ADOBE_MOD='https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/effects.html'
ADOBE_AUDIO='https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/audio-effects-library.html'

CURRENT_VIDEO='''Extract|Levels|Lighting Effects|ProcAmp|Bokeh Blur|Compound Blur|Directional Blur|Focus Blur|Gaussian Blur|Reduce Interlace Flicker|Sharpen|Unsharp Mask|ASC CDL|Brightness & Contrast|Lumetri Color|Tint|Video Limiter|Vignette|Corner Pin|Lens Distortion|Mirror|Spherize|Turbulent Displace|Twirl|Warp Stabilizer|Wave Warp|4-Color Gradient|Black & White|Channel Mix|Color Pass|Color Replace|Gamma Correction|Invert|Rounded Crop|VR Blur|VR Chromatic Aberrations|VR Color Gradients|VR De-Noise|VR Digital Glitch|VR Fractal Noise|VR Glow|VR Plane to Sphere|VR Projection|VR Rotate Sphere|VR Sharpen|Alpha Adjust|Color Key|Logo Cutout|Luma Key|Track Matte Key|Ultra Key|Echo Glow|Edge Glow|Glint|Light Leaks|RGB Split|Volumetric Rays|Wonder Glow|Noise|Basic 3D|Drop Shadow|Long Shadow|Brush Strokes|Color Emboss|Find Edges|Mosaic|Posterize|Roughen Edges|Strobe Light|Posterize Time|3D Rotate|Auto Reframe|Camera Shake|Grow|Horizontal Flip|Move|Offset|Shrink|Spacer|Spin|Transform|Vertical Flip|Wiggle|Gradient Wipe|Auto Align|Cineon Converter|Clone|Metadata & Timecode Burn-in|Simple Text|Stroke'''.split('|')
LEGACY_VIDEO='Camera Blur|Crop|Edge Feather|Magnify|Ramp|Replicate|Alpha Glow|Block Dissolve'.split('|')
OBSOLETE_VIDEO='Color Balance|Lightning|Rolling Shutter Repair|Echo|SDR Conform'.split('|')
REMOVED_VIDEO='Arithmetic|Auto Color|Auto Contrast|Auto Levels|Bevel Alpha|Bevel Edges|Blend|Calculations|Camera View|Cell Pattern|Change Color|Change-to-Color|Channel Mixer|Checkerboard|Circle|Clip Name|Compound Arithmetic|Convolution Kernel|Difference Matte|Dust & Scratches|Ellipse|Emboss|Equalize|Eyedropper Fill|Fast Blur|Fast Color Corrector|Ghosting|Grid|Horizontal Hold|Image Matte Key|Leave Color|Luma Corrector|Luma Curves|Median (Legacy)|Noise Alpha|Noise HLS|Noise HLS Auto|Non Red Key|Paint Bucket|Radial Shadow|Reduce Interlace Flicker|Remove Matte|RGB Color Corrector|RGB Curves|Set Matte|Shadow/Highlight|Solarize|Solid Composite|Texturize|Threshold|Three-Way Color Corrector|Timecode|Venetian Blinds|Vertical Hold|Video Limiter (Legacy)|Write-On'.split('|')
# 26.2 and 26.5 added replacements for historic/removed effects: do NOT confuse exact older plug-in identifier with the modern replacement.
NEW_VIDEO='Channel Blur|Gradient|Lens Flare|Magnify|Noise|Twirl|Mosaic|3D Spinback'.split('|')
VIDEO_RENAMES={'Lens Flare':'New modern 26.5 Lens Flare effect; the older Lens Flare plug-in was classified obsolete in 26.0.',
  'Channel Blur':'Modern 26.2 effect; the old Channel Blur plug-in was removed in 26.0.',
  'Noise':'Modern 26.2 effect; the older Noise plug-in was removed in 26.0.',
  'Magnify':'New modern 26.3 replacement; the former Magnify lives in Legacy.',
  'Twirl':'Redesigned 26.5 effect; older Twirl is under Legacy.',
  'Mosaic':'26.5 modern mosaic with Softness controls; a prior Mosaic is in Legacy.',
  'Gradient':'Modern 26.2 effect, not the older Ramp.',
  'Crop':'Legacy category; use modern Rounded Crop when appropriate; geometry and alpha behavior are not identical.',
  'Ramp':'Legacy category; Gradient is the modern replacement.',
  'Gaussian Blur':'Modern effect; separate Gaussian Blur (Legacy) remains for compatibility.',
  'Directional Blur':'Modern effect; separate Directional Blur (Legacy) remains.',
  'Lens Distortion':'The 26.0 active Distort list contains Lens Distortion; a former plug-in with the same name appears in the removed list. Check exact modern/legacy identity.'}
# Never claim a transition is present just because a similarly named effect exists.
TRANSITION_GROUPS={
'Animation':'Block Motion|Flip Motion|Fold Motion|Pop Motion|Pull Motion|Spin Motion|Spring Motion|Travel Motion',
'Dissolve':'Additive Dissolve|Blur Dissolve|Burn Alpha|Cross Dissolve|Dip to Black|Dip to Color|Dip to White|Film Dissolve|Luma Fade|Morph Cut|Mosaic',
'Grunge & Distort':'Chaos|Earthquake|Flicker|Glass|Glitch|Grunge|Kaleidoscope|Liquid Distortion|TV Power|VHS Damage',
'Immersive Video':'VR Chroma Leaks|VR Gradient Wipe|VR Iris Wipe|VR Light Leaks|VR Light Rays|VR Mobius Zoom|VR Random Blocks|VR Spherical Blur',
'Lights & Blurs':'Burn Chroma|Chroma Leak|Cross Zoom|Directional Blur|Flare|Flash|Glow|Lens Blur|Light Leak|Light Sweep|Phosphor|Radial Blur|Ray|Solarize|Stripe|Zoom Blur',
'Slide':'3D Roll|Film Roll|Push|Roll|Split|Stretch|Whip',
'Smart Tools':'Motion Camera|Motion Tween|Shape Flow',
'Text':'Text Animator|Typewriter',
'Transformers':'3D Spin|Frame|Louver|Mirror|Page Peel|Slice|Wave',
'Wipe':'Clock Wipe|Linear Wipe|Neon Wipe|Panel Wipe|Plateau Wipe|Radial Wipe|Soft Wipe|Star Wipe|Stretch Wipe'}
TRANS_LEGACY='Barn Doors|Center Split|Inset|Iris Box|Iris Cross|Iris Diamond|Iris Round|Non-Additive Dissolve|Wipe'.split('|')
TRANS_REMOVED='Gradient Wipe|Cube Spin|Flip Over'.split('|')
TRANS_ADDED='3D Spinback|Slide|Shape Dissolve'.split('|')
# Specific verified behavior for common effects/transitions; others have a clearly labeled inspection protocol.
EFFECT_PURPOSE={
 'Gaussian Blur':'Softens high-frequency detail; apply with masking to isolate a subject or obscure background.',
 'Directional Blur':'Simulates blur along a chosen direction to convey motion.',
 'Channel Blur':'Blurs selected color or alpha channels independently; useful for selective edge/color work.',
 'Crop':'Legacy crop effect; reduces visible rectangle; consider modern Rounded Crop where appropriate.',
 'Lens Flare':'Adds adjustable flare artifacts; match flare origin and direction to plausible light sources.',
 'Gradient':'Generates linear/radial gradients with options for interpolation, repetition, texture, and alpha.',
 'Twirl':'Rotates pixels around a defined center with controls for amount and radius.',
 'Mosaic':'Pixelates the image using tile geometry; 26.5 adds a Softness control.',
 'Warp Stabilizer':'Analyzes motion and reframes/warps frames to compensate for camera shake; cropping or distortion can result.',
 'Lumetri Color':'Provides exposure, curves, hue/saturation and other color correction and grading controls.',
 'Ultra Key':'Keys a green/blue screen image using selected screen color and matte cleanup controls.',
 'Track Matte Key':'Uses another layer as a matte to regulate which pixels remain visible.',
 'Noise':'Modern noise/grain generator; check amount and color-channel settings at full preview resolution.',
 'Magnify':'Modern magnifying-lens effect; adjust zoom, center, shape/softness to highlight details.',
 'Channel Mix':'Remaps or blends color channels; useful for stylized channel combinations.',
 'Vignette':'Darkens or lightens edges to direct attention inward.',
 'Metadata & Timecode Burn-in':'Overlays machine-readable metadata/time indications for review copies; check visibility in final master.'}
LENS_DESCS={'Cross Dissolve':'Blend outgoing and incoming images gradually, requiring suitable handles around the edit.',
'Dip to Black':'Fade down to black before revealing the following image.',
'Morph Cut':'Morph between similar interview frames; examine faces/edges for artifacts.',
'3D Spinback':'Modern 26.2 transition spinning clips in 3D with adjustable easing and blur.',
'Slide':'Modern 26.2 transition moving one clip relative to another with selectable motion controls.',
'Shape Dissolve':'Modern 26.3 shaped dissolve with geometry and motion controls.',
'Cross Zoom':'Move the outgoing view toward an enlarged region while revealing the incoming shot.',
'Clock Wipe':'Reveal the next image with a rotating radial sweep.',
'Linear Wipe':'Reveal one image along a configurable straight edge.',
'Star Wipe':'Reveal one image using an expanding or contracting star-shaped edge.'}
# Conceptual descriptions checked against Adobe's active 26.0 effect naming and family classification.
# These are not claims about every individual parameter in 26.5.2.
MODERN_EFFECT_PURPOSE={
'Bokeh Blur':'Creates a shallow-depth-of-field-inspired blur with soft highlights; test important subject edges.',
'Compound Blur':'Varies blur spatially using another luminance or image influence rather than one uniform radius.',
'Focus Blur':'Creates focus-like softening; check transition between sharp and soft regions.',
'Reduce Interlace Flicker':'Reduces high-frequency horizontal detail that can produce interlace display flicker; check resolution loss.',
'ASC CDL':'Applies ASC Color Decision List slope, offset, power and saturation corrections for predictable handoff.',
'Color Pass':'Keeps a selected hue region while desaturating much of the remaining image.',
'Invert':'Reverses selected image channel values, useful for negative/inversion graphics.',
'Rounded Crop':'Crops or frames an image with rounded corner geometry; distinguish from the Legacy Crop effect.',
'VR Blur':'Blurs immersive/equirectangular imagery while accounting for spherical presentation limitations.',
'VR Chromatic Aberrations':'Applies color-channel offsets to immersive footage for a lens-fringing look.',
'VR Color Gradients':'Produces color gradients for immersive video using its VR coordinate space.',
'VR De-Noise':'Reduces visible noise in immersive video; compare detail preservation after processing.',
'VR Digital Glitch':'Adds stylized glitch/disruption artifacts to immersive footage.',
'VR Fractal Noise':'Creates procedurally varying cloud/noise-like textures for immersive compositions.',
'VR Glow':'Adds glow around bright regions in immersive imagery.',
'VR Plane to Sphere':'Maps planar imagery into spherical/VR presentation; verify projection and seam behavior.',
'VR Projection':'Reprojects or adjusts the view of spherical video for different immersive viewing geometry.',
'VR Rotate Sphere':'Rotates spherical image orientation without moving the original camera.',
'VR Sharpen':'Enhances edge contrast for spherical footage, with possible halos or noise enhancement.',
'Logo Cutout':'Uses opacity/matte behavior to form a logo-shaped cutout or reveal.',
'Echo Glow':'Adds trailing or echo-like glow contributions from highlight regions.',
'Edge Glow':'Highlights detected image edges with a colored glow.',
'Glint':'Produces stylized glints or sparkle around bright image features.',
'Light Leaks':'Simulates stray light bleeding across the frame; use sparingly for coherence.',
'RGB Split':'Offsets red, green and blue channels to create chromatic separation.',
'Volumetric Rays':'Creates visible shafts of light radiating from bright image regions.',
'Wonder Glow':'Adds a stylized bloom/halation-like light treatment.',
'Long Shadow':'Extends a graphic element’s cast shadow along a direction.',
'Brush Strokes':'Makes image detail resemble a painting or stylized brush texture.',
'Color Emboss':'Uses channel/edge differentiation to create a colored raised-detail impression.',
'3D Rotate':'Transforms an image plane through perspective-inspired spatial rotation.',
'Auto Reframe':'Analyzes subject framing to recompose a sequence for a different aspect ratio; inspect auto choices.',
'Camera Shake':'Simulates camera jitter for an effect; avoid making motion difficult to watch.',
'Grow':'Scales or expands the image over time for an animated reveal.',
'Move':'Animates an image or graphic position with effect-specific controls.',
'Offset':'Wraps or shifts the picture in two dimensions to reposition its pixel content.',
'Shrink':'Animates a reduction in subject/clip scale with effect-specific controls.',
'Spacer':'Produces spacing/separation behavior for a visual element or transition; confirm exact installed controls.',
'Spin':'Animates rotation around a pivot or axis for dynamic motion.',
'Wiggle':'Introduces procedurally varied motion instead of a perfectly smooth static path.',
'Gradient Wipe':'Transitions image visibility through a luminance gradient map; a clip-level effect, not simply a cut.',
'Auto Align':'Attempts to register or align image components automatically; review framing and borders.',
'Cineon Converter':'Converts encoded Cineon-style film-log image values for an intended viewing or compositing pipeline.',
'Clone':'Copies a region or element within a composition; watch for repeating patterns and obvious seams.',
'Simple Text':'Creates straightforward text information within an effect workflow; compare dedicated title tools.',
'Stroke':'Draws an outline or traced stroke along a shape/matte or image feature, depending on effect configuration.'}
STAGE_PRACTICES={
1:'Keep three labels visible: original file on disk, project item, and timeline instance. If one is deleted, identify which other two survive.',
2:'Temporarily rename a COPY of a media folder (not the original); diagnose the offline link, then restore or relink it. Record the exact path.',
3:'Before pressing Insert or Overwrite, state the chosen source In/Out, playhead time, and destination source patch. Then predict duration.',
4:'Draw source-range and timeline-range before and after the operation; write which neighboring clips move and whether sequence duration changes.',
5:'Play both edits without looking at the timeline; describe what the viewer learns and why this cut is preferable.',
6:'Level-match the processed and bypassed versions before judging quality. Check intelligibility, pumping, and peak meters.',
7:'Disable the effect to compare. Inspect start, midpoint and end frames at full resolution; check any mask edge in motion.',
8:'Separate input interpretation, working space, and output transform. Compare scopes before approving a look.',
9:'Read captions without sound at normal speed; confirm timing, speaker, spelling and safe margins. Check actual exported output.',
10:'Measure source/picture/audio alignment at both beginning and end; verify proxy-to-original substitution on final export.',
11:'Log service availability and credit prompts before running generation. Manually review every edit produced by assistance.',
12:'Inspect actual encoded file metadata and play it outside the NLE. A successful export dialog is not delivery acceptance.',
13:'Keep a known-good copy, reproduce once, change one variable, and note if the failure follows media, sequence, effect or system.',
14:'Deliver a saved project, a separately playable file, source manifest and short acceptance report; another person must reproduce the result.'}
STAGE_TIPS={
1:'Explain the source-time to sequence-time mapping aloud; the timeline is an instruction list, not rewritten camera media.',
2:'Keep a clear source/working/export directory split. Never rename/move media merely to solve an unrelated preview issue.',
3:'Look at highlighted source patching and targeting before invoking edits. Unintended tracks can change the result.',
4:'For each trim, inspect the two frames either side of the edit and the exact overall sequence length.',
5:'Choose a cut for comprehension, emotion or emphasis; hide a bad cut only after checking whether the right shot was selected.',
6:'Avoid repairing a noisy waveform solely by loudness; compare processed signal at matched gain and inspect headroom.',
7:'Check effect stacking and local mask edge behavior. Avoid heavy processing until the story cut is stable.',
8:'Match technical exposure and neutral balance first. A creative LUT does not fix incorrect source interpretation.',
9:'An SRT sidecar does not carry all style choices. Test target captions in a separate playback application.',
10:'Proxies protect decoding performance but should not silently replace masters in final output.',
11:'AI can generate plausible but false or inconsistent results; validate facts, rights, artifacts and consent.',
12:'Name output profiles by container, codec, resolution, frame rate, color mode and audio specification.',
13:'Save a duplicate before resets, migrations or clearing caches. Record exact reproduction steps.',
14:'Have a second person test archived files, captions and deliverables; edit acceptance includes handoff.'}
# Curated micro explanations for high-risk lessons; more detailed material also lives in field guides.
DEEP={
'L001':'A project file is not the movie. A clip in Project may be used repeatedly with different In/Out ranges, and sequence changes do not change the bytes in the original MP4.',
'L002':'Timecode frame address 00:00:03:24 at 25 fps means three seconds and 24 frames; the next frame is 00:00:04:00. Timecode fields are not decimal fractions.',
'L009':'Save projects and source media separately; a project records source paths. Copying only the project file rarely constitutes a self-contained archive.',
'L014':'A proxy is a deliberately linked alternate representation, not a permanently substituted master. Verify relinking and export-source choice.',
'L018':'Source patching directs source video/audio when inserting or overwriting. Track targeting controls which sequence tracks participate in many timeline commands. They are not the same switch.',
'L021':'Ripple trims change sequence duration by shifting downstream material (subject to track sync rules). A rolling trim reallocates frames between adjacent clips while preserving their shared boundary and total duration.',
'L022':'In a slip, a clip’s visible source frames change but its sequence slot stays put. In a slide, the clip moves in sequence while neighboring edits compensate and its source selection stays put.',
'L023':'For a trim, ask: did the source In or Out change? Did the sequence position change? Did adjacent clips change? Did overall duration change?',
'L039':'Source gain is an input-level adjustment; a timeline clip volume envelope is automation; a track mixer fader changes the track output. Their position in processing affects downstream meters and effects.',
'L045':'dBFS marks digital sample magnitude relative to full scale; LUFS estimates perceived program loudness. Peak compliance and integrated loudness are different checks.',
'L055':'Color primaries/gamut, transfer curve, interpretation and display output all matter. SDR Rec.709 and HDR PQ deliverables require distinct checks.',
'L057':'A correction makes the source technically believable in the output space; a creative grade follows intent. A LUT cannot identify the correct source log curve by itself.',
'L060':'An input transform converts source encoding into working representation; a creative look changes the aesthetic; an output transform maps into delivery gamut and transfer function.',
'L065':'Transcript words are search/edit metadata, while subtitle captions are time-addressed text deliverables. Editing the transcript is not automatically the same as proofreading the exported captions.',
'L069':'Multicam sync may use audio waveforms, timecode, markers or clap; check early and late frames, especially on variable-frame-rate recordings.',
'L072':'A proxy increases playback efficiency by trading resolution/codec complexity. High-resolution exports generally require verifying that original media is online.',
'L076':'Automated generation, automated selection and manually created media have different provenance. Label service dependencies and document external credit usage.',
'L080':'Treat generated frames and sound as new editorial source clips, not ground truth or a guaranteed replacement for recorded evidence.',
'L083':'Timeline preview render files cache the image stream for smoother playback. A final export can recompute the sequence, use compatible previews when explicitly permitted, or encode into a different delivery codec. Preview bar color alone is not evidence of the exported file’s quality.',
'L084':'A container such as MP4 organizes streams; a codec such as H.264 compresses frames. Codec/profile/pixel format and data rate, not the file extension alone, determine compatibility and quality.',
'L085':'H.264 and HEVC are widely used interframe delivery codecs; ProRes and DNxHR families are often chosen as editing or mastering intermediates when a compatible codec, profile and wrapper are available. Every receiver must confirm the exact codec variant and audio specification.',
'L086':'Constant bitrate is predictable storage/network load; variable bitrate reallocates bits where complexity needs them. Hardware mode may alter quality/performance tradeoffs.',
'L090':'Export QC should include audio channel mapping, caption mode, color, scaling, start/end, and independent playback—not just the “completed” status.',
'L093':'A Windows virtual display adapter does not automatically expose hardware video encoding or GPU accelerated effects. Check actual guest driver and encoder availability.',
'L105':'The capstone is accepted only when the production, delivery files, permissions and relinkable archive independently satisfy the brief.'}

# Exercise verification is tied to the subject, not a universal "play it back" boilerplate.
STAGE_VERIFY={
1:'Record the calculated result or exact visible interface setting in your practice log; explain which variable you changed and which did not.',
2:'Check import metadata, media paths and the Project panel for the expected change; save a practice-project copy without moving the originals.',
3:'Play the two frames around the edit, verify sequence duration and source In/Out, and save a named practice version.',
4:'Check handles, immediate neighboring edits and overall sequence duration before/after; undo to confirm the change is reversible.',
5:'Watch the scene without inspecting the timeline; explain how shot order changes viewer knowledge, and preserve both versions.',
6:'Listen to matched-level before/after at realistic monitoring level; inspect sample and true-peak or loudness meters where applicable.',
7:'Preview the start, middle and end frames with the effect enabled and disabled; note masking, artifacts and performance.',
8:'Compare waveform/vectorscope before and after along with monitoring appearance; verify source/output color interpretation.',
9:'Proofread title/caption timing, spelling and contrast; where relevant, inspect the actual exported sidecar or burned-in image.',
10:'Check picture and sound sync at the start and end, then check whether proxy/original references resolve as intended.',
11:'Record version, service availability, permissions and output limitations; skip credit-consuming tests if your account does not include them.',
12:'Inspect the resulting encoded file in a separate player and read codec, frame rate, dimensions and audio channel metadata.',
13:'Document the observed symptom, one controlled test and the rollback path; preserve a known-good project copy before system changes.',
14:'Compare exports and archive against the brief and signed-off checklist; record one independently reproducible acceptance result.'}
STAGE_OBSERVE={
1:'In your own words, compare the concept to the expected result. No video playback is required for a paper or installation exercise.',
2:'Re-check source folder references, import metadata or current project settings without altering the original files.',
3:'Inspect the actual monitor and edit position. Write the exact In/Out values and the resulting timeline duration.',
4:'Observe which boundary moved, which source frames changed and whether duration is preserved.',
5:'Watch the assembled story and justify the cut against an alternative editorial choice.',
6:'Compare processed and bypassed sound at matched levels while observing clipping and dynamics.',
7:'Disable and re-enable the effect; inspect edge fidelity, opacity and the animation endpoints.',
8:'Compare scopes and visually inspected output separately; record any difference in interpretation or contrast.',
9:'Read the text aloud without sound and check style/timing in its actual exported form.',
10:'Inspect sync markers or matching sound events at two separated timeline positions.',
11:'Record which workflow is local and which relies on external services; evaluate outputs for artifacts or factual errors.',
12:'Compare export settings with output file metadata and replay both the start and end of the encoded file.',
13:'Record the system/driver state and reversible test outcome; do not modify a working production original.',
14:'Verify saved project and deliverables against the production acceptance list.'}
SAFER_CUSTOM_STEPS={
'L002':['At 25 fps, compute the duration of 100 frames as 4.00 seconds.',
       'Write frames 00:00:03:23, 00:00:03:24 and the next address, 00:00:04:00.',
       'Explain why 00:00:03:25 is invalid at 25 fps, and contrast a frame address with decimal seconds.'],
'L003':['Choose a 1920×1080 frame and divide width by height to obtain 16:9.',
       'Draw the same 16:9 framing inside a 1080×1920 vertical canvas; identify pillarboxing/cropping tradeoffs.',
       'Write the difference between pixel dimensions, display aspect ratio, and a creative reframing choice.'],
'L005':['Check Adobe’s Windows requirements against the OS edition, RAM, GPU driver, and available disk space on a nonproduction machine.',
       'Document Adobe login/activation requirements; confirm whether installed Premiere shows version 26.5.2 using Help > About Premiere.',
       'Open the application, record one launch problem if present, and avoid GPU/driver changes without a rollback plan.'],
'L006':['Open a disposable project and identify Project, Source Monitor, Program Monitor, Timeline, Effects, Effect Controls and Properties.',
       'Choose a workspace and reset its saved layout if needed; explain which panel changes source versus sequence context.',
       'Use the panels’ names—not their screen coordinates—to find them after moving a panel.'],
'L018':['Create a disposable sequence with V1, V2 and A1, then load a clip with video and audio into Source Monitor.',
       'Set source V1 patch to sequence V2 and source A1 patch to sequence A1, with adequate empty space.',
       'Place the playhead at a known time and press the documented Insert command (comma) once; verify the new clip is on V2/A1.',
       'Change sequence track targeting to V1 without changing source patching, repeat on a duplicated disposable sequence and compare outcomes.'],
'L039':['Using a nonclipping duplicate voice clip, set Audio Gain to +4 dB and compare input level with the untouched original.',
       'Reduce that instance volume by 2 dB; compare track fader movement on another clip on the same audio track.',
       'Verify relative loudness and metering with no overload; restore saved fader settings before continuing.'],
'L083':['Place a heavy effect on a five-second section of disposable footage and render a sequence preview.',
       'Play the preview while noting whether the render-status indicator changes after a further parameter edit.',
       'Export a separate output file, inspect the actual encoded codec and replay it outside Premiere.',
       'State explicitly whether preview render files or the exported deliverable were created at each step.'],
'L084':['For one media file, record its extension/container, video codec, frame dimensions and frame rate using a media-info tool.',
       'Choose an H.264 MP4 export, then compare its video stream identity and bitrate with the original file.',
       'Explain why renaming an .mp4 to .mov would not itself transcode the video.'],
'L085':['Create a receiver table for a mobile upload, a postproduction intermediate and a high-quality archive.',
       'Select an appropriate supported codec/profile/container for each receiver and estimate storage implications.',
       'Export two short approved samples only where the required encoder is available; compare playback and measured metadata.']}


def enrich(lessons, quizzes, shortcuts, fx, trans, SOURCE, version_audit):
    for L in lessons:
        n=int(L['id'][1:]); stage=L['stage']
        L['objective']=L['mastery'].rstrip('.')+'.'
        L['why']=L['concept'].rstrip('.')+'. '+('This determines what you must verify after editing: '+STAGE_PRACTICES[stage])
        L['use_cases']='Applicable when '+L['title'].lower()+' affects a real edit. '+STAGE_PRACTICES[stage]
        L['tip']=STAGE_TIPS[stage]
        L['deep_dive']=DEEP.get(L['id'],L['concept'].rstrip('.')+'. In a practice copy, verify the stated expected result and distinguish the setting being adjusted from the original media or unrelated tracks.')
        L['review_test']='Without changing any original media, explain how to recognize and prevent this possible mistake: '+L['mistakes'][0].rstrip('.')+'. Then reproduce the safe exercise and compare against its stated result.'
        L['steps']=[STAGE_VERIFY[stage] if 'Compare before and after at normal playback; save a named practice version and record one observation.' in v
                    else STAGE_OBSERVE[stage] if ('Observe the Program Monitor, timeline positions, and any modified controls before you undo or save.' in v or 'Repeat once, explaining which source frames or output signals changed.' in v)
                    else v for v in L['steps']]
        if L['id'] in SAFER_CUSTOM_STEPS:L['steps']=SAFER_CUSTOM_STEPS[L['id']]
        # A paper-based mental-model exercise has no preview/playback and no saveable Premiere sequence.
        if n==1:
            L['steps']=['Draw two 100-frame strips labelled A and B; number their source frames 0–99.',
            'On paper, select A frames 20–49 (inclusive) and B frames 40–69 (inclusive).',
            'Place both selections end-to-end in a 30 fps paper timeline.',
            'Count 60 timeline frames (= 2 seconds), locate A source frame 20 at sequence frame zero, and explain why neither source strip changed.']
        if n==105:
            L['steps']=['Choose and document an achievable 2:30–3:30 production brief and original/licensed footage.',
            'Create folders and import originals without breaking paths. Construct rough cut, then picture lock.',
            'Finish dialogue/music, normalize cameras, add titles/captions and review at normal speed.',
            'Export a specified H.264 MP4 and a high-quality master after checking color, audio and caption modes.',
            'Reopen the archived project from a copied location and play both exported deliverables outside Premiere.',
            'Complete the capstone rubric and note any unmet acceptance tests.']
    # Independent Stage-14 projects do not require completing all advanced chapters.
    applied={
      'L097':['L016','L039','L040'],
      'L098':['L033','L044'],
      'L099':['L020','L063','L087'],
      'L100':['L036','L045','L065'],
      'L101':['L053','L054','L061'],
      'L102':['L069','L070','L073'],
      'L103':['L045','L057','L061'],
      'L104':['L062','L068','L090'],
      'L105':['L075','L088','L090','L096','L104']}
    for L in lessons:
        if L['id'] in applied:L['prerequisites']=applied[L['id']]
    # Effect parameters cannot be guessed merely from a category name.
    for effect in fx:
        if effect['parameters'].startswith('Intensity, position, mask or sliders'):
            effect['parameters']='Inspect the controls in the installed Effect Controls panel; parameter names and range vary by effect/version.'
    for effect in fx:
        if effect['kind']=='Video':
            specific={'Lumetri Color':'Basic Correction (exposure, balance), Curves, Color Wheels, HSL Secondary and other modules.',
                      'Gaussian Blur':'Blurriness; repeat-edge and/or masking options depend on selected version.',
                      'Channel Blur':'Color mode/channel selection and individual blur controls (modern 26.2 version).',
                      'Mosaic':'Grid/tile geometry and Softness (modern 26.5 version).',
                      'Twirl':'Center, radius/angle and related spatial controls (modern 26.5 version).',
                      'Gradient':'Gradient stops, linear/radial direction, opacity, texture and interpolation.',
                      'Ultra Key':'Key color, matte generation, matte cleanup and spill suppression settings.',
                      'Warp Stabilizer':'Motion analysis, stabilization smoothness/method and framing/crop tradeoffs.',
                      'Lens Flare':'Flare source position, shape, streak intensity and color in modern 26.5 version.'}
            if effect['name'] in specific:effect['parameters']=specific[effect['name']]
    # Rotate options while preserving which answer is correct: previously all 42 answers were A.
    # This is a genuine assessment-design flaw, not a programmatic validity error.
    for i,q in enumerate(quizzes):
        offset=i%4
        if offset:
            q['options']=q['options'][-offset:]+q['options'][:-offset]
            q['answer']=(q['answer']+offset)%4
    # All rows from Adobe's published 2026 shortcuts chart (by category) are authoritative when context is reproduced.
    for k in shortcuts:
        k['status']='Adobe 2026 Windows default table; verify installed shortcut set'
    def addkey(cat,name,keys,ctx='Menu command / active appropriate panel',source='keys'):
        if any(x['command']==name and x['windows']==keys for x in shortcuts): return
        shortcuts.append({'category':cat,'command':name,'windows':keys,'context':ctx,'status':'Adobe 2026 Windows default table; verify installed shortcut set','source':source})
    for name,key in [('Duplicate','Ctrl+Shift+/')]:addkey('Editing',name,key)
    for name,key in [('Extract',"'"),('Zoom In','='),('Zoom Out','-'),('Next in Sequence','Shift+;'),('Previous in Sequence','Ctrl+Shift+;'),('Make Subsequence','Shift+U'),('Add new caption track','Ctrl+Alt+A'),('Add caption at playhead','Ctrl+Alt+C'),('Next caption segment','Ctrl+Alt+Down'),('Previous caption segment','Ctrl+Alt+Up')]:addkey('Sequence',name,key)
    addkey('Markers / source','Clear all markers','Ctrl+Alt+Shift+M')
    for name,key in [('Show/hide tracks','Ctrl+Alt+T'),('Loop (Audio Track Mixer)','Ctrl+L'),('Meter input only','Ctrl+Shift+I')]:addkey('Audio Track Mixer panel',name,key,'Audio Track Mixer focused')
    for name,key in [('Remove selected effect','Backspace'),('Loop during audio-only playback','Ctrl+L')]:addkey('Effect Controls panel',name,key,'Effect Controls panel focused')
    for name,key in [('New custom bin','Ctrl+/'),('Delete custom item','Backspace')]:addkey('Effects panel',name,key,'Effects panel focused')
    for name,key in [('Step backward','Left'),('Step forward','Right'),('Delete history step','Backspace')]:addkey('History panel',name,key,'History panel focused')
    for name,key in [('Select directory list','Shift+Left'),('Select media list','Shift+Right')]:addkey('Media Browser panel',name,key,'Media Browser focused')
    for name,key in [('Loop (Metadata)','Ctrl+L'),('Play (Metadata)','Space')]:addkey('Metadata panel',name,key,'Metadata panel focused')
    for name,key in [('Nudge graphic up 1 unit','Ctrl+Up'),('Nudge graphic down 1 unit','Ctrl+Down'),('Nudge graphic up 5 units','Ctrl+Shift+Up'),('Nudge graphic down 5 units','Ctrl+Shift+Down'),('Nudge graphic left 5 units','Ctrl+Shift+Left'),('Nudge graphic right 5 units','Ctrl+Shift+Right')]:addkey('Program Monitor',name,key,'Program Monitor selected graphic layer; Adobe table labels movement as frames, interface positioning is spatial')
    for name,key in [('Project view toggle','Shift+\\'),('Project thumbnail larger','Shift+]'),('Project thumbnail smaller','Shift+['),('Project next column','Tab'),('Project previous column','Shift+Tab')]:addkey('Project panel',name,key,'Project panel focused')
    for name,key in [('Set work area In','Alt+['),('Set work area Out','Alt+]'),('Show next screen','Page Down'),('Show previous screen','Page Up')]:addkey('Timeline panel',name,key,'Timeline panel focused')
    # Complete Adobe's explicit Project/Timeline panel navigation rows without guessing undocumented keys.
    for name,key in [
        ('Project delete','Backspace'),('Project extend selection down','Shift+Down'),
        ('Project extend selection left','Shift+Left'),('Project extend selection right','Shift+Right'),
        ('Project extend selection up','Shift+Up'),('Project move selection down','Down'),
        ('Project move selection end','End'),('Project move selection home','Home'),
        ('Project move selection left','Left'),('Project move selection page down','Page Down'),
        ('Project move selection page up','Page Up'),('Project move selection right','Right'),
        ('Project move selection up','Up'),('Project next row field','Enter'),
        ('Project previous row field','Shift+Enter'),('Project zoom in','='),
        ('Project zoom out','-')]:
        addkey('Project panel',name,key,'Project panel focused; availability depends on icon/list and selection mode')
    addkey('Timeline panel','Timeline clear selection','Backspace','Timeline panel focused; distinguish from other Backspace commands')
    # FilmCraft & Premiere Pro verified shortcuts: tools, multicam, trimming, clip volume, zoom and typography
    for name,key,ctx in [
        ('Selection Tool','V','Tools panel / Timeline'),
        ('Track Select Forward Tool','A','Tools panel / Timeline'),
        ('Track Select Backward Tool','Shift+A','Tools panel / Timeline'),
        ('Ripple Edit Tool','B','Tools panel / Timeline'),
        ('Rolling Edit Tool','N','Tools panel / Timeline'),
        ('Rate Stretch Tool','R','Tools panel / Timeline'),
        ('Razor Tool','C','Tools panel / Timeline'),
        ('Slip Tool','Y','Tools panel / Timeline'),
        ('Slide Tool','U','Tools panel / Timeline'),
        ('Pen Tool','P','Tools panel / Timeline'),
        ('Hand Tool','H','Tools panel / Timeline'),
        ('Zoom Tool','Z','Tools panel / Timeline'),
        ('Type Tool','T','Tools panel / Canvas'),
    ]: addkey('Tools',name,key,ctx)
    for name,key,ctx in [
        ('Select Camera 1','1','Multi-Camera view / Program Monitor'),
        ('Select Camera 2','2','Multi-Camera view / Program Monitor'),
        ('Select Camera 3','3','Multi-Camera view / Program Monitor'),
        ('Select Camera 4','4','Multi-Camera view / Program Monitor'),
        ('Select Camera 5','5','Multi-Camera view / Program Monitor'),
        ('Select Camera 6','6','Multi-Camera view / Program Monitor'),
        ('Select Camera 7','7','Multi-Camera view / Program Monitor'),
        ('Select Camera 8','8','Multi-Camera view / Program Monitor'),
        ('Select Camera 9','9','Multi-Camera view / Program Monitor'),
        ('Cut to Camera 1','Ctrl+1','Timeline / Multi-Camera view'),
        ('Cut to Camera 2','Ctrl+2','Timeline / Multi-Camera view'),
        ('Cut to Camera 3','Ctrl+3','Timeline / Multi-Camera view'),
        ('Cut to Camera 4','Ctrl+4','Timeline / Multi-Camera view'),
        ('Cut to Camera 5','Ctrl+5','Timeline / Multi-Camera view'),
        ('Cut to Camera 6','Ctrl+6','Timeline / Multi-Camera view'),
        ('Cut to Camera 7','Ctrl+7','Timeline / Multi-Camera view'),
        ('Cut to Camera 8','Ctrl+8','Timeline / Multi-Camera view'),
        ('Cut to Camera 9','Ctrl+9','Timeline / Multi-Camera view'),
        ('Multi-Camera Record On/Off Toggle','0','Multi-Camera view / Program Monitor'),
        ('Multi-Camera View Toggle','Shift+0','Program Monitor'),
    ]: addkey('Multi-Camera',name,key,ctx)
    for name,key,ctx in [
        ('Ripple Trim Previous Edit to Playhead','Q','Timeline panel'),
        ('Ripple Trim Next Edit to Playhead','W','Timeline panel'),
        ('Extend Previous Edit to Playhead','Shift+Q','Timeline panel'),
        ('Extend Next Edit to Playhead','Shift+W','Timeline panel'),
        ('Trim Previous Edit Point','Alt+Q','Timeline panel'),
        ('Trim Next Edit Point','Alt+W','Timeline panel'),
    ]: addkey('Trimming',name,key,ctx)
    for name,key,ctx in [
        ('Go to Next Edit Point on Any Track','Shift+Down','Timeline panel'),
        ('Go to Previous Edit Point on Any Track','Shift+Up','Timeline panel'),
        ('Go to Sequence Start','Home','Timeline panel'),
        ('Go to Sequence End','End','Timeline panel'),
        ('Go to Selected Clip Start','Shift+Home','Timeline panel'),
        ('Go to Selected Clip End','Shift+End','Timeline panel'),
        ('Select Clip at Playhead','D','Timeline panel'),
        ('Select Next Clip','Ctrl+Down','Timeline panel'),
        ('Select Previous Clip','Ctrl+Up','Timeline panel'),
        ('Step Forward 1 Frame','Right','Timeline / Monitor focus'),
        ('Step Backward 1 Frame','Left','Timeline / Monitor focus'),
        ('Step Forward 5 Frames','Shift+Right','Timeline / Monitor focus'),
        ('Step Backward 5 Frames','Shift+Left','Timeline / Monitor focus'),
        ('Zoom to Sequence','\\','Timeline panel'),
        ('Expand All Tracks','Shift+=','Timeline panel'),
        ('Minimize All Tracks','Shift+-','Timeline panel'),
        ('Toggle All Video Targets','Ctrl+0','Timeline panel'),
        ('Toggle All Audio Targets','Ctrl+9','Timeline panel'),
        ('Toggle All Source Video','Ctrl+Alt+0','Timeline panel'),
        ('Toggle All Source Audio','Ctrl+Alt+9','Timeline panel'),
    ]: addkey('Timeline panel',name,key,ctx)
    addkey('Sequence','Reveal Nested Sequence','Ctrl+Alt+F','Timeline panel')
    for name,key,ctx in [
        ('Increase Clip Volume (1 dB)',']','Timeline / Audio track'),
        ('Decrease Clip Volume (1 dB)','[','Timeline / Audio track'),
        ('Increase Clip Volume Many (6 dB)','Shift+]','Timeline / Audio track'),
        ('Decrease Clip Volume Many (6 dB)','Shift+[','Timeline / Audio track'),
        ('Toggle Audio Scrubbing','Shift+S','Application / Timeline'),
        ('Set Poster Frame','Ctrl+P','Project panel / Clip'),
        ('Clear Poster Frame','Alt+P','Project panel / Clip'),
        ('Replace with Clip from Bin','Ctrl+Shift+R','Timeline / Project panel'),
        ('Replace with Clip from Source Monitor','Ctrl+Alt+Shift+R','Timeline / Source Monitor'),
    ]: addkey('Clip actions',name,key,ctx)
    for name,key,ctx in [
        ('Maximize or Restore Active Frame','Shift+`','Workspace / panel focus'),
        ('Maximize or Restore Frame Under Cursor','`','Workspace / cursor location'),
        ('Toggle Full Screen','Ctrl+`','Application / Monitor'),
        ('Select Next Panel','Ctrl+Shift+.','Workspace focus'),
        ('Select Previous Panel','Ctrl+Shift+,','Workspace focus'),
        ('Select Find Box','Shift+F','Active panel / Project'),
    ]: addkey('Panels / workspaces',name,key,ctx)
    addkey('Program Monitor','Zoom Program Monitor to 100%','Ctrl+Shift+1','Program Monitor focused')
    addkey('Program Monitor','Zoom Program Monitor to Fit','Ctrl+Shift+0','Program Monitor focused')
    addkey('Source Monitor','Zoom Source Monitor to 100%','Ctrl+Alt+Shift+1','Source Monitor focused')
    addkey('Source Monitor','Zoom Source Monitor to Fit','Ctrl+Alt+Shift+0','Source Monitor focused')
    addkey('Playback / editing tools','Play In to Out with Preroll','Shift+Space','Source / Program Monitor',source='playback')
    addkey('Playback / editing tools','Play from Playhead to Out Point','Ctrl+Space','Source / Program Monitor',source='playback')
    for name,key,ctx in [
        ('Increase Font Size by 1 Unit','Ctrl+Alt+Right','Essential Graphics / Text layer'),
        ('Decrease Font Size by 1 Unit','Ctrl+Alt+Left','Essential Graphics / Text layer'),
        ('Increase Font Size by 5 Units','Ctrl+Alt+Shift+Right','Essential Graphics / Text layer'),
        ('Decrease Font Size by 5 Units','Ctrl+Alt+Shift+Left','Essential Graphics / Text layer'),
        ('Increase Leading by 1 Unit','Alt+Up','Essential Graphics / Text layer'),
        ('Decrease Leading by 1 Unit','Alt+Down','Essential Graphics / Text layer'),
        ('Increase Leading by 5 Units','Alt+Shift+Up','Essential Graphics / Text layer'),
        ('Decrease Leading by 5 Units','Alt+Shift+Down','Essential Graphics / Text layer'),
        ('Left Align Text','Ctrl+Shift+L','Essential Graphics / Text layer'),
        ('Center Align Text','Ctrl+Shift+C','Essential Graphics / Text layer'),
        ('Right Align Text','Ctrl+Shift+R','Essential Graphics / Text layer'),
        ("Begin Text Editing for Graphic Layer","Ctrl+Alt+'",'Program Monitor / Graphics'),
        ('Export Frame','Shift+E','Program Monitor / Source Monitor'),
    ]: addkey('Graphics',name,key,ctx)
    addkey('Project panel','New Bin from Selection','Shift+B','Project panel focused')
    addkey('Editing','Paste Insert','Ctrl+Shift+V','Timeline panel')
    addkey('Editing','Open Search','Ctrl+Shift+F','Application')
    addkey('File and project','Preferences General','Ctrl+,','Application')
    # The remaining five rows have separate 26.x Adobe gameplay reference, not the default menu table.
    for k in shortcuts:
        if k['command'] in ('Playback toggle','Play reverse','Stop','Play forward'):
            k['status']='Adobe 26.x playback documentation; check key set/panel focus'
            k['source']='playback'
        if k['command']=='Snap':
            k['status']='Adobe 2026 Windows default table; verify installed shortcut set';k['source']='keys'
    # Audio page directly documents these effects, but its some descriptions refer to Audition-specific controls.
    audio_doc={ 'Amplify','Channel Volume','DeEsser','Dynamics','Dynamics Processing','Hard Limiter','Multiband Compressor','Single-band Compressor','Analog Delay','Delay','Echo','Bass','FFT Filter','Notch Filter','Parametric Equalizer','Scientific Filter','Flanger','Phaser','Automatic Click Remover','Convolution Reverb','Studio Reverb','Surround Reverb','Distortion','Guitar Suite','Vocal Enhancer','Pitch Shifter','Stereo Expander','DeNoise','DeReverb'}
    audio_uncertain={'Adaptive Noise Reduction','Fill Left with Right','Fill Right with Left','Balance','Graphic Equalizer (10 Bands)','Graphic Equalizer (20 Bands)','Graphic Equalizer (30 Bands)','Chorus/Flanger','Treble'}
    for f in fx:
        name=f['name'];kind=f['kind'];f['source']='effectchange' if kind=='Video' else 'audio'
        if kind=='Audio':
            if name in audio_doc: f['status']='Current Adobe 2026 audio reference; verify exact effect controls in Premiere'
            elif name in audio_uncertain: f['status']='Audio feature/name not conclusively established by current Premiere catalog; verify installed seat'
            else: f['status']='Audio: category documented but name/device availability needs installed-seat verification'
            continue
        if name in VIDEO_RENAMES: f['limitations']=VIDEO_RENAMES[name]+' '+f['limitations']
        if name in NEW_VIDEO: f['status']='Current 26.2–26.5 replacement documented (do not confuse old plug-in)';f['source']='effects'
        elif name in LEGACY_VIDEO: f['status']='Legacy in Adobe 26.0 taxonomy, not the modern default'
        elif name in OBSOLETE_VIDEO: f['status']='Obsolete/hidden for new effects in Adobe 26.0 taxonomy'
        elif name in REMOVED_VIDEO and name not in CURRENT_VIDEO: f['status']='Removed in Premiere 26.0; not a usable current effect'
        elif name in CURRENT_VIDEO: f['status']='Adobe 26.0 active video effects list (patch-level UI untested)'
        else:f['status']='Unresolved name in official 26.x effect catalog — do not assume available'
        if name in EFFECT_PURPOSE:f['purpose']=EFFECT_PURPOSE[name]
    # Add documented current effects lacking from first-pass historical catalog.
    present={f['name'] for f in fx if f['kind']=='Video'}
    for name in CURRENT_VIDEO:
        if name in present: continue
        fx.append({'name':name,'kind':'Video','category':'Adobe 26.x active video list',
             'purpose':'Adobe lists this as an active video effect. Inspect the specific parameter tooltips and preview behavior before production use.',
             'parameters':'Specific controls vary by effect; inspect its Effect Controls/Properties entry in version 26.5.2.',
             'example':'Apply to a duplicate 5-second clip, modify one control, toggle bypass, check start/mid/end and output.',
             'performance':'GPU usage and renderer depend on effect, resolution, combination and installed driver.',
             'limitations':'The 26.0 list confirms name/category, not exhaustive patch-specific controls; test in 26.5.2.',
             'status':'Adobe 26.0 active video effects list (patch-level UI untested)', 'related':'Effects panel; Effect Controls; adjustment layers', 'source':'effectchange'})
    for name in ['Auto Align','Clone','Channel Mix','Mosaic','Vignette','Stroke','Long Shadow','Rounded Crop','Focus Glow']:
        if name not in present:
            pass # current 26.0 list already covers most; new `Focus Glow` separately included below.
    if 'Focus Glow' not in {x['name'] for x in fx if x['kind']=='Video'}:
        fx.append({'name':'Focus Glow','kind':'Video','category':'Modern lights and glows','purpose':'Adds a localized glow around focal areas.','parameters':'Inspect effect-specific controls in installed version.','example':'Apply to a bright isolated object and compare subtle vs high intensity at 100% preview.','performance':'Official modern effect family uses GPU acceleration; actual playback varies by hardware.','limitations':'Exact modern Effects-panel display may differ from historical “FX” marketing name.','status':'Current modern effects document, name requires panel confirmation','related':'Glow; mask; exposure','source':'effects'})
    for effect in fx:
        if effect['purpose'].startswith('Adobe lists this as an active video effect.') and (effect['name'] in MODERN_EFFECT_PURPOSE or effect['name'] in EFFECT_PURPOSE):
            effect['purpose']=MODERN_EFFECT_PURPOSE.get(effect['name'],EFFECT_PURPOSE.get(effect['name'],effect['purpose']))
    # Restore Adobe's specific 26.0 effect panel taxonomy instead of a generic "active" bucket.
    adobe_groups={
      'Adjust':'Extract|Levels|Lighting Effects|ProcAmp',
      'Blur & Sharpen':'Bokeh Blur|Compound Blur|Directional Blur|Focus Blur|Gaussian Blur|Reduce Interlace Flicker|Sharpen|Unsharp Mask',
      'Color Correction':'ASC CDL|Brightness & Contrast|Lumetri Color|Tint|Video Limiter|Vignette',
      'Distort':'Corner Pin|Lens Distortion|Mirror|Spherize|Turbulent Displace|Twirl|Warp Stabilizer|Wave Warp',
      'Generate':'4-Color Gradient',
      'Image Control':'Black & White|Channel Mix|Color Pass|Color Replace|Gamma Correction|Invert|Rounded Crop',
      'Immersive Video':'VR Blur|VR Chromatic Aberrations|VR Color Gradients|VR De-Noise|VR Digital Glitch|VR Fractal Noise|VR Glow|VR Plane to Sphere|VR Projection|VR Rotate Sphere|VR Sharpen',
      'Keying':'Alpha Adjust|Color Key|Logo Cutout|Luma Key|Track Matte Key|Ultra Key',
      'Lights & Glows':'Echo Glow|Edge Glow|Glint|Light Leaks|RGB Split|Volumetric Rays|Wonder Glow',
      'Noise & Grain':'Noise',
      'Perspective':'Basic 3D|Drop Shadow|Long Shadow',
      'Stylize':'Brush Strokes|Color Emboss|Find Edges|Mosaic|Posterize|Roughen Edges|Strobe Light',
      'Time':'Posterize Time',
      'Transform':'3D Rotate|Auto Reframe|Camera Shake|Grow|Horizontal Flip|Move|Offset|Shrink|Spacer|Spin|Transform|Vertical Flip|Wiggle',
      'Transition':'Gradient Wipe',
      'Utility':'Auto Align|Cineon Converter|Clone|Metadata & Timecode Burn-in|Simple Text|Stroke'}
    group_index={name:cat for cat,pipes in adobe_groups.items() for name in pipes.split('|')}
    for fx_item in fx:
        if fx_item['kind']=='Video' and fx_item['name'] in group_index:
            fx_item['category']=group_index[fx_item['name']]
    # A reviewer needs alphabetical reference lookup, unlike chronological lesson ordering.
    fx.sort(key=lambda item:(item['kind'],item['category'].casefold(),item['name'].casefold()))
    trans.sort(key=lambda item:(item['category'].casefold(),item['name'].casefold()))
    # Reconcile release-specific audit record with the reclassified catalog.
    for i, row in enumerate(version_audit):
        if row[0]=='Effects catalogue':
            version_audit[i]=('Effects catalogue','26.0–26.5.2','Adobe taxonomy cross-checked; installed inventory untested',
                'Separates active, Legacy, Obsolete, Removed, new replacements and unresolved names in exported data. Exact installed controls require a Windows Premiere test.')
    # Distinguish modern names vs marketing FX suffix (Adobe document uses both) without creating duplicate invented plug-ins.
    lookup={x['name']:x for x in trans}; allnow={n:c for c,names in TRANSITION_GROUPS.items() for n in names.split('|')}
    for t in trans:
        n=t['name'];t['source']='effectchange' if n not in ('Constant Gain','Constant Power','Exponential Fade') else 'transitions'
        if n in TRANS_ADDED: t['status']='Confirmed added 26.2–26.3 modern transition';t['source']='new'
        elif n in TRANS_REMOVED: t['status']='Removed in Premiere 26.0; do not use for new projects'
        elif n in TRANS_LEGACY: t['status']='Legacy transition (Adobe 26.0); separate from modern replacements'
        elif n in allnow: t['status']='Adobe 26.0 active transition list (installed panel untested)';t['category']='Video '+allnow[n]
        elif n in ('Constant Gain','Constant Power','Exponential Fade'):t['status']='Adobe audio transition family (installed panel untested)'
        else:t['status']='Unresolved: check installed Effects panel before use'
        if n in LENS_DESCS:t['description']=LENS_DESCS[n]
    for name,group in allnow.items():
        if name in lookup: continue
        trans.append({'name':name,'category':'Video '+group,'description':LENS_DESCS.get(name,'Current Adobe-documented transition in the '+group+' family; compare visually with a cut and verify available source handles.'),
            'parameters':'Duration, alignment and effect-specific controls; inspect the applied transition in Effect Controls.',
            'example':'Test two 5-second clips with 15-frame handles, then adjust transition duration and compare the edit.',
            'limitations':'Adobe lists the transition in 26.0; actual GPU behavior, handles and parameters depend on installed 26.5.2.',
            'status':'Adobe 26.0 active transition list (installed panel untested)','source':'effectchange'})
    for name in TRANS_ADDED:
        if any(t['name']==name for t in trans):continue
        trans.append({'name':name,'category':'Modern video transition','description':LENS_DESCS.get(name,'Modern animated video transition added in 26.2–26.3.'),
            'parameters':'Duration, alignment and effect-specific direction/shape/motion controls.', 'example':'Apply to two clips with handles, adjust the effect, review at 25 fps.',
            'limitations':'Confirm transition handles and output in 26.5.2.', 'status':'Confirmed added 26.2–26.3 modern transition', 'source':'new'})
    # add a genuinely useful difference between historical exact plug-in versions where names overlap
    version_audit.append(('26.0 effects removal/legacy migration','26.0','Yes','Modern named effects replace or coexist with historical plug-ins; old removed variants may fail to render in legacy projects.'))
    version_audit.append(('Windows shortcut audit','26.0–26.5.2','Reference verified; live UI untested','Expanded Adobe default keyboard table, plus separate Adobe playback J/K/L verification; conflicts explicitly panel-scoped.'))
    SOURCE['effectchange']=('Effects and transitions changes in Premiere 26.0',ADOBE_EFF,'26.0; still relevant to 26.5.2','Authoritative active, Legacy, Obsolete and Removed inventories; later re-added effects tracked separately.')
    SOURCE['playback']=('Play active sequence in Program Monitor','https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-active-sequence-in-program-monitor.html','26.x','Adobe explicitly documents Space, J, K and L playback controls.')
    SOURCE['effectremove']=('Removed effects and transitions','https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/effects-and-transitions-removed-from-adobe-premiere.html','26.x','Explains obsolete/replaced effects behavior in existing projects.')
    SOURCE['effects']=('Modern Premiere effects',ADOBE_MOD,'26.2–26.5','GPU-accelerated modern effects including replacement Lens Flare and Channel Blur.')
    trans.sort(key=lambda item:(item['category'].casefold(),item['name'].casefold()))
    return {'shortcuts':len(shortcuts),'videoeffects':sum(x['kind']=='Video' for x in fx),'audioeffects':sum(x['kind']=='Audio' for x in fx),'transitions':len(trans)}
