"""Curated encyclopedias for Photoshop 27.11 Windows. Entries use an editorial shared schema."""
TOOLS_RAW=r'''
Move|Arrange|V|Moves selected layers or selections; can auto-select under configured options.|Auto-Select; Show Transform Controls; alignment|Use with multiple selected layers for precise layouts.|Dragging a locked or wrong layer appears to do nothing.|s02l03
Artboard|Arrange||Creates multiple layout canvases in one file.|Preset dimensions; orientation; artboard properties|Useful for multiple screen-size variants.|Artboards are not independent PSD files.|s10l05
Frame|Arrange|K|Creates image placeholder frames using shape boundaries.|Rectangular/elliptical frames; frame content fit|Use for replacing photos inside layouts.|A frame is not a normal empty raster selection.|s07l06
Rectangular Marquee|Selection|M|Selects a rectangular pixel region.|Feather; selection mode; fixed size|Use for crisp tiles and straight areas.|Nonzero Feather softens edges.|s03l01
Elliptical Marquee|Selection|M|Selects circular or elliptical regions.|Feather; fixed ratio; selection mode|Use for round badges and masked highlights.|Dragging by eye may create an ellipse rather than circle.|s03l01
Single Row Marquee|Selection||Selects a one-pixel-high horizontal row.|Selection mode; location|Useful for exact row sampling or rules.|At low zoom the selection can be hard to see.|s03l01
Single Column Marquee|Selection||Selects a one-pixel-wide vertical column.|Selection mode; location|Useful for precise column operations.|Affected width is only one pixel.|s03l01
Lasso|Selection|L|Freehand selection traced with mouse or pen.|Feather; Add/Subtract; anti-alias|Use for rough subject boundaries.|Hand jitter creates uneven edges.|s03l01
Polygonal Lasso|Selection|L|Connects straight selection segments.|Feather; Add/Subtract|Use for faceted objects and architecture.|Every click adds a corner.|s03l01
Magnetic Lasso|Selection|L|Suggests edges while cursor follows them.|Width; Contrast; Frequency|Useful for defined contrast edges.|Low-contrast boundaries cause drift.|s03l02
Object Selection|Selection|W|Detects a probable object from region or hover.|Rectangle/Lasso modes; Object Finder; selection operations|Use for recognizable objects.|Detection is not final-quality masking.|s03l02
Quick Selection|Selection|W|Paints a selection that expands toward edges.|Brush size; Add/Subtract; Sample All Layers|Use for manual-plus-assisted extraction.|Fast strokes may spill across weak boundaries.|s03l02
Magic Wand|Selection|W|Chooses similar contiguous or discontiguous colors.|Tolerance; Contiguous; Anti-alias|Use for flat-color graphics.|Low tolerance leaves fringe; high selects too much.|s03l02
Selection Brush|Selection||Paints selection regions directly.|Brush size; Add/Subtract; edge behavior|Use for irregular selectable areas.|Painted selection is not itself a layer mask.|s03l02
Crop|Geometry|C|Reframes and optionally removes cropped pixels.|Aspect ratio; Delete Cropped Pixels; straighten|Use to recompose photography.|Destructive crop can remove hidden pixels.|s02l01
Perspective Crop|Geometry|C|Rectifies a photographed quadrilateral to rectangular edges.|Corner handles; dimensions|Use for documents photographed at an angle.|Severe correction stretches low-res detail.|s02l01
Slice|Web legacy|C|Defines web slices for legacy sliced exports.|Slice type; boundaries|Use only with legacy asset pipelines.|Modern export usually favors individual assets.|s10l04
Slice Select|Web legacy|C|Selects and edits existing slices.|Slice properties; selection|Maintain existing sliced layouts.|Does not select pixels for ordinary painting.|s10l04
Eyedropper|Color|I|Samples color from image or composite.|Sample Size; Sample layers|Use to match colors in a design.|Edge samples mix neighboring tones.|s06l03
Color Sampler|Color|I|Places persistent color readout sample points.|Sample Size; Info readout|Use to compare color before/after edits.|Readouts depend on selected color model.|s08l03
Ruler|Measure|I|Measures distance and angle on image.|Units; straighten interactions|Use to check tilted horizon or scale.|Ruler measurement does not resize the image.|s01l05
Note|Measure|I|Stores annotations in supported documents.|Author; note text|Use for editorial feedback on a working file.|Not all delivery formats retain notes.|s10l01
Count|Measure|I|Marks numbered count items.|Count groups; marker size|Use for inventory or object count.|Marks are metadata overlays, not finished art.|s01l05
Spot Healing Brush|Retouch|J|Automatically repairs small defects from neighbors.|Content-Aware/Proximity Match; Sample All Layers|Use for tiny blemishes.|Brush larger than defect often smears texture.|s05l01
Healing Brush|Retouch|J|Repairs target using chosen source texture and tone adaptation.|Source Aligned; Sample; diffusion|Use for controlled skin or surface repair.|Wrong source area repeats unwanted detail.|s05l01
Patch|Retouch|J|Repairs a selected patch with source content.|Source/Destination; Normal/Content-Aware|Use for broad skin or wall blemishes.|Dragged source with different lighting looks wrong.|s05l02
Content-Aware Move|Retouch|J|Moves a selected object and infers replacement around it.|Move/Extend; structure/color|Use for local object repositioning.|Complex backgrounds show repeated content.|s05l03
Red Eye|Retouch|J|Darkens camera-flash red eye areas.|Pupil Size; Darken Amount|Use for old flash portraits.|Avoid clicking non-eye red features.|s05l04
Remove|Retouch|J|Paints over unwanted objects with reconstruction options.|Brush size; Remove after each stroke; processing mode|Use for wires and distractions after review.|AI reconstruction may invent details; local model needs supported hardware/download.|s05l03
Brush|Paint|B|Paints with a brush tip and configured color.|Size; hardness; opacity; flow; smoothing|Use for art and masks.|Painting on wrong thumbnail damages content.|s06l01
Pencil|Paint|B|Draws hard-edged marks without soft antialias blending.|Size; opacity; tip behavior|Use for pixel-style art or crisp marks.|Poor for feathered blending.|s06l01
Color Replacement|Paint|B|Recolors targeted hue while attempting to preserve texture.|Limits; tolerance; sampling|Use for local color tweaks.|Color edges may contaminate nearby objects.|s06l03
Mixer Brush|Paint|B|Simulates mixing and dragging wet pigment.|Wet; Load; Mix; Flow|Use for painterly blending.|High Wet and Mix can smear structure.|s06l06
Clone Stamp|Retouch|S|Copies pixels from an Alt-clicked source.|Aligned; opacity; sample layers|Use for repeatable structural repair.|Repeated sampling creates cloned patterns.|s05l02
Pattern Stamp|Paint|S|Paints a chosen repeating pattern.|Pattern; impressionist; scale|Use for textures and surfaces.|Repetition becomes obvious at large scale.|s06l04
History Brush|History|Y|Paints from a selected earlier history state.|History source; blending; brush options|Use for selective temporary restoration.|Earlier states disappear after document closure.|s06l05
Art History Brush|History|Y|Stylizes painting based on a history state.|Style; Area; Tolerance|Use for painterly variations.|Not a restoration tool for accurate pixels.|s06l05
Eraser|Erase|E|Deletes or reduces pixels or transparency.|Brush mode; opacity; flow|Use when deletion is intended.|Not reversible like a mask after history expires.|s06l05
Background Eraser|Erase|E|Erases background colors based on sampled tone.|Limits; tolerance; sampling|Use for simple high-contrast edge isolation.|Can chew into similar-colored foreground.|s03l04
Magic Eraser|Erase|E|Deletes similar-colored pixels with a click.|Tolerance; contiguous; anti-alias|Use only on simple flat-color backgrounds.|Permanent edge deletion is difficult to revise.|s03l03
Gradient|Fill|G|Draws gradient transition; mode/version behavior varies.|Preset; angle; style; scale|Use for smooth lighting or backgrounds.|A gradient rasterized on source can be destructive.|s06l04
Paint Bucket|Fill|G|Fills contiguous or related pixels with color/pattern.|Tolerance; contiguous; sample layers|Use for flat artwork.|Anti-aliased edge fringe may remain.|s06l04
Blur|Retouch|R|Locally softens pixel details.|Strength; brush size; Sample All Layers|Use sparingly on distracting small edges.|Overuse destroys texture.|s08l07
Sharpen|Retouch|R|Locally increases contrast of fine edges.|Strength; Protect Detail|Use for selective detail emphasis.|Repeated strokes amplify noise.|s08l07
Smudge|Retouch|R|Pushes pixel colors along a stroke.|Strength; Finger Painting|Use for painterly blending.|Often produces smeared photographic details.|s06l06
Dodge|Tone|O|Locally lightens pixels based on tonal range.|Range; exposure; Protect Tones|Use on a duplicate or controlled local task.|Direct painting accumulates destructive changes.|s05l05
Burn|Tone|O|Locally darkens pixels based on tonal range.|Range; exposure; Protect Tones|Use to sculpt contrast carefully.|Can create colored dark patches.|s05l05
Sponge|Tone|O|Locally increases or decreases saturation.|Mode Saturate/Desaturate; flow|Use for isolated color intensity changes.|Strong saturation exaggerates artifact.|s08l03
Pen|Path|P|Draws editable straight and Bézier paths.|Path/Shape mode; path operations|Use for precise contours.|Too many anchors create bumps.|s07l04
Freeform Pen|Path|P|Draws paths by tracing freely.|Curve fit; Magnetic behavior where available|Use with a pen tablet for organic paths.|Automatic points may be hard to edit.|s07l04
Curvature Pen|Path|P|Creates smooth curves by clicking anchors.|Path/Shape mode; anchors|Use for fluid rounded outlines.|Corners require explicit control.|s07l04
Add Anchor Point|Path||Adds a point to editable path.|Path selection; hover location|Use to refine an existing segment.|Too many anchors reduce smoothness.|s07l04
Delete Anchor Point|Path||Removes a point from a path.|Path selection|Simplify overbuilt contours.|Removing critical point alters shape unexpectedly.|s07l04
Convert Point|Path||Converts smooth/corner handles.|Click/drag point behavior|Fix kinks in a Bézier contour.|Can alter neighboring segments.|s07l04
Path Selection|Path|A|Moves or selects whole path components.|Path Operations; multiple path selection|Use to reposition compound shapes.|Different from Direct Selection on anchors.|s07l04
Direct Selection|Path|A|Edits anchors and handles directly.|Anchor and handle editing|Use for precise curve changes.|Moving wrong handle changes curvature.|s07l04
Horizontal Type|Type|T|Creates editable left-to-right text.|Font; size; color; anti-alias|Use for headlines and body text.|Type field focus consumes keyboard shortcuts.|s07l01
Vertical Type|Type|T|Creates text in vertical orientation.|Character; paragraph settings|Use for designs requiring vertical type.|Letter layout may need font-specific care.|s07l01
Horizontal Type Mask|Type|T|Creates a text-shaped selection instead of type layer.|Font; size; tracking|Use for masking typography.|Result is a selection, not editable glyph layer.|s07l01
Vertical Type Mask|Type|T|Creates vertically oriented text selection.|Font; size|Use for special type-shaped selections.|Selection loses editability after deselection unless saved.|s07l01
Rectangle|Shape|U|Draws rectangles as shapes/paths/pixels.|Mode; fill; stroke; corners|Use for containers and precise cards.|Drawing in Pixels mode is destructive to that layer.|s07l03
Rounded Rectangle|Shape|U|Draws rounded rectangles or adjustable corner paths.|Corner radii; stroke; fill|Use for interface cards and labels.|Scaling may change visual corner treatment.|s07l03
Ellipse|Shape|U|Draws ellipse and circle geometry.|Constrain proportions; fill; stroke|Use for icons and circles.|Eyeballed drag may not be circular.|s07l03
Triangle|Shape|U|Draws triangle vector geometry.|Corner controls; fill|Use for arrows and symbols.|Angle choices affect alignment.|s07l03
Polygon|Shape|U|Creates regular multi-sided paths.|Sides; radius; corner controls|Use for geometric badges.|Too many sides can become inefficient.|s07l03
Line|Shape|U|Draws straight lines with configurable appearance.|Weight; fill; stroke; arrowheads if supported|Use for dividers and construction lines.|Very thin strokes may disappear on export.|s07l03
Custom Shape|Shape|U|Draws shapes from a preset library.|Custom Shape picker; fill; stroke|Use for reusable symbols.|Preset availability depends on installed libraries.|s07l03
Hand|View|H|Pans the canvas without moving image content.|Scroll direction; rotate gestures context|Use at high zoom.|View pan does not reposition a layer.|s01l05
Rotate View|View|R|Rotates the canvas view without rotating pixels.|Angle; Reset View|Use for natural brush strokes.|Export remains unaffected by view rotation.|s01l05
Zoom|View|Z|Changes on-screen magnification.|Scrubby Zoom; animated zoom support|Use to assess at 100%.|Zoom cannot create real detail.|s01l05
Color Sampler and measuring tools|Measure||Sample, inspect and annotate image values with grouped measurement tools.|Sample size; info display|Use for calibrated edit checks.|Readout is only as meaningful as chosen profile.|s08l01
'''
FILTERS_RAW=r'''
Gaussian Blur|Blur|Radius|Smooths pixels with Gaussian weighting; blur grows with radius.|Soft backgrounds and feathered shadows|Loses fine detail if applied directly; Smart Filter normally available.|s04l03
Box Blur|Blur|Radius|Averages colors within a rectangular neighborhood.|Stylized flat smoothness|May create boxy edges at high radius.|s08l07
Average|Blur|None|Replaces selected area with its average color.|Determine or generate representative color|Removes all local detail.|s06l03
Blur|Blur|Preset strength|Applies a mild blur.|Tiny softening|Repeated destructive use stacks loss.|s08l07
Blur More|Blur|Preset strength|Applies stronger standard blur.|Quick broad softening|Less controllable than Gaussian Blur.|s08l07
Motion Blur|Blur|Angle; Distance|Blurs along a line, suggesting motion.|Motion trails and effects|Wrong angle contradicts movement.|s09l04
Radial Blur|Blur|Amount; Blur Method; Quality|Blurs outward or in rotation from a center.|Speed or rotational effects|Center and quality need previewing.|s09l04
Lens Blur|Blur|Blur amount; depth map; iris controls|Simulates defocus using depth information.|Depth-of-field effects|Adobe lists 16/32-bit compatibility limits; check mode.|s09l04
Smart Blur|Blur|Radius; Threshold; Quality|Blurs within similar-color regions while attempting to retain edges.|Flattening noise in graphics|Can create unnatural smooth regions.|s08l07
Surface Blur|Blur|Radius; Threshold|Smooths areas while preserving some edges.|Subtle surface corrections|High thresholds erase texture.|s05l04
Field Blur|Blur Gallery|Blur pins; amount|Blurs by spatial pins with adjustable strength.|Depth progression|GPU capability may affect availability.|s09l04
Iris Blur|Blur Gallery|Iris shape; blur; feather|Creates localized depth-of-field approximation.|Portrait or product focal emphasis|Fake falloff if geometry conflicts.|s09l04
Tilt-Shift|Blur Gallery|Blur bands; transition; distortion|Simulates plane of focus and miniature aesthetic.|Architectural miniatures|Strong use makes full scene toy-like.|s09l04
Path Blur|Blur Gallery|Path; speed; shape|Blurs along specified curved motion paths.|Stylized motion streaks|Wrong path looks physically implausible.|s09l04
Spin Blur|Blur Gallery|Ellipse; blur angle|Simulates object rotation motion.|Wheels and circular objects|Center misalignment creates wobble.|s09l04
Unsharp Mask|Sharpen|Amount; Radius; Threshold|Adds contrast along transitions to create sharpness impression.|Output sharpening|Causes halos at high Amount/Radius.|s08l07
Smart Sharpen|Sharpen|Amount; Radius; Reduce Noise; Shadow/Highlight|Selective algorithmic sharpening with detailed controls.|Precise sharpening|Cannot fully recover badly blurred source information.|s08l07
Sharpen|Sharpen|Preset|Simple sharpening pass.|Minor quick contrast increase|Stacked passes magnify noise.|s08l07
Sharpen More|Sharpen|Preset|Stronger automatic sharpening.|Strong stylized edges|Often excessive for natural photos.|s08l07
Sharpen Edges|Sharpen|Preset|Emphasizes localized edges.|Linework|Bit-depth restrictions according to Adobe reference.|s08l07
Shake Reduction|Sharpen|Settings vary by availability|Legacy motion restoration option; do not assume present in 27.11.|Historical tutorial context|Availability not independently confirmed; not a recommended current workflow.|s08l07
Add Noise|Noise|Amount; Distribution; Monochromatic|Adds random pixel variations.|Grain matching in composites|Strong noise worsens compression.|s09l06
Reduce Noise|Noise|Strength; Preserve Details; Reduce Color Noise|Smooths luminance/color noise.|High ISO image cleanup|Blurs small features at strong settings.|s08l07
Dust & Scratches|Noise|Radius; Threshold|Blurs small defects based on radius and threshold.|Scanned image scratches|Softens small true details.|s05l06
Median|Noise|Radius|Replaces pixels based on neighborhood median.|Salt-and-pepper noise|Smooths small fine lines.|s05l06
Despeckle|Noise|Preset|Suppresses speckled transitions.|Quick noise treatment|Less control than dedicated reduction.|s08l07
Displace|Distort|Horizontal/Vertical scale; map; edges|Moves pixels using grayscale map.|Fabric and surface mockups|Needs separate appropriate PSD displacement map.|s09l05
Ripple|Distort|Amount; Size|Creates short waterlike wavy displacement.|Water or stylized glass|Strong values break straight geometry.|s09l05
Wave|Distort|Generators; wavelength; amplitude|Creates periodic distortions.|Abstract wave effects|Regularity becomes visibly artificial.|s09l05
ZigZag|Distort|Amount; Ridges; Style|Distorts pixels radially like ripples.|Water drops and rings|Avoid on faces and text.|s09l05
Twirl|Distort|Angle|Rotates pixels increasingly toward center.|Abstract swirls|Can twist edges unnaturally.|s09l05
Spherize|Distort|Amount; Mode|Bulges or pinches image in region.|Lens-like sphere effects|Stretched details appear near edge.|s09l05
Pinch|Distort|Amount|Compresses or expands local image area.|Stylized warps|Can damage straight geometry.|s09l05
Polar Coordinates|Distort|Rectangular/Polar conversion|Maps rectangular layout into circular coordinates or back.|Panoramic little-planet studies|Seam placement matters.|s09l05
Shear|Distort|Curve control points; edge handling|Displaces image horizontally along a path.|Wavy surfaces|Edge repeat/undefined choices can show seams.|s09l05
Glass|Filter Gallery / Distort|Distortion; Smoothness; Texture|Creates rippled refractive surface.|Window glass stylization|Not a physics-based refractive renderer.|s09l05
Ocean Ripple|Filter Gallery / Distort|Ripple Size; Magnitude|Simulates ripple-like distortion.|Water textures|Low resolution source may pixelate.|s09l05
Diffuse Glow|Filter Gallery / Distort|Graininess; Glow Amount; Clear Amount|Adds pale glowing grain around subject.|Dreamlike highlights|Can flatten tonal range.|s09l05
Liquify|Special|Brush size; pressure; mesh|Warps geometry with specialized tools.|Shape adjustments and effects|GPU/mode limitations; identity ethics matter.|s05l05
Perspective Warp|Special|Layout; Warp pins/planes|Reorients planar content in perspective.|Architecture integration|Hard with nonplanar subjects.|s05l05
Camera Raw Filter|Special|Basic; Color Mixer; Detail; Masking|Runs Camera Raw adjustments on rendered pixels.|Consistent color and tone controls|Adobe documents 8/16-bit support for this filter.|s08l04
Lens Correction|Special|Distortion; Vignette; Chromatic Aberration|Compensates for lens artifacts.|Architectural/RAW lens cleanup|Profile support depends on lens metadata.|s08l04
Vanishing Point|Special|Perspective plane; Clone/Transform|Edits pixels respecting drawn planar perspective.|Wall and packaging mockups|Inaccurate plane causes stretching.|s09l05
High Pass|Other|Radius|Keeps high-frequency edges while suppressing low-frequency tone.|Frequency/detail composites|Can introduce halos when blended strongly.|s09l06
Maximum|Other|Radius; Preserve|Expands brighter regions.|Mask edge morphology|Can eliminate tiny dark detail.|s03l04
Minimum|Other|Radius; Preserve|Expands darker regions.|Mask choke or erosion depending on mask convention|Can destroy fine light structure.|s03l04
Offset|Other|Horizontal/Vertical; edge mode|Rolls or offsets pixel locations.|Seamless texture evaluation|Wrap Around needs periodic content to hide seams.|s06l04
Color Halftone|Pixelate|Max Radius; channel angles|Simulates printed halftone dots.|Retro print aesthetics|Fine lines may moiré on downsizing.|s07l06
Mosaic|Pixelate|Cell Size|Converts nearby pixels to colored blocks.|Pixelation and concealment effects|Not suitable as secure anonymization.|s06l06
Crystallize|Pixelate|Cell Size|Builds polygonal color cells.|Geometric texture|Large cells remove scene readability.|s06l06
Mezzotint|Pixelate|Type|Creates mottled or lined tonal noise.|Print-styled graphics|Can overwhelm detail.|s06l06
Pointillize|Pixelate|Cell Size|Renders scene with colored dots.|Pointillist illustration|Holes expose lower content/background.|s06l06
Fragment|Pixelate|Preset|Offsets and softens duplicate pixel fragments.|Soft fragmented effect|Limited parameter control.|s06l06
Clouds|Render|Foreground/Background color|Synthesizes a cloudy pattern.|Atmospheric texture masks|Default result depends on current colors.|s06l04
Difference Clouds|Render|Foreground/Background color|Combines cloud-like random fields.|Texture variation|Repeated use changes unpredictably.|s06l04
Fibers|Render|Variance; Strength|Generates streaked fibrous texture.|Wood/fabric bases|Artificial regularity at full scale.|s06l04
Lens Flare|Render|Brightness; Lens Type; position|Adds simulated bright lens artifacts.|Stylized highlights|Easy to make light direction inconsistent.|s09l02
Tree|Render|Tree type; foliage and branch options|Generates procedural trees where installed.|Background illustration elements|Needs version and bit-depth compatibility test.|s09l04
Flame|Render|Flame type; length; width|Generates stylized flames along paths where supported.|Graphic fire accents|Depends on a valid path and tool availability.|s09l04
Oil Paint|Stylize|Stylization; Cleanliness; Scale; lighting|Creates painterly surface and brushwork.|Artistic paintings|Requires supported GPU features for some systems.|s06l06
Emboss|Stylize|Angle; Height; Amount|Renders apparent raised relief.|Texture maps|Alters normal tonal appearance.|s07l03
Find Edges|Stylize|Preset|Maps intensity transitions into edge traces.|Sketch effects|Noise may create too many edges.|s06l06
Glowing Edges|Filter Gallery / Stylize|Edge Width; Brightness; Smoothness|Renders colored luminous edges.|Neon-like effects|Fine noise can glow undesirably.|s09l06
Wind|Stylize|Method; Direction|Creates horizontal streaks.|Speed and stylized typography|May require layer rotation for other angles.|s09l06
Solarize|Stylize|Preset|Partially inverts bright tones.|Experimental tone design|Little tonal control.|s08l03
Poster Edges|Filter Gallery / Artistic|Edge Thickness; Intensity; Posterization|Simplifies and darkens graphic boundaries.|Comic/painterly look|Loses photorealism quickly.|s06l06
Cutout|Filter Gallery / Artistic|Number of Levels; Edge Simplicity; Fidelity|Reduces image to flat-tone regions.|Paper-cut look|Small details disappear.|s06l06
Colored Pencil|Filter Gallery / Artistic|Pencil Width; Stroke Pressure; Paper Brightness|Simulates pencil-on-paper texture.|Illustrative textures|Paper settings strongly affect color.|s06l06
Watercolor|Filter Gallery / Artistic|Brush Detail; Shadow Intensity; Texture|Simulates watercolor wash edges.|Painterly graphics|Often muddy on low contrast art.|s06l06
Dry Brush|Filter Gallery / Artistic|Brush Size; Detail; Texture|Creates dry-brush strokes.|Poster illustration|Text may become unreadable.|s06l06
Film Grain|Filter Gallery / Artistic|Grain; Highlight/Intensity|Adds stylized film-like grain.|Retro looks|Different from sensor noise modeling.|s08l07
Accented Edges|Filter Gallery / Brush Strokes|Edge Width; Brightness; Smoothness|Emphasizes brushy boundaries.|Graphic edge effects|Too much creates hard outlines.|s06l06
Crosshatch|Filter Gallery / Brush Strokes|Stroke Length; Sharpness; Strength|Simulates crossing drawn strokes.|Hatched illustrations|Can obscure small subject details.|s06l06
Bas Relief|Filter Gallery / Sketch|Detail; Smoothness; Light|Makes light-dark relief-like shading.|Engraving effects|FG/BG colors change the result.|s06l06
Chalk & Charcoal|Filter Gallery / Sketch|Charcoal Area; Chalk Area; Stroke Pressure|Simulates chalk and charcoal.|Hand-drawn rendering|Reduced color fidelity intentional.|s06l06
Grain|Filter Gallery / Texture|Intensity; Contrast; Grain Type|Adds textured grain patterns.|Surface texture|Oversized grain hurts readability.|s06l06
Texturizer|Filter Gallery / Texture|Texture; Scaling; Relief; Light|Embosses surface texture.|Paper and canvas mockups|Lighting direction may conflict with photo.|s09l05
Craquelure|Filter Gallery / Texture|Crack Spacing; Depth; Brightness|Creates cracked surface texture.|Aged-paint simulation|Unrealistic when applied uniformly.|s05l06
Neural Filters|Neural / AI|Per-filter settings; cloud vs downloaded status|A category of ML-assisted edits; each filter has separate availability.|Explore targeted ML treatments|Some require download, online processing or are Beta; verify in app.|s11l06
AI Sharpen (Topaz)|AI partner|MP output; service action|Credit-consuming generative sharpen feature documented in 2026.|Damaged or soft photos with disclosure|Adobe notes direct current-layer update; test on a copy.|s08l07
AI Denoise (Topaz)|AI partner|MP output; service action|Credit-consuming generative noise reduction documented in 2026.|High-noise imagery requiring extra recovery|Adobe notes current-layer update; not a general offline filter.|s08l07
'''

