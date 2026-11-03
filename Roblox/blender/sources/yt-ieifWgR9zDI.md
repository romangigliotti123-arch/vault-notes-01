---
type: research-source
id: yt-ieifWgR9zDI
title: "HOW TO ATTACH HAIR/ACCESORIES TO A RIG (Roblox GFX) (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=ieifWgR9zDI"
published: "2024-04-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "rigging-animation", "texturing-baking-uv"]
---
# yt-ieifWgR9zDI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender tutorial (Roblox GFX, Apr 2024) on attaching hair/accessories to a rig. Covers splitting a character model by groups, parenting accessories to the head (Ctrl+P), clearing parents, using a Child Of constraint with Set Inverse, and copying the rig's material (Fluid Texture R6/R15) onto accessories. Not about blender-mcp, bpy scripting, or the Roblox import pipeline.

## Claims
- c1: [0:29] Split the character model by groups on import so accessories separate into their own objects; delete everything except the accessory. *(demo, medium; avatar-ugc-accessories)*
- c2: [0:50] Parenting an accessory to the head makes the head control its movement; the accessory follows without deforming. Select accessory, shift-click head, Ctrl+P, Object. *(demo, medium; rigging-animation)*
- c3: [1:30] Alt+P in Blender clears parent: Clear Parent, Clear and Keep Transformation, or Clear Parent Inverse, each removing different corrections. *(demo, medium; common-mistakes-fixes)*
- c4: [2:04] Alternative to parenting: add a Child Of constraint on the accessory, set Target to the head, then click Set Inverse to restore the correct position. *(demo, medium; rigging-animation)*
- c5: [2:44] Child Of constraint Influence slider can blend the attachment; tutorial leaves it at default. *(demo, low; rigging-animation)*
- c6: [2:57] Optional: in Material Properties, replace accessory material with the rig's material (Fluid Texture R15 or R6) to match shading and sheen. *(demo, medium; texturing-baking-uv)*

## Techniques
- t1: **Child Of constraint with Set Inverse**: Add Child Of constraint to accessory, pick head as Target via eyedropper, click Set Inverse to correct offset; accessory stays in place and follows head.
- t2: **Parent to head (Ctrl+P)**: Shift-select accessory then head, Ctrl+P > Object; undo via Alt+P with Clear Parent / Keep Transformation / Parent Inverse.
