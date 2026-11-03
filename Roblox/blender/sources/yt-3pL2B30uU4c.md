---
type: research-source
id: yt-3pL2B30uU4c
title: "Eclipse Animator - Beginner's Guide (2026)"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=3pL2B30uU4c"
published: "2026-10-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "other", "rigging-animation"]
---
# yt-3pL2B30uU4c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner walkthrough of Eclipse Animator, a Roblox Studio plugin for posing and animating R6/R15 rigs. It does not cover Blender, bpy, Claude/MCP, or Blender-to-Roblox export. Only the Roblox-side animation export is relevant to the asset pipeline topic.

## Claims
- c1: [0:09] Eclipse Animator is found by searching the Creator Store in Roblox Studio; the video says it is free for a few days after release. *(demo, medium; other)*
- c2: [0:23] Rig Tools lets you insert a rig by Roblox username, or a template, in R6 or R15; the video says most users animate in R6. *(demo, high; rigging-animation)*
- c3: [1:04] Accessories tab accepts a full Marketplace URL, so the asset ID does not need to be copied; inserted accessories come pre-parented and move with the rig. *(demo, high; avatar-ugc-accessories)*
- c4: [1:46] Tools/swords work without a primary part or model setup; only the arm and tool need welding (Alt-select arm, Ctrl-select tool, bind in place). *(demo, medium; rigging-animation)*
- c5: [2:10] Animations can be imported onto a selected rig from the Animation tab and then edited in place. *(demo, medium; rigging-animation)*
- c6: [3:28] Animated GIF menu backgrounds need Preferences search for GIF; preset 3 does not move, 2 moves at low FPS, 1 moves smoothly. *(demo, medium; other)*
- c7: [4:02] Ctrl+C/Ctrl+V can paste the wrong object (e.g., spawn location) when that was last copied; Shift+C/Shift+V copies keyframes reliably most of the time. *(experience, medium; other)*
- c8: [6:03] Live recording must stay on or moving a part creates no keyframe; it acts like auto-keying. Loop toggle loops after the timeline end (30 frames in demo). *(demo, high; rigging-animation)*
- c9: [6:40] Default FPS is set in Preferences (24 or 60 shown); per-animation FPS is in File > Animation Settings. Enabling transform channels may break existing animations. *(demo, medium; rigging-animation)*
- c10: [7:36] Edit > Paste Flipped mirrors a pose, but in the demo it flipped everything unexpectedly; the presenter suspects a bug. *(demo, low; rigging-animation)*
- c11: [8:20] Ctrl+B toggles camera view in Eclipse; FOV is set by keyframe values or dragging handles. *(demo, medium; other)*
- c12: [9:46] IK toggle sits beside FK; presenter uses IK on both legs only, not arms or torso, and says IK lets the torso move without dragging legs. *(opinion, medium; rigging-animation)*
- c13: [10:27] Pole handles are enabled by default; they can be disabled in Preferences by searching 'pole'. *(demo, medium; rigging-animation)*
- c14: [10:36] P resets position and U resets rotation for the selected bone or whole rig. *(demo, high; rigging-animation)*
- c15: [11:18] Default rotation mode is quaternion; presenter recommends switching to Euler XYZ in Preferences, calling quaternion more complicated (opinion). *(opinion, medium; rigging-animation)*
- c16: [12:09] Interpolation modes (constant, bezier, linear) and easing styles are set by double-clicking a keyframe; constant gives choppy stop-motion-like motion. *(demo, medium; rigging-animation)*
- c17: [13:29] Dynamic parenting: unparenting a part (e.g., head or tool) at a keyframe makes it detach mid-animation; it is set via the icon next to the handle. *(demo, medium; rigging-animation)*
- c18: [14:46] Built-in library saves poses, animations, faces and sounds, which the presenter says Roblox itself does not offer for poses. *(opinion, medium; automation-and-creator-workflows)*
- c19: [15:57] Export Animation icon saves the animation directly to Roblox (Save to Roblox dialog), for use in games or sending to commission clients. *(demo, high; rigging-animation)*

## Numbers
- n1: **FPS options**: 24 default, 60 shown 
- n2: **GIF preset**: 1 smooth, 2 low FPS, 3 static 
- n3: **Loop length**: 30 frames in demo 

## Techniques
- t1: **Reset pose**: Select bone or rig; press P to clear position, U to clear rotation.
- t2: **Keyframe copy/paste**: Select keyframes; Shift+C copy, Shift+V paste (Ctrl+C may paste scene objects instead).
- t3: **Mid-animation unparent**: Click the handle-side icon at a keyframe to detach a part from its parent at that frame.
