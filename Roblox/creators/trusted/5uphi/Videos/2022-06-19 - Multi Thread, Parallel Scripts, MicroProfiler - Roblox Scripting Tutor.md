---
title: "Multi Thread, Parallel Scripts,  MicroProfiler  - Roblox Scripting Tutorial"
url: https://youtu.be/BbIPalpAfaI
creator: Suphi Kaner
official: false
advice_density: medium
date: 2022-06-19
views: 46461
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Multi Thread, Parallel Scripts,  MicroProfiler  - Roblox Scripting Tutorial

[Watch](https://youtu.be/BbIPalpAfaI) | 5uphi | 46,461 views | 2022-06-19

## Summary
Tutorial on Roblox's MicroProfiler (Ctrl+Alt+F6, Ctrl+P to pause) and parallel Luau scripting. Shows how RunService events run on worker threads via Actors and ConnectParallel, how task.desynchronize/synchronize work, and that threads run in series within one actor. Mostly a technical walkthrough, no monetisation or growth advice.

## Tips
- [0:07](https://youtu.be/BbIPalpAfaI?t=7) **[[scripting-and-performance]]** Open MicroProfiler with Ctrl+Alt+F6 and pause with Ctrl+P to inspect frame timing per thread and per script.
- [3:33](https://youtu.be/BbIPalpAfaI?t=213) **[[scripting-and-performance]]** Use debug.profilebegin/debug.profileend labels to see exactly which chunks of script code cost frame time in MicroProfiler.
- [8:21](https://youtu.be/BbIPalpAfaI?t=501) **[[scripting-and-performance]]** RenderStepped runs on the main thread; Stepped and Heartbeat can run on worker threads when connected with ConnectParallel inside an Actor.
- [10:27](https://youtu.be/BbIPalpAfaI?t=627) **[[optimization-and-streaming]]** If render work is too heavy, Roblox may skip render-step work to keep up; keep per-frame client work small.
- [13:39](https://youtu.be/BbIPalpAfaI?t=819) **[[scripting-and-performance]]** Put scripts that should run in parallel inside separate Actors; scripts in the same Actor still run one after another.
- [14:59](https://youtu.be/BbIPalpAfaI?t=899) **[[scripting-and-performance]]** Use task.desynchronize() for heavy computation on worker threads and task.synchronize() before touching the DataModel or Instances.
- [18:24](https://youtu.be/BbIPalpAfaI?t=1104) **[[luau-language-and-types]]** Do not rely on the observed execution order of parallel scripts; it may change in future Roblox updates.

## Tools
MicroProfiler, RunService, Actor, task.desynchronize, task.synchronize, debug.profilebegin, debug.profileend

## Topics
[[luau-language-and-types]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
