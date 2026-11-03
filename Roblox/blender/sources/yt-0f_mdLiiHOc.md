---
type: research-source
id: yt-0f_mdLiiHOc
title: "DON'T DELETE THE HEAD WHEN MAKING ROBLOX GFX (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=0f_mdLiiHOc"
published: "2022-10-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "other", "rigging-animation"]
---
# yt-0f_mdLiiHOc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender GFX tutorial for Roblox avatars. Argues against deleting the head in the default rig file; instead open a provided faces.blend, set up face texture via Shader editor, parent accessories to head with Ctrl+P, and optionally delete the head-rotation switch and its driver. Nothing on blender-mcp, bpy, Claude, or export settings.

## Claims
- c1: [0:00] Creator says deleting the head/face rig from the default Roblox Blender file is wrong; it breaks drivers and the rig controls. *(opinion, medium; blender-roblox-export-import)*
- c2: [0:40] Roblox avatar rigs downloaded for GFX contain a face rig; deleting the head and re-adding it to the control requires manual repositioning of parts. *(demo, medium; rigging-animation)*
- c3: [1:35] Use the provided faces.blend file instead of default file; in it there is no face rig, just a switch controlling head rotation when torso rotates. *(demo, medium; rigging-animation)*
- c4: [2:15] Material setup: in Shader editor, add Image Texture, connect Color to Principled BSDF Base Color, connect BSDF to Material Output Surface. *(demo, high; other)*
- c5: [2:54] Parent accessories to head: select accessories, then head last, Ctrl+P, Set Parent to Object, so accessories follow the head without moving each one. *(demo, high; avatar-ugc-accessories)*
- c6: [3:36] Creator suspects the head switch may slow render and Blender; optionally delete the switch and its driver. *(opinion, low; rigging-animation)*
- c7: [3:44] Optional cleanup: delete switch in Object mode; in Pose mode on head control, Bone Properties > Relations > Inherit Rotation, right-click, Delete Driver. *(demo, medium; rigging-animation)*
- c8: [4:25] Creator recommends building a personal rig for frequent GFX work; not worth it if changing avatars often. *(opinion, low; automation-and-creator-workflows)*
- c9: [1:20] Creator says the same steps apply to Blender 2.7x and 2-point-something; shortcuts are the same. *(opinion, low; blender-roblox-export-import)*

## Numbers
- n1: **video length**: 5:07 

## Techniques
- t1: **Parent accessories to head**: Shift-select accessories, select head last, Ctrl+P, Set Parent to Object. Accessories then follow head movement.
- t2: **Remove head rotation driver**: Delete head switch in Object mode. In Pose mode select head control, Bone Properties > Relations > Inherit Rotation, right-click, Delete Driver.

## Quotes (brief, for attribution)
> if you have been opening the default Dublin file whenever you're making a gfx and deleting the head you have done your gfx completely wrong  (at 0:00, Comix Productions)
> don't delete it but if you don't like this  (at 3:36, Comix Productions)

## Points to
- Roblox channel video linked in description (faces.blend download via media file link)
