---
type: research-source
id: yt-yyztiraQMms
title: "How To Make A Roblox Rig: EP4, Vertex Groups (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=yyztiraQMms"
published: "2023-09-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "rigging-animation"]
---
# yt-yyztiraQMms

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial (Comix Productions, 2023, EP4) on making a Roblox-style rig in Blender by hand: parenting body parts to an armature with empty groups, then weight painting per-face vertex groups for arms and legs and head. No Claude, blender-mcp, bpy or Roblox export content. Off-topic for the stated focus; only manual rigging basics are relevant.

## Claims
- c1: [0:39] Select mesh parts first, Armature last, Ctrl+P, choose 'With Empty Groups' to parent body parts to the armature before weight assignment. *(demo, medium; rigging-animation)*
- c2: [1:19] Two vertex groups are created per limb (upper and lower), named exactly to match bone names; the tutorial stresses exact spelling and capitalisation. *(demo, high; rigging-animation)*
- c3: [1:49] Weights are assigned by box-selecting faces in Edit mode (face select, X-ray on) and clicking Assign with weight 1.0 for each limb section. *(demo, high; rigging-animation)*
- c4: [3:55] Correct test: limb moves as expected when posing; if it does not, wrong faces were assigned to the wrong vertex group. *(demo, medium; rigging-animation)*
- c5: [4:08] Head is rigged by selecting head mesh then Armature in Pose mode with head bone active, Ctrl+P > Bone. *(demo, high; rigging-animation)*
- c6: [2:47] Bending at joints is not yet clean after this step; the author defers fixing bends to later episodes. *(opinion, low; common-mistakes-fixes)*

## Numbers
- n1: **vertex groups per limb**: 2 (upper and lower) 
- n2: **video length**: 4:52 

## Techniques
- t1: **Manual face-box weight painting**: Front view, X-ray on, face select, box-select the limb section, set weight 1, click Assign in Object Data vertex groups panel; repeat per upper/lower group.
- t2: **Bone parenting for head**: Select head mesh, then Armature in Pose mode with head bone active last, Ctrl+P and choose Bone.

## Quotes (brief, for attribution)
> make sure the names are correctly put in make sure they're spelled correctly make sure there no wrong capitals it's all it needs to be the exact same  (at 1:49, Comix Productions)
