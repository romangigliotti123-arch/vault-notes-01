---
name: lobby-matchmaking-builder
description: "Build lobby queue logic for round games: parties stay together, a match starts when full or when the oldest party has waited long enough and the minimum is met, plus leave handling and the reserved-server teleport checklist. Use for queue-to-match flows; the state machine inside a match is round-system-builder."
category: systems
tags: lobby, matchmaking, queue, party, reserved server, teleport, match, minimum players
kb: Roblox/roblox-kb/matchmaking-and-teleport.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/case-studies-bed-wars.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: round-system-builder, teleport-hub-builder, spawn-system-builder, rbx-rounds, discord-server-setup
---

# lobby-matchmaking-builder

One job: decide who plays together. `scripts/Matchmaker.luau` queues parties (never splitting them), starts a match when a group reaches `maxSize` or the oldest party has waited `waitSeconds` with at least `minSize` players, handles leaving mid-queue, and refuses double-queueing. The Roblox side (reserved servers, TeleportAsync with retries) is in the glue and the checklist below.

## When to use
Games where players queue in a lobby place and are teleported into match servers. Not for: single-server round loops (`round-system-builder`), world hubs with portals (`teleport-hub-builder`), skill-based rating systems (not covered; say so and stop).

## Inputs (max 2)
1. Match size range and max wait (default: min 4, max 8, wait 30 s). 2. Party support (default: parties up to max size stay together).

## Procedure
1. Fix the numbers from the game, not from the vault: vault sources give only single-game examples (5 per group in a story game's lobby, a 2-player start in an indie round game) and no verified defaults, so label yours as assumptions and playtest queue times.
2. Copy `Matchmaker.luau`; `Matchmaker.new({ minSize, maxSize, waitSeconds, now = os.time })`. Remote `JoinQueue()` / `LeaveQueue()` (rate-limited) call `enqueue({userId, ...party})` / `leave(userId)`; party membership comes from the server (friends/party system), not the payload.
3. Run `mm:step()` once per second; each returned match is a list of user ids. Create the destination with `TeleportService:ReserveServer(placeId)` (vault: one routing field per TeleportOptions - `ReservedServerId` for developer-created reserved servers; generate the code once per match).
4. Teleport with `TeleportAsync` inside `pcall` and retry on failure (vault example: up to 5 attempts; use `Portals.retryDelay` from `teleport-hub-builder` if you want the same backoff) and handle `TeleportInitFailed` for failures after a successful call. On final failure put the players back into the queue head.
5. In the match server, identify it by a non-empty `PrivateServerId` with `PrivateServerOwnerId == 0` (reserved) and read the expected player list from `TeleportData`; players not in the list are kicked or sent back.
6. Return flow: after the round, teleport back to the lobby place (again with retries); store results in PlayerData before leaving.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/lobby-matchmaking-builder/scripts/tests/Matchmaker.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Matchmaker.luau` and the queue/teleport script -> `start_stop_play` -> `execute_luau` (Server) to enqueue fake users and print the matches from `step()` -> `get_console_output` to read the result. Teleports need a published multi-place experience: `untested` until run live.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (ReserveServer, TeleportAsync, TeleportData, return flow) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/matchmaking-and-teleport.md` (each TeleportOptions sets one routing field - ReservedServerId for developer-created reserved servers; reserved servers are identified on arrival by a non-empty PrivateServerId with PrivateServerOwnerId == 0; wrap TeleportAsync in pcall with retries and handle TeleportInitFailed; group players, five per group in one story-game example, in a lobby then teleport once into a reserved server; no verified minimum player counts or intermission defaults exist in the vault), `Roblox/roblox-kb/social-features-and-virality.md`. Teleport API details change: live-check the Creator Docs.

## Output
`Matchmaker.luau`, queue and teleport script, `design/matchmaking.md` (sizes, wait, party rule, failure handling).

## Acceptance checks
- [ ] A full match starts immediately; a short one only after the wait and with the minimum met (Matchmaker tests 1-3).
- [ ] Parties are never split (test 4); double queueing and oversized parties are refused (test 5).
- [ ] A failed teleport puts players back (design doc says how; `untested` until run).
- [ ] Matchmaker Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/lobby-matchmaking-builder/scripts/tests/Matchmaker.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Teleporting without `pcall`. Creating a reserved server per player instead of per match. Trusting a client-sent party. Starting a match with fewer players than the rules need. No path back to the lobby on failure (players stranded).

## Related
`round-system-builder`, `teleport-hub-builder`, `spawn-system-builder`, `rbx-rounds`.
