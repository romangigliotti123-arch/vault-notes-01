---
type: research-source
id: off-art_modeling_export-requirements
title: "Roblox Creator Docs: art_modeling_export-requirements"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/export-requirements"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# off-art_modeling_export-requirements

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page giving FBX export settings for Blender and Maya for Studio import. Blender: Path Mode Copy, Embed Textures, Apply Scalings FBX Unit Scale, disable Add Leaf Bones, disable Bake Animation unless keyframed. Maya: Smooth Mesh, Referenced Asset Content, Units Automatic, Up Axis Y, animation toggles. No blender-mcp, bpy, or Claude workflow content.

## Claims
- c1: Blender FBX export: set Path Mode to Copy and enable Embed Textures so textures travel with the .fbx. *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX export: set Transform > Apply Scalings to 'FBX Unit Scale' to avoid scale problems on import. *(doc, high; blender-roblox-export-import)*
- c3: Blender FBX export: disable 'Add Leaf Bones' under Armature section. *(doc, high; blender-roblox-export-import)*
- c4: Blender FBX export: disable Bake Animation unless exporting keyframed content (walk cycle, facial animation). *(doc, high; rigging-animation)*
- c5: Maya FBX export: enable Smooth Mesh and Referenced Asset Content in Geometry; set Units to Automatic and Up Axis to Y. *(doc, high; blender-roblox-export-import)*
- c6: Maya FBX export: disable Animation unless importing animation; enable Bake Animation when exporting animation. *(doc, high; rigging-animation)*
- c7: Maya: enable Embed Media only if textures must be imported as .png. *(doc, medium; blender-roblox-export-import)*
- c8: Rigid accessories, layered accessories and avatar characters have separate spec and export pages in addition to general .fbx settings. *(doc, medium; avatar-ugc-accessories)*
- c9: Roblox says .fbx export gives access to all Studio 3D import features; rig and skinning influence data are included in the .fbx. *(doc, high; blender-roblox-export-import)*
- c10: Source does not mention blender-mcp, bpy scripting, or Claude integration; it covers only manual export settings. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Blender Transform Scale**: 0.01 (per screenshot alt text) Shown in Blender export sidebar image

## Techniques
- t1: **Blender FBX export for Studio**: File > Export > FBX. Path Mode Copy, Embed Textures on. Apply Scalings: FBX Unit Scale. Disable Add Leaf Bones. Disable Bake Animation unless keyframed. Export FBX.
- t2: **Maya FBX export for Studio**: File > Export All, type FBX export. Geometry: Smooth Mesh and Referenced Asset Content on. Animation off unless needed (then Bake Animation on). Units Automatic, Up Axis Y.

## Quotes (brief, for attribution)
> Export your mesh or model as a .fbx to take advantage of all of Studio's 3D import features.  (create.roblox.com)
> Set Transform > Apply Scalings to FBX Unit Scale.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/avatar/dynamic-heads/index.md
- https://create.roblox.com/docs/art/modeling/specifications.md

## Visual notes
Blender sidebar: Path Mode Copy, Apply Scalings FBX Unit Scale, Transform Scale 0.01, Add Leaf Bones unchecked. Maya sidebar: Bake Animation unchecked.
