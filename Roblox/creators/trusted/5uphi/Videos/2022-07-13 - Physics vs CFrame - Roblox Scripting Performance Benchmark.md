---
title: "Physics vs CFrame - Roblox Scripting Performance Benchmark"
url: https://youtu.be/thfUspopuGE
creator: Suphi Kaner
official: false
advice_density: medium
date: 2022-07-13
views: 19743
transcript: auto-captions
confidence: medium
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Physics vs CFrame - Roblox Scripting Performance Benchmark

[Watch](https://youtu.be/thfUspopuGE) | 5uphi | 19,743 views | 2022-07-13

## Summary
Benchmark video claiming Roblox physics-driven parts outperform CFrame-manually-updated parts. Shows micro-profiler frame times (~4ms vs ~8ms at 1000 parts), can-touch/can-collide behaviour differences, and network data costs (CFrame sends far more data; Roblox throttles distant updates). Technical, low on business advice.

## Tips
- [0:41](https://youtu.be/thfUspopuGE?t=41) **[[scripting-and-performance]]** Prefer physics-driven movement (AssemblyLinearVelocity/anchored parts) over manually setting CFrame each Heartbeat; benchmark showed ~50% lower script cost at 1,000–2,000 parts.
- [6:19](https://youtu.be/thfUspopuGE?t=379) **[[scripting-and-performance]]** Don't rely on Touched or query events for CFrame-moved parts; they did not fire when CFrame was set manually, while physics-moved parts triggered them.
- [7:00](https://youtu.be/thfUspopuGE?t=420) **[[scripting-and-performance]]** CFrame-moved parts do not collide with other parts; physics parts do. Choose physics if collisions matter.
- [10:04](https://youtu.be/thfUspopuGE?t=604) **[[scripting-and-performance]]** Manual CFrame updates on the server replicate far more data (~271 KB/s vs ~40 KB/s for 100 parts in the test); physics replication is throttled by distance and saves bandwidth.
- [11:26](https://youtu.be/thfUspopuGE?t=686) **[[scripting-and-performance]]** Roblox's physics replication reduces update rate for parts far from the camera, scaling much better than CFrame updates when part counts grow.
- [10:45](https://youtu.be/thfUspopuGE?t=645) **[[optimization-and-streaming]]** Benchmark network stats with Studio's Network view, but remember Studio runs server locally so bandwidth numbers must be multiplied by player count for estimates.

## Numbers
- [0:41](https://youtu.be/thfUspopuGE?t=41) Script cost, CFrame vs physics: **~8 ms vs ~4 ms (about 50% faster physics), 1,000 parts** (Heartbeat CFrame loop vs physics step, benchmark in Studio)
- [4:11](https://youtu.be/thfUspopuGE?t=251) Frame budget: **At 3,000 parts per side, CFrame movement could not finish in one frame** (Author's own machine)
- [9:23](https://youtu.be/thfUspopuGE?t=563) Incoming server-to-client data, 100 parts: **Physics ~40 KB/s vs CFrame ~271 KB/s** (Network stats, single client)
- [11:26](https://youtu.be/thfUspopuGE?t=686) Incoming data at 200 parts: **Physics ~50 KB/s vs CFrame ~542 KB/s** (Physics only rose ~10 KB/s when doubling parts)
- [10:04](https://youtu.be/thfUspopuGE?t=604) Outgoing client-to-server, CFrame 100 parts: **66 KB/s (physics ~1 KB/s)** (Single client)
- [13:36](https://youtu.be/thfUspopuGE?t=816) 720p YouTube recommended bitrate: **5 Mbps ≈ 625 KB/s** (Author compares to 200-part CFrame data rate)

## Tools
Roblox Studio Micro Profiler, Roblox Studio Network stats viewer, RunService.Heartbeat

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
