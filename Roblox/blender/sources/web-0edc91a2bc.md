---
type: research-source
id: web-0edc91a2bc
title: "Roblox docs: art/accessories/creating/armature-setup"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/armature-setup.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 4
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "rigging-animation"]
---
# web-0edc91a2bc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on armature setup for clothing in Blender. Covers appending Roblox's Rig_And_Attachments_Template.blend R15 armature, reorienting it and applying all transforms, then parenting the shirt mesh to the armature with Parent > With Automatic Weights for automatic skinning, followed by pose testing. No bpy, MCP, or Claude-specific content.

## Claims
- c1: Roblox provides a premade standard R15 armature template (Rig_And_Attachments_Template.blend) to append into a clothing project; the doc says this saves time and reduces error versus building your own rig. *(doc, high; rigging-animation)*
- c2: Armature is added via File > Append, selecting Armature > Armature; then rotate it to align with the mesh and apply Object > Apply > All Transforms before parenting. *(doc, high; rigging-animation)*
- c3: Parent the clothing mesh to the armature with Shift-select mesh then armature (armature must be last selected), right-click viewport > Parent > With Automatic Weights to auto-skin. *(doc, high; rigging-animation)*
- c4: Doc recommends testing basic poses after rigging to confirm clothing moves and stretches correctly with any character body. *(doc, high; avatar-ugc-accessories)*
- c5: Armature must be in Object mode when appending; reorienting unapplied rotation before parenting is implied as a required step to avoid misalignment. *(doc, medium; common-mistakes-fixes)*

## Techniques
- t1: **Append R15 rig and parent with automatic weights**: Append Armature from Roblox template .blend; align via Item sidebar; Apply All Transforms; select mesh, shift-select armature last; Parent With Automatic Weights; test poses.

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- Rig_and_Attachments_Templates.zip (Roblox reference files)
