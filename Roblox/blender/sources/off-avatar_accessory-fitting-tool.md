---
type: research-source
id: off-avatar_accessory-fitting-tool
title: "Roblox Creator Docs: avatar_accessory-fitting-tool"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/accessory-fitting-tool"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories"]
---
# off-avatar_accessory-fitting-tool

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs on the Accessory Fitting Tool in Studio: tests custom Model/MeshPart as layered (Clothing, cage-based) or rigid (Accessory, attachment-based) accessories across bodies, animations, and custom assets, then generates Class.Accessory. Covers setup, cage/bounding-box fit edits, and generation. Nothing on Blender, bpy, or MCP.

## Claims
- c1: Accessory Fitting Tool (AFT) is a built-in Studio tool to test custom Model/MeshPart on character bodies, animations, and accessories before generating a Class.Accessory. *(doc, high; avatar-ugc-accessories)*
- c2: AFT Asset Type page offers Clothing (layered, inner/outer cage) or Accessory (rigid, attachment-point static placement); AFT auto-generates AccessoryType and body attachment points. *(doc, high; avatar-ugc-accessories)*
- c3: Body scale options are Classic, Proportions Slender, Proportions Normal; setting only affects rigid accessories when body part has differing AvatarPartScaleType; no effect on layered. *(doc, high; avatar-ugc-accessories)*
- c4: Cage editing: disable Move snapping to nudge individual cage vertices; Falloff Distance controls influence radius on neighboring vertices. Docs say use it for minor-to-moderate edits only; major sculpting should be done in third-party software and reimported. *(doc, high; avatar-ugc-accessories)*
- c5: Layered accessories offer EnabledPreserved (original modeling-software skinning) vs EnabledOverride (skinning transferred from avatar) via auto-skin toggle. *(doc, high; avatar-ugc-accessories)*
- c6: Rigid accessories show a bounding box around mannequin; box turns red when accessory sits outside allowed space. *(doc, high; avatar-ugc-accessories)*
- c7: Custom assets (Accessory, Model, MeshPart, Animation, Folder) can be added to AFT catalog via the ⊕ icon next to search, appearing under Custom category. *(doc, high; avatar-ugc-accessories)*
- c8: Generate MeshPart Accessory button creates the Accessory hierarchy; can then equip via HumanoidDescription or drop under character Model. *(doc, high; avatar-ugc-accessories)*
- c9: Playtest from AFT replaces avatar with selected body and accessories; Studio-only workflow, no Blender scripting or MCP covered. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Asset type options**: 2 (Clothing, Accessory) Layered vs rigid selection in AFT Asset Type page
- n2: **Body scale options**: 3 (Classic, Proportions Slender, Proportions Normal) Sets AvatarPartScaleType for rigid accessories

## Techniques
- t1: **AFT rigid fitting**: Select MeshPart/Model in Explorer, pick Accessory type, choose body scale, then position/rotate/scale within bounding box until it turns non-red.
- t2: **AFT cage editing**: Enable cage editing, disable Move snapping, select vertices, move with Move tool, adjust Falloff Distance and opacity sliders; reset via Reset Inner/Outer Cage.

## Quotes (brief, for attribution)
> The AFT automatically handles the conversion of the custom Class.Model or Class.MeshPart based on your menu selections  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/layered-accessories
- https://create.roblox.com/docs/avatar/rigid-accessories
- https://create.roblox.com/docs/marketplace/marketplace-policy
- https://create.roblox.com/docs/characters/appearance
