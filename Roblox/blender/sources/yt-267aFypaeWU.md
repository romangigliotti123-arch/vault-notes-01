---
type: research-source
id: yt-267aFypaeWU
title: "Roblox ANIMATION Guide #1 - Moon Animator (2026)"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=267aFypaeWU"
published: "2025-10-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt-267aFypaeWU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial on animating Roblox R6 rigs in Moon Animator (a Roblox Studio plugin), not Blender. Covers keybinds, keyframes, onion skin, camera FOV, easing, OBS recording, exporting animations to Roblox via Save/Export, and copying animations between rigs. No Blender, bpy, blender-mcp, Claude, or Blender-to-Roblox export content.

## Claims
- c1: Moon Animator is a Roblox Studio plugin used to animate R6 rigs; the video inserts rigs via Plugins > Character Inserter. *(demo, high; rigging-animation)*
- c2: Exporting a Moon Animator animation: explorer Rigs > anim saves model > right-click keyframe object > Save/Export to Roblox, which yields an animation ID and share link. *(demo, high; rigging-animation)*
- c3: Copying an animation to another rig: add rig, export source as anim saves model, then File > Import and Paste Keyframes onto target rig. *(demo, high; rigging-animation)*
- c4: Video does not cover Blender, bpy, blender-mcp, Claude, or Blender-to-Roblox mesh import; these topics are absent. *(doc, high; other)*

## Numbers
- n1: **Default timeline length**: 5 seconds 
- n2: **FPS default / choppy option**: 60 default; 24 suggested for choppy look 
- n3: **Camera FOV range and typical value**: Limit 120; typical 50-80 
- n4: **Recording resolution**: HD 1080 device emulator, actual resolution 

## Techniques
- t1: **Duplicate-loop run cycle**: Keyframe a pose, move 30 frames forward, select keyframes, Ctrl+C, Ctrl+R, Ctrl+V to paste a copy for a looping animation.
- t2: **Onion skin reference**: Press B to show prior pose outline, then animate new pose against it to judge arc and distance of motion.

## Points to
- Moon Animator
- OBS
