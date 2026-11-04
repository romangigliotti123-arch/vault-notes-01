---
name: strict-mode-migrator
description: "Plan and run a move to --!strict for a whole codebase, one module at a time: leaves first, cheapest first inside each layer, cycles flagged, progress counted. Use when a project has many untyped scripts; luau-type-annotator does each single module."
category: scripting
tags: strict, migration, luau, types, typecheck, rollout, codebase, order, luau-lsp, ci
kb: Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/code-architecture-and-frameworks.md
related: luau-type-annotator, require-cycle-finder, module-architecture-planner, roblox-luau-style, roblox-rojo-project-setup
---

# strict-mode-migrator

The plan, not the annotating. A module whose dependencies are already typed gives its callers real types instead of `any`, so the order matters: types flow upward from the leaves. The per-module work is `luau-type-annotator`; the dependency facts come from `require-cycle-finder`.

## When to use
Ten or more scripts, mixed typing, and a wish to end with the analyzer green in CI. Not for: one file (use the annotator), or a prototype that will be rewritten.

## Inputs (max 2)
1. Source root (default `src/`). 2. Modules per working session (default 5, one commit each).

## Procedure
1. Collect every `.luau` source into `{ name = source }` (runner snippet below).
2. Run `scripts/StrictPlan.luau` with the two helpers passed in: `StrictPlan.order(sources, RequireGraph, TypeScan)`. It returns `rows` ordered by layer then gap score, and `done` (already strict and clean). Layer 1 has no dependencies.
3. Cycle members come last with a note. Break each cycle first (`require-cycle-finder`); types across a cycle stay unreliable.
4. Baseline the analyzer: `luau-lsp analyze` over the repo, record the error count with all files in their current mode. This is the only number that matters; the plan's scores are a ranking.
5. Work the rows top-down in batches: annotate with `luau-type-annotator`, run the analyzer, commit one batch. Stop a batch when the analyzer count rises elsewhere (a stricter dependency exposed a caller): fix the caller in the same batch.
6. Gate it: add `luau-lsp analyze` to the project check (see the template `luau-check.sh`) so a regression fails. New files start with `--!strict`.
7. Re-run the plan after each batch; the `done` list grows and the table shrinks.

```lua
local fs = require("@lune/fs")
local function collect(dir: string, out: { [string]: string })
	for _, name in fs.readDir(dir) do
		local path = dir .. "/" .. name
		if fs.isDir(path) then collect(path, out) elseif string.match(name, "%.luau?$") then out[string.gsub(name, "%.luau?$", "")] = fs.readFile(path) end
	end
	return out
end
local plan = require("./StrictPlan").order(collect("src", {}), require("./RequireGraph"), require("./TypeScan"))
for _, r in plan.rows do print(r.layer, r.name, r.score, r.effort, r.note or "") end
```

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` for scripts -> `script_read` each into the sources table -> run the plan with `execute_luau` -> `multi_edit` per module. Without a Rojo project, the Script Analysis panel is the analyzer.

## Fallback
Rojo repo plus Lune and luau-lsp. Module names must be unique for the name-keyed graph; duplicates are listed by hand.

## Evidence
`Roblox/roblox-kb/luau-language-and-types.md` (`--!strict` per script or via the Workspace type-check mode; avoid `any`; official Creator Docs 2026-10). `Roblox/roblox-kb/version-control-and-tooling.md` (linters and CI gates with StyLua --check and Selene; luau-lsp is the editor-side checker). The effort buckets (5 and 20 points) are this skill's own heuristic.

## Output
`strict-plan.md`: ordered table (layer, module, mode, score, effort, note), the done list, the analyzer baseline and the latest count.

## Acceptance checks
- [ ] Executed: `StrictPlan.order` ran on the real sources; row count plus done count equals the module count.
- [ ] No module is planned before a dependency of it (layer numbers never decrease down the table).
- [ ] Cycle members are listed last with the break-first note.
- [ ] The analyzer count is quoted before and after each batch and never rises across a batch.
- [ ] CI or the project check runs the analyzer.

## Pitfalls
Setting the Workspace default to strict first (hundreds of errors, nobody fixes them). Fixing the biggest file first. Using `any` casts to hit zero errors. Migrating a module that is about to be removed. Forgetting that annotations do not validate runtime input.

## Related
`luau-type-annotator`, `require-cycle-finder`, `module-architecture-planner`, `roblox-luau-style`.
