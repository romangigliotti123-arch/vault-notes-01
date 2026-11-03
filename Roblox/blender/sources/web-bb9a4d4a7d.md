---
type: research-source
id: web-bb9a4d4a7d
title: "Roblox docs: art/characters/creating/verify-attachments"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/verify-attachments.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "other", "rigging-animation"]
---
# web-bb9a4d4a7d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on verifying attachment placement for a Blender character before Studio import. Covers _Att attachment points (Hat, Hair, FaceFront) that must be nudged when head geometry changes, with steps to isolate them in the Outliner and Grab them along Y to about half-embedded. Thin on claude/bpy/MCP content; mainly a manual Blender step in the character-creation sequence.

## Claims
- c1: Roblox creator docs: attachment points are non-rendered avatar objects ending in _Att where rigid accessories attach; templates include them at expected locations. *(doc, high; rigging-animation)*
- c2: After changing head shape in Blender, only Hat, Hair and FaceFront attachments need adjusting; each attachment should overlap roughly halfway with the character mesh. *(doc, high; avatar-ugc-accessories)*
- c3: Attachment placement is verified and adjusted before export when model shape was changed; the tutorial example is a goblin with a shorter head than the template. *(doc, high; avatar-ugc-accessories)*
- c4: Workflow to view attachments: enable disabled objects in Outliner, hide Joints parent via Shift+click Hide, then unhide Head_Geo, Hat_Att, Hair_Att, FaceFront_Att; disable Disable In Viewport if needed. *(doc, high; other)*
- c5: Adjust attachments by selecting them, entering Edit mode, and using Grab to move along the Y-axis (Blender vertical) until about halfway embedded in the head. *(doc, high; other)*

## Techniques
- t1: **Isolate and move attachments in Blender**: Enable disabled objects in Outliner; hide Joints with Shift+click; unhide Head_Geo and the Hat/Hair/FaceFront _Att objects; select attachments, Edit mode, Grab along Y until ~half embedded.

## Quotes (brief, for attribution)
> Center attachment points at their respective locations. Each attachment should overlap approximately halfway with the character's mesh.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/characters/creating/index
- https://create.roblox.com/docs/art/characters/creating/remove-extra-bones
- https://create.roblox.com/docs/art/characters/creating/final-checks
