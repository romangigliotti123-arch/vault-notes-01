---
name: tool-weapon-system-builder
description: "Build tools and weapons with server-validated activation: equipped, alive, cooldown on a server clock, ammo, reload time and damage taken from a server table, never from the client. Use for swords, guns and abilities; hit detection is hitbox-combat-builder."
category: systems
tags: weapons, tools, cooldown, ammo, reload, activation, damage table, gun, sword, server validated
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/case-studies-phantom-forces.md
related: hitbox-combat-builder, health-damage-builder, spawn-system-builder, remote-guard-builder, inventory-system-builder
---

# tool-weapon-system-builder

One job: decide whether an activation happens and how much damage it carries. `scripts/Weapons.luau` checks the weapon exists, the player holds it and is alive, the cooldown has passed (with a small latency allowance), ammo is available and no reload is running; the damage number comes from the server's weapon table. It returns `ok, reason, damage`; hit detection (`hitbox-combat-builder`) and applying damage (`health-damage-builder`) are separate steps.

## When to use
Any weapon, tool or ability with cooldown or ammo. Not for: hit detection, health, animations and visual effects.

## Inputs (max 2)
1. Weapon list: cooldown, damage, magazine, reload (default: 1 melee, 1 hitscan gun). 2. Latency allowance (default 0.05 s).

## Procedure
1. Fill the weapon table: `{ cooldown, damage, mag?, reload? }`; `mag` and `reload` come together or the constructor asserts. Cooldown above 0 is mandatory. Vault: derive fire rate from RPM as `60 / rpm`.
2. Copy `Weapons.luau`; `Weapons.new({ defs, now = os.clock, latency = 0.05 })`.
3. Remote `Activate(weaponName, aimHint)` (rate-limited, argument types checked by `remote-guard-builder`): the handler builds `player = { equipped = <name of the Tool the SERVER sees equipped>, alive = humanoid.Health > 0 }` and calls `weapons:activate(userId, name, player)`. The name argument is only checked against the equipped tool, never trusted.
4. On `ok` run hit detection with `HitCheck` (ranges and angles also come from the server table) and then `health:damage(state, dmg, type)`; on refusal do nothing and optionally tell the client the reason for UI.
5. Reload: `Reload(weaponName)` remote -> `weapons:reload`; the module sets the ammo to full and blocks activation for `reload` seconds. Cancel-on-switch policies are a design choice in the glue.
6. Clean up per-player state on leave (`weapons:forget(userId)`); ammo for saved/persistent weapons can be stored in `data` instead if it must survive death.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/tool-weapon-system-builder/scripts/tests/Weapons.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Weapons.luau`, the weapon table and the Activate handler -> `start_stop_play` -> `execute_luau` (Server) to fire a weapon twice quickly and once after the cooldown with a fake equipped state -> `get_console_output` to read the result. Tool models, animations and client prediction are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (Tool instances, animations, client feedback) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/combat-and-gameplay-systems.md` (for client-side hit detection check range with a lag margin, enforce attack cooldown with os.clock, check facing unless AoE; track last fire time, ammo, alive status and block firing during reload; example 800 RPM = `wait(60/rpm)` with a canFire flag), `Roblox/roblox-kb/anti-exploit-and-security.md` (never trust client-sent values), `Roblox/roblox-kb/client-server-and-remotes.md`.

## Output
`Weapons.luau`, the weapon table, remotes, `design/weapons.md` (stats table with the reasoning for cooldowns).

## Acceptance checks
- [ ] Damage comes from the table and the cooldown is enforced (Weapons test 1).
- [ ] Not equipped, dead, unknown and non-string weapon names are refused (test 2).
- [ ] Ammo runs out, reload refills after its time (test 3).
- [ ] No remote carries a damage number (grep the handlers).
- [ ] Weapons Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/tool-weapon-system-builder/scripts/tests/Weapons.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Cooldown kept on the client. `os.time()` for sub-second cooldowns (use `os.clock`). Firing allowed while reloading because the reload flag is a client Attribute. Damage multiplied by a client-supplied value. Forgetting `forget` on leave.

## Related
`hitbox-combat-builder`, `health-damage-builder`, `spawn-system-builder`, `remote-guard-builder`, `inventory-system-builder`.
