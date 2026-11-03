---
type: research-source
id: web-e59e06c37f
title: "Roblox docs: avatar/automatic-skinning-transfer"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/automatic-skinning-transfer.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "other"]
---
# web-e59e06c37f

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on Automatic Skinning Transfer for layered/facial accessories: enabling WrapLayer.AutoSkin (EnabledOverride/EnabledPreserve), cage-based transfer behavior, RBX_Leader/RBX_Follower joints for eyelashes/eyebrows, Marketplace cage and joint rules, and per-category AutoSkin recommendations. Does not cover Blender MCP, bpy, or FBX export pipeline.

## Claims
- c1: Automatic Skinning Transfer makes layered and facial accessories deform with the body without manual skinning; the engine creates and applies skinning at runtime. *(doc, high; avatar-ugc-accessories)*
- c2: Requires StarterPlayer.LoadCharacterLayeredClothing enabled and WrapLayer.AutoSkin set to EnabledOverride or EnabledPreserve on the layered Accessory. *(doc, high; avatar-ugc-accessories)*
- c3: EnabledOverride replaces existing accessory skinning; EnabledPreserve keeps existing skinning and only generates new data if none exists. *(doc, high; avatar-ugc-accessories)*
- c4: Transfer uses the character body's outer cage; accessories must still meet layered accessory requirements. Transfer is based on closest distance between accessory and inner cage, so wrong cage shapes cause wrong deformation. *(doc, high; avatar-ugc-accessories)*
- c5: Special joints RBX_Leader and RBX_Follower allow controlled transfer for eyelashes and eyebrows; Follower vertices transfer based on nearest leader vertex. Create them directly beneath Root. *(doc, high; avatar-ugc-accessories)*
- c6: RBX_Leader/RBX_Follower rules: no partial weights (must be 1.0); if present, accessory must be EnabledOverride; body part meshes containing these joints are rejected by validation; Eyebrow and Eyelash types require them. *(doc, high; avatar-ugc-accessories)*
- c7: Partial cages are rejected by Marketplace validation; modifying the outer cage to head-only is allowed for in-game assets only. *(doc, high; avatar-ugc-accessories)*
- c8: Suggested AutoSkin settings: Beard, Eyebrow, Eyelash = EnabledOverride; Hair, Hat, Glasses = Disabled; Shirt, Pants, Shoes = EnabledOverride or EnabledPreserve. *(doc, high; avatar-ugc-accessories)*
- c9: Hat and glasses accessories should stay rigid with no skinning data, since auto-transfer introduces unwanted deformation. *(doc, high; avatar-ugc-accessories)*
- c10: In Blender, vertex groups are auto-created when a bone object is made; manage assignments under Object Data Properties > Vertex Groups. *(doc, medium; avatar-ugc-accessories)*
- c11: Source does not cover Blender MCP, bpy scripting, or Blender-to-Roblox FBX/glTF export settings; off-topic for the requested Claude/Blender pipeline. *(doc, high; other)*

## Numbers
- n1: **Vertex weight for RBX_Leader/RBX_Follower joints**: 1.0 

## Techniques
- t1: **Leader/Follower eyelash skinning**: Skin eyelid-adjacent vertices to RBX_Leader, rest to RBX_Follower at weight 1.0; create joints under Root; set AutoSkin EnabledOverride.
- t2: **Cage trimming for in-game assets**: Remove non-relevant outer cage parts (e.g., keep head only) so transfer samples correct region; not valid for Marketplace.

## Quotes (brief, for attribution)
> No skinning of accessory geometry is required to use Automatic Skinning Transfer.  (create.roblox.com)
> You can't upload assets with a partial cage to the Marketplace.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/rigging
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model
- https://create.roblox.com/docs/avatar/character-bodies/specifications
