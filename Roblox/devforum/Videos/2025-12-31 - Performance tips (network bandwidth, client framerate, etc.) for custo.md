---
title: "Performance tips (network bandwidth, client framerate, etc.) for custom NPC replication"
url: https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236
creator: Roblox DevForum
official: false
advice_density: high
date: 2025-12-31
views: 70
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Performance tips (network bandwidth, client framerate, etc.) for custom NPC replication

[Open](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) | Roblox DevForum | 70 views | 2025-12-31

## Summary
Downrest's DevForum guide on performance for custom NPC replication in Roblox: why humanoids are bandwidth-expensive, sending data at reduced rates, compressing CFrames with Vector3int16/Vector2int16 and buffers, BulkMoveTo rendering, render throttling, flowfield pathfinding, Actors and networking libraries.

## Tips
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[scripting-and-performance]]** Don't replicate large NPC counts as moving Humanoids; use a custom system where the server sends position data and clients render it, to offload replication cost.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Keep total replication under Roblox's ~50 KB/s throttle; above it, humanoids replicate slowly, laggily or teleport. Budget per-player unit counts accordingly.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[client-server-and-remotes]]** Send NPC position data only ~10 times per second (every 10 Heartbeats) and only for NPCs whose positions changed; tune the rate per game.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[client-server-and-remotes]]** Interpolate NPCs on the client with CFrame:Lerp and scale alpha by deltaTime/(1/60) so movement stays smooth across FPS spikes and above 60 FPS.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Use arrays instead of dictionaries for sent data; string keys add extra bytes per packet with no benefit.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Compress CFrames: send position as Vector3int16 (~6 bytes) instead of CFrame (~20 bytes), or Vector2int16 (X,Z) if the client derives height from a heightmap.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Send only the Y rotation of NPCs and pack it into a 2-byte integer with the buffer library (buffer.writei16) instead of an 8-byte float.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Use workspace:BulkMoveTo with Enum.BulkMoveMode.FireCFrameChanged to move many NPC parts in one batch instead of looping over CFrame sets.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Throttle rendering when NPC counts reach 1000+: render 500 per frame alternating (~50% workload cut) or 250 per frame (~75% cut), accepting slight choppiness, as a last resort.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[scripting-and-performance]]** Use flowfield pathfinding (e.g. FastFlow) for hordes: one calculated field is shared by all NPCs and only recalculated when targets or the environment change.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[luau-language-and-types]]** For Actors-based parallel Luau, use roughly 32-64 Actors, avoid long computations in them, and note the client is currently capped at 3 parallel threads. CFrame setting is not parallel-safe.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[optimization-and-streaming]]** Try @native on server compression code, but verify with the ScriptProfiler since performance gains are not guaranteed.
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) **[[client-server-and-remotes]]** Use a networking library to batch RemoteEvents and cut the ~9-byte per-RemoteEvent overhead, which matters most past 1000+ NPCs.

## Numbers
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Moving humanoids bandwidth (5 / 25 / 75 / 200 / 500 units): **~4 / ~17 / ~40 / ~110 / ~160 KB/s**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Roblox replication throttle threshold: **50 KB/s**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Byte sizes: CFrame / Vector3 / Vector3int16 / number / RemoteEvent overhead: **~20 / ~12 / ~6 / ~8 / ~9 bytes**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Recommended position send rate: **~every 0.1 s (10 Heartbeats), i.e. ~6 sends per second**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Render workload reduction with batching: **50% (500/frame) or 75% (250/frame)**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Recommended Actor count for parallel Luau: **32-64 Actors**
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) Client parallel thread cap: **3 threads**

## Tools
BulkMoveTo, buffer library, Vector3int16/Vector2int16, FastFlow, ScriptProfiler, Actors, @native

## He points to
- @PysephDEV data-type byte-size resource
- @Atrazine heightmap post
- @bob_factory (FastFlow)
- @happya_x 3D flowfield post
- @Content_Corrupted019 networking library post
- Astro Force bandwidth optimization post (60x reduction)

## Quotes
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) "The rule of thumb is you should only send necessary data, when it is necessary."
- [page](https://devforum.roblox.com/t/performance-tips-network-bandwidth-client-framerate-etc-for-custom-npc-replication/4202236) "Pushing as much load away from the server and leaving it up to the clients."

## Topics
[[client-server-and-remotes]] [[luau-language-and-types]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
