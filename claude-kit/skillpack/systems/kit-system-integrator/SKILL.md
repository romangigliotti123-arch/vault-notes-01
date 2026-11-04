---
name: kit-system-integrator
description: "Wire the kit's tested systems (PlayerData, Shop, DailyRewards, Analytics, Admin) into a project in the right order and verify the wiring with a static checker: one ProcessReceipt owner, BindToClose, PlayerRemoving, no server APIs in client folders, no hard-coded secrets. Use when starting a project or after adding a system."
category: systems
tags: kit systems, PlayerData, Shop, DailyRewards, Analytics, Admin, integration, wiring, BindToClose, ProcessReceipt
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: rbx-rojo, datastore-schema-builder, devproduct-handler, gamepass-maker, remote-guard-builder, exploit-audit
---

# kit-system-integrator

One job: get the five drop-in systems working together without the classic integration bugs. The systems are server-authoritative modules with injected Roblox services (`systems/README.md`): `PlayerData` holds `Receipts` (Shop) and `Daily` (DailyRewards); Shop and DailyRewards ask for `getData`/`saveNow` callbacks. `scripts/integrate_check.py` reads the project's Luau files and reports FAIL/WARN leads; it is static analysis, not a live test.

## When to use
Starting a game on the kit, adding a system, or reviewing a project that already uses them. Not for: designing what each system should do (their own skills), runtime testing.

## Inputs (max 2)
1. Project folder (default: the current Rojo project). 2. Which systems are wanted (default: PlayerData + Shop; DailyRewards/Analytics/Admin when the design calls for them).

## Procedure
1. Install what is needed: `python ~/.claude/claude-kit/tools/games.py system add <Name> --project <project>` copies `src/` to `src/server/Systems/<Name>/`. Read each system's README (setup, config, pitfalls) before wiring.
2. Order of wiring in one server script: create PlayerData with the template and migrations; on `PlayerAdded` call `LoadAsync` and keep `session.Data` in a table by user id; give `getData(userId)` and `saveNow(userId)` closures to Shop and DailyRewards; start Shop (the ONLY `ProcessReceipt` owner) and Analytics; add Admin last.
3. Shutdown: `game:BindToClose` releases all sessions (`PlayerData:ReleaseAll`); `Players.PlayerRemoving` releases the player's session after any pending trade/round cleanup. Both must exist.
4. Pack modules (Wallet, Inventory, Quests, ...) store their state inside `session.Data`: add their default tables to the PlayerData template and bump the schema version with a migration when changing shapes (`datastore-schema-builder`).
5. Run the checker: `python -I ~/.claude/claude-kit/skillpack/systems/kit-system-integrator/scripts/integrate_check.py <project>`; fix every FAIL, read every WARN. Re-run until FAIL is 0.
6. Run the kit's own gate: `cd ~/.claude/claude-kit/systems && python check.py` (stylua, selene, luau-lsp, Lune tests) and quote its final line.
7. Live test (`untested` until done in Studio): join, change data, leave, rejoin; buy a product with a test account twice (retry) and confirm one grant; stop the server mid-play and confirm the data saved.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add the system folders and the wiring script -> `start_stop_play` -> `execute_luau` (Server) to join a test player, change `session.Data`, call `saveNow` and read the store -> `get_console_output` to read the result. Everything beyond the static checker is live-Studio work.

## Fallback
Files + the static checker + the kit's `check.py`. Everything that needs a running Studio session (the whole runtime: DataStore round trips, purchases, shutdown) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/data-persistence.md` (save on leave and in BindToClose; session locking), `Roblox/roblox-kb/anti-exploit-and-security.md` (server APIs stay out of replicated containers; no secrets in client-visible places), `Roblox/roblox-kb/monetisation-devproducts.md` (one receipt handler), `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`. Kit guarantees: `systems/*/README.md` (all live-Studio behaviour is marked not yet run).

## Output
Wired project plus the checker report (FAIL/WARN counts) and the `check.py` result line; a short `design/systems-wiring.md` listing which system owns what.

## Acceptance checks
- [ ] `integrate_check.py <project>` prints `0 FAIL` (quote the summary line).
- [ ] `integrate_check.py --selftest` prints `selftest ok`.
- [ ] `python check.py` in `systems/` ends with ALL PASSED (quote it).
- [ ] Exactly one `ProcessReceipt` assignment exists, inside Shop.
- [ ] A live double-purchase and shutdown test is recorded as run or `untested`.

## Pitfalls
Assigning `ProcessReceipt` twice (the last wins, purchases vanish). Saving only on leave (shutdown loses data). Systems that keep their own copy of player data instead of `session.Data`. Treating a clean static report as a working game. Editing a system's `src/` in the project and forgetting the kit copy.

## Related
`rbx-rojo`, `datastore-schema-builder`, `devproduct-handler`, `gamepass-maker`, `remote-guard-builder`, `exploit-audit`.
