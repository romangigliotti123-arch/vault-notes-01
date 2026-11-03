---
name: part-count-auditor
description: "Count parts, meshes, unions and partially transparent parts per map region and per 3x3 neighbourhood, compare them with a visible-parts, draw-call and triangle budget, and produce a ranked list of the regions to cut. Use when a particular area drops frame rate or before locking a level's content."
category: perf
tags: part count, draw calls, triangles, budget, region, overdraw, unions, meshparts, scene stats, instances
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/building-and-level-design.md
related: game-optimizer, render-cost-auditor, model-cleaner, lod-planner, streaming-enabler, cpu-vs-gpu-diagnoser
---

# part-count-auditor

Total part count is a poor number; what a player SEES at once is the one that hurts. This skill buckets parts into grid cells, sums each cell with its neighbours, and ranks the worst views against a budget, so the cuts go where players actually stand.

## When to use
One area is slower than the rest, a level is nearly finished, or the render prep (blue bars) dominates a MicroProfiler frame. Not for: lights, particles and shadows (`render-cost-auditor`), physics (`physics-load-reducer`), or deciding which bound you have (`cpu-vs-gpu-diagnoser`).

## Inputs (max 2)
1. Target device and frame goal (default: low-end phone, 30 FPS; budgets switch to the MOBILE table). 2. Whether streaming is on (default: read it from the place); with streaming on, the counts that matter are those inside the streaming radius.

## Procedure
1. Run `scripts/count_regions.luau` (read-only). Save the output. It prints parts, 3x3 neighbourhood sum, mesh parts, unions and partially transparent parts per 256-stud cell, worst first. Stop if the place has no parts in Workspace.
2. Read the real renderer numbers for the worst cell: stand in it (Play, or camera in Edit) and read Render stats and Scene Draw Count (Ctrl+Shift+F2) for draw calls and triangles. These are the numbers the budget uses; part counts are only the lead.
3. Evaluate with `scripts/PartBudget.luau`: `PartBudget.evaluate(regions, PartBudget.MOBILE)` where each region is `{name, parts, drawCalls?, triangles?}`; use `PartBudget.combine` to sum the cells a player sees together. Status is ok below 80 percent of any budget, warn from 80, over above 100.
4. Cut in this order for each over/warn region: delete hidden, duplicate and unreachable parts (under terrain, behind walls, identical stacked parts); merge groups of meshes into one asset late in development (docs example 8 draw calls to 1); reuse MeshIds and materials so draw calls batch; replace SpecialMesh and most unions with meshes; collapse stacked partially transparent parts; greedy-mesh voxel builds into larger cuboids (vault example 15,931 to 508 instances). Hand the heavy cleanup to `model-cleaner`, distance cuts to `lod-planner`.
5. Re-run steps 1-3 after each batch of cuts. Stop when no region in a playable route is over budget; do not strip detail from regions that are ok.
6. Record the budget table used and each region's before/after numbers.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/count_regions.luau` -> `screen_capture` of the worst cell for the visual record. `PartBudget.luau` is pure logic: run it under Lune or paste it into `execute_luau` with the cell table. Draw calls and triangle numbers come from the Studio stats overlay: MCP cannot read it, so ask the owner or mark them `untested`.

## Fallback
Command bar: paste `count_regions.luau`. Without Studio, ask for an exported list of cell counts and run `PartBudget` under Lune: `lune run` with the table in a scratch file. Triangle and draw-call columns stay `untested` without the overlay.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: budget visible parts not total parts (about 5k visible parts for 60 FPS in one creator test, 25-30 FPS at 9k; indie), merge and reuse meshes, delete hidden content. Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (under about 1,000 draw calls and 1,000,000 triangles as an example baseline-device threshold) and `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization scene-analysis.md` (Instance Composition view). Phone figures of about 500 draw calls and 500k triangles are indie (`Roblox/roblox-kb/scripting-and-performance.md`). Budgets are labelled defaults in the script header; replace them with your own device's measured numbers.

## Output
```
PART AUDIT <place> <date>   budget: <DEFAULT|MOBILE|custom values>
1. City north (cells 2,1..): visible parts 9,200 (184%) worst=visibleParts -> over
   cuts: 1,400 hidden, 900 duplicates, merge shopfronts (est. -35 draw calls)
2. ...
After: <region>: parts A -> B, draw calls C -> D (stats overlay) | untested items listed
```

## Acceptance checks
- [ ] Every ranked region shows the budget it was judged against and the metric that was worst.
- [ ] Draw-call and triangle values come from the stats overlay or are labelled `untested`.
- [ ] Re-count after the cuts shows the region at ok/warn, and the level still plays (core loop run).
- [ ] No visual regression in a before/after `screen_capture` of the worst cell.
- [ ] Executed check: `PartBudget.test.luau` passes under Lune, and both scripts pass luau-check.

## Pitfalls
Counting the whole map. Treating a part count as a draw-call count (batching changes it). Cutting detail in regions nobody sees. Merging meshes early and losing per-part editing. Forgetting that partial transparency adds overdraw even at low part counts. Applying the PC budget to phones.

## Related
`game-optimizer`, `render-cost-auditor`, `model-cleaner`, `lod-planner`, `streaming-enabler`, `cpu-vs-gpu-diagnoser`.
