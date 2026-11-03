---
type: research-source
id: off-art_modeling_specifications
title: "Roblox Creator Docs: art_modeling_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# off-art_modeling_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs general modeling specs for custom meshes from Blender or Maya: 20,000-triangle per-mesh cap, watertight geometry, quads preferred, frozen transforms on bones, max 4 influences per vertex, single animation track per FBX, and _InnerCage/_OuterCage naming for cages. Does not cover blender-mcp, bpy, or Claude workflows.

## Claims
- c1: Individual meshes cannot exceed 20,000 triangles; avatar items have separate budgets for character bodies, rigid accessories, layered accessories. *(doc, high; blender-roblox-export-import)*
- c2: All geometry must be watertight with no exposed holes or backfaces; meshes cannot be zero thickness. *(doc, high; mesh-texture-limits)*
- c3: Avoid N-gons; meshes should be quads where possible. *(doc, high; mesh-texture-limits)*
- c4: All Blender bones (or Maya joints) must be frozen with scale 1,1,1 and rotation 0,0,0 before export. *(doc, high; rigging-animation)*
- c5: Root bone/joint should be at 0,0,0; no vertex may be influenced by more than 4 bones; no influences applied to the Root bone. *(doc, high; rigging-animation)*
- c6: Maintain symmetry when applying skin influences where possible. *(doc, medium; rigging-animation)*
- c7: Roblox supports basic color textures and modern PBR textures; texture images can be assigned in modeling tools to import with the mesh. *(doc, high; mesh-texture-limits)*
- c8: An animation can be included on any .fbx mesh export, but only a single animation track per export; export multiple animations as separate files. *(doc, high; rigging-animation)*
- c9: Inner and outer cage meshes must be named after the primary mesh with _InnerCage and _OuterCage suffixes. *(doc, high; avatar-ugc-accessories)*
- c10: Character models must include an outer cage to equip layered accessories; non-deforming targets only need an outer cage. *(doc, high; avatar-ugc-accessories)*
- c11: Do not delete vertices or alter UVs on inner/outer cages; this can cause import errors or equip failures. *(doc, high; avatar-ugc-accessories)*
- c12: Page lists Blender and Maya as supported third-party tools and points to separate export-settings pages; it does not cover Blender scripting, MCP, or Claude. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Max triangles per individual mesh**: 20,000 General geometry budget; avatar items have own budgets
- n2: **Max bone influences per vertex**: 4 Vertex cannot be influenced by more than 4 bones or joints

## Techniques
- t1: **Freeze bone transforms before export**: Freeze all bones/joints so scale is 1,1,1 and rotation 0,0,0; keep root at 0,0,0; then skin with max 4 influences per vertex.
- t2: **Cage naming**: Name cage objects after the primary mesh with _InnerCage or _OuterCage suffix; do not alter cage vertices or UVs.

## Quotes (brief, for attribution)
> Individual meshes can not exceed 20,000 triangles.  (create.roblox.com)
> Only a single animation track can be exported with a mesh or model.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/export-requirements
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://create.roblox.com/docs/art/modeling/texture-specifications
- https://create.roblox.com/docs/art/characters/export-avatar-animations-from-maya
- https://www.blender.org
