---
title: "Docs: cloud-services / memory-stores / observability"
url: https://create.roblox.com/docs/cloud-services/memory-stores/observability.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / observability

[Open](https://create.roblox.com/docs/cloud-services/memory-stores/observability.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page on the Memory Stores observability dashboard: where to find it, its quota and API charts, and the four built-in email alerts (memory and request thresholds) with their warning/critical levels.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[analytics-metrics]]** Open the Memory Stores dashboard via Creations > game > Monitoring > Memory Stores; you need game owner or analytics group permission.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[optimization-and-streaming]]** Keep memory store data structures lean: clean up processed data and avoid long expiration times, since extra data fills the memory quota even with few keys.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[analytics-metrics]]** Act on a yellow warning once memory passes 70% of quota within an hour, before it turns into a critical overage.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[scripting-and-performance]]** Reduce request volume: DataStructureRequestsOverLimit and TotalRequestsOverLimit throttling triggers a critical alert above 10% of requests in an hour; count is what matters, not size.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[scripting-and-performance]]** Investigate request failures immediately: a critical alert fires when failures exceed 20% of requests within an hour.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[analytics-metrics]]** Use the Request Count by Status and Request by API x Status charts to find the ratio of Success to error responses when troubleshooting.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) **[[analytics-metrics]]** Dashboard data covers only the past 30 days; earlier custom ranges return a Request Failed error, so export or record older data in time.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Memory usage warning threshold: **70% of total quota within the past hour** (Yellow warning alert on Memory Usage chart)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Memory usage critical threshold: **Exceeded memory size quota within the past hour** (Red critical alert on Memory Usage chart)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Request failure critical threshold: **20% of requests failed within the past hour** (Critical email alert)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Throttling critical threshold: **More than 10% of requests throttled within the past hour** (Based on DataStructureRequestsOverLimit + TotalRequestsOverLimit)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Dashboard history window: **30 days** (Earlier time ranges return Request Failed error)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/observability) Alert frequency: **At most once a day per alert** (Email notifications per alert type)

## Tools
Memory Stores observability dashboard, Error Report

## He points to
- Observability status code table
- Troubleshooting
- Limits and Quotas

## Topics
[[analytics-metrics]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
