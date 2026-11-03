---
name: collision-group-setup
description: "Design collision groups and their matrix as data, validate it (names, duplicates, the 32-group budget, conflicts), then apply it through an adapter that follows the current API. Use for players that must not block each other, NPC separation, pickups, projectiles and vehicle parts."
category: scripting
tags: collision group, physics, matrix, nocollide, players, npc, pickups, worldroot, physicsservice, collidable
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: raycast-recipes, roblox-npc-pathfinding, vehicle-system-builder, model-cleaner, game-optimizer
---

# collision-group-setup

Collision groups say which kinds of parts collide. The design is a small matrix; the failures are bad names, too many groups, forgotten parts (accessories, tools, streamed parts) and calling an API that has since moved. `scripts/CollisionMatrix.luau` makes the matrix data, checks it, and applies it through an adapter so the API change touches one function.

## When to use
Players should pass through each other, NPCs should not push players, pickups should be touchable but not solid, projectiles should skip friendly characters, wheels should not hit their chassis. Not for: a single pair (a `NoCollisionConstraint` between two parts is simpler for wheel and body).

## Inputs (max 2)
1. The kinds of objects (groups). 2. For each pair, collide or not (default: everything collides, list only the exceptions).

## Procedure
1. List groups (letters, digits, space, underscore; max 100 characters; `Default` always exists, do not redeclare it). Keep the count low: the vault gives a budget of 32 groups per world, so reuse groups rather than one per object.
2. Write the spec: `groups`, `noCollide` pairs and any explicit `collide` pairs. Roblox collides every pair by default, so the plan only needs the exceptions.
3. `CollisionMatrix.plan(spec)` returns `register` (names), `pairs` (collidable changes) and `problems` (duplicates, unknown group, a pair listed both ways, over budget). Fix problems before applying; `CollisionMatrix.apply` refuses a plan that has any. `CollisionMatrix.matrix(spec)` prints an X and dot grid for review.
4. API check, live: the vault records that collision group management moved from PhysicsService to WorldRoot (official, 2026-09-03; each WorldModel has its own 32-group budget; PhysicsService collision methods are deprecated). The WorldRoot method names are not in the vault: read the current docs, then write the `Adapter` (`register(name)`, `setCollidable(a, b, on)`) against them. Do not paste PhysicsService calls into new code.
5. Assign parts: `CollisionMatrix.assign(character, "Players")` sets `CollisionGroup` on every `BasePart` under the model and on parts added later (accessories, tools, streamed parts). Loop only `BasePart`; other instances error.
6. Pair with queries: a `RaycastParams.CollisionGroup` makes rays respect the matrix (see `raycast-recipes`).
7. Apply once on the server at startup, before characters spawn (`CharacterAdded` then `assign`). Collision group properties replicate, so one server-side setup is enough.
8. Test: `lune run ../skillpack/scripting/collision-group-setup/scripts/tests/CollisionMatrix.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) to list registered groups and current settings via the adapter -> `multi_edit` to add the setup script -> `start_stop_play` -> `execute_luau` (Server) walking two test characters into each other / firing a ray, `screen_capture` or `get_console_output` for the result.

## Fallback
The matrix and validation run in Lune. The adapter and `assign` need a place; marked `untested` until played. The Studio editor window (Window, 3D, Collision Groups) can set groups by hand when scripting is not wanted.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md`: collision groups move to WorldRoot, 32-group budget per WorldModel, PhysicsService methods deprecated (official 2026-09-03, live-check); collision visualisers filter by CanCollide, CanQuery and groups. `Roblox/roblox-kb/building-and-level-design.md`: set up groups so NPCs do not collide with each other or players; loop only BaseParts when assigning to characters. `Roblox/roblox-kb/combat-and-gameplay-systems.md`: separate wheels and body.

## Output
`collision.md` (matrix and rationale), the spec table in code, the adapter file, the test line.

## Acceptance checks
- [ ] Executed: `plan(spec).problems` is empty (quote it); Lune test passes (`6 passed, 0 failed`).
- [ ] Group count including Default is within the budget.
- [ ] Adapter written against the current docs (URL/date noted), no deprecated calls.
- [ ] Characters and tools get the group, including late-added parts.
- [ ] Walk-through test in play, or marked untested.

## Pitfalls
Setting groups on the character model instead of each part. Forgetting `CanCollide` is separate from groups (non-colliding parts can still be touched/queried). A group per item type until the budget is gone. Applying groups after characters spawn.

## Related
`raycast-recipes`, `roblox-npc-pathfinding`, `vehicle-system-builder`, `model-cleaner`.
