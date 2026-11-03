---
title: "Docs: tutorials / curriculums / gameplay-scripting / add-rounds"
url: https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / gameplay-scripting / add-rounds

[Open](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on structuring gameplay into rounds in the sample laser tag game: start loop with score reset and team spawning, configurable objective via TEAM_SCORE_LIMIT, syncing team points separately from leaderboard, round-end results UI and audio, and resetting teams to the lobby with a 10-second intermission.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[core-loops-and-game-design]]** Track team points in a separate attribute store rather than only the Teams service, because a leaving player's contribution is deducted from team score on disconnect.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[core-loops-and-game-design]]** Set a clear round objective shown at the top of the screen so players know what the team must do to win.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[core-loops-and-game-design]]** Use rounds with clear start and finish points so players can measure progress and get periodic equal footing, especially in team games.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[core-loops-and-game-design]]** Keep the objective limit in a single shared config module so the UI and server both read the same value and can be tuned quickly.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[first-session-onboarding]]** Spawn new joiners into the team with the fewest players during a round, and keep lobby players sorted into balanced teams.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[player-psychology-and-game-feel]]** Give distinct victory or defeat feedback (UI text plus audio) on round end so winners and losers each get clear, different outcomes.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[retention-d1-d7]]** Use a short intermission (the tutorial uses 10 seconds) between rounds before restarting the loop.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[client-server-and-remotes]]** Send each client the winning team and their own team at round end, since the player's team is removed before the client can check it.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[client-server-and-remotes]]** Have the server compute the winner and fire a RemoteEvent to clients; clients only render the result UI and sound.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[core-loops-and-game-design]]** Reset all leaderboard and team points to zero at the start of each round loop before sorting players into teams.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[matchmaking-and-teleport]]** Control spawn access by toggling a neutral spawn's Neutral flag: disable it during active rounds and enable it when players return to the lobby.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) **[[common-mistakes]]** Do not rely on the default Teams scoring for round-based games, since it ties team score to current players and drops points when a scorer disconnects.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) Objective score limit (example): **3 points to win in sample; example test value 200**
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds) Intermission between rounds: **10 seconds**

## Games
- **Laser tag sample game (Roblox tutorial)**: Reference project for round structure: teams, objective prompt, point tracking, results UI, lobby reset.

## Tools
Roblox Studio, Luau

## He points to
- Roblox Creator Docs: Spawning and Respawning (Configure Spawn Locations)
- Roblox Creator Docs: UI Curriculum (Objective UI component)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[matchmaking-and-teleport]] [[player-psychology-and-game-feel]] [[retention-d1-d7]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
