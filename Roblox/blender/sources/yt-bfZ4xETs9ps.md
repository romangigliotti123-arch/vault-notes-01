---
type: research-source
id: yt-bfZ4xETs9ps
title: "How To Upload UGC Items On Roblox"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=bfZ4xETs9ps"
published: "2024-04-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# yt-bfZ4xETs9ps

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox UGC accessory walkthrough, not Blender scripting. Shows exporting a car model as FBX from Blender, importing into Studio as a MeshPart, aligning it to an R15 Block Rig, and using the Asset Creator plugin to create a shoulder accessory with an attachment point. Covers triangle count, upload validation, and pricing. No blender-mcp, bpy, or Claude content.

## Claims
- c1: [0:17] Uploading UGC items requires Premium (speaker cites $10 or $20 tier) and ID age verification before modeling and uploading. *(demo, medium; avatar-ugc-accessories)*
- c2: [0:54] Workflow: export model from Blender as FBX, insert via MeshPart file import in Studio, and accept import dialog defaults; the first import came in mangled and was reinserted. *(demo, medium; blender-roblox-export-import)*
- c3: [1:35] Speaker uses the Rig Builder plugin, R15, Block Rig to place the accessory against a character shape; other rigs are possible. *(demo, medium; rigging-animation)*
- c4: [2:16] Asset Creator plugin converts a selected part into an accessory: pick character, accessory type (e.g. Left Shoulder), and Classic style, creating a named attachment. *(demo, medium; avatar-ugc-accessories)*
- c5: [3:38] Attachment point initially too high; test in Play mode by dragging accessory onto character and move the attachment down to fit the shoulder. *(demo, medium; avatar-ugc-accessories)*
- c6: [4:44] Save to Roblox with Avatar item (not Development item), set asset category to Shoulder Accessory; validation succeeded for the model. *(demo, medium; avatar-ugc-accessories)*
- c7: [4:55] Speaker's model has about 3.2k triangles; he says 4,000 triangles is too many for a UGC item and causes problems. Opinion from one test, not a documented spec. *(opinion, low; mesh-texture-limits)*
- c8: [5:45] Upload cost shown as 750 Robux for the test item; later the speaker says a regular non-limited upload costs 1,000 Robux. *(demo, low; avatar-ugc-accessories)*
- c9: [6:38] Limited items cost 100 Robux per copy; limited publishing costs 15,000 Robux; minimum resale price for a shoulder accessory is 20 Robux. *(doc, low; avatar-ugc-accessories)*
- c10: [8:00] Speaker says Roblox takes 30% commission only after the 1,000 Robux upload fee is recovered in sales, i.e. after 3,000 Robux earned. *(opinion, low; automation-and-creator-workflows)*
- c11: [8:37] Submitted items show pending for a period while Roblox verifies them before purchase; non-public test items did not require the full upload fee. *(demo, low; avatar-ugc-accessories)*

## Numbers
- n1: **triangle count (test model)**: ~3,200 
- n2: **triangle threshold cited by speaker**: 4,000 (claimed) 
- n3: **upload cost (test item)**: 750 Robux 
- n4: **regular upload cost**: 1,000 Robux 
- n5: **limited item cost per copy**: 100 Robux 
- n6: **limited publishing cost**: 15,000 Robux 
- n7: **minimum resale price, shoulder accessory**: 20 Robux 
- n8: **commission threshold**: 30% after 3,000 Robux recovered 

## Techniques
- t1: **FBX export and MeshPart import**: Export FBX from Blender via File > Export. In Studio, add MeshPart, use the file icon to open the FBX, accept defaults, check result, reinsert if mangled.
- t2: **Align to R15 Block Rig**: Insert Rig Builder R15 Block Rig from Plugins. Hold Alt while scaling. Position the part on the rig where the accessory would sit.
- t3: **Asset Creator accessory setup**: Run Asset Creator plugin, pick the part, choose the character and accessory type, pick Classic, then rename and scale. Test in Play mode by dragging onto the character, then move the attachment point.
- t4: **Save to Roblox as Avatar item**: Right-click accessory, Save to Roblox, choose Avatar item, set name, description, category, and tags, then publish.

## Quotes (brief, for attribution)
> if you have 4,000 for a ugc item it does mess up  (at 4:55, Kingkade 3D)
> it looks like you only have to pay the th000 Robux if you do want to sell it  (at 8:37, Kingkade 3D)

## Contradictions flagged
- Upload cost is 750 Robux (test item at 5:45) (vs Regular upload cost is stated as 1,000 Robux at 7:59 in the same video)
- Minimum price for a non-limited item is 20 Robux and free is not allowed (vs Speaker also says setting price to zero makes it free, 'if you want it to be free then it would be zero')

## Points to
- Asset Creator plugin (linked in video description)
- Rig Builder plugin (Roblox Studio)
- Dusty Trip (Roblox game, inspiration for model)
