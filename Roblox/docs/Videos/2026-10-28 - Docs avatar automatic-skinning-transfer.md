---
title: "Docs: avatar / automatic-skinning-transfer"
url: https://create.roblox.com/docs/avatar/automatic-skinning-transfer.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / automatic-skinning-transfer

[Open](https://create.roblox.com/docs/avatar/automatic-skinning-transfer.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Automatic Skinning Transfer: layered accessories deform with the character body without manual skinning. Covers enabling LoadCharacterLayeredClothing and WrapLayer.AutoSkin modes, RBX_Leader/RBX_Follower joints for eyelashes/eyebrows, cage modification, and per-category AutoSkin recommendations.

## Tips
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[3d-modeling-rigging-and-animation]]** Enable StarterPlayer.LoadCharacterLayeredClothing, then set WrapLayer.AutoSkin on each layered accessory to EnabledOverride or EnabledPreserve. No accessory skinning is needed.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[3d-modeling-rigging-and-animation]]** Use EnabledOverride to replace existing accessory skinning at runtime; use EnabledPreserve to keep existing skinning and auto-generate only when none exists.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[3d-modeling-rigging-and-animation]]** For eyelashes and eyebrows, skin vertices to RBX_Leader (eyelid/browline edges) and RBX_Follower (remaining strands), placing joints directly beneath Root.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[3d-modeling-rigging-and-animation]]** RBX_Leader/RBX_Follower vertices must be weighted 1.0 to the joint, not partial. Accessories using them must be EnabledOverride. Eyelash/eyebrow types require these joints.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[3d-modeling-rigging-and-animation]]** Body part meshes containing RBX_Leader or RBX_Follower joints are rejected by validation.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[building-art-and-assets]]** Test auto-skinned accessories on multiple avatar body types and animations; the transfer is based on closest distance to the body's outer cage.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[building-art-and-assets]]** Trim irrelevant regions from the outer cage (e.g. keep only head for beards) to stop skinning from wrong body parts. Partial cages are in-game only, not Marketplace-valid.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[common-mistakes]]** Do not auto-skin hats, hair or glasses; set AutoSkin to Disabled since they should stay rigid and skinning introduces unwanted deformation.
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) **[[ugc-and-avatar-economy]]** Marketplace validation rejects accessories with partial cages; only use partial cages for in-game assets.

## Numbers
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) RBX_Leader/RBX_Follower vertex weight: **1.0 required (no partial weights)** (Special skinning joints must be fully weighted when uploaded as UGC)
- [page](https://create.roblox.com/docs/avatar/automatic-skinning-transfer) AutoSkin suggested per category: **Beard/Eyebrow/Eyelash: EnabledOverride; Hair/Hat/Glasses: Disabled; Shirt/Pants/Shoes: EnabledOverride or EnabledPreserve** (Docs table of recommended WrapLayer.AutoSkin values)

## Tools
Roblox Studio, Blender, WrapLayer.AutoSkin property

## He points to
- Skin a humanoid model (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
