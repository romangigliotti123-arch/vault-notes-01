---
type: research-source
id: off-avatar_classic-clothing
title: "Roblox Creator Docs: avatar_classic-clothing"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/classic-clothing"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories"]
---
# off-avatar_classic-clothing

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on 2D classic clothing (T-shirt, Shirt, Pants) made from images, not Blender. Covers template pixel layouts for shirts/pants, testing via Studio Block Avatar rig with ShirtGraphic/Shirt/Pants objects, and uploading via Creator Dashboard for an 80 Robux fee. No Blender, bpy, MCP, FBX/glTF or Claude content. Only tangentially relevant.

## Claims
- c1: Classic clothing are 2D image decals applied to a classic character's surface; the page says you need only an image editor and browser to create them. *(doc, high; avatar-ugc-accessories)*
- c2: Doc warns many user-generated avatars on the Marketplace do not support 2D classic clothing; modern 3D cosmetics are recommended instead. *(doc, high; avatar-ugc-accessories)*
- c3: T-shirts are square images, e.g. 512x512, and display on the front torso of a blocky character. *(doc, high; avatar-ugc-accessories)*
- c4: Shirt and pants templates use face-region layouts: 128x128 large square (FRONT/BACK), 64x128 tall rectangle (torso sides, arm/leg sides), 128x64 wide rectangle (UP/DOWN), 64x64 small square (arm/leg top/bottom). *(doc, high; avatar-ugc-accessories)*
- c5: Pants art whose shoe designs extend too far up the leg regions reads as part of the pants; keep shoes near the bottom of leg regions. *(doc, medium; avatar-ugc-accessories)*
- c6: Testing is done in Studio: Avatar tab > Character > Block Avatar rig, insert ShirtGraphic (T-shirt), Shirt, or Pants under Rig, then set the template property to the uploaded image. *(doc, high; avatar-ugc-accessories)*
- c7: Property to set: ShirtGraphic.Graphic for T-shirts, Shirt.ShirtTemplate for shirts, Pants.PantsTemplate for pants. *(doc, high; avatar-ugc-accessories)*
- c8: Uploading a classic clothing item to the Marketplace costs an 80 Robux upload fee per submission, subject to creator requirements. *(doc, high; avatar-ugc-accessories)*
- c9: Upload path: Creator Dashboard > Avatar Items > Classics tab, set Asset Type to T-Shirt/Shirt/Pants, fill Name and Description, click Upload. *(doc, high; automation-and-creator-workflows)*
- c10: Items are managed in Creator Dashboard Classics tab; you can edit name, description, On Sale toggle, and price in Robux. *(doc, high; avatar-ugc-accessories)*

## Numbers
- n1: **T-shirt image size**: 512x512 px (square) 
- n2: **Large square template (FRONT/BACK)**: 128x128 px 
- n3: **Tall rectangle template (sides)**: 64x128 px 
- n4: **Wide rectangle template (UP/DOWN)**: 128x64 px 
- n5: **Small square template (arm/leg top/bottom)**: 64x64 px 
- n6: **Upload fee per classic clothing submission**: 80 Robux 

## Techniques
- t1: **Classic clothing Studio test**: Avatar tab > Character > choose Block Avatar; hover Rig, click plus, insert ShirtGraphic/Shirt/Pants; select it; set Graphic/ShirtTemplate/PantsTemplate to uploaded image; verify on Rig.
- t2: **Start from provided templates**: Download Classic-Clothing-Templates.zip for shirt/pants; edit in image editor; export .png or .jpg before testing and uploading.

## Quotes (brief, for attribution)
> Many user-generated avatars on the Marketplace do not support 2D classic clothing.  (create.roblox.com)
> you can upload and sell your clothing item on the Marketplace for an upload fee of 80 Robux per submission.  (create.roblox.com)

## Points to
- https://create.roblox.com/dashboard/creations
- https://www.roblox.com/catalog
- https://create.roblox.com/docs/avatar/index.md
- Classic-Clothing-Templates.zip
