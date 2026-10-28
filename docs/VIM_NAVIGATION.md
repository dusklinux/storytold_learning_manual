# Optional Vim navigation

Vim keys are off by default. Use the visible **Vim keys** button or **Alt+M** to toggle them. The preference is saved in this browser when local storage is available, and shared with the three embedded readers. It is a reader preference, separate from learning-progress backups. Alt+M deliberately works while typing so the mode is always easy to disable.

The interaction borrows the supplied clipboard manager’s explicit mode toggle, `j/k`, single `g`/`G`, and separation of search typing from navigation. The clipboard script itself was only read and was not changed or executed. No shell/fzf code is run by the manual.

| Key, while Vim mode is on | Action |
|---|---|
| `j` / `k` | Move down/up through visible shared-search results; otherwise scroll the current page |
| `g` / `G` | First/last visible result; otherwise top/bottom of the current page |
| `/` | Focus shared search in the library/embedded readers; standalone readers focus their own search |
| Escape in the shared search input | Leave typing, retaining the query; focus the first result (or the page if empty) |
| Enter on a result | Open it using the ordinary link behavior |
| Alt+M | Toggle Vim keys |

Typing in inputs, notes, dropdowns, contenteditable areas and textbox controls retains ordinary letter keys. IME composition and modified keys are left alone. Native Tab/Enter, existing arrow navigation, Ctrl+K, printing and app-specific controls remain available. The mode does not implement text editing, selection operators, terminal quitting or browser history shortcuts. In particular, `q` and Ctrl+D/U were not borrowed because their terminal meanings do not fit the browser reliably.

`assets/vim.js` holds the shared implementation. The self-contained Photoshop/AE readers embed it at build time, while the library and Premiere load the adjacent local file. It uses the existing parent/reader message bridge to synchronize mode changes without relying on local-file shared origins. No additional runtime package, local service, internet request or learning-content change is required.

Verification: real offline Chromium and Firefox tests cover default-off behavior, Alt+M, shared search selection, query retention, typing and dropdown preservation, scrolling in all three readers, `/` handoff, persisted mode, and 320/768 px layouts. Core structural/source/export checks and existing fuzzy-search browser checks are also run. These tests validate browser-reader navigation, not Adobe application keybindings; keys apply only when the browser has focus.
