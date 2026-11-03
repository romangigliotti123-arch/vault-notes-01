---
type: research-source
id: off-avatar_automatic-skinning-transfer
title: "Roblox Creator Docs: avatar_automatic-skinning-transfer"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/automatic-skinning-transfer"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "other"]
---
# off-avatar_automatic-skinning-transfer

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs on Automatic Skinning Transfer for layered and facial accessories: enable LoadCharacterLayeredClothing and WrapLayer.AutoSkin (EnabledOverride/EnabledPreserve), cage-based runtime skinning, RBX_Leader/RBX_Follower joints for eyelashes and brows, partial-cage Marketplace restrictions, and per-category AutoSkin recommendations. Only tangential to Blender/Claude workflows.

## Claims
- c1: Automatic Skinning Transfer requires StarterPlayer.LoadCharacterLayeredClothing enabled, and WrapLayer.AutoSkin set to EnabledOverride or EnabledPreserve on the layered Accessory. *(doc, high; avatar-ugc-accessories)*
- c2: EnabledOverride replaces existing accessory skinning at runtime; EnabledPreserve keeps existing skinning and only generates new skinning if none exists. *(doc, high; avatar-ugc-accessories)*
- c3: Skinning is computed at runtime by the engine from the character body's outer cage; accessory geometry needs no skinning. *(doc, high; avatar-ugc-accessories)*
- c4: Special joints RBX_Leader and RBX_Follower allow controlled transfer; Follower vertices transfer based on their nearest leader vertex. Recommended under Root. *(doc, high; avatar-ugc-accessories)*
- c5: RBX_Leader/RBX_Follower vertices cannot be partially weighted; must have weight 1.0. Body meshes containing these joints are rejected by validation; Eyebrow and Eyelash types require them with EnabledOverride. *(doc, high; avatar-ugc-accessories)*
- c6: Partial cages are rejected by Marketplace validation; they are allowed only for in-game assets. *(doc, high; avatar-ugc-accessories)*
- c7: Suggested AutoSkin settings: Beard, Eyebrow, Eyelash use EnabledOverride; Hair, Hat, Glasses use Disabled; Shirt, Pants, Shoes use EnabledOverride or EnabledPreserve. *(doc, high; avatar-ugc-accessories)*
- c8: Auto-skinning uses closest distance between accessory and inner cage, so a blocky full-body cage can make a beard deform to the chest; trimming cage to head fixes it but is not valid for Marketplace. *(doc, medium; avatar-ugc-accessories)*
- c9: Source is Roblox docs for Automatic Skinning Transfer; it does not cover Blender MCP, bpy scripting, or the Blender-to-Roblox export pipeline. *(doc, high; other)*

## Numbers
- n1: **RBX_Leader/RBX_Follower vertex weight**: 1.0 

## Techniques
- t1: **Leader/Follower skin transfer joints**: Create RBX_Leader and RBX_Follower bones under Root in Blender; assign eyelid-edge verts to RBX_Leader at weight 1.0 and the rest to RBX_Follower; set AutoSkin to EnabledOverride.

## Points to
- https://create.roblox.com/docs/art/modeling/rigging.md
- https://create.roblox.com/docs/avatar/layered-accessories/specifications.md
- https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model.md
- https://create.roblox.com/docs/avatar/character-bodies/specifications.md
