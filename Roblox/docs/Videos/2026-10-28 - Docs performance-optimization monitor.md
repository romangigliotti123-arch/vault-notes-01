---
title: "Docs: performance-optimization / monitor"
url: https://create.roblox.com/docs/performance-optimization/monitor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / monitor

[Open](https://create.roblox.com/docs/performance-optimization/monitor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Performance Dashboard. Shows how to use client/server tabs with date ranges to spot crash-rate and memory regressions, then drill into the Developer Console Memory tab (PlaceScriptMemory) to find a leaking script.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[analytics-metrics]]** Use the Performance Dashboard client and server tabs with date ranges to track how each update affected performance over time.
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[testing-debugging-and-qa]]** Reproduce memory issues by playing longer sessions and watching memory over time; short Studio tests can miss growth that crashes live players.
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[optimization-and-streaming]]** Watch client memory on lower-end devices; steadily growing usage can cause crashes there even when Studio looks fine.
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[optimization-and-streaming]]** Check the Developer Console Memory tab, PlaceScriptMemory breakdown, to find scripts whose memory grows with player interactions.
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[scripting-and-performance]]** Clean up data added to large tables on interaction; unbounded tables that never release entries cause infinite memory growth and crashes.
- [page](https://create.roblox.com/docs/performance-optimization/monitor) **[[analytics-metrics]]** Compare the Performance Dashboard with other analytics dashboards to link performance changes to business metrics like session time.

## Tools
Performance Dashboard, Developer Console Memory tab

## He points to
- Analytics

## Topics
[[analytics-metrics]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
