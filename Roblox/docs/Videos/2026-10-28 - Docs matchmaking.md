---
title: "Docs: matchmaking"
url: https://create.roblox.com/docs/matchmaking.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: matchmaking

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/matchmaking.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on matchmaking: how the service filters eligible servers, scores them via a weighted sum of signals (default Roblox or custom), and assigns the player to the top-scoring server. Covers numerical vs categorical attributes, custom signals/attributes, weight tuning, mock-server evaluation, and analytics.

## Tips
- [page](https://create.roblox.com/docs/matchmaking) **[[matchmaking-and-teleport]]** Use custom matchmaking only if default matching is insufficient; adjust signal weights to control which factors (e.g., latency, skill) matter most in server selection.
- [page](https://create.roblox.com/docs/matchmaking) **[[matchmaking-and-teleport]]** Increase the latency signal weight to prioritise low-ping servers for smoother gameplay.
- [page](https://create.roblox.com/docs/matchmaking) **[[matchmaking-and-teleport]]** Preview weight changes by evaluating them on mock servers before deploying them to live matchmaking.
- [page](https://create.roblox.com/docs/matchmaking) **[[matchmaking-and-teleport]]** Custom signals require a custom attribute first; custom attributes are how you pull data from your DataStores into matchmaking.

## Tools
Matchmaking service, Custom attributes, Custom signals, Mock servers

## Topics
[[analytics-metrics]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
