---
title: "Docs: cloud / guides / alert / metrics"
url: https://create.roblox.com/docs/cloud/guides/alert/metrics.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / alert / metrics

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/guides/alert/metrics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference table of Roblox Analytics alert metrics and their supported dimensions, granularities, and 28-day data retention. Covers client performance (CPU, FPS, memory, crashes), server metrics, cross-server messaging, DataStore and MemoryStore request quotas, HTTP service, OOM exits, concurrency, and session time.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) **[[analytics-metrics]]** Set alerts on client crash rate (ClientCrashRate15m) and OOM exits by platform and memory group to catch device-specific stability problems early.
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) **[[analytics-metrics]]** Use percentile metrics (P10/P50/P90) for frame rate and memory, not just averages, to see how low-end players experience the game.
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) **[[optimization-and-streaming]]** Alert on ClientMemoryUsagePercentage and OomUnexpectedExits per platform, since mobile and low-memory devices hit out-of-memory exits first.
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) **[[data-persistence]]** Monitor DataStore read, write, list and remove quota consumption by DataStoreRequestSource to detect quota exhaustion before players lose data.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) Data retention for alert metrics: **28 days** (Applies to all listed alert metrics)
- [page](https://create.roblox.com/docs/cloud/guides/alert/metrics) Alert granularities: **OneMinute, HalfHour, OneHour, OneDay (Server memory adds None)** (Granularity options for alert evaluation windows)

## Tools
Roblox Analytics alerts

## Topics
[[analytics-metrics]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
