---
type: research-source
id: off-art_modeling_rig-a-humanoid-model
title: "Roblox Creator Docs: art_modeling_rig-a-humanoid-model"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 3
density: medium
tags: ["research-source", "web", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# off-art_modeling_rig-a-humanoid-model

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on manually rigging an R15 humanoid in Blender 3.0: import Lola FBX into a template, align bones to meshes with X-mirror, parent 15 meshes to armature via Empty Groups, assign full vertex-group influence, test in Pose mode, export FBX. Root/HumanoidRootNode must have no influences. Does not cover blender-mcp, Claude, or bpy scripting.

## Claims
- c1: An R15 humanoid model consists of 15 individual mesh objects; all 15 must be parented to one armature to bind the skeleton. *(doc, high; rigging-animation)*
- c2: Workflow: import model into Rig_and_Attachments_Template.blend, position template bones, parent meshes to armature with Empty Groups, then assign full influence per mesh vertex group, then test in Pose mode. *(doc, high; rigging-animation)*
- c3: Root and HumanoidRootNode bones must have no influences; any added influences are dropped on import into Studio. *(doc, high; rigging-animation)*
- c4: Bones should be centered inside their corresponding mesh objects (e.g. Head bone centered in Head_Geo); bone positions may need revisiting after weight painting. *(doc, high; rigging-animation)*
- c5: Use X-Axis Mirror in Edit Mode to keep left/right bones symmetric; doc says maintain symmetry whenever possible to reduce posing/animation issues. *(doc, high; rigging-animation)*
- c6: Bone hierarchy and naming must follow standard or advanced R15 rig conventions if modifying or creating bones. *(doc, high; rigging-animation)*
- c7: Guide is written for Blender 3.0; other versions may differ slightly in UI and settings. *(doc, high; blender-roblox-export-import)*
- c8: Import the reference model via File > Import > FBX; scale model to match armature with G (move) and S (scale) if needed. *(doc, high; blender-roblox-export-import)*
- c9: Final rigged model is exported as .fbx for use in Studio, following the export-requirements page. *(doc, high; blender-roblox-export-import)*
- c10: Test by Pose mode: Shift-click bone, R to rotate, Alt+A to deselect, Alt+R resets rotation to neutral. *(doc, high; rigging-animation)*
- c11: Skinning (multi-bone influence per mesh) is a separate subsequent step covered by 'Skin a humanoid model'; rigging alone gives full single-bone influence. *(doc, high; rigging-animation)*
- c12: Source does not mention blender-mcp, Claude, or bpy scripting; no AI-assisted workflow content. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **mesh objects per R15 humanoid**: 15 All 15 must be parented to one armature
- n2: **Blender version used**: 3.0 Guide tested version; other versions may differ

## Techniques
- t1: **Parent with Empty Groups**: Select meshes, shift-select armature, Ctrl+P-style Parent > With Empty Groups in Viewport; then per mesh in Edit Mode select all, assign to bone vertex group.
- t2: **X-Axis Mirror bone editing**: Edit Mode, enable X-Axis Mirror in sidebar Tool panel, position bone tips with G so left/right stay symmetric.
- t3: **Pose-mode bone test**: Pose mode, Shift-click bone, R to rotate, Alt+A deselect, Alt+R reset, check meshes follow bones.

## Quotes (brief, for attribution)
> You must parent all 15 mesh objects to one armature.  (create.roblox.com)
> The Root and HumanoidRootNode parent bones in a humanoid rig should not have any influences applied to them. Any added influences are dropped when importing into Studio.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model
- https://create.roblox.com/docs/art/modeling/export-requirements
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://www.blender.org/download/releases/3-0/
- https://www.autodesk.com/products/maya/overview
