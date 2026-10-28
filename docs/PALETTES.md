# Shared color palettes

Three families, each with dark and light variants, keep the choices distinct:

- Ember: warm charcoal, cream and orange; the default dark reading palette.
- Woodland: the supplied #2c3930 / #3f4f44 / #a27b5c / #dcd7c9 reference. Bronze serves as a border; brighter bronze supplies readable dark-mode links. Its light version uses cream and green.
- Ocean: blue-black and pale blue, or a cool light surface with deep blue text.

The other green example was omitted because it overlapped with Woodland. The red/cream/blue example informed the warm light palette and Ocean family; exact swatches were adjusted for text contrast rather than repeated as extra palettes.

The persistent header selector updates open and subsequently opened readers. Existing Photoshop/Premiere theme buttons select the matching light/dark family and synchronize back to the library. Standalone readers retain their toggle. Palette storage is optional, separate from original learning records and backups; blocked storage leaves the current session functional. No OS theme assumption, network request, dependency or server is required.

`assets/palette.js` owns the selection and validates saved IDs. `assets/palette.css` defines semantic tokens and aliases native reader variables, including stronger-contrast preferences. `scripts/palettes.py` generates color-only adapters for literal UI declarations in the original CSS, preserving original files and responsive layout. Changes to source styles regenerate these adapters through `scripts/build.py`. Photoshop and AE inline the styles and script; Premiere loads local assets. Initialization and changes use the existing message bridge, which supports local file URLs without shared-origin assumptions.

Exercise images, app identity marks and SVG fills/strokes retain their source colors. The AE SVG canvas keeps its original light background so its fixed dark labels remain legible. Diagrams are teaching material, not a screen-wide color filter. Print uses light surfaces and dark ink.

Verification: `tests/palette_browser.py` exercises all six palettes in Chromium/Firefox offline, checks 90 semantic text/background pairs at a minimum 4.5:1 contrast, opens all three readers in each palette, checks reader toggles, persistence, standalone operation and narrow layouts. These token checks do not claim every pixel in instructional media has a text contrast guarantee. The ordinary validation, search, Vim navigation and integration regression suites also exercise the changed readers.
