---
name: PlayerData
type: system
what: Session-locked, versioned player data saving on DataStore:UpdateAsync (retries with backoff, autosave, BindToClose release, schema migrations, rollback guard).
tags: datastore, save data, session locking, autosave, bindtoclose, migrations, player data, profile
tested: unit-tested headless (Lune) + analyzed + linted; NOT tested in live Studio
---
# PlayerData

**What:** one save record per player that only one server can write at a time (session lock), with retries, autosave, a final save on leave and on shutdown, and a schema version with migrations.
**Not tested in live Studio.** The pure logic is tested against a fake DataStore shared by several fake servers; the Roblox glue (`PlayerDataService.luau`) type-checks but has not run in Studio. Run it in a published test place first.

## Why this and not ProfileStore
Chosen: our own small implementation in the ProfileStore style (session lock inside the stored record, written only through `UpdateAsync`, release on leave).
- Why not vendor ProfileStore: its licence is not stated in the places we could read (check `github.com/MadStudioRoblox/ProfileStore` before copying it into a game), and we cannot ship code with an unknown licence in a drop-in kit.
- Why not plain `SetAsync`/`GetAsync`: no lock means two servers overwrite each other during server hops (the classic item-duplication / data-loss bug).
- If you prefer a battle-tested library for a big game, use ProfileStore (successor of ProfileService, by loleris / MAD STUDIO); the rest of this kit (`Shop`, `DailyRewards`, ...) only needs "a table of the player's data", so it works with either.
- Differences you get here: no MessagingService fast handover (a joining server polls every 3 s up to `lockWait`), no `MessageAsync`, no global updates. Fine for most games.

## Files
- `src/PlayerData.luau` pure module (no Roblox globals; all services injected).
- `src/PlayerDataService.luau` Roblox glue: PlayerAdded/PlayerRemoving, autosave loop, `BindToClose`, in-memory fallback in Studio without API access.
- `tests/PlayerData.test.luau` Lune tests.

## Setup
1. Copy the `src/` files into your server scripts folder (or run `python ~/.claude/claude-kit/tools/games.py system add PlayerData --project <project>`).
2. One server script:
```lua
local PlayerDataService = require(script.Parent.Systems.PlayerData.PlayerDataService)
PlayerDataService.Start({
	storeName = "PlayerData_v1",
	template = { coins = 0, inventory = {}, Receipts = {}, Daily = { streak = 0, total = 0 } },
	version = 1,
})
local data = PlayerDataService.Get(player)      -- nil until loaded
PlayerDataService.Loaded:Connect(function(player, data) end)
```
3. Enable Studio access to API services (Game Settings > Security) to test real saving; publish the place.

## API (`PlayerData.new(config)`)
`:LoadAsync(key, cancel?) -> session?, reason?` reasons: `locked`, `newer`, `failed`, `cancelled`. `:SaveAsync(session)`, `:ReleaseAsync(session)`, `:AutosaveDue()`, `:ReleaseAll(timeout?)`, `:GetSession(key)`, `:ActiveCount()`. `session.Data` is the live table you mutate; `session.State` is `active | released | lost`.
Service: `Start(opts)`, `Get(player)`, `WaitFor(player, timeout?)`, `SaveNow(player)`, `Loaded` event.

## Config
`lockTimeout` (600 s: a foreign lock older than this is treated as a crashed server), `autosaveInterval` (120 s, keep far below `lockTimeout`: every autosave refreshes the lock), `loadAttempts` 6, `saveAttempts` 5, `lockWait` 30 s, `backoffBase` 1 s (doubling, max 30 s), `version` + `migrations[n]` (upgrades data from version n to n+1), `onLost(session, reason)` (the service kicks the player).

## Guarantees (each has a test)
- The lock lives in the same record as the data and is claimed/checked inside one `UpdateAsync` call, so two servers never both believe they own it.
- A server that lost its lock (taken over after a crash/timeout) cannot overwrite: its save fails, state becomes `lost`, the player is kicked.
- Data written by a newer schema version is never loaded by older code (rollback safety).
- Unserialisable data (functions, NaN, mixed tables, Instances) is refused before any request, with the path of the bad value.
- Saves copy the data first, so game code mutating during the yield cannot corrupt the write.
- Migration with a missing step fails the load and leaves the stored record untouched.

## Pitfalls
- Never keep a second copy of the data in a variable you save from; mutate `session.Data`.
- Do not store Instances, Vector3, Color3, functions; store numbers/strings/booleans/tables (convert on read/write).
- Change the template, not the store name, for new fields (they are filled in automatically). Bump `version` and add a migration only for renames/type changes.
- `Start` must be called once, before players join, in a Script (server).
- DataStore limits apply (4 MB per key, request budget); keep the record small, no per-tick saves. Call `SaveNow` after purchases only.
- The in-memory fallback in Studio means nothing persists when API access is off; the glue warns loudly.

## Tests (run on the host that built this, 2026-11-01)
```
cd <claude-kit>/systems && python check.py PlayerData
  stylua ok | selene ok (src) | selene ok (tests) | analyze ok (0 errors, 0 warnings; luau-lsp 1.70.1 with Roblox definitions, files are --!strict)
  lune PlayerData.test.luau: 16 passed, 0 failed
```
Needs the toolchain: `rokit install` in `systems/` (see skill `roblox-studio-connect`).

## Sources
Roblox docs: DataStore best practices and `DataStore:UpdateAsync` (create.roblox.com/docs/cloud-services/data-stores, /docs/reference/engine/classes/GlobalDataStore); ProfileStore design (devforum.roblox.com "Introducing ProfileStore", github.com/MadStudioRoblox/ProfileStore); KB notes `roblox-datastore-safe-save` skill.
