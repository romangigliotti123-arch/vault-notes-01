---
title: "Docs: performance-optimization / microprofiler / network"
url: https://create.roblox.com/docs/performance-optimization/microprofiler/network.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / microprofiler / network

[Open](https://create.roblox.com/docs/performance-optimization/microprofiler/network.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on capturing and reading network traffic in MicroProfiler frame dumps. Covers High/Low/Off verbosity, Rx/Tx graphs by traffic type (physics, data, assets, terrain, large replicator), and the Network events window for diagnosing latency and loading problems.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/network) **[[optimization-and-streaming]]** Network data appears only in MicroProfiler frame dumps from desktop client or Studio, not the real-time overlay. Save dumps when you suspect network-related lag.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/network) **[[optimization-and-streaming]]** Use Low network verbosity to capture more frames in a dump; it is less computationally intensive and is the default, including for mobile profiling.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/network) **[[optimization-and-streaming]]** Enable Log Scale Graph when a few large spikes hide small traffic bars, so small network bars become visible.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/network) **[[optimization-and-streaming]]** Use High verbosity to see items within batch packets, the deserializing task, and asset IDs, so you can trace which assets or properties cause load.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/network) **[[optimization-and-streaming]]** Right-click a frame's stacked bar to open Network events and click individual events to see size, direction and type.

## Tools
MicroProfiler, Roblox Studio, Roblox desktop client

## He points to
- Roblox docs: MicroProfiler

## Topics
[[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
