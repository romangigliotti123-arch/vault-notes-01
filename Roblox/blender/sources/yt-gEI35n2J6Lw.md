---
type: research-source
id: yt-gEI35n2J6Lw
title: "How To Make A Roblox Rig: EP2, Adding Bones (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=gEI35n2J6Lw"
published: "2023-08-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "other", "rigging-animation"]
---
# yt-gEI35n2J6Lw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender tutorial (ep. 2 of a Roblox rig series) on hand-placing armature bones for an R15-style character: add an Armature in object mode, set viewport display to In Front, extrude bones with E, name them with .L suffixes, parent with Ctrl+P keep offset, add IK target and pole bones, then symmetrize. No Claude, blender-mcp, bpy, or Roblox export/import steps are covered.

## Claims
- c1: [0:14] Add armature via Shift+A in Object mode; set Object Data > Viewport Display > In Front to see bones through the mesh. *(demo, high; rigging-animation)*
- c2: [0:55] Bones have head and tail; select an end and press E to extrude a connected child bone. *(demo, high; rigging-animation)*
- c3: [3:02] Leg bones parented to torso bone via select child, then parent (Ctrl+P) with Keep Offset; without it no relation line appears. *(demo, high; rigging-animation)*
- c4: [4:40] IK bones are extruded from ankle/wrist joints and given their own FK-separate hierarchy; Alt+P clears parent before re-parenting. *(demo, medium; rigging-animation)*
- c5: [6:09] Name left-side bones with a .L suffix so Blender treats them as left; R15 naming uses upper arm and lower arm. *(demo, high; rigging-animation)*
- c6: [6:49] Naming scheme used: arm ik .L as IK target, arm pole as pole bone, leg ik .L and leg pole for legs. *(demo, medium; rigging-animation)*
- c7: [7:53] IK bones intentionally do not follow FK bones; pole bones parented to IK bones with Keep Offset. *(demo, medium; rigging-animation)*
- c8: [8:11] Upper leg must be parented to the hip bone, not lower torso, for legs to move with the hip; do not use Connected parenting. *(demo, medium; rigging-animation)*
- c9: [8:49] Build left side only, then box-select left bones in Edit mode and use Symmetrize to create the right side. *(demo, high; rigging-animation)*
- c10: [2:28] Opinion/advice: do not duplicate left-arm bones for the right side manually; use Symmetrize instead. *(opinion, medium; common-mistakes-fixes)*
- c11: [9:18] Video length 9:40, posted 2023-08-22, 54,796 views; ends with a saved, partially working rig, not exported to Roblox. *(data, high; other)*

## Numbers
- n1: **video length**: 9:40 
- n2: **views**: 54796 

## Techniques
- t1: **Front-view bone placement**: Front view, Shift+A Armature in Object mode, set Viewport Display In Front or wireframe, enter Edit mode, extrude with E from head/tail.
- t2: **Keep-offset parenting**: Select child, shift-select parent last, Ctrl+P, choose Keep Offset to parent without moving bones.
- t3: **Side suffix naming**: Rename bones with F2 using .L suffix for left side so Blender recognizes side for symmetry.
- t4: **Symmetrize left to right**: Front view, Edit mode, box-select all left bones, right-click, Symmetrize.

## Quotes (brief, for attribution)
> name them something like upper arm dot l so because of that L at the end it's going to think that's a left bone not a right bone  (at 6:09, Comix Productions)
> box select everything that is on the left ... and just right click and click on symmetrize  (at 8:49, Comix Productions)
