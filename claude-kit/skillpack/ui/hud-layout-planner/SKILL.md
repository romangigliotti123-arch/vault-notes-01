---
name: hud-layout-planner
description: "Plan a Roblox HUD that shows only what the core loop needs, keeps it out of the phone's thumb zones and safe insets, and reveals the rest with progression; output is an element list with rects and a tested overlap/safe-area report. Use before building or when the HUD feels crowded."
category: ui
tags: ui, hud, layout, mobile, thumb zone, safe area, progression, clutter, wireframe
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/first-session-onboarding.md
related: mobile-ui-audit, safe-area-checker, ui-scale-fixer, currency-display-designer, minimap-planner, first-minute-designer, menu-flow-mapper
---

# hud-layout-planner

A HUD is the always-on screen layer. Every element costs view area and attention, and on a phone the thumbs already own the bottom corners. This skill decides what earns a place, where it sits, and when it appears.

## When to use
New game or new HUD element; reviews say "too much on screen" or "buttons hidden"; before `mobile-ui-audit`. Not for menus you open (`menu-flow-mapper`, `shop-ui-planner`), for currency widget internals (`currency-display-designer`), or for the minimap decision (`minimap-planner`).

## Inputs (max 2)
1. The core loop in one sentence and the list of numbers/buttons the player reads or presses during it (default: ask `core-loop-designer` output or the current HUD from the game tree). 2. Target devices (default: phone landscape first, then tablet and desktop).

## Procedure
1. List every candidate element. Tag each priority: `core` (needed every few seconds), `situational` (needed in some moments), `optional` (nice to have). Stop condition: nothing untagged.
2. Cut: anything `optional` that the loop does not need leaves the HUD (it can live in a menu). Gate the rest by progression with `unlockLevel` (vault: gate features and UI behind progression; teach one mechanic at a time).
3. Place elements as Scale rects (0..1). Rules from the vault: keep the screen clear, tuck HUD to device insets, keep custom mobile UI out of the default control zones, pin to edges with AnchorPoint. Put read-only status top-centre or top-right, repeated actions bottom-centre-ish between the thumb zones, never over the character.
4. Run `scripts/HudLayout.luau` logic (`HudLayout.check`) with the real insets and the real default control zones read from the emulator (the built-in zone defaults are illustrative). Stop condition: zero `outside-safe-area`, `in-control-zone`, `overlap`; `too-much-screen` cleared or accepted with a reason.
5. Check each `visibleAt(level)` stage, not just the final HUD: the first-minute HUD should show 2-4 elements.
6. Build in grayscale blocks first (vault: wireframe before art), one `ScreenGui`, `ResetOnSpawn = false`, mobile controls untouched in their own space.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (StarterGui) -> `inspect_instance` on each HUD frame -> `execute_luau` to read `AbsolutePosition/AbsoluteSize` in a Client playtest (`start_stop_play`) and convert to Scale rects -> `HudLayout.check` -> `screen_capture` per emulated device (owner switches the Device Emulator).

## Fallback
Plan on paper as a table (element, priority, rect, unlock). Run the Lune test file's pattern with your rects. Without Studio, everything visual is `untested`.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (keep the screen clear and design around flows; tuck HUD to insets; keep custom mobile UI out of default control zones; reserve space for touch controls). `Roblox/roblox-kb/cross-platform-and-console.md` (design mobile-first: most Roblox sessions are on mobile, multiple creators plus official docs; isolate mobile controls in their own ScreenGui). `Roblox/roblox-kb/first-session-onboarding.md` (gate UI behind progression; clear goals and next steps). The 25% coverage cap and zone sizes are heuristics.

## Output
```
HUD PLAN <game>   devices: phone landscape, tablet, desktop
element | priority | rect (x,y,w,h scale) | unlock
...
check: 0 issues | N issues -> list     first-minute elements: N
```

## Acceptance checks
- [ ] `HudLayout.check` run on the final rects with real insets; output attached.
- [ ] Every element has a priority and a reason to exist; optional ones are cut or gated.
- [ ] First-minute HUD (level 1) shows no more than 4 elements.
- [ ] Nothing important sits in a control zone or under an inset.
- [ ] Lune test passes (`HudLayout.test.luau`, 6 tests).

## Pitfalls
Showing every stat from minute one. Designing on a 16:9 desktop view and discovering the thumb zones later. Trusting the default zone numbers instead of the emulator. Covering the character with a top-heavy HUD.

## Related
`mobile-ui-audit`, `safe-area-checker`, `ui-scale-fixer`, `currency-display-designer`, `minimap-planner`, `first-minute-designer`.
