# Photoshop Field Manual — Windows Edition
Photoshop 27.11; researched 2026-10-28. Offline Linux/Windows reading; Photoshop directions are Windows only.

The research cutoff requested was October 29, 2026, one day after verified execution date. No October 29 release is presumed.

## How to use
Study stages in order, perform each exercise in Photoshop, then check its success criteria. The website contains navigation, searchable references and portable progress, all without networking. This Markdown edition is also fully readable offline.

# Stage 1 — Orientation & image fundamentals
See files, pixels, resolution and the interface before editing.

## s01l01 — What Photoshop edits: pixels versus vectors
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute what photoshop edits: pixels versus vectors.  
**Prerequisites:** None
### Concept and principle
A raster image is a grid of colored samples. Pixel dimensions limit recoverable detail; vector paths represent mathematically defined contours, although Photoshop eventually rasterizes the display/export. A photo can contain editable vector text and shapes in the same PSD.
### Location (Windows)
File > New; Window > Layers
### Walkthrough
1. Create a 600 × 400 px, RGB Color, 8-bit, white document.
2. Select Brush Tool (B), create a blank pixel layer, click once with a hard brush, then zoom to 400% to inspect the painted pixel edge.
3. Select Rectangle Tool in Shape mode, draw a rectangle, then zoom in.
4. Inspect the new shape layer and compare its editable edges with raster painting.
### Expected result
A shape layer remains a separate editable object; painted pixels show discrete squares at high zoom.
### Why it works
Raster images sample color at finite coordinates; vectors describe geometry independently of that grid.
### Practical application
Use this distinction when choosing Photoshop raster editing versus editable shape/type artwork for logos, graphics and photographs.
### Common mistake and fix
Do not confuse zooming the view with increasing real resolution.
### Efficiency tip
Use Shape mode rather than Pixels mode when you want editable geometry.
### Independent exercise
Create one raster mark and one Shape layer, rename both and compare them at 800% zoom.
### Completion criteria
Explain which artwork tolerates repeated scaling and why.
### Knowledge check
Which is resolution-independent before export?
- A raster brushstroke
- A vector path
- A flattened JPEG
**Answer:** A vector path. Raster images sample color at finite coordinates; vectors describe geometry independently of that grid.
### Connections
s01l02

## s01l02 — Pixels, dimensions, PPI and print size
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute pixels, dimensions, ppi and print size.  
**Prerequisites:** s01l01
### Concept and principle
Pixel width × pixel height determines image samples; PPI is metadata about their physical placement, not a magic detail generator. For example 3000 pixels at 300 PPI spans 10 inches at native size. Resampling changes the pixel count.
### Location (Windows)
Image > Image Size
### Walkthrough
1. Open or create a 1200 × 800 px document.
2. Choose Image > Image Size and disable Resample.
3. Change Resolution from 72 to 300 Pixels/Inch; observe pixel dimensions.
4. Enable Resample, change width to 600 pixels, and compare the dimensions again.
### Expected result
With Resample off, only print dimensions change; with it on, the number of pixels changes.
### Why it works
Resampling estimates samples, whereas PPI without resampling only changes the conversion between pixels and physical units.
### Practical application
Use these measurements when preparing screen assets and calculating native-size photographic prints without inventing image detail.
### Common mistake and fix
Blindly typing 300 PPI does not improve detail in a small JPEG.
### Efficiency tip
Keep Resample off while testing print-size relationships.
### Independent exercise
Find the print width of a 2400 px image at 300 PPI without a calculator dialog.
### Completion criteria
Correct answer is 8 inches; keep 2400 original pixels.
### Knowledge check
What does changing PPI with Resample disabled alter?
- Physical print size only
- Pixel width
- Number of layers
**Answer:** Physical print size only. Resampling estimates samples, whereas PPI without resampling only changes the conversion between pixels and physical units.
### Connections
s01l03

## s01l03 — Create, open, save and close safely
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute create, open, save and close safely.  
**Prerequisites:** s01l02
### Concept and principle
A layered PSD or large PSB is a working master; JPEG is a usually flattened, lossy delivery copy; PNG can retain alpha but is not a layered PSD replacement. Work on copies and save an editable source.
### Location (Windows)
File > New; File > Open; File > Save As; File > Save a Copy
### Walkthrough
1. Create a 1000 × 800 px RGB document, then paint a mark on a new layer.
2. Choose File > Save As and save a local PSD named 01-master.psd.
3. Reopen it and verify the Layers panel contains the painted layer.
4. Use File > Save a Copy to create a JPEG or PNG delivery file; reopen separately.
### Expected result
The PSD retains distinct layers; an exported flattened file is for distribution.
### Why it works
Working and delivery files have different jobs; reversible structure belongs in the master.
### Practical application
Use a layered master plus separate delivery files whenever a client may request revisions after an export.
### Common mistake and fix
Do not overwrite the only layered master with a flattened format.
### Efficiency tip
Use revision suffixes or versioned folders for critical deliverables.
### Independent exercise
Make a folder named project and save master.psd plus a delivery.png.
### Completion criteria
Reopen master.psd and demonstrate that the mark can be independently hidden.
### Knowledge check
What should be kept for revising layers later?
- JPEG only
- Screenshot
- PSD master
**Answer:** PSD master. Working and delivery files have different jobs; reversible structure belongs in the master.
### Connections
s01l04

## s01l04 — Interface, panels, workspaces and preferences
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute interface, panels, workspaces and preferences.  
**Prerequisites:** s01l03
### Concept and principle
The Toolbar chooses an operation; the Options bar changes its parameters; panels expose the document structure and adjustment controls. A workspace stores panel layout, not image pixels. Shortcuts may be intercepted by text fields.
### Location (Windows)
Window > Workspace; Window > Layers; Window > Properties; Edit > Preferences > General
### Walkthrough
1. Open Window > Layers and Window > Properties.
2. Drag a panel tab to rearrange the workspace; restore it using Window > Workspace > Reset Essentials (when Essentials is active).
3. Select Edit > Preferences > General and inspect settings without changing unknown options.
4. Click inside and outside a numeric field; test a tool key only when focus is off the field.
### Expected result
Panels can be repositioned without changing the image; keyboard focus affects commands.
### Why it works
UI layout is separate from document content, so workspace changes are safe to experiment with.
### Practical application
Use a consistent workspace when switching between retouching, compositing and layout without altering document content.
### Common mistake and fix
If a shortcut types a letter into a field, click the canvas or press Esc to exit the field.
### Efficiency tip
Save a custom workspace only after its layout is useful.
### Independent exercise
Configure a workspace with Layers, Properties and History visible; restore Essentials.
### Completion criteria
Locate both panels and show the default layout again.
### Knowledge check
Which choice restores a workspace layout?
- File > Export
- Window > Workspace > Reset Essentials
- Image > Mode
**Answer:** Window > Workspace > Reset Essentials. UI layout is separate from document content, so workspace changes are safe to experiment with.
### Connections
s01l05

## s01l05 — Zoom, pan, rulers and guides
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute zoom, pan, rulers and guides.  
**Prerequisites:** s01l04
### Concept and principle
View zoom changes screen magnification, not pixel content. Rulers, guides and the Info panel help measure and align without altering artwork. A hand-pan does not move document layers.
### Location (Windows)
View > Rulers; View > New Guide; Window > Info; Zoom Tool; Hand Tool
### Walkthrough
1. Open a document and press Ctrl+0 to fit it on screen.
2. Press Ctrl+1 to inspect 100% view.
3. Press Ctrl+R to display rulers, then drag a guide from a ruler.
4. Use Hand Tool (H) to pan around the canvas and inspect the Info panel.
### Expected result
The document content stays fixed as the view changes and guide overlays appear.
### Why it works
Display transformations and editing transformations are independent.
### Practical application
Use 100% zoom for pixel judgment and guides/rulers for repeatable spacing before export.
### Common mistake and fix
Do not mistake low zoom interpolation for actual file blur.
### Efficiency tip
At 100%, judge edge sharpness more reliably than at arbitrary zoom.
### Independent exercise
Set horizontal and vertical guides at the canvas midpoint and inspect at 100%.
### Completion criteria
Guides intersect at the middle without changing any pixel.
### Knowledge check
Does zooming to 400% add pixels?
- No
- Yes, four times
- Yes, only for PSD
**Answer:** No. Display transformations and editing transformations are independent.
### Connections
s01l06

## s01l06 — History, undo and disciplined experiments
**Stage 1:** Orientation & image fundamentals  
**Objective:** Explain and independently execute history, undo and disciplined experiments.  
**Prerequisites:** s01l05
### Concept and principle
Undo reverses recent actions but is not a durable backup; History states can be lost when a file closes or the list is purged. Save versions before destructive experiments.
### Location (Windows)
Edit > Undo; Window > History
### Walkthrough
1. Create a shape layer and paint three distinct short strokes on a new pixel layer.
2. Press Ctrl+Z once and observe the most recent step disappear.
3. Open Window > History and select an earlier state.
4. Return to the newest desired state, then save the PSD as v02.psd.
### Expected result
History walks through session states; the saved PSD records only the chosen current result.
### Why it works
History is temporal state, not a substitute for named snapshots or file versions.
### Practical application
Use History for immediate experiments, but save versioned PSDs before risky reconstruction or filters.
### Common mistake and fix
Jumping to a past History state and making new edits may discard later redo states.
### Efficiency tip
Duplicate a layer before testing filters or retouching.
### Independent exercise
Make three editing changes, deliberately revert one and create a new saved version.
### Completion criteria
Show a v01 and v02 file and explain their differences.
### Knowledge check
What survives closing and reopening a document?
- All unsaved History states
- Current undo buffer
- Saved PSD versions
**Answer:** Saved PSD versions. History is temporal state, not a substitute for named snapshots or file versions.
### Connections
s02l01; s01l01

## Stage 1 project — Pixel field guide
Create a labeled 800 × 600 PSD comparing raster marks, vector shapes, PPI and zoom; keep two versions.
**Pass condition:** Show 100% and 400% views; correctly distinguish pixel count from print density.

# Stage 2 — Documents, layers & geometry
Build safely editable files and navigate space.

## s02l01 — Canvas size, crop and image size
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute canvas size, crop and image size.  
**Prerequisites:** s01l06
### Concept and principle
Canvas Size adds or removes document area; Crop changes the framing; Image Size resamples or reinterprets resolution. Their effects differ despite all changing visible bounds.
### Location (Windows)
Image > Canvas Size; Crop Tool (C); Image > Image Size
### Walkthrough
1. Create 800 × 600 px with two Shape layers.
2. Choose Image > Canvas Size and set Width to 1000 px, keeping anchor centered.
3. Choose Crop Tool (C), drag a tighter frame and commit with Enter.
4. Choose Image > Image Size and compare pixel dimensions before resampling.
### Expected result
Canvas expands first; crop restricts framing; resampling alters sample count.
### Why it works
Three commands solve layout, composition and pixel-density problems respectively.
### Practical application
Use crop, canvas size and image size as separate choices for framing, adding space and changing resolution.
### Common mistake and fix
Cropping with Delete Cropped Pixels enabled removes hidden pixels.
### Efficiency tip
Disable Delete Cropped Pixels when you need an adjustable crop.
### Independent exercise
Prepare two outputs from one master: wide banner and cropped square without harming the master.
### Completion criteria
Record dimensions of each version and retain the original master.
### Knowledge check
Which increases empty document area without resampling existing artwork?
- Smart Sharpen
- Canvas Size
- Image Size with Resample
**Answer:** Canvas Size. Three commands solve layout, composition and pixel-density problems respectively.
### Connections
s02l02; s01l02

## s02l02 — Create, rename, reorder and group layers
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute create, rename, reorder and group layers.  
**Prerequisites:** s02l01
### Concept and principle
Layers composite top-to-bottom. Visibility, opacity, locks and groups change the editing structure, not the pixel size of the canvas. Accurate names matter during revisions.
### Location (Windows)
Window > Layers; Layer > New > Layer; Layer > Group Layers
### Walkthrough
1. Create three layers with colored rectangles on each.
2. Rename them Background color, Middle form, and Foreground accent.
3. Drag their order in Layers and toggle the eye icon.
4. Select related layers and press Ctrl+G to create a group.
### Expected result
Front layers cover rear layers; hiding or reordering visibly changes overlap.
### Why it works
Layer order is a compositing operation, not merely a file organizer.
### Practical application
Use descriptive layer names and groups when a multi-element design must be handed to someone else.
### Common mistake and fix
Painting on the wrong selected layer causes unexpected changes.
### Efficiency tip
Use descriptive names before a file reaches dozens of layers.
### Independent exercise
Build a three-color geometric composition using six named layers in two groups.
### Completion criteria
Hide either group and identify exactly what changes.
### Knowledge check
Which panel controls layer stacking?
- Layers
- Histogram
- Navigator
**Answer:** Layers. Layer order is a compositing operation, not merely a file organizer.
### Connections
s02l03; s01l03

## s02l03 — Move, align and distribute components
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute move, align and distribute components.  
**Prerequisites:** s02l02
### Concept and principle
Move changes layer position; align brings selected items to a common reference; distribute spaces multiple items evenly. Transform changes dimensions, rotation or orientation.
### Location (Windows)
Move Tool (V); Edit > Free Transform
### Walkthrough
1. Make three distinct square Shape layers.
2. Select all three in Layers, choose Move Tool (V), and inspect alignment/distribution controls in the Options bar.
3. Align their top edges, then distribute their horizontal centers.
4. Select one square and press Ctrl+T; resize with a corner handle and commit.
### Expected result
Three elements share a common top alignment and regular spacing; one element scales.
### Why it works
Geometry operations use selected layer bounds and alignment reference, not assumed eyeballing.
### Practical application
Use alignment/distribution and numeric transforms for tiled layouts, badges and systematic mockups.
### Common mistake and fix
Alignment and Distribute require the correct target layers, selection and sometimes an explicit reference; check the Options bar before assuming they will operate.
### Efficiency tip
Use guides and Smart Guides for precision, but inspect actual positions.
### Independent exercise
Lay out three icon tiles with consistent spacing and top alignment.
### Completion criteria
Use ruler guides to check alignment at 100%.
### Knowledge check
What is the purpose of Distribute?
- Flatten all layers
- Change color profile
- Make spacing systematic
**Answer:** Make spacing systematic. Geometry operations use selected layer bounds and alignment reference, not assumed eyeballing.
### Connections
s02l04; s01l04

## s02l04 — Transparency, alpha and the checkerboard
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute transparency, alpha and the checkerboard.  
**Prerequisites:** s02l03
### Concept and principle
Transparency means pixels contribute partially or not at all to an output. The checkerboard is a display indicator, not actual artwork; exporting JPEG cannot preserve alpha.
### Location (Windows)
Window > Layers; File > Export > Export As
### Walkthrough
1. Create a new document with Transparent Background Contents.
2. Draw an opaque ellipse on a Shape layer.
3. Hide any opaque background and observe checkerboard around it.
4. Use File > Export > Export As, choose PNG and enable Transparency if available.
### Expected result
PNG retains clear surrounding pixels; checkerboard appears only in the workspace.
### Why it works
An alpha channel controls opacity of pixel contributions, distinct from their RGB colors.
### Practical application
Use alpha transparency for logos, stickers, overlays and icons that must sit on varied backgrounds.
### Common mistake and fix
A hidden white background layer is not the same as an exported white fill.
### Efficiency tip
Check exported transparency in a second viewer or document.
### Independent exercise
Export a 512 × 512 transparent badge with no white rectangle.
### Completion criteria
Open the PNG over a dark layer and verify no white border.
### Knowledge check
Which format normally preserves transparency for web assets?
- BMP with default settings
- PNG
- JPEG
**Answer:** PNG. An alpha channel controls opacity of pixel contributions, distinct from their RGB colors.
### Connections
s02l05; s01l05

## s02l05 — Layer styles and reusable appearance
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute layer styles and reusable appearance.  
**Prerequisites:** s02l04
### Concept and principle
Layer effects such as Stroke, Drop Shadow and Color Overlay are attached to the layer instead of baked into pixels. Effect order, size and blending affect the result.
### Location (Windows)
Layer > Layer Style > Blending Options; Layers panel fx
### Walkthrough
1. Create a rounded rectangle Shape layer.
2. Double-click its empty layer row area to open Layer Style.
3. Add Stroke, set Position to Inside and Size to 8 px.
4. Add Drop Shadow with modest Distance and Size; then toggle fx visibility.
### Expected result
Stroke and shadow appear and can be disabled without altering the shape path.
### Why it works
Effects are parameterized render steps applied to content boundaries.
### Practical application
Use live layer styles for reusable outlined text, subtle shadows and brand-consistent interface graphics.
### Common mistake and fix
Do not confuse layer Fill 0% with Opacity 0%—styles may remain visible at Fill 0%.
### Efficiency tip
Use subtle shadows; large opaque shadows often look artificial.
### Independent exercise
Make a reusable badge with 2 styles and save as PSD.
### Completion criteria
Reopen effects and change stroke width without repainting.
### Knowledge check
How can a stroke remain independently adjustable?
- Layer Style
- Rasterize layer
- JPEG export
**Answer:** Layer Style. Effects are parameterized render steps applied to content boundaries.
### Connections
s02l06; s01l06

## s02l06 — Smart Guides, grids and measurement
**Stage 2:** Documents, layers & geometry  
**Objective:** Explain and independently execute smart guides, grids and measurement.  
**Prerequisites:** s02l05
### Concept and principle
Guides, grids and rulers organize precision work. Snapping may be toggled; alignment must be checked rather than assumed from temporary overlays.
### Location (Windows)
View > Show > Grid; View > Snap; View > Rulers
### Walkthrough
1. Create a 1000 × 1000 px document.
2. Show grid using View > Show > Grid and enable View > Snap if desired.
3. Draw four evenly sized shape tiles and position them near grid intersections.
4. Temporarily hide the grid and evaluate spacing at fit view.
### Expected result
Tiles align consistently without grid lines appearing in exported artwork.
### Why it works
Guides and grids are nonprinting reference overlays.
### Practical application
Use Smart Guides and grid snapping where repeated margins and exact alignment matter more than visual guesswork.
### Common mistake and fix
A grid unit is not necessarily one pixel; inspect preferences for spacing.
### Efficiency tip
For precise print measurements, select suitable ruler units.
### Independent exercise
Construct a four-tile contact sheet with equal margins and gaps.
### Completion criteria
Use guides to measure equal borders on every side.
### Knowledge check
Do guides normally appear in exported PNG files?
- Always
- Only in CMYK
- No
**Answer:** No. Guides and grids are nonprinting reference overlays.
### Connections
s03l01; s02l01

## Stage 2 project — Editable six-tile layout
Build six organized shape/text layers, two groups, clear alignment and transparent PNG output.
**Pass condition:** Grid spacing consistent within 4 px; PSD layers remain editable.

# Stage 3 — Selections, masks & isolation
Control precisely where changes appear.

## s03l01 — Marquee and lasso: selecting regions
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute marquee and lasso: selecting regions.  
**Prerequisites:** s02l06
### Concept and principle
A selection is a temporary spatial constraint on editing, often shown as marching ants. Geometric selections are suitable for hard-edged areas; freehand selections suit irregular boundaries.
### Location (Windows)
Rectangular Marquee Tool (M); Lasso Tool (L); Select > Deselect
### Walkthrough
1. Create a document with a colored pixel layer.
2. Use Rectangular Marquee (M) to select the left half.
3. Choose Layer > New > Layer, then Edit > Fill using a foreground color.
4. Press Ctrl+D, use Lasso (L) to trace a rough area and fill on a separate layer.
### Expected result
Only selected areas receive fills; deselection removes the boundary, not the filled pixels.
### Why it works
Selection masks specify edit coverage rather than storing artwork by themselves.
### Practical application
Use geometric selections for bounded fills, crops and controlled local pixel operations.
### Common mistake and fix
Watch whether the selection is set to New, Add, Subtract or Intersect in the Options bar.
### Efficiency tip
Feathering should be 0 px for crisp geometric artwork.
### Independent exercise
Create an abstract poster with one sharp rectangle and one freeform filled region.
### Completion criteria
Each fill occupies only its intended selected boundary.
### Knowledge check
What does Ctrl+D do in a selection workflow?
- Duplicate layer
- Deselect
- Delete selected pixels
**Answer:** Deselect. Selection masks specify edit coverage rather than storing artwork by themselves.
### Connections
s03l02; s02l02

## s03l02 — Object Selection, Quick Selection and color range
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute object selection, quick selection and color range.  
**Prerequisites:** s03l01
### Concept and principle
Object Selection detects likely objects; Quick Selection grows a brush-guided selection based on edges; Color Range targets sampled colors and tolerance. Each fails differently on low contrast.
### Location (Windows)
Object Selection Tool (W group); Quick Selection Tool (W group); Selection Brush Tool (L group); Select > Color Range
### Walkthrough
1. Open the included practice/mask-shapes.png.
2. Use Object Selection Tool to target a distinct shape.
3. Switch to Quick Selection Tool and paint inside a colored region; use subtract mode to trim spill.
4. Choose Select > Color Range and sample a different solid color, adjusting Fuzziness; confirm with OK.
### Expected result
Each method creates a usable but differently shaped selection.
### Why it works
The correct selector depends on semantic objects, visible boundaries or chromatic similarity.
### Practical application
Use a selection method matched to object shape, edge contrast and color complexity before refining a mask.
### Common mistake and fix
Color Range may select similar colors elsewhere in the image.
### Efficiency tip
Use the Selection Brush (L tool group) for painted selection refinement when available; do not confuse its overlay with a persistent layer mask.
### Independent exercise
Select and isolate each of the three large colored elements using a different method.
### Completion criteria
After each choice, toggle Quick Mask to examine missed edges.
### Knowledge check
Which method targets repeated similar colors?
- Color Range
- Crop Tool
- Character panel
**Answer:** Color Range. The correct selector depends on semantic objects, visible boundaries or chromatic similarity.
### Connections
s03l03; s02l03

## s03l03 — Layer masks: hiding without deleting
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute layer masks: hiding without deleting.  
**Prerequisites:** s03l02, s02l02, s02l04
### Concept and principle
A raster layer mask is grayscale coverage: white reveals, black hides, gray partially reveals. The pixels underneath are intact. Painting on a mask changes visibility rather than source RGB values.
### Location (Windows)
Layer > Layer Mask > Reveal All; Window > Layers
### Walkthrough
1. Open practice/mask-shapes.png.
2. Duplicate the image layer with Ctrl+J.
3. Choose Layer > Layer Mask > Reveal All and click the mask thumbnail.
4. Paint black with Brush (B) to hide part of the upper layer; press X to switch colors and paint white to restore it.
### Expected result
Part of the duplicate disappears and returns without losing RGB pixels.
### Why it works
The mask multiplies the layer opacity at each location.
### Practical application
Use a layer mask wherever temporary isolation, retouch restraint or revision-friendly concealment is required.
### Common mistake and fix
Check whether the image thumbnail or mask thumbnail is selected before painting.
### Efficiency tip
Alt-click a mask thumbnail to inspect the grayscale mask directly.
### Independent exercise
Create a diagonal blend between two differently colored layers using a mask.
### Completion criteria
You can reverse or refine the blend entirely by repainting the mask.
### Knowledge check
What restores a hidden area on a standard white layer mask?
- Delete pixels
- Flatten document
- Paint white on mask
**Answer:** Paint white on mask. The mask multiplies the layer opacity at each location.
### Connections
s03l04; s02l04

## s03l04 — Select and Mask: refining difficult boundaries
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute select and mask: refining difficult boundaries.  
**Prerequisites:** s03l03, s03l02
### Concept and principle
Edge refinement considers transitions, fine strands and color contamination. Hair and transparent items rarely have an objectively perfect binary edge. Output to a new layer with mask to preserve the original. Photoshop 27.11 adds AI-powered Enhance edge refinement; availability or processing conditions should be checked in the live selection workflow.
### Location (Windows)
Select > Select and Mask
### Walkthrough
1. Use practice/mask-shapes.png or an owned portrait with a clear background.
2. Create a rough subject selection using Quick Selection.
3. Open Select > Select and Mask, inspect On Black and On White views.
4. Adjust Smooth/Feather/Contrast sparingly and Output To: New Layer with Layer Mask.
5. If the 27.11 Enhance edge control is available, compare its result with standard Select and Mask refinement; retain the version with fewer fringes rather than assuming AI is always better.
### Expected result
A separate subject layer appears with a retouchable mask; edge quality varies by source.
### Why it works
A refined mask models partial pixel coverage instead of hard clipping alone.
### Practical application
Use Select and Mask for hair, soft edges and contrast-dependent composites that must work on multiple backgrounds.
### Common mistake and fix
Large Feather values cause a halo; excessive Contrast destroys wispy details.
### Efficiency tip
Inspect both light and dark backgrounds. Enhance edge is a version-specific, AI-assisted option; availability and processing requirements are not a promise of offline use.
### Independent exercise
Extract a subject and place it on three differently colored backgrounds.
### Completion criteria
No obvious old-background fringe at 100% on all three tests.
### Knowledge check
Why test extraction on different backgrounds?
- To improve PPI
- To expose edge halos
- To increase file size
**Answer:** To expose edge halos. A refined mask models partial pixel coverage instead of hard clipping alone.
### Connections
s03l05; s02l05

## s03l05 — Quick Mask, channels and saved selections
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute quick mask, channels and saved selections.  
**Prerequisites:** s03l04
### Concept and principle
Quick Mask visualizes selection coverage as a temporary overlay. Selections can be saved as alpha channels and loaded later, independent of a layer mask. Channel thumbnails may also be inspected for contrast.
### Location (Windows)
Quick Mask Mode button in Toolbar or Q; Select > Save Selection; Window > Channels
### Walkthrough
1. Make a lasso selection on an image.
2. Press Q to enter Quick Mask and paint black or white to revise coverage.
3. Press Q again, then Select > Save Selection with name detail-boundary.
4. Deselect, open Window > Channels, and use Select > Load Selection to restore it.
### Expected result
The refined selected area returns after being saved and loaded.
### Why it works
An alpha channel stores grayscale selection coverage for reuse.
### Practical application
Use saved selection channels when the same complex region needs several separate corrections later.
### Common mistake and fix
Do not edit a color channel accidentally when you intend to paint the Quick Mask.
### Efficiency tip
Name saved selections according to meaning, not date alone.
### Independent exercise
Create two named selections for separate image regions and reload each.
### Completion criteria
Both can be loaded without recreating the marquee.
### Knowledge check
What does a saved alpha channel preserve?
- Selection coverage
- A complete editable font
- Document history
**Answer:** Selection coverage. An alpha channel stores grayscale selection coverage for reuse.
### Connections
s03l06; s02l06

## s03l06 — Clipping masks versus vector masks
**Stage 3:** Selections, masks & isolation  
**Objective:** Explain and independently execute clipping masks versus vector masks.  
**Prerequisites:** s03l05, s02l02, s03l03
### Concept and principle
A clipping mask uses the transparency of a lower base layer to limit upper artwork. A vector mask uses an editable path boundary. A raster mask stores pixel coverage. They solve related but distinct problems.
### Location (Windows)
Layer > Create Clipping Mask; Layer > Vector Mask
### Walkthrough
1. Make a text or rectangle Shape layer called container.
2. Place a colorful pixel layer immediately above it and choose Layer > Create Clipping Mask.
3. Change the base shape and watch the image clip to its outline.
4. On a different pixel layer, draw a path and explore Layer > Vector Mask > Current Path.
### Expected result
One image is bounded by base-layer opacity; another by a vector path.
### Why it works
Clipping follows the lower layer; vector masks are path-defined.
### Practical application
Use clipping masks for content inside editable letters/shapes and vector masks for crisp geometric reveal boundaries.
### Common mistake and fix
A clipping mask is not the same as combining two layers permanently.
### Efficiency tip
Use editable text or shape bases for flexible mockups.
### Independent exercise
Place an image within a word and a separate image in an elliptical vector boundary.
### Completion criteria
Resizing the lower text/shape updates the visible crop.
### Knowledge check
What determines a clipping mask boundary?
- Canvas size
- Resolution metadata
- Transparency of its base layer
**Answer:** Transparency of its base layer. Clipping follows the lower layer; vector masks are path-defined.
### Connections
s04l01; s03l01

