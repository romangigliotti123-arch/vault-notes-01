---
name: asset-pipeline-planner
description: "Plan how art, audio and model assets move from source file to a Roblox asset id the game uses: sources and licences, naming, a single constants registry of ids (0 until set), upload and reimport routine, and who may upload. Use when assets start piling up, when a builder or artist joins, or before ids are hard-coded in scripts."
category: workflow
tags: assets, pipeline, upload, ids, registry, naming, reimport, art, audio, sources
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/tools-and-resources.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/version-control-and-tooling.md, Mentor/Combined-Brain.md
related: asset-license-checker, naming-convention-enforcer, texture-budget-checker, folder-structure-planner, team-roles-planner, rbx-assets, place-backup-planner
---

# asset-pipeline-planner

A small, written route for every asset so ids do not scatter through scripts and nothing unlicensed ships. It decides the process; the checks are other skills: provenance is `asset-license-checker`, naming enforcement is `naming-convention-enforcer`, texture sizes are `texture-budget-checker`, finding assets is `rbx-assets`. Uploading and spending Robux are the user's actions.

## When to use
More than a handful of assets exist, an artist or builder is joining, or scripts contain pasted `rbxassetid://` numbers. Not for: modelling technique (build skills) or choosing a style (`brand-kit-builder`).

## Inputs (max 2)
1. The asset types in this game (models, meshes, textures, sounds, animations, UI images). 2. Who creates them (you, a builder or artist, free/bought assets).

## Procedure
1. List **Sources** per type: made by us (source files kept in `assets/source/`, not in git if huge), bought or free (record the licence and URL in the registry), AI-generated (flag it; check the platform's current rules, live-check). Anything of unknown origin is not used.
2. Set **Naming**: `Type_Subject_Variant_v01` for sources, matching Roblox names on upload; a rename creates a new MeshPart on reimport, so lock names before first import.
3. Define the **Upload** routine: upload once and reuse the same id everywhere (duplicates get separate ids and break batching); update with Reimport rather than re-uploading; a hidden backup copy of iterations is kept in the source folder, not only in Studio. The owner (or a named uploader) uploads; workers never upload or pay.
4. Create the **Registry**: one `src/shared/AssetIds.luau` ModuleScript (constants table) plus `assets/registry.csv` (`name,type,id,source,licence,checked_date`). Ids are `0` with the note `SET IN CREATOR HUB` until a real id exists; never invent an id. Scripts read the registry; no pasted ids elsewhere.
5. Check the repo: `grep -rnE "rbxassetid://[0-9]+" src | grep -v AssetIds.luau` must print nothing (move any hits into the registry); confirm every registry row with an id has a licence entry.
6. Add budget notes where relevant (texture sizes matched to surface area; triangle limits for UGC items) and hand to the matching checker skills.
7. Save `docs/ASSETS.md` (headings Sources, Naming, Upload, Registry; under 100 lines) and check it.

## Studio MCP path
Optional: `script_grep` for `rbxassetid://` across the open place to find hard-coded ids; `search_game_tree` to count MeshParts with duplicate MeshIds (read-only).

## Fallback
`grep` over the Rojo project and a hand-kept CSV; Creator Hub upload and permission steps are manual and `untested` here.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (upload each mesh once and reuse it; reimport instead of re-uploading and keep names stable; organise and credit free assets; size textures to surface area; UGC naming rules), `Roblox/roblox-kb/development-process-and-speed.md` (use templates and existing assets to save time; keep a hidden backup collection of iterations), `Roblox/roblox-kb/tools-and-resources.md`, `Roblox/roblox-kb/version-control-and-tooling.md` (assets stay uploaded to Roblox; referenced by id in a constants module). Platform rules on AI content and licences are live-check.

## Output
`docs/ASSETS.md`, `assets/registry.csv`, `src/shared/AssetIds.luau` (ids `0` until set).

## Acceptance checks
- [ ] Executed: `grep -rnE "rbxassetid://[0-9]+" src | grep -v AssetIds.luau` prints nothing (paste the empty result).
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/ASSETS.md --kind assets` prints PASS.
- [ ] Every registry row has a source and licence field.
- [ ] No invented ids; unset ids are `0`.

## Pitfalls
The same mesh uploaded five times. Renaming after import. Ids pasted into twenty scripts. Free assets with scripts hidden inside (hand to `asset-license-checker` and `model-cleaner`). A worker told to "upload the icons".

## Related
`asset-license-checker`, `naming-convention-enforcer`, `texture-budget-checker`, `folder-structure-planner`, `team-roles-planner`, `rbx-assets`.
