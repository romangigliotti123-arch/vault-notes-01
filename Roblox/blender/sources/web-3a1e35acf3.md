---
type: research-source
id: web-3a1e35acf3
title: "Roblox docs: art/modeling/export-requirements"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/export-requirements.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-3a1e35acf3

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Roblox doc giving Studio-ready FBX export settings for Blender and Maya. Blender: Path Mode Copy, Embed Textures, Apply Scalings to FBX Unit Scale, disable Add Leaf Bones, disable Bake Animation unless keyframed. Maya: Smooth Mesh, Referenced Asset Content, Units Automatic, Up Axis Y. No blender-mcp, bpy, or Claude content.

## Claims
- c1: Roblox doc says export Blender models as .fbx to get all Studio 3D import features; rigged/skinned FBX contains both rig and influence data. *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX export: Path Mode set to Copy and Embed Textures enabled. *(doc, high; blender-roblox-export-import)*
- c3: Blender FBX export: Transform > Apply Scalings set to FBX Unit Scale; alternative scaling fixes are in the Blender FBX scaling section. *(doc, high; blender-roblox-export-import)*
- c4: Blender FBX export: disable Add Leaf Bones under Armature section. *(doc, high; rigging-animation)*
- c5: Blender FBX export: disable Bake Animation unless exporting keyframed content such as a walk cycle or facial animation data. *(doc, high; rigging-animation)*
- c6: Maya FBX export: enable Smooth Mesh and Referenced Asset Content under Geometry; enable Embed Media if textures must be imported as PNG. *(doc, high; blender-roblox-export-import)*
- c7: Maya FBX export: Advanced Options set Units to Automatic and Axis Conversion Up Axis to Y. *(doc, high; blender-roblox-export-import)*
- c8: Maya FBX export: disable Animation unless an animation is needed in Studio; some avatar assets require animation; enable Bake Animation when exporting animation. *(doc, high; rigging-animation)*
- c9: Doc separates specs and export settings for rigid accessories, layered accessories, and avatar characters, each with its own page. *(doc, high; avatar-ugc-accessories)*
- c10: Models should meet Roblox modeling specifications before export; the page itself gives no numeric limits. *(doc, medium; mesh-texture-limits)*
- c11: Source does not mention blender-mcp, bpy scripting, or Claude; no coverage of AI-assisted Blender workflows. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Transform scale in Blender export example**: 0.01 Image caption shows Transform Scale set to .01 (scale example)

## Techniques
- t1: **Blender FBX export for Studio**: File > Export > FBX. Path Mode=Copy, enable Embed Textures. Apply Scalings=FBX Unit Scale. Disable Add Leaf Bones. Disable Bake Animation unless keyframed. Export FBX.

## Quotes (brief, for attribution)
> Export your mesh or model as a .fbx to take advantage of all of Studio's 3D import features.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/specifications
- https://create.roblox.com/docs/art/blender
- https://create.roblox.com/docs/avatar/rigid-accessories/export
- https://create.roblox.com/docs/avatar/layered-accessories/export
- https://create.roblox.com/docs/avatar/character-bodies/export
- https://create.roblox.com/docs/avatar/dynamic-heads

## Visual notes
Screens show Path Mode Copy with Embed Textures enabled, Apply Scalings set to FBX Unit Scale, Add Leaf Bones unchecked, and Maya Bake Animation unchecked.
