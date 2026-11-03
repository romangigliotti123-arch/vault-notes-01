---
type: research-source
id: web-a9dd2a9668
title: "DevForum thread 2136849"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2136849"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "web", "other", "roblox-export-settings", "roblox-mesh-limits"]
---
# web-a9dd2a9668

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum Q&A (Jan 2023) on whether a ~3200-tri tree mesh (target 2200) suits a 5.5k x 5k stud forest map. Replies are forum opinion: no fixed Roblox triangle budget, keep low poly, use chunk loading for distant objects, and pick renderFidelity Automatic (general) or Performance (decorative or out-of-bounds meshes). Not about Blender MCP, bpy, or the Blender-to-Roblox export pipeline.

## Claims
- c1: No definitive triangle count is acceptable for a whole Roblox game; forum replies gave no hard budget. *(opinion, high; roblox-mesh-limits)*
- c2: Taveple advises modelling with as few triangles as possible; low-poly is usually fine depending on art style. *(opinion, medium; roblox-mesh-limits)*
- c3: Taveple says Roblox engine handles many standard-sized games well, so triangle count is 'not much of a worry' for them (opinion). *(opinion, low; roblox-mesh-limits)*
- c4: Custom chunk loading code can be used to render distant objects less, per Taveple. *(opinion, medium; roblox-mesh-limits)*
- c5: Taveple recommends RenderFidelity Automatic as the general choice; Performance for decorative meshes or ones out of bounds that need no precision. *(opinion, medium; roblox-export-settings)*
- c6: OP's tree is ~3200 tris, planned to reduce to ~2200; intended for a 5.5k x 5k stud map with dense tree cover. *(experience, low; roblox-mesh-limits)*
- c7: Shade Smooth in Blender is cited as a common low-poly trick to make faceted shapes look round at a glance. *(opinion, low; other)*

## Numbers
- n1: **tree mesh triangles**: ~3200 current, ~2200 target OP's tree model before and planned optimisation
- n2: **map size**: 5.5k x 5k studs OP's forest map, heavy tree cover

## Techniques
- t1: **Shade Smooth for low-poly**: Use Shade Smooth in Blender on low-poly geometry so it reads as rounder at a distance. Forum-cited trick, not tested in thread.
- t2: **Chunk loading for distant objects**: Write custom chunk-loading code to render far objects less. Mentioned only, no implementation given.

## Quotes (brief, for attribution)
> there is no definite solution to how many triangles are acceptable for the whole game itself  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/t/reasonable-amount-of-triangles-for-models