# Conservatively selected Windows default shortcuts (dialog may be customized).
SHORTCUTS_RAW=r'''
File|New document|Ctrl+N|Global|Default application shortcut; verify after customization
File|Open file|Ctrl+O|Global|Opens standard file picker
File|Save|Ctrl+S|Global|Dialog differs for new documents
File|Save As|Ctrl+Shift+S|Global|Save route can depend on format and modern save settings
File|Print|Ctrl+P|Global|Printer availability varies
File|Close document|Ctrl+W|Document|Prompts if unsaved
File|Close all documents|Ctrl+Alt+W|Document|Verify in customized menu
File|Undo|Ctrl+Z|Document|Undo action in editing context; text inputs can consume it
File|Step backward|Ctrl+Alt+Z|History|History behavior depends on state
File|Step forward|Ctrl+Shift+Z|History|Redo behavior depends on state
Interface|Preferences|Ctrl+K|Global|General preferences in Windows
Interface|Keyboard Shortcuts dialog|Ctrl+Alt+Shift+K|Global|Adobe documented
Interface|Show/hide panels|Tab|Workspace|While not typing in a field
Interface|Show/hide side panels|Shift+Tab|Workspace|While not typing in a field
Interface|Rulers|Ctrl+R|Document|View overlay only
Interface|Hide/show extras|Ctrl+H|Document|May affect guides/selection edges
Interface|Grid|Ctrl+'|Document|Depends on keyboard layout and shortcut settings
View|Fit on Screen|Ctrl+0|Document|View-only
View|Actual Pixels 100%|Ctrl+1|Document|View-only
View|Zoom in|Ctrl++|Document|May require key-layout adaptation
View|Zoom out|Ctrl+-|Document|View-only
View|Zoom tool|Z|Tool|Only when no text field captures keystroke
View|Hand tool|H|Tool|Only when no text field captures keystroke
View|Temporary Hand|Space|Tool gesture|Hold while using many tools; conflicts with text entry
View|Rotate View|R|Tool|May be grouped by tool configuration
Layers|New layer|Ctrl+Shift+N|Document|Opens naming dialog
Layers|Duplicate layer|Ctrl+J|Layer|Also copies an active selection onto a new layer
Layers|Group selected layers|Ctrl+G|Layers panel|Selection-dependent
Layers|Ungroup layers|Ctrl+Shift+G|Layers panel|Group-selection-dependent
Layers|Free Transform|Ctrl+T|Document|Active editable content required
Layers|Transform again|Ctrl+Shift+T|Document|Availability depends on recent transform
Layers|New layer via copy|Ctrl+J|Selection/layer|Same key changes scope with active selection
Selection|Select All|Ctrl+A|Document|Selects entire active canvas
Selection|Deselect|Ctrl+D|Document|Requires active selection for visible effect
Selection|Reselect|Ctrl+Shift+D|Document|Last selection state needed
Selection|Inverse selection|Ctrl+Shift+I|Document|Active selection needed
Selection|Quick Mask toggle|Q|Tool/selection|Keyboard focus must be outside text
Selection|Marquee family|M|Tool|Shift+M may cycle group if configured
Selection|Lasso family|L|Tool|Shift+L may cycle group if configured
Selection|Selection family|W|Tool|Group member varies by toolbar
Tools|Move|V|Tool|Auto-select may change target layer
Tools|Crop|C|Tool|Tool family includes other grouped tools
Tools|Eyedropper|I|Tool|May cycle measurement tools
Tools|Spot Healing family|J|Tool|Group member varies
Tools|Brush|B|Tool|Can cycle Pencil etc. depending on settings
Tools|Clone Stamp|S|Tool|Group member varies
Tools|History Brush|Y|Tool|Depends on available history state
Tools|Eraser|E|Tool|Destructive on raster layer
Tools|Gradient|G|Tool|May share Paint Bucket
Tools|Blur/Sharpen/Smudge|R|Tool|Grouped tools may cycle
Tools|Dodge/Burn/Sponge|O|Tool|Grouped tools may cycle
Tools|Pen|P|Tool|Mode (Path/Shape) must be checked
Tools|Type|T|Tool|Text caret captures other shortcuts when editing
Tools|Path/Direct Selection|A|Tool|Selected subtool may vary
Tools|Shape|U|Tool|Shape mode/Path/Pixels determines results
Paint|Default black/white colors|D|Tool|Foreground/background swatches
Paint|Swap foreground/background|X|Tool|Useful when painting masks
Paint|Increase brush size|]|Brush tool|Keyboard focus and layout dependent
Paint|Decrease brush size|[|Brush tool|Keyboard focus and layout dependent
Paint|Increase brush hardness|Shift+]|Brush tool|Brush-dependent
Paint|Decrease brush hardness|Shift+[|Brush tool|Brush-dependent
Paint|Fill foreground|Alt+Backspace|Pixel/edit context|May fill selection or active pixels
Paint|Fill background|Ctrl+Backspace|Pixel/edit context|May fill selection or active pixels
Paint|Brush temporary eyedropper|Alt (hold)|Brush gesture|Context-dependent sampling
View|Cycle screen modes|F|Document|May conflict with text entry
View|Full screen menus varies|F|Document|Cycles interface presentation
Text|Commit type / exit field|Ctrl+Enter|Type editing|Behavior depends on active text context
Text|Cancel text changes|Esc|Type editing|May exit or cancel depending on state
Reference|Open Photoshop Help/Discover|Ctrl+F|Global|Discover in supported versions; app-search not website search
'''

