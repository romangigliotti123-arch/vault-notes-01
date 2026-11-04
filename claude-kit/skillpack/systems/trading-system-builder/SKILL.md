---
name: trading-system-builder
description: "Build safe player-to-player trading that is server-authoritative and duplication-safe: server-owned sessions, offers validated against real inventories, version-bound accepts with a lock window, one synchronous commit with rollback, uid-preserving transfers and a trade log. Built on the pack Inventory and Wallet over the kit's PlayerData."
category: systems
tags: trading, trade, swap, gift, dupe, duplication, exploit, escrow, offer, accept, inventory, atomic
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md, Roblox/roblox-kb/case-studies-adopt-me.md, Roblox/roblox-kb/ugc-and-avatar-economy.md
related: inventory-system-builder, currency-system-builder, pet-system-builder, exploit-audit, remote-guard-builder, dupe-exploit-hunter, datastore-schema-builder, rbx-remote-sec
---

# trading-system-builder

Trading is where economies die: one duplication bug and every item is worthless. This skill builds the smallest design that holds up: the client can only say "set my offer" and "accept version N"; the server owns the session, re-checks both inventories at the moment of commit, moves everything in one synchronous step with a snapshot rollback, and keeps each item's original uid so one item is never two records. Requires `inventory-system-builder` and `currency-system-builder` modules and the kit's `PlayerData` session data.

## When to use
Adding trading, gifting or a player market. Not for: Robux sales (`devproduct-handler`), auction houses across servers (needs a MemoryStore/DataStore design this skill does not cover: say so and stop), item storage (`inventory-system-builder`).

## Inputs (max 2)
1. Which items and currencies are tradable and per-trade caps (default: unique items + Coins, 8 lines, 1e6 coins). 2. Anti-scam rules (default: 5 s lock after any offer change, both sides must accept the same version).

## Procedure
1. Mark `tradable = true` only on items that should move; equipped or bound items are locked through the `locked(data, uid)` hook (pets use `Pets.locked`). Decide the per-trade caps and the lock seconds before writing code.
2. Install PlayerData; add `Inventory.luau`, `Wallet.luau`, `Trade.luau` from the pack scripts. Build `Trade.new({ inventory, wallet, currency, getData, now, newId, lockSeconds = 5, maxItems = 8, log, locked })`; `getData` returns `session.Data` for a user id or nil when not loaded.
3. Remotes (rate-limited via `remote-guard-builder`): `RequestTrade(targetUserId)`, `SetOffer(offerTable)`, `Accept(version)`, `Cancel`. Handlers call `trade:open`, `setOffer`, `accept`, `cancel` with the SENDER's user id from the remote, never an id from the payload. Check distance/area rules in the handler, not in the module.
4. Offers contain only uids or (id, qty) pairs; the module resolves them against the owner's inventory (`resolve`), rejecting unowned uids, duplicates in one offer, untradable items, quantities that are not positive integers, too many lines, and coin amounts above the owner's balance or the cap. Changing an offer resets both accepts and bumps the version.
5. Commit (inside `accept` when both accepted the same version): re-resolve both offers against the CURRENT data, snapshot both inventories and wallets, take from both sides, give to both sides (original uids preserved), and on any failure restore the snapshots and cancel. Nothing between the check and the change may yield (no DataStore calls, no waits).
6. After `done`, force a save for both players (`PlayerData:SaveAsync`) before telling the clients; wire `Players.PlayerRemoving` to `trade:playerLeft(userId)` BEFORE releasing the session. Write the `trade_done` log entry (ids, items, coins) to your analytics/log sink.
7. Dupe audit tooling: run the uid scan `Inventory:uids` over all loaded players in a test server and assert every uid appears once; keep this check in a debug command (`Admin` system). Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/trading-system-builder/scripts/tests/Trade.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Trade.luau` plus the Inventory and Wallet modules and the four remote handlers -> `start_stop_play` -> `execute_luau` (Server) to open a trade between two test players (use the multi-client test or two fake data tables), run a full trade and a cancelled trade, then run the uid-uniqueness scan -> `get_console_output` to read the result. Two-client behaviour and the leave-during-trade race are `untested` until two real clients try it.

## Fallback
Files + Lune tests: 10 tests cover happy path, version reset, lock window, forged uids, untradable items, bad quantities, rollback with no room, replay after done, leave-cancel and locked items. Everything that needs a running Studio session (two real clients, crash between the two saves) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md` (reject amounts <= 0 and floor fractions or trades create negative currency; never accept a price from the client; destroy the player's data handle after saving on PlayerRemoving so trade events fired during leave cannot duplicate items - single creator source, treated as a tip; do not give away tradable value freely), `Roblox/roblox-kb/_tools/CHECKLIST-launch.md` (validate gifting and trading on the server and run dupe tests before launch), `Roblox/roblox-kb/case-studies-adopt-me.md`. The commit design is this pack's own and is verified only by its Lune tests and the checklist above.

## Output
`Trade.luau` wired to remotes, `design/trading.md` (rules, caps, lock seconds, what is locked), the dupe-scan debug command, test results.

## Acceptance checks
- [ ] Totals of every item and coin are identical before and after any trade, including failed ones (Trade tests 1, 6, 7 assert it).
- [ ] No uid exists twice across the loaded players after a trade (`totals` helper in the test).
- [ ] Changing an offer after accepting invalidates the old accept (test 2); accept inside the lock window is refused (test 3).
- [ ] A finished trade cannot be replayed with the old version (test 8).
- [ ] The commit contains no yielding call (read it: no `task.wait`, DataStore or HTTP between resolve and finish).
- [ ] Trade Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/trading-system-builder/scripts/tests/Trade.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Accepting an item list from the client without resolving it. Trusting `accept` without a version (bait and switch). Committing across a yield. Not handling the crash window: both players are saved separately, so a server crash between the two saves can duplicate or lose one side. This module narrows it (immediate saves, one synchronous commit, preserved uids) but cannot close it; the uid scan and the trade log are how you detect and repair it, and a game with a very valuable economy should add a journal entry in both players' data before the swap (not built here). Letting equipped or bound items be offered.

## Related
`inventory-system-builder`, `currency-system-builder`, `pet-system-builder`, `exploit-audit`, `remote-guard-builder`, `dupe-exploit-hunter`, `datastore-schema-builder`.
