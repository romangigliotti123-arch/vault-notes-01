---
title: "Docs: cloud / guides / analytics / benchmarks"
url: https://create.roblox.com/docs/cloud/guides/analytics/benchmarks.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / analytics / benchmarks

[Open](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference doc for the experimental Roblox Benchmarks API (analytics-benchmark/v1). Covers auth via x-api-key with universe.analytics:read, request fields (metric, date range, benchmarkType, percentiles, filter, l7_average variant), benchmark types (genre, similarity, top experiences), response structure, and error codes.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Use the Benchmarks API to compare your metrics against genre, similarity, or top-experience groups rather than judging numbers in isolation.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Set endTime one day later in Analytics Query API than in Benchmarks API, since Benchmarks endTime is inclusive and Analytics endTime is exclusive.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Request BENCHMARK_TYPE_SIMILARITY explicitly for metrics that only have similarity benchmarks, otherwise the series come back empty.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** If the requested benchmark type has no data, read availableTypes in the response and retry with a supported type.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Start and end times must be RFC 3339 midnight UTC; a start time later in the day excludes that day's benchmark value.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Benchmarks API returns 400 for benchmarkVariantId on metrics that don't support l7_average; omit it for those metrics.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Top-experience benchmarks ignore the percentiles field and return one percentile chosen from your 30-day average value.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Keep date ranges within 400 days and at most 10 percentiles per request to avoid 400 errors.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** On 429 rate-limit responses, wait and retry at a lower request rate.
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) **[[analytics-metrics]]** Generate the API key with your experience in Access Permissions and grant universe.analytics:read on universe-analytics, then send it in the x-api-key header.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) Max date range: **400 days** (Benchmarks API endTime must be at most 400 days after startTime)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) Max percentiles per request: **10 values, integers 0-100** (percentiles field in Benchmarks API request body)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) Default percentiles: **50 and 90 (10 and 50 for lower-is-better metrics)** (Used when percentiles field is omitted)
- [page](https://create.roblox.com/docs/cloud/guides/analytics/benchmarks) Example ForwardD1Retention benchmark: **0.3 (50th pct), 0.45 (90th pct)** (Example genre benchmark values for 2026-01-01; illustrative only)

## Tools
Benchmarks API (analytics-benchmark/v1), Analytics Query API, Creator Dashboard

## He points to
- Roblox Analytics Query API docs
- Supported metrics list (Roblox docs)
- Roblox DevForum (for 500 error reports)

## Topics
[[analytics-metrics]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
