---
title: "Docs: production / analytics / funnel-events"
url: https://create.roblox.com/docs/production/analytics/funnel-events.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / funnel-events

[Open](https://create.roblox.com/docs/production/analytics/funnel-events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Funnel events in the Analytics dashboard. Covers how to log one-time (onboarding) and recurring (shop) funnel steps server-side, funnelSessionId usage, skipped/repeated step behavior, filters, date-range handling after edits, and validating client-sent step numbers to block exploiters.

## Tips
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Start funnel tracking with the onboarding flow; it is likely where most users are lost. Log a step after each player completes it.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Be consistent about when you call LogFunnelStepEvent and use easy-to-interpret step names; call after the player completes the step.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Funnel events can only be sent from the server in published games; they cannot be sent from the client or Studio.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Use a GUID funnelSessionId for recurring funnels like shop opens within one session; use a item-based key for longer upgrade-path funnels.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Validate step numbers received from clients on the server against max step before logging, to keep funnel data clean from exploiters.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** After editing funnel steps, set the dashboard date range to start at the edit date to see the updated funnel; mixed ranges show a warning.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[analytics-metrics]]** Use custom fields on funnels to compare segments, e.g. starter car choice or map, to find which variant gives better progression.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[core-loops-and-game-design]]** If a funnel step has the largest drop-off, add contextual indicators guiding players to that action, or require it before exploring the rest of the game.
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) **[[retention-d1-d7]]** Improve new-user retention and session time by tracking and fixing the onboarding funnel drop-offs.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) Funnel tabs on dashboard: **up to 10 funnels** (Analytics dashboard Funnel page on Creator Hub)
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) Saved step expiry: **180 days with no events** (User then counts as new for that funnel if they return)
- [page](https://create.roblox.com/docs/production/analytics/funnel-events) Unique funnelSessionId tracked per user per funnel: **10 most recent** (Older reused IDs count as a new session)

## Games
- **Plant**: Tycoon example: onboarding funnel (In Farm, Plant Seed, Water Plant); largest drop-off at step 2 Plant Seed.
- **ArmoryCheckout (example shop funnel)**: Recurring shop funnel example: Opened Store, Viewed Item, Added to Cart, tracked with a GUID funnelSessionId.

## Tools
Analytics dashboard (Creator Hub), AnalyticsService:LogFunnelStepEvent, AnalyticsService:LogOnboardingFunnelStepEvent, RemoteEvent

## He points to
- Creator Hub Analytics dashboard
- Custom fields docs

## Topics
[[analytics-metrics]] [[core-loops-and-game-design]] [[retention-d1-d7]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