## Stage 3 project — Edge isolation studio
Extract three objects using color range, object selection and a Pen/vector mask; test on dark/light backgrounds.
**Pass condition:** Three separately toggled masks; no major hard fringe at 100%.

# Stage 4 — Nondestructive editing
Preserve source pixels and remain revision-ready.

## s04l01 — Adjustment layers and scoped corrections
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute adjustment layers and scoped corrections.  
**Prerequisites:** s03l06
### Concept and principle
Adjustment layers compute a tonal or color transformation above source layers. Their built-in masks let you target a region without duplicating source pixels. In Photoshop 27.10 and later, Light is a dedicated editable adjustment layer providing Exposure, Contrast, Highlights, Shadows, Whites and Blacks; it is not the same panel as traditional Curves.
### Location (Windows)
Layer > New Adjustment Layer > Curves; Window > Properties
### Walkthrough
1. Open practice/tone-gradient.png.
2. Choose Layer > New Adjustment Layer > Curves.
3. Raise a midtone point slightly, then click the mask thumbnail and paint black over one side.
4. Toggle adjustment layer visibility to compare.
5. Add Layer > New Adjustment Layer > Light in Photoshop 27.11; test Highlights −15 and Shadows +15 in Properties, then toggle visibility and compare with the Curves result.
### Expected result
Only the unmasked side becomes brighter; the original gradient remains intact.
### Why it works
A function maps input tonal values to new output values, modulated by mask coverage.
### Practical application
Use adjustment layers when tonal or color changes need client-review toggles and separately controlled masks.
### Common mistake and fix
If changes affect everything, inspect the adjustment mask and clipping.
### Efficiency tip
Name each adjustment by intent such as mids lift or cool highlights. For six basic tonal controls try Light; for exact curve shapes and channel control use Curves.
### Independent exercise
Make the left half brighter without touching the right; save editable PSD.
### Completion criteria
Hiding adjustment restores the unaltered source instantly.
### Knowledge check
Which allows later editing of the tonal mapping?
- JPEG
- Curves adjustment layer
- Image > Adjustments applied to pixels
**Answer:** Curves adjustment layer. A function maps input tonal values to new output values, modulated by mask coverage.
### Connections
s04l02; s03l02

## s04l02 — Smart Objects: embedded versus linked
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute smart objects: embedded versus linked.  
**Prerequisites:** s04l01
### Concept and principle
Smart Objects wrap original content so transforms and many filters can be reevaluated. Embedded content lives inside the PSD; linked content depends on an external file path. Neither guarantees lossless enlarging beyond the source detail.
### Location (Windows)
File > Place Embedded; File > Place Linked; Layer > Smart Objects > Convert to Smart Object
### Walkthrough
1. Create a PSD master and choose File > Place Embedded for practice/mask-shapes.png.
2. Resize it down using Ctrl+T, commit; resize up and compare.
3. Place the same PNG as Linked and inspect the link indicator in Layers.
4. Move the linked PNG externally in Windows Explorer and note how relinking may be required.
### Expected result
The embedded item travels inside the PSD; linked item references an external dependency.
### Why it works
A Smart Object retains the source transform data; linked assets add file-system dependencies.
### Practical application
Use embedded Smart Objects for portable components; use linked sources when shared artwork must update in multiple files.
### Common mistake and fix
Do not assume linked assets are bundled when sharing only the PSD.
### Efficiency tip
Package assets with predictable relative folder paths.
### Independent exercise
Make a mockup with one embedded logo and one linked reference.
### Completion criteria
List the external file required to reopen the project correctly.
### Knowledge check
Which is self-contained within the PSD?
- Embedded Smart Object
- Linked Smart Object
- Missing link
**Answer:** Embedded Smart Object. A Smart Object retains the source transform data; linked assets add file-system dependencies.
### Connections
s04l03; s03l03

## s04l03 — Smart Filters and reversible blur
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute smart filters and reversible blur.  
**Prerequisites:** s04l02
### Concept and principle
Filters applied to supported Smart Objects appear as editable Smart Filters with their own mask. Some filters and document modes impose restrictions; not all operations become Smart Filters.
### Location (Windows)
Layer > Smart Objects > Convert to Smart Object; Filter > Blur > Gaussian Blur
### Walkthrough
1. Create a detailed pixel layer and convert it to Smart Object.
2. Choose Filter > Blur > Gaussian Blur and set Radius to 6 px.
3. Double-click Gaussian Blur under Smart Filters and change Radius to 2 px.
4. Paint black on the Smart Filters mask over a detail that must remain sharp.
### Expected result
The blur changes reversibly; selected detail escapes the filter.
### Why it works
The filter parameters are stored separately from source pixels and masked after computation.
### Practical application
Use Smart Filters when sharpening or blur settings must remain adjustable after saving and reopening.
### Common mistake and fix
A large blur mask painted white exposes blur, not underlying image visibility.
### Efficiency tip
Place filters on Smart Objects before committing a design.
### Independent exercise
Blur a simple background while keeping a central badge sharp.
### Completion criteria
Change blur radius twice after saving without duplicating source pixels.
### Knowledge check
Which reopens Gaussian Blur parameters?
- Rasterize
- Save a JPEG
- Double-click its Smart Filter entry
**Answer:** Double-click its Smart Filter entry. The filter parameters are stored separately from source pixels and masked after computation.
### Connections
s04l04; s03l04

## s04l04 — Blend modes, opacity and fill
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute blend modes, opacity and fill.  
**Prerequisites:** s04l03
### Concept and principle
Blend modes mathematically combine layer pixel values with the composite below. Opacity scales the entire layer contribution, while Fill changes the interior contribution and can behave differently with layer styles.
### Location (Windows)
Window > Layers > blend mode / Opacity / Fill
### Walkthrough
1. Make a gray-filled layer above colored rectangles.
2. Test Multiply, Screen and Overlay, observing darkening/lightening tendencies.
3. Add a Stroke layer style to the top layer.
4. Lower Fill to 0%, then restore and lower Opacity to 0% to compare the style.
### Expected result
Multiply generally darkens, Screen brightens; Fill and Opacity affect styles differently.
### Why it works
Blend functions and alpha multiplication are distinct steps in rendering.
### Practical application
Use blend modes and Fill/Opacity controls for realistic shadow, highlight and special-effect layer composites.
### Common mistake and fix
Blending depends strongly on the colors below; no mode has a universal look.
### Efficiency tip
Compare at 100% and in the intended output color space.
### Independent exercise
Create three variations of a textured poster with different blending modes.
### Completion criteria
Explain the visual difference rather than choosing a mode by name alone.
### Knowledge check
Which setting can hide fill while leaving some layer effects visible?
- Lock Pixels
- Fill 0%
- Opacity 0%
**Answer:** Fill 0%. Blend functions and alpha multiplication are distinct steps in rendering.
### Connections
s04l05; s03l05

## s04l05 — Blend If and conditional compositing
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute blend if and conditional compositing.  
**Prerequisites:** s04l04
### Concept and principle
Blend If uses underlying or current layer brightness to reveal and conceal areas without painting masks. Split slider halves make transitions gradual; tonal changes below can alter the blend.
### Location (Windows)
Layer > Layer Style > Blending Options
### Walkthrough
1. Create a grayscale gradient layer and a bright color texture above it.
2. Open Blending Options for the upper layer.
3. Under Blend If: Gray, move the Underlying Layer dark slider to reveal dark background areas.
4. Alt-drag one half of a slider to split its ramp and smooth the transition.
### Expected result
The upper texture fades selectively based on underlying brightness.
### Why it works
Luminance-conditioned blending is an automatic mask derived from pixel intensities.
### Practical application
Use Blend If to reveal underlying texture/luminance without permanently deleting or painting source pixels.
### Common mistake and fix
A non-split slider can create severe clipping edges.
### Efficiency tip
Split sliders while zoomed in to evaluate haloes.
### Independent exercise
Integrate a light streak into a dark gradient without erasing pixels.
### Completion criteria
The transition remains editable and shows no abrupt hard band.
### Knowledge check
What does Underlying Layer control?
- Reveal based on lower composite tone
- Selection size
- Document PPI
**Answer:** Reveal based on lower composite tone. Luminance-conditioned blending is an automatic mask derived from pixel intensities.
### Connections
s04l06; s03l06

## s04l06 — Versionable editing and review handoff
**Stage 4:** Nondestructive editing  
**Objective:** Explain and independently execute versionable editing and review handoff.  
**Prerequisites:** s04l05
### Concept and principle
Professional files should record structure, dependencies, revision status and flattened previews. Nondestructive editing is also about naming, file integrity and a reliable recovery route.
### Location (Windows)
File > Save As; File > Save a Copy; Window > Layers
### Walkthrough
1. Open an earlier project and group source, adjustments and design layers.
2. Name groups 01_SOURCE, 02_EDIT and 03_OUTPUT.
3. Save a new PSD revision and export a PNG preview.
4. Close and reopen the revision, confirm no missing linked elements or font warnings.
### Expected result
Editable master reopens with organized, visible layers and preview matches the intended version.
### Why it works
Stable naming and verification prevent lost context between sessions.
### Practical application
Use versioned working documents and named adjustments for accountable client revisions and team handoffs.
### Common mistake and fix
A preview is not a substitute for the master.
### Efficiency tip
Keep the source layer untouched or backed up.
### Independent exercise
Deliver a revisioned PSD and PNG preview with a short change note.
### Completion criteria
Another editor can find the source and isolate your final changes.
### Knowledge check
What is best for an editable client revision?
- Single flattened PNG
- Unlabeled working history
- Organized PSD plus preview
**Answer:** Organized PSD plus preview. Stable naming and verification prevent lost context between sessions.
### Connections
s05l01; s04l01

## Stage 4 project — Reversible visual treatment
Create an original PSD plus three looks using Curves, Smart Filters, Blend If and named layer styles.
**Pass condition:** Each look toggles independently; master pixels untouched.

# Stage 5 — Retouching & restoration
Remove distractions and repair images without damaging texture.

## s05l01 — Spot healing versus healing brush
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute spot healing versus healing brush.  
**Prerequisites:** s04l06
### Concept and principle
Spot Healing estimates replacement texture automatically; Healing Brush samples from a chosen source and adapts tonal appearance. Both are preferable on a separate cleanup layer when tool settings permit.
### Location (Windows)
Spot Healing Brush Tool (J); Healing Brush Tool (J)
### Walkthrough
1. Open practice/retouch-dots.png and add an empty layer named cleanup.
2. Choose Spot Healing Brush, set Sample All Layers in Options (if available), and dab individual dots.
3. Switch to Healing Brush; Alt-click a clean sample near a larger defect, then paint it.
4. Toggle cleanup visibility and compare texture.
### Expected result
Small colored defects disappear while surrounding gradient texture remains continuous.
### Why it works
Healing uses local statistics and source texture to blend a correction.
### Practical application
Use healing on small skin marks, dust and sensor spots where the surrounding texture supports reconstruction.
### Common mistake and fix
Oversized brush tips create soft or duplicated details; sample nearby.
### Efficiency tip
Work from small blemishes to larger regions and inspect at 100%.
### Independent exercise
Remove 10 intentionally planted spots without painting on the source layer.
### Completion criteria
At 100%, repair boundaries are not visibly smeared.
### Knowledge check
Why use a blank cleanup layer?
- To increase PPI
- To preserve original pixels
- To make JPEG lossless
**Answer:** To preserve original pixels. Healing uses local statistics and source texture to blend a correction.
### Connections
s05l02; s04l02

## s05l02 — Clone Stamp, Patch and pattern repetition
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute clone stamp, patch and pattern repetition.  
**Prerequisites:** s05l01
### Concept and principle
Clone Stamp copies sampled pixels, including both texture and tonal pattern; Patch repairs a selected area using another region and may blend boundary behavior. Clone is precise but repeating source patterns can betray edits.
### Location (Windows)
Clone Stamp Tool (S); Patch Tool (J)
### Walkthrough
1. Open practice/retouch-dots.png and duplicate the background.
2. Use Clone Stamp (S); Alt-click a clean region and paint over an obvious spot.
3. Use the Patch Tool to outline a separate blemish and drag to clean texture (Source mode).
4. Inspect for repeated motifs; undo any noticeable repetition.
### Expected result
Damage is replaced, but careless cloning can reproduce exact nearby shapes.
### Why it works
Sampling is literal reconstruction rather than generation from scene semantics.
### Practical application
Use cloning for straight structures and patterned texture that automatic healing tends to distort.
### Common mistake and fix
Do not sample across a strong lighting gradient unnecessarily.
### Efficiency tip
Resample frequently and work on an empty layer when Clone Stamp sampling supports it.
### Independent exercise
Repair a linear blemish using multiple short source samples.
### Completion criteria
No recognizable repeated dot or mirrored texture in the repaired region.
### Knowledge check
What is the main risk of repeated cloning from one spot?
- Visible repeated pattern
- Loss of ruler units
- Missing alpha channel
**Answer:** Visible repeated pattern. Sampling is literal reconstruction rather than generation from scene semantics.
### Connections
s05l03; s04l03

## s05l03 — Remove tool and content-aware corrections
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute remove tool and content-aware corrections.  
**Prerequisites:** s05l02
### Concept and principle
Remove Tool estimates plausible replacement content from surrounding context; Content-Aware Fill gives more explicit region and sampling control. Some Remove models process on device after download; cloud options differ.
### Location (Windows)
Remove Tool (J group); Edit > Content-Aware Fill
### Walkthrough
1. Open a photograph or the retouch practice PNG; duplicate or create a cleanup layer.
2. Paint over an unwanted mark using Remove Tool, using its configured processing mode.
3. Undo if needed; select a larger unwanted area with Lasso.
4. Choose Edit > Content-Aware Fill, inspect preview/sampling region and output to a new layer.
### Expected result
Unwanted area is reconstructed; results differ by local texture and model choice.
### Why it works
These methods infer missing content and may invent implausible structure.
### Practical application
Use Remove/Content-Aware techniques for distractions when inpainted content can be checked against real context.
### Common mistake and fix
Generated repairs must be checked for duplicated objects and factual distortion.
### Efficiency tip
Choose Remove processing mode deliberately: on-device requires an available locally downloaded model and suitable hardware; cloud processing requires service access. Confirm labels in 27.11.
### Independent exercise
Remove an isolated mark and a larger distraction, compare both methods.
### Completion criteria
Edges, repeated lines and texture remain consistent at 100%.
### Knowledge check
Which gives explicit sampling-region preview?
- Marquee tool
- History panel
- Content-Aware Fill workspace
**Answer:** Content-Aware Fill workspace. These methods infer missing content and may invent implausible structure.
### Connections
s05l04; s04l04

## s05l04 — Portrait retouching: texture and restraint
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute portrait retouching: texture and restraint.  
**Prerequisites:** s05l03, s03l03, s04l01
### Concept and principle
Retouching should preserve pore texture, facial shape and identity. Separate tonal unevenness from isolated texture blemishes; global skin blurring loses realistic detail.
### Location (Windows)
Healing Brush Tool; Layer > New Adjustment Layer > Curves
### Walkthrough
1. Use an authorized portrait; duplicate the source layer and create cleanup above it.
2. Heal isolated temporary blemishes at 100%, not permanent identifying marks by default.
3. Add a Curves adjustment layer and invert its mask using Ctrl+I after selecting the mask.
4. Paint soft white at low brush opacity to lighten only selected shadow regions.
### Expected result
Skin looks naturally even, with fine texture intact and no obvious patches.
### Why it works
Selective local correction changes specific problems while preserving normal surface variation.
### Practical application
Use conservative portrait retouching where subject texture and identity must remain recognizable.
### Common mistake and fix
Avoid excessive smoothing, reshaping or removing meaningful identity features.
### Efficiency tip
Zoom out regularly to judge whether local edits remain believable.
### Independent exercise
Edit a portrait using no more than two healing passes and two subtle tonal adjustments.
### Completion criteria
Toggle off all retouch layers: identity and natural skin texture remain recognizable.
### Knowledge check
Best first step for one small blemish?
- Flatten all layers
- Localized healing
- Global blur
**Answer:** Localized healing. Selective local correction changes specific problems while preserving normal surface variation.
### Connections
s05l05; s04l05

## s05l05 — Dodge and burn for form
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute dodge and burn for form.  
**Prerequisites:** s05l04, s04l01, s03l03
### Concept and principle
Dodge brightens and burn darkens local areas. Separate Curves layers with masks provide adjustable and often safer light shaping than repeatedly brushing the original pixels.
### Location (Windows)
Layer > New Adjustment Layer > Curves; Brush Tool (B)
### Walkthrough
1. Create a curves layer raising midtones and name Dodge.
2. Invert its white mask to black with Ctrl+I.
3. Create a second Curves layer lowering midtones named Burn; invert mask.
4. Paint white at low opacity on respective masks to refine highlights and shadows.
### Expected result
Local form and contrast improve without obvious bright or dark brush circles.
### Why it works
Small spatial tone changes reinforce perceived lighting and shape.
### Practical application
Use Curves-based dodge/burn for local dimensionality without permanently altering the raw photo layer.
### Common mistake and fix
Painting a mask at 100% brush opacity creates harsh patches.
### Efficiency tip
Use a soft brush at 5–15% opacity for gradual work.
### Independent exercise
Build a simple ball from practice/tone-gradient.png using subtle dodge/burn.
### Completion criteria
Smooth gradual change with no patchy halos at 100%.
### Knowledge check
Where should you paint for editable dodge/burn?
- On Curves layer masks
- Directly on background pixels
- In Channels as RGB
**Answer:** On Curves layer masks. Small spatial tone changes reinforce perceived lighting and shape.
### Connections
s05l06; s04l06

## s05l06 — Liquify, perspective and ethical changes
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute liquify, perspective and ethical changes.  
**Prerequisites:** s05l05
### Concept and principle
Liquify warps local geometry; perspective correction aligns planar structures. Geometric editing can alter identity and meaning: disclose material manipulations in documentary or evidentiary contexts.
### Location (Windows)
Filter > Liquify; Edit > Transform > Perspective
### Walkthrough
1. Create a patterned layer and convert to a Smart Object.
2. Choose Filter > Liquify, use Forward Warp with modest pressure and commit.
3. Reopen the Smart Filter to revise; compare straight lines.
4. Separately use Edit > Transform > Perspective on a shape and inspect convergence.
### Expected result
Objects bend or converge predictably; Smart Filter settings remain reversible when supported.
### Why it works
Warping moves sample coordinates and can distort backgrounds and scale cues.
### Practical application
Use Liquify and perspective tools for optical or geometric correction while documenting image integrity changes.
### Common mistake and fix
Do not use Liquify casually for identity-sensitive retouching.
### Efficiency tip
Use a duplicate/Smart Object and compare to unedited reference.
### Independent exercise
Correct an obviously tilted rectangular label while preserving its proportions.
### Completion criteria
Edges align more plausibly without stretching the text unnaturally.
### Knowledge check
What makes Liquify adjustable after application?
- Flattening image
- JPEG save
- Applying as supported Smart Filter
**Answer:** Applying as supported Smart Filter. Warping moves sample coordinates and can distort backgrounds and scale cues.
### Connections
s05l07; s05l01

## s05l07 — Old photo repair and reconstruction
**Stage 5:** Retouching & restoration  
**Objective:** Explain and independently execute old photo repair and reconstruction.  
**Prerequisites:** s05l06
### Concept and principle
Restoration begins with separating tone/fading, dirt/scratches and missing geometry. Reconstructing missing faces or text is inherently interpretive, not an authentic recovery of historical facts.
### Location (Windows)
Spot Healing Brush; Clone Stamp Tool; Layer > New Adjustment Layer > Levels
### Walkthrough
1. Open an owned scanned photograph or practice/retouch-dots.png.
2. Duplicate the image layer and crop only outside borders if permitted.
3. Use Levels adjustment to set sensible tonal endpoints without clipping.
4. Retouch scratches on a separate layer; rebuild repeated lines with short Clone Stamp samples.
### Expected result
Contrast improves and major marks recede while original structure stays preserved.
### Why it works
Restoration is constrained inference: maintain provenance and reversible corrections.
### Practical application
Use separate repair layers and an edit log for family archives, scanned prints and ethically documented restoration.
### Common mistake and fix
Do not treat AI-invented missing historical details as recovered truth.
### Efficiency tip
Keep a separate original archival scan with embedded profile.
### Independent exercise
Produce before/after and a note describing which pixels were reconstructed.
### Completion criteria
Original scan remains retained; reconstruction is documented.
### Knowledge check
For archival restoration, which is mandatory?
- Delete history of intervention
- Retain original and document changes
- Overwrite scan
**Answer:** Retain original and document changes. Restoration is constrained inference: maintain provenance and reversible corrections.
### Connections
s06l01; s05l02

## Stage 5 project — Careful restoration
Repair a damaged practice image, showing healing, cloning, dodge/burn and an annotated before/after.
**Pass condition:** No major repeated textures; source copy preserved.

# Stage 6 — Painting & brushes
Understand strokes, color, brush behavior and fills.

## s06l01 — Brush fundamentals: tip, size and hardness
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute brush fundamentals: tip, size and hardness.  
**Prerequisites:** s05l07
### Concept and principle
Brush Tip Shape defines diameter and hardness, Opacity controls stroke contribution, and Flow controls accumulation as the tip moves. Low flow builds color gradually.
### Location (Windows)
Brush Tool (B); Window > Brush Settings
### Walkthrough
1. Create a transparent layer and choose Brush Tool (B).
2. Paint three strokes at Hardness 100%, 50%, and 0% using the same diameter.
3. Set Opacity to 30% and paint a single stroke; then set Flow to 10% and make overlapping strokes.
4. Compare the buildup at intersections and edges.
### Expected result
Hard brushes have crisp edges; soft brushes feather; low-flow strokes accumulate color.
### Why it works
A brush deposits samples along a path, blended with existing pixels.
### Practical application
Use brush opacity, flow and hardness choices to control edges, gradients and masks instead of guessing at stroke strength.
### Common mistake and fix
Painting directly on the white Background loses flexibility.
### Efficiency tip
Use [ and ] for brush diameter only when the brush is focused and shortcuts are default.
### Independent exercise
Create a reference swatch of 4 brush behaviors, label it with Type.
### Completion criteria
Describe which produces crisp contours and which builds shading.
### Knowledge check
What makes a stroke build slowly with repeated passes?
- Low Flow
- Higher PPI
- Canvas Size
**Answer:** Low Flow. A brush deposits samples along a path, blended with existing pixels.
### Connections
s06l02; s05l03

## s06l02 — Brush dynamics and tablet pressure
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute brush dynamics and tablet pressure.  
**Prerequisites:** s06l01
### Concept and principle
Shape Dynamics may vary diameter with pen pressure or other inputs. Without a pressure-capable tablet, pressure controls do not respond as expected. Smoothing stabilizes trajectories at a cost in immediacy.
### Location (Windows)
Window > Brush Settings; Brush Tool Options bar
### Walkthrough
1. Open Brush Settings and enable Shape Dynamics.
2. Inspect Size Jitter Control and choose Pen Pressure only if a pressure tablet is available.
3. Paint slow and fast curves with Smoothing 0% and then a higher value.
4. Compare curves; if no tablet exists, use a fixed tip and note the limitation.
### Expected result
Stroke taper depends on tablet pressure; smoothing reduces small jagged deviations.
### Why it works
Input devices determine which brush dynamics are measurable.
### Practical application
Use pressure and brush dynamics for natural-looking pen-tablet drawing and repeated texture creation.
### Common mistake and fix
Do not mistake absent tablet pressure for an application defect.
### Efficiency tip
Save a tested brush preset with a descriptive name.
### Independent exercise
Make a labeled brush study with fixed size, scatter, and smoothing examples.
### Completion criteria
Report whether pen pressure is available and demonstrate smooth deliberate strokes.
### Knowledge check
What hardware enables true pen-pressure size control?
- Ordinary mouse only
- External SSD
- Pressure-sensitive tablet
**Answer:** Pressure-sensitive tablet. Input devices determine which brush dynamics are measurable.
### Connections
s06l03; s05l04

## s06l03 — Color picker, swatches and sampling
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute color picker, swatches and sampling.  
**Prerequisites:** s06l02
### Concept and principle
Foreground/Background colors are active state, distinct from color profiles. Eyedropper samples pixels or composites; Swatches store reusable color choices.
### Location (Windows)
Foreground color swatch; Eyedropper Tool (I); Window > Swatches
### Walkthrough
1. Open practice/color-palette.png.
2. Select Eyedropper (I), click a palette square and inspect Foreground color.
3. Open Color Picker and record hexadecimal RGB value.
4. Create a new layer and paint two sampled colors; save them as Swatches if supported.
### Expected result
Brush strokes match sampled palette tones when same color-management conditions apply.
### Why it works
Sampling records channel values of rendered pixels for later reuse.
### Practical application
Use sampling and swatch libraries for consistent product colors, UI palettes and digital painting.
### Common mistake and fix
Eyedropper sample size and Sample settings can alter noisy-edge results.
### Efficiency tip
Sample flat interior areas, not anti-aliased edges.
### Independent exercise
Create a 5-color palette strip and verify hex values for each.
### Completion criteria
Colors can be independently repainted from saved swatches.
### Knowledge check
Which control samples a pixel color?
- Dodge
- Eyedropper
- Hand
**Answer:** Eyedropper. Sampling records channel values of rendered pixels for later reuse.
### Connections
s06l04; s05l05

## s06l04 — Gradients, patterns and fill layers
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute gradients, patterns and fill layers.  
**Prerequisites:** s06l03
### Concept and principle
A Gradient Fill layer generates a controllable continuous transition; Pattern Fill tiles a source. Compared with painting directly, fill layers preserve their parameters and mask options.
### Location (Windows)
Layer > New Fill Layer > Gradient; Layer > New Fill Layer > Pattern
### Walkthrough
1. Create a 1000 × 600 px document.
2. Choose Layer > New Fill Layer > Gradient; select linear transition and adjust Angle.
3. Open Gradient Fill properties later and change Scale.
4. Add a Pattern Fill layer if patterns are installed; adjust Scale then hide it to compare.
### Expected result
Background colors form a consistent gradual sweep; pattern repeat changes with scale.
### Why it works
Fill layers render procedural pixels during compositing.
### Practical application
Use gradient/pattern fill layers for editable backgrounds, vignettes and repeated graphic motifs.
### Common mistake and fix
Very narrow gradients in 8-bit images may band visibly.
### Efficiency tip
Consider 16-bit mode for demanding smooth gradients, subject to export support.
### Independent exercise
Produce three backgrounds from the same master using adjustable fills.
### Completion criteria
No hand-painted seam or uneven banding visible at usual output zoom.
### Knowledge check
What remains editable on a Gradient Fill layer?
- Gradient and angle
- Only history
- JPEG quantization
**Answer:** Gradient and angle. Fill layers render procedural pixels during compositing.
### Connections
s06l05; s05l06

