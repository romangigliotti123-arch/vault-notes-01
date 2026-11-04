---
name: npc-spawner-builder
description: "Build NPC spawn rules with a cost cap: global and per-zone caps checked before spawning, a despawn sweep for NPCs nobody is near, an idle/aggro/return decision with a leash, and server network ownership. Use for enemy and creature spawning; pathfinding is rbx-npc."
category: systems
tags: npc, spawner, enemies, cap, despawn, aggro, leash, network ownership, zone, budget
kb: Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: rbx-npc, health-damage-builder, loot-drop-builder, hitbox-combat-builder, game-optimizer, lag-hunter
---

# npc-spawner-builder

One job: keep NPC counts and cost bounded. `scripts/NpcBudget.luau` refuses a spawn when the global cap or the zone cap is reached, finds NPCs with no player within the despawn distance, and decides an NPC's next state from distances (aggro inside range, forced return beyond the leash, idle again at home). Models, animation and pathfinding live in the glue and in the installed `rbx-npc` skill.

## When to use
Wave or area-based enemies, ambient creatures, zone spawners. Not for: the AI itself or pathfinding (`rbx-npc`), combat maths, boss scripting.

## Inputs (max 2)
1. Zones, cap per zone and a global cap (default: 40 global, 10-15 per zone; measure on a phone). 2. Aggro range, leash and despawn distance (default: 40, 80, 200 studs).

## Procedure
1. Set the caps from a measurement, not a guess: spawn NPCs until the lowest-end target device drops below the frame budget (`lag-hunter`/`game-optimizer`) and set the global cap at about 70% of that count.
2. Copy `NpcBudget.luau`; the constructor requires `leash >= aggroRange` and `despawnDistance > aggroRange` so NPCs do not give up as they notice you or vanish while chasing.
3. Spawn flow: `if budget:canSpawn(zone) then model = clone; budget:add(id, zone) end`; on death or despawn `budget:remove(id)`. Count registered NPCs, not Workspace children.
4. Ownership: call `SetNetworkOwner(nil)` on NPC root parts so clients cannot move them (vault). Keep NPC state as attributes on the model within the per-instance attribute limit, or in a server table.
5. Every 2-5 s: `budget:sweep(npcPositions, playerPositions)` returns ids with no player near; despawn them (with `Debris` or `Destroy`) and free the budget. Run `budget:decide(current, nearest, home)` per NPC at a low rate (4-10 Hz), not every frame.
6. Loot and death: use `loot-drop-builder` and `health-damage-builder`; despawn uncollected drops with a lifetime (vault example 20 s).
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/npc-spawner-builder/scripts/tests/NpcBudget.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `NpcBudget.luau` and the spawner script -> `start_stop_play` -> `execute_luau` (Server) to spawn to the cap, remove some, and print `budget:total()` and the sweep result for fake positions -> `get_console_output` to read the result. Pathfinding, models and real frame cost are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (frame cost on devices, pathfinding, network ownership behaviour) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md` (call SetNetworkOwner(nil) on unanchored NPCs, zombies, coins and pushed items so clients cannot move them), `Roblox/roblox-kb/combat-and-gameplay-systems.md` (store NPC state as attributes under the 64-attribute-per-instance limit; despawn uncollected loot with a lifetime), `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md`, `Roblox/roblox-kb/optimization-and-streaming.md`.

## Output
`NpcBudget.luau`, spawner script, `design/npcs.md` (caps with the measurement behind them, ranges, ownership rule).

## Acceptance checks
- [ ] Zone and global caps hold (NpcBudget test 1); unknown zones and duplicate ids are refused (test 2).
- [ ] `remove` frees the budget and is safe twice (test 3).
- [ ] Sweep lists only NPCs with no player nearby (test 4); decide covers aggro, leash and return (test 5).
- [ ] A Studio run at the cap stays within the frame budget on the target device (`untested` unless measured).
- [ ] NpcBudget Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/npc-spawner-builder/scripts/tests/NpcBudget.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Caps that count only live models (leaks from failed despawns). Aggro checks every frame for every NPC. NPCs left with client network ownership. Despawn distance below aggro range. Sweeping so rarely that abandoned zones keep full cost.

## Related
`rbx-npc`, `health-damage-builder`, `loot-drop-builder`, `game-optimizer`, `lag-hunter`.
