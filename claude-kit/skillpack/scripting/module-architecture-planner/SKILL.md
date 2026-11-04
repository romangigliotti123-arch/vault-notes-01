---
name: module-architecture-planner
description: "Turn a growing pile of scripts into services and modules: classify each file as server, client or shared, flag files to split, find dependencies that cross sides, and propose a folder layout and init order. Use when a script passes a few hundred lines or does several jobs."
category: scripting
tags: architecture, modules, services, refactor, split, server, client, shared, folders, init, layout, rojo
kb: Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md
related: require-cycle-finder, script-dependency-mapper, event-bus-builder, replicated-loader-builder, kit-system-integrator, roblox-luau-style
---

# module-architecture-planner

A plan for the shape of the code, produced from what the code does today. It never rewrites anything by itself. Cycle detection is `require-cycle-finder` (its graph is reused); the remote and tag map is `script-dependency-mapper`.

## When to use
One script has grown several jobs, server and client logic are tangled, or a new feature has no obvious home. Not for: a tiny game with three scripts, or choosing a framework (the vault compares them; this plans a plain-module layout).

## Inputs (max 2)
1. Where the scripts are (default: whole project). 2. Constraints (default: plain ModuleScripts, Rojo layout, no third-party framework).

## Procedure
1. Collect `{ name = source }` for every script (not only ModuleScripts).
2. `ModulePlan.analyse(sources, RequireGraph)` from `scripts/ModulePlan.luau`. Each module gets `side` (server, client, shared from the APIs it touches), `lines`, `functions`, `requires`, `splitReasons`; the plan gets `layout` and `violations`.
3. Read `violations` first. Server code in a place clients can read leaks it (exploiters read everything replicated), and a client cannot load a server module at all. Each violation has one fix: move the shared part down into a shared module, or call across the boundary with a remote instead of a require.
4. `ModulePlan.splitCandidates(plan)` lists files over 300 lines, over 20 functions or using both server and client APIs. For each, name the jobs inside (data, rules, presentation, input) and propose one module per job. The thresholds are this skill's defaults; adjust to the project.
5. Propose the layout from `plan.layout`: `src/server/Services/*` (own state, own remotes), `src/client/Controllers/*` (input, UI, effects), `src/shared/*` (types, config, pure logic, no side effects). Pure logic goes shared so it is unit-testable under Lune.
6. Define init order: require everything first, then `Init` on each module, then `Start` (cross-module calls and connections only in `Start`). Never yield in either (the vault warns the loader stalls). Reuse the kit systems (PlayerData, Shop, DailyRewards, Analytics, Admin) as services instead of writing new ones; `kit-system-integrator` wires them.
7. Hand the proposal to the human before moving files. Move one module per commit and rerun the plan; violations must only decrease.

```lua
local fs = require("@lune/fs")
local sources = {}
for _, name in fs.readDir("src") do
	if string.match(name, "%.luau?$") then sources[string.gsub(name, "%.luau?$", "")] = fs.readFile("src/" .. name) end
end
local plan = require("./ModulePlan").analyse(sources, require("./RequireGraph"))
for _, v in plan.violations do print("VIOLATION", v) end
for _, name in require("./ModulePlan").splitCandidates(plan) do print("SPLIT", name, table.concat(plan.modules[name].splitReasons, "; ")) end
```

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` for every Script, LocalScript, ModuleScript with its parent path -> `script_read` -> run the plan with `execute_luau` -> after approval `multi_edit` and `execute_luau` reparenting. The path of each script (which service it sits in) is a stronger side signal than the text scan: report mismatches.

## Fallback
Rojo `src/` with Lune. The text scan misses APIs reached through variables; the human review of the layout is the real check.

## Evidence
`Roblox/roblox-kb/code-architecture-and-frameworks.md`: plain ModuleScript classes, thin entry scripts, two-phase init then start, auto-load folders with unique names, signals to break cycles, one-way dependency direction. `Roblox/roblox-kb/anti-exploit-and-security.md`: keep authority in server-only containers. `Roblox/roblox-kb/scripting-and-performance.md`: singleton service modules, never yield in Init/Start.

## Output
`architecture.md`: layout tree, per-module side and job, violations with fixes, split list, init order, migration steps (one commit each).

## Acceptance checks
- [ ] Executed: `analyse` ran on the real sources; violation and split lists quoted.
- [ ] Every proposed move says which side the module ends on and why.
- [ ] No shared module depends on a server or client module in the proposed layout.
- [ ] Unit tests pass: `lune run ../skillpack/scripting/module-architecture-planner/scripts/tests/ModulePlan.test.luau`.
- [ ] Nothing was moved without human approval.

## Pitfalls
Splitting by file size alone (cohesion is the test: one job per module). Putting shared code in ReplicatedStorage and server secrets next to it. A "Utils" module that everything requires and that requires everything. Moving files and rewriting logic in the same commit.

## Related
`require-cycle-finder`, `script-dependency-mapper`, `event-bus-builder`, `replicated-loader-builder`, `kit-system-integrator`.
