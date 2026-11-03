---
title: "Docs: performance-optimization / microprofiler"
url: https://create.roblox.com/docs/performance-optimization/microprofiler.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / microprofiler

[Open](https://create.roblox.com/docs/performance-optimization/microprofiler.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the MicroProfiler: reading frame time, colour-coded bar meanings (orange/blue/red), timeline navigation, threads, custom profilebegin/profileend labels, Assistant analysis, dumps, server profiling, and web/desktop-only features.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[scripting-and-performance]]** Profile on a mobile device via the MicroProfiler web UI; if a game runs well on a midrange Android tablet it will perform much better on a gaming desktop.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Aim for consistent frame times, not just high FPS; one 410 ms frame among 59 frames in 10 ms causes a jarring stutter even at 60 FPS.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Don't rely on desktop profiling with a 60 FPS cap; a 4 ms vs 16 ms frame looks identical, but on mobile a 133 ms frame is easy to notice.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Use orange bars (Jobs Wall Time > Render Wall Time) to investigate scripts, physics and animations when frame goals are missed.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Use blue bars (Render Wall Time > Jobs Wall Time) to diagnose rendering bottlenecks: object density, object movement and lighting.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Red bars (render-bound with GPU Wait Time > 2.5 ms) usually come from object complexity, texture size and visual effects.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Focus on frame time rather than bar colour; colour mixes are fine if frame time goals are met, and colour only guides optimisation when goals are missed.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[scripting-and-performance]]** Wrap expensive script sections in debug.profilebegin/debug.profileend to create named timeline labels and measure their cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** When drilling into a parent task, troubleshoot its worst-performing child tasks; a parent can never be shorter than the sum of its children.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Use flame graphs (Export menu in web UI) to find frequently-run tasks that are individually cheap but add up to significant time.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[testing-debugging-and-qa]]** Compare before and after updates by dropping a second dump into the web UI and using Combine & Compare to generate a diff flame graph.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[ai-and-tools]]** Pause a spike in Studio and ask Assistant to analyse the capture; it can report bottlenecks and propose fixes, and works via the Studio MCP server.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) **[[optimization-and-streaming]]** Dumps only contain the selected frames, not the full session; use counters mode if you need data from startup to the dump time.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) frame time: **16.67 ms = 60 FPS; 33.33 ms = 30 FPS; 8.33 ms = 120 FPS; 4.17 ms = 240 FPS** (Frame time to FPS conversion table from docs)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) GPU Wait Time threshold for red bars: **> 2.5 ms** (Red bar condition alongside Render Wall Time exceeding Jobs Wall Time)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) default mobile web UI frames: **30 recent frames (add /90 to URL for more)** (MicroProfiler web UI on mobile device at IP:1338)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler) server capture limits: **max 60 frames, max 4 s delay** (Developer Console server MicroProfiler recording)

## Tools
MicroProfiler, Roblox Studio, Developer Console, Assistant, Studio MCP server, Flame graphs

## He points to
- Roblox Creator Docs: MicroProfiler Tag reference
- Roblox Creator Docs: Improve performance

## Topics
[[ai-and-tools]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
