---
type: research-source
id: web-b24bec908c
title: "Roblox docs: art/accessories/publish-eyebrows-eyelashes"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/publish-eyebrows-eyelashes.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "roblox-import-pipeline"]
---
# web-b24bec908c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on publishing eyelashes and eyebrows as layered Accessory objects bundled with a character body Model for Marketplace upload. Covers Importer import, Accessory Fitting Tool steps, MeshPart generation, parenting under the character Model, naming, and the restriction that only eyelashes, eyebrows and hair can be bundled with a body. Tangential to Blender scripting and the Blender-to-Roblox pipeline.

## Claims
- c1: Only eyelashes, eyebrows and hair can be bundled with a body on Marketplace upload; horns, makeup, glitter and other facial cosmetics are not accepted. *(doc, high; avatar-ugc-accessories)*
- c2: Eyelashes and eyebrows must use Automatic Skinning Transfer with RBX_Leader and RBX_Follower special joints to be published on the Marketplace. *(doc, high; avatar-ugc-accessories)*
- c3: Face accessory and body FBX files are imported via the Importer; for the reference body set Rig General > Rig Type to Rthro. *(doc, high; roblox-import-pipeline)*
- c4: Accessory Fitting Tool workflow: select Eyelash or Eyebrow model, choose Accessory > Eyelash or Accessory > Eyebrow asset type, then Generate MeshPart Accessory. *(doc, high; avatar-ugc-accessories)*
- c5: Face Accessory objects are dragged into the character Model in the Outliner and auto-attach; rename to EyelashAccessory or EyebrowAccessory if required. *(doc, high; avatar-ugc-accessories)*
- c6: Eyelashes and eyebrows are layered accessories that must include caging, rigging and skinning components to meet accessory requirements. *(doc, medium; avatar-ugc-accessories)*

## Numbers
- n1: **Rig Type for reference body**: Rthro 

## Techniques
- t1: **Accessory Fitting Tool face accessory setup**: Import FBX via Importer; run Accessory Fitting Tool on eyelash/eyebrow model; choose Accessory asset type; generate MeshPart Accessory; drag Accessory into character Model; upload with body.

## Points to
- https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories
- https://create.roblox.com/docs/avatar/automatic-skinning-transfer
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/marketplace/marketplace-policy
- https://create.roblox.com/docs/marketplace/publish-to-marketplace