## s06l05 — Eraser, history brush and restoration methods
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute eraser, history brush and restoration methods.  
**Prerequisites:** s06l04, s03l03
### Concept and principle
Eraser removes or reduces pixels; a mask usually provides the same visual result more safely. History Brush can paint an earlier image state into current pixels but depends on History source availability.
### Location (Windows)
Eraser Tool (E); History Brush Tool (Y); Window > History
### Walkthrough
1. Make a pixel layer with colored paint and duplicate it.
2. Erase part of the duplicate with Eraser (E) and compare with a mask on another copy.
3. Open History panel and review source states for History Brush.
4. Save and reopen: observe that the original History sequence does not remain available.
### Expected result
Mask-based hiding is reversible; erasing changes alpha of the chosen pixel layer.
### Why it works
Editing coverage and removal of stored pixels are separate concepts.
### Practical application
Use History Brush sparingly for session-based variants; prefer reversible masks for persistent revisions.
### Common mistake and fix
Do not assume History Brush can resurrect changes after closing Photoshop.
### Efficiency tip
Default to masks unless permanent pixel deletion is intentional.
### Independent exercise
Recreate the same missing area using Eraser and using a layer mask.
### Completion criteria
Only the masked version can restore hidden content by painting white.
### Knowledge check
Which hides pixels without deleting their RGB content?
- Eraser on raster layer
- Flatten Image
- Layer mask
**Answer:** Layer mask. Editing coverage and removal of stored pixels are separate concepts.
### Connections
s06l06; s05l07

## s06l06 — Digital painting with layers and value structure
**Stage 6:** Painting & brushes  
**Objective:** Explain and independently execute digital painting with layers and value structure.  
**Prerequisites:** s06l05
### Concept and principle
Readable digital painting begins with large value masses, then color and edge hierarchy, and finally detail. Layer organization prevents foreground/background mixing.
### Location (Windows)
Brush Tool (B); Window > Layers
### Walkthrough
1. Set up a 1200 × 800 px RGB canvas with background, midground and foreground layers.
2. Paint three large value masses in grayscale using a broad soft brush.
3. Add smaller hard-edged focal forms, then introduce a Color blend mode layer for hue.
4. Check the design in grayscale using a temporary Black & White adjustment.
### Expected result
A coherent scene reads by value even before small details appear.
### Why it works
Perception of form depends more on large contrasts than local decorative detail.
### Practical application
Use independent paint layers and value planning to build original illustrations with consistent lighting.
### Common mistake and fix
Adding small details before solving composition wastes time.
### Efficiency tip
Toggle between fit view and 100% while painting.
### Independent exercise
Paint a simple cityscape with a clear focal point using at most five layers.
### Completion criteria
At thumbnail size the focal object is still identifiable.
### Knowledge check
What should be established first in a painting?
- Output ZIP name
- Large value structure
- Individual eyelashes
**Answer:** Large value structure. Perception of form depends more on large contrasts than local decorative detail.
### Connections
s07l01; s06l01

## Stage 6 project — Limited-palette artwork
Paint a five-layer scene and a swatch board using fixed and dynamics brushes, gradient and value hierarchy.
**Pass condition:** Scene reads at 10% view; colors can be recreated from swatches.

# Stage 7 — Typography, shapes & paths
Build readable layouts and precise vector-edged components.

## s07l01 — Point type, paragraph type and editable text
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute point type, paragraph type and editable text.  
**Prerequisites:** s06l06
### Concept and principle
Point type is created by clicking; paragraph type uses a bounding box. Type stays editable until rasterized, and font substitution can change line breaks and layout.
### Location (Windows)
Horizontal Type Tool (T); Window > Character; Window > Paragraph
### Walkthrough
1. Create a 1200 × 800 px document.
2. Choose Type Tool (T), click once and type a short headline.
3. Drag a text box and paste three sentences for paragraph type.
4. Change font size and leading in Character panel, and compare wrapping before and after resizing box.
### Expected result
Headline remains a single type object; paragraph text wraps within its frame.
### Why it works
Type layers store characters and layout rules rather than fixed painted shapes.
### Practical application
Use live text layers for posters, thumbnails and design systems where wording may change.
### Common mistake and fix
Selecting the Move Tool while editing text may require committing the text first.
### Efficiency tip
Keep critical fonts installed and package font licensing information appropriately.
### Independent exercise
Design a typographic title plus a two-column paragraph block.
### Completion criteria
Both remain editable; text does not overflow its intended boxes.
### Knowledge check
What makes a paragraph box wrap text?
- Its bounding width
- Image PPI
- Layer opacity
**Answer:** Its bounding width. Type layers store characters and layout rules rather than fixed painted shapes.
### Connections
s07l02; s06l02

## s07l02 — Kerning, tracking, leading and hierarchy
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute kerning, tracking, leading and hierarchy.  
**Prerequisites:** s07l01
### Concept and principle
Kerning changes a specific character pair; tracking adjusts spacing across a selection; leading sets baseline-to-baseline distance. Good hierarchy depends on consistent spacing, size and contrast.
### Location (Windows)
Window > Character; Window > Paragraph
### Walkthrough
1. Type AVATAR as a headline and select the AV pair.
2. In Character panel, compare Metrics/Optical kerning where available and manual pair adjustment.
3. Select the entire heading and adjust Tracking.
4. Create three body lines and change Leading to compare dense versus airy layout.
### Expected result
Letter and line spacing visibly change without changing the wording.
### Why it works
Typography works as a spatial rhythm, not only the choice of font.
### Practical application
Use kerning, tracking and leading to fix poor visual rhythm and readability in client-facing typography.
### Common mistake and fix
Overtracking small body text damages legibility.
### Efficiency tip
Audit at actual output size, not just an enlarged canvas.
### Independent exercise
Create three text levels: title, subheading and body; align to a common edge.
### Completion criteria
Hierarchy is obvious in 3 seconds and no line collisions occur.
### Knowledge check
Which sets spacing between text baselines?
- Kerning
- Opacity
- Leading
**Answer:** Leading. Typography works as a spatial rhythm, not only the choice of font.
### Connections
s07l03; s06l03

## s07l03 — Shape tools and vector operations
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute shape tools and vector operations.  
**Prerequisites:** s07l02
### Concept and principle
Shape layers contain paths with fills and strokes. Combining, subtracting and intersecting shapes controls topology while keeping crisp edges at working resolution.
### Location (Windows)
Rectangle Tool (U); Shape mode; Path Operations in Options bar
### Walkthrough
1. Choose Rectangle Tool (U) and set tool mode to Shape.
2. Draw one rectangle and then an ellipse with separate Shape layers.
3. Select one Shape layer and use Path Operations to subtract an inner hole where supported.
4. Change fill, stroke and corner radius in Properties.
### Expected result
The composite geometry responds to path operations and stays editable.
### Why it works
Shape paths define coverage mathematically, with fills and strokes rendered at export.
### Practical application
Use vector shape paths for icons, panel backgrounds, adjustable borders and editable geometry.
### Common mistake and fix
Drawing in Pixels mode rasterizes output instead of adding editable shapes.
### Efficiency tip
Check mode (Shape/Path/Pixels) before drawing.
### Independent exercise
Create a simple icon with a hole and 2 shape colors.
### Completion criteria
Icon still has crisp boundaries after a reversible transform.
### Knowledge check
Which mode produces a vector-edged editable shape layer?
- Quick Mask
- Shape
- Pixels
**Answer:** Shape. Shape paths define coverage mathematically, with fills and strokes rendered at export.
### Connections
s07l04; s06l04

## s07l04 — Pen tool, anchor points and Bézier handles
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute pen tool, anchor points and bézier handles.  
**Prerequisites:** s07l03
### Concept and principle
A Bézier path consists of anchors and direction handles; moving handles changes tangent direction and curvature. Fewer well-placed anchors typically produce smoother curves.
### Location (Windows)
Pen Tool (P); Direct Selection Tool (A); Window > Paths
### Walkthrough
1. Select Pen Tool (P) and choose Path mode.
2. Click two points for a straight segment; click-drag the third to create smooth handles.
3. Close the contour, then select Direct Selection (A) and modify a handle.
4. Convert path to selection using Paths panel; create a masked fill from it.
### Expected result
Curved boundary changes as handles move while original samples remain untouched.
### Why it works
Bezier segments interpolate a smooth curve between control points.
### Practical application
Use Bézier paths for product cutouts and smooth logos where automated selections are imprecise.
### Common mistake and fix
Too many points create lumpy geometry and make revision slow.
### Efficiency tip
Place anchors at major direction changes, not every few pixels.
### Independent exercise
Trace a simple leaf outline with six or fewer anchors.
### Completion criteria
Curve has no visible kinks where the contour should be smooth.
### Knowledge check
What primarily controls Bézier curvature?
- Direction handles
- PPI
- Blend mode
**Answer:** Direction handles. Bezier segments interpolate a smooth curve between control points.
### Connections
s07l05; s06l05

## s07l05 — Text on paths and shape-following type
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute text on paths and shape-following type.  
**Prerequisites:** s07l04, s07l01
### Concept and principle
Text on a path remains editable and its baseline follows the vector path. Dynamic Text features available in recent stable releases can reflow certain shapes, but are not prerequisites for standard path text.
### Location (Windows)
Pen Tool (P); Type Tool (T)
### Walkthrough
1. Draw a curved path in Path mode with the Pen Tool.
2. Choose Type Tool and hover until the insertion cursor indicates path text.
3. Click the path and type a short phrase; use path selection to reposition the text start/end controls.
4. Adjust tracking to fit the curve without compression.
### Expected result
Words follow the curve rather than a horizontal box.
### Why it works
Glyph positions are laid out along a geometric baseline.
### Practical application
Use path text for badges, labels and curved headlines while preserving editable type.
### Common mistake and fix
Crowded path text becomes unreadable; choose shorter copy.
### Efficiency tip
Use ordinary path text before exploring 27.10 Dynamic Text behavior.
### Independent exercise
Create a circular seal with a curved top caption and a straight subtitle.
### Completion criteria
Type remains editable and avoids overlap.
### Knowledge check
What does path text follow?
- A raster mask
- History states
- A vector baseline
**Answer:** A vector baseline. Glyph positions are laid out along a geometric baseline.
### Connections
s07l06; s06l06

## s07l06 — Layout system and reusable mockup
**Stage 7:** Typography, shapes & paths  
**Objective:** Explain and independently execute layout system and reusable mockup.  
**Prerequisites:** s07l05
### Concept and principle
Reusable graphics use guides, named layers, Smart Objects and text styles. A mockup should separate replaceable content from lighting, surface detail and branding.
### Location (Windows)
View > New Guide; File > Place Embedded; Window > Layers
### Walkthrough
1. Create a 1600 × 900 px document and guides for 64 px margins.
2. Draw a device/screen placeholder with a rectangular Shape layer.
3. Place the included color-palette PNG as an embedded Smart Object; position it over the screen.
4. Add editable heading, subtitle and call-to-action text in groups.
### Expected result
Layout remains aligned and each asset is replaceable without flattening.
### Why it works
Modularity keeps content swaps separate from permanent scene design.
### Practical application
Use templates with replaceable Smart Objects for a repeatable campaign or client presentation.
### Common mistake and fix
A stretched placeholder can distort imported art; preserve aspect ratio.
### Efficiency tip
Use consistent margin spacing as a simple design system.
### Independent exercise
Swap the placed image with a different PNG while preserving headline placement.
### Completion criteria
No overlapping text, inconsistent margins, or misplaced layers.
### Knowledge check
What makes a mockup reusable?
- Repeated destructive crops
- Separate editable content and structure
- One flattened image
**Answer:** Separate editable content and structure. Modularity keeps content swaps separate from permanent scene design.
### Connections
s08l01; s07l01

## Stage 7 project — Typographic poster
Create a 1200 × 1600 poster with two type sizes, correct tracking/leading, 3 vector shapes and a Bézier icon.
**Pass condition:** Editable live text; consistent 64 px margins; no overflow.

# Stage 8 — Photography & color
Make principled tonal, color, RAW and output decisions.

## s08l01 — Histogram, exposure and tonal clipping
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute histogram, exposure and tonal clipping.  
**Prerequisites:** s07l06
### Concept and principle
Histogram graphs the number of pixels at tonal values. It reveals distribution and possible clipping but does not declare a single correct exposure; a night scene may naturally cluster left.
### Location (Windows)
Window > Histogram; Layer > New Adjustment Layer > Levels
### Walkthrough
1. Open practice/tone-gradient.png and show Window > Histogram.
2. Add a Levels adjustment layer.
3. Move black and white point sliders inward slowly, watching endpoints; then reset and move midtone slider.
4. Observe whether fine gradient steps lose distinction near the extremes.
### Expected result
Distribution and perceived contrast change; extreme endpoint changes clip detail.
### Why it works
Levels remaps tonal values using input black, gamma-like midtone and white controls.
### Practical application
Use histograms and Levels to diagnose tonal clipping before interpreting a photograph by screen brightness alone.
### Common mistake and fix
Never force every histogram to span full width by habit.
### Efficiency tip
Use clipping preview methods when available and inspect at 100%.
### Independent exercise
Make two versions: gentle contrast and intentionally clipped contrast.
### Completion criteria
Explain which image retained more steps in bright and dark regions.
### Knowledge check
What does a histogram primarily show?
- Tonal frequency distribution
- Exact color truth
- Printer resolution
**Answer:** Tonal frequency distribution. Levels remaps tonal values using input black, gamma-like midtone and white controls.
### Connections
s08l02; s07l02

## s08l02 — Curves and channel-level color balance
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute curves and channel-level color balance.  
**Prerequisites:** s08l01
### Concept and principle
Curves independently remaps each channel, enabling contrast and color correction. Multiple anchored points let you preserve some values while changing others; aggressive curves can posterize smooth tones.
### Location (Windows)
Layer > New Adjustment Layer > Curves; Window > Properties
### Walkthrough
1. Open a colorful practice image and add Curves adjustment.
2. Place two anchors around quarter and three-quarter tones, build a gentle S curve.
3. Choose Red channel and lift the midtone slightly; observe warmth shift.
4. Undo color move, then compare composite RGB and single-channel results.
### Expected result
S curve boosts perceived midtone contrast; red-channel lift warms affected regions.
### Why it works
Per-channel mappings alter color balance because RGB outputs no longer change identically.
### Practical application
Use Curves for selective contrast and neutral color corrections that require channel-level precision.
### Common mistake and fix
Large single-channel edits may tint intended neutrals.
### Efficiency tip
Use multiple anchor points to protect highlights and shadows.
### Independent exercise
Fix a deliberately cool image with an adjustable channel curve.
### Completion criteria
Neutral grays remain nearly neutral while overall color becomes more plausible.
### Knowledge check
Which Curves channel changes red without directly modifying green mapping?
- RGB composite
- Luminosity only
- Red
**Answer:** Red. Per-channel mappings alter color balance because RGB outputs no longer change identically.
### Connections
s08l03; s07l03

## s08l03 — White balance, HSL and selective grading
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute white balance, hsl and selective grading.  
**Prerequisites:** s08l02
### Concept and principle
White balance neutralizes lighting tint; HSL adjustments target hue families, saturation and luminance. Color grading is a deliberate creative look layered on a technically credible base.
### Location (Windows)
Layer > New Adjustment Layer > Color Balance; Layer > New Adjustment Layer > Hue/Saturation
### Walkthrough
1. Open practice/color-palette.png as a reference for stable colors.
2. Add Color Balance adjustment and inspect Midtones Cyan/Red changes; reset afterward.
3. Add Hue/Saturation adjustment; choose a named color range instead of Master.
4. Move Hue modestly and observe which swatches react.
### Expected result
Selected color families change while some other colors remain comparatively steady.
### Why it works
Channel weighting and hue classification are different control models.
### Practical application
Use local color-family corrections to fix casts or build a reproducible creative grade.
### Common mistake and fix
Strong saturation increases can clip output gamut and skin tones.
### Efficiency tip
Use masks for global adjustments that contaminate unrelated areas.
### Independent exercise
Build a natural and a stylized grade using separate adjustment groups.
### Completion criteria
Both can be toggled independently without source loss.
### Knowledge check
Which adjusts one color family without shifting all hues equally?
- Crop
- Targeted Hue/Saturation range
- Image Size
**Answer:** Targeted Hue/Saturation range. Channel weighting and hue classification are different control models.
### Connections
s08l04; s07l04

## s08l04 — RAW development and Camera Raw Smart Objects
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute raw development and camera raw smart objects.  
**Prerequisites:** s08l03, s04l02
### Concept and principle
Camera Raw interprets sensor data and stores edits non-destructively; JPEG and TIFF can enter its tools but cannot recover data already discarded by camera processing. Open as Smart Object to preserve reopenable raw controls.
### Location (Windows)
File > Open (select a supported camera RAW file); Filter > Camera Raw Filter; Help > About Plug-In > Camera Raw
### Walkthrough
1. Open a supported owned camera RAW file via File > Open; review white balance and exposure in Camera Raw.
2. Hold Shift when the Open Image button offers Open Object (label varies by context) or use Camera Raw workflow options to open as Smart Object.
3. Double-click the Smart Object thumbnail in Layers to reopen Camera Raw settings.
4. For a non-RAW image converted to Smart Object, compare Filter > Camera Raw Filter.
### Expected result
Raw Smart Object retains revisable develop settings; ordinary filter works on rendered pixels.
### Why it works
RAW processing starts with sensor measurements, while Camera Raw Filter receives an already-rendered image.
### Practical application
Use Camera Raw Smart Objects when exposure/white balance may need to be changed after the Photoshop composite is built.
### Common mistake and fix
Camera RAW is not the same as Photoshop Raw file format.
### Efficiency tip
Check supported camera models and Camera Raw plug-in version for new cameras.
### Independent exercise
Develop a RAW landscape in two separate mood versions.
### Completion criteria
Reopen a saved Smart Object and adjust white balance without re-importing.
### Knowledge check
What is preserved by a RAW Smart Object?
- Reopenable RAW development settings
- Infinite sensor detail
- An unchanged JPEG export
**Answer:** Reopenable RAW development settings. RAW processing starts with sensor measurements, while Camera Raw Filter receives an already-rendered image.
### Connections
s08l05; s07l05

## s08l05 — RGB, CMYK, Lab, grayscale and bit depth
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute rgb, cmyk, lab, grayscale and bit depth.  
**Prerequisites:** s08l04
### Concept and principle
Color mode defines channels; profiles interpret numbers; bit depth controls channel precision. RGB generally suits photo/screen editing, CMYK depends on print process, Lab separates perceptual lightness/chroma axes.
### Location (Windows)
Image > Mode; Edit > Convert to Profile; Edit > Color Settings
### Walkthrough
1. Duplicate a colorful PSD and inspect Image > Mode > RGB Color and 8 Bits/Channel.
2. Open Edit > Convert to Profile; inspect available destination spaces without committing at first.
3. Make a copy and try Image > Mode > Grayscale, noting the loss of color info.
4. Keep original RGB master untouched for comparison.
### Expected result
Grayscale copy loses chromatic information; profile conversion affects numerical representation.
### Why it works
The same numbers appear differently under different color interpretations.
### Practical application
Use mode, bit depth and ICC profile discipline to avoid color shifts between editing, export and print.
### Common mistake and fix
Assign Profile and Convert to Profile are not interchangeable.
### Efficiency tip
Obtain printer-specific ICC guidance before committing to CMYK conversion.
### Independent exercise
Produce two named variants for display and grayscale proofing.
### Completion criteria
Original RGB file opens unchanged; profile choices documented.
### Knowledge check
Which action preserves appearance better across profiles when performed correctly?
- Blindly assign unrelated profile
- Delete ICC metadata
- Convert to Profile
**Answer:** Convert to Profile. The same numbers appear differently under different color interpretations.
### Connections
s08l06; s07l06

## s08l06 — Soft proofing, gamut and print preparation
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute soft proofing, gamut and print preparation.  
**Prerequisites:** s08l05
### Concept and principle
Soft proofing simulates an output profile on your monitor; gamut warnings are approximations, not a substitute for a calibrated display and printer proof. Print success depends on PPI, profile, paper and output sharpening.
### Location (Windows)
View > Proof Setup > Custom; View > Proof Colors; File > Print
### Walkthrough
1. Open a finished RGB image and make a duplicate.
2. Choose View > Proof Setup > Custom and select a real printer/paper ICC if supplied; otherwise use an available reference profile and label it a simulation.
3. Toggle View > Proof Colors.
4. Inspect Image Size print dimensions with Resample disabled and confirm document bleed requirements externally.
### Expected result
Soft-proof appearance may change, but source pixels are not converted merely by toggling proof.
### Why it works
Display color management models expected output gamut and tone behavior.
### Practical application
Use soft proofing before committing to an actual printer or narrow-gamut output destination.
### Common mistake and fix
Do not promise precise print color without paper, printer, ink and profile details.
### Efficiency tip
Preserve the tagged RGB master and supply printer-requested format separately.
### Independent exercise
Make an annotated proofing checklist for a 6 × 4 inch print at 300 PPI.
### Completion criteria
Target output has at least 1800 × 1200 pixels without invented detail.
### Knowledge check
Does View > Proof Colors permanently convert image pixels?
- Only in PSD
- No
- Yes
**Answer:** No. Display color management models expected output gamut and tone behavior.
### Connections
s08l07; s08l01

## s08l07 — Sharpening, noise and HDR discipline
**Stage 8:** Photography & color  
**Objective:** Explain and independently execute sharpening, noise and hdr discipline.  
**Prerequisites:** s08l06
### Concept and principle
Sharpening boosts local contrast; it cannot truly reconstruct lost focus. Noise reduction trades grain against small detail. HDR 32-bit workflows have display and export restrictions, so test final targets.
### Location (Windows)
Filter > Sharpen > Smart Sharpen; Filter > Noise > Reduce Noise; Image > Mode
### Walkthrough
1. Duplicate a detailed photo or use practice/retouch-dots.png.
2. Convert duplicate to Smart Object; apply Filter > Sharpen > Smart Sharpen with a small Amount and Radius.
3. At 100%, compare halos around high-contrast lines; adjust downward.
4. Try a noise-reduction filter on a separate Smart Object and compare fine detail.
### Expected result
Moderate sharpening clarifies edges; too much creates light/dark halos and artificial texture.
### Why it works
Sharpening and denoising are competing spatial-frequency operations.
### Practical application
Use controlled final-size sharpening and noise reduction in photographic delivery without introducing halos.
### Common mistake and fix
Never judge sharpening solely at Fit on Screen.
### Efficiency tip
Do output sharpening only after final pixel dimensions are fixed.
### Independent exercise
Create a before/after crop for web versus print sharpness.
### Completion criteria
Edges are enhanced but no visible bright halos or plastic texture appear.
### Knowledge check
What does oversharpening commonly produce?
- Bright/dark edge halos
- Extra sensor information
- Larger gamut
**Answer:** Bright/dark edge halos. Sharpening and denoising are competing spatial-frequency operations.
### Connections
s09l01; s08l02

## Stage 8 project — Color-managed portrait and print proof
Prepare a neutral and creative grade, inspect histogram, record output profile and native print size.
**Pass condition:** No accidental clipping; ICC assumptions documented.

# Stage 9 — Advanced compositing
Integrate disparate source elements believably.

## s09l01 — Composite planning: light, camera and scale
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute composite planning: light, camera and scale.  
**Prerequisites:** s08l07, s03l03, s04l02, s08l02
### Concept and principle
A convincing composite must agree in horizon, perspective, relative scale, direction of light, sharpness, noise and color. Solving camera geometry first avoids wasting time on effects.
### Location (Windows)
File > Place Embedded; Edit > Free Transform; View > Rulers
### Walkthrough
1. Create a background with a visible floor/horizon from simple shape layers.
2. Place an isolated PNG shape as a Smart Object.
3. Align its apparent base with the floor plane and scale it relative to a known reference.
4. Draw arrows on a separate planning layer showing camera horizon and light direction.
### Expected result
Placed subject occupies a plausible plane with declared light and size assumptions.
### Why it works
Visual plausibility emerges from consistency across several independent cues.
### Practical application
Use geometry and lighting planning to prevent believable individual assets from producing an implausible overall composite.
### Common mistake and fix
Matching colors cannot fix impossible perspective.
### Efficiency tip
Plan in grayscale before refining saturation.
### Independent exercise
Assemble a three-object scene and write a one-sentence lighting plan.
### Completion criteria
All objects share coherent horizon and light direction.
### Knowledge check
What should be solved before elaborate grading?
- Decorative texture
- Export compression
- Perspective and scale
**Answer:** Perspective and scale. Visual plausibility emerges from consistency across several independent cues.
### Connections
s09l02; s08l03

## s09l02 — Realistic contact and cast shadows
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute realistic contact and cast shadows.  
**Prerequisites:** s09l01, s04l03
### Concept and principle
Contact shadows anchor objects where they touch a plane; cast shadows project away from a light source and typically soften with distance. A single black Gaussian Blur shadow rarely fits every scene.
### Location (Windows)
Layer > New > Layer; Edit > Transform; Filter > Blur > Gaussian Blur
### Walkthrough
1. Place an isolated object above a light floor layer.
2. Create a new shadow layer beneath it and paint a tight dark contact shape.
3. Draw a longer low-opacity cast silhouette, transform it along floor direction.
4. Convert shadow layer to Smart Object, blur slightly and reduce opacity.
### Expected result
Object feels attached to the plane; shadow direction follows planned light.
### Why it works
Light occlusion reduces illumination in geometrically consistent regions.
### Practical application
Use separate contact/cast shadows for believable product insertions and ground-plane integration.
### Common mistake and fix
Hard contact edges and distant shadow softness should not be identical.
### Efficiency tip
Use separate contact and cast shadow layers for control.
### Independent exercise
Produce two versions of same scene with different light directions.
### Completion criteria
Each shadow direction and softness matches its chosen light.
### Knowledge check
Which shadow anchors an object at its base?
- Outer Glow
- Contact shadow
- Lens flare
**Answer:** Contact shadow. Light occlusion reduces illumination in geometrically consistent regions.
### Connections
s09l03; s08l04

## s09l03 — Edge integration and local color matching
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute edge integration and local color matching.  
**Prerequisites:** s09l02
### Concept and principle
Edge fringing, chromatic mismatch and inappropriate focus announce a cutout. Use subject masks, Curves, local color adjustments and selective blur/grain instead of one global filter.
### Location (Windows)
Select > Select and Mask; Layer > New Adjustment Layer > Curves
### Walkthrough
1. Place an isolated object above a contrasting background.
2. Inspect cutout at 100% on both dark and light backgrounds.
3. Refine layer mask edge, then clip a Curves adjustment to subject.
4. Match subject black/white points to scene and add subtle edge softening only where needed.
### Expected result
Subject no longer carries a conspicuous fringe; tonal range aligns with background.
### Why it works
Compositing succeeds when each edge reproduces the background transition expected by the viewer.
### Practical application
Use edge and color matching when a good cutout still looks pasted onto a different background.
### Common mistake and fix
Global blur to hide a bad mask destroys subject detail.
### Efficiency tip
Evaluate cutouts at both 100% and final output zoom.
### Independent exercise
Insert a new cutout into two different scenes and refine each separately.
### Completion criteria
No obvious halo, incorrect sharpness or color boundary at actual viewing size.
### Knowledge check
What is the most targeted way to fix subject-only tone?
- Clipped Curves adjustment
- Global Exposure adjustment
- Change canvas size
**Answer:** Clipped Curves adjustment. Compositing succeeds when each edge reproduces the background transition expected by the viewer.
### Connections
s09l04; s08l05

## s09l04 — Depth, atmosphere and selective focus
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute depth, atmosphere and selective focus.  
**Prerequisites:** s09l03
### Concept and principle
Distance tends to reduce contrast and sometimes shift hue toward atmospheric light; depth of field depends on camera focus and aperture. Apply effects by depth groups instead of blanket fog and blur.
### Location (Windows)
Layer masks; Filter > Blur > Gaussian Blur
### Walkthrough
1. Make a three-plane scene with foreground, midground and background shapes.
2. Convert background to Smart Object and apply mild Gaussian Blur.
3. Add a pale atmosphere layer, mask it to reveal mostly distant objects.
4. Compare layers with and without reductions in distant contrast.
### Expected result
Far objects appear less contrasted and softer, while foreground retains detail.
### Why it works
Scattering and focus cues help indicate distance.
### Practical application
Use depth cues and local atmosphere for layered landscapes, posters and concept art.
### Common mistake and fix
Uniform blur makes the entire scene look out of focus.
### Efficiency tip
Vary effect strength by depth masks and light sources.
### Independent exercise
Build three distinct depth bands and caption which cues create separation.
### Completion criteria
Foreground and distance read as different planes even at thumbnail size.
### Knowledge check
Which plane usually receives the strongest atmospheric haze?
- Near focal subject
- All equally
- Far background
**Answer:** Far background. Scattering and focus cues help indicate distance.
### Connections
s09l05; s08l06

