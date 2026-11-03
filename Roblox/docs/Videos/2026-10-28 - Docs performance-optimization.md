---
title: "Docs: performance-optimization"
url: https://create.roblox.com/docs/performance-optimization.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization

[Open](https://create.roblox.com/docs/performance-optimization.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on performance optimization: design for performance while building, then a cycle of identifying issues, improving, and monitoring. Defines frame rate (60 FPS target, 16.67 ms per frame), server heartbeat, memory usage, and join time, and explains why each affects retention, reach and revenue.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization) **[[development-process-and-speed]]** Follow performance best practices as you build a new game rather than optimizing only after publishing.
- [page](https://create.roblox.com/docs/performance-optimization) **[[analytics-metrics]]** Run the cycle: identify issues with built-in tools, improve, then monitor impact with analytics tools.
- [page](https://create.roblox.com/docs/performance-optimization) **[[scripting-and-performance]]** Target 60 FPS by default; expensive computation overtaxing CPU or GPU is the typical cause of low frame rate.
- [page](https://create.roblox.com/docs/performance-optimization) **[[scripting-and-performance]]** Keep server heartbeat high; a low server heartbeat lowers frame rate for all clients and increases latency.
- [page](https://create.roblox.com/docs/performance-optimization) **[[scripting-and-performance]]** Fix memory leaks, since memory use can grow over time even when starting usage is low.
- [page](https://create.roblox.com/docs/performance-optimization) **[[scripting-and-performance]]** Reduce memory usage to avoid server crashes that disconnect everyone and to reach lower-end and mobile devices.
- [page](https://create.roblox.com/docs/performance-optimization) **[[first-session-onboarding]]** Cut join time; long joins hurt acquisition and retention because players leave before entering.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization) Default target frame rate: **60 FPS (one frame every 16.67 ms with proper frame pacing)**
- [page](https://create.roblox.com/docs/performance-optimization) Join time definition: **Time from clicking play to world rendered and player can move**

## Tools
Roblox built-in performance tools, Roblox analytics tools

## Topics
[[analytics-metrics]] [[development-process-and-speed]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
