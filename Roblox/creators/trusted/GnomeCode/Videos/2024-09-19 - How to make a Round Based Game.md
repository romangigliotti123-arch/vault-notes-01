---
title: "How to make a Round Based Game"
url: https://youtu.be/oEWoyT-GBZY
creator: GnomeCode
official: false
advice_density: medium
date: 2024-09-19
views: 82292
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Round Based Game

[Watch](https://youtu.be/oEWoyT-GBZY) | GnomeCode | 82,292 views | 2024-09-19

## Summary
Beginner tutorial building a round-based Roblox system: a looping server script with intermission and round countdowns, minimum player check, teleporting players to a spawn part in a random map cloned from ReplicatedStorage, and a client ScreenGui that reads workspace attributes to display status and timer. Teaches the basic round loop pattern, not a full game.

## Tips
- [0:35](https://youtu.be/oEWoyT-GBZY?t=35) **[[development-process-and-speed]]** Enable Output window before coding so errors are visible while building systems step by step.
- [1:15](https://youtu.be/oEWoyT-GBZY?t=75) **[[scripting-and-performance]]** Use ALL_CAPS names for constants like intermission and round time that you won't change at runtime.
- [3:22](https://youtu.be/oEWoyT-GBZY?t=202) **[[code-architecture-and-frameworks]]** Split round logic into functions (intermission, runGame, countdown) so the main while-true loop stays readable.
- [5:09](https://youtu.be/oEWoyT-GBZY?t=309) **[[matchmaking-and-teleport]]** Check player count against a minimum (e.g. 2) before starting a round; otherwise loop and show 'waiting for players'.
- [6:37](https://youtu.be/oEWoyT-GBZY?t=397) **[[building-and-level-design]]** Mark spawn positions with an invisible, anchored, non-collidable part named exactly 'spawn' in each map instead of hardcoding coordinates.
- [7:57](https://youtu.be/oEWoyT-GBZY?t=477) **[[scripting-and-performance]]** Skip characters that haven't loaded yet (player.Character nil) when teleporting, rather than erroring.
- [11:03](https://youtu.be/oEWoyT-GBZY?t=663) **[[building-and-level-design]]** Store maps in ReplicatedStorage and clone a random one into Workspace each round so player damage resets, then destroy it at round end.
- [14:05](https://youtu.be/oEWoyT-GBZY?t=845) **[[client-server-and-remotes]]** Use workspace attributes (status, clock) to pass simple server state to clients; RemoteEvents are optional for this. Connect GetAttributeChangedSignal and call the update function once at startup so the UI isn't stale.
- [14:05](https://youtu.be/oEWoyT-GBZY?t=845) **[[ui-ux-design]]** Uncheck ResetOnSpawn on the ScreenGui so the status label persists across respawns.

## Numbers
- [0:35](https://youtu.be/oEWoyT-GBZY?t=35) Intermission duration: **5 seconds** (Example constant in tutorial code)
- [1:15](https://youtu.be/oEWoyT-GBZY?t=75) Round duration: **10 seconds** (Example constant in tutorial code)
- [5:09](https://youtu.be/oEWoyT-GBZY?t=309) Minimum players to start: **2** (Example value in tutorial; changed to 1 for testing)

## Games
- **Desert / Exosap / Garden maps (tutorial examples, unnamed Roblox games)** [11:03](https://youtu.be/oEWoyT-GBZY?t=663): Map variants stored in ReplicatedStorage and cloned randomly per round; each contains a 'spawn' part.

## Tools
Roblox Studio, Luau, Workspace attributes, ScreenGui, TextLabel

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[development-process-and-speed]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[GnomeCode - How to make successful Roblox games]]
