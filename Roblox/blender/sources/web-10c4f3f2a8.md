---
type: research-source
id: web-10c4f3f2a8
title: "Roblox docs: art/characters/facial-animation/create-face-accessories"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/facial-animation/create-face-accessories.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "other", "rigging-animation"]
---
# web-10c4f3f2a8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc for face accessories (eyebrows, eyelashes, glasses) built in Blender 5.2 on the Cubie dynamic head. Covers parenting to armature with automatic weights, optional manual skinning, inner/outer cage creation, export cleanup, and testing via Accessory Fitting Tool. Does not cover blender-mcp, bpy, or Claude workflows.

## Claims
- c1: Face accessories are layered accessories that equip to dynamic heads and deform with facial animation (eyebrows, eyelashes, glasses). *(doc, high; avatar-ugc-accessories)*
- c2: Face accessory must be parented (Blender) or bound (Maya) to a standard or advanced R15 rig and include an inner and outer cage. *(doc, high; avatar-ugc-accessories)*
- c3: Multi-piece face accessories (eyebrows, eyelashes) should be combined into a single mesh after modeling and rigging; no _Geo naming needed. *(doc, high; avatar-ugc-accessories)*
- c4: Parent accessory to armature via Shift-select mesh then joint, Parent > Armature Deform > With Automatic Weights; Empty Weights gives manual skinning control. *(doc, high; rigging-animation)*
- c5: Cages: rename to start with accessory name before _InnerCage/_OuterCage, then stretch Outer Cage vertices to fit accessory with minimal space. *(doc, high; avatar-ugc-accessories)*
- c6: Export only accessory mesh, armature and cage meshes; delete other objects, animation data, lights and cameras; follow layered accessory export settings. *(doc, high; avatar-ugc-accessories)*
- c7: Test in Studio by generating Accessory via Accessory Fitting Tool; enable automatic skinning transfer; only EnabledOverride applies transfer when parenting data was applied. *(doc, medium; avatar-ugc-accessories)*
- c8: Tutorial uses Blender 5.2; minor UI and settings differences expected in other versions. *(doc, medium; blender-roblox-export-import)*
- c9: Source does not cover blender-mcp, Claude integration, bpy scripting, or the Roblox Blender plugin; it is a manual Blender tutorial. *(doc, high; other)*

## Numbers
- n1: **Blender version used**: 5.2 tutorial version; other versions may differ slightly

## Techniques
- t1: **Automatic weights parenting**: Shift-select accessory and armature joint, then Parent > Armature Deform > With Automatic Weights; alternatively Empty Weights for manual skinning.
- t2: **Outer cage fitting**: Import Cubie-Cage-Only, rename cages with accessory prefix, edit outer cage vertices to hug accessory; remove unneeded cage sections to limit automatic skinning transfer.

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/layered-accessories/specifications.md
- https://www.blender.org
- Accessory Fitting Tool
- Automatic Skinning Transfer
