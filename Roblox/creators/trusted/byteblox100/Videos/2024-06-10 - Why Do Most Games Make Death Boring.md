---
title: "Why Do Most Games Make Death Boring?"
url: https://youtu.be/_rksdF5JoHo
creator: ByteBlox
official: false
advice_density: medium
date: 2024-06-10
views: 60807
transcript: auto-captions
confidence: medium
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Why Do Most Games Make Death Boring?

[Watch](https://youtu.be/_rksdF5JoHo) | byteblox100 | 60,807 views | 2024-06-10

## Summary
Speaker argues most Roblox games treat death as a plain health-hits-zero reset and proposes three alternatives: a shared team health pool, ghost/state-switch deaths that grant new abilities, and death loops where knowledge carries over between lives (Outer Wilds, Undertale style). Includes a live Studio script for the shared pool and a ghost-revive demo.

## Tips
- [0:41](https://youtu.be/_rksdF5JoHo?t=41) **[[core-loops-and-game-design]]** Make death meaningful: harsh-but-fair death makes the risk-taking before it interesting, as in Minecraft. Trivial respawns remove the tension that gives earlier play its stakes.
- [1:32](https://youtu.be/_rksdF5JoHo?t=92) **[[combat-and-gameplay-systems]]** Try a shared team health pool: players keep individual HP but damage drains one team bar (e.g. 200 total); everyone dies when it hits zero. Offer an opt-out for players who want individual health.
- [2:53](https://youtu.be/_rksdF5JoHo?t=173) **[[scripting-and-performance]]** Use Players' Humanoid HealthChanged via GetPropertyChangedSignal('Health') to react to damage. Use GetDescendants() instead of GetChildren() when you need nested parts.
- [4:56](https://youtu.be/_rksdF5JoHo?t=296) **[[scripting-and-performance]]** Reset Humanoid.Health to MaxHealth inside the health-changed handler, with an early return when the pool is depleted. Health events fire before the death check, so this keeps characters alive while the pool drains.
- [16:04](https://youtu.be/_rksdF5JoHo?t=964) **[[client-server-and-remotes]]** Wait for the character with player.CharacterAdded before reading character parts. Code that works on the server can fail on the client because the character loads at a different time.
- [9:02](https://youtu.be/_rksdF5JoHo?t=542) **[[combat-and-gameplay-systems]]** Add respawn limits as a mode mechanic: give each player a fixed number of respawns (e.g. 10) and make the team lose when the pool is exhausted, as in Brawl Stars knockout.
- [11:16](https://youtu.be/_rksdF5JoHo?t=676) **[[core-loops-and-game-design]]** Give dead players something to do: ghost states that unlock abilities or new interactions keep them playing 24/7 instead of waiting for respawn. Roblox games should always have an activity available.
- [14:01](https://youtu.be/_rksdF5JoHo?t=841) **[[scripting-and-performance]]** Keep Studio scripts small and test each change in play mode; the speaker shows that client and server behave differently for the same code.
- [19:31](https://youtu.be/_rksdF5JoHo?t=1171) **[[core-loops-and-game-design]]** Consider a death-loop structure: death resets the world but keeps the player's knowledge, so later runs go further. Outer Wilds and Undertale show this, and Doors teaches cues through death.
- [22:54](https://youtu.be/_rksdF5JoHo?t=1374) **[[core-loops-and-game-design]]** Store player knowledge in a persistent ship-log-style UI so information gained across loops stays visible and players can solve clues without re-reading everything.
- [24:56](https://youtu.be/_rksdF5JoHo?t=1496) **[[combat-and-gameplay-systems]]** Respawn immediately only when a shared-health or other fairness mechanic prevents the enemy team from being punished unfairly; otherwise add a short respawn wait.

## Numbers
- [0:00](https://youtu.be/_rksdF5JoHo?t=0) Shared health pool example: **100 HP per player, 200 total pool for two players**
- [5:37](https://youtu.be/_rksdF5JoHo?t=337) Health pool tick interval: **0.5 seconds (task.wait(0.5) debug print)**
- [9:02](https://youtu.be/_rksdF5JoHo?t=542) Respawn cap example: **10 free respawns before team loses (knockout mode)**
- [17:25](https://youtu.be/_rksdF5JoHo?t=1045) Ghost state visuals and speed: **Transparency 0.6 on parts except HumanoidRootPart; WalkSpeed +30**
- [18:46](https://youtu.be/_rksdF5JoHo?t=1126) Ghost lives before permanent death: **Speaker suggests ~3 ghost cycles before a real death**

## Games
- **Minecraft** [0:00](https://youtu.be/_rksdF5JoHo?t=0): Harsh death makes the buildup and risk meaningful; hardcore mode shows permanent death works when the stakes are clear.
- **Blade Ball** [12:38](https://youtu.be/_rksdF5JoHo?t=758): Always give players something to do between matches: training, chests, spinning, emotes, server hopping.
- **Outer Wilds** [19:31](https://youtu.be/_rksdF5JoHo?t=1171): Death resets the world but keeps knowledge; the first loop can already contain the answers, so the loop design rewards learning.
- **Doors** [20:12](https://youtu.be/_rksdF5JoHo?t=1212): Dying teaches the player what cues like flickering lights mean, turning deaths into lessons.
- **Undertale** [24:16](https://youtu.be/_rksdF5JoHo?t=1456): Boss deaths return the player to the start with new knowledge, a loop structure that works outside shooters.
- **Overwatch** [11:57](https://youtu.be/_rksdF5JoHo?t=717): Hammond the hamster leaving the dead mech shows players enjoy post-death actions; the idea can be adapted.

## Tools
Roblox Studio, Luau, Output/print debugging, Humanoid events (HealthChanged, GetPropertyChangedSignal)

## He points to
- Outer Wilds
- Undertale
- Doors
- Minecraft
- Blade Ball
- Brawl Stars

## Quotes
- [0:41](https://youtu.be/_rksdF5JoHo?t=41) "if death wasn't such a punishment well then all of the risks that you take while you're alive don't feel that interesting"
- [11:16](https://youtu.be/_rksdF5JoHo?t=676) "you want your game to be played 24/7 ... you want people to continuously have something to do"

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[byteblox100 - How to make successful Roblox games]]
