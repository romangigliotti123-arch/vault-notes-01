---
type: research-source
id: off-avatar_layered-accessories_caging-best-practices
title: "Roblox Creator Docs: avatar_layered-accessories_caging-best-practices"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/layered-accessories/caging-best-practices"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "other"]
---
# off-avatar_layered-accessories_caging-best-practices

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs on caging layered accessories: start from provided templates, keep clothing between inner and outer cages, keep outer cage vertices even, unstacked and UV-unchanged, and avoid listed configurations that fail validation (identical cages, missing limbs, outer inside inner, collapsed vertices). Does not cover Blender scripting, blender-mcp, or Claude.

## Claims
- c1: Always start caging from Roblox's provided caging templates, which include inner and outer cages with properly set UVs; do not edit cage UVs. *(doc, high; avatar-ugc-accessories)*
- c2: Clothing mesh must sit between inner cage and outer cage; it is deformed by the layering system. Clothing outside outer cage is not deformed. *(doc, high; avatar-ugc-accessories)*
- c3: Cage vertices must not be stacked/collapsed; stacked vertices cause artifacts and are rejected in validation. *(doc, high; avatar-ugc-accessories)*
- c4: Outer cage edits: move vertices outward along normals, keep vertex/edge/face count unchanged, keep spacing even, do not alter UVs, keep close to clothing. *(doc, high; avatar-ugc-accessories)*
- c5: Identical inner and outer cages, outer cage inside inner cage, missing limbs/head in cage, and layered mesh fully outside cage are all rejected during validation. *(doc, high; avatar-ugc-accessories)*
- c6: Roblox enforces stricter validation; improper cages may block Marketplace upload and lead to removal of existing catalog items. *(doc, high; avatar-ugc-accessories)*
- c7: Bulky clothing needs extra outer-cage displacement along vertex normals with smooth, neighboring-vertex-consistent movement; avoid moving uncovered regions. *(doc, medium; avatar-ugc-accessories)*
- c8: For protrusions (puffy hoods, shoulder pads, spikes), keep outer cage below the protrusion so it stays visible when other layers are equipped. *(doc, high; avatar-ugc-accessories)*
- c9: Clothing inside the inner cage causes artifacts when layered over other clothing; avoid it. *(doc, high; avatar-ugc-accessories)*
- c10: Uneven outer cage spacing creates undulating surfaces that cause artifacts on any accessory layered on top. *(doc, medium; avatar-ugc-accessories)*
- c11: Source does not mention Blender, blender-mcp, bpy, Claude, or the Blender-to-Roblox export pipeline; relevance to the requested topic is low. *(doc, high; other)*

## Techniques
- t1: **Outer cage editing**: Start from template; move outer cage verts outward along normals symmetrically; keep vertex/edge/face count and UVs unchanged; keep spacing even; keep just outside clothing silhouette.
- t2: **Protrusion handling**: Place outer cage below protruding region (hood, pads, spikes) so it stays visible under additional layers.

## Quotes (brief, for attribution)
> Always start any caging work with one of Roblox's provided caging templates. These templates include an inner cage and outer cage with properly set UVs.  (create.roblox.com)
> You should not edit the cage UVs since this will introduce visual artifacts.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/assets/modeling/meshes/reference-files/Clothing_Cage_Templates.zip
