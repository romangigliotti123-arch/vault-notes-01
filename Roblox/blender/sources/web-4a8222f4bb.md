---
type: research-source
id: web-4a8222f4bb
title: "Roblox docs: art/accessories/creating-rigid/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating-rigid/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "roblox-import-pipeline"]
---
# web-4a8222f4bb

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official tutorial for making a first rigid accessory: model a simple mesh in Blender, import to Studio, convert to a Class.Accessory that can be sold, saved to Toolbox, or used in games. Covers rigid accessories attaching to avatar attachment points. Does not mention blender-mcp, bpy scripting, or Claude. Marketplace listing requires Plus/Premium, upload fee, publishing advance.

## Claims
- c1: Rigid accessories attach to avatar attachment points; buyers can adjust position and rotation away from the attachment point per avatar body type. *(doc, high; avatar-ugc-accessories)*
- c2: Listing a rigid accessory on the Marketplace requires a Roblox Plus or Premium account, an upload fee, and a publishing advance. *(doc, high; avatar-ugc-accessories)*
- c3: Workflow: create simple 3D model in Blender, import into Studio, then convert to a Marketplace-ready Class.Accessory object. *(doc, high; roblox-import-pipeline)*
- c4: The same concepts can be applied to other third-party modeling applications, not only Blender. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **Account requirement**: Roblox Plus or Premium to list on Marketplace 

## Techniques
- t1: **Blender to Studio to Class.Accessory**: Model simple mesh in Blender, import into Studio, convert the mesh into a Class.Accessory object for Marketplace, toolbox, or in-game use.

## Quotes (brief, for attribution)
> Rigid accessories are 3D objects that attach to attachment points around an avatar character's body.  (create.roblox.com)

## Points to
- https://www.roblox.com/catalog
- ../../../marketplace/marketplace-policy.md#creator-requirements
- /art/accessories/creating-rigid/modeling-setup
