---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-art-blender.md
title: "Roblox/creator-docs/content/en-us/art/blender.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/art/blender.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0972
relevance: 3
density: medium
tags: ["research-source", "github", "avatar-ugc-accessories", "common-mistakes-fixes", "rigging-animation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# gh-Roblox-creator-docs-f-content-en-us-art-blender.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator-docs Blender guide: configure Blender units and axes to match Studio, import/export settings for OBJ/FBX/glTF, FBX scale fixes, workspaces, modeling tools, and UV/texturing basics (trim sheets). No Claude/MCP/bpy content. Text truncated at the Unwrap tool.

## Claims
- c1: Set Blender Scene > Units > Unit System to None and Rotation to Degrees so measurements stay consistent with studs. *(doc, high; roblox-export-settings)*
- c2: Blender uses Z-up; Studio uses Y-up. Export with Forward = Z Forward and Up = Y Up, and enable Limit to Selected Objects. *(doc, high; roblox-export-settings)*
- c3: For FBX export, set Transform > Apply Scalings to FBX Unit Scale; this is the recommended way to keep scale. All other scale values should be 1.0. *(doc, high; roblox-export-settings)*
- c4: Default Blender FBX export settings often import into Studio at an unexpectedly large scale. *(doc, high; common-mistakes-fixes)*
- c5: glTF (.gltf) does not require the extra FBX scaling configuration in Studio. *(doc, high; roblox-export-settings)*
- c6: Alternative FBX scale fixes: export Transform > Scale 0.01, or set Scene Unit Scale to 0.01. The latter can cause camera and modifier problems in Blender. Both make re-import into Blender too small unless you rescale. *(doc, high; common-mistakes-fixes)*
- c7: Studio importer: enable Import Only as a Model to group multiple objects into a Model, Upload to Roblox for an asset ID, and Insert Using Scene Position to keep Blender position. *(doc, high; roblox-import-pipeline)*
- c8: Studio importer transform settings: World Forward = Front, World Up = Top, and File Geometry Scale Unit = Stud, to match Blender orientation and scale. *(doc, high; roblox-import-pipeline)*
- c9: Importing Studio-exported files into Blender: Scale 1, Forward Axis Z, Up Axis Y. *(doc, high; roblox-import-pipeline)*
- c10: Avatar items (rigid accessories, layered accessories, characters) need their own specs and export settings, separate from the general guide. *(doc, high; avatar-ugc-accessories)*
- c11: Trim sheets let multiple meshes share one UV map and texture, adding visual complexity without extra textures and saving memory. The Laser Tag template's doorframe, ceiling and card reader share one UV map. *(doc, high; texturing-baking-uv)*
- c12: Fill and New Faces from Edges close holes so meshes are watertight. *(doc, medium; common-mistakes-fixes)*
- c13: Existing reference files, demo projects and tutorials may use older or inconsistent scale settings; test them against your own export workflow. *(doc, high; common-mistakes-fixes)*
- c14: Weight Paint mode sets which armature parts influence which body parts; it is useful for avatars. *(doc, medium; rigging-animation)*

## Numbers
- n1: **FBX export Scale workaround**: 0.01 Transform > Scale so model imports at expected size in Studio
- n2: **Scene Unit Scale workaround**: 0.01 Alternative to scale the whole scene
- n3: **Sculpt brush types**: over 20 Sculpting workspace brushes

## Techniques
- t1: **Blender to Studio FBX export**: File > Export > FBX; enable Limit to Selected; Apply Scalings = FBX Unit Scale; Forward = Z Forward; Up = Y Up; export. In Studio importer set World Forward Front, World Up Top, Scale Unit Stud.
- t2: **Mark seams then unwrap**: In UV Editing workspace, select edges in Edit mode, press Ctrl+E > Mark Seam, then Unwrap so enclosed faces become their own island. Example: leather grip of a rivet gun.
- t3: **Trim sheet UV sharing**: Map multiple objects onto one shared texture and UV layout in UV Editing to reuse a single texture across meshes and save memory.

## Quotes (brief, for attribution)
> when exporting from Blender using its default .fbx settings, models often import at an unexpectedly large scale in Roblox Studio.  (Roblox)

## Points to
- https://www.blender.org/download/
- ../avatar/rigid-accessories/export.md
- ../avatar/layered-accessories/export.md
- ../avatar/character-bodies/export.md
- ../art/modeling/surface-appearance.md
- Roblox Laser Tag template
- Environmental art curriculum: Develop polished assets - Trim sheets
