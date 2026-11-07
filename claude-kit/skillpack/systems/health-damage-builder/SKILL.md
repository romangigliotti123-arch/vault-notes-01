---
name: health-damage-builder
description: "Build health and damage on the server: damage types, flat armor, percentage resistance (capped at 1), minimum damage, delayed regeneration, one death event and bad-amount rejection. Use for any combat or hazard; hit checks are hitbox-combat-builder."
category: systems
tags: health, damage, armor, resistance, regen, death, humanoid, damage types, true damage
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/case-studies-phantom-forces.md, Roblox/roblox-kb/player-psychology-and-game-feel.md
related: hitbox-combat-builder, tool-weapon-system-builder, spawn-system-builder, npc-spawner-builder, round-system-builder
---

# health-damage-builder

One job: one place that turns an attempted damage into a state change. `scripts/Health.luau` applies resistance by damage type, then flat armor, then a minimum damage floor (True damage skips all three), never lets a negative or non-finite amount heal, reports death exactly once, and regenerates only after a delay since the last hit. The glue copies `hp` to `Humanoid.Health` for display and handles the respawn.

## When to use
Player and NPC health, hazards, environmental damage. Not for: deciding who was hit (`hitbox-combat-builder`), cooldowns (`tool-weapon-system-builder`), respawn placement (`spawn-system-builder`).

## Inputs (max 2)
1. Max health, armor, resistances per entity type (default: players 100 hp, no armor). 2. Regen rule (default: starts 5 s after the last hit, 2 hp/s).

## Procedure
1. Define damage types (`Physical`, `Fire`, ...) and which entities resist which; resist is a 0..1 fraction (the constructor rejects values over 1 because they would heal).
2. Copy `Health.luau`; one `Health.new` per entity type, one state per entity (`h:newState()`); store NPC state in a table keyed by the NPC, player state next to the character.
3. All damage goes through `h:damage(state, amount, kind)`; it returns `dealt, died`. Handle `died` once: drop loot, award, start respawn. Calls on a dead entity return `0, false`.
4. Order is fixed: resistance, then armor, then the minimum (default 1) so armor can never make a hit free; True damage is for hazards like the void. Document the order in the design doc so balance changes use the same maths.
5. Healing: `h:heal(state, amount)` is capped at max and ignores the dead; revive explicitly with `h:revive`. Regen: call `h:tick(state, dt)` from the single server loop, not per-entity threads.
6. Mirror to the Humanoid: set `Humanoid.Health = state.hp` after changes (display only). Do not let `Humanoid:TakeDamage` be the source of truth if you use this module.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/health-damage-builder/scripts/tests/Health.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Health.luau` and the mirroring script -> `start_stop_play` -> `execute_luau` (Server) to apply damage of each type to a test state and print hp -> `get_console_output` to read the result. Humanoid mirroring and death/respawn flow are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (Humanoid mirroring, respawn flow, kill feed) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/combat-and-gameplay-systems.md` (server-validated combat and death handling), `Roblox/roblox-kb/anti-exploit-and-security.md` (reject non-positive or invalid amounts), `Roblox/roblox-kb/case-studies-phantom-forces.md`, `Roblox/roblox-kb/player-psychology-and-game-feel.md` (clear damage feedback). Default regen numbers are starting guesses.

## Output
`Health.luau`, entity configs, `design/health.md` (types, resistances, armor order, regen).

## Acceptance checks
- [ ] Resist then armor then minimum, True ignores all (Health test 1).
- [ ] Negative, zero, NaN, infinite and non-number damage does nothing (test 2).
- [ ] Death fires once; the dead take no damage or healing (test 3).
- [ ] Regen waits for the delay (test 5); resist over 1 is rejected (test 6).
- [ ] Health Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/health-damage-builder/scripts/tests/Health.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Letting a client call damage or heal remotes. Percent armor that reaches 100% (immortal) - keep resist below 1 in design even though 1 is allowed. Two sources of truth (Humanoid and module). Regen ticking per entity thread. Counting overkill as dealt damage in stats (the module returns the clamped value).

## Related
`hitbox-combat-builder`, `tool-weapon-system-builder`, `spawn-system-builder`, `npc-spawner-builder`, `round-system-builder`.
