---
name: collision-fidelity-tuner
description: "Set CanCollide, CanTouch, CanQuery and CollisionFidelity by what each part is for: turn collision off on decoration nobody scripts, drop Precise collision to Box or Hull, and list invisible walls, without touching anything a script names. Use when collision cost is high or players snag on scenery."
category: build
tags: collision, collisionfidelity, cancollide, cantouch, canquery, hull, box, precise, decoration, physics
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/building-and-level-design.md
related: model-cleaner, anchor-checker, union-fixer, collision-group-setup, game-optimizer
---

# collision-fidelity-tuner

Collision settings are a budget: every part that can collide, fire Touched and answer raycasts costs something. This audits the whole place by purpose and applies two narrow, opt-in fixes. Per-model cleaning is `model-cleaner`; who collides with whom at runtime is `collision-group-setup`.

## When to use
Players catch on grass or trim, a map has many Precise-collision meshes, or `Touched` handlers fire from parts that should be inert. Not for: changing gameplay collision (walls players must hit), or physics groups.

## Inputs (max 2)
1. Scope (Workspace default, or a folder). 2. Target fidelity for Precise meshes: `Hull` (default; cheapest-first order is Box, Hull, Default, Precise) or `Box` for boxy props.

## Procedure
1. Connect (below). Save or confirm version history first.
2. Run `scripts/tune_collision.luau` with both `APPLY_*` flags false. It reads every script source once and lists: decor-looking parts that still collide/touch/query (not named in any script), decor left alone because a script mentions the name, Precise-collision meshes and unions, and invisible collidable parts.
3. If it prints "sources could not be read", script references are unknown: do not apply decor changes; ask the owner to run it from the command bar, or check names by hand with `script_grep`.
4. Review the decor list. Extend `DECOR_WORDS` for the game's own naming (for example `cobweb`). Anything players walk on or click must not be in it.
5. Set `APPLY_DECOR = true` to switch CanCollide, CanTouch and CanQuery off on that list (one undo step). Do not run both flags in the same pass; review in between.
6. For Precise meshes, set `FIDELITY_TARGET` and `APPLY_FIDELITY = true`. Walk the changed objects in Play: stairs, ramps and doorframes are where Hull is too loose.
7. Invisible collidable parts are only reported. Keep real boundary walls; set `CanTouch = false` on them by hand if no script listens.
8. Re-run read-only and report before/after counts from the script output.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/tune_collision.luau` -> `script_grep` for any name you doubt -> flags on -> re-run -> `start_stop_play`, `screen_capture` of stairs/ramps -> `get_console_output`.

## Fallback
Command bar with the script pasted. Without Studio: `.rbxl`/Rojo export gives properties but not script references reliably; produce the list and mark applying `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (use the cheapest collision fidelity; disable collision, touch and query on non-interactive parts), `Roblox/roblox-kb/building-art-and-assets.md` (simple collision on meshes). Fidelity names and behaviour: verify in Creator Docs (`kbq.py docs "CollisionFidelity"`).

## Output
```
COLLISION AUDIT: Workspace parts=5200
decor still colliding 310 -> 0 | precise meshes 42 -> 0 (Hull) | decor skipped (script names it) 6 | invisible collidable 18 (reviewed, kept)
Untested: stair and ramp feel in Play
```

## Acceptance checks
- [ ] The audit ran before and after; counts in the report are copied.
- [ ] No part named in a script source was changed (the script skips them; spot-check three with `script_grep`).
- [ ] Each fidelity change was walked in Play at stairs, ramps and doorways.
- [ ] Both fixes ran as separate undo steps.
- [ ] Invisible walls are listed, not silently changed.

## Pitfalls
Turning CanQuery off on parts that click detectors, tools or raycast-based interaction rely on. Hull on concave shapes (arches, bowls) that players walk through. Parts found by tag or attribute rather than name are invisible to the name test: check `CollectionService` tags first. Dropping collision on a part another script welds to.

## Related
`model-cleaner`, `anchor-checker`, `union-fixer`, `collision-group-setup`, `game-optimizer`.
