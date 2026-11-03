---
id: "roblox-luau-style"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-luau-style/SKILL.md"
description: "Luau coding standard for Roblox scripts: strict typing, services, modules, task library, cleanup, events, no legacy APIs. Use when writing, reviewing or refactoring Luau."
orig_name: "roblox-luau-style"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-luau-style

> Luau coding standard for Roblox scripts: strict typing, services, modules, task library, cleanup, events, no legacy APIs. Use when writing, reviewing or refactoring Luau.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-luau-style/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Luau style for Roblox

Apply when producing or reviewing Luau. Prefer small ModuleScripts with one job.

1. Start every file with `--!strict`. Annotate function signatures, export types (`export type PlayerState = {...}`), avoid `any`.
2. Get services once at the top with `game:GetService("X")`. Always `local`; no globals, no `_G`/`shared`.
3. Use the `task` library: `task.wait`, `task.spawn`, `task.defer`, `task.delay`. Never `wait()`, `spawn()`, `delay()`.
4. Connections and instances need cleanup. Keep a Maid/Janitor (or a table of connections) and disconnect on player leave or `Destroying`. No per-player connection leaks.
5. Prefer events and `:GetPropertyChangedSignal` over polling loops. Heartbeat/RenderStepped handlers must be cheap.
6. `Instance.new(class)`, set properties, set `Parent` last. Use `CollectionService` tags to attach behaviour to many objects instead of one script per object.
7. Structure: `ServerScriptService` (server logic), `ServerStorage` (server-only assets), `ReplicatedStorage` (shared modules, remotes), `StarterPlayerScripts` (client). One entry script per side that `require`s modules.
8. `pcall` anything that can fail on the network or a service (DataStore, Marketplace, HTTP, `InsertService`); handle the false branch.
9. `WaitForChild(name, timeout)` for objects that may not have replicated; never assume replication order on the client.
10. Use `table.clone`, `table.freeze` for constants, `table.concat` for string building; avoid O(n^2) scans in hot paths; cache `workspace.CurrentCamera`.
11. Naming: PascalCase for modules/classes and Instances, camelCase for locals/functions, UPPER_SNAKE for constants.
12. Comments explain why, not what. No dead code. Run `selene` and `stylua` or Studio Script Analysis if available and fix warnings.

Review output: findings ordered by severity (leaks, race conditions, deprecated API, then style), each with file:line and the fix.
