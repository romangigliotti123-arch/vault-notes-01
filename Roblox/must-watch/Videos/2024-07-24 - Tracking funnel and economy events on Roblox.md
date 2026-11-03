---
title: "Tracking funnel and economy events on Roblox"
url: https://youtu.be/NFLP-FVv834
creator: Roblox Creators
official: true
advice_density: medium
date: 2024-07-24
views: 5809
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Tracking funnel and economy events on Roblox

[Watch](https://youtu.be/NFLP-FVv834) | MustWatch | 5,809 views | 2024-07-24

## Summary
Roblox Creator Analytics team walks through instrumenting Economy and Funnel events via AnalyticsService: source/sink logging, custom fields, one-time vs recurring funnels, reading economy and funnel charts, validation against exploiters, and limits (100 unique item SKUs).

## Tips
- [1:27](https://youtu.be/NFLP-FVv834?t=87) **[[analytics-metrics]]** Track onboarding funnel steps; fixing a big drop-off (e.g. plant-seed step) can raise day-1 retention and session time, which feed discovery.
- [3:13](https://youtu.be/NFLP-FVv834?t=193) **[[analytics-metrics]]** Keep sources and sinks balanced: a constantly growing currency means not enough places to spend it; add sinks.
- [4:34](https://youtu.be/NFLP-FVv834?t=274) **[[analytics-metrics]]** Watch average wallet balance: spikes mean too few sinks; always at zero means players need more currency.
- [16:10](https://youtu.be/NFLP-FVv834?t=970) **[[analytics-metrics]]** Validate events server-side before sending to analytics, since exploiters can fire client events and corrupt charts.
- [16:51](https://youtu.be/NFLP-FVv834?t=1011) **[[first-session-onboarding]]** Without a tutorial, instrument basic core-loop steps as an onboarding funnel to find where players get confused, then build the tutorial around it.
- [17:52](https://youtu.be/NFLP-FVv834?t=1072) **[[first-session-onboarding]]** Compare funnel drop-off across segments (e.g. age groups); younger players dropped less with visual instruction than text, but test your own game.
- [14:49](https://youtu.be/NFLP-FVv834?t=889) **[[analytics-metrics]]** Send the first funnel step explicitly (not automatic on join); repeated steps collapse, and skipped steps are assumed completed.
- [6:55](https://youtu.be/NFLP-FVv834?t=415) **[[analytics-metrics]]** Log economy events after the transaction is saved; pass enum names as strings for transactionType fields.
- [19:56](https://youtu.be/NFLP-FVv834?t=1196) **[[analytics-metrics]]** Item SKUs beyond the top 100 group into 'Other'; keep item SKU counts manageable for readable sales charts.

## Numbers
- [1:27](https://youtu.be/NFLP-FVv834?t=87) Onboarding drop-off example: **Drop-off at plant-seed step (example, not a measured figure)** (Speaker's illustrative example of fixing onboarding)
- [17:52](https://youtu.be/NFLP-FVv834?t=1072) Fabled Legacy room 2 drop-off: **21%** (Dungeon crawler onboarding funnel, 13+ players)
- [18:34](https://youtu.be/NFLP-FVv834?t=1114) Drop-off by age: **13+: 21%; 12 and under: 23%** (Fabled Legacy room 2 funnel by age range)
- [19:56](https://youtu.be/NFLP-FVv834?t=1196) Unique item SKU limit: **100 (then grouped into 'Other')** (Economy item SKU reporting limit)
- [20:48](https://youtu.be/NFLP-FVv834?t=1248) Event rate limit: **120 + (20 * CCU) AnalyticsService requests per minute** (Limits slide on screen; economy and funnel events)
- [20:48](https://youtu.be/NFLP-FVv834?t=1248) Custom fields per event: **3 for economy events; 10 funnels; 20 unique values before 'Other'** (Limits slide; unique values per custom field)

## Games
- **Fabled Legacy** [17:11](https://youtu.be/NFLP-FVv834?t=1031): Dungeon crawler; onboarding funnel showed 21% drop at room 2 where difficulty ramps up; used as example of reading funnels.

## Tools
AnalyticsService (Roblox Studio), Economy events, Funnel events (one-time and recurring), Creator Analytics Suite

## He points to
- Roblox Creator Analytics economy and funnel docs

## Quotes
- [16:10](https://youtu.be/NFLP-FVv834?t=970) "Do some basic validation on your events in server-side code before you send them to us, because exploiters can fire events manually."
- [16:51](https://youtu.be/NFLP-FVv834?t=1011) "Even if you don't have a nice tutorial, just instrument those basic steps; that will help you see where your drop off is."

## On screen
Screens show Studio code for AnalyticsService economy/funnel logging, economy charts (total sources/sinks, average wallet balance), a funnel table with step completion and churn for Fabled Legacy (Joined Game, Selected Class, Loaded Into Dungeon, Dungeon Rooms 1-12), a filter panel (age range, gender, platform, device), and a limits slide (120 + 20×CCU requests/min, 10 funnels, 100 steps, 20 unique custom field values).

## Topics
[[analytics-metrics]] [[first-session-onboarding]]

Back to [[MustWatch - How to make successful Roblox games]]
