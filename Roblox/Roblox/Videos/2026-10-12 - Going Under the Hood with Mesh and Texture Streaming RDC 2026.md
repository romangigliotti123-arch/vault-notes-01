---
title: "Going Under the Hood with Mesh and Texture Streaming | RDC 2026"
url: https://youtu.be/OToDz3Ghpjo
creator: Roblox
official: true
advice_density: medium
date: 2026-10-12
views: 2530
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Going Under the Hood with Mesh and Texture Streaming | RDC 2026

[Watch](https://youtu.be/OToDz3Ghpjo) | RobloxOfficial | 2,530 views | 2026-10-12

## Summary
Roblox rendering talk (RDC 2026) explaining texture streaming, mesh streaming and the new mesh LOD system: how they manage memory budgets, load times, and performance, with Driving Empire and Sesame Street as examples, plus limitations and adoption guidance.

## Tips
- [22:39](https://youtu.be/OToDz3Ghpjo?t=1359) **[[scripting-and-performance]]** Mesh LOD/streaming can significantly cut GPU frame time in heavy scenes (gas station: ~12.5ms to just under 6ms on Samsung S20). Reducing geometry matters most on mobile.
- [24:15](https://youtu.be/OToDz3Ghpjo?t=1455) **[[building-art-and-assets]]** Disable your own custom mesh LOD systems when enabling Roblox mesh streaming; otherwise you get LODs of LODs.
- [24:55](https://youtu.be/OToDz3Ghpjo?t=1495) **[[building-art-and-assets]]** Increase texture variety and resolution incrementally while monitoring stability, since texture streaming now scales automatically across devices.
- [24:55](https://youtu.be/OToDz3Ghpjo?t=1495) **[[building-art-and-assets]]** Enable mesh streaming via its workspace property (opt-in phase); skinned meshes are not yet supported.
- [27:38](https://youtu.be/OToDz3Ghpjo?t=1658) **[[building-art-and-assets]]** Don't use texture atlases unless needed; if you use them, ensure parts sharing an atlas are on screen together, since streaming unloads whole maps only.
- [27:38](https://youtu.be/OToDz3Ghpjo?t=1658) **[[building-art-and-assets]]** When memory and draw calls conflict, prioritise memory: running out of memory is fatal, while slower performance is less severe.
- [29:44](https://youtu.be/OToDz3Ghpjo?t=1784) **[[building-art-and-assets]]** Use uniform UV density across texture mapping so the system doesn't wrongly request higher-resolution mips.
- [16:58](https://youtu.be/OToDz3Ghpjo?t=1018) **[[building-art-and-assets]]** Avoid heavy UI textures on desktop for now; UI textures are not streamable there yet.
- [29:44](https://youtu.be/OToDz3Ghpjo?t=1784) **[[scripting-and-performance]]** Use Slim (runtime baked model optimisation) only if you can afford baking and don't change the object at runtime; mesh LODs/streaming work without that constraint.

## Numbers
- [16:17](https://youtu.be/OToDz3Ghpjo?t=977) Average time to load all textures at ideal quality (Android): **22s before -> 14s with texture streaming; 11s to minimal quality**
- [16:58](https://youtu.be/OToDz3Ghpjo?t=1018) Overall client transferred bytes: **Roughly halved across the platform**
- [21:59](https://youtu.be/OToDz3Ghpjo?t=1319) Triangle reduction, Driving Empire scene: **About one third of raw triangles at quality level 1; about one fifth at level 21**
- [21:21](https://youtu.be/OToDz3Ghpjo?t=1281) Triangle reduction, Beyond the Dark: **About half at quality level 1; about one fifth at quality level 21**
- [8:21](https://youtu.be/OToDz3Ghpjo?t=501) Sample level load time: **About 3s with texture streaming vs about 20s legacy**
- [15:25](https://youtu.be/OToDz3Ghpjo?t=925) Texture memory, Driving Empire pavement (low-end device): **36 MB with streaming vs 24 MB before, with much smoother performance**
- [15:56](https://youtu.be/OToDz3Ghpjo?t=956) Texture memory, Sesame Street: **45 MB with streaming vs 100 MB before**
- [12:08](https://youtu.be/OToDz3Ghpjo?t=728) Memory for a reference scene under old system: **Between 2 and 12 GB with legacy full-resolution loading**
- [19:16](https://youtu.be/OToDz3Ghpjo?t=1156) Mesh simplification chain: **Original ~5,000 triangles reduced down to 120 triangles while keeping silhouette**

## Games
- **Driving Empire** [4:29](https://youtu.be/OToDz3Ghpjo?t=269): Used as the test scene (gas station) and production example; texture streaming let low-end Android run smoother with more detail on pavement.
- **Sesame Street (Roblox experience)** [15:36](https://youtu.be/OToDz3Ghpjo?t=936): Texture streaming gave finer feather and brick detail while cutting texture memory from 100 MB to 45 MB.
- **Beyond the Dark** [21:21](https://youtu.be/OToDz3Ghpjo?t=1281): Roblox-authored place used to measure triangle reductions with mesh LOD system on and off.

## Tools
Roblox Studio, Texture streaming (engine feature), Mesh streaming and Mesh LOD system (workspace property, opt-in), Slim (runtime model baking), Debug views (texture resolution and LOD legends)

## He points to
- Roblox DevForum (bug reports for mesh streaming)

## Quotes
- [14:55](https://youtu.be/OToDz3Ghpjo?t=895) "Memory is fatal... having performance that is a little slower is not as much. I would always pick memory first."
- [24:15](https://youtu.be/OToDz3Ghpjo?t=1455) "If you enable this system your own LODs will have LODs. You don't want that. So disable your user side LODs."

## On screen
Contact sheet shows texture-streaming debug views (color-coded mip legend, memory graph with budget line), a loading-speed comparison, Driving Empire and Sesame Street before/after renders, mesh LOD debug views of a deer model and car, and the Android/Windows/iOS/PS5 time-to-ideal-quality table (Android 22s before, 14s TTIQ, 11.3s TTMQ).

## Topics
[[building-art-and-assets]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
