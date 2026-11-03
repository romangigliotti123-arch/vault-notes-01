---
name: speed-teleport-detector
description: "Add server-side detection of speed, teleport, fly and noclip-style movement cheats: sample the SERVER position, compare with what the game allows, exempt legitimate teleports and vehicles, reset quietly first and escalate only on repeats. Use when players can move faster or farther than your rules, or before adding any movement-based reward."
category: qa
tags: speed hack, teleport, fly, noclip, movement, anti-cheat, server authority, exploit, walkspeed, detection
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md, Mentor/Combined-Brain.md
related: honeypot-remote-builder, exploit-audit, server-authority-checker, remote-guard-builder, join-leave-race-tester, playtest-bot-writer
---

# speed-teleport-detector

Movement checks run on the server against server-observed positions. Client properties (WalkSpeed, state, a client "anti-cheat" flag) can be spoofed or hooked, so they are never evidence. `scripts/MovementCheck.luau` is the tested sampler (positions in, verdict out); this skill wires it in with generous tolerance, exemptions and a quiet response. It returns verdicts; the policy ladder is `honeypot-remote-builder/scripts/Honeypot.luau`.

## When to use
Players cover distance faster than the design allows, a reward depends on movement (obby checkpoints, delivery, races), or you just added teleports, vehicles, dashes or knockback that need exemptions. Not for: combat hit validation (`remote-guard-builder`, hit requests), or a game where physics is fully server-authoritative already (Server Authority mirrors scripted movement; check the current docs).

## Inputs (max 2)
1. Maximum legit speeds: base WalkSpeed, sprint, speed pass, vehicles, dashes (default: read them from the code). 2. The legit teleports in the game: spawn, checkpoints, doors, portals, respawn (default: grep `PivotTo|CFrame =|SetPrimaryPartCFrame|TeleportService`).

## Procedure
1. List every speed source and every teleport source from the code; each becomes either a `SetSpeed(userId, n)` value or an `Exempt(userId, seconds, now)` call. Stop when no code path moves a character without being on the list.
2. Copy `scripts/MovementCheck.luau` into ServerScriptService. Sample every 0.25-1 s from one server loop (`Heartbeat` accumulator), passing `HumanoidRootPart.Position`, `os.clock()` and `Humanoid.FloorMaterial == Enum.Material.Air`. Do not sample per frame.
3. Use generous tolerance: `margin` 2 studs per sample and a speed allowance a little above the real maximum; the vault flags WalkSpeed 16 only above roughly 24-28 studs/s. Start permissive, log-only.
4. Exempt around every legit teleport, respawn, seat/vehicle entry and knockback for 2-3 s, and re-baseline after `maxDt`. A false positive on a teleport is the usual bug.
5. Respond quietly: on `speed`/`teleport` set the character back to `verdict.resetTo` and add a low-weight flag (`Honeypot:Flag(userId, "speed", 1)`); only repeated flags climb to restriction or human review. Never kick from one sample; prefer reversible actions.
6. Fly: use the airborne timer (`maxAirtime`), not Humanoid state; noclip needs a raycast from last to current position (flag only when it crosses solid geometry) and is optional.
7. Verify: Lune tests (below), then in a TEST place move a character with `execute_luau` (`root.CFrame += Vector3.new(500,0,0)`, then `root.AssemblyLinearVelocity`) and read the log. Test with a NON-dev account too: dev accounts can be exempt, and one teleport false positive stayed hidden that way (vault).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) to add the sampler and to move the character past the limits -> `get_console_output` for the flag lines -> `character_navigation` to walk a legit route to prove no flags -> `start_stop_play` (stop).

## Fallback
No Studio: run `lune run ../skillpack/qa/speed-teleport-detector/scripts/tests/MovementCheck.test.luau` from `claude-kit/systems`; replay recorded position logs through `Sample` by hand. In-engine behaviour (lag, physics, vehicles) is `untested`.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: validate movement by server position, not client properties; generous tolerance with lag leeway; explicit exemptions for teleports and vehicles; fly via airborne timers; check horizontal and vertical separately; neutralise quietly before punishing; escalating consequence ladder with a suspicion score; thresholds are game-specific (tune and test against custom physics). `Roblox/roblox-kb/testing-debugging-and-qa.md`: test anti-cheat with non-dev accounts. Trust: indie and DevForum guidance, labelled; the numbers in `MovementCheck` defaults are starting points, not platform facts.

## Output
`ServerScriptService/MovementCheck.luau` + a small sampler script, an exemption list (source -> seconds), the thresholds chosen with the reason, and a test log (legit route = 0 flags, forced teleport/speed = flagged and reset).

## Acceptance checks
- [ ] `lune run` of the MovementCheck test file prints "10 passed, 0 failed".
- [ ] A normal playthrough (spawn, doors, vehicle, sprint) produced 0 flags in the log.
- [ ] A forced 500-stud move and a sustained 2x speed were flagged and the character was reset to the last valid position.
- [ ] Every teleport/vehicle code path has an exemption; none of the response code kicks on a single sample.
- [ ] Tested with a non-dev account, or reported `untested`.

## Pitfalls
Sampling per frame (noise, cost). Judging on client-reported speed. Forgetting exemptions after adding a new teleporter. Banning on one flag. Network ownership of parts/vehicles moving the character. Thresholds copied from another game.

## Related
`honeypot-remote-builder`, `exploit-audit`, `server-authority-checker`, `remote-guard-builder`, `playtest-bot-writer`.
