---
type: research-source
id: off-art_modeling_skin-a-humanoid-model
title: "Roblox Creator Docs: art_modeling_skin-a-humanoid-model"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# off-art_modeling_skin-a-humanoid-model

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs guide to skinning an R15 humanoid mesh in Blender 3.0 after rigging. Covers armature Display As Sticks, Auto Normalize, and weight painting head, hand, lower arm, upper arm and shoulder, with a test-by-rotating-bone method. Notes the 4-bone-per-vertex limit, the Root/HumanoidRootNode influence drop, and FBX export. No Claude, blender-mcp or bpy content.

## Claims
- c1: Studio does not support more than 4 bones influencing any single vertex; can happen in complex rigs or with Auto Normalize disabled. *(doc, high; rigging-animation)*
- c2: Influences applied to the Root or HumanoidRootNode parent bones are dropped on import into Studio. *(doc, high; rigging-animation)*
- c3: Extra bones skinned to a mesh that do not match a Humanoid bone name (e.g. LowerTorso, LeftFoot) import into Studio as Class.Bone with the same name. *(doc, high; rigging-animation)*
- c4: Auto Normalize forces vertex influence sums to 1, so painting a wrong bone removes influence from the original bone, making mistakes easier to catch. *(doc, high; rigging-animation)*
- c5: Set armature Object Data Properties Display As to Sticks to make bones easier to see during weight painting. *(doc, high; rigging-animation)*
- c6: Head mesh is shared between Head bone (neck up) and Upper Torso bone (neck down), with brush strength 1 at the neckline. *(doc, medium; rigging-animation)*
- c7: Shoulder upper-torso influence uses partial brush strength 0.25 since the movement is subtle; adjust by testing. *(doc, medium; rigging-animation)*
- c8: Full-range arm rotation can cause a candy-wrapper effect at shoulder-torso that may be unavoidable in many cases. *(doc, medium; rigging-animation)*
- c9: A skinned model without inner and outer cage mesh data cannot equip layered accessories. *(doc, high; avatar-ugc-accessories)*
- c10: Export the skinned model as .fbx using the Blender export settings for Studio; guide uses Blender version 3.0. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **max bone influences per vertex**: 4 Studio limit; exceeding occurs in complex rigs or with Auto Normalize off
- n2: **brush strength (neck, hand, arms)**: 1 used for head neckline and hand/wrist/elbow painting
- n3: **brush strength (shoulder)**: 0.25 partial influence on upper torso at shoulder, adjustable
- n4: **Blender version used**: 3.0 guide version; UI may differ in other versions

## Techniques
- t1: **Auto Normalize weight painting**: Select armature, shift-select mesh, enter Weight Paint, Tool tab > Options > enable Auto Normalize. Paint with brush strength 1 and check by rotating bones with R.
- t2: **Bone-by-bone painting with hide**: Hide neighboring mesh in Outliner to access joint vertices; shift-select the bone to paint; test with R rotation in Weight Paint mode.
- t3: **Partial shoulder influence**: Paint upper torso vertices at shoulder with brush strength 0.25 using Upper Torso bone, then test by rotating the upper arm.

## Quotes (brief, for attribution)
> Studio doesn't support more than 4 bones to influence any single vertex. This may occur in complex rigs or inadvertently with Auto Normalize disabled.  (create.roblox.com)
> Do not apply influences on the Root or HumanoidRootNode parent bones in a humanoid rig. Any added influences are dropped when importing into Studio.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model
- https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh
- https://create.roblox.com/docs/art/modeling/export-requirements
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://www.blender.org/download/releases/3-0/
- https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/tool_settings/options.html
