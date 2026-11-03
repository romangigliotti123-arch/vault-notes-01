---
type: research-source
id: web-046b20e0cd
title: "Roblox docs: art/characters/creating/modeling-tips"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/modeling-tips.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "web", "blender-roblox-export-import", "other"]
---
# web-046b20e0cd

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page with beginner Blender modeling tips for character creation: hiding inactive objects in the Outliner (with Shift-click bulk hide on Cage/Joints parents) and enabling wireframe view per object. Contains no blender-mcp, bpy, Claude, export, or Roblox import specifics, so it is only marginally relevant to the topic.

## Claims
- c1: Roblox character modeling docs recommend hiding inactive objects in Blender's Outliner via the Hide In Viewport icon to avoid unintended edits to other objects or collections. *(doc, high; blender-roblox-export-import)*
- c2: Shift-clicking the Hide In Viewport icon on a parent object such as Cage or Joints bulk hides/unhides its child objects, skipping disabled ones. *(doc, high; blender-roblox-export-import)*
- c3: To view mesh vertices, enable Wireframe under Object Properties > Viewport Display for the selected object (example: Head_Geo). *(doc, high; blender-roblox-export-import)*
- c4: Source is a generic Blender UI tips page for Roblox character modeling; it does not cover blender-mcp, bpy scripting, Claude integration, or export settings. *(doc, high; other)*

## Techniques
- t1: **Bulk hide child objects**: In Outliner, select parent (Cage or Joints), Shift-click Hide In Viewport icon to toggle visibility of its children.
- t2: **Wireframe overlay for modeling**: Select Head_Geo, open Object Properties, enable Wireframe under Viewport Display to see vertices over the shaded mesh.

## Quotes (brief, for attribution)
> hide objects you aren't editing by enabling the Hide In Viewport icon. This cleans up your workspace and helps ensure you don't make unintentional changes  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/characters/creating/modeling-best-practices
- https://create.roblox.com/docs/art/characters/creating/sculpting
