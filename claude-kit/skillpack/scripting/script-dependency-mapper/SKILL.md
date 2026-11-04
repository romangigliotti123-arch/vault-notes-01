---
name: script-dependency-mapper
description: "Map which scripts touch which remotes, modules, CollectionService tags, attributes and services, and list remotes that are only fired or only handled. Use before a refactor, when onboarding to an unfamiliar project, or to find dead and unprotected endpoints."
category: scripting
tags: dependency map, remotes, tags, attributes, services, audit, onboarding, dead code, orphan remote, documentation
kb: Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: require-cycle-finder, module-architecture-planner, remote-guard-builder, exploit-audit, collection-tag-wiring
---

# script-dependency-mapper

A table of who talks to whom. The require graph (modules) is `require-cycle-finder`; this adds the other coupling in Roblox projects: remotes, tags, attributes and services. It reads text and runs nothing, so it works on any project, including one you cannot launch.

## When to use
New to a codebase, before moving or deleting scripts, hunting a remote nobody handles, or building the `remotes.md` that `remote-guard-builder` wants. Not for: runtime tracing (use the console and the profiler).

## Inputs (max 2)
1. Source root or place. 2. What to map (default all five: remotes, requires, tags, attributes, services).

## Procedure
1. Collect `{ path = source }` for every script, using the full container path as the key so you can tell the server copy from the client copy (`ServerScriptService/Shop`, `StarterPlayerScripts/ShopUI`).
2. `DependencyMap.scan(sources, RequireGraph)` (`scripts/DependencyMap.luau`; pass in `RequireGraph` from `require-cycle-finder/scripts/RequireGraph.luau`). Result: `remotes[name] = { fires, handles }`, plus `requires`, `tags`, `attributes`, `services`, each name mapped to the scripts that use it.
3. `DependencyMap.orphans(map)`: `onlyFired` are calls to a remote nobody handles (a bug or a handler on a name the scanner could not see); `onlyHandled` are endpoints nothing in the project calls, which is either dead code or an attack surface exposed for nothing. List both for the human.
4. `DependencyMap.remoteTable(map)` prints a markdown table of remotes with firing and handling scripts: paste it into `remotes.md` and add the validator and rate limit columns with `remote-guard-builder`.
5. Cross-check the side: a remote handled in a client script, or `FireServer` called from a server script, is wrong. A tag read on both sides is fine, but a tag used only by one side with a server-only effect should not be settable by clients.
6. Attributes: names used in only one script are likely typos; names read on the client that the server also writes are replicated state, flag any that gate rewards.
7. Services: list unusual ones (`HttpService`, `MessagingService`, `TeleportService`) to find where external calls live.
8. Limits: matching is by the last identifier before the call, so aliased remotes (`local R = remotes.Buy`) appear under `R`; resolve those by hand and note them.

```lua
local fs = require("@lune/fs")
local sources = {}
local function walk(dir: string)
	for _, name in fs.readDir(dir) do
		local path = dir .. "/" .. name
		if fs.isDir(path) then walk(path) elseif string.match(name, "%.luau?$") then sources[path] = fs.readFile(path) end
	end
end
walk("src")
local DependencyMap = require("./DependencyMap")
local map = DependencyMap.scan(sources, require("./RequireGraph"))
print(DependencyMap.remoteTable(map))
```

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` for every script path -> `script_read` each -> `execute_luau` to run the scan -> `script_grep` to resolve aliases the scan could not.

## Fallback
Rojo repo with Lune (above). Remotes created dynamically by name from strings are invisible; search for `Instance.new("RemoteEvent")` and list them manually.

## Evidence
`Roblox/roblox-kb/client-server-and-remotes.md`: define remotes and packet types once in a shared module; send minimal identifiers; the server is the gatekeeper. `Roblox/roblox-kb/anti-exploit-and-security.md`: every remote is a public API; validate and rate-limit each; honeypot remotes catch scanners. `Roblox/roblox-kb/code-architecture-and-frameworks.md`: one-way dependency direction, tags drive behaviour.

## Output
`dependencies.md`: the remote table, orphan lists, require/tag/attribute/service tables, and a "resolve by hand" list.

## Acceptance checks
- [ ] Executed: `scan` and `orphans` run on the real sources; outputs quoted. Lune test passes (`4 passed, 0 failed`).
- [ ] Each orphan is explained (dead, dynamic name, alias) or removed.
- [ ] No remote is handled on the wrong side.
- [ ] Single-use attribute names reviewed for typos.
- [ ] The table feeds `remotes.md` for `remote-guard-builder`.

## Pitfalls
Reading the map as complete: it is a text scan. Treating "only handled" as safe because nobody calls it (an exploiter can). Forgetting remotes defined in a shared packet module. Using script names without paths when server and client scripts share a name.

## Related
`require-cycle-finder`, `module-architecture-planner`, `remote-guard-builder`, `exploit-audit`, `collection-tag-wiring`.
