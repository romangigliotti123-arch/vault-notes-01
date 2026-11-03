---
title: "Docs: resources / battle-royale / core-scripts"
url: https://create.roblox.com/docs/resources/battle-royale/core-scripts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / core-scripts

[Open](https://create.roblox.com/docs/resources/battle-royale/core-scripts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Battle Royale template docs on core scripts: server/client core loop scripts, InitialSetup preloading, stage-based GameStageHandler/StageManager architecture, and the three place roles (Lobby, Queue, Gameplay) with a 3:00 queue countdown.

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) **[[code-architecture-and-frameworks]]** Organise game flow as discrete stages; on stage change, call shutdown on the old stage handler before initialising the new one to avoid overlapping systems.
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) **[[matchmaking-and-teleport]]** Split a battle royale across places by role: Lobby for mode selection, Queue for gathering players, Gameplay for the match, so each server only runs what it needs.
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) **[[first-session-onboarding]]** Preload required assets on the client before gameplay starts (the template uses an AssetPreloads config) so players don't hit missing-asset delays mid-match.
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) **[[code-architecture-and-frameworks]]** Keep stage lists in a single config module (e.g. MainConfiguration) mapping each gameplay mode to its ordered stages, so modes are changed without editing stage code.
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) **[[matchmaking-and-teleport]]** In queue places, start a countdown once the minimum player count is reached rather than starting immediately; the template uses a 3:00 countdown.

## Numbers
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) Queue countdown: **3:00 minutes after minimum players reached** (Battle Royale template queue place default configuration)
- [page](https://create.roblox.com/docs/resources/battle-royale/core-scripts) Place roles: **3 (Lobby, Queue, Gameplay)** (Battle Royale template place role structure)

## Games
- **Roblox Battle Royale (template)**: Template splits match flow into Lobby, Queue and Gameplay places, with stage handlers swapped per game stage on server and client.

## Tools
Roblox Studio, Luau

## He points to
- Roblox Battle Royale template (ServerScriptService/Server, StarterPlayerScripts/Client, ReplicatedFirst/InitialSetup)

## Topics
[[code-architecture-and-frameworks]] [[first-session-onboarding]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