GLOSSARY_RAW=r'''
Pixel|Smallest addressable raster sample; a color/alpha value at a grid coordinate.|s01l01
Raster|Image stored as an array of samples rather than mathematical objects.|s01l01
Vector|Geometry encoded by points, paths and equations, rendered to pixels for display.|s01l01
Resolution|Context-dependent amount of detail, commonly pixel dimensions or PPI.|s01l02
PPI|Pixels per inch in intended output; does not by itself create detail.|s01l02
DPI|Dots per inch of printing hardware; not interchangeable with image PPI.|s01l02
Resampling|Computing a new pixel grid at different dimensions.|s01l02
Interpolation|Estimating sample values between original samples.|s01l02
Canvas|Document's finite coordinate area.|s02l01
Crop|Changes visible frame and potentially removes outside pixels.|s02l01
Canvas Size|Command expanding or contracting document bounds without image resampling.|s02l01
Image Size|Command to change dimensions/resolution and optionally resample.|s02l01
Layer|Independently composited source of pixels, type, shape or adjustment.|s02l02
Stacking order|Front-to-back sequence determining occlusion/composite result.|s02l02
Group|Container organizing related layers.|s02l02
Opacity|Factor controlling the visibility of a layer or effect.|s04l04
Fill|Layer interior visibility setting distinct from overall Opacity when effects are used.|s04l04
Alpha|Opacity or coverage value stored per pixel or as a channel.|s02l04
Transparency|Partial or total absence of opacity in compositing.|s02l04
Checkerboard|UI visualization of transparent areas, not source pixels.|s02l04
PSD|Native layered Photoshop document format.|s01l03
PSB|Large Document Format for documents exceeding PSD practical limits.|s11l05
JPEG|Lossy photographic compression; generally flattened, with no alpha.|s01l03
PNG|Raster format supporting alpha transparency; not a full PSD replacement.|s02l04
TIFF|Flexible raster exchange and archival format, often supporting higher bit depths.|s01l03
WebP|Modern image format supporting efficient compression and optional transparency.|s10l04
RAW|Camera sensor-derived source data needing development rather than fixed rendering.|s08l04
DNG|Digital Negative raw container/specification supported by Camera Raw.|s08l04
XMP sidecar|Metadata file containing develop settings for some raw workflows.|s08l04
Selection|Temporary per-pixel editing coverage field.|s03l01
Marching ants|Animated boundary depicting part of a selection threshold.|s03l01
Feather|Softens selection or mask edge transition.|s03l04
Anti-aliasing|Blends edge pixels to reduce jagged contour appearance.|s03l04
Tolerance|Threshold controlling similarity in some selection/fill tools.|s03l02
Color Range|Selection from color similarity and fuzziness rather than just geometric area.|s03l02
Quick Mask|Temporary view/edit mode showing selection coverage as mask.|s03l05
Layer mask|Grayscale visibility control attached to a layer.|s03l03
Vector mask|Visibility boundary generated from editable path geometry.|s03l06
Clipping mask|Upper layer constrained by transparency of lower base layer.|s03l06
Alpha channel|Grayscale auxiliary channel that can store selection data.|s03l05
Composite channel|Combined color display assembled from component channels.|s08l02
RGB|Red/green/blue additive-color channel model.|s08l05
CMYK|Cyan/magenta/yellow/key print-separation channel model.|s08l05
Lab|Color model separating lightness from two opponent chromatic axes.|s08l05
Grayscale|Single-intensity color mode without normal chromatic channel variation.|s08l05
ICC profile|Data interpreting color numbers for a specific color space/device process.|s08l05
Embedded profile|Color profile stored in a file for correct interpretation.|s08l05
Assign Profile|Reinterprets existing color numbers under a new profile, potentially changing appearance.|s08l05
Convert to Profile|Changes channel values to retain approximate appearance under another profile.|s08l05
Working space|Color space used for editing or interpreting untagged data under settings.|s08l05
Gamut|Range of colors representable by a device or space.|s08l06
Soft proof|On-screen simulation of output profile under calibrated conditions.|s08l06
Rendering intent|Rule for mapping out-of-gamut colors during conversion.|s08l06
Bit depth|Number of binary bits per color component defining precision/range.|s08l05
8-bit/channel|Usually 256 encoded values per channel in integer representation.|s08l05
16-bit/channel|Higher-precision channel representation useful for smooth corrections.|s08l05
32-bit/channel|Floating-point precision often used for HDR workflows.|s08l07
HDR|High dynamic range content or representation with extended luminance information.|s08l07
Histogram|Count of image pixels by channel or tonal interval.|s08l01
Exposure|Amount of image brightness associated with captured or interpreted light.|s08l01
White balance|Correction for color cast from illumination or camera setting.|s08l03
Clipping|Loss of differentiable highlight/shadow color values after limits are hit.|s08l01
Black point|Input or output value mapped to deepest intended tone.|s08l01
White point|Input or output value mapped to brightest intended tone.|s08l01
Levels|Tonal mapping through black, mid and white controls.|s08l01
Curves|Arbitrary control-point mapping of input to output tones.|s08l02
S-curve|Curve raising highlights and lowering shadows to increase contrast.|s08l02
Color grading|Intentional global/local color style beyond basic neutrality.|s08l03
HSL|Hue, saturation and lightness descriptors for color adjustment.|s08l03
Hue|Perceived color family or angle in color models.|s08l03
Saturation|Color intensity relative to gray at comparable lightness.|s08l03
Luminance|Light-related intensity measure; specific meaning depends on space.|s08l03
Smart Object|Container retaining source content for transforms and supported smart filters.|s04l02
Embedded Smart Object|Smart Object source stored inside PSD.|s04l02
Linked Smart Object|Smart Object whose source is an external file.|s04l02
Smart Filter|Editable supported filter attached to a Smart Object.|s04l03
Filter mask|Grayscale control of combined Smart Filter influence.|s04l03
Adjustment layer|Non-destructive computed tone/color adjustment over underlying pixels.|s04l01
Blend mode|Rule mathematically combining layer and underlying image color values.|s04l04
Multiply|Blend mode tending to darken through channel multiplication.|s04l04
Screen|Blend mode tending to brighten through inverse multiplicative math.|s04l04
Overlay|Contrast blend mode combining Multiply/Screen behavior conditionally.|s04l04
Blend If|Layer Style threshold-based visibility using tonal ranges.|s04l05
Layer Style|Live appearance effects such as Stroke, Shadow and Glow.|s02l05
Drop Shadow|Layer effect producing offset shadow based on layer contours.|s02l05
Stroke|Visible line placed around a vector path or layer boundary.|s02l05
Transform|Geometric change such as scale, rotate, warp or skew.|s02l03
Free Transform|General handles-based transform workflow.|s02l03
Perspective|Projection geometry causing parallel 3D lines to converge in image.|s09l01
Vanishing point|Projected location where parallel scene lines appear to meet.|s09l01
Horizon|Camera eye-level reference in perspective geometry.|s09l01
Contact shadow|Darkening immediately beneath contact where light is blocked.|s09l02
Cast shadow|Shadow projected onto a separate surface by an object blocking light.|s09l02
Atmospheric perspective|Reduced distant contrast and possible color shift from air scattering.|s09l04
Depth of field|Range of subject distances appearing acceptably sharp.|s09l04
Gaussian Blur|Spatial smoothing weighted by Gaussian distribution.|s04l03
Unsharp Mask|Edge-contrast sharpening with controls Amount, Radius and Threshold.|s08l07
Halo|Unnatural light or dark band around an edge from edits or masking.|s09l03
Noise|Unpredictable pixel variations from capture, processing or synthesis.|s08l07
Denoise|Reduction of noise, often at some fine-detail cost.|s08l07
Texture|Small repeating or stochastic image detail.|s05l01
Healing|Retouch method matching borrowed texture with target surroundings.|s05l01
Cloning|Direct copying of pixels from source to target.|s05l02
Content-Aware Fill|Synthesizes replacement pixels using analyzed neighborhood information.|s05l03
Remove Tool|Photoshop retouch brush for inferred removal, with model-dependent processing.|s05l03
Frequency separation|Technique operating on different spatial scales of image detail.|s09l06
Dodge|Local brightening operation.|s05l05
Burn|Local darkening operation.|s05l05
Liquify|Specialized image geometry warp interface.|s05l05
Brush opacity|Maximum contribution of brush stroke across area.|s06l01
Brush flow|Rate of paint deposition during a stroke.|s06l01
Hardness|Softness of a brush tip edge.|s06l01
Smoothing|Pointer path stabilization for brush strokes.|s06l02
Pen pressure|Stylus force data used for brush dynamics on supported tablets.|s06l02
Gradient|Continuous transition between colors or opacity levels.|s06l04
Pattern|Tiled repeated image or fill design.|s06l04
Foreground color|Current primary painting/fill color.|s06l03
Swatch|Saved color for repeated access.|s06l03
Path|Editable geometric contour defined by anchors and segments.|s07l04
Anchor point|Path control point that defines contour position.|s07l04
Bézier handle|Direction vector influencing tangent and curvature of path segment.|s07l04
Point type|Text entered at single click origin, extending with text.|s07l01
Paragraph type|Text flowing inside a sized bounding box.|s07l01
Kerning|Spacing adjustment for a particular glyph pair.|s07l02
Tracking|Overall spacing across selected glyphs.|s07l02
Leading|Distance from one line baseline to the next.|s07l02
Glyph|Specific drawn appearance of a character in font.|s07l02
Anti-aliased type|Rasterized glyph edges smoothed by partial pixel coverage.|s07l01
Dynamic Text|Recent feature extending text layout along shapes/paths; availability version-specific.|s07l05
Actions|Recorded command sequences replayable in Photoshop.|s10l02
Batch|Automatic operation across a set of source files.|s10l02
UXP|Modern Photoshop plugin extensibility platform.|s10l04
Export As|Asset-oriented export dialog distinct from editable Save As.|s10l05
Preflight|Structured verification of outputs against recipient technical requirements.|s10l06
Scratch disk|Drive space used by Photoshop for temporary working data.|s11l01
GPU|Graphics processor accelerating compatible display and image operations.|s11l01
DirectX|Windows graphics API used to describe supported GPU feature levels.|s11l02
VRAM|Graphics memory available to GPU features.|s11l02
Virtual GPU|Graphics adapter presented by virtualization host to guest system.|s11l02
PCIe passthrough|Advanced technique assigning physical hardware directly to a guest where supported.|s11l02
Preferences|Application configuration settings, distinct from document data.|s01l04
Workspace|Stored UI panel arrangement.|s01l04
History state|Session snapshot of editing actions, not permanent backup.|s01l06
Generative credits|Plan-based metering of certain Adobe and partner AI operations.|s11l06
Generative Fill|Prompt-based image insertion/removal/replacement using supported generative service.|s11l06
On-device model|ML model running locally after installation and hardware checks.|s11l06
Beta|Pre-release feature/channel not to be assumed stable or permanent.|s11l06
LTS|Long-term-support release branch with extended security/maintenance policy.|s11l06
'''

