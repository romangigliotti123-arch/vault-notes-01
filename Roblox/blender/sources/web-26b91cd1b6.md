---
type: research-source
id: web-26b91cd1b6
title: "Roblox docs: avatar/accessory-fitting-tool"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/accessory-fitting-tool.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "other"]
---
# web-26b91cd1b6

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for Studio's Accessory Fitting Tool: setup (Clothing vs Accessory type, body scale), testing on bodies/layered accessories/animations/custom assets, cage editing for layered items, bounding-box fitting for rigid items, and generating a Class.Accessory. Covers accessory fit only; no Blender, bpy, or export-pipeline content.

## Claims
- c1: Accessory Fitting Tool (AFT) is a built-in Studio tool to test custom Model/MeshPart on multiple bodies, animations and accessories before generating a Class.Accessory. *(doc, high; avatar-ugc-accessories)*
- c2: AFT opens from toolbar Avatar tab > Accessory; asset type choices are Clothing (layered, inner/outer cage) or Accessory (rigid, attachment point). *(doc, high; avatar-ugc-accessories)*
- c3: Body type options are Classic, Proportions Slender, Proportions Normal; setting sets AvatarPartScaleType and does not affect layered accessories. *(doc, high; avatar-ugc-accessories)*
- c4: Layered accessory cage editing: disable Move snapping, select vertices, move them; Falloff Distance controls influence on nearby vertices. Docs say use it for minor/moderate edits only. *(doc, high; avatar-ugc-accessories)*
- c5: Rigid accessory fit uses a bounding box around the mannequin; box turns red if the accessory is outside allowed space. *(doc, high; avatar-ugc-accessories)*
- c6: Autoskin toggles between EnabledPreserved (original skinning from modeling software) and EnabledOverride (skinning transferred from avatar character). *(doc, high; avatar-ugc-accessories)*
- c7: Generate MeshPart Accessory button creates the Class.Accessory hierarchy, sets AccessoryType and generates body attachment points. *(doc, high; avatar-ugc-accessories)*
- c8: Custom test assets can be added via the plus icon: Accessory, Model, MeshPart, Animation or Folder objects from viewport or Explorer. *(doc, high; avatar-ugc-accessories)*
- c9: Playtest from AFT replaces avatar with the currently selected body and accessories; major fit or sculpting changes should be done in third-party modeling software and reimported. *(doc, medium; automation-and-creator-workflows)*
- c10: Source does not mention Blender, Claude, blender-mcp, bpy, FBX/glTF settings, or Blender-to-Roblox pipeline steps; relevance to the topic is low. *(doc, high; other)*

## Numbers
- n1: **Body scale options**: 3 (Classic, Proportions Slender, Proportions Normal) Asset Type page body type selection

## Techniques
- t1: **Cage vertex editing in AFT**: Disable Move snapping, select cage vertices, move with Move tool, set Falloff Distance, reset via Reset Inner/Outer Cage.

## Quotes (brief, for attribution)
> test your custom models on multiple combinations of character bodies, animations, and accessories before generating the final Class.Accessory object  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/accessory-fitting-tool.md
- layered-accessories
- rigid-accessories
- automatic-skinning-transfer
- marketplace-policy
- HumanoidDescription
