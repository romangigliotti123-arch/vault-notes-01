---
title: "Docs: production / analytics / custom-fields"
url: https://create.roblox.com/docs/production/analytics/custom-fields.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / custom-fields

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/production/analytics/custom-fields.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on custom fields for the AnalyticsService. Explains how to attach up to three string-valued custom dimensions (CustomField01-03) to economy, funnel and custom events for filtering, with an 8,000 unique-combination limit and a code example.

## Tips
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) **[[analytics-metrics]]** Use custom fields to slice economy, funnel and custom events by game-specific dimensions such as level, class or weapon type.
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) **[[analytics-metrics]]** Pass custom field values as strings; convert booleans and numbers to string format before logging.
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) **[[analytics-metrics]]** Only Enum.AnalyticsCustomFieldKeys.CustomField01/02/03 keys are read; any other keys are silently ignored.
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) **[[analytics-metrics]]** Prefix values with the dimension name (e.g. "Level - 10") to make charts easier to read later.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) Custom fields per event: **3** (Maximum number of custom fields (CustomField01-03) per event)
- [page](https://create.roblox.com/docs/production/analytics/custom-fields) Unique value combinations: **8,000** (Maximum unique combinations across the three custom fields)

## Tools
AnalyticsService:LogEconomyEvent, Enum.AnalyticsCustomFieldKeys

## Topics
[[analytics-metrics]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
