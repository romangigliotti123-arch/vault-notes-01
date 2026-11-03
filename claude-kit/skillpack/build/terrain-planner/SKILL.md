---
name: terrain-planner
description: "Plan terrain before sculpting: map size in 4-stud voxels and heightmap pixels, tile splits for big maps, work order, water and hollowing rules, and a read-only audit of what the place already has. Use when starting a map, importing a heightmap, or when terrain is heavy or boxy."
category: build
tags: terrain, heightmap, voxel, water, hollow, sculpt, island, map, region, streaming
kb: Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md
related: graybox-builder, lod-planner, lighting-preset-picker, prop-set-planner, game-optimizer
---

# terrain-planner

Terrain is efficient when it is planned: aligned to the voxel grid, hollowed, and only as big as the game needs. The vault gives hard numbers for heightmaps and voxels; this turns them into a plan and checks the place against it.

## When to use
Starting a map, importing a heightmap, a map that feels boxy, terrain with excess memory or physics cost, or a huge map that needs tiles. Not for: the level's layout and pacing (`level-flow-planner`, `graybox-builder`), or sky and fog (`lighting-preset-picker`).

## Inputs (max 2)
1. Map size in studs (width x depth) and rough height range. 2. Features: water, roads or plazas, a hard boundary or an island edge (default: land only).

## Procedure
1. Fix the design first (genre, theme, map shape, player count); sketch the layout with 1-3 simple shapes. Terrain follows the plan, not the other way round.
2. Snap sizes to the 4-stud voxel grid and compute the heightmap: `TerrainPlan.heightmap(widthStuds, depthStuds)` in `scripts/TerrainPlan.luau` (Lune-tested). One pixel is one 4-stud voxel; images are .png or .jpg of at most 4096 x 4096 px, so one image spans about 16384 studs. Bigger maps get tiles; the plan lists each tile's size.
3. If the map is more than a few thousand studs wide, ask whether it needs to be: the vault favours compact hubs and bottlenecks and gives low-end mobile a budget of tens of thousands of parts per area.
4. Get the work order from `TerrainPlan.order(hasWater, hasRoads)`: bounds and grid, base land from top-down, rounded and varied edges, water and island edge, hollow or delete hidden terrain, flatten corridors, materials last and few.
5. Sculpt in Studio's Terrain Editor (owner action) or import the heightmap; round off boxy shapes, vary sizes, use curves and jogs.
6. Audit with `scripts/terrain_audit.luau`: used extent in studs and its heightmap equivalent, water properties, decoration, streaming settings, and ground-sized flat parts that terrain would replace.
7. Hollow with Subtract and delete terrain under surfaces nobody sees (vault: the hollow tool alone can leave excess detail, 3 MB voxels and 5 MB physics in one test). Re-audit and compare with the Developer Console memory view on a device.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/terrain_audit.luau` -> `screen_capture` from top-down and at player height -> owner sculpts with Terrain Editor tools (no safe scripted equivalent for design work) -> re-audit.

## Fallback
Without Studio, the plan (sizes, tiles, order) works from numbers alone; the audit and sculpting are `untested`. For a heightmap, an image editor producing a grayscale .png at the planned pixel size is enough.

## Evidence
`Roblox/roblox-kb/building-and-level-design.md` (heightmaps .jpg/.png at most 4096 x 4096, 1 px = 4 studs; voxels 4x4x4 studs; sculpt from top-down and fill water; round and vary terrain; build in stages: terrain, zones and roads, buildings, props), `Roblox/roblox-kb/optimization-and-streaming.md` (terrain: hollow and flatten; delete what is hidden), `Roblox/roblox-kb/building-art-and-assets.md`. Heightmap height scaling: live-check in Creator Docs.

## Output
```
TERRAIN PLAN: 8000 x 6000 studs -> heightmap 2000 x 1500 px (single image)
Order: bounds+grid, base land, round edges, water, hollow, flatten roads, materials
Audit: extent 7996 x 168 x 5996 studs; ground-sized parts 4 (candidates for terrain)
```

## Acceptance checks
- [ ] Sizes in the plan are multiples of 4 and the pixel maths comes from the module (7 Lune tests).
- [ ] Tiles are listed when either side exceeds 4096 px.
- [ ] The audit ran and its figures are quoted.
- [ ] Hidden terrain was removed or the reason it was kept is stated.
- [ ] Device memory was checked after sculpting, or marked untested.

## Pitfalls
Sculpting before the layout is approved. Hollow-only cleanups. Exporting terrain to meshes (the vault calls terrain efficient: do not). Spawning NPCs on terrain that has not streamed in.

## Related
`graybox-builder`, `lod-planner`, `lighting-preset-picker`, `prop-set-planner`, `game-optimizer`.
