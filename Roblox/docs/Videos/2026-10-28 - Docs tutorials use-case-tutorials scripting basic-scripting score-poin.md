---
title: "Docs: tutorials / use-case-tutorials / scripting / basic-scripting / score-points"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / basic-scripting / score-points

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial building a survival-style points game: platforms plus lava, a leaderstats folder with an IntValue Points counter, a server loop awarding 1 point per second, and per-player IsAlive attribute gating. Points reset to 0 on Humanoid.Died.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[scripting-and-performance]]** Put scripts that set up game state in ServerScriptService so they run automatically when the game starts.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[scripting-and-performance]]** Name the service variable exactly as the service (e.g. local Players = game:GetService("Players")) per Roblox convention.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[scripting-and-performance]]** Name the leaderstats folder exactly "leaderstats"; the leaderboard silently fails otherwise.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[client-server-and-remotes]]** Award points and track state on the server; player attributes and IntValues replicate to clients for display.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[scripting-and-performance]]** Use WaitForChild on the Character to safely wait for Humanoid before connecting Died, since model contents assemble at spawn.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[common-mistakes]]** Gate score accrual with a per-player alive flag so dead players stop earning points; a score that keeps counting while dead undermines the game.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[core-loops-and-game-design]]** Frame the game as a competitive survival loop: score per second alive, reset on death, so players compete for the highest score.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) **[[core-loops-and-game-design]]** Add a lobby to teleport users in together, and announce round winners, to improve multiplayer rounds.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/score-points) Points award interval: **1 point per second alive** (Tutorial's scoring tick: task.wait(1) loop awards +1 to alive players)

## Tools
Roblox Studio, Luau, Leaderboard (leaderstats)

## He points to
- Roblox Creator Docs: Score points tutorial

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