## s09l05 — Displacement and realistic surface mockups
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute displacement and realistic surface mockups.  
**Prerequisites:** s09l04, s04l02, s07l04
### Concept and principle
Displacement maps perturb coordinates using tonal data from a surface map; they help graphics inherit material folds or curvature. They do not automatically reproduce realistic surface shading.
### Location (Windows)
Filter > Distort > Displace; File > Save As
### Walkthrough
1. Create a grayscale texture and save it locally as a PSD displacement map.
2. Place a logo as a Smart Object over a textured base image.
3. Use Filter > Distort > Displace on a suitable raster or Smart Object layer, choose modest horizontal/vertical scale and select the map PSD.
4. Try Multiply or luminosity blending and mask unwanted areas.
### Expected result
Logo geometry follows some surface undulations but remains visually readable.
### Why it works
A map converts grayscale changes to positional offsets; shading must still be integrated.
### Practical application
Use displacement maps where a graphic must conform to fabric, paper or architectural surfaces.
### Common mistake and fix
Exaggerated displacement creates warped lettering and obvious artifact.
### Efficiency tip
Start with small displacement values and keep the map at appropriate dimensions.
### Independent exercise
Mock a graphic onto a wrinkled material and retain original flat logo.
### Completion criteria
The logo follows folds without severe tears or inconsistent shadows.
### Knowledge check
What does a displacement map encode?
- Printer profile
- Geometric pixel offsets
- Font licenses
**Answer:** Geometric pixel offsets. A map converts grayscale changes to positional offsets; shading must still be integrated.
### Connections
s09l06; s08l07

## s09l06 — Frequency separation and advanced retouch judgement
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute frequency separation and advanced retouch judgement.  
**Prerequisites:** s09l05, s05l04, s08l05
### Concept and principle
Frequency separation places broad color/tone and fine texture on different layers. It can be powerful but introduces halos, plastic skin and workflow overhead if used automatically. Start with local healing and dodge/burn instead.
### Location (Windows)
Filter > Blur > Gaussian Blur; Image > Apply Image (advanced)
### Walkthrough
1. Duplicate an owned test image twice and name layers low frequency and high frequency.
2. Blur the low frequency layer only enough to reduce fine texture.
3. Study Image > Apply Image options and channel/bit-depth dependence before computing high frequency; avoid assuming one formula fits every document.
4. Compare with an ordinary healing/dodge-burn edit and keep the result that retains texture.
### Expected result
A properly constructed pair can reproduce the source when combined; careless settings change tone.
### Why it works
Spatial frequencies describe detail scale, not separate physical layers in the photographed subject.
### Practical application
Use frequency separation only where a precise diagnosis justifies separating texture from broad tonal changes.
### Common mistake and fix
Do not use unverified one-click Apply Image formulas across 8/16/32-bit modes.
### Efficiency tip
Begin with a reversible duplicate and validate reconstruction before retouching.
### Independent exercise
Document a before/after explaining why frequency separation was or was not necessary.
### Completion criteria
No plastic texture, halos or color bleeding around boundaries.
### Knowledge check
Is frequency separation always the preferred portrait workflow?
- No
- Yes
- Only for CMYK
**Answer:** No. Spatial frequencies describe detail scale, not separate physical layers in the photographed subject.
### Connections
s09l07; s09l01

## s09l07 — Blend layers into a high-quality final composite
**Stage 9:** Advanced compositing  
**Objective:** Explain and independently execute blend layers into a high-quality final composite.  
**Prerequisites:** s09l06
### Concept and principle
Final compositing integrates shadows, local grading, common grain, edge quality, proofing and delivery. A unified adjustment can help, but it must not conceal unresolved geometry.
### Location (Windows)
Layer > New Adjustment Layer > Curves; File > Export > Export As
### Walkthrough
1. Open a composite with at least three independent layer groups.
2. Inspect perspective and masks at 100% before final grading.
3. Create a restrained top-level Curves grade, optionally add controlled texture on a separate layer.
4. Export PNG/JPEG and compare at final viewing size with the PSD version.
### Expected result
Exported scene looks coherent at both actual pixels and reduced size.
### Why it works
Final cohesion combines local corrections with global rendering consistency.
### Practical application
Use systematic final review to catch compositing defects that global color grading alone cannot fix.
### Common mistake and fix
A global color overlay cannot repair incorrect edges or scale.
### Efficiency tip
Use a final visual checklist and preserve source groups.
### Independent exercise
Deliver an 1800 × 1200 scene with editable object groups and a flattened proof.
### Completion criteria
No obvious clipped mask, unsupported shadow, missing source or accidental crop.
### Knowledge check
Which is the final quality standard?
- Maximum filter count
- Smallest PSD possible
- Cohesion at actual output size
**Answer:** Cohesion at actual output size. Final cohesion combines local corrections with global rendering consistency.
### Connections
s10l01; s09l02

## Stage 9 project — Multi-plane photo composite
Composite subject, floor, sky and graphic insert with perspective, shadows, haze and selective color adjustments.
**Pass condition:** No floating object; coherent key-light direction and mask boundaries.

# Stage 10 — Professional production
Deliver many assets reliably with automation and collaboration.

## s10l01 — Folder structure, asset naming and linked delivery
**Stage 10:** Professional production  
**Objective:** Explain and independently execute folder structure, asset naming and linked delivery.  
**Prerequisites:** s09l07
### Concept and principle
A professional source package must retain original assets, rights notes, working PSDs, exports, and versioned revisions. File dependencies should survive a transfer to another Windows machine.
### Location (Windows)
File > Place Linked; File > Save As
### Walkthrough
1. Create folders source, work, exports and references in Windows File Explorer.
2. Place a linked local PNG from source into a new PSD.
3. Save PSD into work and export a PNG into exports.
4. Copy the entire project folder to a new location and open the PSD from there; relink if required.
5. After saving the PSD, inspect File > Package as Adobe’s built-in option to gather linked source assets, and verify packaged files before handoff.
### Expected result
PSD opens with complete visual content and exports are clearly separated.
### Why it works
An editable document is only portable if dependencies and metadata travel with it.
### Practical application
Use predictable source/work/export folders and packaging for revisable files transferred across computers.
### Common mistake and fix
Absolute or changed link paths can break when folders move.
### Efficiency tip
Bundle linked source files and avoid arbitrary names like final_FINAL2.
### Independent exercise
Prepare a folder that another editor can inspect without a verbal explanation.
### Completion criteria
Every linked file exists and file names indicate purpose.
### Knowledge check
Where should immutable original inputs live?
- temporary cache
- source folder
- exports folder only
**Answer:** source folder. An editable document is only portable if dependencies and metadata travel with it.
### Connections
s10l02; s09l03

## s10l02 — Actions and batch processing
**Stage 10:** Professional production  
**Objective:** Explain and independently execute actions and batch processing.  
**Prerequisites:** s10l01, s01l03, s02l01
### Concept and principle
Actions record repeatable UI operations; Batch applies them to many files. Their reliability depends on dialogs, file assumptions and target naming. Start with a small test set.
### Location (Windows)
Window > Actions; File > Automate > Batch
### Walkthrough
1. Make three copies of practice/color-palette.png in a temporary folder.
2. Open Window > Actions, create an action and record a safe resize or adjustment on an opened copy.
3. Stop recording and test action on one different copy.
4. Choose File > Automate > Batch and point Source/Destination to separate folders; inspect output before scaling up.
### Expected result
Consistent edits appear in multiple outputs without changing source files.
### Why it works
Automation replays a recorded sequence with limited contextual reasoning.
### Practical application
Use Actions and Batch for repeated, tested production tasks with strict output naming safeguards.
### Common mistake and fix
Recording Save As with absolute paths can cause overwrites.
### Efficiency tip
Test one file, then three, before processing hundreds.
### Independent exercise
Batch-process three small files into a different output directory.
### Completion criteria
All three have intended dimensions, unique names and originals remain untouched.
### Knowledge check
What should happen before a large batch run?
- Test small dataset
- Delete masters
- Assume every image identical
**Answer:** Test small dataset. Automation replays a recorded sequence with limited contextual reasoning.
### Connections
s10l03; s09l04

## s10l03 — Templates and Smart Object replacement
**Stage 10:** Professional production  
**Objective:** Explain and independently execute templates and smart object replacement.  
**Prerequisites:** s10l02
### Concept and principle
Templates encode stable geometry and interchangeable content. Linked or embedded Smart Objects let designers update a logo or photo without rebuilding layout every time.
### Location (Windows)
Layer > Smart Objects > Replace Contents; File > Place Embedded
### Walkthrough
1. Make a product card with a logo Smart Object and editable title layer.
2. Duplicate the entire PSD as a variant.
3. Right-click logo Smart Object and choose Replace Contents (or Layer > Smart Objects > Replace Contents).
4. Pick another same-aspect-ratio PNG and adjust its transform only if required.
### Expected result
Replacement updates the artwork within the preserved layout.
### Why it works
A Smart Object container separates content from scene transformations and effects.
### Practical application
Use Smart Object replacement to generate dozens of consistent visual mockup variants.
### Common mistake and fix
Replacement assets with different aspect ratios may fit unpredictably.
### Efficiency tip
Use standardized asset boxes and document expected proportions.
### Independent exercise
Produce three branded variations from one saved master.
### Completion criteria
All maintain margins, text hierarchy and shadow style.
### Knowledge check
What changes when replacing Smart Object contents?
- All Photoshop preferences
- Document mode automatically
- Its source artwork
**Answer:** Its source artwork. A Smart Object container separates content from scene transformations and effects.
### Connections
s10l04; s09l05

## s10l04 — Scripting and supported extensibility boundaries
**Stage 10:** Professional production  
**Objective:** Explain and independently execute scripting and supported extensibility boundaries.  
**Prerequisites:** s10l03
### Concept and principle
Actions are built-in; scripting and plugins can automate richer operations but require compatibility checks. UXP is a modern Photoshop extensibility system; legacy script examples may rely on different APIs.
### Location (Windows)
File > Scripts; Plugins menu (when installed)
### Walkthrough
1. Open File > Scripts and inspect available built-in commands.
2. Record a simple Action as a baseline no-code solution.
3. Review a script only from a trusted local source and determine required Photoshop API/version.
4. Run scripts on copies, inspect output, and check logs if they fail.
### Expected result
Built-in scripts appear where installed; no third-party tool is needed for the core lessons.
### Why it works
Automation code is versioned software and must be treated as a dependency.
### Practical application
Use vetted scripts and plug-ins where a supported automation capability exceeds what Actions can reliably do.
### Common mistake and fix
Do not blindly run untrusted JSX or UXP plugin code.
### Efficiency tip
Prefer Actions for simple repeatable editing; Adobe UXP plug-ins and Photoshop scripting are different extension methods with distinct support and security constraints.
### Independent exercise
Write an automation plan identifying which operations need only Actions versus scripting.
### Completion criteria
Plan includes inputs, outputs, safe retries and test conditions.
### Knowledge check
Which is built into Photoshop without a plugin?
- External cloud API
- Actions panel
- Any downloaded automation extension
**Answer:** Actions panel. Automation code is versioned software and must be treated as a dependency.
### Connections
s10l05; s09l06

## s10l05 — Export As, Quick Export and format decisions
**Stage 10:** Professional production  
**Objective:** Explain and independently execute export as, quick export and format decisions.  
**Prerequisites:** s10l04, s02l04, s08l05
### Concept and principle
Export is a delivery transformation, not a working-file save. PNG supports transparent graphics; JPEG is lossy and opaque; formats such as WebP depend on receiving system support and export options.
### Location (Windows)
File > Export > Export As; File > Export > Quick Export (output format follows Export preferences)
### Walkthrough
1. Create a 1080 × 1080 design with text and a transparent margin.
2. Use File > Export > Export As; compare PNG and JPEG available settings.
3. Export one PNG with transparency and one JPEG at an appropriate quality.
4. Reopen both on a contrasting background and inspect size and edge behavior.
### Expected result
PNG preserves transparency; JPEG may show compression and fills transparent areas.
### Why it works
Different encoders trade alpha, size and artifact behavior.
### Practical application
Use format-appropriate export when exact transparency, dimensions and compression are delivery requirements.
### Common mistake and fix
Do not rely on a flattened PNG to restore text editability.
### Efficiency tip
Always inspect exported assets, not only the PSD.
### Independent exercise
Deliver one social banner as JPEG and one icon as transparent PNG.
### Completion criteria
Both fit exact requested dimensions and display correctly in target viewer.
### Knowledge check
Which output is suited to transparent logos?
- PNG
- JPEG
- Flattened RGB-only BMP
**Answer:** PNG. Different encoders trade alpha, size and artifact behavior.
### Connections
s10l06; s09l07

## s10l06 — Print, preflight and external application handoffs
**Stage 10:** Professional production  
**Objective:** Explain and independently execute print, preflight and external application handoffs.  
**Prerequisites:** s10l05
### Concept and principle
Print preflight covers dimensions, bleed, safe area, ICC conversion and fonts; cross-app delivery requires knowing what stays editable. Illustrator paths and Lightroom develop adjustments are not identical to Photoshop layers.
### Location (Windows)
Image > Image Size; Edit > Convert to Profile; File > Print
### Walkthrough
1. Open a print-sized PSD and check pixel dimensions with Image > Image Size.
2. Inspect type layers for missing fonts and links for absent assets.
3. Use View > Proof Setup > Custom if the print profile is supplied.
4. Save a versioned master plus a printer-requested delivery copy; communicate bleed/trimming externally.
### Expected result
You have a clean production file and explicit unresolved printer requirements.
### Why it works
Production constraints come from a destination system, not one universal print preset.
### Practical application
Use preflight checklists when delivering for a particular print shop or handoff application.
### Common mistake and fix
There is no universally correct CMYK profile for every printer.
### Efficiency tip
Use the destination printer’s specification rather than generic recipes.
### Independent exercise
Prepare a 5 × 7 inch poster briefing with print specification checklist.
### Completion criteria
Required profile, bleed, stock and export format are explicitly listed as confirmed or TBD.
### Knowledge check
Before converting to CMYK, what is needed?
- A random profile
- Only a JPEG filename
- Destination print conditions/profile
**Answer:** Destination print conditions/profile. Production constraints come from a destination system, not one universal print preset.
### Connections
s11l01; s10l01

## Stage 10 project — Production export bundle
Build a reusable template, export three sizes and run/test one Action against 3 different source files.
**Pass condition:** Correct filenames/sizes; zero overwritten sources.

# Stage 11 — Performance & troubleshooting
Diagnose failures, bottlenecks and virtualized setups.

## s11l01 — GPU, memory and scratch disk triage
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute gpu, memory and scratch disk triage.  
**Prerequisites:** s10l06
### Concept and principle
Photoshop uses CPU, RAM, GPU and scratch disk for different tasks. Low scratch space, incompatible drivers or an unsupported GPU can cause lag, missing features and crashes.
### Location (Windows)
Edit > Preferences > Performance; Edit > Preferences > Scratch Disks
### Walkthrough
1. Open Edit > Preferences > Performance and note Memory Usage and detected GPU.
2. Confirm the intended scratch disk has substantial free space in Windows File Explorer.
3. Check Edit > Preferences > Scratch Disks for active locations; do not change them blindly.
4. Save your file and run one operation that previously lagged while monitoring system load.
### Expected result
You can identify whether memory, scratch space or GPU availability is an obvious bottleneck.
### Why it works
Photoshop spills work to disk when memory is inadequate; GPU functions require compatible capability.
### Practical application
Use performance diagnostics before changing Photoshop preferences or deleting scratch data.
### Common mistake and fix
Never clear unknown scratch files while Photoshop is running.
### Efficiency tip
Prefer internal fast SSD scratch space and tested graphics drivers.
### Independent exercise
Make a system inventory with RAM, free scratch space, GPU and driver version.
### Completion criteria
Inventory identifies at least two potential bottlenecks if present.
### Knowledge check
What resource handles spillover when RAM is insufficient?
- ICC profile
- Scratch disk
- Font manager
**Answer:** Scratch disk. Photoshop spills work to disk when memory is inadequate; GPU functions require compatible capability.
### Connections
s11l02; s10l02

## s11l02 — Windows VM graphics and feature limitations
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute windows vm graphics and feature limitations.  
**Prerequisites:** s11l01
### Concept and principle
A Windows guest needs virtualized DirectX feature support and real GPU capabilities; a Linux host GPU does not automatically become available to Photoshop inside the VM. Official Photoshop system requirements apply to the guest, but hypervisor support varies.
### Location (Windows)
Edit > Preferences > Performance; Help > System Info
### Walkthrough
1. Inside the Windows guest, open Help > System Info and record GPU/driver details.
2. Check Windows Device Manager > Display adapters for guest-presented hardware.
3. Open Photoshop Performance preferences and verify whether Use Graphics Processor can be selected.
4. If unsupported, test basic 2D workflows and compare with GPU-dependent ones without assuming pass-through works.
### Expected result
The guest’s actual graphics capability is documented and feature gaps are identified.
### Why it works
Virtual GPUs expose only their emulated or passed-through capabilities to the guest OS.
### Practical application
Use guest-visible GPU diagnostics before deciding if a Windows VM is suitable for GPU-dependent Photoshop work.
### Common mistake and fix
Do not claim PCIe passthrough or hardware acceleration exists because the host GPU is powerful.
### Efficiency tip
Use native Windows hardware when GPU-heavy features are essential and virtualization cannot satisfy them.
### Independent exercise
Create a VM compatibility report with Windows version, vRAM, DirectX level and Photoshop GPU status.
### Completion criteria
Report distinguishes Adobe minimums from practical VM observations.
### Knowledge check
What GPU matters to Photoshop in a VM?
- GPU capability exposed to guest
- Host specification alone
- Linux desktop theme
**Answer:** GPU capability exposed to guest. Virtual GPUs expose only their emulated or passed-through capabilities to the guest OS.
### Connections
s11l03; s10l03

## s11l03 — Crashes, resets and safe diagnostics
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute crashes, resets and safe diagnostics.  
**Prerequisites:** s11l02
### Concept and principle
Crashes can arise from drivers, plugins, fonts, corrupt preferences, scratch exhaustion or damaged documents. Isolate variables before resetting preferences or reinstalling.
### Location (Windows)
Help > System Info; Edit > Preferences > General
### Walkthrough
1. Save a separate backup and record the exact crash action.
2. Note installed Photoshop version via Help > About Photoshop and GPU information via Help > System Info.
3. Test with nonessential third-party plugins disabled and a small new document.
4. Only after preserving settings, use documented Reset Preferences on Quit and restart if indicated.
### Expected result
A reproducible trigger or narrowed category is recorded rather than guessed.
### Why it works
Controlled experiments change one variable at a time.
### Practical application
Use controlled, reversible troubleshooting before resetting preferences or blaming document corruption.
### Common mistake and fix
Resetting preferences may discard custom settings, presets and workspace changes.
### Efficiency tip
Export/back up preferences and presets first.
### Independent exercise
Write a troubleshooting incident log with symptoms, versions and 3 discriminating tests.
### Completion criteria
Another person could reproduce or eliminate the fault systematically.
### Knowledge check
What is the first good response to repeated crashes?
- Randomly delete files
- Flatten every PSD
- Record reproducible trigger and configuration
**Answer:** Record reproducible trigger and configuration. Controlled experiments change one variable at a time.
### Connections
s11l04; s10l04

## s11l04 — Missing fonts, links, color shifts and corruption
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute missing fonts, links, color shifts and corruption.  
**Prerequisites:** s11l03
### Concept and principle
Broken links and missing fonts change composition. Color shifts arise from unmanaged viewers, missing embedded profiles and proof settings. Corrupt documents require backups rather than optimistic destructive repairs.
### Location (Windows)
Window > Layers; Edit > Color Settings; File > Open
### Walkthrough
1. Open a PSD with linked content and inspect link warning icons.
2. Review text layers for missing fonts and compare a rendered preview with live text.
3. Check whether image has an embedded profile and inspect color settings; compare in a color-managed viewer.
4. Save a fresh copy before any relink or font replacement.
### Expected result
You can separate missing-dependency issues from profile/display differences.
### Why it works
Documents encode assets, text layout and color interpretation that depend on environment.
### Practical application
Use missing-font/link/profile checks before editing source pixels to fix a delivery mismatch.
### Common mistake and fix
Assigning a random ICC profile to fix a color mismatch can worsen it.
### Efficiency tip
Investigate embed/convert/viewer before changing pixel colors.
### Independent exercise
Produce a dependency checklist for a client PSD and verify linked assets.
### Completion criteria
No silent font substitution or missing photo remains at final export.
### Knowledge check
Which can cause text to reflow on another PC?
- Larger mouse cursor
- Missing font
- More scratch space
**Answer:** Missing font. Documents encode assets, text layout and color interpretation that depend on environment.
### Connections
s11l05; s10l05

## s11l05 — Large files, cache levels and robust recovery
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute large files, cache levels and robust recovery.  
**Prerequisites:** s11l04
### Concept and principle
Large PSDs may need PSB; cache levels influence preview performance, and recovery copies are not guaranteed. Separate working copies and periodic verified backups are essential.
### Location (Windows)
Edit > Preferences > Performance; File > Save As
### Walkthrough
1. Duplicate a multi-layer PSD and record its file size.
2. Inspect History & Cache settings in Performance without guessing ideal values.
3. If a document exceeds PSD format limits, choose PSB when saving and confirm receiving tools accept PSB.
4. Save versioned files to a backed-up drive and test reopening the most recent revision.
### Expected result
There is at least one recoverable editable copy separate from the active working file.
### Why it works
Recovery depends on valid stored content, not merely auto-recovery preferences.
### Practical application
Use PSB, versioned saves and reopening tests for very large, long-lived layered productions.
### Common mistake and fix
Do not assume auto-recovery is a full versioning/backup system.
### Efficiency tip
Verify a backup by opening it, not just checking file existence.
### Independent exercise
Design a 3-2-1-inspired backup plan for working PSDs and source assets.
### Completion criteria
Test restores at least one file and specifies storage locations.
### Knowledge check
What is PSB intended for?
- Large Photoshop documents
- Compressed web thumbnails
- Vector font installation
**Answer:** Large Photoshop documents. Recovery depends on valid stored content, not merely auto-recovery preferences.
### Connections
s11l06; s10l06

## s11l06 — Offline, account and AI availability
**Stage 11:** Performance & troubleshooting  
**Objective:** Explain and independently execute offline, account and ai availability.  
**Prerequisites:** s11l05
### Concept and principle
The manual is offline. Photoshop activation and subscription validation may require internet, and Adobe generative services can use cloud processing and credits. Some recent Remove Tool AI processing may use a locally downloaded model on supported hardware.
### Location (Windows)
Help > About Photoshop; Edit > Preferences > Performance; Creative Cloud desktop account/subscription information
### Walkthrough
1. Inspect the account status and known online requirements before a disconnected session.
2. For a local editing trial, use non-AI tools such as layers, masks, Clone Stamp and Curves.
3. If Remove Tool offers on-device versus cloud model options, note required download and hardware availability.
4. Keep manual files on both Linux and Windows; export website progress as JSON between machines.
### Expected result
You can distinguish editing that works locally from account- and network-dependent operations.
### Why it works
Offline reference availability does not imply every Photoshop feature is offline.
### Practical application
Use a dependency inventory before planning a disconnected editing session or relying on model-based AI tools.
### Common mistake and fix
Do not confuse newly introduced Beta AI Assisted Editor with stable tool behavior.
### Efficiency tip
Check credits and terms inside the live Adobe account for actual entitlement.
### Independent exercise
Create a two-column inventory of offline core editing and online-dependent services.
### Completion criteria
Each listed feature has a specific dependency rather than vague AI label.
### Knowledge check
Does a fully offline manual guarantee offline Generative Fill?
- Yes
- Only on Linux
- No
**Answer:** No. Offline reference availability does not imply every Photoshop feature is offline.
### Connections
s12l01; s11l01

## Stage 11 project — Technical incident report
Audit your own system and run a safe VM-or-native GPU, memory, scratch, account/offline diagnostic.
**Pass condition:** Document contains exact observed GPU, vRAM, Photoshop version and unknowns.

# Stage 12 — Mastery & capstones
Apply the entire skill system with evidence-based review.

## s12l01 — Portrait retouching capstone
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute portrait retouching capstone.  
**Prerequisites:** s11l06
### Concept and principle
Combine source preservation, selective healing, tonal dodge/burn, skin-texture protection and delivery review. Quality is judged against a plausible untouched reference.
### Location (Windows)
Healing Brush; Curves adjustment layers; File > Export > Export As
### Walkthrough
1. Choose an owned portrait and save a versioned PSD master.
2. Create cleanup layers for temporary defects and separate Dodge/Burn Curves masks.
3. Correct tone while preserving subject identity and texture.
4. Deliver a full-resolution JPEG and a two-panel before/after preview.
### Expected result
Portrait looks more polished but still natural under close inspection.
### Why it works
Local changes with editable layers are easier to audit and reverse.
### Practical application
Use a controlled portrait capstone to demonstrate texture preservation, layer hygiene and readable before/after evidence.
### Common mistake and fix
Over-retouching is not professional finish.
### Efficiency tip
Judge both 100% details and full-face expression.
### Independent exercise
Produce a final portrait and written edit log identifying each intervention.
### Completion criteria
At 100% pores and facial texture remain; no obvious healing repetition.
### Knowledge check
What is the main capstone standard?
- Maximal symmetry
- Natural, reversible improvement
- Zero remaining texture
**Answer:** Natural, reversible improvement. Local changes with editable layers are easier to audit and reverse.
### Connections
s12l02; s11l02

## s12l02 — Photo restoration capstone
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute photo restoration capstone.  
**Prerequisites:** s12l01
### Concept and principle
Repair a damaged photo while separating evidenced recovery from imaginative reconstruction. A versioned archive and change log are part of technical quality.
### Location (Windows)
Clone Stamp; Spot Healing; Levels; Layers
### Walkthrough
1. Scan or choose owned restoration material; keep immutable original.
2. Create separate tone and damage repair groups.
3. Use local cloning/healing with frequent resampling; label missing-content reconstruction as interpreted.
4. Deliver layered PSD and a contact sheet showing stages.
### Expected result
Damage is reduced without fabricating unmarked historical certainty.
### Why it works
Transparent restoration records what is known and what is inferred.
### Practical application
Use restoration deliverables to show an honest separation between documented recovery and interpreted detail.
### Common mistake and fix
Never overwrite the archival scan.
### Efficiency tip
Compare before/after at consistent scale and color-management settings.
### Independent exercise
Restore five distinct damaged regions with an edit log.
### Completion criteria
Original can be retrieved, and repaired areas remain individually reviewable.
### Knowledge check
Why record speculative reconstruction?
- It is not recoverable evidence
- It guarantees historical accuracy
- It reduces PSD size
**Answer:** It is not recoverable evidence. Transparent restoration records what is known and what is inferred.
### Connections
s12l03; s11l03

