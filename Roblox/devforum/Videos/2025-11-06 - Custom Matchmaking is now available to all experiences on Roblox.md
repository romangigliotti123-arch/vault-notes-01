---
title: "Custom Matchmaking is now available to all experiences on Roblox"
url: https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-11-06
views: 389
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Custom Matchmaking is now available to all experiences on Roblox

[Open](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) | Roblox DevForum | 389 views | 2025-11-06

## Summary
Roblox DevForum announcement: Custom Matchmaking and Experimentation are now available to all experiences. Custom Matchmaking lets creators reweight built-in matchmaking signals (Latency, Language, Device Type, etc.) or add up to 2 custom signals from their own data. Experiments measure impact on playtime, retention and revenue per user.

## Tips
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[matchmaking-and-teleport]]** Adjust only a few matchmaking signal weights, a little at a time, to avoid making matchmaking too restrictive.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[matchmaking-and-teleport]]** Prioritise a few signals. Weights are relative across all signals, so raising many weights dilutes the important ones.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[matchmaking-and-teleport]]** For competitive games, store a skill rating in a DataStore, expose it as a custom signal, and weight it to match similar-skill players.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[matchmaking-and-teleport]]** Raise the Latency signal weight if your game needs responsive server-to-client replication.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[matchmaking-and-teleport]]** Raise the Language signal weight for co-op or social games where players need to chat and coordinate.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[ab-testing-and-experiments]]** Run matchmaking experiments at 100% of traffic; players are matched within the same variant, so lower rollouts shrink the server pool and reduce statistical significance.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[ab-testing-and-experiments]]** Matchmaking experiments need enough servers to choose from; without them, monitor matchmaking changes through analytics dashboards instead.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[ab-testing-and-experiments]]** Without enough players for an A/B test, use a pre-post analysis comparing matchmaking signal dashboards before and after the change.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[ab-testing-and-experiments]]** Measure matchmaking configs against playtime, retention and revenue per user before full rollout.
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) **[[analytics-metrics]]** Preview weight changes against mock data in the Custom Matchmaking page to confirm matching behaves as intended before publishing.

## Numbers
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) Custom signals allowed: **2 per matchmaking scoring configuration** (Maximum custom signals per Custom Matchmaking configuration)
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) Recommended experiment traffic rollout: **100%** (Players matched only within same variant, so lower rollout limits server pool)
- [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) New signal default weight (custom config): **0** (New signals added to custom configs start at weight 0; Roblox Default gets default weight)

## Tools
Custom Matchmaking dashboard page, Experiments dashboard tab

## He points to
- Roblox Learn video on Custom Matchmaking
- Custom Matchmaking documentation (Server Scoring, Attributes and signals)
- Roblox DevForum post on beta launch

## Topics
[[ab-testing-and-experiments]] [[analytics-metrics]] [[matchmaking-and-teleport]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
