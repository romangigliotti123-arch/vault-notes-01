---
name: hitbox-combat-builder
description: "Build the server's yes/no on a claimed hit: range with a capped lag allowance scaled by target speed, facing-angle limit, optional line-of-sight result, and once-per-swing de-duplication. Use for melee and ranged hit checks; cooldowns/ammo are tool-weapon-system-builder, damage is health-damage-builder."
category: systems
tags: hitbox, hit detection, range, lag compensation, facing angle, raycast, melee, swing, dedupe
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/case-studies-rivals.md
related: tool-weapon-system-builder, health-damage-builder, remote-guard-builder, exploit-audit, spawn-system-builder
---

# hitbox-combat-builder

One job: given a claimed hit, answer `true, "hit"` or `false, reason` from server knowledge. `scripts/HitCheck.luau` checks the positions are finite, the distance is within `range + targetSpeed * min(lag, maxLag)`, the target is inside the facing cone unless the attack is area, a supplied raycast did not report a wall, and the swing id has not already hit. A refused claim does not burn the swing id.

## When to use
Server-side verification for melee swings, projectiles resolved on hit, and area attacks. Not for: cooldowns and ammo (`tool-weapon-system-builder`), applying damage (`health-damage-builder`), client-side hit effects.

## Inputs (max 2)
1. Attack type: melee cone, hitscan, area (default: melee cone, 70 degrees). 2. Measured server ping source (default: `player:GetNetworkPing()` capped at 0.2 s).

## Procedure
1. Decide where hits are found. Client-detected hits are fast and cheap but must be re-validated here; server-only detection is safest but feels laggy. Vault: for client-side detection, check range with a lag margin, enforce cooldown, check facing unless AoE.
2. Copy `HitCheck.luau`; `HitCheck.new({ maxLag = 0.2, now = os.clock })` (the constructor refuses lag above 1 s: more is an exploit window).
3. The client sends `Hit(swingId, targetUserId)` (rate-limited); the server looks up both characters, reads attacker position, target position and target speed itself, and builds the claim. Never accept positions, speeds or ranges from the client.
4. Run the optional raycast on the server (`workspace:Raycast` with an exclusion filter for both characters) and pass `blocked`. Keep rays few: one per claim.
5. On `true`: call the damage path once. `swingId` comes from the server's own swing counter for that player (issued when `Activate` succeeded), so a client cannot reuse or invent ids.
6. Tune `range` and `maxAngle` from playtests with real latency; log refusals by reason to see if honest players hit the wall (too many 'out of range' means widen the lag allowance, not remove the check).
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/hitbox-combat-builder/scripts/tests/HitCheck.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `HitCheck.luau` and the Hit handler -> `start_stop_play` -> `execute_luau` (Server) to build claims from two test characters and print the verdicts -> `get_console_output` to read the result. Real lag behaviour needs two clients with network simulation: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (real latency, raycast results, client feel) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/combat-and-gameplay-systems.md` (client-side hit detection: check range with a lag margin, enforce attack cooldown with os.clock, check facing angle unless AoE), `Roblox/roblox-kb/anti-exploit-and-security.md` (server decides outcomes; reject NaN and bad values), `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md` (keep gameplay-critical parts under server network ownership), `Roblox/roblox-kb/case-studies-rivals.md`. The 0.2 s lag cap and 70 degree cone are starting guesses to tune.

## Output
`HitCheck.luau`, the Hit handler, `design/hit-checks.md` (ranges, angles, lag cap, how swing ids are issued).

## Acceptance checks
- [ ] In-range and facing is a hit; out of range is refused; the lag allowance widens range by speed times capped lag (HitCheck tests 1-2).
- [ ] One swing hits a target once (test 4).
- [ ] Blocked, NaN and infinite positions are refused (test 5); refused claims do not burn the swing id (test 6).
- [ ] No remote carries positions, speeds or damage (grep).
- [ ] HitCheck Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/hitbox-combat-builder/scripts/tests/HitCheck.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Trusting the client's reported positions. Unlimited lag allowance (turns it into a long-range cheat). Network ownership of weapons or NPCs left with a client. Re-issuing swing ids from the client. Making the angle check so strict that mobile aim fails.

## Related
`tool-weapon-system-builder`, `health-damage-builder`, `remote-guard-builder`, `exploit-audit`, `spawn-system-builder`.
