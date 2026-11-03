---
title: "Docs: tutorials / fundamentals / coding-3 / powerups-with-if-statements"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-3 / powerups-with-if-statements

[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on using the `and` operator in if statements to build a touch-activated WalkSpeed powerup. Covers Touched events, Humanoid detection, capping speed with a condition, and using CanTouch plus task.wait to prevent repeated triggers.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) **[[scripting-and-performance]]** Combine conditions with `and` (e.g. `if humanoid and humanoid.WalkSpeed <= 50`) so stacking effects is capped and cannot grow unbounded.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) **[[scripting-and-performance]]** Touched fires on every step or bounce; disable the trigger with CanTouch=false after applying an effect to prevent repeated application.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) **[[scripting-and-performance]]** Use character:FindFirstChildWhichIsA("Humanoid") on otherPart.Parent to verify a touched part belongs to a character before acting.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) **[[core-loops-and-game-design]]** Limit repeated power-ups with a cooldown (task.wait(1) then re-enable) so players get a controlled, rewarding boost instead of runaway stats.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) WalkSpeed boost increment: **+10 per touch** (Example powerup adds 10 to Humanoid.WalkSpeed on each touch)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) WalkSpeed cap condition: **<= 50 (max 60 after boost)** (Boost only applies if current WalkSpeed is 50 or less)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) Cooldown: **1 second** (task.wait(1) before re-enabling CanTouch)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/powerups-with-if-statements) WalkSpeed range/default: **default 16, max 100 in finished script** (Values suggested to be tuned in finished script)

## Tools
Roblox Studio, Luau

## Topics
[[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
