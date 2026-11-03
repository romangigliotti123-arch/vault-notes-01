---
name: palette-picker
description: "Pick and verify a game colour palette: roles, contrast ratios for text, distinctness under protanopia, deuteranopia and tritanopia, and brightness separation in monochrome, with a tested checker that names every failing pair and a fix for each. Use when choosing colours for a world or UI, or when teams or hazards might be indistinguishable."
category: build
tags: palette, colour, color, contrast, wcag, colorblind, accessibility, grayscale, ui, team colours
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md
related: art-bible-writer, material-consistency-checker, lighting-preset-picker, mobile-ui-audit, thumbnail-maker
---

# palette-picker

Colour choices fail in three predictable ways: text that cannot be read, two colours that look the same to colour-blind players, and two colours with the same brightness that vanish in monochrome. All three can be measured. `scripts/Palette.luau` does WCAG contrast, Machado colour-blind simulation (protan, deutan, tritan) and a grayscale gap test, with seven Lune tests.

## When to use
Choosing a world or UI palette, picking team or rarity colours, auditing a UI that "looks muddy", before locking an art bible. Not for: auditing what colours a place already uses (`material-consistency-checker`), or lighting mood (`lighting-preset-picker`).

## Inputs (max 2)
1. A starting hue or reference (or "propose one"), and the roles needed (ground, structure, accent, hazard, UI background, UI text, team A, team B). 2. Which pairs must stay distinct and which pairs carry text (default: every pair distinct; text on its background).

## Procedure
1. Choose 5-8 colours with roles; keep the palette small (tweak shades rather than abandon it when a check fails).
2. Put them in a Lune runner (a throwaway file beside the module): `local P = require("./Palette")`, then `P.check(entries, { pairs = {...}, textPairs = { {"uiText","uiBg"} } })`. Entries are `{ name, hex }`. Bad hex strings come back in the second return value, not as errors.
3. Read the issues: `contrast` (value is the ratio; below 4.5 for normal text, 3 acceptable for large text and UI shapes), `deuteranopia`/`protanopia`/`tritanopia` (the pair is distinct normally but confusable under that type; value is the CIE76 colour difference after simulation, flagged under 12), `gray` (brightness gap under 25 of 255).
4. Fix by changing lightness first (it solves contrast and gray together), then hue. For team colours: pair each colour with a symbol or icon, never colour alone. White text on yellow is a classic failure.
5. Re-run until clean. Keep the final hex list with roles and the check result.
6. Optionally view the result: set the colours on swatch parts or a UI mock in Studio (`execute_luau`) and `screen_capture` it; also view it in monochrome by eye (vault check) to catch what the metrics miss.
7. Hand the palette to `art-bible-writer`; apply to the place as a separate, reviewed change.

## Studio MCP path
Not required. Optional: `list_roblox_studios` -> `execute_luau` (Edit) to place swatches -> `screen_capture`. Colours are applied with `Color3.fromHex` or `Color3.fromRGB`.

## Fallback
Entirely offline under Lune. Simulation is a screening aid, not a diagnosis; real colour-blind review is `untested`.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (use WCAG-based contrast checked with a calculator, avoid white text on yellow, tweak shades rather than abandon the palette; view UI in monochrome; never convey meaning by colour alone, pair colour with symbols; scale contrast requirements to font size), `Roblox/roblox-kb/ui-ux-design.md`. The 12 and 25 thresholds are this skill's defaults; the simulation matrices are from the published Machado et al. 2009 method.

## Output
```
PALETTE: 7 colours, 9 pairs checked
[contrast] uiText / uiAccent 3.1 (< 4.5)   [deuteranopia] teamA / teamB dE 8.4   [gray] hazard / ground 18
Fixes: darken uiAccent 15%; add shield and sword icons to teams; raise hazard lightness
Final: ground #..., structure #..., accent #...
```

## Acceptance checks
- [ ] The checker ran on the final palette with zero issues (output quoted), or each remaining issue is justified.
- [ ] Text pairs were listed explicitly and pass 4.5 (or 3 for large text).
- [ ] Team/rarity colours have a non-colour cue.
- [ ] The palette was viewed in monochrome.
- [ ] Hex values and roles are recorded.

## Pitfalls
Judging colours on one monitor. Trusting simulation as medical truth. Passing contrast but failing brightness separation. Applying the palette over lighting that tints everything (check in the lit scene). Bright saturated palettes on neon/bloom lighting. Checking only pairs you chose, not adjacent surfaces.

## Related
`art-bible-writer`, `material-consistency-checker`, `lighting-preset-picker`, `mobile-ui-audit`, `thumbnail-maker`.
