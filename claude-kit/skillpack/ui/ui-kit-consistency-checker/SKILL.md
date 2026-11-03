---
name: ui-kit-consistency-checker
description: "Scan a Roblox game's UI for inconsistent corner radii, stroke thickness, fonts, text sizes and padding: report the dominant value per property and the rare outliers with paths, then move styling into shared tokens. Use when screens look like they came from different games."
category: ui
tags: ui, consistency, design system, corner radius, stroke, font, padding, tokens, polish, audit
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md
related: font-and-color-picker, mobile-ui-audit, button-feedback-designer, accessibility-checker, ui-scale-fixer
---

# ui-kit-consistency-checker

A consistent kit reads as quality and is faster to change. This skill measures drift: which values the UI mostly uses, and which instances differ. `scripts/ui_scan.luau` collects values from Instances; `scripts/Consistency.luau` is the same rule as a tested pure module (dominant at least 50%, outlier under 15%).

## When to use
After several people or sessions touched the UI, before a polish pass, or before introducing StyleSheets/tokens. Not for sizing problems (`mobile-ui-audit`) or choosing the palette (`font-and-color-picker`).

## Inputs (max 2)
1. Which ScreenGuis (default: all). 2. Properties to check (default: corner radius, stroke thickness, font family, text size, padding).

## Procedure
1. Run `scripts/ui_scan.luau` in Edit mode (StarterGui) and in a Client playtest (PlayerGui, includes runtime UI). Save both outputs.
2. Read the report per property: dominant value and share, then outliers with up to three example paths each. A property with no dominant value (under 50%) means there is no system yet: pick one first (type scale, radius scale) rather than chasing outliers.
3. Classify outliers: intentional (a hero element, a logo) versus drift. Intentional ones get a comment/tag; drift gets fixed to the dominant value.
4. Fix mechanically: set values via `execute_luau`, or better, move the shared values into tokens/StyleSheets and tags so one change updates all (vault: style with tokens, StyleSheets and tags rather than per-instance overrides). Corner radius: set the base `CornerRadius` first, then override per corner only where needed.
5. Re-run the scan; the outlier list should be empty or all marked intentional. Take screenshots of two or three screens side by side.
6. Add a rule to your process: new UI starts from a template instance (restyle templates, do not ship them as-is - vault).

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/ui_scan.luau` -> `start_stop_play` -> `execute_luau` (Client) with the same script -> property fixes via `execute_luau` or `multi_edit` -> re-run -> `screen_capture`.

## Fallback
Paste the script into the command bar; or grep code/Rojo files for `CornerRadius`, `Thickness`, `Font`. Visual claims stay `untested`.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (style with tokens, StyleSheets and tags; set CornerRadius first then override per corner; use strokes sparingly; restyle templates instead of shipping them as-is; design clear, consistent UI per `first-session-onboarding.md`). Thresholds (50% and 15%) are heuristics.

## Output
```
UI CONSISTENCY <game> <date>
property: dominant (share)  outliers: value xN paths...
actions: fixed N, intentional M, token migration plan
```

## Acceptance checks
- [ ] Scan output from Edit and Client runs attached, before and after.
- [ ] Every outlier is fixed or tagged intentional.
- [ ] Shared values live in tokens/styles, not copied per instance.
- [ ] Lune test passes (`Consistency.test.luau`, 5 tests).

## Pitfalls
Fixing outliers when no dominant value exists. Normalising a deliberate hero style. Scanning only StarterGui and missing runtime UI. Counting `TextScaled` labels' TextSize.

## Related
`font-and-color-picker`, `mobile-ui-audit`, `button-feedback-designer`, `accessibility-checker`, `ui-scale-fixer`.
