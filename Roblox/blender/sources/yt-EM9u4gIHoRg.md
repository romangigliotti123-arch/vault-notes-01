---
type: research-source
id: yt-EM9u4gIHoRg
title: "Roblox Animation in Blender: Advanced Guide (2026)"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=EM9u4gIHoRg"
published: "2026-07-06"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0786
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# yt-EM9u4gIHoRg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Nisky's advanced tutorial on animating an R6 IK rig in Blender for Roblox: importing avatar textures and accessories via OBJ, 24 FPS, pose assets, cyclic and stepped animation, duplicating rigs, and exporting animations to Roblox Studio via clipboard with the RBX animations add-on. No Claude, MCP, or bpy scripting content.

## Claims
- c1: [2:25] To get an avatar texture into the rig: insert the character with a plugin (e.g. Moon Animator inserter), right-click the model in Explorer, Save and Export as OBJ, and use the exported texture (handle..._diff) in Blender's Shader Editor. *(demo, medium; avatar-ugc-accessories)*
- c2: [3:06] Export accessories separately as OBJ, because exporting the whole character also brings in the baseplate and other objects. Ctrl-click to select multiple accessories. *(demo, medium; avatar-ugc-accessories)*
- c3: [5:08] Roblox-exported OBJ accessories import off-center in Blender. Fix: Object > Set Origin > Origin to Geometry, then zero location in the N panel Item tab. The speaker also fixed rotation (180 on Z) and then moved it by hand with G. *(demo, medium; blender-roblox-export-import)*
- c4: [6:29] To attach an accessory to the rig: select the accessory, shift-select the armature root, enter Pose mode, shift-select the target bone (e.g. head), Ctrl+P > Set Parent to Bone. The accessory then follows that bone. *(demo, high; avatar-ugc-accessories)*
- c5: [7:55] Keep the scene at 24 FPS (Output > Format) for Roblox animations. Speaker's opinion: 60 FPS looks too smooth or CG, and most animators use 24. *(opinion, medium; rigging-animation)*
- c6: [9:24] Pose assets save reusable poses: select all bones (keyframes not selected), Create Pose Asset in the Asset Browser, save to User Library (available in every project) or Current File. Unsaved assets show a star icon and can be lost on close. *(demo, high; rigging-animation)*
- c7: [14:52] Pose asset thumbnails are not auto-generated. Use the asset settings dropdown > Preview > Capture Screenshot Preview. Assets without a catalog land in 'Unassigned'. *(demo, medium; rigging-animation)*
- c8: [12:08] Idle cycle workflow: right-click pose idle A at frame 0, set end frame to 60, apply idle B at the midpoint and idle A again at the end. Select all keys in the dope sheet, Shift+E > Make Cyclic. Delay head and arm keys by 2-3 frames for smoother follow-through. *(demo, medium; rigging-animation)*
- c9: [17:35] Stop-motion style: in the Graph Editor, add a Stepped Interpolation F-modifier to one curve, select all curves (A), Copy F-Modifiers and paste to all. The step size sets animating on twos or threes. *(demo, high; rigging-animation)*
- c10: [19:45] To reset the rig to its default pose, select all bones in pose mode and press Alt+G (clear location) and Alt+R (clear rotation). *(demo, high; rigging-animation)*
- c11: [20:04] To animate two rigs, don't copy-paste the rig, which breaks it. Put the hair accessory inside the collection, right-click the collection > Duplicate Collection, then re-hide the helper bones and circle objects with the eye icon. The duplicate animates independently. *(demo, high; rigging-animation)*
- c12: [22:37] Move rigs a long distance in Object mode rather than with the root control, which has bone-pointer side effects. Use the root control only when the movement is part of the animation. *(opinion, medium; rigging-animation)*
- c13: [23:59] The rig file has auto-keying on. Moving anything in Object mode away from frame 0 creates unwanted keyframes at the current frame, a source of confusing animation bugs. *(experience, high; rigging-animation)*
- c14: [25:06] Purple or missing-texture rig is caused by not extracting the downloaded zip. The texture image must sit in the same directory as the .blend file. *(experience, high; blender-roblox-export-import)*
- c15: [26:23] Export animation: select the rig in Object mode, open the RBX Animations add-on in the N panel, and click Export Animation. This copies baked animation data to the system clipboard. Exporting to a file also works but is unnecessary. *(demo, high; automation-and-creator-workflows)*
- c16: [28:27] In Studio, import with the Blender Animations plugin using 'import animation from clipboard'. The rig's PrimaryPart (HumanoidRootPart) must be anchored, or the plugin errors 'Rig primary part is not anchored'. This was the cause for most failed imports. Moon Animator's rig inserter anchors automatically. *(demo, high; automation-and-creator-workflows)*
- c17: [29:49] After import, set the animation priority (e.g. Idle) and upload the animation to Roblox from the plugin. Moon Animator is not required, only convenient; the speaker says the free character inserter works with anchoring and a hidden name. *(demo, medium; automation-and-creator-workflows)*
- c18: [0:23] The speaker supplies an R6 IK rig (the 'R6 IK fix' version) with swappable face textures, changed by replacing the face image or via Shader Editor > open image on a body part. *(demo, medium; rigging-animation)*

## Numbers
- n1: **animation frame rate**: 24 FPS recommended for Roblox animations in Blender
- n2: **idle cycle length**: 60 frames end frame set for idle A to B to A cycle
- n3: **kick animation length**: 24 frames scaled down from slower version
- n4: **keyframe delay for head and arms**: 2-3 frames gives smoother idle

## Techniques
- t1: **Import Roblox-exported OBJ accessory**: File > Import > Wavefront OBJ. Object > Set Origin > Origin to Geometry. In the N panel Item tab, zero location, and set Z rotation to 180. Position with G. Parent to bone via Ctrl+P > Bone.
- t2: **Blender animation to Roblox via clipboard**: Select the rig and click Export Animation in the RBX Animations add-on. In Studio, insert a rig and anchor HumanoidRootPart. Use the plugin's import from clipboard, set priority, and upload.
- t3: **Stepped (choppy) animation**: In the Graph Editor, select one point, add the Stepped Interpolation modifier, press A, click Copy F-Modifiers, then paste. Set the frame step to 2 or 3.
- t4: **Reusable pose assets**: Select all in pose mode, Create Pose Asset, save to User Library. Capture a screenshot preview for the thumbnail. Apply poses by right-clicking an asset.
- t5: **Duplicate a rig for multi-character scenes**: Put all rig parts, including accessories, in one collection. Right-click > Duplicate Collection, then hide the unhidden bones and circles with the eye icon.

## Quotes (brief, for attribution)
> That's literally the problem 99% of you guys were having... it literally said over there it's not anchored.  (at 29:09, Nisky)

## Contradictions flagged
- Moon Animator is not required to import animations, only convenient. (vs Some commenters thought the paid Moon Animator was necessary.)

## Points to
- Moon Animator (Roblox plugin)
- Load Character Lite (Roblox plugin)
- RBX Animations Blender add-on
- R6 IK fix rig (Nisky tutorial files)
- Nisky beginner's guide for Roblox animation in Blender
