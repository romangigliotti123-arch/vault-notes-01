---
title: "Docs: matchmaking / glossary"
url: https://create.roblox.com/docs/matchmaking/glossary.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: matchmaking / glossary

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/matchmaking/glossary.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Glossary for Roblox matchmaking scoring. Defines attributes (raw player/server values), signals (attributes transformed to 0-1 scores), weights, and how the weighted sum picks the highest-scoring server for a joining player. Covers numerical vs categorical custom signals and common device/language signals.

## Tips
- [page](https://create.roblox.com/docs/matchmaking/glossary) **[[matchmaking-and-teleport]]** Define custom attributes at universe level: player attributes (e.g. skill level, preferred mode) and server attributes (e.g. active game mode) to feed matchmaking scoring.
- [page](https://create.roblox.com/docs/matchmaking/glossary) **[[matchmaking-and-teleport]]** Set signal weights to control importance. Weights must be non-negative; higher-weight signals have a bigger impact on which server a player is matched to.

## Numbers
- [page](https://create.roblox.com/docs/matchmaking/glossary) Signal score range: **0 to 1** (Signal score after transformations; weights are non-negative)
- [page](https://create.roblox.com/docs/matchmaking/glossary) Server selection rule: **Highest server score** (Server score = weighted sum of signals; player joins highest)

## Topics
[[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
