---
name: model-cleaner
description: "Audit one Roblox model (a Toolbox find, an import, your own build) for the problems that cost performance or break behaviour - unanchored parts, default names, heavy collision, risky unions, scripts hiding inside, missing PrimaryPart - and apply only the safe fixes, with a before/after report and one undo step. Use before a model goes into the game."
category: build
tags: model, clean, audit, cleanup, anchored, collision, union, toolbox, import, names, primarypart, malware
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: model-rebuild, asset-license-checker, collision-fidelity-tuner, anchor-checker, naming-convention-enforcer, game-optimizer, exploit-audit
---

# model-cleaner

Cleans ONE model. Rebuilding it from scratch is `model-rebuild`; place-wide performance is `game-optimizer`; reading its scripts for backdoors is the "scripts inside" step here plus `exploit-audit`. The audit is read-only; fixes are opt-in and limited to changes that cannot alter how the model looks or plays.

## When to use
A model from the Toolbox or an import, or one of yours that lags or misbehaves ("falls apart", "jitters", "players get stuck"). Not for: terrain, or character rigs (`rig-checker`).

## Inputs (max 2)
1. Which model (Studio selection, or a path like `Workspace.Map.Castle`). 2. Is it meant to move? (default: static scenery; say ragdoll/vehicle/physics prop to allow unanchored parts).

## Procedure
1. Connect and snapshot (below). Ask the owner to save a copy or confirm Studio version history if you will run fixes.
2. Run the audit: `scripts/audit_model.luau`. Set `TARGET` (or select the model), `EXPECT_STATIC` per input 2, `APPLY_SAFE_FIXES = false`. Read the report.
3. Triage each row with these rules (vault building/optimisation rules):
   - Unanchored static parts -> anchor (they cost physics and fall apart). Moving assemblies stay unanchored with welds.
   - PreciseConvexDecomposition -> Box or Hull unless exact collision is needed (cheapest first: Box, Hull, Default, Precise).
   - Decorative parts the player never touches: CanCollide, CanTouch and CanQuery off (grass, vines, props). Confirm no script uses them first (grep scripts for the part name).
   - Unions -> keep only where no part/mesh substitute exists; large unions cost memory and can have collision surprises.
   - Default names (`Part`, `Part2`, `MeshPart`) -> rename by purpose so scripts and Rojo paths are stable.
   - Scripts inside the model -> read them. Anything with `require(<number>)`, `loadstring`, HTTP calls or obfuscated strings is a backdoor risk: remove it and say so. Move legitimate logic to the right container.
   - No PrimaryPart or a far-off pivot -> set PrimaryPart (largest part is the suggestion); a bad pivot makes `PivotTo` place the model wrongly.
   - Empty Folders/Models, near-zero parts, invisible-but-collidable parts -> delete or fix intentionally.
4. Apply the SAFE fixes only by setting `APPLY_SAFE_FIXES = true` (sets a missing PrimaryPart and `CastShadow=false` on parts smaller than 0.5 studs; one undo step). Everything else is applied by hand or with explicit property edits you list in the report.
5. Re-run the audit and compare counts. Write the report.
6. Place-level effects (streaming, part budget) belong to `game-optimizer`; note them, do not fix them here.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `search_game_tree` to find the model -> `execute_luau` (datamodel_type Edit) with the contents of `scripts/audit_model.luau` (TARGET set to the path: edit the line `local TARGET: Instance? = game.Workspace.Map.Castle`) -> read the string result -> property edits via `execute_luau` or `inspect_instance` for single parts -> re-run. Script bodies: `script_read` / `script_grep`.

## Fallback
Paste `scripts/audit_model.luau` into the Studio command bar with the model selected; it prints the report. Without Studio: ask for the model's `.rbxm`/`.rbxl` or work from a Rojo project tree (names, hierarchy, script sources only; mesh and collision checks are `untested`).

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (collision fidelity cheapest-first; disable collision/touch/query on non-interactive parts; streaming mode on models), `Roblox/roblox-kb/building-art-and-assets.md` (consistency and organisation), `Roblox/roblox-kb/anti-exploit-and-security.md` (free-model scripts are untrusted; keep authority server-side). Facts about Roblox property behaviour: verify in Creator Docs when unsure (`kbq.py docs "CollisionFidelity"`).

## Output
```
MODEL CLEAN: <path>  before -> after
parts 412 -> 412 | unanchored 37 -> 0 | precise collision 9 -> 0 | scripts 3 (1 removed: backdoor pattern) | renamed 55
Fixed: ...   Needs owner decision: ...   Left alone on purpose: ...   Untested: ...
```
Plus the raw audit text in a collapsed block or file `reports/model-clean-<name>.txt`.

## Acceptance checks
- [ ] Audit ran before and after; counts in the report are copied from the script output.
- [ ] No fix changed appearance or gameplay (ask for a visual check when in doubt; screenshots before/after with `screen_capture`).
- [ ] Every removed script is named with the reason; backdoor patterns are called out explicitly.
- [ ] Anchoring changes did not freeze parts that must move (checked against input 2).
- [ ] The report lists anything not checked (e.g. collision behaviour in play).

## Pitfalls
Anchoring a ragdoll or door. Turning CanQuery off on parts that raycast-based tools or click-to-interact rely on. Renaming parts a script finds by name. Deleting "empty" folders that Rojo or scripts expect. Trusting a Toolbox model's scripts.

## Related
`model-rebuild`, `asset-license-checker`, `collision-fidelity-tuner`, `anchor-checker`, `game-optimizer`, `exploit-audit`.
