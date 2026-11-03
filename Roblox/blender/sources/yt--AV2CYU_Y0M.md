---
type: research-source
id: yt--AV2CYU_Y0M
title: "Blender Grease Pencil Tutorial : Character Creation : Part Two - 2D Rigging"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=-AV2CYU_Y0M"
published: "2021-06-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: medium
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt--AV2CYU_Y0M

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Grease Pencil 2D character tutorial (part two): draw separate body parts as strokes with fill layers, split with P > selected strokes, then rig with an armature. Covers bone chains, parenting objects to bones with Ctrl+P, IK constraints (chain length 2, pole targets) and empty-based controls. No Claude, blender-mcp, bpy, Roblox export or import content.

## Claims
- c1: [4:11] Armature bones are built in edit mode by extruding (E) from a single bone; the video uses a separate neck bone, head bone, and arm/leg chains. *(demo, high; rigging-animation)*
- c2: [7:43] Bones are controlled with an Inverse Kinematics constraint in pose mode; the target is set by eyedropper to an empty, and the chain length is set to 2 for arms and legs. *(demo, high; rigging-animation)*
- c3: [8:25] To parent a mesh part to a bone: select the object, shift-select the armature, enter edit mode to pick the bone, then Ctrl+P and choose Bone. Wrong bone selection is a common cause of misparenting. *(demo, high; rigging-animation)*
- c4: [16:22] An IK chain can flip direction; fix it with a pole target (an empty) and pole angle of 180 degrees, or -180 depending on the rig. *(demo, medium; rigging-animation)*
- c5: [2:08] Grease Pencil body parts are split by selecting strokes in edit mode and pressing P > By Selected Strokes so each part becomes its own object. *(demo, high; other)*
- c6: [14:59] Control hierarchy: small empties parent limb controls to a central empty, and a cube empty parents everything for whole-body movement. *(demo, medium; rigging-animation)*

## Numbers
- n1: **IK chain length**: 2 Set on lower arm and leg bones with IK constraint
- n2: **Pole angle**: 180 degrees (or -180) Used to flip IK bend direction

## Techniques
- t1: **Split Grease Pencil parts by selected strokes**: Edit mode, select strokes of one part, press P, choose By Selected Strokes. Draw each body part as its own stroke, lock other layers, and delete empty layers afterwards.
- t2: **Parent to bone with Ctrl+P**: Object mode: select part, shift-select armature, Ctrl+P, choose Bone. Re-enter edit mode first to select the target bone.
- t3: **IK with empty target**: Add circle empty, pose mode, bone constraint IK, eyedrop target, chain length 2. Use copy location for hips/arms to follow controllers.
