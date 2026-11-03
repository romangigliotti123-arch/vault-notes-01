---
title: "Using Roblox Tools to Improve Performance | RDC 2024"
url: https://youtu.be/cWDNVvOh4o0
creator: Roblox
official: true
advice_density: high
date: 2024-09-23
views: 17533
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Using Roblox Tools to Improve Performance | RDC 2024

[Watch](https://youtu.be/cWDNVvOh4o0) | RobloxOfficial | 17,533 views | 2024-09-23

## Summary
Roblox DevConference 2024 talk by Mr Chicken Rocket (Peter McNeill) on performance tooling. Covers a six-point health check: triangles, draw calls, CPU usage, memory, load times and bandwidth, with the built-in tools and per-device budgets for phone targets.

## Tips
- [5:59](https://youtu.be/cWDNVvOh4o0?t=359) **[[scripting-and-performance]]** Budget in-camera scene triangles, not total triangles: aim for about 500k on phone targets. Check with Ctrl/Cmd+Shift+F2 rendering stats.
- [10:39](https://youtu.be/cWDNVvOh4o0?t=639) **[[scripting-and-performance]]** Keep scene draw calls around 500 for phone targets; every draw call has a fixed cost even with one triangle. Subtract UI draw calls from the budget.
- [12:43](https://youtu.be/cWDNVvOh4o0?t=763) **[[scripting-and-performance]]** Reuse the same MeshId and material to batch draw calls. Color3 and SurfaceAppearance property changes batch well; transparency, decals and textures add draw calls.
- [18:56](https://youtu.be/cWDNVvOh4o0?t=1136) **[[scripting-and-performance]]** Use transparent and decal-heavy elements sparingly; they break batching and raise draw calls. Re-check the scene draw-call budget as you build.
- [21:29](https://youtu.be/cWDNVvOh4o0?t=1289) **[[scripting-and-performance]]** Test CPU on real low-end phones: a 10 ms PC frame can become ~40 ms on phone. Target under 16.66 ms per frame for 60 FPS.
- [25:25](https://youtu.be/cWDNVvOh4o0?t=1525) **[[scripting-and-performance]]** Spread raycasts and heavy loops across frames; use the Microprofiler (Ctrl/Cmd+F6) to find script hotspots.
- [27:36](https://youtu.be/cWDNVvOh4o0?t=1656) **[[scripting-and-performance]]** Target 2 GB devices. Ejections rise around 66% of device memory (~1.3 GB client memory). Check with F9 on device, not in Studio.
- [30:08](https://youtu.be/cWDNVvOh4o0?t=1808) **[[building-art-and-assets]]** Watch texture memory: one fully resident 1,024 SurfaceAppearance set is ~2.8 MB; 100 of them is ~300 MB of client memory.
- [30:49](https://youtu.be/cWDNVvOh4o0?t=1849) **[[scripting-and-performance]]** Limit instances sent to the client with StreamingEnabled; each part costs roughly 1 KB of client memory.
- [31:30](https://youtu.be/cWDNVvOh4o0?t=1890) **[[building-art-and-assets]]** Don't keep audio resident on the client until it is needed; loaded sounds sit in memory.
- [32:52](https://youtu.be/cWDNVvOh4o0?t=1972) **[[first-session-onboarding]]** Keep load time down: about 10,000 instances replicate per second on join, so 150k instances is ~15 s. Use StreamingEnabled and a content-aware loading bar.
- [33:34](https://youtu.be/cWDNVvOh4o0?t=2014) **[[first-session-onboarding]]** Remember textures, audio and other players' character appearances must finish loading before a player enters; new joiners push load back up.
- [34:15](https://youtu.be/cWDNVvOh4o0?t=2055) **[[scripting-and-performance]]** Limit server-owned moving assemblies to about 50 at a time (~1 KB/s each). Watch the recv stat (Ctrl/Cmd+F7).
- [3:58](https://youtu.be/cWDNVvOh4o0?t=238) **[[development-process-and-speed]]** Check performance continuously during development rather than doing an optimization pass at the end.
- [3:17](https://youtu.be/cWDNVvOh4o0?t=197) **[[retention-d1-d7]]** Slow loads and overheating phones end sessions early; optimized games get played longer, and more than half of players are on mobile.

## Numbers
- [8:05](https://youtu.be/cWDNVvOh4o0?t=485) Example scene draw calls / triangles: **77 draw calls, ~130,000 triangles** (Example hotspot in rendering stats)
- [8:38](https://youtu.be/cWDNVvOh4o0?t=518) Phone scene triangle budget: **~500,000 (iPhone 6s / Galaxy S6 class, 2GB)** (Covers ~90% of player base per speaker)
- [10:39](https://youtu.be/cWDNVvOh4o0?t=639) Scene draw call budget: **~500 for phone; iPhone 4 Jetpack budget was 40** (Speaker's phone target)
- [17:36](https://youtu.be/cWDNVvOh4o0?t=1056) Shadow draw calls healthy ratio: **Up to 3x scene draw calls** (Only for shadow-enabled rendering modes)
- [21:29](https://youtu.be/cWDNVvOh4o0?t=1289) CPU frame budget at 60 FPS: **16.66 ms** (Per-frame CPU and GPU must stay under this)
- [22:09](https://youtu.be/cWDNVvOh4o0?t=1329) Low-end phone CPU slowdown: **~4x slower than average desktop (~1 GHz)** (10 ms PC frame becomes ~40 ms, ~20 FPS)
- [27:36](https://youtu.be/cWDNVvOh4o0?t=1656) Client memory ejection threshold (2GB device): **~66% of total memory, ~1.3 GB** (Ejections increase above this point)
- [30:08](https://youtu.be/cWDNVvOh4o0?t=1808) Max resident SurfaceAppearance texture memory: **2.8 MB per 1,024x1,024 set; 100 sets ~300 MB** (Fully resident surface appearance textures)
- [30:49](https://youtu.be/cWDNVvOh4o0?t=1849) Client memory per Part: **~1 KB; 250k parts ~250 MB** (Approximate system impact)
- [32:52](https://youtu.be/cWDNVvOh4o0?t=1972) Instance replication rate on connect: **~10,000 instances/s; 300k instances = ~30 s load** (Speaker's benchmark)
- [35:38](https://youtu.be/cWDNVvOh4o0?t=2138) Recommended instance count: **~150,000 instances (~15 s load)** (Speaker's preferred benchmark)
- [34:15](https://youtu.be/cWDNVvOh4o0?t=2055) Moving server assembly bandwidth: **~1 KB/s each; 50 = ~50 KB/s; throttling near 40 KB/s** (Recv stat, Ctrl/Cmd+F7)
- [2:37](https://youtu.be/cWDNVvOh4o0?t=157) Extra play hours from engine optimizations: **300 million** (Claimed from keynote)
- [3:17](https://youtu.be/cWDNVvOh4o0?t=197) Share of players on mobile: **More than half** (Speaker's claim)

## Games
- **Jetpack Joy Ride** [0:47](https://youtu.be/cWDNVvOh4o0?t=47): Shipped under 20 MB; iPhone 4 scene draw call budget was 40, showing how tight early mobile budgets were.
- **Candy Crush** [2:03](https://youtu.be/cWDNVvOh4o0?t=123): Speaker was engine director on it; background only.
- **Fruit Ninja** [1:23](https://youtu.be/cWDNVvOh4o0?t=83): Speaker worked on several versions; background only.

## Tools
Rendering stats (Ctrl/Cmd+Shift+F2), Microprofiler (Ctrl/Cmd+F6), F9 memory bar (device client memory), Developer Console memory tab, F7 network stats (recv), Analytics dashboard crash/memory insights, StreamingEnabled, SurfaceAppearance

## He points to
- Roblox DevForum performance article/book by Mr Chicken Rocket (QR code shown)
- Roblox Docs Microprofiler documentation

## Quotes
- [3:58](https://youtu.be/cWDNVvOh4o0?t=238) "it's way better to stay on top of performance and optimization as you work on your project as opposed to making it a process that you try and do at the end"
- [26:26](https://youtu.be/cWDNVvOh4o0?t=1586) "most crashes in Roblox are really out of memory errors"

## On screen
Contact sheet shows rendering stats overlay, triangle-budget history bar chart (N64 2,000 to PS5 10,000,000 triangles), batching tier list, 2-draw-call example, microprofiler healthy vs overloaded frames, memory 2GB device ejection cards with 'Aim for <1.3GB client memory', and the analytics dashboard crash insights panel.

## Topics
[[building-art-and-assets]] [[development-process-and-speed]] [[first-session-onboarding]] [[retention-d1-d7]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
