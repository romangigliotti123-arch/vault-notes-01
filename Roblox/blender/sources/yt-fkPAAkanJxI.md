---
type: research-source
id: yt-fkPAAkanJxI
title: "HOW TO ATTACH FACE RIGS TO BODY RIGS (Roblox GFX)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=fkPAAkanJxI"
published: "2023-01-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-fkPAAkanJxI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender tutorial (Comix Productions, Jan 2023) on attaching a face rig to a Roblox GFX body rig. Steps: delete body head on faceless rigs, append face rig from collection, move settings bone, add Object Child Of constraint to the Head bone, click Set Inverse. Not about Roblox export, bpy, or Claude/MCP.

## Claims
- c1: [0:00] Face rigs (author's Cloud Face) can be attached to a body rig; the face rig's control bone is the master, so moving it in object mode moves the whole face rig. *(demo, medium; rigging-animation)*
- c2: [0:41] Delete the body rig's head only for faceless rigs; for a Roblox Rthumbnail-style rig with a head, the author says to stop and watch a different video instead. *(opinion, low; rigging-animation)*
- c3: [1:21] Append face rig from a collection folder by name, which brings the full face rig with everything included. *(demo, medium; rigging-animation)*
- c4: [2:03] Overlap fix: enter edit mode, select the face settings bone and move it upward; it does not change much. *(demo, medium; rigging-animation)*
- c5: [2:03] Attach method: on face rig controls, Object Constraints (not Bone Constraints) > Child Of, pick body rig with eyedropper, choose Head bone; if bone not listed try H or select head bone in rig. *(demo, high; rigging-animation)*
- c6: [2:45] After adding Child Of constraint the rig looks bugged; clicking Set Inverse restores the pose and the face then follows the head. *(demo, high; rigging-animation)*
- c7: [3:26] Author is fixing known issues in Cloud Face: teeth, deep-set eyes, eyes disappearing when moved down; plans a Cloud Face update. *(experience, low; rigging-animation)*

## Numbers
- n1: **video length**: 4:05 

## Techniques
- t1: **Child Of object constraint for face attachment**: Select face control; Object Constraints > Add Child Of; set target to body rig via eyedropper; set bone to Head; then click Set Inverse to reset pose.
- t2: **Delete body head for faceless rigs**: In object mode select the body head and delete it to avoid overlapping the face rig's head.
