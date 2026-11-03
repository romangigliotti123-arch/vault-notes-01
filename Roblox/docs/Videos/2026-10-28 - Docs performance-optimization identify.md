---
title: "Docs: performance-optimization / identify"
url: https://create.roblox.com/docs/performance-optimization/identify.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / identify

[Open](https://create.roblox.com/docs/performance-optimization/identify.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on identifying performance issues: lists diagnostic tools (Developer Console, MicroProfiler, Performance Stats, Debug Stats, Scene Analysis, Network Simulation, Performance Dashboard) and gives thresholds for server heartbeat, server/client memory, frame rate, load time measurement, and ping types.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[scripting-and-performance]]** Check server heartbeat in Developer Console Server Jobs tab (Steps Per Sec); heartbeat is capped at 60, so lower values indicate a performance issue.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Use MicroProfiler to find frames exceeding 16.67 ms and inspect spikes where some frames take much longer than others.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Keep server memory usage below 50%; server memory is roughly 6.25 GiB + 100 MiB × peak connected players.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Server memory grows as players join but does not shrink when they leave, so base planning on peak player count.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Investigate client memory if crash rate rises above 2-3%, especially after an update; check GraphicsMeshParts, GraphicsTexture and Sounds in Developer Console.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Evaluate frame rate on the client, not Studio, since Studio skews performance stats; test on low-end devices where problems are more visible.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Set Graphics Mode to manual and max graphics quality when evaluating frame rate to remove frame rate manager effects.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** If heartbeat stays low after optimizing, reserve more CPU via Extended Services for Compute.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Measure load time before and after each change with a stopwatch or the ReplicatedFirst script; sudden increases often mean new content in ReplicatedStorage or larger assets.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Inspect free Creator Store models for unrecognized or obfuscated scripts that generate thousands of extra instances, inflating join size.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[optimization-and-streaming]]** Enable instance streaming to replicate only the Workspace area near spawn at join time, reducing load time.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[testing-debugging-and-qa]]** If data ping is significantly higher than network ping, use MicroProfiler to view network traffic and reduce replication queueing.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[testing-debugging-and-qa]]** Use Network Simulation in Studio (latency, jitter, packet loss) to playtest connection quality.
- [page](https://create.roblox.com/docs/performance-optimization/identify) **[[analytics-metrics]]** Use the Performance Dashboard to track client/server memory, client FPS, server heartbeat and crash rates over time in live sessions.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/identify) Server heartbeat cap: **60 FPS (16.67 ms per frame)** (Server heartbeat cap for all games; lower suggests performance issue)
- [page](https://create.roblox.com/docs/performance-optimization/identify) Server memory formula: **6.25 GiB + 100 MiB × max connected players** (Keep usage below 50%; 30 players ≈ 9.18 GiB)
- [page](https://create.roblox.com/docs/performance-optimization/identify) Client crash rate threshold: **2-3%** (Investigate if crash rates rise above this in Performance Dashboard)
- [page](https://create.roblox.com/docs/performance-optimization/identify) Default client FPS cap: **60 FPS (up to 240 on Windows)** (Users can raise cap to 240 FPS on Windows)
- [page](https://create.roblox.com/docs/performance-optimization/identify) Frame budget: **16.67 ms** (Frame time threshold in MicroProfiler for client and server)

## Tools
Developer Console, MicroProfiler, Scene Analysis, Performance Stats, Debug Stats, Network Simulation, Performance Dashboard

## He points to
- Roblox docs: monitoring performance
- Roblox docs: Improve performance
- Roblox docs: networking and replication
- Roblox docs: Extended Services for Compute

## Topics
[[analytics-metrics]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
