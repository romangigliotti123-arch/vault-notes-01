---
type: research-source
id: off-art_modeling_cage-meshes_create-cages
title: "Roblox Creator Docs: art_modeling_cage-meshes_create-cages"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/cage-meshes/create-cages"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# off-art_modeling_cage-meshes_create-cages

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on creating cage meshes in Blender for WrapTarget/WrapLayer deformation. Covers outer/inner cage naming, matching UVs, low-poly cage shells, FBX/glTF export with Apply Scalings set to FBX Unit Scale, and 3D Importer Uses Cages. Does not cover Claude, blender-mcp, or bpy scripting.

## Claims
- c1: Cage meshes define an invisible surface for a render mesh; Studio needs at minimum a WrapTarget and a WrapLayer to interact. Cages must be made in a third-party tool like Blender or Maya. *(doc, high; mesh-texture-limits)*
- c2: Naming: target cage is Name_OuterCage (imports as WrapTarget); layered mesh needs Name_InnerCage and Name_OuterCage together (imports as WrapLayer). *(doc, high; blender-roblox-export-import)*
- c3: Export render mesh and cages together as one .fbx or .gltf; set FBX Apply Scalings to FBX Unit Scale; import with 3D Importer with Uses Cages enabled. *(doc, high; blender-roblox-export-import)*
- c4: Cage UVs must match across target and layered cages, since Roblox pairs layered mesh to target by UV. Do not add/delete cage vertices or change UVs after setup; this causes import errors or wrong deformation. *(doc, high; mesh-texture-limits)*
- c5: A cage should be a coarse shell: example avatar head render mesh up to 12,000 vertices, its cage only 335 vertices. *(doc, high; mesh-texture-limits)*
- c6: For avatar bodies and Marketplace clothing, do not create custom cages; use Roblox downloadable cage templates or the Avatar Setup tool to generate a supported cage. *(doc, high; avatar-ugc-accessories)*
- c7: If Uses Cages is not enabled in the 3D Importer, cage detection failed; recheck naming and re-export. *(doc, medium; blender-roblox-export-import)*
- c8: The source does not mention Claude, blender-mcp, or bpy scripting; it covers manual Blender cage modeling only. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **avatar head render mesh vertex count**: up to 12,000 
- n2: **avatar head cage vertex count**: 335 
- n3: **cube loop cuts per axis in example**: 10 

## Techniques
- t1: **Cage setup via duplicate-and-rename**: Duplicate render mesh, rename with _OuterCage or _InnerCage suffix, shrink-wrap outer just outside surface, inner just inside; keep UVs matching; export render plus cages in one FBX/glTF.

## Quotes (brief, for attribution)
> You must create these types of deformable meshes using a third-party modeling tool, such as Blender or Maya, and import them into Studio.  (create.roblox.com)
> Don't add or delete cage vertices after setting up a cage, and don't change its UVs. Destructive edits break vertex pairing and cause import errors or incorrect deformation.  (create.roblox.com)

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- ../../../assets/modeling/meshes/reference-files/Cage-Mesh-Examples.blend
- ../../../studio/importer.md
- ../../../avatar/resources.md#project-files
- ../../../avatar-setup/
- ../export-requirements.md#blender
- ../../../art/blender.md#adjust-scale-fbx
- apply-deformation.md
