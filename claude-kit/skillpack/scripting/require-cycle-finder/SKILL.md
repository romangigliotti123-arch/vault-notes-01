---
name: require-cycle-finder
description: "Detect circular require() chains between ModuleScripts, show one concrete cycle per tangle, suggest the cheapest edge to cut and the load order that results. Use when Studio reports a require cycle, a module is nil at load, or before a strict-mode or architecture refactor."
category: scripting
tags: require, cycle, circular dependency, modulescript, load order, architecture, refactor, dependency graph
kb: Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/luau-language-and-types.md
related: module-architecture-planner, strict-mode-migrator, script-dependency-mapper, event-bus-builder, luau-type-annotator
---

# require-cycle-finder

Roblox raises an error when two modules require each other while loading ("requested module was required recursively"). The error names one require; this skill finds every tangle and tells you where to cut. The shared graph module `scripts/RequireGraph.luau` is also used by `strict-mode-migrator`, `module-architecture-planner` and `script-dependency-mapper`.

## When to use
A recursive-require error, a module value that is `nil` or an empty table at use time, or before any refactor that moves modules. Not for: remote or tag wiring (that is `script-dependency-mapper`).

## Inputs (max 2)
1. Source root or the list of scripts (default: all ModuleScripts). 2. Whether to also print the load order (default yes).

## Procedure
1. Gather `{ name = source }` for every ModuleScript (Studio: `script_read`; repo: read `src/**/*.luau`). Module names must be unique for the graph to be right; list duplicates first and stop if there are any.
2. `local g = RequireGraph.build(sources)`. `g.unknown` lists requires that point outside the set (packages, services): note them, they cannot be part of a cycle you control.
3. `RequireGraph.findCycles(g.edges)` returns one concrete cycle per tangled group: `{ "A", "B", "C" }` means A requires B requires C requires A. Self-requires appear as a one-item cycle.
4. For each cycle `RequireGraph.suggestBreak(g.edges, cycle)` proposes an edge. Treat it as a starting point (it picks the module with the fewest dependencies) and choose among the standard breaks: (a) move the shared piece both modules need into a third module that depends on neither; (b) invert one dependency through a signal or callback (`event-bus-builder`); (c) pass the dependency in at construction or `Init` instead of requiring at the top; (d) as a last resort `require` inside the function that needs it (lazy). Prefer (a) and (b).
5. Apply one cut, re-run from step 2. Stop at zero cycles; do not stack cuts blindly because one cut often resolves several.
6. `RequireGraph.layers(g.edges)` gives the load order: layer 1 has no dependencies. Keep this as the project's dependency direction (lower layers never require higher ones).

```lua
-- Lune runner (outside scripts/): lune run cycles.luau
local fs = require("@lune/fs")
local RequireGraph = require("./RequireGraph")
local sources = {}
for _, name in fs.readDir("src") do
	if string.match(name, "%.luau?$") then sources[string.gsub(name, "%.luau?$", "")] = fs.readFile("src/" .. name) end
end
local g = RequireGraph.build(sources)
for _, c in RequireGraph.findCycles(g.edges) do print("cycle:", table.concat(c, " -> ") .. " -> " .. c[1]) end
```

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` (ModuleScripts) -> `script_read` each -> `execute_luau` with the module source embedded -> read the printed cycles -> `multi_edit` for the cut -> `start_stop_play` and `get_console_output` to confirm the recursive-require error is gone.

## Fallback
Rojo repo with Lune. Dynamic requires (`require(variable)`) and requires built from strings are invisible to the text scan; the skill lists any `require(` whose argument it could not name as "unresolved" for a manual look.

## Evidence
`Roblox/roblox-kb/code-architecture-and-frameworks.md`: use signals to break cycles and keep dependency direction one-way; give modules an init then start phase so cross-module calls happen after everything is required; do not yield at module load. `Roblox/roblox-kb/scripting-and-performance.md`: never yield in Init or Start (stalls the loader for every other module).

## Output
`cycles.md`: each cycle, the chosen cut and why, the layer table before and after.

## Acceptance checks
- [ ] Executed: `RequireGraph.findCycles` run on the real sources, output quoted.
- [ ] After the cuts the same command returns an empty list.
- [ ] Unit tests for the graph pass: `lune run ../skillpack/scripting/require-cycle-finder/scripts/tests/RequireGraph.test.luau` from the kit `systems` folder.
- [ ] No cut was a lazy require unless (a) to (c) were rejected with a reason.
- [ ] Play test loads without a recursive-require error (or marked untested).

## Pitfalls
Breaking a cycle by moving code into a bigger module that other things now require (new cycle). Fixing the symptom with a lazy require and leaving the design tangled. Two modules with the same name in different folders (the graph merges them). Treating a type-only dependency as free: `export type` imports are requires too.

## Related
`module-architecture-planner`, `strict-mode-migrator`, `script-dependency-mapper`, `event-bus-builder`.