## s12l03 — Product advertisement capstone
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute product advertisement capstone.  
**Prerequisites:** s12l02
### Concept and principle
Product graphics combine extraction, contact shadows, controlled highlights, typography, color consistency and platform-specific output. Revision flexibility is part of the deliverable.
### Location (Windows)
Select > Select and Mask; Layer Styles; Type Tool; File > Export > Export As
### Walkthrough
1. Place an owned product photo over an editable background.
2. Refine mask, build contact and cast shadows on separate layers.
3. Add headline, offer and disclaimer text with hierarchy and safe margins.
4. Deliver a 1080 × 1350 JPEG and a transparent product PNG plus layered PSD.
### Expected result
Product is believable and both outputs have the requested dimensions.
### Why it works
Good advertising composition coordinates geometry, light and information.
### Practical application
Use a product campaign to integrate masks, shadows, typography and export requirements in one brief.
### Common mistake and fix
Do not make unsupported factual product claims in promotional text.
### Efficiency tip
Inspect type on a typical mobile-sized preview.
### Independent exercise
Make a product promo using no paid stock and no flattened working master.
### Completion criteria
Clear subject silhouette, readable text, no clipped shadows at crop edges.
### Knowledge check
Which PSD organization best supports revisions?
- One merged image
- Only smart filters
- Separate product, shadows, text and background
**Answer:** Separate product, shadows, text and background. Good advertising composition coordinates geometry, light and information.
### Connections
s12l04; s11l04

## s12l04 — Advanced scene-composite capstone
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute advanced scene-composite capstone.  
**Prerequisites:** s12l03
### Concept and principle
Build a multi-source environment through geometry, lighting and edge integration. The rubric prioritizes perceptual consistency over effect novelty.
### Location (Windows)
File > Place Embedded; Select and Mask; Curves; Smart Filters
### Walkthrough
1. Make a scene from at least three independently editable visual assets.
2. Set a common horizon and one key-light direction.
3. Integrate each subject with a mask, contact shadow and clipped color correction.
4. Apply a restrained common grade and export 1800 × 1200 at final quality.
### Expected result
Scene reads as one environment, with believable scale and lighting.
### Why it works
Plausibility is the sum of independent visual consistency tests.
### Practical application
Use a scene composite to prove camera, scale, mask, depth and light integration under final-size scrutiny.
### Common mistake and fix
Do not use color grading to hide incorrect perspective.
### Efficiency tip
Turn layers on/off during review to isolate mismatches.
### Independent exercise
Deliver source/PSD/export folders and note all source provenance.
### Completion criteria
At 100%, no major halos, contradicted light, floating objects or repeated cloned texture.
### Knowledge check
What should be audited before final grade?
- Font family count
- Scale, masks and light
- File compression only
**Answer:** Scale, masks and light. Plausibility is the sum of independent visual consistency tests.
### Connections
s12l05; s11l05

## s12l05 — Reusable campaign design capstone
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute reusable campaign design capstone.  
**Prerequisites:** s12l04
### Concept and principle
Campaign work demands one coherent design system across formats, predictable text reflow, Smart Object replacement and accurate exports. Production readiness is as important as beauty.
### Location (Windows)
File > Place Embedded; Window > Character; Actions; File > Export > Export As
### Walkthrough
1. Create one master design with groups for brand, image, text and background.
2. Adapt a square 1080 × 1080 version and a vertical 1080 × 1920 version as separate PSD variants.
3. Replace one Smart Object asset and adjust text safe areas.
4. Export both and inspect for accidental cropping and legibility.
### Expected result
Two formats share clear visual identity with correct safe zones.
### Why it works
A design system expresses stable rules while permitting composition changes.
### Practical application
Use a multi-format campaign to demonstrate portable assets and responsive design rather than blind scaling.
### Common mistake and fix
Simply scaling the whole square often crops text in vertical output.
### Efficiency tip
Design responsive compositions rather than blind resizes.
### Independent exercise
Deliver two sizes, master PSD and a short update guide.
### Completion criteria
Both are legible and editable with consistent typography.
### Knowledge check
What should remain stable across campaign formats?
- Design rules, not pixel coordinates
- Absolute text position
- Every crop box
**Answer:** Design rules, not pixel coordinates. A design system expresses stable rules while permitting composition changes.
### Connections
s12l06; s11l06

## s12l06 — Final assessment: end-to-end editable project
**Stage 12:** Mastery & capstones  
**Objective:** Explain and independently execute final assessment: end-to-end editable project.  
**Prerequisites:** s12l05, s09l07, s10l02, s10l05, s11l05
### Concept and principle
An expert-ready project proves fundamentals, compositing, retouching, typography, color, automation, output and technical handoff in one traceable artifact. Demonstrate decisions as well as mouse actions.
### Location (Windows)
All previously studied menus and panels
### Walkthrough
1. Choose a real brief: a three-format campaign built around a retouched original image.
2. Create an intact source archive and layered PSD with named adjustment, masking and typography groups.
3. Build one composite/mockup and automate at least one repeatable export or adjustment across three files.
4. Preflight exports for PNG transparency, JPEG dimensions, color profile, readability and expected recipient needs.
5. Write a one-page decision log and deliver all variants in a transferable folder.
### Expected result
Every output matches the brief and remains explainable and revisable.
### Why it works
Mastery is tested by controlled tradeoffs, diagnostic skill and reproducible delivery.
### Practical application
Use the final assignment as a repeatable evidence-based professional workflow from original files to checked handoff.
### Common mistake and fix
An attractive JPEG alone does not prove professional Photoshop competence.
### Efficiency tip
Peer-review the layered PSD, not just exported appearance.
### Independent exercise
Complete the entire project without relying on paid stock, plugins or Generative Fill.
### Completion criteria
Rubric: 20% preservation/structure; 20% masks/composite; 20% tonal/color; 15% typography/layout; 15% delivery; 10% documentation. Target ≥85% with no critical failure.
### Knowledge check
Which evidence best demonstrates complete mastery?
- Only one attractive thumbnail
- Shortcut memorization alone
- Editable project, verified outputs and decision log
**Answer:** Editable project, verified outputs and decision log. Mastery is tested by controlled tradeoffs, diagnostic skill and reproducible delivery.
### Connections
s12l01

## Stage 12 project — Complete campaign brief
Produce three-format advertisement, an optional advanced photo restoration, editable PSD, proof images and change log.
**Pass condition:** Target 85%+ final rubric; no critical source loss or missing linked assets.

# Reference encyclopedias

## Tools

### Move
**Purpose:** Moves selected layers or selections; can auto-select under configured options.  
**Location:** Toolbar > Move/Artboard tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** V  
**Controls:** Auto-Select; Show Transform Controls; alignment  
**Use:** Use with multiple selected layers for precise layouts.  
**Caution:** Dragging a locked or wrong layer appears to do nothing.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s02l03  

### Artboard
**Purpose:** Creates multiple layout canvases in one file.  
**Location:** Toolbar > Move/Artboard tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** V  
**Controls:** Preset dimensions; orientation; artboard properties  
**Use:** Useful for multiple screen-size variants.  
**Caution:** Artboards are not independent PSD files.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s10l05  

### Frame
**Purpose:** Creates image placeholder frames using shape boundaries.  
**Location:** Toolbar > Frame tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** K  
**Controls:** Rectangular/elliptical frames; frame content fit  
**Use:** Use for replacing photos inside layouts.  
**Caution:** A frame is not a normal empty raster selection.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l06  

### Rectangular Marquee
**Purpose:** Selects a rectangular pixel region.  
**Location:** Toolbar > Marquee tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** M  
**Controls:** Feather; selection mode; fixed size  
**Use:** Use for crisp tiles and straight areas.  
**Caution:** Nonzero Feather softens edges.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Elliptical Marquee
**Purpose:** Selects circular or elliptical regions.  
**Location:** Toolbar > Marquee tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** M  
**Controls:** Feather; fixed ratio; selection mode  
**Use:** Use for round badges and masked highlights.  
**Caution:** Dragging by eye may create an ellipse rather than circle.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Single Row Marquee
**Purpose:** Selects a one-pixel-high horizontal row.  
**Location:** Toolbar > Marquee tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Selection mode; location  
**Use:** Useful for exact row sampling or rules.  
**Caution:** At low zoom the selection can be hard to see.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Single Column Marquee
**Purpose:** Selects a one-pixel-wide vertical column.  
**Location:** Toolbar > Marquee tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Selection mode; location  
**Use:** Useful for precise column operations.  
**Caution:** Affected width is only one pixel.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Lasso
**Purpose:** Freehand selection traced with mouse or pen.  
**Location:** Toolbar > Lasso/Selection Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** L  
**Controls:** Feather; Add/Subtract; anti-alias  
**Use:** Use for rough subject boundaries.  
**Caution:** Hand jitter creates uneven edges.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Polygonal Lasso
**Purpose:** Connects straight selection segments.  
**Location:** Toolbar > Lasso/Selection Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** L  
**Controls:** Feather; Add/Subtract  
**Use:** Use for faceted objects and architecture.  
**Caution:** Every click adds a corner.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l01  

### Magnetic Lasso
**Purpose:** Suggests edges while cursor follows them.  
**Location:** Toolbar > Lasso/Selection Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** L  
**Controls:** Width; Contrast; Frequency  
**Use:** Useful for defined contrast edges.  
**Caution:** Low-contrast boundaries cause drift.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l02  

### Object Selection
**Purpose:** Detects a probable object from region or hover.  
**Location:** Toolbar > Object/Quick Selection/Magic Wand tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** W  
**Controls:** Rectangle/Lasso modes; Object Finder; selection operations  
**Use:** Use for recognizable objects.  
**Caution:** Detection is not final-quality masking.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l02  

### Quick Selection
**Purpose:** Paints a selection that expands toward edges.  
**Location:** Toolbar > Object/Quick Selection/Magic Wand tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** W  
**Controls:** Brush size; Add/Subtract; Sample All Layers  
**Use:** Use for manual-plus-assisted extraction.  
**Caution:** Fast strokes may spill across weak boundaries.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l02  

### Magic Wand
**Purpose:** Chooses similar contiguous or discontiguous colors.  
**Location:** Toolbar > Object/Quick Selection/Magic Wand tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** W  
**Controls:** Tolerance; Contiguous; Anti-alias  
**Use:** Use for flat-color graphics.  
**Caution:** Low tolerance leaves fringe; high selects too much.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l02  

### Selection Brush
**Purpose:** Paints selection regions directly.  
**Location:** Toolbar > Lasso/Selection Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** L  
**Controls:** Brush size; Add/Subtract; edge behavior  
**Use:** Use for irregular selectable areas.  
**Caution:** Painted selection is not itself a layer mask.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l02  

### Crop
**Purpose:** Reframes and optionally removes cropped pixels.  
**Location:** Toolbar > Crop/Slice tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** C  
**Controls:** Aspect ratio; Delete Cropped Pixels; straighten  
**Use:** Use to recompose photography.  
**Caution:** Destructive crop can remove hidden pixels.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s02l01  

### Perspective Crop
**Purpose:** Rectifies a photographed quadrilateral to rectangular edges.  
**Location:** Toolbar > Crop/Slice tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** C  
**Controls:** Corner handles; dimensions  
**Use:** Use for documents photographed at an angle.  
**Caution:** Severe correction stretches low-res detail.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s02l01  

### Slice
**Purpose:** Defines web slices for legacy sliced exports.  
**Location:** Toolbar > Crop/Slice tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** C  
**Controls:** Slice type; boundaries  
**Use:** Use only with legacy asset pipelines.  
**Caution:** Modern export usually favors individual assets.  
**Status:** Legacy workflow  
**Lesson:** s10l04  

### Slice Select
**Purpose:** Selects and edits existing slices.  
**Location:** Toolbar > Crop/Slice tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** C  
**Controls:** Slice properties; selection  
**Use:** Maintain existing sliced layouts.  
**Caution:** Does not select pixels for ordinary painting.  
**Status:** Legacy workflow  
**Lesson:** s10l04  

### Eyedropper
**Purpose:** Samples color from image or composite.  
**Location:** Toolbar > Eyedropper/Measurement tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** I  
**Controls:** Sample Size; Sample layers  
**Use:** Use to match colors in a design.  
**Caution:** Edge samples mix neighboring tones.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l03  

### Color Sampler
**Purpose:** Places persistent color readout sample points.  
**Location:** Toolbar > Eyedropper/Measurement tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** I  
**Controls:** Sample Size; Info readout  
**Use:** Use to compare color before/after edits.  
**Caution:** Readouts depend on selected color model.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s08l03  

### Ruler
**Purpose:** Measures distance and angle on image.  
**Location:** Toolbar > Eyedropper/Measurement tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** I  
**Controls:** Units; straighten interactions  
**Use:** Use to check tilted horizon or scale.  
**Caution:** Ruler measurement does not resize the image.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s01l05  

### Note
**Purpose:** Stores annotations in supported documents.  
**Location:** Toolbar > Eyedropper/Measurement tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** I  
**Controls:** Author; note text  
**Use:** Use for editorial feedback on a working file.  
**Caution:** Not all delivery formats retain notes.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s10l01  

### Count
**Purpose:** Marks numbered count items.  
**Location:** Toolbar > Eyedropper/Measurement tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** I  
**Controls:** Count groups; marker size  
**Use:** Use for inventory or object count.  
**Caution:** Marks are metadata overlays, not finished art.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s01l05  

### Spot Healing Brush
**Purpose:** Automatically repairs small defects from neighbors.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Content-Aware/Proximity Match; Sample All Layers  
**Use:** Use for tiny blemishes.  
**Caution:** Brush larger than defect often smears texture.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l01  

### Healing Brush
**Purpose:** Repairs target using chosen source texture and tone adaptation.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Source Aligned; Sample; diffusion  
**Use:** Use for controlled skin or surface repair.  
**Caution:** Wrong source area repeats unwanted detail.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l01  

### Patch
**Purpose:** Repairs a selected patch with source content.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Source/Destination; Normal/Content-Aware  
**Use:** Use for broad skin or wall blemishes.  
**Caution:** Dragged source with different lighting looks wrong.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l02  

### Content-Aware Move
**Purpose:** Moves a selected object and infers replacement around it.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Move/Extend; structure/color  
**Use:** Use for local object repositioning.  
**Caution:** Complex backgrounds show repeated content.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l03  

### Red Eye
**Purpose:** Darkens camera-flash red eye areas.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Pupil Size; Darken Amount  
**Use:** Use for old flash portraits.  
**Caution:** Avoid clicking non-eye red features.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l04  

### Remove
**Purpose:** Paints over unwanted objects with reconstruction options.  
**Location:** Toolbar > Healing/Remove tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** J  
**Controls:** Brush size; Remove after each stroke; processing mode  
**Use:** Use for wires and distractions after review.  
**Caution:** AI reconstruction may invent details; local model needs supported hardware/download.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l03  

### Brush
**Purpose:** Paints with a brush tip and configured color.  
**Location:** Toolbar > Brush/Adjustment Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** B  
**Controls:** Size; hardness; opacity; flow; smoothing  
**Use:** Use for art and masks.  
**Caution:** Painting on wrong thumbnail damages content.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l01  

### Pencil
**Purpose:** Draws hard-edged marks without soft antialias blending.  
**Location:** Toolbar > Brush/Adjustment Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** B  
**Controls:** Size; opacity; tip behavior  
**Use:** Use for pixel-style art or crisp marks.  
**Caution:** Poor for feathered blending.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l01  

### Color Replacement
**Purpose:** Recolors targeted hue while attempting to preserve texture.  
**Location:** Toolbar > Brush/Adjustment Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** B  
**Controls:** Limits; tolerance; sampling  
**Use:** Use for local color tweaks.  
**Caution:** Color edges may contaminate nearby objects.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l03  

### Mixer Brush
**Purpose:** Simulates mixing and dragging wet pigment.  
**Location:** Toolbar > Brush/Adjustment Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** B  
**Controls:** Wet; Load; Mix; Flow  
**Use:** Use for painterly blending.  
**Caution:** High Wet and Mix can smear structure.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l06  

### Clone Stamp
**Purpose:** Copies pixels from an Alt-clicked source.  
**Location:** Toolbar > Stamp tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** S  
**Controls:** Aligned; opacity; sample layers  
**Use:** Use for repeatable structural repair.  
**Caution:** Repeated sampling creates cloned patterns.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l02  

### Pattern Stamp
**Purpose:** Paints a chosen repeating pattern.  
**Location:** Toolbar > Stamp tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** S  
**Controls:** Pattern; impressionist; scale  
**Use:** Use for textures and surfaces.  
**Caution:** Repetition becomes obvious at large scale.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l04  

### History Brush
**Purpose:** Paints from a selected earlier history state.  
**Location:** Toolbar > History Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** Y  
**Controls:** History source; blending; brush options  
**Use:** Use for selective temporary restoration.  
**Caution:** Earlier states disappear after document closure.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l05  

### Art History Brush
**Purpose:** Stylizes painting based on a history state.  
**Location:** Toolbar > History Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** Y  
**Controls:** Style; Area; Tolerance  
**Use:** Use for painterly variations.  
**Caution:** Not a restoration tool for accurate pixels.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l05  

### Eraser
**Purpose:** Deletes or reduces pixels or transparency.  
**Location:** Toolbar > Eraser tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** E  
**Controls:** Brush mode; opacity; flow  
**Use:** Use when deletion is intended.  
**Caution:** Not reversible like a mask after history expires.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l05  

### Background Eraser
**Purpose:** Erases background colors based on sampled tone.  
**Location:** Toolbar > Eraser tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** E  
**Controls:** Limits; tolerance; sampling  
**Use:** Use for simple high-contrast edge isolation.  
**Caution:** Can chew into similar-colored foreground.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l04  

### Magic Eraser
**Purpose:** Deletes similar-colored pixels with a click.  
**Location:** Toolbar > Eraser tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** E  
**Controls:** Tolerance; contiguous; anti-alias  
**Use:** Use only on simple flat-color backgrounds.  
**Caution:** Permanent edge deletion is difficult to revise.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s03l03  

### Gradient
**Purpose:** Draws gradient transition; mode/version behavior varies.  
**Location:** Toolbar > Gradient/Paint Bucket tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** G  
**Controls:** Preset; angle; style; scale  
**Use:** Use for smooth lighting or backgrounds.  
**Caution:** A gradient rasterized on source can be destructive.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l04  

### Paint Bucket
**Purpose:** Fills contiguous or related pixels with color/pattern.  
**Location:** Toolbar > Gradient/Paint Bucket tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** G  
**Controls:** Tolerance; contiguous; sample layers  
**Use:** Use for flat artwork.  
**Caution:** Anti-aliased edge fringe may remain.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l04  

### Blur
**Purpose:** Locally softens pixel details.  
**Location:** Toolbar > Blur/Sharpen/Smudge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Strength; brush size; Sample All Layers  
**Use:** Use sparingly on distracting small edges.  
**Caution:** Overuse destroys texture.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s08l07  

### Sharpen
**Purpose:** Locally increases contrast of fine edges.  
**Location:** Toolbar > Blur/Sharpen/Smudge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Strength; Protect Detail  
**Use:** Use for selective detail emphasis.  
**Caution:** Repeated strokes amplify noise.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s08l07  

### Smudge
**Purpose:** Pushes pixel colors along a stroke.  
**Location:** Toolbar > Blur/Sharpen/Smudge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Strength; Finger Painting  
**Use:** Use for painterly blending.  
**Caution:** Often produces smeared photographic details.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s06l06  

### Dodge
**Purpose:** Locally lightens pixels based on tonal range.  
**Location:** Toolbar > Dodge/Burn/Sponge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** O  
**Controls:** Range; exposure; Protect Tones  
**Use:** Use on a duplicate or controlled local task.  
**Caution:** Direct painting accumulates destructive changes.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l05  

### Burn
**Purpose:** Locally darkens pixels based on tonal range.  
**Location:** Toolbar > Dodge/Burn/Sponge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** O  
**Controls:** Range; exposure; Protect Tones  
**Use:** Use to sculpt contrast carefully.  
**Caution:** Can create colored dark patches.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s05l05  

### Sponge
**Purpose:** Locally increases or decreases saturation.  
**Location:** Toolbar > Dodge/Burn/Sponge tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** O  
**Controls:** Mode Saturate/Desaturate; flow  
**Use:** Use for isolated color intensity changes.  
**Caution:** Strong saturation exaggerates artifact.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s08l03  

### Pen
**Purpose:** Draws editable straight and Bézier paths.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** P  
**Controls:** Path/Shape mode; path operations  
**Use:** Use for precise contours.  
**Caution:** Too many anchors create bumps.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Freeform Pen
**Purpose:** Draws paths by tracing freely.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** P  
**Controls:** Curve fit; Magnetic behavior where available  
**Use:** Use with a pen tablet for organic paths.  
**Caution:** Automatic points may be hard to edit.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Curvature Pen
**Purpose:** Creates smooth curves by clicking anchors.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** P  
**Controls:** Path/Shape mode; anchors  
**Use:** Use for fluid rounded outlines.  
**Caution:** Corners require explicit control.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Add Anchor Point
**Purpose:** Adds a point to editable path.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Path selection; hover location  
**Use:** Use to refine an existing segment.  
**Caution:** Too many anchors reduce smoothness.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Delete Anchor Point
**Purpose:** Removes a point from a path.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Path selection  
**Use:** Simplify overbuilt contours.  
**Caution:** Removing critical point alters shape unexpectedly.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Convert Point
**Purpose:** Converts smooth/corner handles.  
**Location:** Toolbar > Pen tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:**   
**Controls:** Click/drag point behavior  
**Use:** Fix kinks in a Bézier contour.  
**Caution:** Can alter neighboring segments.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Path Selection
**Purpose:** Moves or selects whole path components.  
**Location:** Toolbar > Path/Direct Selection tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** A  
**Controls:** Path Operations; multiple path selection  
**Use:** Use to reposition compound shapes.  
**Caution:** Different from Direct Selection on anchors.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Direct Selection
**Purpose:** Edits anchors and handles directly.  
**Location:** Toolbar > Path/Direct Selection tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** A  
**Controls:** Anchor and handle editing  
**Use:** Use for precise curve changes.  
**Caution:** Moving wrong handle changes curvature.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l04  

### Horizontal Type
**Purpose:** Creates editable left-to-right text.  
**Location:** Toolbar > Type tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** T  
**Controls:** Font; size; color; anti-alias  
**Use:** Use for headlines and body text.  
**Caution:** Type field focus consumes keyboard shortcuts.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l01  

### Vertical Type
**Purpose:** Creates text in vertical orientation.  
**Location:** Toolbar > Type tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** T  
**Controls:** Character; paragraph settings  
**Use:** Use for designs requiring vertical type.  
**Caution:** Letter layout may need font-specific care.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l01  

### Horizontal Type Mask
**Purpose:** Creates a text-shaped selection instead of type layer.  
**Location:** Toolbar > Type tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** T  
**Controls:** Font; size; tracking  
**Use:** Use for masking typography.  
**Caution:** Result is a selection, not editable glyph layer.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l01  

### Vertical Type Mask
**Purpose:** Creates vertically oriented text selection.  
**Location:** Toolbar > Type tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** T  
**Controls:** Font; size  
**Use:** Use for special type-shaped selections.  
**Caution:** Selection loses editability after deselection unless saved.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l01  

### Rectangle
**Purpose:** Draws rectangles as shapes/paths/pixels.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Mode; fill; stroke; corners  
**Use:** Use for containers and precise cards.  
**Caution:** Drawing in Pixels mode is destructive to that layer.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Rounded Rectangle
**Purpose:** Draws rounded rectangles or adjustable corner paths.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Corner radii; stroke; fill  
**Use:** Use for interface cards and labels.  
**Caution:** Scaling may change visual corner treatment.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Ellipse
**Purpose:** Draws ellipse and circle geometry.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Constrain proportions; fill; stroke  
**Use:** Use for icons and circles.  
**Caution:** Eyeballed drag may not be circular.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Triangle
**Purpose:** Draws triangle vector geometry.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Corner controls; fill  
**Use:** Use for arrows and symbols.  
**Caution:** Angle choices affect alignment.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Polygon
**Purpose:** Creates regular multi-sided paths.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Sides; radius; corner controls  
**Use:** Use for geometric badges.  
**Caution:** Too many sides can become inefficient.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Line
**Purpose:** Draws straight lines with configurable appearance.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Weight; fill; stroke; arrowheads if supported  
**Use:** Use for dividers and construction lines.  
**Caution:** Very thin strokes may disappear on export.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Custom Shape
**Purpose:** Draws shapes from a preset library.  
**Location:** Toolbar > Shape tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** U  
**Controls:** Custom Shape picker; fill; stroke  
**Use:** Use for reusable symbols.  
**Caution:** Preset availability depends on installed libraries.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s07l03  

### Hand
**Purpose:** Pans the canvas without moving image content.  
**Location:** Toolbar > Hand tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** H  
**Controls:** Scroll direction; rotate gestures context  
**Use:** Use at high zoom.  
**Caution:** View pan does not reposition a layer.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s01l05  

### Rotate View
**Purpose:** Rotates the canvas view without rotating pixels.  
**Location:** Toolbar > Rotate View tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** R  
**Controls:** Angle; Reset View  
**Use:** Use for natural brush strokes.  
**Caution:** Export remains unaffected by view rotation.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s01l05  

### Zoom
**Purpose:** Changes on-screen magnification.  
**Location:** Toolbar > Zoom tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** Z  
**Controls:** Scrubby Zoom; animated zoom support  
**Use:** Use to assess at 100%.  
**Caution:** Zoom cannot create real detail.  
**Status:** Tool family; inspect toolbar configuration  
**Lesson:** s01l05  

### Adjustment Brush
**Purpose:** Paints the coverage of a non-destructive local adjustment while adjusting image tone or color.  
**Location:** Toolbar > Brush/Adjustment Brush tool group (expand the tool group; Edit > Toolbar if not visible)  
**Shortcut:** B  
**Controls:** Adjustment type; brush size; hardness; Add/Subtract; properties vary  
**Use:** Make local reversible correction without manually creating the mask first.  
**Caution:** Verify that the adjustment mask, not source pixels, is selected and account for the current Tool group.  
**Status:** Modern built-in tool; verify toolbar layout  
**Lesson:** s04l01  

## Filters

### Gaussian Blur
**Effect:** Smooths pixels with Gaussian weighting; blur grows with radius.  
**Location:** Filter > Blur > Gaussian Blur  
**Controls:** Radius  
**Use:** Soft backgrounds and feathered shadows  
**Caution:** Loses fine detail if applied directly; Smart Filter normally available.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s04l03  

### Box Blur
**Effect:** Averages colors within a rectangular neighborhood.  
**Location:** Filter > Blur > Box Blur  
**Controls:** Radius  
**Use:** Stylized flat smoothness  
**Caution:** May create boxy edges at high radius.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Average
**Effect:** Replaces selected area with its average color.  
**Location:** Filter > Blur > Average  
**Controls:** None  
**Use:** Determine or generate representative color  
**Caution:** Removes all local detail.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l03  

### Blur
**Effect:** Applies a mild blur.  
**Location:** Filter > Blur > Blur  
**Controls:** Preset strength  
**Use:** Tiny softening  
**Caution:** Repeated destructive use stacks loss.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Blur More
**Effect:** Applies stronger standard blur.  
**Location:** Filter > Blur > Blur More  
**Controls:** Preset strength  
**Use:** Quick broad softening  
**Caution:** Less controllable than Gaussian Blur.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Motion Blur
**Effect:** Blurs along a line, suggesting motion.  
**Location:** Filter > Blur > Motion Blur  
**Controls:** Angle; Distance  
**Use:** Motion trails and effects  
**Caution:** Wrong angle contradicts movement.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Radial Blur
**Effect:** Blurs outward or in rotation from a center.  
**Location:** Filter > Blur > Radial Blur  
**Controls:** Amount; Blur Method; Quality  
**Use:** Speed or rotational effects  
**Caution:** Center and quality need previewing.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Lens Blur
**Effect:** Simulates defocus using depth information.  
**Location:** Filter > Blur > Lens Blur  
**Controls:** Blur amount; depth map; iris controls  
**Use:** Depth-of-field effects  
**Caution:** Adobe lists 16/32-bit compatibility limits; check mode. Not available as an editable Smart Filter in Adobe’s Oct 2026 Smart Filter documentation.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Smart Blur
**Effect:** Blurs within similar-color regions while attempting to retain edges.  
**Location:** Filter > Blur > Smart Blur  
**Controls:** Radius; Threshold; Quality  
**Use:** Flattening noise in graphics  
**Caution:** Can create unnatural smooth regions.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Surface Blur
**Effect:** Smooths areas while preserving some edges.  
**Location:** Filter > Blur > Surface Blur  
**Controls:** Radius; Threshold  
**Use:** Subtle surface corrections  
**Caution:** High thresholds erase texture.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l04  

