---
type: research-source
id: off-art_accessories_creating_armature-setup
title: "Roblox Creator Docs: art_accessories_creating_armature-setup"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/accessories/creating/armature-setup"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# off-art_accessories_creating_armature-setup

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs tutorial on the armature step of custom clothing in Blender. Covers appending Roblox's R15 Rig_and_Attachments template, aligning and applying transforms on the armature, and parenting the t-shirt mesh with Automatic Weights for skinning, followed by pose tests. Official, concise, no code or numeric limits.

## Claims
- c1: Roblox provides Rig_and_Attachments_Template.blend as a premade R15 armature; importing it saves time and reduces error versus building your own rig. *(doc, high; blender-roblox-export-import)*
- c2: Armature is added via File > Append, selecting Armature > Armature from the appended template, then pressing Append. *(doc, high; rigging-animation)*
- c3: Before parenting, rotate the armature to align with the mesh, then Object > Apply > All Transforms to freeze rotation values. *(doc, high; blender-roblox-export-import)*
- c4: Parent the clothing mesh to the armature with Parent > With Automatic Weights: select mesh, shift-click armature last, right-click viewport. *(doc, high; rigging-animation)*
- c5: Automatic Weights parenting also applies skinning (vertex weights) automatically, saving time versus manual skinning of clothing. *(doc, high; rigging-animation)*
- c6: Rigging should be followed by basic pose tests to confirm clothing moves and stretches correctly across any character body. *(doc, high; avatar-ugc-accessories)*
- c7: Clothing is parented to the Roblox standard R15 rig; the tutorial says to verify Automatic Skinning Transfer data. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Append premade R15 armature**: File > Append Rig_And_Attachments_Template.blend, pick Armature > Armature, press Append. Stay in Object mode first.
- t2: **Parent With Automatic Weights**: Select clothing mesh, Shift-click armature last, right-click viewport > Parent > With Automatic Weights to auto-skin.
- t3: **Freeze armature transforms**: Item tool sidebar: align armature rotation to mesh, then Object > Apply > All Transforms.

## Quotes (brief, for attribution)
> Roblox provides base rigging armatures that you can import into your own project.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications#standard-r15-rigs
- Rig_and_Attachments_Templates.zip (Roblox reference file)
