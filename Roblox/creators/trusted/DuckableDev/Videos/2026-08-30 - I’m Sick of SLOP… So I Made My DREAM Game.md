---
title: "I’m Sick of SLOP… So I Made My DREAM Game"
url: https://youtu.be/3XX3Y74hzq0
creator: Duckable
official: false
advice_density: low
date: 2026-08-30
views: 1670103
transcript: auto-captions
confidence: medium
tags: [roblox, duckabledev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I’m Sick of SLOP… So I Made My DREAM Game

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/3XX3Y74hzq0) | DuckableDev | 1,670,103 views | 2026-08-30

## Summary
Devlog of the creator building a Roblox Card Wars dream game demo. Covers rapid prototyping with clone helpers, card systems (frame, abilities, triggers), bot AI with play styles, scope overwhelm, assembling a 11-person dev team via Discord, matchmaking (PvE/PvP/ranked queue) and a near-playable demo. Little concrete Roblox growth advice.

## Tips
- [2:44](https://youtu.be/3XX3Y74hzq0?t=164) **[[client-server-and-remotes]]** Keep game state on the server and send visual updates to each client instead of spawning boards for everyone on the server; only two players use each board.
- [4:05](https://youtu.be/3XX3Y74hzq0?t=245) **[[testing-debugging-and-qa]]** Build a playtest bot early to exercise placement and attacks; the creator went hours without a playtest and hit errors late.
- [6:52](https://youtu.be/3XX3Y74hzq0?t=412) **[[building-art-and-assets]]** Put repeated character animation code into one reusable animator module rather than duplicating it into every character model.
- [10:24](https://youtu.be/3XX3Y74hzq0?t=624) **[[code-architecture-and-frameworks]]** Use a data-driven ability system with named event triggers (on ally enter, turn start, attacked) so new cards are added by data, not new code.

## Numbers
- [0:00](https://youtu.be/3XX3Y74hzq0?t=0) Previous attempts at this game: **12 failed attempts over ~6 years**
- [18:33](https://youtu.be/3XX3Y74hzq0?t=1113) Dev team applications: **200 submissions narrowed to 11**
- [2:44](https://youtu.be/3XX3Y74hzq0?t=164) Time to first playable loop: **about 8 hours**
- [16:31](https://youtu.be/3XX3Y74hzq0?t=991) Time spent in honeymoon phase before slowdown: **about 1 week of slowed progress**

## Games
- **Adventure Time Card Wars** [0:40](https://youtu.be/3XX3Y74hzq0?t=40): Childhood inspiration; removed from App Store in 2020, motivating the creator's remake.
- **Blocks (card game)** [11:06](https://youtu.be/3XX3Y74hzq0?t=666): Referenced as a card design influence alongside Adventure Time Card Wars.
- **Roblox Card Wars (creator's game)** [23:59](https://youtu.be/3XX3Y74hzq0?t=1439): Dream-game remake in progress, demo with PvE/PvP/ranked queue; not yet released.

## Tools
Roblox Studio, Luau

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[community-and-discord]] [[development-process-and-speed]] [[mindset-and-strategy]] [[scripting-and-performance]] [[team-and-budget]] [[testing-debugging-and-qa]]

Back to [[DuckableDev - How to make successful Roblox games]]