### Field Blur
**Effect:** Blurs by spatial pins with adjustable strength.  
**Location:** Filter > Blur Gallery > Field Blur  
**Controls:** Blur pins; amount  
**Use:** Depth progression  
**Caution:** GPU capability may affect availability.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Iris Blur
**Effect:** Creates localized depth-of-field approximation.  
**Location:** Filter > Blur Gallery > Iris Blur  
**Controls:** Iris shape; blur; feather  
**Use:** Portrait or product focal emphasis  
**Caution:** Fake falloff if geometry conflicts.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Tilt-Shift
**Effect:** Simulates plane of focus and miniature aesthetic.  
**Location:** Filter > Blur Gallery > Tilt-Shift  
**Controls:** Blur bands; transition; distortion  
**Use:** Architectural miniatures  
**Caution:** Strong use makes full scene toy-like.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Path Blur
**Effect:** Blurs along specified curved motion paths.  
**Location:** Filter > Blur Gallery > Path Blur  
**Controls:** Path; speed; shape  
**Use:** Stylized motion streaks  
**Caution:** Wrong path looks physically implausible.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Spin Blur
**Effect:** Simulates object rotation motion.  
**Location:** Filter > Blur Gallery > Spin Blur  
**Controls:** Ellipse; blur angle  
**Use:** Wheels and circular objects  
**Caution:** Center misalignment creates wobble.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Unsharp Mask
**Effect:** Adds contrast along transitions to create sharpness impression.  
**Location:** Filter > Sharpen > Unsharp Mask  
**Controls:** Amount; Radius; Threshold  
**Use:** Output sharpening  
**Caution:** Causes halos at high Amount/Radius.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Smart Sharpen
**Effect:** Selective algorithmic sharpening with detailed controls.  
**Location:** Filter > Sharpen > Smart Sharpen  
**Controls:** Amount; Radius; Reduce Noise; Shadow/Highlight  
**Use:** Precise sharpening  
**Caution:** Cannot fully recover badly blurred source information.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Sharpen
**Effect:** Simple sharpening pass.  
**Location:** Filter > Sharpen > Sharpen  
**Controls:** Preset  
**Use:** Minor quick contrast increase  
**Caution:** Stacked passes magnify noise.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Sharpen More
**Effect:** Stronger automatic sharpening.  
**Location:** Filter > Sharpen > Sharpen More  
**Controls:** Preset  
**Use:** Strong stylized edges  
**Caution:** Often excessive for natural photos.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Sharpen Edges
**Effect:** Emphasizes localized edges.  
**Location:** Filter > Sharpen > Sharpen Edges  
**Controls:** Preset  
**Use:** Linework  
**Caution:** Bit-depth restrictions according to Adobe reference.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Shake Reduction
**Effect:** Legacy motion restoration option; do not assume present in 27.11.  
**Location:** REMOVED in Photoshop 23.3 (historical: Filter > Sharpen > Shake Reduction)  
**Controls:** Settings vary by availability  
**Use:** Historical tutorial context  
**Caution:** Removed starting in Photoshop 23.3 (April 2022); do not attempt this historical command in 27.11. Use contemporary non-destructive sharpening or qualifying AI methods instead. Adobe documentation confirms the removal.  
**Status:** REMOVED in 23.3; legacy reference only, unavailable in 27.11  
**Lesson:** s08l07  

### Add Noise
**Effect:** Adds random pixel variations.  
**Location:** Filter > Noise > Add Noise  
**Controls:** Amount; Distribution; Monochromatic  
**Use:** Grain matching in composites  
**Caution:** Strong noise worsens compression.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l06  

### Reduce Noise
**Effect:** Smooths luminance/color noise.  
**Location:** Filter > Noise > Reduce Noise  
**Controls:** Strength; Preserve Details; Reduce Color Noise  
**Use:** High ISO image cleanup  
**Caution:** Blurs small features at strong settings.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Dust & Scratches
**Effect:** Blurs small defects based on radius and threshold.  
**Location:** Filter > Noise > Dust & Scratches  
**Controls:** Radius; Threshold  
**Use:** Scanned image scratches  
**Caution:** Softens small true details.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l06  

### Median
**Effect:** Replaces pixels based on neighborhood median.  
**Location:** Filter > Noise > Median  
**Controls:** Radius  
**Use:** Salt-and-pepper noise  
**Caution:** Smooths small fine lines.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l06  

### Despeckle
**Effect:** Suppresses speckled transitions.  
**Location:** Filter > Noise > Despeckle  
**Controls:** Preset  
**Use:** Quick noise treatment  
**Caution:** Less control than dedicated reduction.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Displace
**Effect:** Moves pixels using grayscale map.  
**Location:** Filter > Distort > Displace  
**Controls:** Horizontal/Vertical scale; map; edges  
**Use:** Fabric and surface mockups  
**Caution:** Needs separate appropriate PSD displacement map.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Ripple
**Effect:** Creates short waterlike wavy displacement.  
**Location:** Filter > Distort > Ripple  
**Controls:** Amount; Size  
**Use:** Water or stylized glass  
**Caution:** Strong values break straight geometry.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Wave
**Effect:** Creates periodic distortions.  
**Location:** Filter > Distort > Wave  
**Controls:** Generators; wavelength; amplitude  
**Use:** Abstract wave effects  
**Caution:** Regularity becomes visibly artificial.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### ZigZag
**Effect:** Distorts pixels radially like ripples.  
**Location:** Filter > Distort > ZigZag  
**Controls:** Amount; Ridges; Style  
**Use:** Water drops and rings  
**Caution:** Avoid on faces and text.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Twirl
**Effect:** Rotates pixels increasingly toward center.  
**Location:** Filter > Distort > Twirl  
**Controls:** Angle  
**Use:** Abstract swirls  
**Caution:** Can twist edges unnaturally.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Spherize
**Effect:** Bulges or pinches image in region.  
**Location:** Filter > Distort > Spherize  
**Controls:** Amount; Mode  
**Use:** Lens-like sphere effects  
**Caution:** Stretched details appear near edge.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Pinch
**Effect:** Compresses or expands local image area.  
**Location:** Filter > Distort > Pinch  
**Controls:** Amount  
**Use:** Stylized warps  
**Caution:** Can damage straight geometry.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Polar Coordinates
**Effect:** Maps rectangular layout into circular coordinates or back.  
**Location:** Filter > Distort > Polar Coordinates  
**Controls:** Rectangular/Polar conversion  
**Use:** Panoramic little-planet studies  
**Caution:** Seam placement matters.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Shear
**Effect:** Displaces image horizontally along a path.  
**Location:** Filter > Distort > Shear  
**Controls:** Curve control points; edge handling  
**Use:** Wavy surfaces  
**Caution:** Edge repeat/undefined choices can show seams.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Glass
**Effect:** Creates rippled refractive surface.  
**Location:** Filter > Filter Gallery  
**Controls:** Distortion; Smoothness; Texture  
**Use:** Window glass stylization  
**Caution:** Not a physics-based refractive renderer.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Ocean Ripple
**Effect:** Simulates ripple-like distortion.  
**Location:** Filter > Filter Gallery  
**Controls:** Ripple Size; Magnitude  
**Use:** Water textures  
**Caution:** Low resolution source may pixelate.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Diffuse Glow
**Effect:** Adds pale glowing grain around subject.  
**Location:** Filter > Filter Gallery  
**Controls:** Graininess; Glow Amount; Clear Amount  
**Use:** Dreamlike highlights  
**Caution:** Can flatten tonal range.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Liquify
**Effect:** Warps geometry with specialized tools.  
**Location:** Filter > Liquify  
**Controls:** Brush size; pressure; mesh  
**Use:** Shape adjustments and effects  
**Caution:** GPU/mode limitations; identity ethics matter.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l05  

### Perspective Warp
**Effect:** Reorients planar content in perspective.  
**Location:** Edit > Perspective Warp  
**Controls:** Layout; Warp pins/planes  
**Use:** Architecture integration  
**Caution:** Hard with nonplanar subjects.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l05  

### Camera Raw Filter
**Effect:** Runs Camera Raw adjustments on rendered pixels.  
**Location:** Filter > Camera Raw Filter  
**Controls:** Basic; Color Mixer; Detail; Masking  
**Use:** Consistent color and tone controls  
**Caution:** Adobe documents 8/16-bit support for this filter.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l04  

### Lens Correction
**Effect:** Compensates for lens artifacts.  
**Location:** Filter > Lens Correction  
**Controls:** Distortion; Vignette; Chromatic Aberration  
**Use:** Architectural/RAW lens cleanup  
**Caution:** Profile support depends on lens metadata.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l04  

### Vanishing Point
**Effect:** Edits pixels respecting drawn planar perspective.  
**Location:** Filter > Vanishing Point  
**Controls:** Perspective plane; Clone/Transform  
**Use:** Wall and packaging mockups  
**Caution:** Inaccurate plane causes stretching. Not available as an editable Smart Filter in Adobe’s Oct 2026 Smart Filter documentation.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### High Pass
**Effect:** Keeps high-frequency edges while suppressing low-frequency tone.  
**Location:** Filter > Other > High Pass  
**Controls:** Radius  
**Use:** Frequency/detail composites  
**Caution:** Can introduce halos when blended strongly.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l06  

### Maximum
**Effect:** Expands brighter regions.  
**Location:** Filter > Other > Maximum  
**Controls:** Radius; Preserve  
**Use:** Mask edge morphology  
**Caution:** Can eliminate tiny dark detail.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s03l04  

### Minimum
**Effect:** Expands darker regions.  
**Location:** Filter > Other > Minimum  
**Controls:** Radius; Preserve  
**Use:** Mask choke or erosion depending on mask convention  
**Caution:** Can destroy fine light structure.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s03l04  

### Offset
**Effect:** Rolls or offsets pixel locations.  
**Location:** Filter > Other > Offset  
**Controls:** Horizontal/Vertical; edge mode  
**Use:** Seamless texture evaluation  
**Caution:** Wrap Around needs periodic content to hide seams.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l04  

### Color Halftone
**Effect:** Simulates printed halftone dots.  
**Location:** Filter > Pixelate > Color Halftone  
**Controls:** Max Radius; channel angles  
**Use:** Retro print aesthetics  
**Caution:** Fine lines may moiré on downsizing.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s07l06  

### Mosaic
**Effect:** Converts nearby pixels to colored blocks.  
**Location:** Filter > Pixelate > Mosaic  
**Controls:** Cell Size  
**Use:** Pixelation and concealment effects  
**Caution:** Not suitable as secure anonymization.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Crystallize
**Effect:** Builds polygonal color cells.  
**Location:** Filter > Pixelate > Crystallize  
**Controls:** Cell Size  
**Use:** Geometric texture  
**Caution:** Large cells remove scene readability.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Mezzotint
**Effect:** Creates mottled or lined tonal noise.  
**Location:** Filter > Pixelate > Mezzotint  
**Controls:** Type  
**Use:** Print-styled graphics  
**Caution:** Can overwhelm detail.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Pointillize
**Effect:** Renders scene with colored dots.  
**Location:** Filter > Pixelate > Pointillize  
**Controls:** Cell Size  
**Use:** Pointillist illustration  
**Caution:** Holes expose lower content/background.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Fragment
**Effect:** Offsets and softens duplicate pixel fragments.  
**Location:** Filter > Pixelate > Fragment  
**Controls:** Preset  
**Use:** Soft fragmented effect  
**Caution:** Limited parameter control.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Clouds
**Effect:** Synthesizes a cloudy pattern.  
**Location:** Filter > Render > Clouds  
**Controls:** Foreground/Background color  
**Use:** Atmospheric texture masks  
**Caution:** Default result depends on current colors.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l04  

### Difference Clouds
**Effect:** Combines cloud-like random fields.  
**Location:** Filter > Render > Difference Clouds  
**Controls:** Foreground/Background color  
**Use:** Texture variation  
**Caution:** Repeated use changes unpredictably.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l04  

### Fibers
**Effect:** Generates streaked fibrous texture.  
**Location:** Filter > Render > Fibers  
**Controls:** Variance; Strength  
**Use:** Wood/fabric bases  
**Caution:** Artificial regularity at full scale.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l04  

### Lens Flare
**Effect:** Adds simulated bright lens artifacts.  
**Location:** Filter > Render > Lens Flare  
**Controls:** Brightness; Lens Type; position  
**Use:** Stylized highlights  
**Caution:** Easy to make light direction inconsistent.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l02  

### Tree
**Effect:** Generates procedural trees where installed.  
**Location:** Filter > Render > Tree  
**Controls:** Tree type; foliage and branch options  
**Use:** Background illustration elements  
**Caution:** Needs version and bit-depth compatibility test. Not available as an editable Smart Filter in Adobe’s Oct 2026 Smart Filter documentation.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Flame
**Effect:** Generates stylized flames along paths where supported.  
**Location:** Filter > Render > Flame  
**Controls:** Flame type; length; width  
**Use:** Graphic fire accents  
**Caution:** Depends on a valid path and tool availability. Not available as an editable Smart Filter in Adobe’s Oct 2026 Smart Filter documentation.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l04  

### Oil Paint
**Effect:** Creates painterly surface and brushwork.  
**Location:** Filter > Stylize > Oil Paint  
**Controls:** Stylization; Cleanliness; Scale; lighting  
**Use:** Artistic paintings  
**Caution:** Requires supported GPU features for some systems.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Emboss
**Effect:** Renders apparent raised relief.  
**Location:** Filter > Stylize > Emboss  
**Controls:** Angle; Height; Amount  
**Use:** Texture maps  
**Caution:** Alters normal tonal appearance.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s07l03  

### Find Edges
**Effect:** Maps intensity transitions into edge traces.  
**Location:** Filter > Stylize > Find Edges  
**Controls:** Preset  
**Use:** Sketch effects  
**Caution:** Noise may create too many edges.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Glowing Edges
**Effect:** Renders colored luminous edges.  
**Location:** Filter > Filter Gallery  
**Controls:** Edge Width; Brightness; Smoothness  
**Use:** Neon-like effects  
**Caution:** Fine noise can glow undesirably.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l06  

### Wind
**Effect:** Creates horizontal streaks.  
**Location:** Filter > Stylize > Wind  
**Controls:** Method; Direction  
**Use:** Speed and stylized typography  
**Caution:** May require layer rotation for other angles.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l06  

### Solarize
**Effect:** Partially inverts bright tones.  
**Location:** Filter > Stylize > Solarize  
**Controls:** Preset  
**Use:** Experimental tone design  
**Caution:** Little tonal control.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l03  

### Poster Edges
**Effect:** Simplifies and darkens graphic boundaries.  
**Location:** Filter > Filter Gallery  
**Controls:** Edge Thickness; Intensity; Posterization  
**Use:** Comic/painterly look  
**Caution:** Loses photorealism quickly.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Cutout
**Effect:** Reduces image to flat-tone regions.  
**Location:** Filter > Filter Gallery  
**Controls:** Number of Levels; Edge Simplicity; Fidelity  
**Use:** Paper-cut look  
**Caution:** Small details disappear.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Colored Pencil
**Effect:** Simulates pencil-on-paper texture.  
**Location:** Filter > Filter Gallery  
**Controls:** Pencil Width; Stroke Pressure; Paper Brightness  
**Use:** Illustrative textures  
**Caution:** Paper settings strongly affect color.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Watercolor
**Effect:** Simulates watercolor wash edges.  
**Location:** Filter > Filter Gallery  
**Controls:** Brush Detail; Shadow Intensity; Texture  
**Use:** Painterly graphics  
**Caution:** Often muddy on low contrast art.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Dry Brush
**Effect:** Creates dry-brush strokes.  
**Location:** Filter > Filter Gallery  
**Controls:** Brush Size; Detail; Texture  
**Use:** Poster illustration  
**Caution:** Text may become unreadable.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Film Grain
**Effect:** Adds stylized film-like grain.  
**Location:** Filter > Filter Gallery  
**Controls:** Grain; Highlight/Intensity  
**Use:** Retro looks  
**Caution:** Different from sensor noise modeling.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s08l07  

### Accented Edges
**Effect:** Emphasizes brushy boundaries.  
**Location:** Filter > Filter Gallery  
**Controls:** Edge Width; Brightness; Smoothness  
**Use:** Graphic edge effects  
**Caution:** Too much creates hard outlines.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Crosshatch
**Effect:** Simulates crossing drawn strokes.  
**Location:** Filter > Filter Gallery  
**Controls:** Stroke Length; Sharpness; Strength  
**Use:** Hatched illustrations  
**Caution:** Can obscure small subject details.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Bas Relief
**Effect:** Makes light-dark relief-like shading.  
**Location:** Filter > Filter Gallery  
**Controls:** Detail; Smoothness; Light  
**Use:** Engraving effects  
**Caution:** FG/BG colors change the result.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Chalk & Charcoal
**Effect:** Simulates chalk and charcoal.  
**Location:** Filter > Filter Gallery  
**Controls:** Charcoal Area; Chalk Area; Stroke Pressure  
**Use:** Hand-drawn rendering  
**Caution:** Reduced color fidelity intentional.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Grain
**Effect:** Adds textured grain patterns.  
**Location:** Filter > Filter Gallery  
**Controls:** Intensity; Contrast; Grain Type  
**Use:** Surface texture  
**Caution:** Oversized grain hurts readability.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s06l06  

### Texturizer
**Effect:** Embosses surface texture.  
**Location:** Filter > Filter Gallery  
**Controls:** Texture; Scaling; Relief; Light  
**Use:** Paper and canvas mockups  
**Caution:** Lighting direction may conflict with photo.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s09l05  

### Craquelure
**Effect:** Creates cracked surface texture.  
**Location:** Filter > Filter Gallery  
**Controls:** Crack Spacing; Depth; Brightness  
**Use:** Aged-paint simulation  
**Caution:** Unrealistic when applied uniformly.  
**Status:** Documented family; mode and GPU limits apply  
**Lesson:** s05l06  

### Neural Filters
**Effect:** A category of ML-assisted edits; each filter has separate availability.  
**Location:** Filter > Neural Filters  
**Controls:** Per-filter settings; cloud vs downloaded status  
**Use:** Explore targeted ML treatments  
**Caution:** Some require download, online processing or are Beta; verify in app. Some models require a download or an online service; do not assume the same offline requirements for all.  
**Status:** Service / check entitlement  
**Lesson:** s11l06  

### AI Sharpen (Topaz)
**Effect:** Credit-consuming generative sharpen feature documented in 2026.  
**Location:** Filter > AI Sharpen (premium cloud service; eligibility and credits required)  
**Controls:** MP output; service action  
**Use:** Damaged or soft photos with disclosure  
**Caution:** Adobe notes direct current-layer update; test on a copy. This premium service operates on the active layer with no new layer; duplicate the original first. Adobe documents a 56 MP file cap and usage-credit charges (verify current entitlement/terms).  
**Status:** Service / check entitlement  
**Lesson:** s08l07  

### AI Denoise (Topaz)
**Effect:** Credit-consuming generative noise reduction documented in 2026.  
**Location:** Filter > AI Denoise (premium cloud service; eligibility and credits required)  
**Controls:** MP output; service action  
**Use:** High-noise imagery requiring extra recovery  
**Caution:** Adobe notes current-layer update; not a general offline filter. This premium service operates on the active layer with no new layer; duplicate the original first. Adobe documents a 56 MP file cap and usage-credit charges (verify current entitlement/terms).  
**Status:** Service / check entitlement  
**Lesson:** s08l07  

## Windows shortcuts

### New document
**Family:** File  
**Keys:** Ctrl+N  
**Context:** Global  
**Note:** Default application shortcut; verify after customization  

### Open file
**Family:** File  
**Keys:** Ctrl+O  
**Context:** Global  
**Note:** Opens standard file picker  

### Save
**Family:** File  
**Keys:** Ctrl+S  
**Context:** Global  
**Note:** Dialog differs for new documents  

### Save As
**Family:** File  
**Keys:** Ctrl+Shift+S  
**Context:** Global  
**Note:** Save route can depend on format and modern save settings  

### Print
**Family:** File  
**Keys:** Ctrl+P  
**Context:** Global  
**Note:** Printer availability varies  

### Close document
**Family:** File  
**Keys:** Ctrl+W  
**Context:** Document  
**Note:** Prompts if unsaved  

### Close all documents
**Family:** File  
**Keys:** Ctrl+Alt+W  
**Context:** Document  
**Note:** Verify in customized menu  

### Undo
**Family:** File  
**Keys:** Ctrl+Z  
**Context:** Document  
**Note:** Undo action in editing context; text inputs can consume it  

### Step backward
**Family:** File  
**Keys:** Ctrl+Alt+Z  
**Context:** History  
**Note:** History behavior depends on state  

### Step forward
**Family:** File  
**Keys:** Ctrl+Shift+Z  
**Context:** History  
**Note:** Redo behavior depends on state  

### Preferences
**Family:** Interface  
**Keys:** Ctrl+K  
**Context:** Global  
**Note:** General preferences in Windows  

### Keyboard Shortcuts dialog
**Family:** Interface  
**Keys:** Ctrl+Alt+Shift+K  
**Context:** Global  
**Note:** Adobe documented  

### Show/hide panels
**Family:** Interface  
**Keys:** Tab  
**Context:** Workspace  
**Note:** While not typing in a field  

### Show/hide side panels
**Family:** Interface  
**Keys:** Shift+Tab  
**Context:** Workspace  
**Note:** While not typing in a field  

### Rulers
**Family:** Interface  
**Keys:** Ctrl+R  
**Context:** Document  
**Note:** View overlay only  

### Hide/show extras
**Family:** Interface  
**Keys:** Ctrl+H  
**Context:** Document  
**Note:** May affect guides/selection edges  

### Grid
**Family:** Interface  
**Keys:** Ctrl+'  
**Context:** Document  
**Note:** Depends on keyboard layout and shortcut settings  

### Fit on Screen
**Family:** View  
**Keys:** Ctrl+0  
**Context:** Document  
**Note:** View-only  

### Actual Pixels 100%
**Family:** View  
**Keys:** Ctrl+1  
**Context:** Document  
**Note:** View-only  

### Zoom in
**Family:** View  
**Keys:** Ctrl++ (plus)  
**Context:** Document  
**Note:** May require key-layout adaptation  

### Zoom out
**Family:** View  
**Keys:** Ctrl+-  
**Context:** Document  
**Note:** View-only  

### Zoom tool
**Family:** View  
**Keys:** Z  
**Context:** Tool  
**Note:** Only when no text field captures keystroke  

### Hand tool
**Family:** View  
**Keys:** H  
**Context:** Tool  
**Note:** Only when no text field captures keystroke  

### Temporary Hand
**Family:** View  
**Keys:** Space  
**Context:** Tool gesture  
**Note:** Hold while using many tools; conflicts with text entry  

### Rotate View
**Family:** View  
**Keys:** R  
**Context:** Tool  
**Note:** R selects Rotate View, not Blur. Document view only; GPU support may affect operation.  

### New layer
**Family:** Layers  
**Keys:** Ctrl+Shift+N  
**Context:** Document  
**Note:** Opens naming dialog  

### Duplicate layer
**Family:** Layers  
**Keys:** Ctrl+J  
**Context:** Layer  
**Note:** Also copies an active selection onto a new layer  

### Group selected layers
**Family:** Layers  
**Keys:** Ctrl+G  
**Context:** Layers panel  
**Note:** Selection-dependent  

### Ungroup layers
**Family:** Layers  
**Keys:** Ctrl+Shift+G  
**Context:** Layers panel  
**Note:** Group-selection-dependent  

### Free Transform
**Family:** Layers  
**Keys:** Ctrl+T  
**Context:** Document  
**Note:** Active editable content required  

### Transform again
**Family:** Layers  
**Keys:** Ctrl+Shift+T  
**Context:** Document  
**Note:** Availability depends on recent transform  

### New layer via copy
**Family:** Layers  
**Keys:** Ctrl+J  
**Context:** Selection/layer  
**Note:** Same key changes scope with active selection  

### Select All
**Family:** Selection  
**Keys:** Ctrl+A  
**Context:** Document  
**Note:** Selects entire active canvas  

### Deselect
**Family:** Selection  
**Keys:** Ctrl+D  
**Context:** Document  
**Note:** Requires active selection for visible effect  

### Reselect
**Family:** Selection  
**Keys:** Ctrl+Shift+D  
**Context:** Document  
**Note:** Last selection state needed  

### Inverse selection
**Family:** Selection  
**Keys:** Ctrl+Shift+I  
**Context:** Document  
**Note:** Active selection needed  

### Quick Mask toggle
**Family:** Selection  
**Keys:** Q  
**Context:** Tool/selection  
**Note:** Keyboard focus must be outside text  

### Marquee family
**Family:** Selection  
**Keys:** M  
**Context:** Tool  
**Note:** Shift+M may cycle group if configured  

### Lasso family
**Family:** Selection  
**Keys:** L  
**Context:** Tool  
**Note:** Shift+L may cycle group if configured  

### Selection family
**Family:** Selection  
**Keys:** W  
**Context:** Tool  
**Note:** Object Selection, Quick Selection and Magic Wand are W-group; Selection Brush is in the L group.  

### Move
**Family:** Tools  
**Keys:** V  
**Context:** Tool  
**Note:** Auto-select may change target layer  

### Crop
**Family:** Tools  
**Keys:** C  
**Context:** Tool  
**Note:** Tool family includes other grouped tools  

### Eyedropper
**Family:** Tools  
**Keys:** I  
**Context:** Tool  
**Note:** May cycle measurement tools  

### Spot Healing family
**Family:** Tools  
**Keys:** J  
**Context:** Tool  
**Note:** Group member varies  

### Brush
**Family:** Tools  
**Keys:** B  
**Context:** Tool  
**Note:** B includes Brush and may cycle to Adjustment Brush; default keyboard focus and tool set matter.  

### Clone Stamp
**Family:** Tools  
**Keys:** S  
**Context:** Tool  
**Note:** Group member varies  

### History Brush
**Family:** Tools  
**Keys:** Y  
**Context:** Tool  
**Note:** Depends on available history state  

### Eraser
**Family:** Tools  
**Keys:** E  
**Context:** Tool  
**Note:** Destructive on raster layer  

### Gradient
**Family:** Tools  
**Keys:** G  
**Context:** Tool  
**Note:** May share Paint Bucket  

### Dodge/Burn/Sponge
**Family:** Tools  
**Keys:** O  
**Context:** Tool  
**Note:** Grouped tools may cycle  

### Pen
**Family:** Tools  
**Keys:** P  
**Context:** Tool  
**Note:** Mode (Path/Shape) must be checked  

### Type
**Family:** Tools  
**Keys:** T  
**Context:** Tool  
**Note:** Text caret captures other shortcuts when editing  

### Path/Direct Selection
**Family:** Tools  
**Keys:** A  
**Context:** Tool  
**Note:** Selected subtool may vary  

### Shape
**Family:** Tools  
**Keys:** U  
**Context:** Tool  
**Note:** Shape mode/Path/Pixels determines results  

### Default black/white colors
**Family:** Paint  
**Keys:** D  
**Context:** Tool  
**Note:** Foreground/background swatches  

### Swap foreground/background
**Family:** Paint  
**Keys:** X  
**Context:** Tool  
**Note:** Useful when painting masks  

### Increase brush size
**Family:** Paint  
**Keys:** ]  
**Context:** Brush tool  
**Note:** Keyboard focus and layout dependent  

### Decrease brush size
**Family:** Paint  
**Keys:** [  
**Context:** Brush tool  
**Note:** Keyboard focus and layout dependent  

### Increase brush hardness
**Family:** Paint  
**Keys:** Shift+]  
**Context:** Brush tool  
**Note:** Brush-dependent  

