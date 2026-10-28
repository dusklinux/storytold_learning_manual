# Comparative audit against the supplied After Effects project

**Date:** October 28, 2026. **Premiere release target:** Windows 26.5.2. **Reference:** user-supplied `ae_manual-main(1).zip`, examined locally for educational and software design, not as an authority about Premiere.

## Decision

The Premiere manual was already stronger at *granular linear sequencing*: 14 stages and 105 lessons, compared with the supplied After Effects manual's six stages and 40 walkthrough lessons plus 100 explanatory topics. A wholesale conversion to the AE course architecture would disrupt useful Premiere prerequisites, make prior saved progress unreliable, and bring no clear educational benefit. **The existing Premiere lesson IDs, stages, quizzes, and v1 study-progress schema were retained.** No AE editing instructions, key assignments, effects or app terminology were copied into the Premiere curriculum.

The AE repository nevertheless demonstrated stronger **exact-result navigation, reading accessibility, rigorous progress import validation, structured technical/reference depth, file integrity verification, and real browser regression design**. Those generic design ideas were adapted and independently implemented for the Premiere site.

## Applied changes and rationale

| Observed reference pattern | Premiere action | Why it matters |
|---|---|---|
| Search navigates to individual catalog items instead of dumping users at the top of a reference table | Added direct links to individual Premiere shortcuts, effects, transitions, glossary terms and panels; the target is isolated and focusable | An editing-time search now yields the actual answer |
| Larger text, high contrast and one-at-a-time lessons | Added reading-settings page and print-safe, single-step exercise mode | Better readability, especially across host/VM desktops and smaller screens |
| Strict study-progress input normalization | Added exact valid lesson, quiz, step and bookmark keys; bounded note lengths; type and range checks; rejected imports never mutate state | Protects personal study history from broken exported data and accidental wrong imports |
| Corrupt stored progress handled separately from blocked storage | Treat malformed saved records as invalid but keep working persistence when the browser permits it | Correct recovery path without falsely telling the learner storage is unavailable |
| Strong topical glossary and symptom-first diagnostic catalog | Curated 48 additional Premiere glossary terms, 17 more troubleshooting cases and 10 extended recipes, with lesson links | Broader practical reference rather than raw lesson count inflation |
| Manifest and deterministic archive build | Added `MANIFEST.sha256`, package/verification scripts and extraction integrity checks | Verifiable handoff and repeatable packaging |
| Adversarial, route-complete browser regression | Added a Playwright/Chromium test covering all 749 lesson/reference/routes, backward-compatible progress and corrupt/blocked storage behavior | Catches faults that counting files or links alone cannot |

## Consciously not copied

- The After Effects feature/shortcut/effect catalog: these are different Windows applications, so similar names do not establish Premiere behaviors.
- AE's single `index.html` embedded-data format: Premiere's local `data.js` / `guides.js` architecture already supports ordinary `file://`-compatible scripts and more maintainable split source files; changing it would create an unnecessary regression risk.
- AE-specific numeric frame-rate lab or animation diagrams: Premiere already has editing-geometry diagrams and technical exercises matched to its learning sequence.
- AE's 25.6-to-26.5 migration rules: those step identifiers and reset rules cannot be applied to Premiere. Premiere's existing exports remain accepted by the stricter compatible validator.
- The AE manual's 300 effects or 386 shortcuts **as quotas**: Premiere catalogs must list accurately supported Premiere commands, not be padded to match another application's counts.

## Verification scope and residual risk

- Adobe's official desktop release notes (October 5, 2026) confirm 26.5.2 as the current documented patch on the research date. The release target is not inferred from the AE archive.
- The added glossary, recipes and diagnostics were independently written for Premiere. Automated tests can confirm their format and internal links, not every practical outcome on all hardware or footage.
- Exact catalog targets are generated from compound entry keys rather than ordinal indexes, so reordering CSV records does not break their current URLs. Renaming catalog entries can still invalidate previously copied deep links; a permanent explicit ID would be preferable for multi-year maintenance.
- Direct `file://` browser navigation remains **untested in this environment** because its browser sandbox rejects file-URL navigation. Chromium tests instead use a DOM with the exact published CSS/JavaScript/data inlined; they validate frontend behavior but are not a real Linux/Windows desktop file-URL certification.
- We have not launched licensed Windows Premiere 26.5.2, verified every keyboard assignment against an actual installation, exhaustively checked all effects at parameter level or tested every export codec in a supported VM. Adobe documentation and the existing status caveats remain the basis for those items.
- Additional technical encyclopedias in the After Effects project suggest potential future depth, but adding unverified Premiere rows merely to increase counts would undermine this manual's accuracy.

## Practical green-light criterion

This edition is fit for learning from the generated offline course and for using its reference **with the documented release and verification caveats**. It cannot honestly be called perfect or completely certified until a real Windows Premiere pass and unrestricted `file://` cross-platform smoke test are performed.
