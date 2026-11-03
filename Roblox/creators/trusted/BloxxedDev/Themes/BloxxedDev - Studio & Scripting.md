---
title: BloxxedDev - Studio & Scripting
creator: BloxxedDev
tags: [roblox, bloxxeddev, theme]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BloxxedDev: Studio & Scripting

All BloxxedDev tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[building-art-and-assets]]
- 2024-09-28 [0:00](https://youtu.be/5cLUGex3nUY?t=0) Use a low-vertex cylinder (8 vertices) as the base for low-poly tree trunks and canopies. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [0:41](https://youtu.be/5cLUGex3nUY?t=41) Color low-poly models by UV-projecting from view and assigning a palette image as an Image Texture base color, rather than per-face colors. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [1:21](https://youtu.be/5cLUGex3nUY?t=81) If palette colors don't show in Blender, switch viewport shading from Material Preview to Solid/Viewport shading. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [2:01](https://youtu.be/5cLUGex3nUY?t=121) Shape organic silhouettes by moving individual vertices and extruding/scaling faces instead of building new primitives. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [2:44](https://youtu.be/5cLUGex3nUY?t=164) Use Ctrl+R loop cuts and scale to add a mid-section bulge so the tree looks rounder and more natural. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [3:25](https://youtu.be/5cLUGex3nUY?t=205) Export as FBX and import into Studio via View > Asset Manager; keep parts separate so you can edit them later. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2024-09-28 [3:25](https://youtu.be/5cLUGex3nUY?t=205) Import errors reported on FBX import can usually be ignored; the mesh still imports correctly. ([[2024-09-28 - Make EPIC Low Poly Trees for Roblox Studio in Blender|Make EPIC Low Poly Trees for Roblox Studio in Blen]])
- 2025-01-13 [0:10](https://youtu.be/xGXCApkkkCE?t=10) Save the place first and build terrain with the Terrain Editor draw tool; shape a messy oval, add an offset second layer, then smooth it for a natural look. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-01-13 [2:13](https://youtu.be/xGXCApkkkCE?t=133) Add water to terrain for realistic lighting and reflections; fill it about halfway up the terrain and scale it to fit so it doesn't stick out. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-01-13 [3:03](https://youtu.be/xGXCApkkkCE?t=183) Set water transparency high and tint it yellow or orange to match the sky; a solid default colour looks cartoonish. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-01-13 [3:34](https://youtu.be/xGXCApkkkCE?t=214) Pick orange or yellow toolbox skies, which look more like sunrise or sunset and read as more realistic. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-01-13 [4:15](https://youtu.be/xGXCApkkkCE?t=255) Use the Celestial Dragger plugin to position the sun lower so it lights the scene with shadows without blowing out the view. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-01-13 [4:56](https://youtu.be/xGXCApkkkCE?t=296) Reduce the sun ray intensity after playtesting; the first setting was too bright and blinded the player. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])
- 2025-06-07 [3:25](https://youtu.be/Gk-iTN8Ru_Q?t=205) Drive visual state (color) from growth progress with a single base color plus an impact multiplier, so one parameter controls how much growth changes appearance. ([[2025-06-07 - How to Make an OFFLINE PROGRESSION System in Roblox|How to Make an OFFLINE PROGRESSION System in Roblo]])
- 2025-08-02 [3:17](https://youtu.be/od95x-afmBU?t=197) Check imported map and model contents for hidden scripts and oversized geometry before placing them; large models caused lag and blocked paths. ([[2025-08-02 - I Made a VIRAL Roblox Game Using Only HORRIBLE Free Models|I Made a VIRAL Roblox Game Using Only HORRIBLE Fre]])

## [[anti-exploit-and-security]]
- 2025-08-02 [0:00](https://youtu.be/od95x-afmBU?t=0) Inspect scripts inside free models before importing; the creator says they can carry viruses or hidden scripts, and some changed game behaviour unexpectedly. ([[2025-08-02 - I Made a VIRAL Roblox Game Using Only HORRIBLE Free Models|I Made a VIRAL Roblox Game Using Only HORRIBLE Fre]])

## [[data-persistence]]
- 2025-06-07 [1:15](https://youtu.be/Gk-iTN8Ru_Q?t=75) Store each planted item's plant timestamp in DataStore so growth can be computed from elapsed time on rejoin instead of simulating while offline. ([[2025-06-07 - How to Make an OFFLINE PROGRESSION System in Roblox|How to Make an OFFLINE PROGRESSION System in Roblo]])
- 2025-06-07 [2:37](https://youtu.be/Gk-iTN8Ru_Q?t=157) Keep all live player data in one central table and route saves through shared core functions to keep the leave/rejoin logic in one place. ([[2025-06-07 - How to Make an OFFLINE PROGRESSION System in Roblox|How to Make an OFFLINE PROGRESSION System in Roblo]])

## [[3d-modeling-rigging-and-animation]]
- 2025-07-27 [0:00](https://youtu.be/rjQtLR9w2s0?t=0) To start animating, open the Avatar tab in Studio and select a rig to animate; the animation editor works from that rig. ([[2025-07-27 - Can I Learn Roblox Animation in Just 1 Hour|Can I Learn Roblox Animation in Just 1 Hour?]])
- 2025-07-27 [2:27](https://youtu.be/rjQtLR9w2s0?t=147) Extend the animation timeline length in the animation editor settings when you need more keyframes than the default length allows. ([[2025-07-27 - Can I Learn Roblox Animation in Just 1 Hour|Can I Learn Roblox Animation in Just 1 Hour?]])
- 2025-07-27 [1:20](https://youtu.be/rjQtLR9w2s0?t=80) Make the first keyframe match the last keyframe when you want a looping animation, by copying the pose and pasting it at the start. ([[2025-07-27 - Can I Learn Roblox Animation in Just 1 Hour|Can I Learn Roblox Animation in Just 1 Hour?]])
- 2025-07-27 [7:25](https://youtu.be/rjQtLR9w2s0?t=445) Set camera shots by positioning the camera at exact animation timestamps in the animation editor rather than guessing by eye during playback. ([[2025-07-27 - Can I Learn Roblox Animation in Just 1 Hour|Can I Learn Roblox Animation in Just 1 Hour?]])

## [[vfx-and-particles]]
- 2025-07-27 [8:07](https://youtu.be/rjQtLR9w2s0?t=487) Use the Cutscene Editor plugin and set it to play on CharacterAdded so camera movement starts when the animation starts. ([[2025-07-27 - Can I Learn Roblox Animation in Just 1 Hour|Can I Learn Roblox Animation in Just 1 Hour?]])

## [[optimization-and-streaming]]
- 2025-01-13 [1:33](https://youtu.be/xGXCApkkkCE?t=93) Use Leafy grass instead of normal grass to reduce lag, since it doesn't stick out as much; normal grass looks better under lighting but costs more. ([[2025-01-13 - How To Make a REALISTIC Game In Roblox Studio|How To Make a REALISTIC Game In Roblox Studio]])

Up: [[BloxxedDev - How to make successful Roblox games]]
