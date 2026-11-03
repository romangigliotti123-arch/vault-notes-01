---
name: naming-convention-enforcer
description: "Write down a naming convention, audit Workspace and ReplicatedStorage against it (default engine names, casing, whitespace, duplicate siblings), propose spellings, and apply only the renames the owner approves in one undo step. Use when scripts break on names, Rojo paths clash, or a team needs one convention."
category: build
tags: naming, names, convention, pascalcase, rename, explorer, rojo, duplicates, organisation
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/version-control-and-tooling.md
related: workspace-organizer, model-cleaner, material-consistency-checker, art-bible-writer, script-dependency-mapper
---

# naming-convention-enforcer

Names are API in Roblox: scripts call `FindFirstChild("Door")`, Rojo turns names into file names, and two siblings with one name make lookups ambiguous. This checks a written convention and renames nothing by itself; every rename is a reviewed line.

## When to use
Before adding a team member, before Rojo/Git adoption, when a search by name returns the wrong thing, or after importing assets full of `Part2` and `MeshPart`. Not for: moving things into folders (`workspace-organizer`), or per-model cleanup (`model-cleaner`).

## Inputs (max 2)
1. Convention (default below, or the project's own). 2. Scope (default Workspace and ReplicatedStorage).

Default convention: Models, Folders, scripts and modules are PascalCase (`EnemySpawner`); parts are PascalCase segments joined by underscores (`Wall_North_02`); no leading or trailing spaces; no default engine names (`Part`, `Part3`, `MeshPart`, `Model`); unique among siblings.

## Procedure
1. Agree the convention in a few lines and put it where the team will see it (the art bible, or a `NAMING.md`).
2. Run `scripts/naming_audit.luau` read-only. The rules are `scripts/NamingRules.luau` (Lune-tested: default-name detection with numbers, PascalCase, segmented names, suggestions, duplicates). Read counts and examples per kind.
3. Default names have no automatic suggestion because a name should say what the thing is: write real names for the ones that matter (anything a script touches, anything Rojo syncs), and leave anonymous filler to `model-cleaner`.
4. For convention violations the report prints a suggested spelling. Collect approved ones as `["Workspace.Map.enemy spawner"] = "EnemySpawner"` lines.
5. Before renaming, search script sources for each old name (`script_grep` for the name, `FindFirstChild`/`WaitForChild` with it, and `workspace.Name` paths). Update scripts in the same change or skip the rename.
6. Put the approved map in `RENAMES`, set `APPLY = true`, run once (one undo step). Paths that no longer resolve are reported, not guessed.
7. Re-run the audit; counts for the fixed kinds go to zero.
8. If Rojo is used, rename the matching files/folders and `init` names in the same commit.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) with `scripts/naming_audit.luau` -> `script_grep` per candidate -> `execute_luau` with `RENAMES` filled and `APPLY = true` -> re-run.

## Fallback
Command bar. Offline, run `NamingRules.check` over a tree listing with Lune (a throwaway runner beside the module requiring `./NamingRules`); the suggestions are the same, applying is by hand.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (document and keep naming/organisation consistent), `Roblox/roblox-kb/building-and-level-design.md` (organise with folders, models and tags), `Roblox/roblox-kb/version-control-and-tooling.md` (Rojo workflows; that names become file names is general Rojo behaviour, not quoted from the vault). The default convention is this skill's own choice, not a platform rule.

## Output
```
NAMING AUDIT: scanned 3120 | default-name 410 | convention 96 | whitespace 4 | duplicate 37
Renamed (approved): 52   Skipped (script references): 11   Left: default names on filler parts
```

## Acceptance checks
- [ ] The convention is written down in the report.
- [ ] Counts before and after are copied from the audit.
- [ ] Every renamed instance was searched for in script sources first.
- [ ] RENAMES held only owner-approved lines; the apply was one undo step.
- [ ] Rojo file names (if any) match the new names.

## Pitfalls
Renaming something a script finds by name (the most common break). Renaming remotes, which the client and server must agree on. Auto-renaming duplicates: duplicates sometimes mean two real things that need different names. Applying PascalCase to third-party model internals you will replace anyway. A `.` in a name breaks the dotted RENAMES paths.

## Related
`workspace-organizer`, `model-cleaner`, `material-consistency-checker`, `art-bible-writer`, `script-dependency-mapper`.
