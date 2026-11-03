---
title: "Docs: tutorials / use-case-tutorials / scripting / basic-scripting / fading-trap"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / basic-scripting / fading-trap

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial showing how to build a platform that fades out when touched, then reappears, using a for loop for transparency, CanCollide toggling, and a boolean debounce variable to prevent repeated Touched triggers.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[core-loops-and-game-design]]** Make fading platforms fade gradually before becoming passable so players have a chance to jump off instead of feeling cheated.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[scripting-and-performance]]** Use a for loop for repetitive property changes instead of writing many repeated lines; a 10-step fade needs one loop, not 20 lines.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[scripting-and-performance]]** Debounce Touched-triggered functions with a boolean flag, since Touched fires on every body part contact and would otherwise restart the effect repeatedly.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[common-mistakes]]** Don't leave Touched-connected functions unguarded; without a debounce, running across the platform resets the fade loop each time.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[genre-mechanics]]** Duplicate fading platforms across wider gaps and adjust fade speed to tune obstacle difficulty.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) **[[retention-d1-d7]]** Restore the platform a few seconds after it fades so players who fail can retry the jump.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) Fade steps: **10 steps of 0.1s each (1 second total fade)** (Transparency loop from count/10 with task.wait(0.1))
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap) Platform gone duration: **3 seconds with CanCollide false before reappearing** (Example timing in the fade tutorial code)

## Games
- **Deadly Lava**: Prerequisite tutorial that teaches triggering code from user behavior; fading platform is placed above its lava floor.

## Tools
Roblox Studio, Luau

## He points to
- Deadly Lava tutorial

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[genre-mechanics]] [[retention-d1-d7]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
