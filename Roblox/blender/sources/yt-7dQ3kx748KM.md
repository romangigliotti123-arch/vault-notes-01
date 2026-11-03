---
type: research-source
id: yt-7dQ3kx748KM
title: "Blender Grease Pencil Tutorial : Character Creation : Part Three - Lip Syncing (and more?)"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=7dQ3kx748KM"
published: "2021-06-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-7dQ3kx748KM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Part 3 of a Blender Grease Pencil 2D character series. Covers drawing mouth shapes per frame, using a Time Offset modifier in Fixed Frame mode, merging layers, and keyframing mouth frames against audio. Nothing on Roblox, Claude, blender-mcp, bpy, or FBX export. Relevance to the target topic is very low.

## Claims
- c1: [0:00] Video is a 2D Grease Pencil lip-sync tutorial in Blender, not about Roblox, Claude, blender-mcp, bpy, or the Roblox export pipeline. *(doc, high; other)*
- c2: [3:43] Time Offset modifier set to 'Fixed Frame' mode lets you pick which mouth-shape frame displays; regular mode plays through frames. *(demo, high; other)*
- c3: [4:53] Time Offset modifier layer influence only works on the layer it targets; merging layers down (Grease Pencil merged down) renames the result so the modifier reference must be reselected. *(demo, high; other)*
- c4: [6:42] For smooth lip sync playback, set playback to play every frame; hide heavy background and other characters with H if frame rate drops below 24 fps. *(demo, medium; other)*
- c5: [7:22] Lip sync method: add keyframes on the Time Offset modifier value at each mouth-shape change, with auto keyframing enabled so changing the number auto-keys. *(demo, high; other)*
- c6: [10:46] Same Time Offset approach is reused for blinks, hand poses and sleeve-follow-arm effects, not just mouth shapes. *(demo, medium; other)*

## Numbers
- n1: **playback frame rate target**: 24 fps 

## Techniques
- t1: **Time Offset lip sync**: Draw mouth shapes on frames, add Time Offset modifier in Fixed Frame mode, keyframe its frame value per phoneme while scrubbing audio in the Video Sequencer.
