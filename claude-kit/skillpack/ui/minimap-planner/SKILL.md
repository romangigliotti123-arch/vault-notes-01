---
name: minimap-planner
description: "Decide whether a minimap earns its screen space, then plan the right kind (static map or player-centred radar), its marker budget and rim-clamped objective arrows; includes tested world-to-map maths. Use before adding any minimap or compass."
category: ui
tags: ui, minimap, radar, map, compass, navigation, markers, hud, mobile
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/first-session-onboarding.md
related: hud-layout-planner, billboard-ui-planner, menu-flow-mapper, mobile-ui-audit, accessibility-checker
---

# minimap-planner

Many games do not need a minimap; a good objective marker or landmark does the job at no screen cost. This skill makes that decision explicitly and, if a map is justified, plans it (`scripts/MinimapMath.luau`, Lune-tested).

## When to use
A request for a minimap/compass, or players getting lost. Not for in-world nameplates (`billboard-ui-planner`) or general HUD (`hud-layout-planner`).

## Inputs (max 2)
1. World size and shape (default: read the playable bounds from the map or terrain). 2. What players need to find (objectives, players, shops, danger).

## Procedure
1. Decision test: is the world large or maze-like enough that players cannot orient by landmarks? Do they travel to places they cannot see? If no, use world cues instead (beams, arrows, trails, landmarks - vault) and stop; record "no minimap" with the reason.
2. Choose kind: static full-map image for small authored worlds (open on a button, not always visible); radar (player-centred, range-limited) for open worlds with moving targets; a simple compass strip for linear levels.
3. Space: a minimap costs HUD area; place it in a corner outside control zones and insets (`hud-layout-planner`), around 15-20% of screen height on phones at most (heuristic), tappable to expand.
4. Maths: static: `MinimapMath.fromBounds(pos, bounds, mapPx)`; radar: `radar(pos, centre, yaw, range, mapRadiusPx, rotate)`; objective markers outside range: `clampToRim(point, radius, inset)` so the arrow still points the right way. Rotation (map-up = facing) is easier for navigation but harder for reading terrain: choose per game, offer a setting.
5. Marker budget: `cluttered(count)` above about 12; group, fade or hide low-priority markers; each marker has a shape and an icon, not colour alone.
6. Rendering: ViewportFrame renders are expensive; prefer a pre-rendered image for static maps and cheap Frame/ImageLabel markers updated at a lower rate (e.g. 10 Hz).
7. Test with the smallest phone viewport: markers readable, tap target for expand at least 44 px.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (map bounds) -> `execute_luau` (Edit) to read bounds from a model's bounding box -> `multi_edit` for the map script -> `start_stop_play` -> `screen_capture`. Update cost on devices is `untested`.

## Fallback
Provide the decision record and formulas; owner verifies orientation in play.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (keep the screen clear and design around user flows; mock up before building; keep text/icons legible). `Roblox/roblox-kb/building-and-level-design.md` (landmarks and guidance in the world). `Roblox/roblox-kb/first-session-onboarding.md` (guide with world cues: beams, arrows, trails, landmarks; make the first objective unmissable). Size and rate numbers are heuristics.

## Output
```
MINIMAP DECISION <game>: yes (radar) | no (reason)
size/position, range, rotate?, marker budget N, update rate
formulas used; clutter check
```

## Acceptance checks
- [ ] A reasoned yes/no was recorded before any building.
- [ ] Map position respects insets and control zones.
- [ ] Off-range objectives are rim-clamped; markers have non-colour cues.
- [ ] Lune test passes (`MinimapMath.test.luau`, 5 tests).

## Pitfalls
Adding a map because other games have one. Rotating maps that disorient. Updating every marker every frame. Mixing up Roblox Y-up with map axes (the maths uses X/Z).

## Related
`hud-layout-planner`, `billboard-ui-planner`, `menu-flow-mapper`, `mobile-ui-audit`, `accessibility-checker`.