### Decrease brush hardness
**Family:** Paint  
**Keys:** Shift+[  
**Context:** Brush tool  
**Note:** Brush-dependent  

### Fill foreground
**Family:** Paint  
**Keys:** Alt+Backspace  
**Context:** Pixel/edit context  
**Note:** May fill selection or active pixels  

### Fill background
**Family:** Paint  
**Keys:** Ctrl+Backspace  
**Context:** Pixel/edit context  
**Note:** May fill selection or active pixels  

### Brush temporary eyedropper
**Family:** Paint  
**Keys:** Alt (hold)  
**Context:** Brush gesture  
**Note:** Context-dependent sampling  

### Cycle screen modes
**Family:** View  
**Keys:** F  
**Context:** Document  
**Note:** May conflict with text entry  

### Commit type / exit field
**Family:** Text  
**Keys:** Ctrl+Enter  
**Context:** Type editing  
**Note:** Behavior depends on active text context  

### Cancel text changes
**Family:** Text  
**Keys:** Esc  
**Context:** Type editing  
**Note:** May exit or cancel depending on state  

### Open Photoshop Help/Discover
**Family:** Reference  
**Keys:** Ctrl+F  
**Context:** Global  
**Note:** Discover in supported versions; app-search not website search  

### Frame Tool
**Family:** Tools  
**Keys:** K  
**Context:** Tool  
**Note:** Current Frame Tool default; historical Blur K listings are obsolete.  

### Artboard tool
**Family:** Tools  
**Keys:** V  
**Context:** Tool  
**Note:** Grouped with Move; use the tool-group cycle or toolbar.  

### Selection Brush tool
**Family:** Tools  
**Keys:** L  
**Context:** Tool  
**Note:** Grouped with Lasso in modern Photoshop; use group cycle.  

### Adjustment Brush tool
**Family:** Tools  
**Keys:** B  
**Context:** Tool  
**Note:** Modern adjustment family grouped with Brush; toolbar configuration may vary.  

### Blur/Sharpen/Smudge tools
**Family:** Tools  
**Keys:** No default key  
**Context:** Tool  
**Note:** Do NOT use R (Rotate View) or K (Frame); access the toolbar or assign custom shortcut.  

### Copy
**Family:** Editing  
**Keys:** Ctrl+C  
**Context:** Document/selection  
**Note:** Standard copy; may copy selected pixel content or object.  

### Cut
**Family:** Editing  
**Keys:** Ctrl+X  
**Context:** Document/selection  
**Note:** Changes pixels or content depending on selection.  

### Paste
**Family:** Editing  
**Keys:** Ctrl+V  
**Context:** Document/selection  
**Note:** Creates/imports pasted content as appropriate.  

### Copy Merged
**Family:** Editing  
**Keys:** Ctrl+Shift+C  
**Context:** Active pixel selection  
**Note:** Copies composite visible pixels rather than one layer.  

### Paste in Place
**Family:** Editing  
**Keys:** Ctrl+Shift+V  
**Context:** Document  
**Note:** Positioned paste; document/clipboard context matters.  

### Fill dialog
**Family:** Editing  
**Keys:** Shift+F5  
**Context:** Document/selection  
**Note:** Application command; menu can also open fill.  

### Color Settings
**Family:** Editing  
**Keys:** Ctrl+Shift+K  
**Context:** Global  
**Note:** Adobe Windows desktop command; changes color management preferences.  

### Export As
**Family:** Editing  
**Keys:** Ctrl+Alt+Shift+W  
**Context:** Document  
**Note:** Legacy Adobe shortcut reference; verify 27.11 shortcut menu.  

### Save for Web (Legacy)
**Family:** Editing  
**Keys:** Ctrl+Alt+Shift+S  
**Context:** Document  
**Note:** Legacy path; may be hidden in recent versions.  

### Revert to last saved
**Family:** Editing  
**Keys:** F12  
**Context:** Document  
**Note:** Discards subsequent edits; use only after saving copies.  

### Quit Photoshop
**Family:** Editing  
**Keys:** Ctrl+Q  
**Context:** Global  
**Note:** Offers save prompts for changed documents.  

### Create layer via cut
**Family:** Layer  
**Keys:** Ctrl+Shift+J  
**Context:** Active selection  
**Note:** Creates a new layer from selected pixels where applicable.  

### Merge selected layers
**Family:** Layer  
**Keys:** Ctrl+E  
**Context:** Selected layers  
**Note:** Destructive; preserve layered master.  

### Merge visible
**Family:** Layer  
**Keys:** Ctrl+Shift+E  
**Context:** Document  
**Note:** Destructive; save layered working file first.  

### Stamp visible on new layer
**Family:** Layer  
**Keys:** Ctrl+Alt+Shift+E  
**Context:** Document  
**Note:** Merges a snapshot of visible layers onto a new layer; verify active target.  

### Clip to layer below
**Family:** Layer  
**Keys:** Ctrl+Alt+G  
**Context:** Layers panel  
**Note:** Create/release clipping mask; needs suitable base layer.  

### Select pixels from layer thumbnail
**Family:** Selection  
**Keys:** Ctrl+click layer thumbnail  
**Context:** Layers panel mouse gesture  
**Note:** Loads layer transparency as a selection.  

### Temporarily add to selection
**Family:** Selection  
**Keys:** Shift+drag  
**Context:** Selection tool gesture  
**Note:** Add selection area while the tool is active.  

### Temporarily subtract from selection
**Family:** Selection  
**Keys:** Alt+drag  
**Context:** Selection tool gesture  
**Note:** Subtract selected area while the tool is active.  

### Intersect with selection
**Family:** Selection  
**Keys:** Shift+Alt+drag  
**Context:** Selection tool gesture  
**Note:** Intersection of new and existing selections.  

### View layer mask alone
**Family:** Masks  
**Keys:** Alt+click mask thumbnail  
**Context:** Layers panel mouse gesture  
**Note:** Toggle grayscale mask-only view.  

### Disable/enable layer mask
**Family:** Masks  
**Keys:** Shift+click mask thumbnail  
**Context:** Layers panel mouse gesture  
**Note:** Temporarily bypass mask; red X marker shows disabled state.  

### Duplicate mask to another layer
**Family:** Masks  
**Keys:** Alt+drag mask thumbnail  
**Context:** Layers panel mouse gesture  
**Note:** Copies mask, leaving original attached.  

### Solo layer visibility
**Family:** Masks  
**Keys:** Alt+click eye icon  
**Context:** Layers panel mouse gesture  
**Note:** Restoration can be affected if you change other layer visibilities while isolated.  

### Zoom temporarily in
**Family:** View  
**Keys:** Ctrl+Space (hold)  
**Context:** Canvas gesture  
**Note:** May interact with Windows keyboard/layout and other tools.  

### Zoom temporarily out
**Family:** View  
**Keys:** Alt+Space (hold)  
**Context:** Canvas gesture  
**Note:** May conflict with Windows system menu in some environments.  

### Fit view to screen via Hand tool
**Family:** View  
**Keys:** Double-click Hand Tool  
**Context:** Toolbar mouse gesture  
**Note:** Shows entire document in available viewport.  

### 100% view via Zoom tool
**Family:** View  
**Keys:** Double-click Zoom Tool  
**Context:** Toolbar mouse gesture  
**Note:** Useful for assessing real pixel sharpness.  

### Previous brush preset
**Family:** Painting  
**Keys:** ,  
**Context:** Brush tool  
**Note:** Preset order and active brush tool determine behavior.  

### Next brush preset
**Family:** Painting  
**Keys:** .  
**Context:** Brush tool  
**Note:** Preset order and active brush tool determine behavior.  

### Temporarily erase with same brush tip
**Family:** Painting  
**Keys:** ~ (hold)  
**Context:** Brush tool  
**Note:** Switches brush to eraser mode on supported modern Photoshop setups.  

### Lock/unlock transparent pixels
**Family:** Painting  
**Keys:** /  
**Context:** Layers panel  
**Note:** Applies to appropriate pixel layer and context; can vary with keyboard layout.  

### Brush Settings panel
**Family:** Panels  
**Keys:** F5  
**Context:** Global/panel  
**Note:** Function keys may be intercepted by keyboard firmware or OS.  

### Color panel
**Family:** Panels  
**Keys:** F6  
**Context:** Global/panel  
**Note:** Function keys may be intercepted by keyboard firmware or OS.  

### Layers panel
**Family:** Panels  
**Keys:** F7  
**Context:** Global/panel  
**Note:** Function keys may be intercepted by keyboard firmware or OS.  

### Info panel
**Family:** Panels  
**Keys:** F8  
**Context:** Global/panel  
**Note:** Function keys may be intercepted by keyboard firmware or OS.  

### Actions panel
**Family:** Panels  
**Keys:** F9  
**Context:** Global/panel  
**Note:** Function keys may be intercepted by keyboard firmware or OS.  

### Liquify workspace
**Family:** Filters  
**Keys:** Ctrl+Shift+X  
**Context:** Document  
**Note:** GPU requirements, layer types and active document can prevent command.  

### Nudge selected content 1 pixel
**Family:** Layer  
**Keys:** Arrow key  
**Context:** Move Tool/transform  
**Note:** Depends on selected layer/selection and active text input.  

### Nudge selected content 10 pixels
**Family:** Layer  
**Keys:** Shift+Arrow key  
**Context:** Move Tool/transform  
**Note:** Depends on selected layer/selection and active text input.  

## Concept glossary

### Pixel
**Definition:** Smallest addressable raster sample; a color/alpha value at a grid coordinate.  
**Lesson:** s01l01  

### Raster
**Definition:** Image stored as an array of samples rather than mathematical objects.  
**Lesson:** s01l01  

### Vector
**Definition:** Geometry encoded by points, paths and equations, rendered to pixels for display.  
**Lesson:** s01l01  

### Resolution
**Definition:** Context-dependent amount of detail, commonly pixel dimensions or PPI.  
**Lesson:** s01l02  

### PPI
**Definition:** Pixels per inch in intended output; does not by itself create detail.  
**Lesson:** s01l02  

### DPI
**Definition:** Dots per inch of printing hardware; not interchangeable with image PPI.  
**Lesson:** s01l02  

### Resampling
**Definition:** Computing a new pixel grid at different dimensions.  
**Lesson:** s01l02  

### Interpolation
**Definition:** Estimating sample values between original samples.  
**Lesson:** s01l02  

### Canvas
**Definition:** Document's finite coordinate area.  
**Lesson:** s02l01  

### Crop
**Definition:** Changes visible frame and potentially removes outside pixels.  
**Lesson:** s02l01  

### Canvas Size
**Definition:** Command expanding or contracting document bounds without image resampling.  
**Lesson:** s02l01  

### Image Size
**Definition:** Command to change dimensions/resolution and optionally resample.  
**Lesson:** s02l01  

### Layer
**Definition:** Independently composited source of pixels, type, shape or adjustment.  
**Lesson:** s02l02  

### Stacking order
**Definition:** Front-to-back sequence determining occlusion/composite result.  
**Lesson:** s02l02  

### Group
**Definition:** Container organizing related layers.  
**Lesson:** s02l02  

### Opacity
**Definition:** Factor controlling the visibility of a layer or effect.  
**Lesson:** s04l04  

### Fill
**Definition:** Layer interior visibility setting distinct from overall Opacity when effects are used.  
**Lesson:** s04l04  

### Alpha
**Definition:** Opacity or coverage value stored per pixel or as a channel.  
**Lesson:** s02l04  

### Transparency
**Definition:** Partial or total absence of opacity in compositing.  
**Lesson:** s02l04  

### Checkerboard
**Definition:** UI visualization of transparent areas, not source pixels.  
**Lesson:** s02l04  

### PSD
**Definition:** Native layered Photoshop document format.  
**Lesson:** s01l03  

### PSB
**Definition:** Large Document Format for documents exceeding PSD practical limits.  
**Lesson:** s11l05  

### JPEG
**Definition:** Lossy photographic compression; generally flattened, with no alpha.  
**Lesson:** s01l03  

### PNG
**Definition:** Raster format supporting alpha transparency; not a full PSD replacement.  
**Lesson:** s02l04  

### TIFF
**Definition:** Flexible raster exchange and archival format, often supporting higher bit depths.  
**Lesson:** s01l03  

### WebP
**Definition:** Modern image format supporting efficient compression and optional transparency.  
**Lesson:** s10l04  

### RAW
**Definition:** Camera sensor-derived source data needing development rather than fixed rendering.  
**Lesson:** s08l04  

### DNG
**Definition:** Digital Negative raw container/specification supported by Camera Raw.  
**Lesson:** s08l04  

### XMP sidecar
**Definition:** Metadata file containing develop settings for some raw workflows.  
**Lesson:** s08l04  

### Selection
**Definition:** Temporary per-pixel editing coverage field.  
**Lesson:** s03l01  

### Marching ants
**Definition:** Animated boundary depicting part of a selection threshold.  
**Lesson:** s03l01  

### Feather
**Definition:** Softens selection or mask edge transition.  
**Lesson:** s03l04  

### Anti-aliasing
**Definition:** Blends edge pixels to reduce jagged contour appearance.  
**Lesson:** s03l04  

### Tolerance
**Definition:** Threshold controlling similarity in some selection/fill tools.  
**Lesson:** s03l02  

### Color Range
**Definition:** Selection from color similarity and fuzziness rather than just geometric area.  
**Lesson:** s03l02  

### Quick Mask
**Definition:** Temporary view/edit mode showing selection coverage as mask.  
**Lesson:** s03l05  

### Layer mask
**Definition:** Grayscale visibility control attached to a layer.  
**Lesson:** s03l03  

### Vector mask
**Definition:** Visibility boundary generated from editable path geometry.  
**Lesson:** s03l06  

### Clipping mask
**Definition:** Upper layer constrained by transparency of lower base layer.  
**Lesson:** s03l06  

### Alpha channel
**Definition:** Grayscale auxiliary channel that can store selection data.  
**Lesson:** s03l05  

### Composite channel
**Definition:** Combined color display assembled from component channels.  
**Lesson:** s08l02  

### RGB
**Definition:** Red/green/blue additive-color channel model.  
**Lesson:** s08l05  

### CMYK
**Definition:** Cyan/magenta/yellow/key print-separation channel model.  
**Lesson:** s08l05  

### Lab
**Definition:** Color model separating lightness from two opponent chromatic axes.  
**Lesson:** s08l05  

### Grayscale
**Definition:** Single-intensity color mode without normal chromatic channel variation.  
**Lesson:** s08l05  

### ICC profile
**Definition:** Data interpreting color numbers for a specific color space/device process.  
**Lesson:** s08l05  

### Embedded profile
**Definition:** Color profile stored in a file for correct interpretation.  
**Lesson:** s08l05  

### Assign Profile
**Definition:** Reinterprets existing color numbers under a new profile, potentially changing appearance.  
**Lesson:** s08l05  

### Convert to Profile
**Definition:** Changes channel values to retain approximate appearance under another profile.  
**Lesson:** s08l05  

### Working space
**Definition:** Color space used for editing or interpreting untagged data under settings.  
**Lesson:** s08l05  

### Gamut
**Definition:** Range of colors representable by a device or space.  
**Lesson:** s08l06  

### Soft proof
**Definition:** On-screen simulation of output profile under calibrated conditions.  
**Lesson:** s08l06  

### Rendering intent
**Definition:** Rule for mapping out-of-gamut colors during conversion.  
**Lesson:** s08l06  

### Bit depth
**Definition:** Number of binary bits per color component defining precision/range.  
**Lesson:** s08l05  

### 8-bit/channel
**Definition:** Usually 256 encoded values per channel in integer representation.  
**Lesson:** s08l05  

### 16-bit/channel
**Definition:** Higher-precision channel representation useful for smooth corrections.  
**Lesson:** s08l05  

### 32-bit/channel
**Definition:** Floating-point precision often used for HDR workflows.  
**Lesson:** s08l07  

### HDR
**Definition:** High dynamic range content or representation with extended luminance information.  
**Lesson:** s08l07  

### Histogram
**Definition:** Count of image pixels by channel or tonal interval.  
**Lesson:** s08l01  

### Exposure
**Definition:** Amount of image brightness associated with captured or interpreted light.  
**Lesson:** s08l01  

### White balance
**Definition:** Correction for color cast from illumination or camera setting.  
**Lesson:** s08l03  

### Clipping
**Definition:** Loss of differentiable highlight/shadow color values after limits are hit.  
**Lesson:** s08l01  

### Black point
**Definition:** Input or output value mapped to deepest intended tone.  
**Lesson:** s08l01  

### White point
**Definition:** Input or output value mapped to brightest intended tone.  
**Lesson:** s08l01  

### Levels
**Definition:** Tonal mapping through black, mid and white controls.  
**Lesson:** s08l01  

### Curves
**Definition:** Arbitrary control-point mapping of input to output tones.  
**Lesson:** s08l02  

### S-curve
**Definition:** Curve raising highlights and lowering shadows to increase contrast.  
**Lesson:** s08l02  

### Color grading
**Definition:** Intentional global/local color style beyond basic neutrality.  
**Lesson:** s08l03  

### HSL
**Definition:** Hue, saturation and lightness descriptors for color adjustment.  
**Lesson:** s08l03  

### Hue
**Definition:** Perceived color family or angle in color models.  
**Lesson:** s08l03  

### Saturation
**Definition:** Color intensity relative to gray at comparable lightness.  
**Lesson:** s08l03  

### Luminance
**Definition:** Light-related intensity measure; specific meaning depends on space.  
**Lesson:** s08l03  

### Smart Object
**Definition:** Container retaining source content for transforms and supported smart filters.  
**Lesson:** s04l02  

### Embedded Smart Object
**Definition:** Smart Object source stored inside PSD.  
**Lesson:** s04l02  

### Linked Smart Object
**Definition:** Smart Object whose source is an external file.  
**Lesson:** s04l02  

### Smart Filter
**Definition:** Editable supported filter attached to a Smart Object.  
**Lesson:** s04l03  

### Filter mask
**Definition:** Grayscale control of combined Smart Filter influence.  
**Lesson:** s04l03  

### Adjustment layer
**Definition:** Non-destructive computed tone/color adjustment over underlying pixels.  
**Lesson:** s04l01  

### Blend mode
**Definition:** Rule mathematically combining layer and underlying image color values.  
**Lesson:** s04l04  

### Multiply
**Definition:** Blend mode tending to darken through channel multiplication.  
**Lesson:** s04l04  

### Screen
**Definition:** Blend mode tending to brighten through inverse multiplicative math.  
**Lesson:** s04l04  

### Overlay
**Definition:** Contrast blend mode combining Multiply/Screen behavior conditionally.  
**Lesson:** s04l04  

### Blend If
**Definition:** Layer Style threshold-based visibility using tonal ranges.  
**Lesson:** s04l05  

### Layer Style
**Definition:** Live appearance effects such as Stroke, Shadow and Glow.  
**Lesson:** s02l05  

### Drop Shadow
**Definition:** Layer effect producing offset shadow based on layer contours.  
**Lesson:** s02l05  

### Stroke
**Definition:** Visible line placed around a vector path or layer boundary.  
**Lesson:** s02l05  

### Transform
**Definition:** Geometric change such as scale, rotate, warp or skew.  
**Lesson:** s02l03  

### Free Transform
**Definition:** General handles-based transform workflow.  
**Lesson:** s02l03  

### Perspective
**Definition:** Projection geometry causing parallel 3D lines to converge in image.  
**Lesson:** s09l01  

### Vanishing point
**Definition:** Projected location where parallel scene lines appear to meet.  
**Lesson:** s09l01  

### Horizon
**Definition:** Camera eye-level reference in perspective geometry.  
**Lesson:** s09l01  

### Contact shadow
**Definition:** Darkening immediately beneath contact where light is blocked.  
**Lesson:** s09l02  

### Cast shadow
**Definition:** Shadow projected onto a separate surface by an object blocking light.  
**Lesson:** s09l02  

### Atmospheric perspective
**Definition:** Reduced distant contrast and possible color shift from air scattering.  
**Lesson:** s09l04  

### Depth of field
**Definition:** Range of subject distances appearing acceptably sharp.  
**Lesson:** s09l04  

### Gaussian Blur
**Definition:** Spatial smoothing weighted by Gaussian distribution.  
**Lesson:** s04l03  

### Unsharp Mask
**Definition:** Edge-contrast sharpening with controls Amount, Radius and Threshold.  
**Lesson:** s08l07  

### Halo
**Definition:** Unnatural light or dark band around an edge from edits or masking.  
**Lesson:** s09l03  

### Noise
**Definition:** Unpredictable pixel variations from capture, processing or synthesis.  
**Lesson:** s08l07  

### Denoise
**Definition:** Reduction of noise, often at some fine-detail cost.  
**Lesson:** s08l07  

### Texture
**Definition:** Small repeating or stochastic image detail.  
**Lesson:** s05l01  

### Healing
**Definition:** Retouch method matching borrowed texture with target surroundings.  
**Lesson:** s05l01  

### Cloning
**Definition:** Direct copying of pixels from source to target.  
**Lesson:** s05l02  

### Content-Aware Fill
**Definition:** Synthesizes replacement pixels using analyzed neighborhood information.  
**Lesson:** s05l03  

### Remove Tool
**Definition:** Photoshop retouch brush for inferred removal, with model-dependent processing.  
**Lesson:** s05l03  

### Frequency separation
**Definition:** Technique operating on different spatial scales of image detail.  
**Lesson:** s09l06  

### Dodge
**Definition:** Local brightening operation.  
**Lesson:** s05l05  

### Burn
**Definition:** Local darkening operation.  
**Lesson:** s05l05  

### Liquify
**Definition:** Specialized image geometry warp interface.  
**Lesson:** s05l05  

### Brush opacity
**Definition:** Maximum contribution of brush stroke across area.  
**Lesson:** s06l01  

### Brush flow
**Definition:** Rate of paint deposition during a stroke.  
**Lesson:** s06l01  

### Hardness
**Definition:** Softness of a brush tip edge.  
**Lesson:** s06l01  

### Smoothing
**Definition:** Pointer path stabilization for brush strokes.  
**Lesson:** s06l02  

### Pen pressure
**Definition:** Stylus force data used for brush dynamics on supported tablets.  
**Lesson:** s06l02  

### Gradient
**Definition:** Continuous transition between colors or opacity levels.  
**Lesson:** s06l04  

### Pattern
**Definition:** Tiled repeated image or fill design.  
**Lesson:** s06l04  

### Foreground color
**Definition:** Current primary painting/fill color.  
**Lesson:** s06l03  

### Swatch
**Definition:** Saved color for repeated access.  
**Lesson:** s06l03  

### Path
**Definition:** Editable geometric contour defined by anchors and segments.  
**Lesson:** s07l04  

### Anchor point
**Definition:** Path control point that defines contour position.  
**Lesson:** s07l04  

### Bézier handle
**Definition:** Direction vector influencing tangent and curvature of path segment.  
**Lesson:** s07l04  

### Point type
**Definition:** Text entered at single click origin, extending with text.  
**Lesson:** s07l01  

### Paragraph type
**Definition:** Text flowing inside a sized bounding box.  
**Lesson:** s07l01  

### Kerning
**Definition:** Spacing adjustment for a particular glyph pair.  
**Lesson:** s07l02  

### Tracking
**Definition:** Overall spacing across selected glyphs.  
**Lesson:** s07l02  

### Leading
**Definition:** Distance from one line baseline to the next.  
**Lesson:** s07l02  

### Glyph
**Definition:** Specific drawn appearance of a character in font.  
**Lesson:** s07l02  

### Anti-aliased type
**Definition:** Rasterized glyph edges smoothed by partial pixel coverage.  
**Lesson:** s07l01  

### Dynamic Text
**Definition:** Recent feature extending text layout along shapes/paths; availability version-specific.  
**Lesson:** s07l05  

### Actions
**Definition:** Recorded command sequences replayable in Photoshop.  
**Lesson:** s10l02  

### Batch
**Definition:** Automatic operation across a set of source files.  
**Lesson:** s10l02  

### UXP
**Definition:** Modern Photoshop plugin extensibility platform.  
**Lesson:** s10l04  

### Export As
**Definition:** Asset-oriented export dialog distinct from editable Save As.  
**Lesson:** s10l05  

### Preflight
**Definition:** Structured verification of outputs against recipient technical requirements.  
**Lesson:** s10l06  

### Scratch disk
**Definition:** Drive space used by Photoshop for temporary working data.  
**Lesson:** s11l01  

### GPU
**Definition:** Graphics processor accelerating compatible display and image operations.  
**Lesson:** s11l01  

### DirectX
**Definition:** Windows graphics API used to describe supported GPU feature levels.  
**Lesson:** s11l02  

### VRAM
**Definition:** Graphics memory available to GPU features.  
**Lesson:** s11l02  

### Virtual GPU
**Definition:** Graphics adapter presented by virtualization host to guest system.  
**Lesson:** s11l02  

### PCIe passthrough
**Definition:** Advanced technique assigning physical hardware directly to a guest where supported.  
**Lesson:** s11l02  

### Preferences
**Definition:** Application configuration settings, distinct from document data.  
**Lesson:** s01l04  

### Workspace
**Definition:** Stored UI panel arrangement.  
**Lesson:** s01l04  

### History state
**Definition:** Session snapshot of editing actions, not permanent backup.  
**Lesson:** s01l06  

### Generative credits
**Definition:** Plan-based metering of certain Adobe and partner AI operations.  
**Lesson:** s11l06  

### Generative Fill
**Definition:** Prompt-based image insertion/removal/replacement using supported generative service.  
**Lesson:** s11l06  

### On-device model
**Definition:** ML model running locally after installation and hardware checks.  
**Lesson:** s11l06  

### Beta
**Definition:** Pre-release feature/channel not to be assumed stable or permanent.  
**Lesson:** s11l06  

### LTS
**Definition:** Long-term-support release branch with extended security/maintenance policy.  
**Lesson:** s11l06  

### Brush spacing
**Definition:** Distance between individual brush-tip imprints; smaller spacing generally produces smoother continuous strokes.  
**Lesson:** s06l01  

### Brush jitter
**Definition:** Controlled randomness in size, angle, position or color of repeated brush marks.  
**Lesson:** s06l02  

### ICC rendering intent
**Definition:** Rule for mapping colors between gamuts during a conversion, especially perceptual versus relative colorimetric.  
**Lesson:** s08l06  

### Smart Filter stacking
**Definition:** Order of filters attached to Smart Objects; changing order can change the final image.  
**Lesson:** s04l03  

### Clipped adjustment
**Definition:** An adjustment constrained by the underlying layer or clip base, distinct from masking by painted gray values.  
**Lesson:** s04l01  

### Alpha lock
**Definition:** Prevents painting into fully transparent areas on supported raster layers.  
**Lesson:** s02l04  

### Export preflight
**Definition:** Final inspection of dimensions, color profile, transparency, filenames and deliverable requirements.  
**Lesson:** s10l05  

## Troubleshooting

### Photoshop won't launch
**Cause:** Outdated driver; corrupt preferences; plugin fault; unsupported Windows build  
**Diagnosis:** Check Help/Creative Cloud version and Windows Event Viewer; launch without optional plugins; test fresh user settings  
**Solution:** Update to compatible driver and supported OS; preserve settings before reset  
**Warning:** Do not delete the only preference backup  
**Lesson:** s11l03  

### Scratch disks are full
**Cause:** Insufficient free storage; huge temporary documents  
**Diagnosis:** Inspect free internal SSD space and scratch preference assignments  
**Solution:** Free disk safely after closing Photoshop; add suitable SSD scratch disk  
**Warning:** Do not manually delete active Photoshop scratch files  
**Lesson:** s11l01  

### GPU unavailable or grayed out
**Cause:** Unsupported DX12 feature level; VM virtual adapter; driver issue  
**Diagnosis:** Help > System Info and Device Manager > Display adapters  
**Solution:** Install vendor driver or provide supported GPU to guest; accept feature limits if not possible  
**Warning:** Do not assume host GPU is visible inside VM  
**Lesson:** s11l02  

### Blur Gallery / Oil Paint missing
**Cause:** GPU unsupported, color depth/mode incompatible  
**Diagnosis:** Edit > Preferences > Performance and Image > Mode  
**Solution:** Enable suitable GPU and test supported mode after saving copy  
**Warning:** Converting bit depth can change image precision  
**Lesson:** s11l01  

### Camera Raw Filter disabled
**Cause:** Unsupported bit depth or layer type  
**Diagnosis:** Image > Mode; selected layer properties  
**Solution:** Try supported 8/16-bit copy and suitable Smart Object  
**Warning:** Preserve 32-bit HDR original  
**Lesson:** s08l04  

### Generative Fill gray
**Cause:** Missing selection; unsupported RGB/bit depth; login or internet/credits  
**Diagnosis:** Check mode, layer, selection, account connectivity  
**Solution:** Use supported RGB 8-bit workflow and verify plan entitlement  
**Warning:** Do not bypass cloud/account restrictions  
**Lesson:** s11l06  

### Remove Tool fails
**Cause:** Unsupported on-device model; networking; GPU; source complexity  
**Diagnosis:** Check model selection, installed state and image mode  
**Solution:** Select compatible processing and refine with healing/cloning  
**Warning:** Inferred replacement may alter scene facts  
**Lesson:** s05l03  

### Brush paints nothing
**Cause:** Wrong layer/mask; hidden layer; zero flow/opacity; selection active  
**Diagnosis:** Inspect layer thumbnail and brush controls; Ctrl+D if unintended selection  
**Solution:** Choose correct editable target, set opacity/flow, unlock  
**Warning:** Avoid accidental painting on master  
**Lesson:** s06l01  

### Layer won't move
**Cause:** Locked layer; wrong target; auto-select settings  
**Diagnosis:** Inspect layer lock and Layers selection  
**Solution:** Unlock permitted layers and select correct layer  
**Warning:** Do not flatten merely to enable move  
**Lesson:** s02l03  

### Cannot select subject accurately
**Cause:** Weak contrast; motion blur; transparency and hair  
**Diagnosis:** Inspect at 100% on light/dark backgrounds  
**Solution:** Combine Object Selection with Select and Mask and local brush refinements  
**Warning:** Do not claim perfect AI edge in all lighting  
**Lesson:** s03l04  

### Mask shows black or white unexpectedly
**Cause:** Selected mask thumbnail; inverted mask; wrong brush color  
**Diagnosis:** Alt-click mask and inspect white/black coverage  
**Solution:** Press D/X for default and swap colors; Ctrl+I deliberately only when appropriate  
**Warning:** Do not delete hidden source pixels  
**Lesson:** s03l03  

### Export has white background
**Cause:** Opaque layer still visible; wrong format; transparency disabled  
**Diagnosis:** Hide all background layers and inspect checkerboard  
**Solution:** Export PNG with transparency, retest in viewer  
**Warning:** JPEG does not store transparency  
**Lesson:** s02l04  

### PNG edges have halos
**Cause:** Selection fringe; premultiplication; matte mismatch  
**Diagnosis:** View over dark and bright test layers  
**Solution:** Refine mask and decontaminate only as needed  
**Warning:** Strong feather can worsen fringing  
**Lesson:** s09l03  

### Text font missing
**Cause:** Font not installed/licensed; creative cloud sync  
**Diagnosis:** Inspect Type warning and Character panel font  
**Solution:** Install licensed font or intentionally substitute and reflow  
**Warning:** Do not redistribute restricted fonts  
**Lesson:** s11l04  

### Text wraps differently
**Cause:** Missing font, differing tracking or bounding box  
**Diagnosis:** Check exact font, Paragraph width and Character settings  
**Solution:** Use installed font and fixed style guide  
**Warning:** Do not rasterize master just to conceal issue  
**Lesson:** s07l02  

### Shortcut types into field
**Cause:** Focus is in text input; custom shortcuts  
**Diagnosis:** Press Esc/click away; inspect Edit > Keyboard Shortcuts  
**Solution:** Exit active text field then retry  
**Warning:** Key mappings differ if customized  
**Lesson:** s01l04  

### Ctrl+Z behaves differently
**Cause:** Text field focus; undo/redo context  
**Diagnosis:** Inspect History panel and active caret  
**Solution:** Exit field and test known document operation  
**Warning:** Undo buffer isn't a backup  
**Lesson:** s01l06  

### Colors look different in viewer
**Cause:** Profile missing; uncalibrated display; unmanaged app  
**Diagnosis:** Check embedded ICC and proof view; compare in color-managed viewer  
**Solution:** Convert with correct profile, embed it on export as supported  
**Warning:** Assigning arbitrary profile may distort appearance  
**Lesson:** s08l05  

### Print too dark
**Cause:** Screen brightness; missing output profile; uncalibrated printer  
**Diagnosis:** Review soft proof and test print with printer/paper ICC  
**Solution:** Calibrate monitor and use correct output workflow  
**Warning:** No universal one-click print fix  
**Lesson:** s08l06  

### Gradients show banding
**Cause:** 8-bit quantization; aggressive stretch; export artifacts  
**Diagnosis:** Inspect at 100% in PSD then final export  
**Solution:** Work at higher precision when appropriate; add modest dither/noise  
**Warning:** Some delivery formats reintroduce banding  
**Lesson:** s06l04  

### Large PSD slow
**Cause:** Memory/scratch pressure; excessive layers; high pixel count  
**Diagnosis:** Inspect Photoshop Performance and Windows Task Manager  
**Solution:** Use organized Smart Objects, adequate RAM and SSD scratch  
**Warning:** Flatten only a delivery copy  
**Lesson:** s11l05  

### PSD too large to save
**Cause:** Exceeds PSD limits  
**Diagnosis:** Review dimensions and file size  
**Solution:** Use PSB if receiver supports it  
**Warning:** PSB acceptance varies by downstream application  
**Lesson:** s11l05  

### Linked files missing
**Cause:** Paths moved or omitted from handoff  
**Diagnosis:** Inspect layer link warning and project folder  
**Solution:** Relink to shipped source files and re-save copy  
**Warning:** Do not send only PSD if links remain external  
**Lesson:** s10l01  

### Corrupt file
**Cause:** Interrupted write; storage trouble; plugin problem  
**Diagnosis:** Try earlier versioned files and verified backups  
**Solution:** Restore known-good copy and investigate storage  
**Warning:** Never overwrite last working revision  
**Lesson:** s11l05  

### Photoshop in VM very slow
**Cause:** No passed GPU; low RAM/vRAM; disk I/O  
**Diagnosis:** Inspect guest GPU capabilities and scratch location  
**Solution:** Allocate adequate guest resources, test appropriate hypervisor GPU features  
**Warning:** Official host spec is not a VM guarantee  
**Lesson:** s11l02  

### Cloud feature unavailable offline
**Cause:** Requires sign-in, credits, cloud request  
**Diagnosis:** Check service docs and account; disconnect only for safe test  
**Solution:** Use manual masking, heal, clone and local adjustment tools  
**Warning:** Offline manual is not offline AI service  
**Lesson:** s11l06  

### Export size wrong
**Cause:** Resampling settings, ratio, artboard bounds  
**Diagnosis:** Inspect File > Export > Export As preview dimensions  
**Solution:** Set explicit dimensions and verify exported pixel size  
**Warning:** Print PPI != pixel count  
**Lesson:** s10l05  

### Smart Filter missing
**Cause:** Layer wasn't Smart Object or operation not supported  
**Diagnosis:** Inspect filter target and layer icon  
**Solution:** Convert eligible layer before filter; confirm smart compatibility  
**Warning:** Not every filter is smart-compatible  
**Lesson:** s04l03  

### Over-sharpened edges
**Cause:** Amount/Radius too strong; repeated sharpening  
**Diagnosis:** Inspect at 100% against original  
**Solution:** Lower sharpening and apply after final resize  
**Warning:** Halos cannot create authentic detail  
**Lesson:** s08l07  

### Automated batch overwrites files
**Cause:** Save path recorded; filename collision  
**Diagnosis:** Test one input and output folder before batch  
**Solution:** Use separate destination and unique naming  
**Warning:** Always preserve originals outside destination  
**Lesson:** s10l02  

## Professional recipes

### Remove a simple solid-color background
**Requires:** s03l02, s03l03  
**Procedure:** Select background with Magic Wand or Color Range; inspect tolerance; add layer mask; refine at 100%; export PNG with alpha.  
**Pass:** Transparent PNG with no obvious fringes.  

### Extract hair against mixed tones
**Requires:** s03l04, s03l03  
**Procedure:** Select subject roughly; enter Select and Mask; check dark/light previews; use edge refinement cautiously; output New Layer with Mask; test on two backdrops.  
**Pass:** No prominent halo or lost major strands.  

### Replace a sky without flattening
**Requires:** s03l03, s04l02, s09l03  
**Procedure:** Duplicate source; mask the sky; place replacement beneath; match horizon and exposure using clipped Curves; inspect tree edges.  
**Pass:** Sky change can be undone by turning off replacement.  

### Restore a clipped logo edge
**Requires:** s03l06, s07l04  
**Procedure:** Trace Pen path with few anchors; form vector mask; adjust handles at 200%; evaluate final-size export.  
**Pass:** Sharp smooth edge without stair-step trace.  

### Make a circular profile image
**Requires:** s03l01, s03l03  
**Procedure:** Make elliptical selection; apply Reveal Selection mask; center portrait; export transparent PNG.  
**Pass:** Correct circular alpha boundary.  

### Brighten only a face
**Requires:** s04l01, s05l05  
**Procedure:** Add Curves brighten layer; invert mask; soft-white low-opacity paint on face; compare before/after.  
**Pass:** Background retains original exposure.  

### Remove a small blemish
**Requires:** s05l01  
**Procedure:** Make blank cleanup layer; sample all layers; paint just over defect with Spot Healing; examine at 100%.  
**Pass:** Texture continuous and source unchanged.  

### Clone a scratch across repeated texture
**Requires:** s05l02  
**Procedure:** Sample near defect with Alt-click; clone short segments while frequently resampling; check for repeated motifs.  
**Pass:** Scratch invisible without repetitive patches.  

### Rebuild damaged image corner
**Requires:** s05l06, s05l02  
**Procedure:** Save archival copy; select good similar region; clone geometric structure on new layer; document inference; blend tone.  
**Pass:** Corner improved and reconstruction documented.  

### Remove a cable from wall
**Requires:** s05l03, s05l02  
**Procedure:** Paint cable using Remove; inspect texture and vertical lines; fix repetitions with Clone/Healing; save editable layer.  
**Pass:** No duplicate wall details.  

### Retouch skin without waxy blur
**Requires:** s05l04, s05l05  
**Procedure:** Heal isolated marks; dodge/burn subtle uneven tone on Curves masks; inspect pores at 100%.  
**Pass:** Texture remains natural.  

### Make a realistic contact shadow
**Requires:** s09l02, s04l03  
**Procedure:** Paint tight dark mark directly under object; separate softer longer shadow; blur on Smart Object; reduce opacity.  
**Pass:** Subject visually rests on floor.  

### Match lighting on a cutout
**Requires:** s09l01, s09l03  
**Procedure:** Identify light direction; clip Curves and Color Balance to subject; refine masked edge; compare black point.  
**Pass:** Subject and scene share illumination logic.  

### Create fake atmospheric depth
**Requires:** s09l04  
**Procedure:** Place distant objects in separate group; mask pale fog layer to distance; reduce distant contrast and blur slightly.  
**Pass:** Foreground stays crisp and distance recedes.  

### Make a glass-style highlight
**Requires:** s04l04, s09l02  
**Procedure:** Paint small controlled highlight on separate Screen layer; mask edges to shape; soften one side; align to scene light.  
**Pass:** Highlight reinforces form without milky haze.  

### Apply print-like grain
**Requires:** s09l06, s08l07  
**Procedure:** Create a grain layer with Add Noise; use blending and opacity modestly; evaluate at final output scale.  
**Pass:** Grain integrates rather than overwhelms.  

### Make a sharp product label
**Requires:** s07l03, s07l02  
**Procedure:** Use shape path for label; set editable type; use consistent guides and padding; add subtle Stroke.  
**Pass:** High contrast, legible at actual size.  

### Create a magazine cover
**Requires:** s07l02, s07l06  
**Procedure:** Place photograph; use three text hierarchy levels; keep safe margins; test contrast with image; export proof.  
**Pass:** Readable title, subhead and caption.  

### Place a logo on fabric
**Requires:** s09l05, s04l04  
**Procedure:** Create grayscale displacement PSD of folds; apply Displace to logo Smart Object if supported; blend fabric shadow through logo; compare at 100%.  
**Pass:** Folds subtly affect logo without excessive warping.  

### Prepare social post variants
**Requires:** s10l03, s10l05  
**Procedure:** Duplicate master, adapt square and portrait canvas; reflow text; inspect every edge; export at specified pixel sizes.  
**Pass:** Two consistent, non-cropped exports.  

### Batch resize event thumbnails
**Requires:** s10l02, s10l05  
**Procedure:** Record safe resize action; test on one, then three files; Batch to separate output folder; validate dimensions.  
**Pass:** All thumbnails consistent, originals untouched.  

### Export transparent UI icon
**Requires:** s02l04, s07l03, s10l05  
**Procedure:** Create shape layer in transparent canvas; export PNG with transparency; reopen over dark and light backgrounds.  
**Pass:** Crisp alpha on both backgrounds.  

### Prepare for print
**Requires:** s08l05, s08l06, s10l06  
**Procedure:** Confirm bleed with printer; verify pixel dimensions and embedded profile; soft proof using provided paper ICC; export as required.  
**Pass:** Printer-specific checklist completed.  

### Create a sharp website hero
**Requires:** s02l01, s08l07, s10l05  
**Procedure:** Crop nondestructively to final ratio; resize delivery copy; apply moderate output sharpen; export suitable JPEG/WebP if receiver supports.  
**Pass:** Clean final pixels without sharpening halos.  

### Fix magenta/green cast
**Requires:** s08l02, s08l03  
**Procedure:** Select neutral sample; adjust green channel Curve or Color Balance gently; inspect flesh tones; constrain with mask.  
**Pass:** Neutrals more plausible without clipped channels.  

### Build an editable color grade
**Requires:** s04l01, s08l03  
**Procedure:** Make Curves for contrast and a separate Hue/Saturation or Color Balance layer; name by effect; compare at reduced size.  
**Pass:** Grade can be disabled in one click.  

### Create type on a curve
**Requires:** s07l04, s07l05  
**Procedure:** Draw Pen path; click with Type Tool; enter short phrase; adjust tracking and start position; keep text layer editable.  
**Pass:** Glyphs flow smoothly without collisions.  

### Make a three-level digital painting
**Requires:** s06l01, s06l06  
**Procedure:** Separate background, midground and subject; establish grayscale value hierarchy; introduce limited hue palette; inspect thumbnail.  
**Pass:** Focal region readable without detail.  

### Repair an overexposed image modestly
**Requires:** s08l01, s08l04  
**Procedure:** Inspect histogram; reduce highlights using Camera Raw or Light adjustment; check whether original channels retain data; avoid inventing recovery.  
**Pass:** Improvement without fabricated texture claims.  

### Package an editable handoff
**Requires:** s10l01, s04l06  
**Procedure:** Bundle source/work/exports; audit links and fonts; save PSD plus preview; reopen from moved folder.  
**Pass:** Another computer can relink and review without guessing.  

### Make a reversible crop
**Requires:** s02l01  
**Procedure:** Select Crop Tool; disable Delete Cropped Pixels; commit; inspect outside frame by expanding crop; keep a layered master.  
**Pass:** Original crop area can be recovered before final delivery.  

### Clean a mask fringe
**Requires:** s03l03, s03l04  
**Procedure:** Place subject against white and black layers; open Select and Mask; try restrained edge refinement and Decontaminate Colors only when outputting safely to a separate result; inspect at 100%.  
**Pass:** Edges remain clean on both backgrounds with original mask retained.  

### Build controlled rim lighting
**Requires:** s04l01, s05l05  
**Procedure:** Create a Curves brighten adjustment, invert mask to black, paint a low-flow soft white edge on subject side and adjust opacity.  
**Pass:** Lighting direction is consistent and no harsh white outline appears.  

### Create multiple editable artboard sizes
**Requires:** s02l02, s10l05  
**Procedure:** Create artboards for distinct delivery sizes; reuse linked Smart Objects and text; inspect each trim independently; export artboards per output constraints.  
**Pass:** Each exported variant has expected dimensions and editable text in the master.  

### Check missing linked assets
**Requires:** s04l02, s10l01  
**Procedure:** Inspect Layers for warning icons; check File > Package where available; duplicate project folder and reopen; relink from included source folder.  
**Pass:** Transferred project opens with the intended original linked graphics.  

### Verify a transparent export
**Requires:** s02l04, s10l05  
**Procedure:** Hide all opaque background layers; use Export As > PNG with transparency; reopen against dark and light backgrounds.  
**Pass:** No white rectangular matte or unwanted halo remains.  

### Inspect two different ICC previews
**Requires:** s08l05, s08l06  
**Procedure:** Preserve RGB master; set destination in View > Proof Setup > Custom; toggle Proof Colors; compare with profile embedded in final exported copy.  
**Pass:** Report identifies soft-proof profile and documents visible changes without overwriting master.  

### Compare blur as Smart Filter and raster edit
**Requires:** s04l02, s04l03  
**Procedure:** Duplicate an image layer; convert one copy to Smart Object and apply Gaussian Blur; blur other raster copy directly; close and reopen PSD; try editing both.  
**Pass:** Smart Filter settings remain separately adjustable; direct blur is baked into raster pixels.  

### Inspect a suspicious keyboard shortcut
**Requires:** s01l04, s11l03  
**Procedure:** Open Edit > Keyboard Shortcuts (Ctrl+Alt+Shift+K); choose Tools or Application Menus; record exact assigned key; compare with manual and look for user customization.  
**Pass:** Report distinguishes installed assignment from historical or documented default.  

### Separate AI-generated and recovered content
**Requires:** s05l07, s11l06  
**Procedure:** Save archival original; keep AI-assisted reconstruction on a named layer; label uncertain invented detail; include original plus change log in handoff.  
**Pass:** A reviewer can see which regions were authentically preserved and which were inferred.  

# Version changes and limitations

### Light adjustment layer
stable; 27.10 (August 2026). Exposure, Contrast, Highlights, Shadows, Whites and Blacks on live adjustment layer.

### Enhance edge
stable; 27.11 (September 2026). AI-powered selection edge refinement; cloud/model conditions need current in-app check.

### GPT Image 2 model
online model option; 27.11 (September 2026). Available for Generate Image/Prompt to edit as listed in release notes; entitlement/model list may change.

### On-device Remove Tool model
stable, conditional; 27.7 (May 2026). Downloadable local model on supported hardware; not the same as all generative features working offline.

### Generative Fill / Generate Image / Harmonize
online/service; features of stable release. Account, service, generative credits and sometimes model picker required.

### AI Assisted Editor
Beta; 27.10 (August 2026). Explicit Beta; not required curriculum and not treated as stable.

### Modernized Toolbar and Tool Options
Beta; Oct 15, 2026 Beta announcement. Not assumed in the 27.11 stable UI.

### Dynamic Text along shapes/paths
stable; 27.6/27.10 (2026). Newer controls; ordinary editable path text taught as universal prerequisite.

### Save As format customization
stable; 27.10 (August 2026). Show, hide and reorder formats in Save As and Save a Copy dialogs.

### Recent document presets management
stable; 27.11 (September 2026). Rename/delete Recents in New Document dialog.

### 3D legacy tools
removed; legacy, removed before 27.11. Do not use old 3D tutorials as current Photoshop production commands.

### Save for Web
legacy / hidden by default; older workflow. Use Export As in modern workflow; historical recipes may mention Save for Web.

### LTS maintenance branch
separate version; 26.11.8 as of Oct 13, 2026. Not same as current feature branch 27.11.

### Camera Raw
separately versioned plugin; 18.7 installer listed Sep 2026. Check Help > About Plug-In > Camera Raw; do not confuse with Photoshop version.

# Research sources

- Adobe Photoshop desktop release notes: https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html (checked 2026-10-28). Last updated Oct 5, 2026. September 2026 version 27.11; recent feature changes in 27.6–27.11.
- Adobe Photoshop security bulletin APSB26-158: https://www.adobe.com/trust/security/products/photoshop/apsb26-158.html (checked 2026-10-28). Published Oct 13, 2026. Photoshop 2026 fixed/updated at 27.11, and LTS branch 26.11.8; confirms patch baseline.
- Adobe supported Photoshop versions: https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/photoshop-supported-versions.html (checked 2026-10-28). Sep 28, 2026. Stable current 27.x and prior 26.x; Help > About Photoshop on Windows.
- Adobe desktop technical requirements: https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/adobe-photoshop-on-desktop-technical-requirements.html (checked 2026-10-28). Sep 9, 2026. Windows requirements for 27.x; CPU/RAM/GPU/DirectX/scratch/internet.
- Adobe View keyboard shortcuts: https://helpx.adobe.com/photoshop/desktop/get-started/settings-and-preferences/view-keyboard-shortcuts.html (checked 2026-10-28). Sep 8, 2026. Edit > Keyboard Shortcuts and Ctrl+Alt+Shift+K; shortcut override verification method.
- Adobe filter effects reference: https://helpx.adobe.com/photoshop/desktop/effects-filters/blur-sharpen-filters/filter-effects-reference.html (checked 2026-10-28). Oct 4, 2026. Blur, sharpen, sketch and other filter classifications and bit-depth caveats.
- Adobe filters overview: https://helpx.adobe.com/photoshop/desktop/effects-filters/get-started-with-filters/filters-overview.html (checked 2026-10-28). Feb 23, 2026. Categories, Smart Filter compatibility and filter restrictions.
- Adobe Filter Gallery overview: https://helpx.adobe.com/photoshop/desktop/effects-filters/get-started-with-filters/filter-gallery.html (checked 2026-10-28). Current Adobe gallery descriptions and category explanations.
- Adobe Adjust image lighting with Light: https://helpx.adobe.com/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/adjust-image-lighting-with-light.html (checked 2026-10-28). Sep 9, 2026. Light adjustment layer introduced in 27.10 and six controls.
- Adobe adjust image color and tone: https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/adjust-image-color-and-tone.html (checked 2026-10-28). Sep 30, 2026. Adjustment layers versus Camera Raw and mask behavior.
- Adobe Generative Fill desktop: https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/edit-images-with-generative-fill.html (checked 2026-10-28). Sep 2026. Selection-based generative edits, model picker and output variations.
- Adobe generative AI overview: https://helpx.adobe.com/photoshop/desktop/generative-ai/generative-ai-features-overview.html (checked 2026-10-28). May 20, 2026. Cloud generative features and credits.
- Adobe generative troubleshooting: https://helpx.adobe.com/photoshop/kb/troubleshoot-generative-ai-features.html (checked 2026-10-28). Mode/bit-depth/selection, account/internet and credits requirements may constrain Generative Fill.
- Adobe on-device Remove model release evidence: https://helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html (checked 2026-10-28). May 2026 feature update: Remove local model after download and hardware check.
- Adobe filters troubleshooting: https://helpx.adobe.com/photoshop/desktop/troubleshoot/tool-feature-issues/filters-and-effects-errors.html (checked 2026-10-28). Oct 4, 2026. Filter limitations; GPU and mode diagnostics.
- Adobe Shake Reduction removal notice: https://helpx.adobe.com/photoshop/using/reduce-camera-shake-induced-blurring.html (checked 2026-10-28). May 2023. Adobe confirms removal starting with Photoshop 23.3 (April 2022); legacy only in 27.11.
- Adobe Topaz AI Sharpen and AI Denoise: https://helpx.adobe.com/in/photoshop/desktop/effects-filters/artistic-stylize-filters/enhance-images-with-generative-ai-filters.html (checked 2026-10-28). December 2025. Filter > AI Sharpen / Filter > AI Denoise, premium usage credits, 56 MP file limit and active-layer replacement.
- Adobe GPU setup: https://helpx.adobe.com/photoshop/desktop/get-started/technical-requirements-installation/enable-photoshop-to-use-the-graphics-processor.html (checked 2026-10-28). Feb 23, 2026. Edit > Preferences > Performance on Windows.
- Adobe Camera Raw introduction: https://helpx.adobe.com/camera-raw/desktop/get-started/overview-and-setup/introduction-camera-raw.html (checked 2026-10-28). Sep 29, 2026. RAW processing, metadata sidecars and Smart Object workflow.
- Adobe Camera Raw installer: https://helpx.adobe.com/camera-raw/desktop/troubleshoot/camera-raw-plug-in-installer.html (checked 2026-10-28). Sep 29, 2026. Lists Camera Raw 18.7 installer; plug-in version may vary from Photoshop.
- Adobe camera raw GPU troubleshooting: https://helpx.adobe.com/camera-raw/desktop/troubleshoot/acr-gpu-faq.html (checked 2026-10-28). GPU compatibility and guest/driver diagnostics.
- Adobe Photoshop preset file locations: https://helpx.adobe.com/photoshop/desktop/apply-painting-techniques/brushes-presets/photoshop-presets-locations.html (checked 2026-10-28). Legacy 3D removed; Save for Web legacy hidden since 23.0 according to current Adobe note.
- Adobe Add layer masks: https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/add-layer-masks.html (checked 2026-10-28). Dec 2025. Reveal and hide selections and mask gestures on Windows.
- Adobe linked Smart Objects: https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/create-linked-smart-objects.html (checked 2026-10-28). Feb 23, 2026. File > Place Linked and linked layer icon.
- Adobe Smart Objects overview: https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/smart-objects-overview-and-benefits.html (checked 2026-10-28). Feb 23, 2026. Editable transforms/filters, embedded versus linked, and painting limits.
- Adobe package linked Smart Objects: https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/package-linked-smart-objects.html (checked 2026-10-28). Feb 23, 2026. File > Package; include linked assets for portable delivery.
- Adobe Remove objects tool: https://helpx.adobe.com/photoshop/desktop/repair-retouch/remove-objects-fill-space/remove-unwanted-objects-and-distractions.html (checked 2026-10-28). Aug 18, 2026. Remove Tool processing modes including Device and Cloud.
- Adobe Remove Tool hardware requirements: https://helpx.adobe.com/photoshop/desktop/repair-retouch/remove-objects-fill-space/remove-tool-minimum-and-recommended-hardware-requirements.html (checked 2026-10-28). Aug 18, 2026. On-device model requirements may substantially exceed normal Photoshop minimum.
- Adobe combine images: https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/transform-manipulate-reshape/combine-images-in-photoshop.html (checked 2026-10-28). Sep 28, 2026. Object Selection, masks and compositing workflow.
- Adobe Batch-process files: https://helpx.adobe.com/photoshop/desktop/automate-tasks/process-a-batch-of-files/batch-process-files.html (checked 2026-10-28). Feb 23, 2026. File > Automate > Batch, Actions and source/destination safeguards.
- Adobe keyboard shortcut troubleshooting: https://helpx.adobe.com/photoshop/desktop/troubleshoot/tool-feature-issues/keyboard-shortcuts-not-working.html (checked 2026-10-28). Shortcut conflicts and resets; observed behavior may depend on customization.
- Adobe compare desktop/web functionality: https://helpx.adobe.com/photoshop/web/get-set-up/learn-the-basics/compare-photoshop-web-and-desktop-features.html (checked 2026-10-28). Broad desktop tool family corroboration; web features must not be mistaken for desktop instructions.
- Adobe Photoshop Beta product update: https://community.adobe.com/product-updates (checked 2026-10-28). Oct 15, 2026 modernized toolbar UI explicitly Beta; excluded from stable instructions.
