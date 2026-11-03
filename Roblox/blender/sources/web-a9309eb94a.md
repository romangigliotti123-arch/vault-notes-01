---
type: research-source
id: web-a9309eb94a
title: "Roblox docs: art/modeling/rig-a-humanoid-model"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/rig-a-humanoid-model.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 2
density: medium
tags: ["research-source", "web", "other", "rigging-animation"]
---
# web-a9309eb94a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for manually rigging an R15 humanoid in Blender 3.0: import Lola FBX into template, enable X-mirror, position bones inside meshes, parent 15 meshes to armature with empty groups, assign full-influence vertex groups, test in Pose mode, export FBX. Root/HumanoidRootNode bones must have no influence. No bpy, MCP, or Claude content.

## Claims
- c1: An R15 humanoid model is 15 separate mesh objects; all 15 must be parented to one armature to bind the skeleton. *(doc, high; rigging-animation)*
- c2: Doc uses Blender 3.0 with a Rig_and_Attachment_Template.blend and Lola reference FBX; other versions may differ in UI slightly. *(doc, high; rigging-animation)*
- c3: Enable X-Axis Mirror in Edit Mode sidebar Tool panel so left/right bone edits stay symmetrical. *(doc, high; rigging-animation)*
- c4: Bones should be centered inside their corresponding mesh objects (e.g., Head bone within Head_Geo); verify with X-ray/perspective views. *(doc, high; rigging-animation)*
- c5: Parent meshes to armature via Parent > With Empty Groups, then assign each mesh's vertices (A to select all) to its bone's vertex group at full influence. *(doc, high; rigging-animation)*
- c6: Root and HumanoidRootNode bones must have no influences; any added influences are dropped on import into Studio. *(doc, high; rigging-animation)*
- c7: Bone names and hierarchy must follow standard or advanced R15 armature conventions; deviations break the rig. *(doc, high; rigging-animation)*
- c8: Test by Pose mode, rotating bones with R; Alt+R resets rotation. Retest after any influence edits. *(doc, high; rigging-animation)*
- c9: Export the rigged model as FBX for Studio, or continue to skinning (multi-bone weights) in the separate skinning guide. *(doc, high; rigging-animation)*
- c10: Source covers no bpy scripting, blender-mcp, Claude integration, or Roblox Blender plugin; it is a manual GUI rigging guide. *(doc, high; other)*

## Numbers
- n1: **mesh objects per R15 humanoid**: 15 Each R15 humanoid is 15 mesh objects all parented to one armature
- n2: **Blender version used**: 3.0 Guide's reference version; other versions may differ in UI

## Techniques
- t1: **Parent With Empty Groups**: Select all 15 geo meshes in Outliner (filter 'geo'), shift-select armature, Right-click Viewport > Parent > With Empty Groups. Then assign vertex groups per mesh in Edit Mode.
- t2: **Symmetric bone placement**: Enable X-Axis Mirror in Edit Mode, drag bone tips with G to fit mesh centers, verify in perspective/X-ray views.
- t3: **Pose-mode bone test**: Switch to Pose mode, Shift-click bone, R to rotate, Alt+A deselect, Alt+R reset, retest after influence edits.

## Quotes (brief, for attribution)
> The Root and HumanoidRootNode parent bones in a humanoid rig should not have any influences applied to them. Any added influences are dropped when importing into Studio.  (create.roblox.com)

## Points to
- https://www.blender.org/download/releases/3-0/
- https://www.autodesk.com/products/maya/overview
- ../../avatar/character-bodies/specifications.md
- ../../art/modeling/skin-a-humanoid-model.md
- ../../art/modeling/export-requirements.md
