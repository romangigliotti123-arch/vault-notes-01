---
type: research-source
id: web-e3e6e6b2fa
title: "Roblox docs: art/modeling/skin-a-simple-mesh"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/skin-a-simple-mesh.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "web", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# web-e3e6e6b2fa

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on skinning a 3-bone tree in Blender 3.0: set scene units, add armature, extrude bones, rename them, parent with automatic weights, then weight paint with Auto Normalize and projected brush, testing poses in Weight Paint mode. Export to FBX for Studio. Does not cover Claude, blender-mcp, bpy, or import settings.

## Claims
- c1: Roblox doc says to set Blender to Studio's relative scene units before importing a model. *(doc, high; blender-roblox-export-import)*
- c2: Rig guide uses 3 bones for a tree so it can move and rotate at three points; bones are created by Extruding (E) from the tip of the root bone in Edit Mode. *(doc, high; rigging-animation)*
- c3: Bone names must be set in the Outliner because bone object names remain the same when the mesh is imported into Studio. *(doc, high; rigging-animation)*
- c4: Parenting uses Parent > With Automatic Weights; selection order matters (mesh first, then armature, with armature active). *(doc, high; rigging-animation)*
- c5: Weight paint colors: blue = 0, red = 1 influence; yellow/green indicate partial influence. Guide uses 0.5 (green) for middle bone and 0.25 (teal) for top bone. *(doc, high; rigging-animation)*
- c6: Auto Normalize forces each vertex's total influence to 1, so full coverage can be painted first and then adjusted per bone. *(doc, high; rigging-animation)*
- c7: Testing bones during weight painting works only if armature and mesh are both selected in Object Mode before entering Weight Paint mode. *(doc, high; rigging-animation)*
- c8: Projected brush falloff with Front Faces Only unchecked helps paint influence through layered foliage rather than just the surface. *(doc, high; rigging-animation)*
- c9: Export guidance is referenced at the Studio export requirements page; the guide itself does not list triangle, texture, or UV limits. *(doc, medium; mesh-texture-limits)*
- c10: Source tested with Blender 3.0; minor UI differences expected in other versions. *(doc, high; other)*
- c11: Source does not mention blender-mcp, Claude, bpy scripting, or any AI-assisted workflow. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **bone count**: 3 Tree example skinned with three bones: bottom, middle, top
- n2: **middle bone weight**: 0.5 Brush Weight set to .5 for partial influence on middle bone
- n3: **top bone weight**: 0.25 Brush Weight set to 0.25 for top bone
- n4: **Blender version tested**: 3.0 Guide's reference version

## Techniques
- t1: **Automatic-weights parenting plus weight paint**: Add armature, position bones in Edit Mode, extrude E for chain, rename in Outliner, Parent With Automatic Weights, enable Auto Normalize, paint bottom bone at 1.0, middle at 0.5, top at 0.25, test with R.
- t2: **Hybrid pose during weight paint**: Select armature then mesh in Object Mode, switch to Weight Paint, shift-click bone, press R to test pose.

## Quotes (brief, for attribution)
> Skinning must be completed after the model is rigged.  (create.roblox.com)
> Bone object names remain the same when you import the mesh object into Studio.  (create.roblox.com)

## Points to
- https://www.blender.org/download/releases/3-0/
- https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/introduction.html
- https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/tool_settings/options.html
- ./rigging.md
- ./rig-a-simple-mesh.md
- ../../art/modeling/export-requirements.md
