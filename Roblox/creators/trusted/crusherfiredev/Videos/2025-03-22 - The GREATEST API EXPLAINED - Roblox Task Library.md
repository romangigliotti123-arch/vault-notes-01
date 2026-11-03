---
title: "The GREATEST API EXPLAINED - Roblox Task Library"
url: https://youtu.be/0jAZOpNHqv8
creator: Crusherfire
official: false
advice_density: medium
date: 2025-03-22
views: 12602
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# The GREATEST API EXPLAINED - Roblox Task Library

[Watch](https://youtu.be/0jAZOpNHqv8) | crusherfiredev | 12,602 views | 2025-03-22

## Summary
Explains Roblox's task library (spawn, defer, delay, wait, cancel) and how the task scheduler runs code at invocation points each frame. Demonstrates execution order with micro profiler tests, and notes Run service events and deprecated RenderStepped/Stepped.

## Tips
- [2:41](https://youtu.be/0jAZOpNHqv8?t=161) **[[scripting-and-performance]]** Use task.spawn to run a function immediately in a new thread so yielding calls (e.g. PlayerService async web requests) don't halt your main script.
- [12:38](https://youtu.be/0jAZOpNHqv8?t=758) **[[scripting-and-performance]]** Prefer task.defer over task.spawn when the work doesn't need to run immediately; it queues to the end of the current resumption cycle for predictable ordering.
- [17:49](https://youtu.be/0jAZOpNHqv8?t=1069) **[[scripting-and-performance]]** task.delay(0) inside Run service RenderStepped-style events runs at the next Heartbeat, which may be in the same frame; inside Heartbeat it runs next frame.
- [24:08](https://youtu.be/0jAZOpNHqv8?t=1448) **[[scripting-and-performance]]** task.wait() with no argument behaves like task.delay(0): it resumes on the next Heartbeat, so use it as a yield, not as a precise timer.
- [25:01](https://youtu.be/0jAZOpNHqv8?t=1501) **[[scripting-and-performance]]** Store the thread returned by task.defer/delay and call task.cancel on it when the work is no longer needed to prevent it running.
- [27:36](https://youtu.be/0jAZOpNHqv8?t=1656) **[[roblox-platform-changes]]** RenderStepped and Stepped events are deprecated; migrate to PreRender and PreSimulation in the Run service.

## Numbers
- [16:26](https://youtu.be/0jAZOpNHqv8?t=986) task.delay accuracy: **1 second delay measured ~1.12 s via os.clock** (Test of task.delay(1) timing in Studio)
- [20:34](https://youtu.be/0jAZOpNHqv8?t=1234) task.delay(0) resume point: **next Heartbeat, frame 94 in same frame as RenderStepped** (Micro profiler test result)

## Tools
Roblox Studio, Micro Profiler (ctrl+F6), debug.profilebegin/profileend, os.clock, Run service

## He points to
- Roblox task scheduler documentation
- Roblox Run service documentation
- Roblox Parallel Luau (creator's prior video)

## Topics
[[roblox-platform-changes]] [[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
