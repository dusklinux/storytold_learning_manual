# Curriculum and dependencies

75 sequential lessons across 12 stages; Photoshop 27.11 (Windows).

Lessons are indexed by stable identifiers. Default prerequisite: immediately prior lesson; earlier skills are explicitly reinforced at stages/projects. The website never locks navigation.

## Stage 1: Orientation & image fundamentals
See files, pixels, resolution and the interface before editing.

- `s01l01` What Photoshop edits: pixels versus vectors (requires none)
- `s01l02` Pixels, dimensions, PPI and print size (requires s01l01)
- `s01l03` Create, open, save and close safely (requires s01l02)
- `s01l04` Interface, panels, workspaces and preferences (requires s01l03)
- `s01l05` Zoom, pan, rulers and guides (requires s01l04)
- `s01l06` History, undo and disciplined experiments (requires s01l05)
**Project:** Pixel field guide — Show 100% and 400% views; correctly distinguish pixel count from print density.

## Stage 2: Documents, layers & geometry
Build safely editable files and navigate space.

- `s02l01` Canvas size, crop and image size (requires s01l06)
- `s02l02` Create, rename, reorder and group layers (requires s02l01)
- `s02l03` Move, align and distribute components (requires s02l02)
- `s02l04` Transparency, alpha and the checkerboard (requires s02l03)
- `s02l05` Layer styles and reusable appearance (requires s02l04)
- `s02l06` Smart Guides, grids and measurement (requires s02l05)
**Project:** Editable six-tile layout — Grid spacing consistent within 4 px; PSD layers remain editable.

## Stage 3: Selections, masks & isolation
Control precisely where changes appear.

- `s03l01` Marquee and lasso: selecting regions (requires s02l06)
- `s03l02` Object Selection, Quick Selection and color range (requires s03l01)
- `s03l03` Layer masks: hiding without deleting (requires s03l02, s02l02, s02l04)
- `s03l04` Select and Mask: refining difficult boundaries (requires s03l03, s03l02)
- `s03l05` Quick Mask, channels and saved selections (requires s03l04)
- `s03l06` Clipping masks versus vector masks (requires s03l05, s02l02, s03l03)
**Project:** Edge isolation studio — Three separately toggled masks; no major hard fringe at 100%.

## Stage 4: Nondestructive editing
Preserve source pixels and remain revision-ready.

- `s04l01` Adjustment layers and scoped corrections (requires s03l06)
- `s04l02` Smart Objects: embedded versus linked (requires s04l01)
- `s04l03` Smart Filters and reversible blur (requires s04l02)
- `s04l04` Blend modes, opacity and fill (requires s04l03)
- `s04l05` Blend If and conditional compositing (requires s04l04)
- `s04l06` Versionable editing and review handoff (requires s04l05)
**Project:** Reversible visual treatment — Each look toggles independently; master pixels untouched.

## Stage 5: Retouching & restoration
Remove distractions and repair images without damaging texture.

- `s05l01` Spot healing versus healing brush (requires s04l06)
- `s05l02` Clone Stamp, Patch and pattern repetition (requires s05l01)
- `s05l03` Remove tool and content-aware corrections (requires s05l02)
- `s05l04` Portrait retouching: texture and restraint (requires s05l03, s03l03, s04l01)
- `s05l05` Dodge and burn for form (requires s05l04, s04l01, s03l03)
- `s05l06` Liquify, perspective and ethical changes (requires s05l05)
- `s05l07` Old photo repair and reconstruction (requires s05l06)
**Project:** Careful restoration — No major repeated textures; source copy preserved.

## Stage 6: Painting & brushes
Understand strokes, color, brush behavior and fills.

- `s06l01` Brush fundamentals: tip, size and hardness (requires s05l07)
- `s06l02` Brush dynamics and tablet pressure (requires s06l01)
- `s06l03` Color picker, swatches and sampling (requires s06l02)
- `s06l04` Gradients, patterns and fill layers (requires s06l03)
- `s06l05` Eraser, history brush and restoration methods (requires s06l04, s03l03)
- `s06l06` Digital painting with layers and value structure (requires s06l05)
**Project:** Limited-palette artwork — Scene reads at 10% view; colors can be recreated from swatches.

## Stage 7: Typography, shapes & paths
Build readable layouts and precise vector-edged components.

