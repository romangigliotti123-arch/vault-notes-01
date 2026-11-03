---
name: graybox-builder
description: "Validate a block-out spec (4-stud grid, overlaps, doorway and corridor clearance from the 6.5-stud avatar), build it as plain grey anchored boxes in one undo step, and run a playtest checklist on the layout before any art is made. Use when starting a level, obby or arena and the layout must be proven first."
category: build
tags: graybox, greybox, blockout, layout, level, playtest, prototype, grid, scale, avatar
kb: Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/development-process-and-speed.md
related: level-flow-planner, terrain-planner, art-bible-writer, prop-set-planner, mvp-definer
---

# graybox-builder

Block the map with plain parts first and playtest it; add art only when the layout works in code and is fun. That keeps changes cheap. This turns an approved sketch into validated boxes and gives the playtest a checklist, so the test is about the layout and not about typos in the build.

## When to use
Starting any new area; before paying for or making art; when a layout "feels wrong" and you need a fast variant. Not for: pacing and landmark design (`level-flow-planner`), terrain (`terrain-planner`), or finished art.

## Inputs (max 2)
1. The layout: rooms, corridors, platforms with sizes (a sketch or a list). 2. Player count and the verbs the area must support (run, jump, shoot, trade); default: one player, run and jump.

## Procedure
1. Decide before opening Studio: genre, theme, player count, map shape; draw the layout using 1-3 basic shapes (square, rectangle, octagon).
2. Write the spec as boxes: name, centre x,y,z, size sx,sy,sz, role (`floor`, `wall`, `door`, `corridor`, `platform`, `cover`, `spawn`). Put it in `SPEC` in `scripts/build_graybox.luau`. Keep sizes multiples of 4 and corners on the grid so terrain and parts align.
3. Validate (build off): the checks are `scripts/Graybox.luau` (Lune-tested) and the same logic inlined in the Studio script: grid alignment, overlaps (mark intended ones `allowOverlap`), duplicate names, doors at least 8.2 studs high and 4 wide (1.25 x the 6.5-stud avatar), corridors at least 8 wide. Fix every issue; the build refuses while any remain.
4. Build with `BUILD = true`: creates `Workspace.Graybox` (Folder), parts anchored, SmoothPlastic, colour by role, in one undo step. `REPLACE = true` rebuilds an existing one.
5. Add spawns, one test objective and a way back; nothing else (no props, no textures).
6. Playtest with the checklist below (`start_stop_play`; humans for feel). Record findings against box names.
7. Change the spec, rebuild, retest. When two consecutive passes find no layout problems, freeze the layout and hand off to art.

Playtest checklist: can a new player see the goal in 10 seconds; are there 2-3 entry points per enterable building; are there dead ends as risk/reward spots; are sight lines and engagement distances what the mode needs; do spawns sit at fair distances (equidistant from centre for teams); are jumps reachable at the avatar's real jump height; can anyone get out of bounds; is cover distributed; does the route read without signs.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/build_graybox.luau` (validate, then `BUILD = true`) -> `start_stop_play` -> `screen_capture` from the player camera and top-down -> `get_console_output`.

## Fallback
Build by hand with Studio's part tools using the validated spec as the list; the script's validation still works as a pre-check under Lune. Feel and flow need human players: `untested` until played.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (graybox before adding art; pipeline concept, graybox, art build, finished map), `Roblox/roblox-kb/building-and-level-design.md` (greybox before art and keep sight-line intent; build in stages with a time box; 2-3 entry points; spawns at opposite ends; scale against the 6.5-stud avatar; invisible walls at edges), `Roblox/roblox-kb/playtesting-and-feedback.md`. Clearance multipliers are this skill's defaults.

## Output
```
GRAYBOX: 24 boxes, 0 issues -> Workspace.Graybox (one undo step)
Playtest pass 1: findings by box name; changes made; pass 2 result
Layout frozen: yes/no   Untested: multiplayer sight lines
```

## Acceptance checks
- [ ] Validation passed (zero issues) before the build ran.
- [ ] Every box is anchored and named; the folder is Workspace.Graybox.
- [ ] A Play pass happened and findings are tied to box names.
- [ ] Doorway and corridor sizes were checked against the avatar, not by eye.
- [ ] No art, textures or props were added at this stage.

## Pitfalls
Polishing the graybox. Rotated geometry in a spec that only supports axis-aligned boxes. Testing alone when the mode is multiplayer. Making doors the exact avatar size (players snag). Skipping the out-of-bounds check. Treating the first layout as final.

## Related
`level-flow-planner`, `terrain-planner`, `art-bible-writer`, `prop-set-planner`, `mvp-definer`.
