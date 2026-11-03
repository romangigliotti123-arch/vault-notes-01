---
type: research-source
id: yt-Lmnpzo--qdg
title: "How To Make UGC Accessories In Roblox"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=Lmnpzo--qdg"
published: "2026-08-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 3
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# yt-Lmnpzo--qdg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video walkthrough of making UGC back accessories in Roblox Studio from FBX meshes (Blender-exported bottle caps). Covers importing, R15 Rig Builder dummy placement, Asset Creator plugin attachment selection (body back, hat, hair, waist center), testing via Rep Kids Storage, UGC Thumbnail Tool configuration, saving to Roblox with fees, moderation, and non-limited pricing floor. Does not cover blender-mcp or bpy scripting.

## Claims
- c1: [0:00] Recommends exporting Blender meshes as FBX over OBJ because FBX keeps the texture on the mesh. *(opinion, medium; blender-roblox-export-import)*
- c2: [0:46] Rig Builder plugin must use an R15 dummy; an R6 dummy will not work for accessory placement. *(experience, high; rigging-animation)*
- c3: [1:26] Accessory mesh is placed on the dummy as if worn; stacking identical items lets all be placed in the same position at once. *(experience, medium; avatar-ugc-accessories)*
- c4: [1:58] Asset Creator plugin is used to convert a mesh into an accessory; the free UGC Thumbnail Tool works about the same as the paid $20 alternative. *(experience, medium; automation-and-creator-workflows)*
- c5: [2:39] Attachment point choices in Asset Creator include body back for back accessories, hat, hair, and waist center for belts. *(experience, high; avatar-ugc-accessories)*
- c6: [2:39] Intended character type set to classic in the Asset Creator flow; the tool teleports the accessory about 10 studs up and may resize it. *(experience, medium; avatar-ugc-accessories)*
- c7: [3:20] Renaming parts inside Roblox Studio has no real effect on the uploaded item. *(opinion, low; automation-and-creator-workflows)*
- c8: [3:42] Test accessories by deleting the character's current accessories and dragging the item from ReplicatedStorage onto the character while in Test mode. *(experience, medium; avatar-ugc-accessories)*
- c9: [4:22] To adjust fit, edit the accessory's handle attachment position (hat attachment) instead of redoing placement; moving it up sinks it into the head, down moves it away. *(experience, medium; avatar-ugc-accessories)*
- c10: [4:47] Thumbnail matters for catalog clicks; UGC Thumbnail Tool configuration can be copied and pasted to selected accessories but each must be reopened and accepted to apply. *(experience, medium; avatar-ugc-accessories)*
- c11: [6:20] Save to Roblox requires a name, a description, content type item, and asset category (e.g. back accessory); validation warns if mesh is too small or too big. *(experience, high; avatar-ugc-accessories)*
- c12: [6:20] Uploading a UGC accessory costs 80 Robux; this is only the upload fee, not the final price. *(experience, high; automation-and-creator-workflows)*
- c13: [6:58] Items need moderation approval before they appear for publishing in the Creations page. *(experience, high; avatar-ugc-accessories)*
- c14: [7:38] Non-limited accessories have a price floor; for a back accessory the floor was 140 Robux at time of recording. *(experience, high; avatar-ugc-accessories)*
- c15: [8:18] Publishing a back accessory for sale cost 1,000 Robux in the video; hats cost 1,500 Robux. Publishing is only needed if others can buy the item. *(experience, high; avatar-ugc-accessories)*
- c16: [8:18] Accessories uploaded are automatically added to the creator's inventory, so no publish fee is needed for personal use. *(experience, medium; avatar-ugc-accessories)*

## Numbers
- n1: **Upload fee to save to Roblox**: 80 Robux Upload cost shown before submit; not the final price
- n2: **Back accessory price floor (non-limited)**: 140 Robux Minimum price for non-limited back accessory
- n3: **Publish fee, back accessory**: 1,000 Robux Fee to publish for sale
- n4: **Publish fee, hat accessory**: 1,500 Robux Fee reported for hats published the previous day
- n5: **Minimum listed price shown for own hats**: 95 Robux Described as lowest possible price
- n6: **Teleport offset after Asset Creator conversion**: 10 studs up Accessory moved up on conversion; may resize
- n7: **Paid UGC Thumbnail Tool cost**: $20 Free alternative used in video

## Techniques
- t1: **Rig Builder R15 dummy placement**: Open Rig Builder plugin, choose R15 (not R6), spawn block rig dummy, place mesh on it as if worn, centered on target body part.
- t2: **Asset Creator accessory conversion**: Asset Creator > Accessory > select mesh part > select dummy > choose attachment (body back, hat, hair, waist center) > classic > next to duplicate as accessory.
- t3: **In-Test fit check**: Click Test, keep game running, delete existing accessories in Workspace character, drag item from ReplicatedStorage onto character, adjust handle attachment.
- t4: **UGC Thumbnail framing**: Select accessory, open UGC Thumbnail Tool, adjust camera, accept; copy config and paste into selected items, then reopen and accept each.
- t5: **Save and export to Roblox**: Right-click accessory > Save and Export > Save to Roblox; fill name, description, content type item, asset category; validate; set creator (user or group); upload.

## Quotes (brief, for attribution)
> I would recommend FBX just because it keeps the texture on there.  (at 0:00, Kingkade 3D)
> If you spawn in an R6, it's not going to work.  (at 0:46, Kingkade 3D)
> you only have to pay this if you want other people to be able to buy it.  (at 8:18, Kingkade 3D)

## Points to
- Rig Builder plugin
- Asset Creator plugin
- UGC Thumbnail Tool (paid $20 and free version)
- Rep Kids Storage / ReplicatedStorage
- Roblox Plus discount
