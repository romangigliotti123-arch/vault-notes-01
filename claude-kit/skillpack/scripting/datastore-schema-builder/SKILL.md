---
name: datastore-schema-builder
description: "Design a versioned player-save schema (what is saved, the template, migration steps, what must never be saved) as one Schema file that the kit's session-locked PlayerData system runs in the game and that offline Lune tests run on old-record fixtures, with a template validator for unsaveable values. Use when starting a save system or changing what a game saves."
category: scripting
tags: datastore, save, schema, migration, version, player data, defaults, template, rollback, persistence
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: rbx-datastore, save-load-tester, data-loss-simulator, retry-wrapper-builder, kit-system-integrator, currency-system-builder, devproduct-handler
---

# datastore-schema-builder

Two separate problems: (1) writing data safely (session lock, retries, autosave, BindToClose, rollback refusal) and (2) what the saved table looks like over time. The kit system `PlayerData` (in `~/.claude/claude-kit/systems/PlayerData`, unit-tested, NOT live-tested) solves (1): it takes `{ template, version, migrations }` and stores `{ v, data }` records, where `migrations[n]` upgrades data from version n to n+1. Kit skill `rbx-datastore` explains the write rules. This skill solves (2): designing the schema and proving the migrations with fixtures BEFORE they meet real data. It does not re-implement PlayerData; `scripts/Migrations.luau` applies the same rules offline and adds a template validator.

## When to use
Before the first save is written, or before shipping any change to saved fields (rename, split, remove, type change). Not for: choosing what to monetise, or fixing a data-loss incident mid-flight (`data-loss-simulator`, `save-load-tester`).

## Inputs (max 3)
1. What the game must remember (default: read `design/core-loop.md` and `systems.md`). 2. Existing saved data shape, if any (default: none = version 1). 3. Whether PlayerData is already installed (default: install it with `games.py system add PlayerData`).

## Procedure
1. List saved state and decide for each item: SAVE (progress, purchases, settings), DERIVE (computed from saved data: levels from XP), or NEVER (live position, cooldown timers, anything the server can recompute, gamepass ownership which comes from the Marketplace API). One table per player under one key `Player_<UserId>`; never key by name.
2. Write the TEMPLATE: the defaults for a brand-new player, with a `_v` version. Keep numbers as plain numbers, ids as strings, collections as dictionaries keyed by stable ids (arrays only for ordered lists you control); no Instances, no functions, no mixed-key tables (they do not survive serialisation). Include `Receipts = {}` for developer products (`devproduct-handler`).
3. Version rule (PlayerData's convention): bump `VERSION` and add `MIGRATIONS[n]` (upgrade from n to n+1, returns the table) only for renames, splits, type changes or meaning changes. Adding a field with a default needs no migration (the template fills it). Removing a field: stop reading it first, delete it in a later migration.
4. Write the migrations as small pure functions on a table: idempotent on already-migrated data, no live services, no reliance on other fields' order.
5. Generate: create `src/server/Systems/PlayerData/Schema.luau` exporting `TEMPLATE`, `VERSION`, `MIGRATIONS`, and pass them to `PlayerDataService.Start({ storeName = ..., template = Schema.TEMPLATE, version = Schema.VERSION, migrations = Schema.MIGRATIONS })`. Copy `scripts/Migrations.luau` into `tests/` (it is the offline checker, not shipped in the game). If PlayerData is not installed: `python ~/.claude/claude-kit/tools/games.py system add PlayerData --project <project>`.
6. Rollback safety is PlayerData's: a record with `v` greater than this server's version is refused (the player is kicked with a retry message, the record is left untouched). `Migrations.migrate` returns `"newer"` for the same case so you can test your fixtures against it.
7. Tests (`tests/Schema.test.luau`, copy the pattern of `scripts/tests/Migrations.test.luau`): for each saved fixture of an old record run `Migrations.migrate({ v = n, data = fixture }, VERSION, MIGRATIONS, TEMPLATE)` and assert the exact result; assert `Migrations.missingSteps(1, VERSION, MIGRATIONS)` is empty; assert `Migrations.validateTemplate(TEMPLATE)` is empty (flags functions, Instances, NaN, mixed or non-string keys, nesting deeper than 6). Keep fixtures of real old records.
8. Run the checks: from `~/.claude/claude-kit/systems`: `lune run ../skillpack/scripting/datastore-schema-builder/scripts/tests/Migrations.test.luau`; `bash ~/.claude/claude-kit/tools/roblox-project-template/luau-check.sh <files>`.
9. Write `design/save-schema.md` (table of fields: name, type, default, since version, saved/derived) and the migration log.

## Studio MCP path
`list_roblox_studios` -> push `Schema.luau` with `multi_edit` under ServerScriptService (and `Migrations.luau` in a test-only folder) -> `start_stop_play` -> `execute_luau` (Server) to run `Migrations.migrate` on a fixture record and return the result -> `get_console_output`. Real DataStore behaviour needs API access enabled in Game Settings and a published place: say `untested` otherwise.

## Fallback
Rojo/files plus Lune tests (headless, no Studio). The real store is untested until the owner runs it in a published test place.

## Evidence
`Roblox/roblox-kb/data-persistence.md` (pcall every call; one table per player keyed by UserId; defaults for new players and never overwrite after a failed load; save on PlayerRemoving and BindToClose; autosave on a timer; do not write on every event), `Roblox/roblox-kb/scripting-and-performance.md` (never rename the store after publishing), `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`. Limits (value size, request budgets) change: confirm with `kbq.py docs "DataStore limits"`.

## Output
`design/save-schema.md`, `src/server/Systems/PlayerData/Schema.luau`, `tests/Migrations.luau` (copy), `tests/Schema.test.luau`, and a short note of what was run with the results quoted.

## Acceptance checks
- [ ] Every field is SAVE / DERIVE / NEVER with a reason; no gamepass ownership, positions or Instances saved.
- [ ] `lune` test output shows all passing (quote "N passed, 0 failed").
- [ ] A fixture of the oldest record loads to the newest version.
- [ ] A newer-version record is refused (`"newer"` in the fixture test), not overwritten.
- [ ] `validateTemplate(TEMPLATE)` returns an empty list.
- [ ] luau-check clean on the generated files.
- [ ] Store name and key pattern are fixed and documented (never rename after publish).

## Pitfalls
Renaming a field without a step (players lose data). Saving derived data that can drift. Arrays that get holes. Reconciling by overwriting. Changing the store name "to start clean" in production. Skipping the version bump when old servers are still running during an update.

## Related
`rbx-datastore`, `kit-system-integrator`, `save-load-tester`, `data-loss-simulator`, `retry-wrapper-builder`, `devproduct-handler`.
