---
title: "Docs: cloud / guides / analytics / metrics"
url: https://create.roblox.com/docs/cloud/guides/analytics/metrics.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / analytics / metrics

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/guides/analytics/metrics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference page for the Roblox Analytics Query API: lists the metrics and dimensions available (retention, engagement, monetization, acquisition, home-recommendation signals, performance, economy, funnels, custom events, thumbnails, matchmaking, DataStore), with granularities, data retention windows, and supported segmentation dimensions. Values are case-sensitive.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) **[[analytics-metrics]]** Query retention by segment dimensions (Platform, Country, AcquisitionSource, UserSegmentationPayerStatus) rather than only the blended D1/D7/D30 number.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) **[[analytics-metrics]]** Export performance metrics within 28 days; client and server performance data is only retained for 28 days.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) **[[analytics-metrics]]** Export thumbnail metrics within 30 days; thumbnail data is only retained for 30 days.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) **[[analytics-metrics]]** Use ClientFpsP10 rather than the average to see the experience of your slowest players; P10 captures low-end performance.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) Metric data retention (most engagement, retention, monetization): **1468 days** (Daily/weekly/monthly granularity metrics kept for about four years)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) Performance and stability data retention: **28 days** (Client/server CPU, memory, FPS, crashes, DataStore quotas)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) Thumbnail metric data retention: **30 days** (Impressions, qualified PTR, session length by thumbnail)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics) Matchmaking signal data retention: **90 days** (Ping, occupancy, skill and friend-match signals)

## Tools
Analytics Query API

## Topics
[[ab-testing-and-experiments]] [[analytics-metrics]] [[discovery-algorithm]] [[optimization-and-streaming]] [[thumbnails-icons]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
