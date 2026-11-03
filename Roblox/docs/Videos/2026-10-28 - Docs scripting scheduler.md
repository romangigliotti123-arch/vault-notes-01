---
title: "Docs: scripting / scheduler"
url: https://create.roblox.com/docs/scripting/scheduler.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / scheduler

[Open](https://create.roblox.com/docs/scripting/scheduler.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page on scheduling code with Library.task (spawn, defer, delay, wait) versus legacy global wait/spawn/delay. Explains each method's timing behaviour, with examples, and recommends task methods over legacy globals for efficiency.

## Tips
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[luau-language-and-types]]** Use task.wait, task.spawn, task.defer and task.delay instead of legacy wait, spawn and delay; the task versions are optimized and configurable and avoid throttling.
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[luau-language-and-types]]** Use task.spawn when a function may yield and you need it to run immediately; it resumes the thread right away through the engine scheduler.
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[luau-language-and-types]]** Use task.defer when you want the thread to run as soon as possible but not immediately; it runs after the current resume point in the frame.
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[luau-language-and-types]]** Use task.delay(0, f) as an alternative to defer; a zero duration resumes on the next Heartbeat step.
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[optimization-and-streaming]]** Do not rely on task.delay timing precision; measure actual elapsed time by passing os.clock() as an argument (e.g. about 2.04s for a 2s delay).
- [page](https://create.roblox.com/docs/scripting/scheduler) **[[luau-language-and-types]]** task.wait() with no argument is equivalent to RunService.Heartbeat and yields one step; capture its return value to get the actual elapsed time.

## Numbers
- [page](https://create.roblox.com/docs/scripting/scheduler) task.delay(2) actual elapsed time: **about 2.038702s (example output)**
- [page](https://create.roblox.com/docs/scripting/scheduler) task.wait(2) actual elapsed time: **about 2.0792941s (example output)**

## Tools
Library.task, Library.coroutine, RunService.Heartbeat

## He points to
- Roblox docs: Schedule code

## Topics
[[luau-language-and-types]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
