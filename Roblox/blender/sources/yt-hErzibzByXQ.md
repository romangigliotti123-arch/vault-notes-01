---
type: research-source
id: yt-hErzibzByXQ
title: "How To Add Inverse Kinematics + Switch To Roblox Rigs (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=hErzibzByXQ"
published: "2022-08-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-hErzibzByXQ

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender rigging tutorial (2022, Comix Productions) on building a Roblox-style leg rig: FK bone chain (upper leg, lower leg, foot, settings bone), IK with side pole target, chain length 2, copy-rotation fancy feet, knee rotation limits, and custom-property switches wired via drivers to toggle IK, fancy feet, and bone visibility. Does not cover blender-mcp, bpy scripting, or the Roblox import/export pipeline.

## Claims
- c1: [3:06] For Roblox characters, IK chain length is set to 2 on the lower leg; a longer hip-inclusive chain needs 3. *(demo, medium; rigging-animation)*
- c2: [4:36] Knee rotation limited via Inverse Kinematics bone settings: limit X min -90, max 0 (may need Y or Z depending on rig build). *(demo, medium; rigging-animation)*
- c3: [3:47] Pole target must be parented to the IK target (Ctrl P, keep offset) to stop the leg looping around when the target moves. *(demo, medium; rigging-animation)*
- c4: [1:44] Pole target and target bones should have no parent (Alt P clear parent) and roll zero (N panel) before IK setup. *(demo, medium; rigging-animation)*
- c5: [5:00] Switches are custom properties on the settings bone; the custom property only applies after pressing OK; descriptions should avoid trailing full stops. *(demo, low; rigging-animation)*
- c6: [7:46] Bone hide driver uses scripted expression: '0 if IK == 1 else 1', variable name must match the custom property name. *(demo, medium; rigging-animation)*
- c7: [6:23] Creator notes the IK toggle driver can be pasted onto the limit constraint to hide the IK line when FK is active; creator says cause unknown. *(opinion, low; rigging-animation)*
- c8: [3:54] Fancy feet: Copy Rotation constraint on foot bone targeting the IK target bone; may need local/other space settings. *(demo, medium; rigging-animation)*

## Numbers
- n1: **IK chain length**: 2 (Roblox); 3 if hip/lower torso included Chain length setting for Roblox leg IK
- n2: **Knee limit X**: min -90, max 0 Lower leg IK limit to stop over-bending
- n3: **Video length**: 10:43 Tutorial length

## Techniques
- t1: **Side pole target IK**: Extrude target bone from hip joint and pole bone at knee in Y axis, clear parents, set roll 0. Add IK constraint on lower leg with pole target, chain length 2, parent pole to target.
- t2: **Fancy feet via Copy Rotation**: Add Copy Rotation to foot bone, target armature + IK target bone, adjust space settings as needed.
- t3: **Custom-property FK/IK switch with drivers**: Add custom property on settings bone, right-click Copy as New Driver, paste onto constraint influence; for bone hide, use scripted expression with inverse 0/1 logic.

### Code: Driver scripted expression for hiding FK bones when IK is on
```text
0 if IK == 1 else 1
```

## Quotes (brief, for attribution)
> I've set the chain length to two, which is specifically for Roblox characters.  (at 3:06, Comix Productions)
