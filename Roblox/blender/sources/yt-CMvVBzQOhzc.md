---
type: research-source
id: yt-CMvVBzQOhzc
title: "How To Make A Roblox Rig: EP9, Bone Shapes (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=CMvVBzQOhzc"
published: "2023-10-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 1
density: medium
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-CMvVBzQOhzc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Episode 9 of a Roblox rig series in Blender (Comix Productions, Oct 2023). Covers building custom bone shapes in a Shapes collection using built-in Extra Objects add-on (gear, cube, circle, sphere empty), assigning them via Bone > Viewport Display > Custom Object, fixing axis/scale, and hiding IK bone shapes via copied drivers with an inverted scripted expression. No blender-mcp, bpy, or Claude content.

## Claims
- c1: [0:49] Bone custom shapes can be made by enabling the built-in Extra Objects add-on (Edit > Preferences > Add-ons, search 'extra') and adding meshes/curves from Shift+A. *(demo, high; rigging-animation)*
- c2: [2:07] Assign a bone shape via bone properties > Viewport Display > Custom Object; the author changed the head bone to a circle and settings bone to a gear. *(demo, high; rigging-animation)*
- c3: [3:32] Cube custom shapes can be scaled per axis to form torso and hip controllers; author warns moving bones inside the rig can disturb vertex groups. *(demo, medium; rigging-animation)*
- c4: [4:55] IK controllers can use an empty set to Sphere display; if pole rotates, set roll to zero in edit mode. *(demo, medium; rigging-animation)*
- c5: [9:12] Hide IK-related bone shapes when IK is off by copying a driver from the IK checkbox and pasting it to Hide in viewport display. *(demo, high; rigging-animation)*
- c6: [10:34] Invert a driver by setting its expression to scripted and using '-left_arm_ik+1' so shapes show when IK is off; then copy driver to pole target. *(demo, medium; rigging-animation)*

## Numbers
- n1: **Torso cube scale**: Z scaled, Y=2, X=2 (author values) Cube bone shape scaled to form upper torso
- n2: **Collection name**: Shapes Bone shapes collection hidden from view; scene collection used

## Techniques
- t1: **Custom bone shapes via Viewport Display**: Create mesh in Shapes collection, hide it, select bone, Bone properties > Viewport Display > Custom Object = that mesh. Armature Display In Front off to see shapes.
- t2: **Driver-based IK shape visibility**: Right-click IK checkbox > Copy as New Driver; paste driver to Hide on each shape; edit driver, set scripted expression with minus and +1 to invert; update dependencies; copy to pole target.

### Code: Inverted driver expression for hiding shapes when IK is off
```text
-left_arm_ik + 1
```

## Quotes (brief, for attribution)
> we need to hide these when ik is off  (at 9:12, Comix Productions)
