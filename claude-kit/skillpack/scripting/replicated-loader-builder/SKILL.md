---
name: replicated-loader-builder
description: "Write the client bootstrap that waits for shared modules and assets with timeouts, requires them in a stable order, reports every missing piece at once and only then starts the game. Use when client scripts error with nil modules or infinite-yield warnings, or load order depends on luck."
category: scripting
tags: client, bootstrap, replicatedfirst, waitforchild, loader, timeout, replication, streaming, modulescript, startup
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/first-session-onboarding.md
related: module-architecture-planner, require-cycle-finder, event-bus-builder, input-handler-builder, game-optimizer
---

# replicated-loader-builder

A client script can run before the modules it needs have replicated. The usual symptoms are "attempt to index nil", "Infinite yield possible" and bugs that appear only on slow connections. The fix is a single bootstrap that waits with timeouts, names what is missing, and starts everything in order.

## When to use
Any game with client scripts that require shared modules or assets, especially with StreamingEnabled or a custom loading screen. Not for: server startup (use the init/start phases from `module-architecture-planner`), or a game with one LocalScript and no modules.

## Inputs (max 2)
1. The folders and modules the client needs (default from the require graph of the client scripts). 2. Timeout (default 10 s per instance).

## Procedure
1. List the client dependencies: for each client script, the modules it requires and the assets it uses at start. `script-dependency-mapper` produces this list.
2. Put one `LocalScript` in `ReplicatedFirst` (it runs before the rest replicate) that holds `scripts/ClientLoader.luau`'s logic. Everything else is a ModuleScript required by it, not a LocalScript that wakes up on its own.
3. Wait and load: `local modules, err = ClientLoader.load(ReplicatedStorage, { Shared = { "Config", "Types" }, Client = { "UI", "Input" } }, 10, require)`. It uses `WaitForChild(name, timeout)` for each folder and module, requires in sorted folder order, and collects every problem (missing folder, missing module, module that errors on require, a module name used twice) into one message instead of failing on the first.
4. On `err`, show a clear message to the player (or log it) and stop; do not continue half-loaded. During the wait you can show your loading screen (`ReplicatedFirst:RemoveDefaultLoadingScreen()` after yours is up).
5. Start in two phases: after all modules are required, call `Init` on each, then `Start` on each. Never yield in a module's top level, `Init` or `Start`: a yield stalls the loader for every module behind it. Do waiting here, in the bootstrap.
6. Assets and instances: `ClientLoader.waitPath(ReplicatedStorage, { "Assets", "Sounds", "Click" }, 5)` returns the node or `nil` plus a message naming the path. Under StreamingEnabled, workspace content may not exist yet: wait for what you need, or wait on the player's character and a streaming radius, not on the whole map.
7. Preload what matters for the first minute only (`ContentProvider:PreloadAsync` on a short list); the vault ties first-session experience to load time, so do not preload everything.
8. Test: `lune run ../skillpack/scripting/replicated-loader-builder/scripts/tests/ClientLoader.test.luau` from the kit `systems` folder (fake tree: missing child, error on require, duplicate names).

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` under ReplicatedFirst/ReplicatedStorage/StarterPlayerScripts -> `multi_edit` the bootstrap -> `start_stop_play` -> `get_console_output` (Client) for load messages; to test a slow join, delay a module's replication (manual) or temporarily rename it and confirm the error names the path.

## Fallback
Lune tests cover the waiting logic with a fake tree. Real replication timing and streaming behaviour are `untested` without a running client.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: replicated scripts can run before their modules replicate, so call `WaitForChild` on required modules; never yield in module Init or Start (the loader stalls and warns). `Roblox/roblox-kb/code-architecture-and-frameworks.md`: give every module an init then start phase; auto-load folders into one table with unique names. `Roblox/roblox-kb/optimization-and-streaming.md` and `Roblox/roblox-kb/first-session-onboarding.md`: streaming and join time shape the first session.

## Output
The bootstrap `LocalScript`, `ClientLoader.luau`, the dependency list it waits for, the error message format, test line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`5 passed, 0 failed`).
- [ ] No client module yields at top level, Init or Start.
- [ ] A missing module produces one message naming its full path.
- [ ] Every client entry goes through the bootstrap; no stray LocalScript requires shared modules itself.
- [ ] Slow-join behaviour tried, or marked untested.

## Pitfalls
`WaitForChild` with no timeout. Waiting for the whole workspace under streaming. Two folders holding modules with the same name (the later overwrites the earlier in an auto-load table; the loader flags it). Starting UI before `Init` finished. A loading screen that never ends on error.

## Related
`module-architecture-planner`, `require-cycle-finder`, `event-bus-builder`, `input-handler-builder`.
