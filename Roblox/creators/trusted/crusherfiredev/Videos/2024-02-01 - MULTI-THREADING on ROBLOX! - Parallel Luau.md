---
title: "MULTI-THREADING on ROBLOX?! - Parallel Luau"
url: https://youtu.be/MyM3JkHEPmA
creator: Crusherfire
official: false
advice_density: high
date: 2024-02-01
views: 39520
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# MULTI-THREADING on ROBLOX?! - Parallel Luau

[Watch](https://youtu.be/MyM3JkHEPmA) | crusherfiredev | 39,520 views | 2024-02-01

## Summary
Explains Roblox Parallel Luau: serial vs parallel execution, reading the Micro Profiler, debug.profilebegin/end labels, deferred signals, Actors with ConnectParallel, task.synchronize for unsafe API calls, and Actor-to-Actor messaging. Demonstrates frame time gains (50ms to 16ms with 72 AI deer).

## Tips
- [0:00](https://youtu.be/MyM3JkHEPmA?t=0) **[[scripting-and-performance]]** Use Parallel Luau only for heavy, frame-time-eating work (AI pathfinding, raycasting, terrain generation); skip it if your game already runs fine serially.
- [1:23](https://youtu.be/MyM3JkHEPmA?t=83) **[[optimization-and-streaming]]** Profile with Ctrl+Alt+F6 (Micro Profiler) in Studio, pause with Ctrl+P, and inspect which threads and labels consume frame time before optimizing.
- [9:00](https://youtu.be/MyM3JkHEPmA?t=540) **[[testing-debugging-and-qa]]** Wrap suspect code in debug.profilebegin(label) / debug.profileend() so it shows as a named block in the Micro Profiler.
- [11:10](https://youtu.be/MyM3JkHEPmA?t=670) **[[scripting-and-performance]]** Heartbeat/RenderStepped connections run serially on one worker thread; many scripts connected to them stack up and inflate frame time.
- [16:46](https://youtu.be/MyM3JkHEPmA?t=1006) **[[scripting-and-performance]]** Put scripts that should run in parallel under an Actor instance; scripts in the same Actor still share one thread, so split workloads across multiple Actors.
- [17:21](https://youtu.be/MyM3JkHEPmA?t=1041) **[[scripting-and-performance]]** Replace :Connect with :ConnectParallel on the signal to run the callback in parallel immediately upon firing.
- [22:47](https://youtu.be/MyM3JkHEPmA?t=1367) **[[scripting-and-performance]]** Check each API member's thread-safety level in the docs; most instance properties are read-only in parallel, so wrap writes like CFrame or MoveTo in task.synchronize().
- [24:51](https://youtu.be/MyM3JkHEPmA?t=1491) **[[scripting-and-performance]]** Converting 72 AI deer from serial to parallel Luau (with task.synchronize for writes) dropped average frame time from about 50ms to about 16ms.
- [28:03](https://youtu.be/MyM3JkHEPmA?t=1683) **[[client-server-and-remotes]]** Use Actor:SendMessage and Actor:BindToMessage to pass data between Actors; bind listeners before sending or early messages are lost.
- [31:28](https://youtu.be/MyM3JkHEPmA?t=1888) **[[scripting-and-performance]]** BindableEvent:Fire is read-and-write safe, so it can be called from parallel code to communicate between threads without errors.

## Numbers
- [14:03](https://youtu.be/MyM3JkHEPmA?t=843) Average frame time with four 1M-iteration serial loops: **67 ms**
- [19:23](https://youtu.be/MyM3JkHEPmA?t=1163) Frame time after splitting scripts into two Actors: **30-40 ms (from 60-70 ms)**
- [26:54](https://youtu.be/MyM3JkHEPmA?t=1614) Frame time of 72 serial AI deer vs 72 parallel deer: **~50 ms serial vs ~16 ms parallel**
- [5:43](https://youtu.be/MyM3JkHEPmA?t=343) Cost of 100,000-iteration loop per frame in RenderStepped: **~6 ms**

## Tools
Micro Profiler (Ctrl+Alt+F6), debug.profilebegin / debug.profileend, Actor instance, task.synchronize / task.desynchronize, Signal:ConnectParallel, Actor:SendMessage / Actor:BindToMessage, BindableEvent

## He points to
- Roblox Parallel Luau documentation
- Roblox API thread safety table

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
