---
type: research-source
id: web-bb1d4731b0
title: "Roblox docs: art/characters/creating/remove-extra-bones"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/remove-extra-bones.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 3
density: medium
tags: ["research-source", "web", "blender-roblox-export-import", "rigging-animation"]
---
# web-bb1d4731b0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on removing extra head helper bones from a Blender character template after combining head geometry. Keeps DynamicHead and facial animation bones (they carry skinning data); deletes other head child joints in Edit mode. Omitting this step breaks validation against the standard geometry and joint hierarchy.

## Claims
- c1: Extra head helper bones in the Blender character template must be removed for the character to validate; they carry no skinning data. *(doc, high; rigging-animation)*
- c2: Do not delete facial animation bones parented under DynamicHead; they hold skinning data that drives facial animation. *(doc, high; rigging-animation)*
- c3: Skipping combine-head-geometry and bone removal causes validation failure because the character deviates from standard geometry and joint hierarchy. *(doc, high; rigging-animation)*
- c4: Workflow: show Armature, expand Joints in Outliner (Shift-click expand), enter Edit mode, Shift-select head child joints under Head except DynamicHead, right-click > Delete Selected Bones. *(doc, high; blender-roblox-export-import)*

## Techniques
- t1: **Delete extra head bones in Edit mode**: Toggle Armature visibility; expand Joints hierarchy in Outliner via Shift-click; enter Edit mode; under Head select all child joints except DynamicHead; right-click viewport > Delete Selected Bones.

## Quotes (brief, for attribution)
> do not delete any of the facial animation bones parented within DynamicHead, as these include important skinning data that drives facial animation.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/combine-head-geometry.md
- /art/characters/creating/verify-attachments
- avatar/character-bodies/specifications (geometry, rigging)
