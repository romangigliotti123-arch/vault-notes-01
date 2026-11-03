---
name: level-flow-planner
description: "Plan the path, landmarks, pacing and rest spots of a map or obby on paper before building geometry, and check walking times between points with levelflow.py (points within about 10 seconds, rest after hazard clusters). Use after the loop and fantasy exist and before greyboxing."
category: design
tags: level design, map, obby, path, landmarks, pacing, checkpoint, flow, greybox, wayfinding
kb: Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-obby.md, Roblox/roblox-kb/case-studies-tower-of-hell.md, Roblox/roblox-kb/case-studies-doors.md
related: difficulty-tuner, core-loop-designer, world-theme-picker, boss-encounter-designer, part-count-auditor, lighting-preset-picker
---

# level-flow-planner

Vault: decide the design before opening Studio, sketch the layout with 1-3 basic shapes, greybox before art, keep points of interest within about 10 seconds' walk, use colour and light to guide, start worlds small, give several routes in combat maps.

## When to use
Before building a map, lobby, obby or dungeon. Not for: difficulty numbers (`difficulty-tuner`), art style (`world-theme-picker`), part budgets (`part-count-auditor`).

## Inputs (max 3)
1. Map type: obby, hub, arena, dungeon, open world (default: from the pitch). 2. Target time to cross it once (default: 3-5 minutes for a first area). 3. Walk speed (default: 16 studs/s, the Roblox default; live-check if changed).

## Procedure
1. Write the one-line purpose of the map: which loop verb happens where. Stop if two purposes compete.
2. Sketch the path on paper: spawn, 3-7 beats (landmark, challenge, reward, rest), goal. Use simple shapes; keep everything in sight of a landmark (a tall tower, colour, light) so players can orient.
3. Make the beat list a CSV `name,kind,x,z` (studs; kinds spawn, poi, rest, checkpoint, hazard, goal) in walking order and run `python level-flow-planner/scripts/levelflow.py points.csv`. Fix every FLAG: empty stretches over 10 s, first point of interest more than 10 s from spawn, no goal, or three hazards without a rest within 60 s.
4. Pacing: tension then release. After a hard beat put a rest spot or checkpoint, then a reward, then the next beat; vary the beat type so no three beats in a row feel the same.
5. Routes: for combat maps give 2-3 entry points per building, 2-4 primary obstacles forcing a choice, a few dead ends as risk/reward spots. For obbies make checkpoints persistent and stage-gated.
6. Fast travel: add after first exploration for larger maps; keep travel short.
7. Greybox plan: list which parts to block out first (path, landmarks, goal), then trigger volumes, then dressing last. Hand the CSV and sketch to the builder skills.
8. Save `design/level-flow.md` with the sketch description and script output.

## Studio MCP path
After greybox: `execute_luau` (Server) to read part positions and compute real distances; `start_stop_play` and `character_navigation` to walk spawn to goal and time it; `screen_capture` at each landmark.

## Fallback
Estimate positions on graph paper (1 square = 10 studs); mark times `estimated`.

## Evidence
`building-and-level-design` (design before Studio; greybox before art; several routes; limited entry points; trigger sizes against the 6.5-stud avatar), `core-loops-and-game-design` (keep travel short; levels cohesive and readable), `case-studies-obby`, `case-studies-tower-of-hell` (stage escalation pattern), `case-studies-doors` (a white hallway with two monsters was already fun: validate the flow cheaply).

## Output
`design/level-flow.md`: purpose, beat table with minutes, `levelflow.py` output ending OK, route notes, greybox build order.

## Acceptance checks
- [ ] Executed: `python level-flow-planner/scripts/levelflow.py --selftest` prints `selftest ok`; the design CSV run ends with `OK`.
- [ ] No leg over 10 s and a rest or checkpoint after every hazard cluster.
- [ ] Each beat names its loop verb or reward.
- [ ] A landmark is visible from spawn.

## Pitfalls
Building art before the path works. Huge empty maps on mobile. A checkpoint far behind the hardest jump. Identical beats repeated.

## Related
`difficulty-tuner`, `world-theme-picker`, `boss-encounter-designer`, `part-count-auditor`.
