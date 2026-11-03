---
type: research-source
id: off-art_modeling_cage-meshes_index
title: "Roblox Creator Docs: art_modeling_cage-meshes_index"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/cage-meshes/index"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# off-art_modeling_cage-meshes_index

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on cage meshes: invisible low-res surfaces on a MeshPart (WrapTarget, WrapLayer) that let one mesh deform and layer over another, powering layered accessories. Cages pair by shared UV layout, not position. Blender setup uses _OuterCage/_InnerCage naming; Uses Cages must be enabled in the 3D Importer. Little on bpy/Claude or blender-mcp.

## Claims
- c1: Cage meshes are invisible surfaces on a MeshPart that let meshes deform and layer over each other; they power layered accessories like jackets and dresses. *(doc, high; avatar-ugc-accessories)*
- c2: Cages pair by UV coordinates rather than position; all targets and layers must share identical UVs. *(doc, high; avatar-ugc-accessories)*
- c3: Cage mesh components in Studio are WrapTarget (initial caged surface, required per deformation) and WrapLayer (wraps parent MeshPart around a target); MeshPart is the only valid parent. *(doc, high; avatar-ugc-accessories)*
- c4: In Blender, a render mesh with a single _OuterCage is a WrapTarget; with _InnerCage and _OuterCage it is a WrapLayer. *(doc, high; blender-roblox-export-import)*
- c5: When importing a model with cages, Uses Cages must be enabled in the 3D Importer so Studio creates the cage objects. *(doc, high; blender-roblox-export-import)*
- c6: Cage meshes are unlike the universal collision system: they only work with other paired cage meshes. *(doc, high; avatar-ugc-accessories)*
- c7: Cages can be created and reshaped programmatically at runtime in specific cases, such as user avatar item customization. *(doc, medium; avatar-ugc-accessories)*
- c8: The page does not mention Claude, blender-mcp, or bpy scripting; cages are authored manually in Blender or Maya. *(doc, high; claude-blender-ai)*

## Techniques
- t1: **Cage pairing by shared UV map**: Give the render mesh, target and layer cages an identical UV layout in Blender; Roblox pairs vertices by UV and reshapes the render mesh to match the target cage.
- t2: **Cage naming in Blender**: Add child meshes named _OuterCage (target) or _InnerCage plus _OuterCage (layer) under the render mesh, then import with Uses Cages enabled.

## Quotes (brief, for attribution)
> Roblox pairs cages by their UV coordinates rather than by position, so any two cages that share a UV layout can wrap over each other, even when their shapes differ.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/cage-meshes/create-cages
- https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/avatar/in-experience-creation
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
