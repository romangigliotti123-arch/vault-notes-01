---
title: "Docs: cloud-services / data-stores / observability"
url: https://create.roblox.com/docs/cloud-services/data-stores/observability.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / observability

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud-services/data-stores/observability.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page describing the Data Stores observability dashboard in Creator Hub: access steps, available charts (storage, request counts by API/status, read/write/list/remove quota usage), filtering by standard vs ordered stores, 30-day data window, and a 3-minute data lag.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) **[[analytics-metrics]]** Open Creations > Monitoring > Data Stores in Creator Hub to watch DataStore request counts and quota usage; you need owner or analytics group permission.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) **[[analytics-metrics]]** Use Request Count by Status and Request by API x Status to find which DataStore API methods are returning errors before players notice data issues.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) **[[analytics-metrics]]** Read Write List Remove Quota Usage charts show usage against future per-category limits; check them before launch and growth to avoid throttling.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) **[[analytics-metrics]]** Dashboard data from the last 3 minutes may be incomplete, so ignore the drop at the chart end.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) Dashboard history window: **30 days** (Charts show past 30 days; earlier custom ranges return Request Failed)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) Data freshness lag: **3 minutes** (Most recent three minutes of data may be incomplete)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/observability) Storage unit conversion: **1 KB = 1024 bytes** (Storage usage and limit displayed in bytes)

## Tools
Creator Hub Data Stores dashboard, Class.DataStoreService

## Topics
[[analytics-metrics]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
