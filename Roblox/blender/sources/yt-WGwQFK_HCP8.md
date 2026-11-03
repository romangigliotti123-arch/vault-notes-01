---
type: research-source
id: yt-WGwQFK_HCP8
title: "Roblox Cutscenes Made Easy (2026) [Full tutorial]"
source_type: "youtube"
creator: "Rool-Studio"
url: "https://www.youtube.com/watch?v=WGwQFK_HCP8"
published: "2026-01-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "rigging-animation"]
---
# yt-WGwQFK_HCP8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio cutscene tutorial (no Blender content). Shows a camera part attached via Motor6D to HumanoidRootPart, animated in the Animator with the rig, published, then played from a LocalScript via a button or a Touched trigger part. Nothing on blender-mcp, bpy, or Blender-to-Roblox export.

## Claims
- c1: [0:08] Cutscene method: add a small part named 'cam' under the rig, attach a SurfaceGui with a frame to show camera direction, and join it to the rig with a Motor6D. *(demo, medium; rigging-animation)*
- c2: [0:08] Motor6D setup: Part0 = HumanoidRootPart, Part1 = cam, so the camera part moves and rotates with the character during animation. *(demo, medium; rigging-animation)*
- c3: [0:49] Animate rig and camera together in the Animator (Avatar tab), publish the animation, and copy its asset ID for use in a script. *(demo, medium; rigging-animation)*
- c4: [1:30] Button trigger: ScreenGui > TextButton with a LocalScript that loads the saved animation ID, gets character, camera, and RunService, and connects a loop that plays the animation and updates camera position. *(demo, medium; automation-and-creator-workflows)*
- c5: [1:30] Part trigger variant: copy the button script to StarterPlayerScripts, add a trigger part in Workspace and an animation under the script, and replace button click logic with a Touched event. *(demo, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Motor6D Part0/Part1**: HumanoidRootPart / cam 

## Techniques
- t1: **Camera-part rig attachment**: Add part 'cam' under rig; SurfaceGui frame for direction; Motor6D Part0=HumanoidRootPart, Part1=cam; animate rig+cam in Animator; publish.
- t2: **LocalScript cutscene playback**: Button click or Touched event loads animation by ID, plays it on character, and drives Camera each RunService frame.
