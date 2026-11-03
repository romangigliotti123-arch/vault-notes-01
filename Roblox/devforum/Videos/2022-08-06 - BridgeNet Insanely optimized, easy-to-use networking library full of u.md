---
title: "BridgeNet | Insanely optimized, easy-to-use networking library full of utilities, now with roblox-ts! | v1.9.9-beta"
url: https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-08-06
views: 777
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# BridgeNet | Insanely optimized, easy-to-use networking library full of utilities, now with roblox-ts! | v1.9.9-beta

[Open](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) | Roblox DevForum | 777 views | 2022-08-06

## Summary
BridgeNet / BridgeNet2 documentation and DevForum post for a Roblox networking library focused on performance. Claims header savings, fewer packets, faster client processing, utilities like FireAllInRange, and a reliability-types feature request for unreliable remotes.

## Tips
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) **[[scripting-and-performance]]** Batch multiple remote calls into one remote call per frame; BridgeNet reports this avoids ordering stalls caused by many individual RemoteEvents.
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) **[[client-server-and-remotes]]** Reduce RemoteEvent packet count per player; BridgeNet2 claims removing 7 bytes of header per call prevents hitting the RemoteEvent throttle limit.
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) **[[scripting-and-performance]]** Compress data before sending using dictionary-to-table conversion and compressed ID strings instead of sending verbose keys each call.
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) **[[client-server-and-remotes]]** Estimate bandwidth as players times per-player KB/s; e.g. 50 players at 100 KB/s is 5 MB/s outbound from the server.
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) **[[optimization-and-streaming]]** Use reliability-aware transport for frequently updated state (e.g. head rotation); Roblox remotes are reliable and ordered, which wastes bandwidth on stale data.

## Numbers
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) Header bytes removed per RemoteEvent call: **7 bytes (BridgeNet2)**
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) Client packet processing time reduction: **approximately 75-80% (BridgeNet2)**
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) Benchmark bandwidth, 200 blank remote calls per frame: **BridgeNet 63 KB/s average vs Roblox 110 KB/s average**
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) Example server outbound load: **50 players x 100 KB/s = 5000 KB/s (about 5 MB/s)**
- [page](https://devforum.roblox.com/t/bridgenet-insanely-optimized-easy-to-use-networking-library-full-of-utilities-now-with-roblox-ts-v199-beta/1909935) Megabyte to megabit conversion: **1 MB = 8 Mb; 5 MB/s needs roughly 40 Mb/s upload**

## Tools
BridgeNet, BridgeNet2, roblox-ts, @rbxts/bridgenet (npm), Chickynoid

## He points to
- https://github.com/ffrostfall/BridgeNet
- https://www.npmjs.com/package/@rbxts/bridgenet
- Roblox DevForum reliability types feature request for RemoteEvents

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
