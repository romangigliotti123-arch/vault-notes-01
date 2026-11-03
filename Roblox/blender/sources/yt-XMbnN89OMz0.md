---
type: research-source
id: yt-XMbnN89OMz0
title: "How To Make A Roblox Rig: EP8, Making an IK Switch (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=XMbnN89OMz0"
published: "2023-10-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-XMbnN89OMz0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Episode 8 of a Roblox rig series (Comix Productions, Oct 2023) on building an IK switch in Blender using custom bone properties and drivers. Nothing on blender-mcp, bpy scripting, Claude, or the Roblox import/export pipeline beyond rig-level setup. Low relevance to the stated topic.

## Claims
- c1: [0:15] Create a dedicated 'settings' bone in edit mode to store IK switches and toggles on the rig. *(demo, high; rigging-animation)*
- c2: [0:59] Add IK toggles as Boolean custom properties on the bone (Bone Properties > Custom Properties > New, change type to Boolean via gear icon) instead of default numeric slider. *(demo, high; rigging-animation)*
- c3: [2:12] Link an IK constraint influence to a custom property by right-clicking the influence field, choosing Copy as New Driver on the toggle, then Paste Driver on the influence. *(demo, high; rigging-animation)*
- c4: [4:00] Hide the bone rotation-track circle in FK mode by pasting the same IK toggle driver onto the bone's Inverse Kinematics display property. *(demo, medium; rigging-animation)*
- c5: [4:40] Creator says selecting the lower leg while IK is on is not solved in this episode and is deferred to the next episode. *(demo, high; rigging-animation)*

## Numbers
- n1: **Rig price**: £3 (creator's own rig, linked in description) Promotional; included only for completeness of source metadata

## Techniques
- t1: **Boolean custom property as IK switch**: Add custom property on settings bone, set type Boolean, name it per limb (e.g. left leg ik), then Copy as New Driver and Paste Driver onto the IK constraint influence of the target bone.
- t2: **Driver-based FK/IK visibility toggle**: Paste the same driver onto the bone's IK property so the rotation circle appears only when IK is enabled.
