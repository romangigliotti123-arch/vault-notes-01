---
title: "Content Streaming - Roblox Scripting Tutorial"
url: https://youtu.be/d8pqcfxqmek
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-03-29
views: 27079
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Content Streaming - Roblox Scripting Tutorial

[Watch](https://youtu.be/d8pqcfxqmek) | 5uphi | 27,079 views | 2023-03-29

## Summary
Technical tutorial on Roblox StreamingEnabled: how the server replicates only nearby instances to clients. Covers StreamingIntegrityMode (disabled, minimum radius, pause outside loaded area), replication focus, StreamOutBehavior (low memory vs opportunistic), ModelStreamingMode (non-atomic, atomic, persistent, persistent per player), and LevelOfDetail imposter meshes.

## Tips
- [1:47](https://youtu.be/d8pqcfxqmek?t=107) **[[optimization-and-streaming]]** Enable StreamingEnabled on Workspace and lower StreamingTargetRadius (e.g. 128 studs) to cut client memory and network use for large worlds.
- [4:01](https://youtu.be/d8pqcfxqmek?t=241) **[[optimization-and-streaming]]** Keep StreamingMinRadius well below StreamingTargetRadius; equal values cause constant pausing while instances stream in.
- [8:31](https://youtu.be/d8pqcfxqmek?t=511) **[[optimization-and-streaming]]** Prefer PauseOutsideLoadedArea over MinRadius integrity mode to avoid frequent client pauses from large minimum radii.
- [12:49](https://youtu.be/d8pqcfxqmek?t=769) **[[optimization-and-streaming]]** Use LowMemory stream-out for large static worlds; use Opportunistic for worlds with many server-moved instances to save memory.
- [15:39](https://youtu.be/d8pqcfxqmek?t=939) **[[optimization-and-streaming]]** Do not hand-roll streaming by moving folders in and out of Workspace; it is not equivalent to Roblox streaming and still sends network data.
- [17:29](https://youtu.be/d8pqcfxqmek?t=1049) **[[optimization-and-streaming]]** Group related instances into a Model and use Atomic stream mode when children should load and unload together, cutting network updates for distant models.
- [19:31](https://youtu.be/d8pqcfxqmek?t=1171) **[[optimization-and-streaming]]** Use NonAtomic model streaming when attributes or model-level properties must stay available to all clients while children stream.
- [28:02](https://youtu.be/d8pqcfxqmek?t=1682) **[[optimization-and-streaming]]** Imposter meshes for LevelOfDetail are precomputed in Studio and stored in the place file; they cannot be generated at runtime.
- [28:44](https://youtu.be/d8pqcfxqmek?t=1724) **[[optimization-and-streaming]]** Moving a model that is streamed out with an imposter still costs network data because the imposter position must update.

## Numbers
- [0:22](https://youtu.be/d8pqcfxqmek?t=22) Part spacing in test world: **64 studs** (Anchored parts spaced 64 studs apart in demo folder)
- [1:05](https://youtu.be/d8pqcfxqmek?t=65) Incoming network KB/s, replicated moving parts without streaming: **0.15 to 1.5 KB/s** (Moving many parts without streaming raises incoming data)
- [14:15](https://youtu.be/d8pqcfxqmek?t=855) Opportunistic stream-out distance formula: **TargetRadius + TargetRadius/2 + 64 studs** (Target 128 gives 256 studs; target 512 gives 832 studs)
- [5:45](https://youtu.be/d8pqcfxqmek?t=345) Example radii used for MinRadius integrity test: **256 studs** (Min and target radius set to 256 for pause test)

## Tools
Roblox Studio, Command Bar

## Topics
[[optimization-and-streaming]]

Back to [[5uphi - How to make successful Roblox games]]
