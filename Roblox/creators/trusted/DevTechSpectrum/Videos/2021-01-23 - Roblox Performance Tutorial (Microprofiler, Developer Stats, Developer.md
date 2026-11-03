---
title: "Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer Console)"
url: https://youtu.be/-PPg4N5sKXE
creator: TechSpectrum
official: false
advice_density: medium
date: 2021-01-23
views: 7769
transcript: auto-captions
confidence: high
tags: [roblox, devtechspectrum, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer Console)

[Watch](https://youtu.be/-PPg4N5sKXE) | DevTechSpectrum | 7,769 views | 2021-01-23

## Summary
Tutorial on Roblox's built-in performance tools: setting graphics to manual level 10 for stress tests, reading memory, CPU/GPU frame time, network sent/received/ping in Developer Stats, using the Microprofiler (pausing, dumping frames, mobile access via IP), and reading the Developer Console memory and network tabs. Warns Studio emulation is not accurate for performance.

## Tips
- [0:01](https://youtu.be/-PPg4N5sKXE?t=1) **[[analytics-metrics]]** Set every test device to manual graphics level 10 so Roblox doesn't auto-disable lighting effects; this keeps stress tests comparable.
- [1:08](https://youtu.be/-PPg4N5sKXE?t=68) **[[optimization-and-streaming]]** Target 400-500 MB memory for a full game; under 400 is a very small game; avoid approaching 1000 MB.
- [2:32](https://youtu.be/-PPg4N5sKXE?t=152) **[[optimization-and-streaming]]** Memory grows from textures, meshes, loops that don't free memory, and undisconnected connections; disconnect events to prevent slow buildup.
- [3:16](https://youtu.be/-PPg4N5sKXE?t=196) **[[optimization-and-streaming]]** Aim for CPU frame time of about 15-20 ms at best; investigate code and physics when it goes above that.
- [3:57](https://youtu.be/-PPg4N5sKXE?t=237) **[[optimization-and-streaming]]** Aim for GPU frame time around 13-20 ms on phone; GPU covers lighting, effects, textures and the whole map.
- [5:37](https://youtu.be/-PPg4N5sKXE?t=337) **[[optimization-and-streaming]]** Keep network sent well under 50 KB/s and optimise received traffic when it reaches 70; received rises when the server broadcasts events like gunfire to all clients.
- [6:31](https://youtu.be/-PPg4N5sKXE?t=391) **[[scripting-and-performance]]** Use the Microprofiler (Ctrl+F6 style toggle in Developer Stats) and pause at the biggest spike; dump 32-64 frames to inspect later.
- [6:31](https://youtu.be/-PPg4N5sKXE?t=391) **[[testing-debugging-and-qa]]** To profile on mobile, enable Microprofiler on the device, then open the shown IP in a browser on the same Wi-Fi (not mobile data).
- [9:28](https://youtu.be/-PPg4N5sKXE?t=568) **[[scripting-and-performance]]** A large RayCast bar in the Microprofiler suggests too many raycasts; reduce how often or how many you cast.
- [11:27](https://youtu.be/-PPg4N5sKXE?t=687) **[[optimization-and-streaming]]** Look for high draw calls or too many shadows in the Microprofiler when a bar is too large; disabling shadows can shrink it.
- [13:24](https://youtu.be/-PPg4N5sKXE?t=804) **[[optimization-and-streaming]]** In Developer Console, read Place memory rather than Core memory; check graphics texture and character memory, which grows with player count.
- [14:45](https://youtu.be/-PPg4N5sKXE?t=885) **[[optimization-and-streaming]]** If texture memory is large, compress and shrink textures; many textures at compressed size is a red flag.
- [15:26](https://youtu.be/-PPg4N5sKXE?t=926) **[[scripting-and-performance]]** Check the Network tab for frequent service calls (FriendService, MarketplaceService, GamePassService) and reduce them on the server.
- [16:39](https://youtu.be/-PPg4N5sKXE?t=999) **[[testing-debugging-and-qa]]** Do not trust Studio emulation for performance; test on real devices because emulation doesn't match actual GPU/CPU limits.

## Numbers
- [1:08](https://youtu.be/-PPg4N5sKXE?t=68) Memory target: **400-500 MB for full game; avoid ~1000 MB** (Developer Stats memory guideline for full games)
- [1:51](https://youtu.be/-PPg4N5sKXE?t=111) Phone memory: **800-900 MB on 2GB phone; 400-500 MB on 4GB phone** (Typical memory usage by device RAM)
- [3:16](https://youtu.be/-PPg4N5sKXE?t=196) CPU frame time: **15-20 ms target; 33 ms threshold to avoid** (Developer Stats CPU)
- [3:57](https://youtu.be/-PPg4N5sKXE?t=237) GPU frame time: **13-20 ms on phone (up to 23); 33 ms threshold** (Developer Stats GPU)
- [5:37](https://youtu.be/-PPg4N5sKXE?t=337) Network sent: **Stay well below 50 (KB/s)** (Roblox recommends up to 50; speaker aims lower)
- [5:37](https://youtu.be/-PPg4N5sKXE?t=337) Network received: **70 observed, considered high** (Speaker's test game, needs optimisation)

## Tools
Developer Stats (performance stats window), Microprofiler, Developer Console, Roblox Studio emulator

## He points to
- Roblox task scheduler documentation page (referenced guide)

## Topics
[[analytics-metrics]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[DevTechSpectrum - How to make successful Roblox games]]
