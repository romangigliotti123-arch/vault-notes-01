---
name: codes-system-builder
description: "Build the server side of a redeem-code system: the CodeBook rules plus a tested RedeemService with an atomic global-use counter, per-player once, undo on a failed grant, guess throttling and logging, wired to PlayerData and a DataStore. Use after codes-campaign-planner has designed the codes."
category: liveops
tags: redeem codes, codes, promo, server, datastore, rate limit, throttle, anti abuse, redeem service, live ops
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/updates-live-ops.md
related: codes-campaign-planner, remote-guard-builder, datastore-schema-builder, feature-flag-config-builder, exploit-audit, event-planner, rbx-datastore, rbx-remote-sec
---

# codes-system-builder

`codes-campaign-planner` decides WHICH codes, rewards and limits (and ships the pure rules in `CodeBook`). This skill is the server implementation: the part that must not fail under two servers, two clicks and a script guessing codes. Vault: codes tied to milestones keep daily logins active; the risk is a leaked or farmed code.

## When to use
You have a code book and need the redeem path in the game. Not for: designing the campaign (`codes-campaign-planner`), purchases (`devproduct-handler`), daily rewards (kit `DailyRewards` system).

## Inputs (max 2)
1. The code book (`CodeBook` entries: reward label, window, per-code cap, creator label) and where it lives (default: a server-only ModuleScript). 2. How rewards are granted (kit `Shop`/`PlayerData` function) and the profile field that records redeemed codes.

## Procedure
1. Copy `CodeBook.luau` (from `marketing/codes-campaign-planner/scripts/`) and `scripts/RedeemService.luau` into server code. Keep the book in `ServerScriptService`/`ServerStorage`; never in a replicated container or a LocalScript. Call `CodeBook.validateBook(book)` at start and fail loudly.
2. Storage for the global counter: a DataStore key per capped code, updated with `UpdateAsync` inside `pcall`: `take(code, maxUses)` returns false if the count is already at the cap, else increments and returns true; `release(code)` decrements. `read(code)` is a plain read. Uncapped codes skip the store. Check the serialised size and request budget (`data-persistence.md`).
3. Per-player once: the redeemed set lives in the kit `PlayerData` profile (field added through `datastore-schema-builder`), loaded before any redeem is allowed, so a rejoin cannot redeem twice.
4. Build the service: `RedeemService.new({ checker = CodeBook, book = book, store = store, now = os.time, grant = grantFn, markRedeemed = markFn, log = logFn })`. `grant` returns true only after the reward was really added; on false the service gives the use back and does not mark the player.
5. Client path: one rate-limited RemoteFunction (kit `RemoteGuard`) that accepts a string of bounded length and returns only a short reason. Never send the code list, the remaining uses or whether a code exists: unknown and expired-removed answer the same.
6. Logging: map `log(event, userId, fields)` to kit `Analytics:Custom` (events `redeem_ok`, `redeem_rejected`, `redeem_throttled`, `redeem_grant_failed`) with low-cardinality fields (code label, creator). Never log the raw typed text or user names. The creator label gives attribution for the campaign table.
7. Throttle: five wrong guesses in 60 seconds per player returns `slow_down`; raise the limits only after you see real misses. One redeem per player in flight (`busy`).
8. Test: `lune run ../skillpack/liveops/codes-system-builder/scripts/tests/RedeemService.test.luau` from `.rbx/claude-kit/systems` (6 tests: grant once, per-player once, global cap, grant-fail undo, throttle, store errors) plus luau-check. Then a Play test with two clients redeeming the last use.
9. Operate: retire leaked codes by changing the book (config flag or republish), publish the active list only to the audience, and expire creator codes later than community codes.

## Studio MCP path
`script_read` the Shop/PlayerData modules -> `multi_edit` to add the profile field and the service wiring -> `start_stop_play` -> `execute_luau` (Server) calling the service with a fake store for a single code and asserting the reward label -> `get_console_output`.

## Fallback
Rojo files plus the Lune suite and luau-check. What stays `untested`: the real DataStore `UpdateAsync` behaviour across servers and the Studio redeem UI.

## Evidence
`Roblox/roblox-kb/data-persistence.md`: wrap every DataStore call in pcall; keep writes small; use UpdateAsync for read-modify-write; session locking for profiles. `anti-exploit-and-security.md` and `client-server-and-remotes.md`: validate every client argument, rate-limit remotes, server owns outcomes. `updates-live-ops.md`: ship redeemable codes tied to milestones (indie, single mention) and drop codes between major updates (single creator). The vault has no code-redemption design guide; the service rules are this skill's own.

## Output
`RedeemService.luau`, the server glue (store, grant, log), the remote handler, the profile field, `liveops/codes-runbook.md` (how to add, retire and audit a code).

## Acceptance checks
- [ ] Lune suite prints "6 passed, 0 failed"; luau-check exit 0.
- [ ] Two simultaneous redeems of the last use produce exactly one grant (Play test or marked untested).
- [ ] A failed grant leaves the counter and the player's set unchanged.
- [ ] The client never receives the code list; unknown and removed codes look identical.
- [ ] Logs contain no raw typed text and no user names.

## Pitfalls
Checking the count and incrementing in two steps. Marking the player before the grant succeeds. Reading the count from a cache on another server. Putting the book in ReplicatedStorage. Rewarding premium currency. No way to retire a leaked code.

## Related
`codes-campaign-planner`, `remote-guard-builder`, `datastore-schema-builder`, `feature-flag-config-builder`, `exploit-audit`.
