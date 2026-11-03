---
title: "Docs: education / battle-royale-series / coding-the-game-loop"
url: https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / battle-royale-series / coding-the-game-loop

[Open](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Education docs lesson on coding a battle royale game loop: GameSettings and MatchManager module scripts, a GameManager server script with a while-true loop containing a nested repeat loop for intermission, and testing with a 2-player local server.

## Tips
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[development-process-and-speed]]** Organise logic as ServerStorage module scripts (GameSettings, MatchManager) required by one ServerScriptService GameManager that runs the main loop.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[core-loops-and-game-design]]** Split the battle royale game loop into three phases: intermission, competition, and cleanup & reset, all inside one main while loop.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[scripting-and-performance]]** Keep task.wait() inside repeat loops; without it the loop runs too many times per second and overloads Studio.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[scripting-and-performance]]** Set intermissionDuration above 1 second; shorter values make the wait loop repeat too often and cause slowdown.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[scripting-and-performance]]** Use a repeat...until loop for intermission so the lobby always runs at least once before checking player count.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[scripting-and-performance]]** Keep all game-loop code inside the while true do block; code placed after it never runs.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[testing-debugging-and-qa]]** Test multi-player logic with Test > Start Test Session > Server and Clients (2 players); single-player playtest never passes a minimumPlayers of 2.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[testing-debugging-and-qa]]** If test prints are missing, confirm the module is required in GameManager and the function is added to the module table.
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) **[[development-process-and-speed]]** Start with rough guessed values in GameSettings (e.g. intermission 5s, match 10s, min players 2, transition 5s) and tune them during testing.

## Numbers
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) Intermission duration (example): **5 seconds** (GameSettings example value in tutorial)
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) Match duration (example): **10 seconds** (GameSettings example value; tutorial says take best guess)
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) Minimum players (example): **2** (Smallest player count to start a match in tutorial)
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) Transition time (example): **5 seconds** (Delay before and after match to smooth transitions)
- [page](https://create.roblox.com/docs/education/battle-royale-series/coding-the-game-loop) Local test players: **2** (Players used in Server and Clients local test session)

## Tools
Roblox Studio, Luau

## He points to
- Firewall and Router Issues article (Roblox docs)

## Topics
[[core-loops-and-game-design]] [[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
