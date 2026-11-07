---
name: spawn-system-builder
description: "Build team, safe and respawn spawn logic: pick the team spawn farthest from enemies with rotation, and a short protection window that ends when the player attacks and never exceeds 10 seconds. Use for team and arena modes; checkpoint respawns are checkpoint-system-builder."
category: systems
tags: spawn, respawn, team spawn, spawn protection, spawn camping, safe spawn, arena
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/case-studies-arsenal.md, Roblox/roblox-kb/case-studies-bed-wars.md
related: round-system-builder, health-damage-builder, hitbox-combat-builder, checkpoint-system-builder, tool-weapon-system-builder
---

# spawn-system-builder

One job: put players where they have a fair start. `scripts/Spawns.luau` chooses a spawn of the player's team that maximises distance to the nearest enemy (skipping the one used last when scores are close) and manages a short protection window: `damageFor` returns 0 while protected and `attacked` ends it, so protection cannot be used to shoot freely. Window lengths above 10 s are rejected as a spawn-camping abuse vector.

## When to use
Team deathmatch, arena, capture modes, any mode with respawns near enemies. Not for: obby resumes (`checkpoint-system-builder`), map design, choosing teams.

## Inputs (max 2)
1. Spawn parts per team and arena size (default: tag parts with attributes `Team`). 2. Protection seconds (default: 3; 0 for modes where it does not fit).

## Procedure
1. Tag spawn parts (`CollectionService` tag `Spawn`, attribute `Team`) and build the `list` of `{ id, team, pos }` at server start; recompute enemy positions at respawn time only (one scan per respawn, not per frame).
2. Copy `Spawns.luau`; `Spawns.new({ protectSeconds = 3, now = os.clock })`. On `CharacterAdded`/respawn: `local s = spawns:pick(list, team, enemyPositions)`; move the character there (`PivotTo`) and `spawns:protect(userId)`.
3. Damage path: every damage function calls `spawns:damageFor(victimId, amount)` first. Shooting, swinging or using an ability calls `spawns:attacked(attackerId)` so protection ends with the first aggressive act. Show a visible indicator (a ForceField works) and keep it in sync with `isProtected`.
4. Team balance, no-spawn-in-view and 'safest of N random' variants are changes to the scoring in `pick` only; keep the signature.
5. Late join and mid-round respawn: use the same call; do not special-case. Spawn parts must be anchored and server-owned.
6. Cleanup: `spawns:forget(userId)` on leave.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/spawn-system-builder/scripts/tests/Spawns.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Spawns.luau` and the respawn handler -> `start_stop_play` -> `execute_luau` (Server) to call `pick` with test enemy positions and print the chosen spawn ids -> `get_console_output` to read the result. Visual indicator and character placement are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (character placement, ForceField sync) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/combat-and-gameplay-systems.md` (combat systems validate on the server; respawn and death handling), `Roblox/roblox-kb/case-studies-arsenal.md` and `case-studies-bed-wars.md` (round/arena shooters and their respawn flow - read for pacing), `Roblox/roblox-kb/anti-exploit-and-security.md` (server decides state). The 3 s default and the 10 s ceiling are this skill's assumptions, not vault numbers: tune from playtests.

## Output
`Spawns.luau`, the spawn tagging convention, respawn handler, `design/spawns.md` (protection seconds, scoring rule, team rules).

## Acceptance checks
- [ ] The chosen spawn belongs to the team and is farthest from enemies (Spawns tests 1-2).
- [ ] With no enemies it rotates (test 3).
- [ ] Protection lasts its window and ends on attack (test 4); long windows are rejected (test 5).
- [ ] Spawns Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/spawn-system-builder/scripts/tests/Spawns.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Protection that survives attacking. Spawn parts a client can move. Choosing from `GetChildren()` order (always the same spawn). Counting dead or spectating players as enemies. Long protection windows that make spawn trapping and stalling.

## Related
`round-system-builder`, `health-damage-builder`, `hitbox-combat-builder`, `checkpoint-system-builder`, `tool-weapon-system-builder`.
