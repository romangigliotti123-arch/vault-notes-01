---
title: "Network Optimization (2021) - Preventing High Latency & Reducing Lag"
url: https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-02-14
views: 227
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Network Optimization (2021) - Preventing High Latency & Reducing Lag

[Open](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) | Roblox DevForum | 227 views | 2021-02-14

## Summary
Hexcede's rebooted (2021) DevForum guide on Roblox network optimization. Covers the ~50 kB/s per-player data limit, unit confusion (kb vs kB), how overload queues cause huge effective ping, and reducing remote/property traffic via batching, unparenting, and client-side visuals. Also covers the parenting trick for terrain and voxel generation.

## Tips
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[client-server-and-remotes]]** Keep data throughput well below Roblox's ~50 kB/s per-player limit. Give yourself a hard goal of about 25 kB/s, reserving half for replication.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[client-server-and-remotes]]** Sustained overload queues data, so measured ping can exceed 100k ms and effective replication latency can reach tens of minutes. Going over the limit for more than a few seconds is harmful.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[optimization-and-streaming]]** Batch remote traffic into fewer, larger requests. Processing one big packet costs far less CPU, memory and network overhead than many small ones.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[optimization-and-streaming]]** Before changing many instances or properties, unparent the target (e.g. a folder), make the changes, then reparent. This collapses many updates into a few ancestry changes.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[scripting-and-performance]]** Don't loop over and destroy many instances individually. Destroy the whole container folder and create a new empty one.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[client-server-and-remotes]]** Avoid server-driven cosmetic updates like spinning or recoloring. Keep them on the client, or send the server's state only occasionally in batches.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[building-and-level-design]]** When generating many voxels or terrain parts, parent them to nil or a folder parented to nil first, then parent to Workspace once done. The author reports up to ~100x speedup.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[optimization-and-streaming]]** Coalesce work into larger chunks, but not so large that it causes stutter. A stable frame rate beats a higher average with periodic 1 FPS spikes.
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) **[[common-mistakes]]** Network efficiency is hard to retrofit. Designing entity and remote systems with it in mind from the start avoids large rewrites later, similar to security.

## Numbers
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Per-player data transfer soft limit: **50 kB/s (1024*50 bytes/s), covering all throughput, not just remotes** (Roblox per-client limit; exceeding it slows or halts replication)
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Recommended self-imposed limit: **25 kB/s** (Author's suggested hard limit, reserving half the throughput for Roblox replication)
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Remote transmission rate: **up to 60 tps, mass requests coalesced** (Remote requests are batched into large requests roughly every second)
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Measured ping under sustained overload: **over 100k ms after a few minutes** (Effective replication ping can reach 10-30 minutes)
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Voxel parenting speedup: **close to 100x** (Parenting a folder to Workspace after terrain generation vs parenting each part immediately)
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) Unit error: **50 kb/s (kilobits) was listed; the real limit is 50 kB/s, 8x larger** (Kilobit vs kilobyte confusion in earlier article and DevHub)

## Tools
Roblox network debugger (network tab)

## He points to
- Hexcede's original 'Network Optimization - Preventing High Latency & Reducing Lag' DevForum article

## Quotes
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) "Sending too close to this limit is a no no, since this limit encompasses all data throughput, not just remotes."
- [page](https://devforum.roblox.com/t/network-optimization-2021-preventing-high-latency-reducing-lag/1046078) "You can always expect to see better, or at least equal performance by coalescing things together into bigger chunks. You'll never see worse overall performance."

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
