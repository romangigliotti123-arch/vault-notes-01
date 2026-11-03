---
name: damage-number-builder
description: "Build readable, cheap floating damage and reward numbers: merge rapid hits, spread simultaneous numbers into lanes, cap the live count, expire by age, and render with a pooled label set. Use when combat or reward popups overlap, lag or are unreadable."
category: ui
tags: ui, damage numbers, floating text, popup, combat feedback, pooling, billboard, performance, juice
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/cross-platform-and-console.md
related: object-pool-builder, billboard-ui-planner, ui-animation-planner, notification-system-planner, accessibility-checker, currency-display-designer
---

# damage-number-builder

Numbers confirm hits and rewards, but a flood of unmerged, uncapped, per-hit GUIs costs frames and hides the action. The bookkeeping (`scripts/FloatingNumbers.luau`, Lune-tested) decides what to show; the pack's `object-pool-builder` supplies reusable label frames; this skill is the glue.

## When to use
Combat popups, loot/XP gains, heal numbers. Not for toasts (`notification-system-planner`) or nameplates (`billboard-ui-planner`).

## Inputs (max 2)
1. Number kinds (default: damage, crit, heal, reward). 2. Hit rate extremes (default: up to 20 hits per second on one target).

## Procedure
1. Server decides the amounts; it tells nearby clients (or the attacker) with a lightweight event carrying target id, amount, kind, crit flag. Clients never invent amounts. Rate-limit and range-limit the event.
2. Client: `FloatingNumbers.new({ mergeWindow = 0.25, maxActive = 24, lifetime = 0.9, lanes = 3 })` (heuristics; tune on a phone). `spawn(target, amount, kind, now, crit)` returns the number and whether it merged; merged numbers update the existing label's text.
3. Rendering: one pooled label per active number (`Pool` from `object-pool-builder`: acquire on new, release on expiry; reset text, size, transparency, position). Parent to a single `BillboardGui` per target or one overlay `ScreenGui` with world-to-screen positions; prefer the overlay for many targets.
4. Motion: lane offset `laneOffset(lane, 24)` horizontally, rise and fade by `progress(n, now)` (feedback/reward roles from `ui-animation-planner`). Crits are bigger and a distinct shape/colour plus "!" or icon, not colour alone.
5. Legibility: stroke or shadow, minimum 18 px on phones, contrast against bright scenes (`font-and-color-picker`), no numbers on far targets (distance cull via `billboard-ui-planner`).
6. Options: respect reduced motion (no rise, fade only) and offer "numbers off/compact" in settings.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `multi_edit` (FloatingNumbers + pool wiring) -> `start_stop_play` -> `execute_luau` (Client) to spawn 100 hits quickly -> `get_console_output` -> `screen_capture`. Frame-time impact needs the MicroProfiler on a phone: `untested`.

## Fallback
Provide the module and the pool wiring; run Lune for bookkeeping proof.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (build diegetic and in-world UI on parts with Adornee; tween rules; keep text legible; fade groups with CanvasGroup). `Roblox/roblox-kb/first-session-onboarding.md` (immediate feedback for every action; early rewards). `Roblox/roblox-kb/cross-platform-and-console.md` (test on a low-end Android before launch - indie advice). Caps and windows are heuristics.

## Output
```
DAMAGE NUMBERS <game>  merge 0.25 s, cap 24, life 0.9 s, lanes 3
render: pooled labels (Pool max 24)   settings: compact/off, reduced motion
stress: 100 hits -> max live 24
```

## Acceptance checks
- [ ] Amounts originate on the server; event is rate-limited.
- [ ] Live count never exceeds the cap in the stress run.
- [ ] Labels are pooled and fully reset on release.
- [ ] Crit is distinguishable without colour.
- [ ] Lune test passes (`FloatingNumbers.test.luau`, 6 tests).

## Pitfalls
Instancing a new BillboardGui per hit. Stale text on reused labels. Numbers stacking at one point. Showing numbers for off-screen or distant targets.

## Related
`object-pool-builder`, `billboard-ui-planner`, `ui-animation-planner`, `notification-system-planner`, `accessibility-checker`.
