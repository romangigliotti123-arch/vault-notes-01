---
name: rbx-luau
description: "Luau coding standard for Roblox scripts: strict typing, services, modules, task library, cleanup, events, no legacy APIs, no code comments by default. Use when writing, reviewing or refactoring Luau."
---

# Luau style for Roblox

Apply when producing or reviewing Luau. Prefer small ModuleScripts with one job.

1. Start every file with `--!strict`. Annotate function signatures, export types (`export type PlayerState = {...}`), avoid `any`. Type untrusted input (remote arguments, decoded JSON) as `unknown` and narrow it with `typeof` checks before use.
2. Get services once at the top with `game:GetService("X")`. Always `local`; no globals, no `_G`/`shared`.
3. Use the `task` library: `task.wait`, `task.spawn`, `task.defer`, `task.delay`. Never `wait()`, `spawn()`, `delay()`.
4. Connections, threads and instances need cleanup: see Lifecycle and leak cleanup below. No per-player connection leaks.
5. Prefer events and `:GetPropertyChangedSignal` over polling loops. Heartbeat/RenderStepped handlers must be cheap.
6. `Instance.new(class)`, set properties, set `Parent` last. Use `CollectionService` tags to attach behaviour to many objects instead of one script per object.
7. Structure: `ServerScriptService` (server logic), `ServerStorage` (server-only assets), `ReplicatedStorage` (shared modules, remotes), `StarterPlayerScripts` (client). One entry script per side that `require`s modules.
8. `pcall` anything that can fail on the network or a service (DataStore, Marketplace, HTTP, `InsertService`); handle the false branch.
9. `WaitForChild(name, timeout)` for objects that may not have replicated; never assume replication order on the client.
10. Use `table.clone`, `table.freeze` for constants (shallow: nested tables stay mutable), `table.concat` for string building; avoid O(n^2) scans in hot paths; cache `workspace.CurrentCamera`.
11. Naming: PascalCase for modules/classes and Instances, camelCase for locals/functions, UPPER_SNAKE for constants.
12. No comments by default (Comments below). No dead code. Run `selene` and `stylua` or Studio Script Analysis if available and fix warnings.

## Comments
NO COMMENTS BY DEFAULT in any code you write (Luau, Lua, scripts, tests, examples). A one-line comment is allowed only to explain WHY something non-obvious is done (an engine quirk, ordering, replication timing, physics ownership), never WHAT the code does. Type annotations and Luau directives (`--!strict`, `--!native`, `--!optimize`, `--!nolint`) are not comments and stay. Name things so the code reads without notes; put design notes in the SKILL.md or reference, not in the file. Existing comments in code you only edit stay unless you rewrite that line.

## Smallest complete change
Build what was asked, nothing speculative, and finish it. Before writing code take the first rung that works: (1) does it need to exist at all (skip unrequested features and say what was skipped); (2) a vault system or `Games/_Reusable` module (`games.py system add PlayerData|Shop|DailyRewards|Analytics|Admin`) or an installed library from `$ASSETS/code`; (3) a Roblox built-in (CollectionService tags, Attributes, PathfindingService, TweenService, ProximityPrompt, leaderstats, Players events); (4) the minimum new code. Never cut: server validation, DataStore and receipt safety, mobile layout and accessibility, anything the user asked for (the user may still order a refactor). No stubs, TODOs, placeholder functions or modules nothing requires; a shortcut with a known limit gets one WHY line. In existing code touch only the lines the task needs. Check: `rbx-critic/scripts/code_gates.py` scores orphan modules, stubs, rebuilt kit systems, unused exports and oversized files (scope SC1-SC5).

## Lifecycle and leak cleanup
Leaks on a long-running server are connections, threads and tables keyed by objects that are gone.

| Thing | Release with |
|---|---|
| `RBXScriptConnection` | `:Disconnect()` |
| `task.spawn/delay/defer` thread | `task.cancel(thread)` (errors on the running thread: guard or `pcall`); guard callbacks already running |
| Tween | `:Cancel()`, drop the reference |
| `RunService:BindToRenderStep` | `UnbindFromRenderStep(name)` |
| Instance you created | `:Destroy()` or return it to a pool |
| `data[player]` and other per-player tables | `= nil` on `PlayerRemoving` |
| Store subscription | call the returned unsubscribe |

Facts (Roblox docs, checked 2026-11-04):
- `Destroy()` disconnects events of the destroyed instance. Connections to `Player`, a character or any other instance you do not destroy stay alive.
- The engine does not destroy the `Player` or the character when a user leaves. Set `Workspace.PlayerCharacterDestroyBehavior` to destroy them, or call `Destroy` in `PlayerRemoving` / `CharacterRemoving` (use `task.defer`).
- `Debris:AddItem` cannot be cancelled; use `task.delay` with a stored thread when you need control.
- `Instance.Destroying` ties an object's cleanup to the instance's life.

Rules:
1. One cleaner per lifetime: object, player, character, round, UI screen. Add everything created for that lifetime; destroy it once at the end (idempotent).
2. Handle players already in game: connect `PlayerAdded`, then loop `Players:GetPlayers()`.
3. A character cleaner ends on `CharacterRemoving` or the next `CharacterAdded`, so respawns do not stack connections.
4. `BindToClose` saves and releases every player (30 second window, run in parallel).
5. Use the project's Maid, Janitor or Trove if present (current status of each is unverified); otherwise this is enough:
No Maid/Janitor/Trove in the project: write a small `Cleaner` module (`new`, `add(item)` returning the item, idempotent `destroy()` that releases items in reverse order: connection `:Disconnect()`, Instance `:Destroy()`, function call, thread `pcall(task.cancel, thread)`, other objects `:Destroy()`). [cold:rbx-luau/cleaner-module.md] read only when the project has no Maid, Janitor or Trove and you must write the Cleaner module.
Wire it per player and per character: one Cleaner each, built in PlayerAdded (plus a GetPlayers loop) and CharacterAdded, destroyed in CharacterRemoving and PlayerRemoving, `playerData[player] = nil`, and BindToClose runs the same release. [cold:rbx-luau/lifetimes-example.md] read only to wire PlayerAdded/CharacterAdded/PlayerRemoving/BindToClose cleanup with the Cleaner above.
Find leaks: Developer Console Memory tab, watch `LuaHeap`, `InstanceCount` and `PlaceScriptMemory` through a long session; join and leave 50 times and check counts return to baseline. Scene Analysis shows script memory and unparented instances. No documented API lists all connections, so instrument your own.

Credit: checklist adapted from excaldev/ro-engineer (MIT, Copyright (c) 2026 excaldev), copy in Imported/ro-engineer/cleanup-lifecycle.md; facts re-checked against the Roblox docs.

Review output: findings ordered by severity (leaks, race conditions, deprecated API, then style), each with file:line and the fix.

## Sources
Smallest complete change: ideas from Ponytail (DietrichGebert, MIT) and Unlazy (Leonxlnx, MIT), re-written in our own words; nothing copied.
