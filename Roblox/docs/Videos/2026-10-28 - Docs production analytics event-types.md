---
title: "Docs: production / analytics / event-types"
url: https://create.roblox.com/docs/production/analytics/event-types.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / event-types

[Open](https://create.roblox.com/docs/production/analytics/event-types.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on AnalyticsService event types: economy, funnel, and custom events feeding free Creator Dashboard analytics. Covers dashboard types, validation via View Events, and rate/cardinality limits (custom fields, resource types, funnel steps, 90-day rolloff).

## Tips
- [page](https://create.roblox.com/docs/production/analytics/event-types) **[[analytics-metrics]]** Log economy events only after a successful operation (e.g. after a purchase succeeds, not when attempted), since failed attempts create misleading data.
- [page](https://create.roblox.com/docs/production/analytics/event-types) **[[analytics-metrics]]** Use custom fields to break down values instead of creating separate currencies, e.g. one XP currency with class as Custom Field 1, to conserve currency cardinality.
- [page](https://create.roblox.com/docs/production/analytics/event-types) **[[analytics-metrics]]** Use the View Events tool on Economy, Funnel, or Custom pages to check near real-time event lists while charts take about 24 hours to appear.
- [page](https://create.roblox.com/docs/production/analytics/event-types) **[[analytics-metrics]]** Check your game's error report to catch errors in event tracking.
- [page](https://create.roblox.com/docs/production/analytics/event-types) **[[analytics-metrics]]** Plan for rate limits: AnalyticsService allows 120 + (20 × CCU) requests per minute globally, so scale logging with server population.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/event-types) Global rate limit for AnalyticsService requests per minute: **120 + (20 * CCU)** (Total AnalyticsService requests per minute across the game)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Custom fields per event: **3** (Economy, funnel, and custom events; e.g. Class, Level, Weapon)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Unique values per custom field before grouping: **8,000 combined values across all custom fields** (Beyond this, values are grouped as Other)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Resource types for economy events: **10** (e.g. Coins, Gold, Credits)
- [page](https://create.roblox.com/docs/production/analytics/event-types) transactionTypes before grouping as Other: **20** (e.g. IAP, Gameplay)
- [page](https://create.roblox.com/docs/production/analytics/event-types) itemSkus before grouping as Other: **100** (Unlimited otherwise, grouped after 100)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Funnels per game: **10** (Funnel events only)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Steps per funnel: **100** (Funnel events only)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Custom eventNames: **100** (Custom events only, e.g. MonsterDefeated, PetAdoption)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Chart appearance delay after adding events: **typically 24 hours** (Use View Events tool for near real-time check meanwhile)
- [page](https://create.roblox.com/docs/production/analytics/event-types) Event retention on dashboard: **90 days from last data received** (Events automatically roll off after this period)

## Tools
Creator Dashboard Analytics, AnalyticsService

## He points to
- Economy events docs
- Funnel events docs
- Custom events docs
- Creator Dashboard error report

## Quotes
- [page](https://create.roblox.com/docs/production/analytics/event-types) "Verify that your calls to the AnalyticsService methods occur after a successful operation, not when the user attempts a purchase."
- [page](https://create.roblox.com/docs/production/analytics/event-types) "Set XP as one currency and Warrior, Mage, Paladin as Custom Field 1 instead of separate currencies."

## Topics
[[analytics-metrics]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
