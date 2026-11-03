---
title: "I Tried Remaking My First Game, 9 Years Later"
url: https://youtu.be/LC8AV8Yy6Z4
creator: Roox4
official: false
advice_density: low
date: 2024-11-01
views: 1968242
transcript: auto-captions
confidence: high
tags: [roblox, roox4official, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I Tried Remaking My First Game, 9 Years Later

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/LC8AV8Yy6Z4) | Roox4Official | 1,968,242 views | 2024-11-01

## Summary
Developer remakes his 2015 Roblox destruction game (rocket launcher, destructible everything, last-man-standing). Covers Humanoid momentum problems and a custom controller for rocket jumps, splitting walls into blocks for destruction, welding for structural collapse, AI bots for testing (hard to build), and faith-plate movement. Mostly a devlog.

## Tips
- [1:20](https://youtu.be/LC8AV8Yy6Z4?t=80) **[[scripting-and-performance]]** Humanoid can override applied forces (rocket jump momentum bled away mid-air). If physics-driven movement matters, build a custom character controller instead.
- [3:07](https://youtu.be/LC8AV8Yy6Z4?t=187) **[[building-and-level-design]]** For destructible walls, build them from many smaller blocks rather than one part so projectiles can carve holes.
- [3:48](https://youtu.be/LC8AV8Yy6Z4?t=228) **[[development-process-and-speed]]** Unanchored destruction needs every block welded to its neighbours; welding hundreds of parts manually is too slow, so script it. Keep the algorithm fast or run it offline.
- [5:11](https://youtu.be/LC8AV8Yy6Z4?t=311) **[[testing-debugging-and-qa]]** Making AI bots that simulate players is harder than expected; overpowered bots are easy, realistic aim and movement are not. Playtest with real people where possible.

## Numbers
- [0:00](https://youtu.be/LC8AV8Yy6Z4?t=0) Video views: **1968242** (Views of this remake devlog video at time of extraction)
- [3:48](https://youtu.be/LC8AV8Yy6Z4?t=228) Offline block-welding algorithm freeze: **~5 seconds** (Freezes developer's computer while running the welding algorithm)

## Games
- **Destroy the Neighborhood** [0:00](https://youtu.be/LC8AV8Yy6Z4?t=0): Inspiration: a rocket-launcher destruction game where everything (houses, cars, furniture, crane) is destructible.

## Tools
Roblox Studio

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roox4Official - How to make successful Roblox games]]
