---
type: research-source
id: web-18ae023bf8
title: "Roblox docs: art/accessories/creating-rigid/converting"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating-rigid/converting.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "creator-workflows", "roblox-import-pipeline"]
---
# web-18ae023bf8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc page on converting a fitted rigid MeshPart into an Accessory using the Accessory Fitting Tool (AFT): select Part, choose Accessory asset type with attachment location (example: Back), adjust position/scale/rotation in AFT preview and viewport, click Generate MeshPart Accessory, then test via Avatar Setup. Covers next steps: publish, equip via HumanoidDescription, or save to Toolbox. Not about Blender specifically.

## Claims
- c1: Imported rigid accessory MeshPart is converted to Class.Accessory via Avatar tab > Accessory (Accessory Fitting Tool), not by Blender export. *(doc, high; roblox-import-pipeline)*
- c2: AFT asset type set to Accessory with a dropdown choosing attachment body location; the tutorial uses Back. *(doc, high; avatar-ugc-accessories)*
- c3: Doc says the clothing mannequin in the viewport does not accurately show how rigid accessories attach; use the AFT preview character instead. *(doc, high; avatar-ugc-accessories)*
- c4: Position, scale and rotation are adjusted with Move, Scale and Rotate tools; clicking back into the AFT panel reselects the accessory. *(doc, high; avatar-ugc-accessories)*
- c5: Final step: Generate MeshPart Accessory button, then test by equipping and using Avatar Setup tool. *(doc, high; avatar-ugc-accessories)*
- c6: Converted accessory can be published to Marketplace, equipped via HumanoidDescription, dragged under a character Model, or saved to Toolbox. *(doc, high; creator-workflows)*

## Techniques
- t1: **AFT rigid accessory conversion**: Avatar tab > Accessory; select MeshPart as Part; Next; set Asset Type Accessory and attachment location; Next; adjust with Move/Scale/Rotate in AFT preview; Generate MeshPart Accessory; test with Avatar Setup.

## Quotes (brief, for attribution)
> it's important to use the Accessory Fitting Tool (AFT) to correctly preview the placement and apply the correct configurations to your accessory.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/art/accessories/creating-rigid/publishing
- https://create.roblox.com/docs/characters/appearance
- https://create.roblox.com/docs/projects/assets/toolbox
