---
type: research-source
id: yt-gALfWtOe5oU
title: "FREE ROBLOX RIGS WITH 2 FACE RIGS, R6, R15 AND MORE! (Blender 3.4+) | Fluid Rig"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=gALfWtOe5oU"
published: "2023-04-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: low
tags: ["research-source", "youtube", "creator-workflows", "other", "rigging-animation", "texturing-baking-uv"]
---
# yt-gALfWtOe5oU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender rig showcase video (Comix Productions, 2023) promoting its own free "Fluid Rig" Blender rig for Roblox-style R6/R15/Roblox 2.0 characters, not a Claude/blender-mcp or bpy pipeline tutorial. Covers Blender 3.4+ requirement, texture swapping, IK toggles, face rigs, R6/R15 generation switch, and LITE vs full file choice.

## Claims
- c1: [0:19] Rig is distributed as a zip that must be extracted; contains Standalone folder of character rigs, Resources folder, and a README. *(demo, high; creator-workflows)*
- c2: [1:16] Fluid Rig requires Blender 3.4 or later. *(doc, high; creator-workflows)*
- c3: [2:12] Cycles render settings were added to the rig UI to prevent users rendering with excessive samples such as 4096. *(demo, medium; creator-workflows)*
- c4: [11:57] LITE rig variants are recommended for low-end devices or background characters; full versions for high-end systems and main characters. *(opinion, medium; creator-workflows)*
- c5: [12:21] Roblox 2.0 LITE rig has no unlocking-limbs setting and no face rig; only generation switch remains; rig detail defaults to zero. *(demo, medium; creator-workflows)*
- c6: [10:30] Package-switching controls let the user swap rig types; switching mid-pose does not seamlessly carry pose; author suggests copying pose since bone names are nearly identical (untested). *(opinion, low; rigging-animation)*
- c7: [4:58] Unlocking limbs off limits arm/limb rotation to 90 degrees; on allows about 112 degrees, only on blocky rig. *(demo, medium; rigging-animation)*
- c8: [3:45] IK controls add arm IK alongside existing leg IK and fancy feet controls. *(demo, medium; rigging-animation)*
- c9: [1:36] Textures are swapped by opening the R6 or R15 texture file; textures show only in Material Preview or Rendered mode, not Solid. *(demo, medium; texturing-baking-uv)*
- c10: [8:12] R6/R15 switch via a 'generation' property swaps rigs without visible clipping, per author. *(demo, low; rigging-animation)*
- c11: [5:43] Rig included classic face pack controls (eyes, mouth, freckles, scar, blush) and a 2D face rig option; face rigs are the author's showcase feature. *(demo, medium; other)*

## Numbers
- n1: **Minimum Blender version**: 3.4 
- n2: **Bend angle (blocky rig, unlocked)**: 112 degrees (stated as 120 in speech) 
- n3: **Locked limb rotation limit**: 90 degrees 
- n4: **Rig detail default on LITE**: 0 

## Techniques
- t1: **Switching R6/R15 texture**: Open the R6 or R15 texture .blend file, then return to the rig file; the texture appears only in Material Preview or Rendered view.
- t2: **Smooth fix / rig detail**: Turn rig detail to zero while smooth fix stays on to keep smoothness with less load; turning smooth fix off may cause lag.

## Quotes (brief, for attribution)
> if you have a high-end device whatever use the normal files  (at 11:57, Comix Productions)

## Points to
- Gumroad (rig distribution)
- Discord server (bug reports)