TROUBLE_RAW=r'''
Photoshop won't launch|Outdated driver; corrupt preferences; plugin fault; unsupported Windows build|Check Help/Creative Cloud version and Windows Event Viewer; launch without optional plugins; test fresh user settings|Update to compatible driver and supported OS; preserve settings before reset|Do not delete the only preference backup|s11l03
Scratch disks are full|Insufficient free storage; huge temporary documents|Inspect free internal SSD space and scratch preference assignments|Free disk safely after closing Photoshop; add suitable SSD scratch disk|Do not manually delete active Photoshop scratch files|s11l01
GPU unavailable or grayed out|Unsupported DX12 feature level; VM virtual adapter; driver issue|Help > System Info and Device Manager > Display adapters|Install vendor driver or provide supported GPU to guest; accept feature limits if not possible|Do not assume host GPU is visible inside VM|s11l02
Blur Gallery / Oil Paint missing|GPU unsupported, color depth/mode incompatible|Edit > Preferences > Performance and Image > Mode|Enable suitable GPU and test supported mode after saving copy|Converting bit depth can change image precision|s11l01
Camera Raw Filter disabled|Unsupported bit depth or layer type|Image > Mode; selected layer properties|Try supported 8/16-bit copy and suitable Smart Object|Preserve 32-bit HDR original|s08l04
Generative Fill gray|Missing selection; unsupported RGB/bit depth; login or internet/credits|Check mode, layer, selection, account connectivity|Use supported RGB 8-bit workflow and verify plan entitlement|Do not bypass cloud/account restrictions|s11l06
Remove Tool fails|Unsupported on-device model; networking; GPU; source complexity|Check model selection, installed state and image mode|Select compatible processing and refine with healing/cloning|Inferred replacement may alter scene facts|s05l03
Brush paints nothing|Wrong layer/mask; hidden layer; zero flow/opacity; selection active|Inspect layer thumbnail and brush controls; Ctrl+D if unintended selection|Choose correct editable target, set opacity/flow, unlock|Avoid accidental painting on master|s06l01
Layer won't move|Locked layer; wrong target; auto-select settings|Inspect layer lock and Layers selection|Unlock permitted layers and select correct layer|Do not flatten merely to enable move|s02l03
Cannot select subject accurately|Weak contrast; motion blur; transparency and hair|Inspect at 100% on light/dark backgrounds|Combine Object Selection with Select and Mask and local brush refinements|Do not claim perfect AI edge in all lighting|s03l04
Mask shows black or white unexpectedly|Selected mask thumbnail; inverted mask; wrong brush color|Alt-click mask and inspect white/black coverage|Press D/X for default and swap colors; Ctrl+I deliberately only when appropriate|Do not delete hidden source pixels|s03l03
Export has white background|Opaque layer still visible; wrong format; transparency disabled|Hide all background layers and inspect checkerboard|Export PNG with transparency, retest in viewer|JPEG does not store transparency|s02l04
PNG edges have halos|Selection fringe; premultiplication; matte mismatch|View over dark and bright test layers|Refine mask and decontaminate only as needed|Strong feather can worsen fringing|s09l03
Text font missing|Font not installed/licensed; creative cloud sync|Inspect Type warning and Character panel font|Install licensed font or intentionally substitute and reflow|Do not redistribute restricted fonts|s11l04
Text wraps differently|Missing font, differing tracking or bounding box|Check exact font, Paragraph width and Character settings|Use installed font and fixed style guide|Do not rasterize master just to conceal issue|s07l02
Shortcut types into field|Focus is in text input; custom shortcuts|Press Esc/click away; inspect Edit > Keyboard Shortcuts|Exit active text field then retry|Key mappings differ if customized|s01l04
Ctrl+Z behaves differently|Text field focus; undo/redo context|Inspect History panel and active caret|Exit field and test known document operation|Undo buffer isn't a backup|s01l06
Colors look different in viewer|Profile missing; uncalibrated display; unmanaged app|Check embedded ICC and proof view; compare in color-managed viewer|Convert with correct profile, embed it on export as supported|Assigning arbitrary profile may distort appearance|s08l05
Print too dark|Screen brightness; missing output profile; uncalibrated printer|Review soft proof and test print with printer/paper ICC|Calibrate monitor and use correct output workflow|No universal one-click print fix|s08l06
Gradients show banding|8-bit quantization; aggressive stretch; export artifacts|Inspect at 100% in PSD then final export|Work at higher precision when appropriate; add modest dither/noise|Some delivery formats reintroduce banding|s06l04
Large PSD slow|Memory/scratch pressure; excessive layers; high pixel count|Inspect Photoshop Performance and Windows Task Manager|Use organized Smart Objects, adequate RAM and SSD scratch|Flatten only a delivery copy|s11l05
PSD too large to save|Exceeds PSD limits|Review dimensions and file size|Use PSB if receiver supports it|PSB acceptance varies by downstream application|s11l05
Linked files missing|Paths moved or omitted from handoff|Inspect layer link warning and project folder|Relink to shipped source files and re-save copy|Do not send only PSD if links remain external|s10l01
Corrupt file|Interrupted write; storage trouble; plugin problem|Try earlier versioned files and verified backups|Restore known-good copy and investigate storage|Never overwrite last working revision|s11l05
Photoshop in VM very slow|No passed GPU; low RAM/vRAM; disk I/O|Inspect guest GPU capabilities and scratch location|Allocate adequate guest resources, test appropriate hypervisor GPU features|Official host spec is not a VM guarantee|s11l02
Cloud feature unavailable offline|Requires sign-in, credits, cloud request|Check service docs and account; disconnect only for safe test|Use manual masking, heal, clone and local adjustment tools|Offline manual is not offline AI service|s11l06
Export size wrong|Resampling settings, ratio, artboard bounds|Inspect File > Export > Export As preview dimensions|Set explicit dimensions and verify exported pixel size|Print PPI != pixel count|s10l05
Smart Filter missing|Layer wasn't Smart Object or operation not supported|Inspect filter target and layer icon|Convert eligible layer before filter; confirm smart compatibility|Not every filter is smart-compatible|s04l03
Over-sharpened edges|Amount/Radius too strong; repeated sharpening|Inspect at 100% against original|Lower sharpening and apply after final resize|Halos cannot create authentic detail|s08l07
Automated batch overwrites files|Save path recorded; filename collision|Test one input and output folder before batch|Use separate destination and unique naming|Always preserve originals outside destination|s10l02
'''

