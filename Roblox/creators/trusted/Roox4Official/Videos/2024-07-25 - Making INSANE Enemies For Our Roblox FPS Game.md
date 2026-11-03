---
title: "Making INSANE Enemies For Our Roblox FPS Game"
url: https://youtu.be/OYfrdTxNdjA
creator: Roox4
official: false
advice_density: low
date: 2024-07-25
views: 235170
transcript: auto-captions
confidence: medium
tags: [roblox, roox4official, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Making INSANE Enemies For Our Roblox FPS Game

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/OYfrdTxNdjA) | Roox4Official | 235,170 views | 2024-07-25

## Summary
Devlog for a physics-based Roblox FPS. Covers building a shotgun and sniper with a realistic scope-zoom (view model aligned to camera), replacing custom enemy suspension with real Roblox springs and wheels after precision issues on small enemies, turret targeting with align constraints, and a giant Titan enemy with a stomp mechanic and laser. Mostly entertainment/experiment.

## Tips
- [2:42](https://youtu.be/OYfrdTxNdjA?t=162) **[[scripting-and-performance]]** When offsetting viewmodels/cframes, check whether offsets are in object space or world space; mixing them broke the scope alignment until made relative to the camera.
- [2:51](https://youtu.be/OYfrdTxNdjA?t=171) **[[physics-pathfinding-and-npc-ai]]** Custom spring math for enemy suspension lost numerical precision on small, fast enemies; using engine-native constraints (real Springs on wheels) fixed it.
- [4:55](https://youtu.be/OYfrdTxNdjA?t=295) **[[building-and-level-design]]** Automate attaching parts/wheels to many enemies with a module instead of manual assignment.
- [5:37](https://youtu.be/OYfrdTxNdjA?t=337) **[[playtesting-and-feedback]]** Stress-test physics systems by dropping enemies off cliffs and onto terrain to find breakage early.

## Numbers
- [3:32](https://youtu.be/OYfrdTxNdjA?t=212) Enemy suspension: **4 invisible springs per enemy** (Custom spring calc broke on small enemies due to precision loss)
- [8:17](https://youtu.be/OYfrdTxNdjA?t=497) Laser damage: **5 damage per hit** (Titan enemy laser beam damage per tick)
- [5:37](https://youtu.be/OYfrdTxNdjA?t=337) Suspension rework time: **a few days** (Time spent fixing enemy suspension system)

## Tools
Roblox Studio, Luau

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[player-psychology-and-game-feel]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[Roox4Official - How to make successful Roblox games]]
