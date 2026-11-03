---
title: "Lerping - How To Move Parts Without TweenService"
url: https://youtu.be/R-xurNJtx7M
creator: GnomeCode
official: false
advice_density: low
date: 2022-12-15
views: 66215
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Lerping - How To Move Parts Without TweenService

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/R-xurNJtx7M) | GnomeCode | 66,215 views | 2022-12-15

## Summary
Tutorial on moving parts in Roblox via CFrame lerping instead of TweenService. Covers CFrame:Lerp with an alpha value, a for-loop with task.wait, and a RunService.Heartbeat loop using deltaTime and elapsed time, plus changing the target mid-movement.

## Tips
- [2:29](https://youtu.be/R-xurNJtx7M?t=149) **[[scripting-and-performance]]** Use CFrame:Lerp(goal, alpha) to move parts; it gives control over partial movement without hand-calculating positions and rotations.
- [4:08](https://youtu.be/R-xurNJtx7M?t=248) **[[scripting-and-performance]]** Drive per-frame movement with RunService.Heartbeat rather than a for-loop with task.wait, and use deltaTime to track elapsed time.
- [6:09](https://youtu.be/R-xurNJtx7M?t=369) **[[scripting-and-performance]]** Compute alpha as elapsed time divided by total duration, then disconnect the Heartbeat connection once alpha reaches 1.
- [7:38](https://youtu.be/R-xurNJtx7M?t=458) **[[core-loops-and-game-design]]** Lerp lets you change the target mid-movement, which TweenService cannot do; use it for dynamic, on-the-fly motion.

## Numbers
- [0:21](https://youtu.be/R-xurNJtx7M?t=21) Movement distance in demo: **30 studs up** (Example part moved upward by CFrame offset)
- [5:29](https://youtu.be/R-xurNJtx7M?t=329) Tween duration in demo: **3 seconds** (Heartbeat-based lerp duration example)
- [4:49](https://youtu.be/R-xurNJtx7M?t=289) Heartbeat frame delta: **~0.01 seconds** (Approximate deltaTime per frame shown in output)

## Tools
Roblox Studio, RunService, TweenService, CFrame

## Topics
[[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[GnomeCode - How to make successful Roblox games]]
