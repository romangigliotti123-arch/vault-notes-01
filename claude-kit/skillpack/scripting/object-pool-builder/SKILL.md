---
name: object-pool-builder
description: "Reuse frequently spawned things (projectiles, hit effects, damage numbers, pickups, table buffers) through a capped pool with a reset function and a full-pool policy, instead of creating and destroying them every time. Use when a profile or the memory tags show churn from instance creation."
category: scripting
tags: object pool, pooling, projectile, effects, instance reuse, gc, allocation, part cache, spawn, destroy
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: connection-leak-auditor, script-profiler, game-optimizer, vfx-and-particles, raycast-recipes
---

# object-pool-builder

Creating and destroying instances costs CPU, memory churn and replication. A pool keeps finished ones aside and hands them out again. It is an optimisation: measure that the churn is real first (`script-profiler`, memory tags), because a pool adds a bug class (stale state).

## When to use
Dozens of identical short-lived objects per second: bullets, impact effects, floating numbers, coins, UI rows. Not for: rare spawns, objects that differ completely each time, or anything the profile does not flag. Servers replicate every created part; for cosmetic effects consider making them on the client only.

## Inputs (max 2)
1. What is spawned, how often and how long each lives. 2. Cap (default: peak concurrent count with 25 percent slack).

## Procedure
1. Count the real numbers: spawns per second and the maximum alive at once. That gives `max`; `prewarm` is the typical steady-state count.
2. Copy `scripts/Pool.luau`. Write `create` (clone a template, fully configured, parked) and `reset` (return it to an inert, invisible, unparented state: `Parent = nil`, velocity zero, transparency and effects cleared, connections disconnected, attributes restored). `reset` runs on release and on prewarm, so every item enters the pool clean.
3. Choose the full-pool policy: `"fail"` (Acquire returns nil, the caller skips the effect; right for gameplay objects you must not steal) or `"recycleOldest"` (reuses the oldest in-use item; right for cosmetic effects where the oldest is already invisible).
4. Use: `local item = pool:Acquire(); if item then configure(item); item.Parent = workspace.Effects end` (configure first, parent last). End of life: `pool:Release(item)`. A double release or a foreign item returns false, so a bug cannot corrupt the pool.
5. Lifetimes: release on a timer (`task.delay`) or on hit. Anything that can be destroyed by other code (a part falling out of the world) must be released or replaced; check `item.Parent` before reuse.
6. Stats: `pool:Stats()` gives free, in-use, created, recycled, refused. Log it during a stress test; `refused` above zero means the cap is too low or releases are missing.
7. Shutdown: `pool:Destroy(function(item) item:Destroy() end)`.
8. Tables are poolable too: reuse scratch tables in hot loops (`table.clear` as the reset); the vault also lists pooling tables to cut GC cost.
9. Test: `lune run ../skillpack/scripting/object-pool-builder/scripts/tests/Pool.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `Instance.new|:Clone()` in hot paths -> `multi_edit` -> `start_stop_play` -> `execute_luau` (Server) stress-firing and printing `pool:Stats()` and `#workspace:GetDescendants()` -> `get_console_output`; Developer Console memory tags (manual).

## Fallback
Lune tests cover the pool logic. The CPU and memory gain is `untested` without a running place and a measurement.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: pool tables and reduce temporary table creation to lower GC cost; clean up projectiles by distance and lifetime; destroy tracked instances on every creation path; set properties before parenting; an indie 2020 DevForum post recommends part caching (older, labelled). `Roblox/roblox-kb/combat-and-gameplay-systems.md`: projectile handling.

## Output
`Pool.luau`, the create/reset functions for the object, the chosen cap and policy, `Stats()` from a stress run.

## Acceptance checks
- [ ] Executed: Lune test quoted (`6 passed, 0 failed`).
- [ ] `reset` restores every property the user changes (checked by listing them).
- [ ] Cap and policy chosen from measured counts.
- [ ] Stress run: `refused` is 0 for gameplay objects, instance count flat.
- [ ] Before/after cost measured, or marked untested.

## Pitfalls
Reset that misses one property (stale colour, velocity, trail). Releasing an item twice or while still referenced by a timer that releases it later. A pool with no cap. Pooling objects with unique state (just create them). Pooling instead of fixing a leak (use `connection-leak-auditor`).

## Related
`connection-leak-auditor`, `script-profiler`, `game-optimizer`, `raycast-recipes`.