RECIPES_RAW=r'''
Remove a simple solid-color background|s03l02,s03l03|Select background with Magic Wand or Color Range; inspect tolerance; add layer mask; refine at 100%; export PNG with alpha.|Transparent PNG with no obvious fringes.
Extract hair against mixed tones|s03l04,s03l03|Select subject roughly; enter Select and Mask; check dark/light previews; use edge refinement cautiously; output New Layer with Mask; test on two backdrops.|No prominent halo or lost major strands.
Replace a sky without flattening|s03l03,s04l02,s09l03|Duplicate source; mask the sky; place replacement beneath; match horizon and exposure using clipped Curves; inspect tree edges.|Sky change can be undone by turning off replacement.
Restore a clipped logo edge|s03l06,s07l04|Trace Pen path with few anchors; form vector mask; adjust handles at 200%; evaluate final-size export.|Sharp smooth edge without stair-step trace.
Make a circular profile image|s03l01,s03l03|Make elliptical selection; apply Reveal Selection mask; center portrait; export transparent PNG.|Correct circular alpha boundary.
Brighten only a face|s04l01,s05l05|Add Curves brighten layer; invert mask; soft-white low-opacity paint on face; compare before/after.|Background retains original exposure.
Remove a small blemish|s05l01|Make blank cleanup layer; sample all layers; paint just over defect with Spot Healing; examine at 100%.|Texture continuous and source unchanged.
Clone a scratch across repeated texture|s05l02|Sample near defect with Alt-click; clone short segments while frequently resampling; check for repeated motifs.|Scratch invisible without repetitive patches.
Rebuild damaged image corner|s05l06,s05l02|Save archival copy; select good similar region; clone geometric structure on new layer; document inference; blend tone.|Corner improved and reconstruction documented.
Remove a cable from wall|s05l03,s05l02|Paint cable using Remove; inspect texture and vertical lines; fix repetitions with Clone/Healing; save editable layer.|No duplicate wall details.
Retouch skin without waxy blur|s05l04,s05l05|Heal isolated marks; dodge/burn subtle uneven tone on Curves masks; inspect pores at 100%.|Texture remains natural.
Make a realistic contact shadow|s09l02,s04l03|Paint tight dark mark directly under object; separate softer longer shadow; blur on Smart Object; reduce opacity.|Subject visually rests on floor.
Match lighting on a cutout|s09l01,s09l03|Identify light direction; clip Curves and Color Balance to subject; refine masked edge; compare black point.|Subject and scene share illumination logic.
Create fake atmospheric depth|s09l04|Place distant objects in separate group; mask pale fog layer to distance; reduce distant contrast and blur slightly.|Foreground stays crisp and distance recedes.
Make a glass-style highlight|s04l04,s09l02|Paint small controlled highlight on separate Screen layer; mask edges to shape; soften one side; align to scene light.|Highlight reinforces form without milky haze.
Apply print-like grain|s09l06,s08l07|Create a grain layer with Add Noise; use blending and opacity modestly; evaluate at final output scale.|Grain integrates rather than overwhelms.
Make a sharp product label|s07l03,s07l02|Use shape path for label; set editable type; use consistent guides and padding; add subtle Stroke.|High contrast, legible at actual size.
Create a magazine cover|s07l02,s07l06|Place photograph; use three text hierarchy levels; keep safe margins; test contrast with image; export proof.|Readable title, subhead and caption.
Place a logo on fabric|s09l05,s04l04|Create grayscale displacement PSD of folds; apply Displace to logo Smart Object if supported; blend fabric shadow through logo; compare at 100%.|Folds subtly affect logo without excessive warping.
Prepare social post variants|s10l03,s10l05|Duplicate master, adapt square and portrait canvas; reflow text; inspect every edge; export at specified pixel sizes.|Two consistent, non-cropped exports.
Batch resize event thumbnails|s10l02,s10l05|Record safe resize action; test on one, then three files; Batch to separate output folder; validate dimensions.|All thumbnails consistent, originals untouched.
Export transparent UI icon|s02l04,s07l03,s10l05|Create shape layer in transparent canvas; export PNG with transparency; reopen over dark and light backgrounds.|Crisp alpha on both backgrounds.
Prepare for print|s08l05,s08l06,s10l06|Confirm bleed with printer; verify pixel dimensions and embedded profile; soft proof using provided paper ICC; export as required.|Printer-specific checklist completed.
Create a sharp website hero|s02l01,s08l07,s10l05|Crop nondestructively to final ratio; resize delivery copy; apply moderate output sharpen; export suitable JPEG/WebP if receiver supports.|Clean final pixels without sharpening halos.
Fix magenta/green cast|s08l02,s08l03|Select neutral sample; adjust green channel Curve or Color Balance gently; inspect flesh tones; constrain with mask.|Neutrals more plausible without clipped channels.
Build an editable color grade|s04l01,s08l03|Make Curves for contrast and a separate Hue/Saturation or Color Balance layer; name by effect; compare at reduced size.|Grade can be disabled in one click.
Create type on a curve|s07l04,s07l05|Draw Pen path; click with Type Tool; enter short phrase; adjust tracking and start position; keep text layer editable.|Glyphs flow smoothly without collisions.
Make a three-level digital painting|s06l01,s06l06|Separate background, midground and subject; establish grayscale value hierarchy; introduce limited hue palette; inspect thumbnail.|Focal region readable without detail.
Repair an overexposed image modestly|s08l01,s08l04|Inspect histogram; reduce highlights using Camera Raw or Light adjustment; check whether original channels retain data; avoid inventing recovery.|Improvement without fabricated texture claims.
Package an editable handoff|s10l01,s04l06|Bundle source/work/exports; audit links and fonts; save PSD plus preview; reopen from moved folder.|Another computer can relink and review without guessing.
'''

def parse_lines(raw, fields, name):
 out=[]
 for n,line in enumerate(raw.strip().splitlines(),1):
  arr=line.split('|')
  if len(arr)!=len(fields): raise ValueError(f'{name} line {n} has {len(arr)} expected {len(fields)}: {line[:90]}')
  out.append(dict(zip(fields,[s.strip() for s in arr])))
 return out
TOOLS=parse_lines(TOOLS_RAW, ['title','family','shortcut','purpose','controls','use','caution','lesson'], 'tools')
FILTERS=parse_lines(FILTERS_RAW, ['title','family','controls','effect','use','caution','lesson'], 'filters')
SHORTCUTS=parse_lines(SHORTCUTS_RAW, ['family','action','keys','context','note'], 'shortcuts')
GLOSSARY=parse_lines(GLOSSARY_RAW, ['term','definition','lesson'], 'glossary')
TROUBLE=parse_lines(TROUBLE_RAW,['symptom','cause','diagnosis','solution','warning','lesson'], 'troubleshooting')
RECIPES=parse_lines(RECIPES_RAW, ['title','requires','procedure','pass'], 'recipes')
for x in RECIPES:x['requires']=x['requires'].split(',')
