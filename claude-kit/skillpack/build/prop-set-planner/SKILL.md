---
name: prop-set-planner
description: "Plan a reusable prop kit that dresses a whole map cheaply: how many variants, how many copies per area, the instance count, load time and client memory it adds, and how reusable the props in the place already are. Use before set-dressing a map or when a map has thousands of one-off props."
category: build
tags: props, kit, set dressing, reuse, instances, modular, variants, density, memory, mesh
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/building-and-level-design.md
related: graybox-builder, part-to-mesh-planner, lod-planner, terrain-planner, texture-budget-checker
---

# prop-set-planner

A small set of props, placed many times with variation, makes a map look rich and stays cheap: cloned mesh parts that reuse a MeshId keep memory roughly constant, and recolouring or resizing does not block that. A large set of one-off props is the opposite. This sizes the kit and costs it before anyone models a thing.

## When to use
Before set-dressing, when a map has far too many unique props, or when planning a reskin. Not for: the layout (`graybox-builder`), merging parts (`part-to-mesh-planner`), or streaming modes (`lod-planner`).

## Inputs (max 2)
1. The dressed area (studs squared) and the biome or theme. 2. Budget: target client instance ceiling (default: the vault's guide of about 150,000 with streaming on) and whether phones are the main device.

## Procedure
1. Take the approved graybox and the art bible. Read the place if props already exist: run `scripts/prop_census.luau` (read-only) for instances, MeshId reuse (copies per unique mesh), the heaviest models and the vault-based load and memory estimate.
2. List prop types the setting needs (trees, rocks, lamps, crates, fences, signs) and how detailed each must be at the camera distance players use. Keep detail low around avatars; use chunky shapes.
3. For each type choose: variants (distinct meshes), instances one placed copy adds (parts + attachments + decals + scripts), and copies per 1000 studs squared.
4. Run the plan under Lune with `scripts/PropKit.luau`: `PropKit.plan(area, props, ceiling)` returns counts placed, total instances, load seconds (about 1 s per 10,000 instances, vault), client memory (about 500 bytes per instance, vault), unique meshes and issues (instance ceiling exceeded; more variants than placed copies). `PropKit.reuse(result)` gives copies per mesh.
5. Iterate: lower density or instances per prop first, then variants. Aim for a high copies-per-mesh ratio (the census warns under 3). Variation comes from recolour, scale, rotation and swapping SurfaceAppearance or MaterialVariant on shared meshes rather than new meshes.
6. Write the kit sheet: type, variants, instances per copy, density, collision setting (usually off for small decor, see `collision-fidelity-tuner`), streaming mode (`lod-planner`).
7. After building, re-run the census and compare with the plan.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/prop_census.luau` -> offline `PropKit.plan` under Lune -> after building, repeat the census -> `screen_capture` for the look.

## Fallback
The planning maths needs no Studio. The census is command-bar Luau; without Studio the current reuse figures are unknown and the plan is `untested` against a real scene.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (about 1 second of load per 10,000 instances; about 500 bytes of client memory per instance; about 150,000 instances or fewer with streaming on; reuse MeshIds; combine static meshes late), `Roblox/roblox-kb/building-art-and-assets.md` (cloned mesh parts keep memory roughly constant; use modular simple low-detail environments; reuse and reskin assets), `Roblox/roblox-kb/building-and-level-design.md` (vary modular pieces with MaterialVariant and tints). The per-type densities are inputs, not recommendations.

## Output
```
PROP KIT: 100,000 studs^2 | tree 3 variants x 200 | rock 2 x 500 | lamp 1 x 60
instances 3,400 (~0.34 s load, ~1.6 MB) | unique meshes 6 | copies/mesh 127 | issues: none
Collision: off for rock/bush decor   Streaming: Atomic for lamps (scripted)
```

## Acceptance checks
- [ ] Every number in the kit sheet comes from the module or the census output.
- [ ] No prop type has more variants than placed copies.
- [ ] The instance ceiling is stated and respected.
- [ ] Variation methods other than new meshes are listed.
- [ ] After the build, the census was re-run and compared.

## Pitfalls
Counting parts but not their children (attachments, decals, scripts, lights add instances). Unique MeshIds for near-identical props. Props with scripts per copy (use tags and one controller). Putting everything into one giant model (streaming suffers). Ignoring physics: small decor should not collide.

## Related
`graybox-builder`, `part-to-mesh-planner`, `lod-planner`, `terrain-planner`, `texture-budget-checker`.
