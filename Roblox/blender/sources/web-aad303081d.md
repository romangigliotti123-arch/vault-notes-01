---
type: research-source
id: web-aad303081d
title: "Roblox docs: art/modeling/reimport"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/reimport.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# web-aad303081d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio doc on Reimport: updates existing Model/MeshPart/SurfaceAppearance from an external 3D file without creating new instances. Matches meshes by path/name, keeps Roblox-specific properties, and detects PBR maps by filename suffix. Does not mention Blender, Claude, or bpy; relevant only to the export-to-Studio step.

## Claims
- c1: Reimport updates an existing Model from the external 3D file and remembers the file path and import settings, so re-running needs no initial import settings. *(doc, high; blender-roblox-export-import)*
- c2: MeshPart matching is by path/name of the mesh in the source file versus Studio. Matches update the MeshPart; new names create new MeshParts; Studio parts with no source match are left unchanged. *(doc, high; blender-roblox-export-import)*
- c3: Renaming a mesh in Blender (Mesh1 to Mesh2) creates a new MeshPart Mesh2 and leaves the original Mesh1 unmodified. *(doc, high; blender-roblox-export-import)*
- c4: Reimport only updates mesh content and transform; it preserves CollisionFidelity and RenderFidelity. If the incoming mesh has no texture, the existing MeshPart texture is kept. *(doc, high; blender-roblox-export-import)*
- c5: Reimport relative to a chosen MeshPart uses that MeshPart's pivot as anchor instead of the Model pivot, useful for custom pivots when that mesh did not move in the 3D file. *(doc, medium; blender-roblox-export-import)*
- c6: PBR map detection uses filename suffixes: color (color, col, diffuse, diff, albedo, alb, base), metalness, roughness, normal, emissive. Files without a recognized suffix are accepted as the color map. *(doc, high; mesh-texture-limits)*
- c7: Reimport hotkey is Alt+Shift+R on a selected Model; a missing or device-foreign reimport config opens the Configure dialog instead. *(doc, high; automation-and-creator-workflows)*
- c8: Reimport memory is local to the device: file paths are not saved in the place file, but the Reimport ID is stored on the Model and survives copy-paste, rbxm/rbxl save and load, and Asset Manager. *(doc, high; automation-and-creator-workflows)*
- c9: A Studio known asset cache reuses existing asset IDs for duplicate imports in the same session instead of re-uploading. *(doc, medium; automation-and-creator-workflows)*
- c10: Keep mesh names and paths unique in the external tool and keep the MeshPart tree structure in Studio, or reimport will not update correctly. *(doc, high; blender-roblox-export-import)*

## Numbers
- n1: **Reimport hotkey**: Alt+Shift+R 
- n2: **Color map suffixes**: 7 (color, col, diffuse, diff, albedo, alb, base) 
- n3: **Normal map suffixes**: 5 (normal, nor, nrm, nrml, norm) 

## Techniques
- t1: **Keep names stable for reimport**: Use unique mesh names and paths in Blender; keep the Studio Model's MeshPart hierarchy unchanged; then Reimport (Alt+Shift+R) to update in place.
- t2: **Reimport relative to a pivot**: Right-click an unmoved MeshPart, choose Reimport > Reimport relative to this, so the model is anchored on that part's pivot.

## Quotes (brief, for attribution)
> Reimport allows you to update existing custom models and their textures from an external 3D file. Unlike regular import, which creates brand new instances, the reimport function updates existing objects non-destructively.  (create.roblox.com)
> If a Class.MeshPart path/name in Studio doesn't exist in the 3D source file, reimport does not modify the Class.MeshPart in Studio.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/projects/assets/packages
- https://create.roblox.com/docs/projects/assets/manager
