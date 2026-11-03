---
title: "Docs: production / analytics / custom-events"
url: https://create.roblox.com/docs/production/analytics/custom-events.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / custom-events

[Open](https://create.roblox.com/docs/production/analytics/custom-events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on Custom Events in AnalyticsService. Covers counters vs. events with values, the 100-event cap, server-only sending in published games, aggregations, custom fields vs. event names for cardinality, and using the Explore page to analyze core loops (Plant reference game).

## Tips
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Track custom events for metrics default analytics miss, such as UI adoption, ability usage per map, or kill/death ratios per weapon.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Send custom events only from the server via AnalyticsService:LogCustomEvent; events can't be sent from the client or Studio.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Use custom fields instead of many event names (e.g. one PlantSeed event with plant-type field) because event name cardinality is much tighter.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Batch events with values (e.g. 10 zombies killed as one event) to stay under rate limits.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Instrument the full core loop (seeds planted, plants watered, shop visits), not just the final action, to find where players drop off or prefer options.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[core-loops-and-game-design]]** Check whether one option dominates a loop (e.g. one plant type strongly preferred) and rebalance to avoid repetitiveness and economy imbalance.
- [page](https://create.roblox.com/docs/production/analytics/custom-events) **[[analytics-metrics]]** Expect up to 24 hours before Explore page charts populate, since events are aggregated daily.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/custom-events) Custom events per game: **up to 100** (Maximum custom events you can add to one game)
- [page](https://create.roblox.com/docs/production/analytics/custom-events) Data latency: **up to 24 hours** (Events aggregated daily before Explore charts populate)
- [page](https://create.roblox.com/docs/production/analytics/custom-events) Counter value: **1** (Counter events use default value 1; max/min/avg equal 1, sum equals count)
- [page](https://create.roblox.com/docs/production/analytics/custom-events) Batching example: **10 zombies in one event** (Send batched value instead of ten single events to respect rate limits)

## Games
- **Plant**: Reference game: HarvestPlant event tracks plants harvested per player per day, broken down by plant type to compare preferences.

## Tools
AnalyticsService, Creator Hub Analytics Explore page

## He points to
- Custom fields documentation

## Quotes
- [page](https://create.roblox.com/docs/production/analytics/custom-events) "You should use custom fields whenever possible instead of event names, since there is a much tighter cardinality limit on event names than custom fields."
- [page](https://create.roblox.com/docs/production/analytics/custom-events) "Events can only be sent from the server and in published games. Events can't be sent from the client or Studio."

## Topics
[[analytics-metrics]] [[core-loops-and-game-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
