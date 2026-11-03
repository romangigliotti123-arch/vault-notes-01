---
title: "How to Boost your Game using Roblox Funnel Analytics"
url: https://youtu.be/u_8p65Bsm2Y
creator: GnomeCode
official: false
advice_density: medium
date: 2025-03-08
views: 19347
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Boost your Game using Roblox Funnel Analytics

[Watch](https://youtu.be/u_8p65Bsm2Y) | GnomeCode | 19,347 views | 2025-03-08

## Summary
Shows how to set up Roblox's onboarding funnel analytics in a linear doors-style game (Gnome Hotel) by logging funnel step events at join, elevator, teleport and each door, then reading the drop-off chart to find where players quit.

## Tips
- [0:40](https://youtu.be/u_8p65Bsm2Y?t=40) **[[analytics-metrics]]** Map your game as ordered funnel steps (join, lobby, elevator, teleport, each checkpoint) and log each with AnalyticsService:LogOnboardingFunnelStepEvent; best for linear games.
- [2:42](https://youtu.be/u_8p65Bsm2Y?t=162) **[[analytics-metrics]]** Log funnel steps server-side from the point where the player actually progresses, e.g. just before teleport logic, so drop-offs reflect real progress.
- [4:23](https://youtu.be/u_8p65Bsm2Y?t=263) **[[analytics-metrics]]** Expect ~24 hours before funnel charts appear; check View Events first to confirm events are arriving.
- [6:17](https://youtu.be/u_8p65Bsm2Y?t=377) **[[analytics-metrics]]** Look for big red drops in step completion; they point to the exact spot to fix, such as a hard encounter or bug.
- [7:00](https://youtu.be/u_8p65Bsm2Y?t=420) **[[core-loops-and-game-design]]** Smooth a sharp difficulty spike by adding an on-screen hint before the hard section so players are not instantly killed.
- [2:02](https://youtu.be/u_8p65Bsm2Y?t=122) **[[core-loops-and-game-design]]** Use per-checkpoint drop-off data to tune difficulty of later rooms, e.g. adjusting after seeing only ~26% finish.

## Numbers
- [4:55](https://youtu.be/u_8p65Bsm2Y?t=295) Players who entered game: **6,000**
- [4:55](https://youtu.be/u_8p65Bsm2Y?t=295) Completion rate: **25.82% (~1,500 players)**
- [5:37](https://youtu.be/u_8p65Bsm2Y?t=337) Lobby join to elevator conversion: **~85%**
- [0:40](https://youtu.be/u_8p65Bsm2Y?t=40) Example expected elevator conversion (hypothetical): **~90%**
- [1:21](https://youtu.be/u_8p65Bsm2Y?t=81) Example expected teleport success (hypothetical): **~99%**
- [0:00](https://youtu.be/u_8p65Bsm2Y?t=0) Game approval rating before analysis: **65%**

## Games
- **Gnome Hotel** [0:00](https://youtu.be/u_8p65Bsm2Y?t=0): Doors-style linear game; funnel data showed biggest drop at Door 22 after bacon chase, so a hint was considered for that section.

## Tools
AnalyticsService (LogOnboardingFunnelStepEvent), Roblox creator dashboard Funnel and View Events

## Quotes
- [5:37](https://youtu.be/u_8p65Bsm2Y?t=337) "we can see where the biggest drop offs are... our biggest drop is actually entering door 22 which is during the bacon chase"
- [7:00](https://youtu.be/u_8p65Bsm2Y?t=420) "if you have any big red bars that's something you really need to take a look at"

## Topics
[[analytics-metrics]] [[core-loops-and-game-design]]

Back to [[GnomeCode - How to make successful Roblox games]]
