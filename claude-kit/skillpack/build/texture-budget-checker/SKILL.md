---
name: texture-budget-checker
description: "Inventory every texture-like asset in a place, add the image sizes, estimate texture memory against a budget, and rank which oversized textures to halve first. Use when mobile devices crash, memory is high, or before shipping an art-heavy update."
category: build
tags: texture, memory, budget, surfaceappearance, mesh, resolution, mobile, oom, audit
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md
related: model-cleaner, game-optimizer, material-consistency-checker, lod-planner, prop-set-planner
---

# texture-budget-checker

Mobile crashes are mostly memory, and texture memory scales with the square of the resolution, not with the PNG file size. Studio cannot read an image's dimensions from its asset id, so this is a two-part job: a script lists what is used where, you supply the sizes, and a tested module does the sums.

## When to use
Out-of-memory crashes on phones, a memory alert, after importing PBR sets, before a content update. Not for: audio/animation memory, or CPU frame cost (`game-optimizer`).

## Inputs (max 2)
1. Memory budget in MB for textures (this skill's default is 200; the vault gives full-game memory of 400-500 MB as the guide, so confirm with the Developer Console Place memory view). 2. Where the sizes come from (Asset Manager, source files, or "unknown": then the report is a ranking by use count only).

## Procedure
1. Connect (below). Read the Developer Console numbers first if you can: Place memory, and graphics texture memory. Record them; they are the ground truth.
2. Run `scripts/texture_inventory.luau`. It lists unique (id, kind) pairs with use counts and an example path, plus the number of SurfaceAppearances and how many have a MetalnessMap. Read-only.
3. Add width and height for the biggest or most used entries (Asset Manager shows the size, or open the source file). Build the list `{ id, width, height, uses, kind }`.
4. Run `scripts/TextureBudget.luau` under Lune with the list (a throwaway runner next to the module: `local TB = require("./TextureBudget")`, then `print(TB.format(TB.report(items, { budgetMB = 200 })))`). It merges duplicate ids (one texture in memory), estimates width x height x 4 bytes x 4/3 for mips, sorts by memory and flags anything above 1024 on a side with a 75 percent saving if halved.
5. Compare the estimate with the Developer Console figure. If they disagree by more than about 2x, say so: the model is an estimate (vault: 1024x1024 is about 5 MB; one resident 1024 SurfaceAppearance set about 2.8 MB).
6. Decide per oversized texture: seen up close or large on screen (keep), small or far (halve), unused map (remove: vault says leave MetalnessMap empty on non-metallic surfaces and drop ColorMap/Roughness/Metalness one or two steps).
6b. Size caps differ by scope; state which applies before calling a texture oversized (official, art/modeling/texture-specifications and the avatar specification pages; `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md` section 3): 4096 is the general upload ceiling, 1024 is the top of the PBR budget table, 2048 is the cap for Marketplace rigid and layered accessory textures (raised 2026-02-12; low-end mobile under 3.5 GB RAM still gets 1k), 256 for non-albedo maps of rigid accessories. By surface size: 5x5 studs 256, 10x10 512, 20x20 1024. PBR maps: OpenGL tangent-space normals, metalness workflow only, albedo with no baked lighting.
7. Fix steps (apply in this order, cheapest first; the owner does the edits, this skill lists them per asset):
   - Drop unneeded PBR maps: on non-metallic surfaces clear MetalnessMap; clear RoughnessMap and NormalMap on small or distant props; keep ColorMap. Each removed map frees a whole texture.
   - Remove auto-generated textureIDs: delete empty or duplicate `TextureID`/`ColorMap` values that Studio or an import filled automatically on MeshParts and SurfaceAppearances nobody sees up close.
   - Dedupe assets: merge entries that point at the same image or near-identical copies (one upload referenced everywhere), then re-point every user to the survivor.
   - Then halve resolution of what is left, largest saving first.
8. After replacing assets (the owner re-uploads; this skill does not), re-run the inventory and the estimate.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/texture_inventory.luau` -> (offline) Lune run of `TextureBudget` -> `screen_capture` of a before/after close-up when a texture is halved.

## Fallback
Command bar with the inventory script. If sizes are unknown the output is a ranking by use count and a list of PBR maps to question; the MB estimate is `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (right-size textures: drop 1-2x where invisible; leave MetalnessMap empty on non-metallic surfaces; mobile crashes are memory first; texture memory scales with resolution), `Roblox/roblox-kb/building-art-and-assets.md` (1024x1024 about 5 MB regardless of PNG size, 2018; 1024 SurfaceAppearance set about 2.8 MB: dated figures, live-check). The default budget is this skill's own.

## Output
```
TEXTURE BUDGET: 138 unique, ~312.4 MB estimated (OVER BUDGET 200)
 21.3 MB  color 2048x2048 x14 uses rbxassetid://...  <- halve if not seen up close
potential saving from oversize textures: ~118 MB    Untested: console figure not compared
```

## Acceptance checks
- [ ] The inventory ran; the report copies its counts.
- [ ] Sizes were supplied for every texture in the top ten, or the report says which are unknown.
- [ ] The estimate was compared with the Developer Console figure and the gap is stated.
- [ ] Every "halve" recommendation names whether the surface is seen up close.
- [ ] Each size verdict names its scope (general 4096, PBR 1024, Marketplace accessory 2048, rigid accessory non-albedo 256), not one blanket cap.
- [ ] No asset was changed by this skill.

## Pitfalls
Trusting the byte model as a measurement. Counting the same texture once per use (it is one in memory). Halving a hero texture or a normal map that carries the look. Forgetting UI images and particle textures. Texture streaming and device quality levels change real memory: check on a low-end phone, not in Studio (vault: Studio memory is much higher than a device).

## Related
`model-cleaner`, `game-optimizer`, `material-consistency-checker`, `lod-planner`, `prop-set-planner`.
