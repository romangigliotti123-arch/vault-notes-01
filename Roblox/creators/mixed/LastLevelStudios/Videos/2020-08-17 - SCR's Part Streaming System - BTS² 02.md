---
title: "SCR's Part Streaming System - BTS² #02"
url: https://youtu.be/0RRGneqSZRY
creator: Last Level Studios
official: false
advice_density: high
date: 2020-08-17
views: 15022
transcript: auto-captions
confidence: high
tags: [roblox, lastlevelstudios, youtube-learn]
creator_trust: MIXED
creator_score: 5.5
---

> [!note] Trust: MIXED (credibility audit score 5.5): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# SCR's Part Streaming System - BTS² #02

[Watch](https://youtu.be/0RRGneqSZRY) | LastLevelStudios | 15,022 views | 2020-08-17

## Summary
Developer walkthrough of Stanford County Railway's v1.6 part streaming rewrite. Covers 1024-stud chunks, flagging vs. re-parenting split, priority-based chunk ordering, FPS-driven auto-throttling, and server/client module architecture. Deeply technical; aimed at developers building large maps.

## Tips
- [3:48](https://youtu.be/0RRGneqSZRY?t=228) **[[building-and-level-design]]** Split the map into fixed-size chunks (SCR uses 1024 studs) and key each by x/y/z index; avoid making chunks 2048 since that forces three loaded chunks per direction.
- [5:51](https://youtu.be/0RRGneqSZRY?t=351) **[[optimization-and-streaming]]** Move out-of-range parts into a storage folder instead of destroying and recreating them; Lua-side destroy/create is too costly, so reparenting is the cheaper option.
- [7:24](https://youtu.be/0RRGneqSZRY?t=444) **[[optimization-and-streaming]]** Separate flagging chunks needing state change from the actual reparenting, then process a priority queue ordered by distance to the player's focus.
- [8:05](https://youtu.be/0RRGneqSZRY?t=485) **[[optimization-and-streaming]]** Load in the chunk ahead of the player before unloading chunks behind, so the player never arrives in empty space.
- [10:41](https://youtu.be/0RRGneqSZRY?t=641) **[[optimization-and-streaming]]** Auto-throttle streaming by measured frame time rather than a part-count limit, since parts have very different render costs.
- [11:22](https://youtu.be/0RRGneqSZRY?t=682) **[[optimization-and-streaming]]** When frames drop, skip the streaming step for that frame instead of letting overrun time compound into the next frame.
- [26:27](https://youtu.be/0RRGneqSZRY?t=1587) **[[optimization-and-streaming]]** Pause streaming only after repeated critical frame drops (below ~5 FPS); single blips shouldn't trigger it, and abrupt toggling causes oscillating lag spikes.
- [21:38](https://youtu.be/0RRGneqSZRY?t=1298) **[[scripting-and-performance]]** When initially processing hundreds of thousands of parts, yield periodically using a time budget rather than after every part, or the load takes unacceptably long.
- [39:23](https://youtu.be/0RRGneqSZRY?t=2363) **[[optimization-and-streaming]]** Enforce a minimum reparent count per cycle (SCR uses 50) so low-end devices still make progress through the queue.
- [41:25](https://youtu.be/0RRGneqSZRY?t=2485) **[[client-server-and-remotes]]** Let the server do the heavy one-time work of indexing and moving parts into storage, and have clients fetch chunk data via a RemoteFunction to avoid freezing low-end clients.
- [49:41](https://youtu.be/0RRGneqSZRY?t=2981) **[[optimization-and-streaming]]** Weight priority chunks by halving their distance magnitude when sorting, so nearby regular chunks can still outrank distant priority chunks.
- [54:17](https://youtu.be/0RRGneqSZRY?t=3257) **[[optimization-and-streaming]]** Keep the draw-distance setting near default; pushing it to max can cause throttling and a negative cycle of chunks not loading when needed.
- [56:20](https://youtu.be/0RRGneqSZRY?t=3380) **[[optimization-and-streaming]]** When training, focus streaming on the front of the vehicle so rails and scenery load ahead of travel, and unload from the rear.
- [1:08:32](https://youtu.be/0RRGneqSZRY?t=4112) **[[building-and-level-design]]** Split very long parts to match chunk size for backward compatibility, but note that automatically splitting unions is tricky.
- [1:10:35](https://youtu.be/0RRGneqSZRY?t=4235) **[[optimization-and-streaming]]** Exempt critical parts like terrain, spawns, and sensors from streaming so they always exist, and keep base plates as priority loads.
- [30:30](https://youtu.be/0RRGneqSZRY?t=1830) **[[optimization-and-streaming]]** Expose a throttle slider in settings so players on different hardware can tune streaming aggressiveness; SCR's testers saw FPS roughly double after the rewrite.

## Numbers
- [2:27](https://youtu.be/0RRGneqSZRY?t=147) Chunk size: **1024x1024 studs** (SCR streaming grid cell size)
- [2:27](https://youtu.be/0RRGneqSZRY?t=147) Chunk count: **over 2200** (Stanford County Railway map chunks)
- [12:45](https://youtu.be/0RRGneqSZRY?t=765) FPS improvement: **roughly doubled for the developer and nearly all testers** (After auto-throttled streaming rewrite)
- [12:45](https://youtu.be/0RRGneqSZRY?t=765) Low-end FPS example: **11 to 20 FPS** (Improvement reported for low-end tester)
- [21:38](https://youtu.be/0RRGneqSZRY?t=1298) Part count: **about 170000 parts** (SCR map parts processed at server start)
- [39:23](https://youtu.be/0RRGneqSZRY?t=2363) Minimum reparents per cycle: **50** (Floor on parts reparented each streaming cycle)
- [26:27](https://youtu.be/0RRGneqSZRY?t=1587) Critical frame threshold: **delta above 0.2s (about 5 FPS)** (Pauses streaming after repeated hits)
- [27:08](https://youtu.be/0RRGneqSZRY?t=1628) Severe frame threshold: **delta above 0.1s (about 10 FPS)** (Triggers heavy throttling)
- [30:30](https://youtu.be/0RRGneqSZRY?t=1830) Streaming time budget: **about 1/120 s per frame** (Roughly half a 60 FPS frame)

## Games
- **Stanford County Railway** [0:01](https://youtu.be/0RRGneqSZRY?t=1): Large train map using chunked part streaming with priority queue, FPS-based auto-throttle, and parts moved to storage rather than destroyed.

## Tools
RunService Heartbeat, table.sort, RemoteFunction, Roblox built-in streaming (referenced)

## He points to
- Roblox built-in streaming system (future migration goal)

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[LastLevelStudios - How to make successful Roblox games]]
