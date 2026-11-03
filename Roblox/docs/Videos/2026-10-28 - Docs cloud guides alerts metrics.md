---
title: "Docs: cloud / guides / alerts / metrics"
url: https://create.roblox.com/docs/cloud/guides/alerts/metrics.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / alerts / metrics

[Open](https://create.roblox.com/docs/cloud/guides/alerts/metrics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference table of Roblox Analytics alert metrics and their supported dimensions (filter-only dimensions noted), with granularities and 28-day data retention. Covers client CPU, crashes, FPS, memory, cross-server messaging, DataStore and MemoryStore request quotas, HTTP service, OOM exits, concurrency, server CPU/frame rate/memory, and session time. Metric names are case-sensitive and the same in the Alerts dashboard and API.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[analytics-metrics]]** Set alerts on client crash rate (ClientCrashRate15m) and unexpected OOM exits (OomUnexpectedExits) to catch stability regressions after releases.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[analytics-metrics]]** Use percentile metrics (P10/P50/P90) for client FPS and memory, not just averages, to see how low-end devices perform.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[analytics-metrics]]** Alert on DataStore quota consumption (read/write/list/remove) per DataStoreRequestSource to spot runaway save loops before hitting limits.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[analytics-metrics]]** Filter alerts by Place to scope them to a single experience; Place is filter-only and cannot be used as a split dimension.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[optimization-and-streaming]]** Monitor server frame rate and server CPU time by category to locate which systems cause server lag.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[scripting-and-performance]]** Track HttpServiceResponseTime P90 and HttpServiceRequestsCount by status to find slow or failing external HTTP calls.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[data-persistence]]** Monitor DataStoreRequests by operation and status to detect failed requests and throttling in save logic.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[client-server-and-remotes]]** Watch cross-server messaging fanout ratio and published/received message counts to detect MessagingService overuse.
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) **[[analytics-metrics]]** Use Session time percentiles (P10/P50/P90) alongside peak concurrent players to read engagement by platform and OS.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) Data retention for alert metrics: **28 days** (Applies to all listed alert metrics)
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) Client crash rate window: **15 minutes (ClientCrashRate15m)** (Metric name suffix indicates 15m window)
- [page](https://create.roblox.com/docs/cloud/guides/alerts/metrics) Granularities available: **OneMinute, HalfHour, OneHour, OneDay (Server memory usage also None)** (Per-metric granularity options)

## Tools
Roblox Analytics Alerts dashboard, Roblox Analytics Alerts API

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
