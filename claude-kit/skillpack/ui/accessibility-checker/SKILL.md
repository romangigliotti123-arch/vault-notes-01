---
name: accessibility-checker
description: "Run an accessibility pass on a Roblox game's UI and effects: colour-blind collisions via simulation, colour-only indicators, text size, contrast hand-off, motion and flashing options, and input alternatives; outputs ranked fixes. Use before launch and after adding colour-coded UI."
category: ui
tags: ui, accessibility, colorblind, colour blind, contrast, motion, flashing, text size, reduced motion, inclusive
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: font-and-color-picker, settings-menu-builder, ui-animation-planner, gamepad-ui-navigator, mobile-ui-audit, damage-number-builder
---

# accessibility-checker

An accessible game is playable by more people, including the many young and mobile players. This pass covers what can be checked by arithmetic (`scripts/Colorblind.luau`, Lune-tested) and by a short manual list. It is a design review, not a compliance certificate.

## When to use
Pre-launch, after adding team/rarity colours, flashing effects or new text. Not for contrast alone (use `font-and-color-picker`) or layout sizes (`mobile-ui-audit`).

## Inputs (max 2)
1. Colour-coded systems (default: teams, rarities, status effects, minimap markers, health bars). 2. Effects that flash or shake (default: hit flashes, screen shake, lightning).

## Procedure
1. Colour-blind simulation: list each set of colours that must be told apart as swatches (0-255 RGB), run `Colorblind.collisions(swatches)`. Each result names the pair and condition (protan, deutan, tritan) where they collapse. The matrices are an approximation (Machado 2009, full severity); the 60-unit distance threshold is a heuristic.
2. Fix collisions by changing lightness or hue and adding a second cue. `Colorblind.colourOnly(indicators)` lists meanings carried by colour alone; each needs an icon, shape, pattern or label (vault: do not rely on colour alone and keep the palette small).
3. Text: minimum sizes per `font-and-color-picker`; offer a large-text option that `AutomaticSize` layouts absorb; contrast pairs checked with `Contrast.checkPalette` (that skill's module).
4. Motion and flashing: provide toggles for screen shake, flashing effects and UI motion (`settings-menu-builder`, `ui-animation-planner` reduced variant); avoid rapid full-screen flashes by default (more than 3 flashes per second is the common photosensitivity guidance - live-check current guidance).
5. Input: all actions possible with touch, pad and keyboard/mouse (`gamepad-ui-navigator`); no required precision-timing hold without an alternative; avoid hover-only information.
6. Audio: important cues have a visual twin (a boss warning has an icon), and volume sliders exist.
7. Report by severity: BLOCKER (core information unreadable or unobtainable), MAJOR, MINOR.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to read `BackgroundColor3`/`Color` of indicator frames and convert to 0-255 -> `Colorblind.collisions` -> fixes -> `start_stop_play` -> `screen_capture`. Colour-blind players' real experience is not simulated by screenshots: a human check is `untested`.

## Fallback
Collect swatches by hand from the design doc and run the module; manual checklist for the rest.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (ship accessibility toggles for motion, flashing and display; do not rely on colour alone and keep the palette small; keep text legible). `Roblox/roblox-kb/cross-platform-and-console.md` (all input types supported; touch first-class). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (audience and content rules around effects, check current rating guidance). Photosensitivity rate and thresholds are general guidance, live-check.

## Output
```
ACCESSIBILITY PASS <game>
colour collisions: pair/kind/dist -> fix     colour-only: names -> second cue
toggles: shake, flashing, motion, text size   findings: BLOCKER/MAJOR/MINOR
```

## Acceptance checks
- [ ] `Colorblind.collisions` output attached for every colour-coded set.
- [ ] Each colour-only indicator has a second cue or a ticket.
- [ ] Motion/flash toggles exist and are consumed.
- [ ] Limits of the simulation are stated in the report.
- [ ] Lune test passes (`Colorblind.test.luau`, 5 tests).

## Pitfalls
Red/green teams with no label. Treating the simulation as medical truth. Toggles that are saved but ignored. Flashing hit effects stacked by many players.

## Related
`font-and-color-picker`, `settings-menu-builder`, `ui-animation-planner`, `gamepad-ui-navigator`, `mobile-ui-audit`.
