---
type: research-source
id: yt-KawVMkCLL44
title: "How To Become a Roblox Animator with Blender (2026)"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=KawVMkCLL44"
published: "2026-07-13"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0663
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# yt-KawVMkCLL44

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial for animating Roblox R6 characters in Blender using a provided IK rig: addon install, viewport shortcuts, 24 FPS timeline, graph editor easing, multi-rig setup, importing avatar texture/accessories via OBJ, and exporting animation to Studio via an RBX Animations addon (clipboard) and Studio plugin. No Claude/MCP/bpy content.

## Claims
- c1: [4:17] The tutorial's R6 rig is an IK rig; the creator claims this makes walk cycles easier and says Blender beats Moon Animator and the Studio animation editor (opinion). *(opinion, medium; rigging-animation)*
- c2: [6:08] To reset a pose: press A to select the whole rig, then Alt+G and Alt+R. Moving bones auto-creates keyframes, so unwanted keys can end up in wrong frames. *(demo, high; rigging-animation)*
- c3: [7:20] Recommends animating at 24 FPS instead of the rig file's 60 FPS, because 60 FPS needs double the poses. Set frame rate in the Output tab and the end frame to 24 for a 1-second animation. *(opinion, medium; rigging-animation)*
- c4: [9:03] Pressing I at frame 0 keys every bone. Make sure frame 0 has keys before animating. *(demo, medium; rigging-animation)*
- c5: [12:28] In the graph editor, overshooting curve handles makes a pose overshoot and settle back, which is useful for arm movements. Steeper curves are the ones driving motion. In-betweens are said to matter more than graph editing. *(demo, medium; rigging-animation)*
- c6: [10:25] Graph editor axes appear inverted relative to the rotation gizmo because the rig uses quaternion channels and Blender's Z-up axes, so a Z-axis head turn shows on the Y curve. *(demo, medium; rigging-animation)*
- c7: [14:59] To animate multiple characters, right-click the rig collection and choose Duplicate Collection, then hide rig meta and circle objects via the eye icon. Delete with Delete Hierarchy. Duplicating copies existing animation, so key frame 0 on both. *(demo, medium; rigging-animation)*
- c8: [16:18] To put your avatar on the rig, load it in Studio with an avatar-inserter plugin as R6 at position 0,3,0, export accessories as OBJ from the right-click menu, then set the body texture image in Blender's Shading tab and import the OBJ. *(demo, medium; blender-roblox-export-import)*
- c9: [19:01] After importing an accessory OBJ, set the origin to geometry. To make it follow the rig, select the accessory then the armature, enter pose mode, shift-select a bone, and Ctrl+P to parent to bone: head for hair, torso for back accessories. *(demo, high; avatar-ugc-accessories)*
- c10: [20:15] Changing the texture on one character changes both because the material is shared. Click the duplicate-material button to copy it. Then select the changed parts with the torso last and press Ctrl+L, Link Materials. *(demo, medium; avatar-ugc-accessories)*
- c11: [22:01] To export an animation, be in object mode with the armature selected, which is the top cause of problems. Press N, open the RBX Animations panel, and click Export Animation, which copies data to the clipboard. Don't copy anything else before importing. *(demo, high; blender-roblox-export-import)*
- c12: [23:23] In Studio, anchor the avatar's HumanoidRootPart and select the rig. With the Blender Animations plugin, choose Import Animation from Clipboard and paste with Ctrl+V into the opened script. Set animation priority, e.g. Idle, then upload and name the animation. *(demo, high; blender-roblox-export-import)*
- c13: [24:45] To use the animation in Moon Animator, create a new rig animation and use File, Import Roblox. This is optional. *(demo, low; automation-and-creator-workflows)*

## Numbers
- n1: **recommended FPS**: 24 (rig file default 60) 24 frames equals 1 second; timeline start left at 0
- n2: **default timeline length**: 40 frames about 1.8 seconds at 24 FPS
- n3: **avatar import position**: 0, 3, 0 Studio position that avoids realigning in Blender

## Techniques
- t1: **Install Blender addons from disk**: Edit, Preferences, Add-ons, dropdown arrow, Install from Disk. Pick each addon in the Blender add-ons folder, such as Lazy Viewport for gizmos and the Roblox animation exporter. Use the Animation workspace.
- t2: **Dope sheet only-show-selected**: Enable the Only Show Selected filter in the dope sheet so only selected bones' keyframes are displayed, which reduces clutter.
- t3: **Clipboard-based animation transfer**: In Blender object mode with the armature selected, press N, RBX Animations, Export Animation. In Studio, open the Blender Animations plugin, select the rig, import from clipboard, paste into the script, set priority, and upload.
- t4: **Parent accessory to bone**: Select the accessory, shift-select the armature root, switch to pose mode with Ctrl+Tab, shift-select the target bone, Ctrl+P, then Bone.

## Points to
- Blender Animations plugin for Roblox Studio
- Moon Animator
- 12 Principles of Animation video
- Insert Avatar / Fast Character Loader plugin
- Lazy Viewport addon
