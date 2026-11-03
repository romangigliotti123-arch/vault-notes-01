---
name: billboard-ui-planner
description: "Plan in-world nameplates, health bars and prompts on BillboardGui: distance fade, a visible-count cap with hysteresis, enable-only-changes updates and a cost budget so many players do not tank frame rate. Use when overhead UI flickers, clutters or lags."
category: ui
tags: ui, billboardgui, nameplate, overhead, health bar, distance fade, performance, in-world ui, proximity prompt
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/building-and-level-design.md
related: damage-number-builder, minimap-planner, hud-layout-planner, object-pool-builder, game-optimizer, accessibility-checker
---

# billboard-ui-planner

Overhead UI is diegetic and readable, but every BillboardGui is a render and update cost, and fifty of them is a wall of text. The selection and fade maths is `scripts/BillboardFade.luau` (Lune-tested).

## When to use
Nameplates, health bars over enemies, NPC prompts, shop signs. Not for screen-space HUD (`hud-layout-planner`) or floating combat numbers (`damage-number-builder`).

## Inputs (max 2)
1. What appears overhead (default: name, health bar, interaction hint). 2. Peak population in view (default: 30 players or NPCs).

## Procedure
1. Decide per element: always (own party only), near (within range), or on-demand (shows when looked at or prompt-triggered). Use `ProximityPrompt` for interactions instead of custom billboards where it fits (vault: build diegetic UI on parts with Adornee and proximity prompts).
2. Ranges: fade start/end and a hard max (`BillboardGui.MaxDistance` is a built-in cull; keep it close to the fade end). `BillboardFade.transparency(distance, fadeStart, fadeEnd)` drives the fade (use a CanvasGroup `GroupTransparency` so children fade together).
3. Count cap: each update gather candidates (id, distance, priority) and call `BillboardFade.select(candidates, { maxCount, maxDistance, previous, slack })`; party members and quest NPCs get priority. Hysteresis (`slack` about 3 studs) stops flicker between near-equal candidates.
4. Apply changes only: `BillboardFade.changes(previous, current)` lists ids to enable/disable; touch no other Instances. Update at 5-10 Hz, not every frame.
5. Size: use `Size` in Scale/pixels with `SizeOffset`/`StudsOffset` above the head, `AlwaysOnTop` only when needed (it draws through walls); keep text 14 px+ at the near range on phones; set `LightInfluence` for readability in the dark.
6. Health bars: drive with a clamped scale ratio; avoid per-frame tweens, tween on change.
7. Privacy/safety: nameplate text must come from the filtered display name, never raw user text.
8. Measure: with 30+ targets compare frame time and memory before/after (`game-optimizer`).

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `multi_edit` for the manager script -> `start_stop_play` -> `execute_luau` (Client) to spawn dummy targets at varied distances -> `get_console_output` -> `screen_capture`. Frame-time effect is `untested` without the MicroProfiler on target devices.

## Fallback
Deliver the manager module and settings; owner profiles in a populated server.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (build diegetic and in-world UI on parts, with Adornee and proximity prompts; drive bars with a clamped scale ratio; fade groups with CanvasGroup). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first; low-end Android testing is indie advice). `Roblox/roblox-kb/building-and-level-design.md` (in-world guidance). Ranges and rates are heuristics, not engine limits.

## Output
```
BILLBOARD PLAN <game>   elements: ...   fade: A-B studs   cap: N   rate: 10 Hz
selection: nearest + priority, hysteresis 3 studs     measured: frame time before -> after
```

## Acceptance checks
- [ ] Visible billboards never exceed the cap in the stress scene.
- [ ] No flicker when two targets swap rank (hysteresis tested).
- [ ] Only changed ids are toggled per update.
- [ ] Text comes from filtered names.
- [ ] Lune test passes (`BillboardFade.test.luau`, 5 tests).

## Pitfalls
A BillboardGui per hit or per NPC regardless of distance. `AlwaysOnTop` everywhere. Per-frame tweens on health bars. Updating every billboard every frame.

## Related
`damage-number-builder`, `minimap-planner`, `hud-layout-planner`, `object-pool-builder`, `game-optimizer`.
