---
name: raycast-recipes
description: "Pick and write the right spatial query for the job (ray, sphere or block cast, overlap in a box or radius, swept ray for fast movers) with RaycastParams set correctly, nil-checked results and server-side use for anything that matters. Use when writing hit detection, line of sight, ground checks or area effects."
category: scripting
tags: raycast, spherecast, blockcast, overlap, hit detection, line of sight, raycastparams, filter, spatial query, bullets
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: collision-group-setup, remote-guard-builder, rbx-npc, actor-parallel-converter, script-profiler
---

# raycast-recipes

Most hit-detection bugs are a wrong query or wrong parameters, not wrong maths. This skill chooses the query, sets the parameters, and keeps the authority on the server. The helpers live in `scripts/RaycastKit.luau`.

## When to use
Bullets, melee sweeps, line of sight, ground detection, interaction targets, area damage, camera probes. Not for: pathing (`rbx-npc`), or physics-driven projectiles that the engine simulates.

## Inputs (max 2)
1. What must be detected and by whom (shooter, NPC, trigger). 2. Who is the authority (default server).

## Procedure
1. Choose the query: thin line = `Raycast`; a thick body (bullets with radius, melee arcs, camera probes) = `Spherecast` or `Blockcast`; "what is inside this volume" = `GetPartBoundsInRadius` or `GetPartBoundsInBox` (overlap, no direction); a fast mover between frames = `RaycastKit.sweep` (cast along the path in steps so thin parts cannot be skipped).
2. Build the filter with `RaycastKit.exclude({ shooterCharacter, projectile })` or `RaycastKit.include({ targets })`. Prefer the 2026 `ExcludeInstances` / `IncludeInstances` fields (faster than `FilterDescendantsInstances`, cheap to update; exclusion wins when an instance is in both). If you still edit a `FilterDescendantsInstances` table, reassign it afterwards: the property copies on assignment.
3. The direction vector's length is the ray length (max 15,000 studs); `RaycastKit.cast` clamps it. Origin should be outside the shooter (start at an attachment or muzzle, and exclude the character), or the ray hits its own body.
4. Always nil-check: `local hit = RaycastKit.cast(o, d, params); if not hit then ... end`. Use `hit.Instance`, `hit.Position`, `hit.Normal`; for damage identify the character from `hit.Instance:FindFirstAncestorOfClass("Model")` and a Humanoid, then validate on the server.
5. Collision rules: parts with `CanQuery = false` are skipped; set `RespectCanCollide` or a `CollisionGroup` on the params when only certain groups should block (see `collision-group-setup`).
6. Authority: the server performs the cast that causes damage, using a client-sent origin only after distance and plausibility checks (`remote-guard-builder`); the client may cast the same ray for instant feedback.
7. Budget: spread many casts across frames and share results; for thousands per frame consider `actor-parallel-converter` (query APIs have varying thread-safety, live-check).
8. Prove it: in a play test cast through known geometry (a wall, a thin part, a character) and print the instance and distance; run the sweep on a fast-moving part to confirm no tunnelling.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) running `RaycastKit` calls against named test parts -> `get_console_output` for the hit report -> `screen_capture` with visualised rays if drawn -> `multi_edit` the fix. The Studio collision visualisers can filter by CanCollide, CanQuery and collision groups to explain misses.

## Fallback
Without Studio the engine casts cannot run. The cast, clamp and sweep logic runs under Lune against a fake world: `lune run ../skillpack/scripting/raycast-recipes/scripts/tests/RaycastKit.test.luau` from the kit `systems` folder. Real geometry checks are `untested`.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: replace the FindPartOnRay family with `Workspace:Raycast`, direction magnitude is the length (15,000 studs), nil-check, ignore the shooter, `CanQuery` false to exclude, budget casts; sub-step position checks for fast movers; ExcludeInstances/IncludeInstances faster than FilterDescendantsInstances (DevForum 2026-04). `Roblox/roblox-kb/luau-language-and-types.md`: reassign filter tables after editing.

## Output
The chosen query and parameter block per use, the call site code, and the play-test hit report.

## Acceptance checks
- [ ] Every cast result is nil-checked and the shooter is excluded.
- [ ] Damage or reward logic runs on the server after plausibility checks.
- [ ] Executed: the Lune test quoted (`5 passed, 0 failed`).
- [ ] Ray length is within 15,000 studs or chained deliberately.
- [ ] Thin-target and fast-mover cases tested in play (or marked untested).
- [ ] No per-frame casts beyond the measured budget.

## Pitfalls
Casting from inside the shooter's own hitbox. Using `Touched` for hit detection that needs precision. Trusting a client-sent hit result. Forgetting that unanchored moving parts change between frames. Using a ray where a sphere is needed (bullets pass between legs).

## Related
`collision-group-setup`, `remote-guard-builder`, `rbx-npc`, `script-profiler`.
