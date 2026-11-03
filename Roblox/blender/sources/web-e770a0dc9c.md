---
type: research-source
id: web-e770a0dc9c
title: "Roblox docs: art/accessories/creating/converting"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/converting.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "open-cloud-automation"]
---
# web-e770a0dc9c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on converting a layered clothing MeshPart into a Class.Accessory using the Accessory Fitting Tool (AFT). Covers the Avatar tab > Accessory workflow, Part selection, Clothing asset type (Shirt example), preview with sample characters, and Generate MeshPart Accessory. Says nothing about Blender, blender-mcp, bpy, or export settings; only the final in-Studio step.

## Claims
- c1: Final step of layered clothing: in Studio Avatar tab, click Accessory to open AFT, set Part to the layered MeshPart, Next, choose asset type Clothing and subtype (tutorial uses Shirt), Next. *(doc, high; avatar-ugc-accessories)*
- c2: AFT preview shows a default character wearing the layered accessory; cage adjustments can be made in Studio or larger changes in third-party modeling software. *(doc, high; avatar-ugc-accessories)*
- c3: Clicking Generate MeshPart Accessory creates a Class.Accessory object in the project. *(doc, high; avatar-ugc-accessories)*
- c4: Converted accessory can be uploaded to Marketplace, equipped via HumanoidDescription, or saved to Toolbox. *(doc, medium; open-cloud-automation)*

## Techniques
- t1: **AFT layered-clothing conversion**: Avatar tab > Accessory; pick MeshPart in Explorer; Next; set Clothing type; Next; test on sample characters/animations; Generate MeshPart Accessory.

## Points to
- https://create.roblox.com/docs/art/accessories/creating/importing
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/art/accessories/creating-rigid/publishing
- https://create.roblox.com/docs/characters/appearance