- `s07l01` Point type, paragraph type and editable text (requires s06l06)
- `s07l02` Kerning, tracking, leading and hierarchy (requires s07l01)
- `s07l03` Shape tools and vector operations (requires s07l02)
- `s07l04` Pen tool, anchor points and Bézier handles (requires s07l03)
- `s07l05` Text on paths and shape-following type (requires s07l04, s07l01)
- `s07l06` Layout system and reusable mockup (requires s07l05)
**Project:** Typographic poster — Editable live text; consistent 64 px margins; no overflow.

## Stage 8: Photography & color
Make principled tonal, color, RAW and output decisions.

- `s08l01` Histogram, exposure and tonal clipping (requires s07l06)
- `s08l02` Curves and channel-level color balance (requires s08l01)
- `s08l03` White balance, HSL and selective grading (requires s08l02)
- `s08l04` RAW development and Camera Raw Smart Objects (requires s08l03, s04l02)
- `s08l05` RGB, CMYK, Lab, grayscale and bit depth (requires s08l04)
- `s08l06` Soft proofing, gamut and print preparation (requires s08l05)
- `s08l07` Sharpening, noise and HDR discipline (requires s08l06)
**Project:** Color-managed portrait and print proof — No accidental clipping; ICC assumptions documented.

## Stage 9: Advanced compositing
Integrate disparate source elements believably.

- `s09l01` Composite planning: light, camera and scale (requires s08l07, s03l03, s04l02, s08l02)
- `s09l02` Realistic contact and cast shadows (requires s09l01, s04l03)
- `s09l03` Edge integration and local color matching (requires s09l02)
- `s09l04` Depth, atmosphere and selective focus (requires s09l03)
- `s09l05` Displacement and realistic surface mockups (requires s09l04, s04l02, s07l04)
- `s09l06` Frequency separation and advanced retouch judgement (requires s09l05, s05l04, s08l05)
- `s09l07` Blend layers into a high-quality final composite (requires s09l06)
**Project:** Multi-plane photo composite — No floating object; coherent key-light direction and mask boundaries.

## Stage 10: Professional production
Deliver many assets reliably with automation and collaboration.

- `s10l01` Folder structure, asset naming and linked delivery (requires s09l07)
- `s10l02` Actions and batch processing (requires s10l01, s01l03, s02l01)
- `s10l03` Templates and Smart Object replacement (requires s10l02)
- `s10l04` Scripting and supported extensibility boundaries (requires s10l03)
- `s10l05` Export As, Quick Export and format decisions (requires s10l04, s02l04, s08l05)
- `s10l06` Print, preflight and external application handoffs (requires s10l05)
**Project:** Production export bundle — Correct filenames/sizes; zero overwritten sources.

## Stage 11: Performance & troubleshooting
Diagnose failures, bottlenecks and virtualized setups.

- `s11l01` GPU, memory and scratch disk triage (requires s10l06)
- `s11l02` Windows VM graphics and feature limitations (requires s11l01)
- `s11l03` Crashes, resets and safe diagnostics (requires s11l02)
- `s11l04` Missing fonts, links, color shifts and corruption (requires s11l03)
- `s11l05` Large files, cache levels and robust recovery (requires s11l04)
- `s11l06` Offline, account and AI availability (requires s11l05)
**Project:** Technical incident report — Document contains exact observed GPU, vRAM, Photoshop version and unknowns.

## Stage 12: Mastery & capstones
Apply the entire skill system with evidence-based review.

- `s12l01` Portrait retouching capstone (requires s11l06)
- `s12l02` Photo restoration capstone (requires s12l01)
- `s12l03` Product advertisement capstone (requires s12l02)
- `s12l04` Advanced scene-composite capstone (requires s12l03)
- `s12l05` Reusable campaign design capstone (requires s12l04)
- `s12l06` Final assessment: end-to-end editable project (requires s12l05, s09l07, s10l02, s10l05, s11l05)
**Project:** Complete campaign brief — Target 85%+ final rubric; no critical source loss or missing linked assets.

## Cross-stage dependency map

Pixels → dimensions → layers → selections → masks → adjustment layers/Smart Objects → retouch & brush foundations → paths/type → color/RAW → perspective/compositing → output automation → troubleshooting → capstones.

Suggested revision: repeat masking after Stage 5; revisit Smart Filters after Stage 8; do a full export/preflight before Stage 12.
