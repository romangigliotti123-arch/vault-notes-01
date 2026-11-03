---
title: "Docs: production / analytics / performance"
url: https://create.roblox.com/docs/production/analytics/performance.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / performance

[Open](https://create.roblox.com/docs/production/analytics/performance.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Hub Performance dashboard docs: where to find client/server metrics, what each chart means, P10/P50/P90 interpretation, place-version regression comparison, Roblox update annotations, troubleshooting steps, and the Client API Calls in First 60s After Join metric.

## Tips
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[analytics-metrics]]** Monitor the Performance dashboard before and after every update to catch regressions early.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[analytics-metrics]]** Dashboard charts require at least 100 daily active users (DAU) to display.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[analytics-metrics]]** Use Breakdown by Place Version to compare the latest release against earlier versions for lower FPS or more out-of-memory exits.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[scripting-and-performance]]** Keep client CPU time under 16 ms to hit a 60 FPS client frame rate.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[scripting-and-performance]]** Keep server CPU time under 16 ms per frame to sustain a 60 FPS server frame rate.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[scripting-and-performance]]** Keep server memory below 50% of total server memory and ideally below 3 GB; investigate if it stays high or keeps rising.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[scripting-and-performance]]** If server CPU time is high but core usage is low, investigate multithreading; use Extended Services for Compute if core usage stays high after optimizing.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[scripting-and-performance]]** Check memory tags with the Developer Console and drill into process groups in the MicroProfiler to locate expensive processes.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[common-mistakes]]** Do not rely on the client crash rate when the chart shows a dashed line (low sample size); check the total crash count instead.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[updates-live-ops]]** If an update severely hurts metrics, consider rolling it back, then troubleshoot using the Developer Console, Script Profiler, and MicroProfiler.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[first-session-onboarding]]** In the first 60 seconds after join, asset delivery should be the most-called API; if inventory, friends, or users is most-hit, refactor join scripts to prioritize asset loading.
- [page](https://create.roblox.com/docs/production/analytics/performance) **[[community-and-discord]]** Gather user feedback from your community when troubleshooting performance problems.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/performance) Minimum DAU for client/server charts: **100 daily active users** (Performance dashboard shows charts only above this threshold)
- [page](https://create.roblox.com/docs/production/analytics/performance) Client CPU time for 60 FPS: **< 16 ms per frame** (Client CPU time must be below this to hit 60 frame rate)
- [page](https://create.roblox.com/docs/production/analytics/performance) Server CPU time for 60 FPS: **< 16 ms per frame** (Server CPU time must be below this to hit 60 frame rate)
- [page](https://create.roblox.com/docs/production/analytics/performance) Server memory guideline: **< 50% of total server memory, and < 3 GB** (Recommended ceiling; chart does not show total server memory)
- [page](https://create.roblox.com/docs/production/analytics/performance) Server frame rate cap: **60 FPS** (Ideal server frame rate is always 60)
- [page](https://create.roblox.com/docs/production/analytics/performance) Compute efficiency: **>100% means above Roblox average** (Higher is more efficient; not an indicator of player experience quality)
- [page](https://create.roblox.com/docs/production/analytics/performance) Percentile example P90 server heartbeat: **59 FPS (90% of servers at or below)** (Docs example for interpreting P90)
- [page](https://create.roblox.com/docs/production/analytics/performance) Percentile example P10 server heartbeat: **40 FPS (10% of servers at or below)** (Docs example for interpreting P10)
- [page](https://create.roblox.com/docs/production/analytics/performance) Metric window for client API calls: **First 60s after join** (Available only to a small number of top games; updated hourly)

## Tools
Creator Hub Performance dashboard, Developer Console, Script Profiler, MicroProfiler, Enum.DeveloperMemoryTag, Extended Services for Compute

## He points to
- Client Compute doc
- Server Compute doc
- Script Computation doc
- Identify performance issues doc
- Improve performance doc
- Memory doc

## Topics
[[analytics-metrics]] [[common-mistakes]] [[community-and-discord]] [[first-session-onboarding]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
