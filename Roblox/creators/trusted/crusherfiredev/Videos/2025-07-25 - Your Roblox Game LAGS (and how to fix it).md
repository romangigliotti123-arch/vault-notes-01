---
title: "Your Roblox Game LAGS (and how to fix it)"
url: https://youtu.be/YWyJHwynM1M
creator: Crusherfire
official: false
advice_density: high
date: 2025-07-25
views: 68191
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Your Roblox Game LAGS (and how to fix it)

[Watch](https://youtu.be/YWyJHwynM1M) | crusherfiredev | 68,191 views | 2025-07-25

## Summary
Performance optimization guide for Roblox games, especially mobile. Covers memory (collision fidelity, sounds, ReplicatedStorage vs ServerStorage, PlayerCharacterDestroyBehavior, textures), draw calls and occlusion, mesh render fidelity, humanoid state machine, BulkMoveTo, animator throttling, physics stepping, and network incoming bandwidth.

## Tips
- [1:42](https://youtu.be/YWyJHwynM1M?t=102) **[[scripting-and-performance]]** Open F9 developer console, Memory tab, sort by high usage; check Physics Parts and Sounds categories to find memory hogs.
- [2:23](https://youtu.be/YWyJHwynM1M?t=143) **[[optimization-and-streaming]]** Set collision fidelity to Box for non-colliding objects, Hole for cylindrical/round colliders, avoid Precise/Default. Use Collision Fidelity visualizer in Settings.
- [8:35](https://youtu.be/YWyJHwynM1M?t=515) **[[optimization-and-streaming]]** For complex collision, disable collisions on the mesh, set fidelity to Box, and build collision manually from simple parts.
- [9:04](https://youtu.be/YWyJHwynM1M?t=544) **[[optimization-and-streaming]]** Don't store sound instances in SoundService; keep sound IDs in scripts and create/play/destroy sounds at runtime to cut sound memory (his game: 500MB to 58MB).
- [11:39](https://youtu.be/YWyJHwynM1M?t=699) **[[optimization-and-streaming]]** Move maps and assets clients don't need yet from ReplicatedStorage to ServerStorage to reduce client memory and load time.
- [12:34](https://youtu.be/YWyJHwynM1M?t=754) **[[scripting-and-performance]]** Set Workspace PlayerCharacterDestroyBehavior to Enable to avoid leaked connections on character models and players.
- [13:42](https://youtu.be/YWyJHwynM1M?t=822) **[[building-art-and-assets]]** Downscale textures to 512x512 where possible, use texture atlases and trim sheets; 1024 uses 4x the graphics memory of 512.
- [15:31](https://youtu.be/YWyJHwynM1M?t=931) **[[optimization-and-streaming]]** Enable StreamingEnabled to stream workspace objects in and out, reducing load times and memory.
- [16:05](https://youtu.be/YWyJHwynM1M?t=965) **[[optimization-and-streaming]]** Keep Scene Draw Count under about 500 (thousands is a problem) and triangles around 500k, especially for mobile.
- [18:55](https://youtu.be/YWyJHwynM1M?t=1135) **[[optimization-and-streaming]]** Occlusion culling does not apply to particles, beams, trails, or grass; manually disable them when far from the camera.
- [19:35](https://youtu.be/YWyJHwynM1M?t=1175) **[[optimization-and-streaming]]** Use Shadow Map lighting with global shadows disabled to drop shadow draw calls to zero for mobile.
- [21:31](https://youtu.be/YWyJHwynM1M?t=1291) **[[building-art-and-assets]]** Reuse identical mesh IDs: meshes imported with separate IDs (duplicate trees, doors, tires) break batching into separate draw calls. Shipping container draw calls fell 50% after fixing.
- [24:08](https://youtu.be/YWyJHwynM1M?t=1448) **[[optimization-and-streaming]]** Set MeshPart Render Fidelity to Automatic instead of Precise; Performance is an option if visuals allow.
- [26:38](https://youtu.be/YWyJHwynM1M?t=1598) **[[optimization-and-streaming]]** On static NPC humanoids, disable Evaluate State Machine; on walking-only NPCs disable unused humanoid states.
- [27:51](https://youtu.be/YWyJHwynM1M?t=1671) **[[scripting-and-performance]]** Use Workspace:BulkMoveTo with BulkMoveMode FireCFrameChanged for many moving parts; it took ~0.49ms vs 0.255ms in his test, and individual CFrame sets were slower.
- [32:02](https://youtu.be/YWyJHwynM1M?t=1922) **[[optimization-and-streaming]]** Enable Workspace ClientAnimatorThrottling so distant animators update at a lower rate.
- [32:43](https://youtu.be/YWyJHwynM1M?t=1963) **[[optimization-and-streaming]]** Set Workspace PhysicsSteppingMethod to Adaptive to reduce physics calculations.
- [33:07](https://youtu.be/YWyJHwynM1M?t=1987) **[[optimization-and-streaming]]** Keep overall incoming network data under about 50 KB/s; reduce unanchored assemblies, welds and motor6D chains on the server.
- [35:53](https://youtu.be/YWyJHwynM1M?t=2153) **[[client-server-and-remotes]]** Serialize frequent replicated data with buffers; a dev forum case cut bandwidth from 300-350 KB/s to about 5 KB/s by having clients simulate.
- [36:33](https://youtu.be/YWyJHwynM1M?t=2193) **[[client-server-and-remotes]]** Never tween or play animations on the server; have clients play them via RemoteEvent. Don't set CFrames for many parts on the server each frame.

## Numbers
- [1:42](https://youtu.be/YWyJHwynM1M?t=102) Physics parts memory: **~1 MB base template; ~420 MB in his project; 1000 MB is a concern threshold**
- [9:04](https://youtu.be/YWyJHwynM1M?t=544) Sounds memory: **~500 MB is a sign of too many loaded sounds; his game uses 58 MB after runtime sound creation**
- [14:23](https://youtu.be/YWyJHwynM1M?t=863) Texture memory: **1024x1024 uses 4x graphics memory of 512x512**
- [16:05](https://youtu.be/YWyJHwynM1M?t=965) Scene draw count budget: **~500 (Mr. Chicken Rocket recommendation); ~500k triangles**
- [25:29](https://youtu.be/YWyJHwynM1M?t=1529) Mesh render fidelity distances: **<250 studs high, 250-500 medium, >500 lowest**
- [33:07](https://youtu.be/YWyJHwynM1M?t=1987) Incoming network baseline: **below 50 KB/s consistently**
- [31:16](https://youtu.be/YWyJHwynM1M?t=1876) BulkMoveTo timing: **~0.49ms individual vs 0.255ms with FireCFrameChanged (~50% faster)**
- [36:33](https://youtu.be/YWyJHwynM1M?t=2193) Bandwidth reduction (dev forum case): **300-350 KB/s down to ~5 KB/s (60x)**
- [23:34](https://youtu.be/YWyJHwynM1M?t=1414) Shipping container draw calls: **reduced 50% by reusing mesh IDs**

## Tools
Roblox Studio F9 Developer Console, Studio Statistics (Ctrl+Shift+F2), MicroProfiler, Explorer search (collision fidelity, render fidelity), Settings collision fidelity visualizer, Roblox documentation

## He points to
- Mr. Chicken Rocket (Roblox performance recommendations)
- Roblox DevForum post on 60x bandwidth reduction
- Roblox documentation on StreamingEnabled and meshes
- Creator's client fidelity service video (self-reference)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
