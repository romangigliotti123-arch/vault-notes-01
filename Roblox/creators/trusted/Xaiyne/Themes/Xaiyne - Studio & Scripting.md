---
title: Xaiyne - Studio & Scripting
creator: Xaiyne
tags: [roblox, xaiyne, theme]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Xaiyne: Studio & Scripting

All Xaiyne tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[building-art-and-assets]]
- 2025-08-08 [0:51](https://youtu.be/aqv5bLmqbzc?t=51) Use a free R15 dummy from Toolbox that has no scripts to avoid malicious code; check reviews first. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])
- 2026-03-17 [1:58](https://youtu.be/O5FjkMlRPPI?t=118) Use an R15 rig in Studio's Avatar > Animation editor; pick a rig whose front/back colours are visible so limbs aren't misposed. ([[2026-03-17 - How I made $690,000 ROBUX as a small developer|How I made $690,000 ROBUX as a small developer]])
- 2026-03-17 [4:02](https://youtu.be/O5FjkMlRPPI?t=242) Make emote animations loop: keyframe a start pose, a mid-point pose, copy the first keyframe to the end so motion returns smoothly. ([[2026-03-17 - How I made $690,000 ROBUX as a small developer|How I made $690,000 ROBUX as a small developer]])
- 2026-03-17 [5:26](https://youtu.be/O5FjkMlRPPI?t=326) Switch keyframes to curved interpolation so motion eases in and out instead of looking robotic; compare with Play before saving. ([[2026-03-17 - How I made $690,000 ROBUX as a small developer|How I made $690,000 ROBUX as a small developer]])
- 2026-10-12 [2:05](https://youtu.be/KhKOSmdX8sc?t=125) Keep UGC accessory meshes under Roblox's 4,000 triangle limit; the speaker targets 3,990 as a safe buffer. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])
- 2026-10-12 [3:29](https://youtu.be/KhKOSmdX8sc?t=209) Export textures at 2K and FBX format, the highest texture resolution Roblox supports for meshes. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])
- 2026-10-12 [3:42](https://youtu.be/KhKOSmdX8sc?t=222) In Studio, ungroup the imported mesh, rename it to Handle, place it inside an Accessory, then fit it using the Avatar accessory tool preview on a character. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])
- 2026-10-21 [3:52](https://youtu.be/wkfCP_09CI8?t=232) Extract the Tripo zip before importing; import FBX via File > Import, then press 3 to scale and Ctrl+U to ungroup, renaming the part to Handle. ([[2026-10-21 - How I Made $1,000 Making Roblox UGC With AI (Tutorial)|How I Made $1,000 Making Roblox UGC With AI (Tutor]])
- 2026-10-21 [5:14](https://youtu.be/wkfCP_09CI8?t=314) Use Avatar Editor accessory fitting: place model in the Face bounds (box turns blue when within limits) before clicking Generate Mesh Part Accessory. ([[2026-10-21 - How I Made $1,000 Making Roblox UGC With AI (Tutorial)|How I Made $1,000 Making Roblox UGC With AI (Tutor]])
- 2026-10-21 [6:21](https://youtu.be/wkfCP_09CI8?t=381) Use the free ThumbMaker plugin to produce the marketplace thumbnail from the Handle, then right-click Handle > Save and Export to Roblox. ([[2026-10-21 - How I Made $1,000 Making Roblox UGC With AI (Tutorial)|How I Made $1,000 Making Roblox UGC With AI (Tutor]])

## [[ai-and-tools]]
- 2026-10-12 [0:41](https://youtu.be/KhKOSmdX8sc?t=41) Use a current image-to-3D model (speaker used Tripo AI) for UGC base meshes; older AI models looked too poor to sell. Refine in Blender if time allows. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])
- 2026-10-12 [2:48](https://youtu.be/KhKOSmdX8sc?t=168) Choose the cheaper HD model setting over Smart Mesh; Smart Mesh gives better results but costs substantially more credits. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])
- 2026-10-21 [2:47](https://youtu.be/wkfCP_09CI8?t=167) In Tripo AI, set texture 2K, PBR off (cheaper upload), triangle count under Roblox's 4,000 max (he used 3,990). ([[2026-10-21 - How I Made $1,000 Making Roblox UGC With AI (Tutorial)|How I Made $1,000 Making Roblox UGC With AI (Tutor]])

## [[3d-modeling-rigging-and-animation]]
- 2025-08-08 [2:12](https://youtu.be/aqv5bLmqbzc?t=132) Use R15 rather than R6 for emotes; R15 has 15 parts and is more versatile and widely used. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])
- 2025-08-08 [3:35](https://youtu.be/aqv5bLmqbzc?t=215) Keyframe each body part; rotating an upper part moves its children (hierarchy), so animate upper limbs first to get natural motion. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])
- 2025-08-08 [4:16](https://youtu.be/aqv5bLmqbzc?t=256) Keep emote length under 10 seconds, the maximum allowed for emotes and animations. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])
- 2025-08-08 [7:39](https://youtu.be/aqv5bLmqbzc?t=459) Make the last keyframe match the first (e.g. same rotation at loop end) so looping emotes don't visibly snap. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])
- 2025-08-08 [8:42](https://youtu.be/aqv5bLmqbzc?t=522) Set the animation to curve type before upload; the marketplace only accepts curve animations. ([[2025-08-08 - How to Make Custom UGC EMOTES for Roblox|How to Make Custom UGC EMOTES for Roblox]])

## [[ui-ux-design]]
- 2026-10-12 [5:45](https://youtu.be/KhKOSmdX8sc?t=345) Use a thumbnail maker plugin to preview how the accessory looks in store listings before uploading. ([[2026-10-12 - How to Make VIRAL Roblox UGC with AI|How to Make VIRAL Roblox UGC with AI...]])

Up: [[Xaiyne - How to make successful Roblox games]]
