---
title: "Docs: cloud / guides / analytics"
url: https://create.roblox.com/docs/cloud/guides/analytics.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / analytics

[Open](https://create.roblox.com/docs/cloud/guides/analytics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API docs for the Analytics Query API. Covers API key setup, querying metrics (DAU, revenue, retention) with granularity, breakdowns, filters, dimension-value discovery, long-running operations, funnels, and error codes.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Create an API key with universe.analytics:read on universe-analytics and add your experience under Access Permissions; include it as x-api-key on every request.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Standard metrics (engagement, monetization, acquisition, retention) have up to 4 years of history; performance metrics only 28 days.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Date ranges over two years only support OneWeek, OneMonth, or None granularity.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Use granularity None with breakdown and limit to rank top-N series, then run a second query filtered to those values for a display metric.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Funnel steps only appear on days when a user reached them; use a 90-day lookback to discover all steps.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Weekly and monthly buckets count distinct users across the period, not a sum of daily values.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Check data point status: Projected values may change; NotStatisticallySignificant values are unreliable (e.g. crash rate in small countries).
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** On 429 (data point budget exceeded), shorten the date range, use coarser granularity, or reduce breakdown series with limit.
- [page](https://create.roblox.com/docs/cloud/guides/analytics) **[[analytics-metrics]]** Buckets are UTC-aligned; convert your reporting day to UTC when comparing against dashboard figures.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/analytics) Standard metric history: **up to 4 years** (Engagement, monetization, acquisition, retention metrics)
- [page](https://create.roblox.com/docs/cloud/guides/analytics) Performance metric history: **28 days** (Crash rate, frame rate, etc.)
- [page](https://create.roblox.com/docs/cloud/guides/analytics) Granularity limit for long ranges: **ranges >2 years: OneWeek, OneMonth, None only** (Date range constraint)
- [page](https://create.roblox.com/docs/cloud/guides/analytics) Top-N breakdown limit example: **limit 5** (Top 5 countries by DAU example)
- [page](https://create.roblox.com/docs/cloud/guides/analytics) Funnel discovery lookback: **90 days** (Recommended safe default for funnel step discovery)

## Tools
Roblox Analytics Query API, Creator Dashboard, curl

## He points to
- Roblox Creator Dashboard
- Roblox DevForum (for API error reports)

## Topics
[[analytics-metrics]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
