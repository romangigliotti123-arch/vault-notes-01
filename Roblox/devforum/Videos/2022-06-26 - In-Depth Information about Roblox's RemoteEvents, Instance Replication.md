---
title: "In-Depth Information about Roblox's RemoteEvents, Instance Replication, and Physics Replication (w/ sources!)"
url: https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-06-26
views: 139
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# In-Depth Information about Roblox's RemoteEvents, Instance Replication, and Physics Replication (w/ sources!)

[Open](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) | Roblox DevForum | 139 views | 2022-06-26

## Summary
Technical deep-dive on Roblox networking: RemoteEvent queueing and reliability, invocation queue drops, physics replication (unreliable, 20Hz, interpolated at 60Hz), instance replication limits, per-type byte costs, and bandwidth targets. Mostly community-sourced and self-described as possibly inaccurate.

## Tips
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[client-server-and-remotes]]** Don't rely on the RemoteEvent invocation queue for events fired before a listener exists; it is small and drops events.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[client-server-and-remotes]]** Don't fire RemoteEvents too rapidly; Roblox throttles networking when too many remote events are fired too fast.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[client-server-and-remotes]]** Keep remote payloads small; a blank remote call costs ~9 bytes and tables add only 2 bytes with no index overhead.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Don't replicate whole instances from the server; send a position or identifier and clone visual parts on the client.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Avoid setting CFrame on many parts at once; CFrame assignment is expensive.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Minimise humanoid count; humanoids are expensive to replicate and use.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Keep purely visual moving parts client-side; replicated physics data for them wastes bandwidth and inherits ping jitter.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Aim for client receive below ~100 kbps and client send below ~20 kbps, adjusted to your player cap and game type.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[client-server-and-remotes]]** Only the latest property value per frame replicates; intermediate changes within one frame are lost.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[client-server-and-remotes]]** Property replication does not follow network ownership; only physics positional data does.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Reduce reliable traffic volume: a lost packet halts all network traffic until resent, causing ping spikes.
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) **[[optimization-and-streaming]]** Frame rate affects measured ping: below 60fps raises reported ping, since networking is processed per frame.

## Numbers
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) Physics replication rate: **20 Hz (interpolated at 60 Hz)** (Physics is unreliable and unordered)
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) Blank remote call overhead: **~9 bytes** (Community estimate, possibly inaccurate)
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) Byte cost per type: **string length+2; boolean 2; number 9; table 2; EnumItem 4; Instance 4; Vector3 13; CFrame 14 axis-aligned, 20 rotated** (Rough community estimates)
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) Client receive bandwidth target: **<100 kbps** (Author's personal target; depends on game and player cap)
- [page](https://devforum.roblox.com/t/in-depth-information-about-robloxs-remoteevents-instance-replication-and-physics-replication-w-sources/1847340) Client send bandwidth target: **<20 kbps** (Author's personal target; depends on game and player cap)

## Tools
Shift F3 (networking data), Shift F3 + Shift 1 (ping without processing delay), Microprofiler, RakNet

## He points to
- RakNet (raknet.com)
- Tomarty's ORE (One Remote Event) DevForum post

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
