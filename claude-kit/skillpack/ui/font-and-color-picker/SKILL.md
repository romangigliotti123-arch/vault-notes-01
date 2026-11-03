---
name: font-and-color-picker
description: "Choose readable Roblox fonts, sizes and a small UI colour system, then verify every text/background pair with a contrast checker (WCAG-style ratios) and set stroke rules for text over busy scenes. Use when starting a UI kit or when text is hard to read."
category: ui
tags: ui, font, color, colour, contrast, palette, typography, legibility, accessibility, theme
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/localization-and-international.md
related: accessibility-checker, ui-kit-consistency-checker, localization-ready-checker, mobile-ui-audit, button-feedback-designer
---

# font-and-color-picker

Pick few fonts, few sizes and a small palette, then prove they are readable. The proof is arithmetic: `scripts/Contrast.luau` computes WCAG 2.x contrast ratios (Lune-tested). WCAG is a general web standard used as a yardstick; Roblox publishes no ratio.

## When to use
Starting a kit, rebranding, or complaints of "can't read it". Not for checking colour blindness (`accessibility-checker`) or consistency of an existing kit (`ui-kit-consistency-checker`).

## Inputs (max 2)
1. The game's mood and audience (default: young, mobile-heavy, bright). 2. Brand colours that must stay (default none).

## Procedure
1. Fonts: one display font for titles, one clean body font; avoid more than two families. Check non-Latin coverage if you will localise (`localization-ready-checker`). Prefer FontFace/Font families that ship with Roblox over unlicensed uploads (`asset-license-checker`).
2. Type scale on a phone: body at least 14 px, important numbers 18-24 px, titles larger (heuristic; `mobile-ui-audit` flags under 14). Use AutomaticSize rather than TextScaled; if scaled, add `UITextSizeConstraint`.
3. Palette tokens: background, surface, text, muted text, primary, danger, success, and one accent; define them once (StyleSheet/tokens or a Lua theme table) rather than per instance (vault). Small palette; do not rely on colour alone.
4. Verify pairs: build a `Pair` for every text/background combination actually used (including text on buttons) and run `Contrast.checkPalette`. Required: 4.5:1 normal text, 3:1 large text (24 px, or 18.66 px bold) and UI components. Fix failures by changing the colour, not by shrinking the requirement. `Contrast.bestText(bg)` picks white or near-black.
5. Text over the 3D world or art: add `UIStroke`/TextStroke and a subtle scrim; test against the lightest and darkest scenes, not one.
6. Export the tokens table and the checked-pairs table; apply to a sample screen and screenshot it on a phone-size viewport.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to read existing `TextColor3`/`BackgroundColor3` pairs (convert with `math.round(c.R*255)`) -> `Contrast.checkPalette` -> property fixes -> `screen_capture`.

## Fallback
Run the pure module with hex values converted by hand; visual judgement stays with the owner.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (keep text legible: contrast, stroke, minimum size and careful TextScaled; do not rely on colour alone and keep the palette small; style with tokens, StyleSheets and tags rather than per-instance overrides). `Roblox/roblox-kb/first-session-onboarding.md` (design clear, consistent UI). `Roblox/roblox-kb/localization-and-international.md` (text length and script changes). Ratios: WCAG 2.x, general standard, not Roblox policy.

## Output
```
UI TYPE+COLOUR <game>   fonts: display X, body Y
tokens: bg #.. surface #.. text #.. ...
contrast: N pairs checked, M failed -> fixes
```

## Acceptance checks
- [ ] Two font families at most; sizes meet the phone minimum.
- [ ] `Contrast.checkPalette` empty for all used pairs.
- [ ] Text over world art has a stroke or scrim and was viewed on light and dark scenes.
- [ ] Tokens defined once and applied (no per-instance colours).
- [ ] Lune test passes (`Contrast.test.luau`, 5 tests).

## Pitfalls
Grey hint text at 3:1. Checking black/white only. Fancy fonts unreadable at 14 px. Status shown by colour only.

## Related
`accessibility-checker`, `ui-kit-consistency-checker`, `localization-ready-checker`, `mobile-ui-audit`.
