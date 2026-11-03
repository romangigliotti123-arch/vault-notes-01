---
type: research-source
id: off-marketplace_publish-to-marketplace
title: "Roblox Creator Docs: marketplace_publish-to-marketplace"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/marketplace/publish-to-marketplace"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories"]
---
# off-marketplace_publish-to-marketplace

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on publishing avatar items to the Marketplace from Studio. It does not cover Blender, blender-mcp, bpy, or FBX/glTF import. Relevant only to the final Roblox step: Studio "Save to Roblox", Accessory objects, upload and publish limits, and updating published items.

## Claims
- c1: Accessories and clothing must be an Accessory object; bodies and heads must be a Model. Convert a Model to Accessory with the Accessory Fitting Tool. *(doc, high; avatar-ugc-accessories)*
- c2: Upload flow: right-click object in Explorer > Save to Roblox > Submit As Avatar Asset > choose Asset type (validation starts on selection) > fill Title and Creator > Submit (pays upload fee, goes to moderation). *(doc, high; avatar-ugc-accessories)*
- c3: Shoes must be two separate accessories named LeftShoeAccessory and RightShoeAccessory, grouped as a Model before upload. *(doc, high; avatar-ugc-accessories)*
- c4: Free Limiteds are capped at 50 publishes per day; paid Limiteds and bodies/heads have no publish limit. Uploading has no limit for any type. *(doc, high; avatar-ugc-accessories)*
- c5: Paid Limited quantity maximum is 3000; free Limiteds have no quantity maximum. *(doc, high; avatar-ugc-accessories)*
- c6: Published rigid or layered accessories can be updated in place via Save to Roblox with 'Update an existing asset' and the asset ID; the asset ID, sales and owners are kept, and each update costs the upload fee and goes through moderation. *(doc, high; avatar-ugc-accessories)*
- c7: Bodies and heads, and bundles, cannot be updated after upload; only rigid and layered accessories can. *(doc, high; avatar-ugc-accessories)*
- c8: Studio validation errors name the failing check on hover (e.g. missing FaceControls on an Avatar Head); fixes usually require re-modeling and re-importing. *(doc, high; automation-and-creator-workflows)*
- c9: Copy limits per user and resellable status cannot be decreased or disabled after publishing; copy limits can only be increased. *(doc, high; avatar-ugc-accessories)*
- c10: Scheduled sales can be set up to 30 days in advance. *(doc, high; avatar-ugc-accessories)*

## Numbers
- n1: **Free Limited publish limit**: 50 per day Publishing enable-on-sale limit for free Limiteds
- n2: **Paid Limited max quantity**: 3000 Maximum quantity for paid Limited items
- n3: **Creations recents view**: 50 items Most recently uploaded avatar items shown under Recents
- n4: **Scheduled sale lead time**: 30 days Maximum advance scheduling for item sale

## Techniques
- t1: **Save to Roblox upload**: Build Accessory in Studio, right-click in Explorer, Save to Roblox, Avatar Asset, pick type, fix validation errors on hover, set title and creator, submit for moderation.
- t2: **In-place item update**: Open item in Studio, Save to Roblox, enable Update an existing asset, enter asset ID, submit. Use for fit, cage, mesh or texture fixes only.

## Quotes (brief, for attribution)
> For accessories and clothing, the item must be an Class.Accessory object.  (create.roblox.com)
> The update keeps the item's asset ID, sales history, and existing owners, and owners receive the updated version automatically.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/marketplace/moderation
