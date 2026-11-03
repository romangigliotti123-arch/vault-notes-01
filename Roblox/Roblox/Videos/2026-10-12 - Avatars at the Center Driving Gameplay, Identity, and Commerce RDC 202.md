---
title: "Avatars at the Center: Driving Gameplay, Identity, and Commerce | RDC 2026"
url: https://youtu.be/gCp4zzjjJ14
creator: Roblox
official: true
advice_density: medium
date: 2026-10-12
views: 8491
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Avatars at the Center: Driving Gameplay, Identity, and Commerce | RDC 2026

[Watch](https://youtu.be/gCp4zzjjJ14) | RobloxOfficial | 8,491 views | 2026-10-12

## Summary
RDC 2026 talk on Roblox avatar tech: upgraded R15-superset rig with finger/hand bones, adaptive animations across R6/R15/custom rigs, animation graphs, Lua-based Character Controller Library, Slim/LOD avatar optimisation, auto-setup, and avatar economy growth stats, with Aetherfall developers and a marketplace creator.

## Tips
- [5:05](https://youtu.be/gCp4zzjjJ14?t=305) **[[building-art-and-assets]]** Adaptive animations let one R15 animation clip play on R6, R15 and custom rigs via humanoid rig description, so no reauthoring is needed.
- [5:51](https://youtu.be/gCp4zzjjJ14?t=351) **[[building-art-and-assets]]** Use animation graphs (node editor in Studio) so animators can own movement logic without writing Luau; swap animation IDs and speed parameters visually.
- [7:50](https://youtu.be/gCp4zzjjJ14?t=470) **[[scripting-and-performance]]** Use the Character Controller Library: transparent Lua replacement for the C++ Humanoid, debuggable and extensible with custom abilities like dashes or double jumps.
- [9:10](https://youtu.be/gCp4zzjjJ14?t=550) **[[development-process-and-speed]]** Tune movement by iterating in playtests rather than editing code repeatedly; CCL makes feel adjustments fast to test.
- [9:51](https://youtu.be/gCp4zzjjJ14?t=591) **[[scripting-and-performance]]** Use CCL action slots so abilities are bound per action rather than per device, avoiding separate mobile/console fixes.
- [11:26](https://youtu.be/gCp4zzjjJ14?t=686) **[[scripting-and-performance]]** Slim for avatars plus LODs gives about 10x fewer triangles at distance with no extra work, for standard R15 player avatars (not yet NPCs or custom scaled avatars).
- [12:33](https://youtu.be/gCp4zzjjJ14?t=753) **[[building-art-and-assets]]** Use Auto Setup with Platform or Development presets to turn a raw mesh into a rigged avatar in minutes; it only fills in missing parts of pre-rigged bodies.
- [13:34](https://youtu.be/gCp4zzjjJ14?t=814) **[[monetisation-other]]** Marketplace creators cite makeup as a major growth driver; do not overweight negative posts when a new category launches.
- [17:41](https://youtu.be/gCp4zzjjJ14?t=1061) **[[ai-and-tools]]** The speaker's generated-UGC system draws only from their own catalog of UGC items to keep quality high, and players said they did not want AI use.
- [18:23](https://youtu.be/gCp4zzjjJ14?t=1103) **[[pricing]]** Emissive UGC has a higher price floor by design, to protect the novelty of the new tech from being washed out.
- [22:31](https://youtu.be/gCp4zzjjJ14?t=1351) **[[building-art-and-assets]]** If Auto Setup output is inconsistent, file a dev forum bug report, or pre-fix the mesh part (e.g. head seams in Blender) and reimport.
- [23:11](https://youtu.be/gCp4zzjjJ14?t=1391) **[[building-art-and-assets]]** Roblox is looking at exposing animation data sources to the graph so values can be set from code, useful for data-driven reloads.
- [24:34](https://youtu.be/gCp4zzjjJ14?t=1474) **[[building-art-and-assets]]** Importing high-poly separated meshes from another engine can flood inventory with parts; previews before committing would prevent this.

## Numbers
- [13:34](https://youtu.be/gCp4zzjjJ14?t=814) Avatar item transactions growth: **Daily 3D avatar transactions up 28% YoY; avatar purchasers up 16% YoY** (Platform-wide avatar commerce growth, last year)
- [14:15](https://youtu.be/gCp4zzjjJ14?t=855) Marketplace creator growth: **63% YoY growth in marketplace creators** (New creators entering avatar marketplace within the last year)
- [11:26](https://youtu.be/gCp4zzjjJ14?t=686) Slim for avatars triangle reduction: **~10x fewer triangles at distance** (In a 200-avatar scene with no extra work required)
- [16:21](https://youtu.be/gCp4zzjjJ14?t=981) In-experience creation output: **Millions of unique creations** (Clothing and accessories, about 10 months after IEC launch)

## Games
- **Aetherfall** [2:17](https://youtu.be/gCp4zzjjJ14?t=137): RPG built on custom R15 rig with finger articulation for NPC gestures; CCL for dash/double jump, animation graphs for movement.
- **Chain Maker (Jonathan's experience)** [15:39](https://youtu.be/gCp4zzjjJ14?t=939): Players craft custom chains via text editor in-experience; shows demand for player-driven creation tools.

## Tools
Animation graphs (Studio), Character Controller Library (CCL), Auto Setup, Slim for avatars / LODs, Humanoid rig description

## He points to
- Roblox developer forum (bug reports for Auto Setup)

## Quotes
- [13:34](https://youtu.be/gCp4zzjjJ14?t=814) "Makeup's been a very big driver in my overall growth this year as a marketplace creator."
- [17:41](https://youtu.be/gCp4zzjjJ14?t=1061) "Players told me that they were not artists and they wanted help in creating their vision, but they were also clear about not wanting AI use."

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[development-process-and-speed]] [[monetisation-other]] [[pricing]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
