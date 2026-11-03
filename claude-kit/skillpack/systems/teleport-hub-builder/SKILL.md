---
name: teleport-hub-builder
description: "Build a hub world's portal logic: a server whitelist of destinations by name, per-player teleport cooldown, party grouping into TeleportAsync batches, retry backoff and a failure release; place ids stay 0 until set in Creator Hub. Use for portal hubs; queue-to-match is lobby-matchmaking-builder."
category: systems
tags: teleport hub, portals, TeleportService, destinations, party, cooldown, retry, reserved server
kb: Roblox/roblox-kb/matchmaking-and-teleport.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/case-studies-brookhaven.md
related: lobby-matchmaking-builder, round-system-builder, remote-guard-builder, exploit-audit, roblox-studio-connect
---

# teleport-hub-builder

One job: let players travel between places safely. `scripts/Portals.luau` resolves a destination NAME against a server whitelist (the client never sends a place id), refuses destinations whose id is still 0 (SET IN CREATOR HUB), enforces party size and a per-player cooldown, splits a party into batches of at most `maxGroup`, and gives retry delays (1, 2, 4, 8, 8 s). `failed` releases the cooldown after an error so players can try again.

## When to use
Hubs with portals to experiences/places, adventure worlds with separate places, party travel. Not for: matchmaking queues (`lobby-matchmaking-builder`), cross-experience economies, in-place teleports (`PivotTo`).

## Inputs (max 2)
1. Destinations: name, place id, reserved server yes/no, max party (default: ids 0 until the owner creates the places). 2. Cooldown and group size (default: 3 s, 50).

## Procedure
1. List destinations and create the places in the experience (Creator Hub; the owner does this). Record place ids in `Destinations.luau`; leave `0` for unknown ids and the plan refuses them with a note.
2. Copy `Portals.luau`; `Portals.new({ destinations, now = os.clock, maxGroup = 50, cooldown = 3, maxAttempts = 5 })`.
3. Portal touch or prompt (server): the player and their party members come from the server; the client sends only the portal NAME if at all (the touched part's attribute is better). `portals:plan(name, userIds)` returns `{ placeId, reserved, groups }` or `nil, reason`.
4. For each group: reserved destinations call `TeleportService:ReserveServer(placeId)` once per party and set `TeleportOptions.ReservedServerId` (vault: exactly one routing field per options); others use plain options. Wrap `TeleportAsync` in `pcall`; on error wait `portals:retryDelay(attempt)` and retry, and when it returns nil call `portals:failed(ids)` and tell the players.
5. Handle `TeleportInitFailed` (failures after a successful call) the same way; never leave a party half-teleported without telling them.
6. Carry data with `TeleportData` only as a hint (party id, destination); the arrival server re-validates everything from its own saved data, never trusting the payload.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/teleport-hub-builder/scripts/tests/Portals.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Destinations.luau`, `Portals.luau` and the portal handler -> `start_stop_play` -> `execute_luau` (Server) to plan teleports for fake users and print groups/reasons -> `get_console_output` to read the result. Real teleports need published places: `untested` until run.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (TeleportAsync, reserved servers, TeleportInitFailed, party carry) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/matchmaking-and-teleport.md` (wrap TeleportAsync in pcall with retries, up to 5 in the docs' SafeTeleport example; TeleportInitFailed; one routing field per TeleportOptions; generate reserved server codes once), `Roblox/roblox-kb/anti-exploit-and-security.md` (validate arguments; treat remote payloads as untrusted), `Roblox/roblox-kb/social-features-and-virality.md`. TeleportService details change: live-check the Creator Docs.

## Output
`Destinations.luau`, `Portals.luau`, portal handler, `design/hub.md` (destinations, party rules, failure handling).

## Acceptance checks
- [ ] Only named, set destinations resolve; non-strings and id 0 are refused (Portals test 1).
- [ ] A party is split into batches of `maxGroup` (test 2); size limits enforced (test 3).
- [ ] Cooldown blocks repeats and `failed` releases it (test 4); retry delays back off and stop (test 5).
- [ ] Portals Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/teleport-hub-builder/scripts/tests/Portals.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Accepting a place id from the client. Teleporting without `pcall`. New reserved server per player of one party. Trusting `TeleportData` on arrival. Forgetting `failed` so a failed teleport locks the player out for the cooldown.

## Related
`lobby-matchmaking-builder`, `round-system-builder`, `remote-guard-builder`, `exploit-audit`.
