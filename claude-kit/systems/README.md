---
name: systems-library
type: system
what: Index of the kit's tested drop-in Roblox systems (PlayerData, Shop, DailyRewards, Analytics, Admin) and how they are checked.
tags: systems library, drop-in, reusable, player data, shop, daily rewards, analytics, admin
---
# Drop-in systems library

Server-authoritative Luau modules you copy into a game instead of rebuilding. Lookup order when a game needs a system: your `Games/_Reusable/` first, then these, then build (`rbx-harvest`).

| System | What | Unit tests |
|---|---|---|
| `PlayerData` | session-locked, versioned saving, retries, autosave, BindToClose | 16 |
| `Shop` | idempotent ProcessReceipt + game-pass ownership | 13 |
| `DailyRewards` | daily claim, streaks, grace days | 10 |
| `Analytics` | validated economy / funnel / progression / custom events | 9 |
| `Admin` | permission-checked commands, hierarchy, audit | 12 |

Each folder: `README.md` (what, API, setup, config, pitfalls, sources, test results), `src/` (pure module + Roblox glue), `tests/*.test.luau`.
Pure modules take every Roblox service by injection, so tests run headless in Lune. The `*Service.luau` / `*Glue.luau` files are the thin Roblox wiring: type-checked, **not yet run in live Studio**.

## Use in a game
`python .rbx/claude-kit/tools/games.py system add <Name> --project <game project folder>` copies `src/` to `<project>/src/server/Systems/<Name>/` (a Rojo project made by `games.py init --rojo` maps it to ServerScriptService). Then follow the system's README Setup.
Systems fit together through plain data tables: PlayerData holds `Receipts` (Shop) and `Daily` (DailyRewards); Shop/DailyRewards ask for `getData`/`saveNow` callbacks, so they also work with ProfileStore or your own storage.

## Check everything (what "tested" means here)
```
cd .rbx/claude-kit/systems
rokit install            # once: stylua, selene, luau-lsp, lune, rojo (see skill rbx-studio)
python check.py          # stylua --check, selene, luau-lsp analyze (Luau type checker, Roblox definitions, --!strict files), Lune tests
```
Exit 0 = all passed, 1 = a check failed, 2 = a tool is missing (reported as SKIPPED, never a silent pass). Config: `rokit.toml`, `stylua.toml`, `selene.toml` (+ `selene-tests.toml`), `_check/` (Rojo project for the analyzer, Lune test harness).
`luau-analyze` is the type checker inside `luau-lsp analyze`; the standalone binary is not needed.

## Adding a system (also for harvest)
Same layout, pure core + glue, tests, README with the sections above and the line "Not tested in live Studio" until you have run it there. Add it to `_check/check.project.json` so it is analysed. Run `python check.py <Name>` before calling it tested.
