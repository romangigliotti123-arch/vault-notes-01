---
name: workspace-organizer
description: "Sort loose top-level Workspace objects into a clear folder structure (Map, Props, Zones, Spawns, Lights, Audio, Interactive) by class and name rules, dry-run first, skipping anything a script names, in one undo step, without renaming anything. Use when the Explorer is a flat pile."
category: build
tags: workspace, explorer, folders, organise, structure, rojo, hierarchy, tags, cleanup
kb: Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/version-control-and-tooling.md
related: naming-convention-enforcer, model-cleaner, lod-planner, script-dependency-mapper, game-optimizer
---

# workspace-organizer

A readable Workspace makes everything else faster: finding builds, scoping audits, setting streaming modes per area. The vault's advice is Folders for sections, Models for related sets, tags for behaviour. This applies that to the flat top level and leaves nested structure alone.

## When to use
The Explorer is hundreds of loose parts and models at the top level; before a handover; before per-area work (streaming, lighting, audits). Not for: renaming (`naming-convention-enforcer`), or restructuring inside a model (`model-rebuild`).

## Inputs (max 2)
1. Target folders (default: Map, Props, Zones, Spawns, Lights, Audio, Interactive, Misc). 2. Is the place Rojo-managed? Default: assume it might be and never rename.

## Procedure
1. Connect (below). Save or confirm version history. Note that Rojo-managed places need the same change in the project tree (this script cannot do that).
2. Run `scripts/organize.luau` with `APPLY = false`. The rules are `scripts/OrganizerPlan.luau` (Lune-tested): Terrain, Camera, Folders and scripts stay; SpawnLocation -> Spawns; Sound -> Audio; lights -> Lights; models/parts named like zones or triggers -> Zones; names like tree, rock, lamp, crate -> Props; models containing scripts -> Interactive; other models/parts -> Map; anything else -> Misc.
3. Read the plan: moves, skipped (a script mentions the name: `workspace.Door`, `FindFirstChild("Door")`, a path string) and kept. Skipped items are the ones whose move would break code.
4. Adjust `PROP_WORDS`/`ZONE_WORDS` for the game's own vocabulary and re-run the dry run.
5. For skipped items either update the referencing scripts (`script_grep`, then edit) and re-run, or leave them where they are on purpose.
6. If script sources cannot be read the script refuses to apply; read references by hand or run it from the command bar.
7. Set `APPLY = true`. Folders are created or reused; each object is re-parented (names untouched); one undo step.
8. Re-run the dry run: the moves list must be empty. Play-test (`start_stop_play`, `get_console_output`) for new "not a valid member" errors.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/organize.luau` -> `script_grep` on skipped names -> apply -> `start_stop_play` -> `get_console_output`.

## Fallback
Command bar. By hand: select the objects in the Explorer, right-click and choose Group as Folder, then name the folder. Offline, `OrganizerPlan.plan` under Lune over a tree listing gives the same plan; applying is `untested`.

## Evidence
`Roblox/roblox-kb/building-and-level-design.md` (organise with Folders, Models and tags; Folders for sections like lobby and arena, Models for related sets), `Roblox/roblox-kb/optimization-and-streaming.md` (keep static world models in Workspace, per-player clones in a Folder), `Roblox/roblox-kb/version-control-and-tooling.md`. The folder set is a sensible default, not a Roblox rule.

## Output
```
WORKSPACE ORGANIZER: 214 to move, 9 skipped (name found in a script), 12 kept
Map 130 | Props 61 | Zones 14 | Spawns 4 | Lights 5   Skipped: Door, Lift, KillBrick1 ...
```

## Acceptance checks
- [ ] Dry run read, adjusted and re-run before applying.
- [ ] Skipped items are listed with the script that references them.
- [ ] After apply the dry run shows zero moves.
- [ ] A Play test produced no new infinite-yield or missing-child warnings.
- [ ] Apply was one undo step; Rojo trees (if any) updated by the owner.

## Pitfalls
Moving a model a script reaches with `workspace.Name` (now nil): that is why referenced names are skipped. Streaming: moving models into a Folder changes nothing about streaming, but Persistent/Atomic models inside a model with the opposite mode still need `lod-planner`. Folders named like existing objects. `Misc` becoming a dumping ground: review it.

## Related
`naming-convention-enforcer`, `model-cleaner`, `lod-planner`, `script-dependency-mapper`, `game-optimizer`.
