---
title: "Docs: tutorials / fundamentals / coding-4 / intro-to-for-loops"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-4 / intro-to-for-loops

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs tutorial on for loops in Luau. Explains control, end, and increment values, the step-by-step logic of iterations, and builds a countdown script in ServerScriptService. Covers negative increments, default increment of 1, and why loops starting beyond the end value never run.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) **[[luau-language-and-types]]** Use a for loop when code should run a fixed number of times; the loop takes control, end, and increment values separated by commas.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) **[[luau-language-and-types]]** Increment defaults to 1 if omitted. Use a negative increment (e.g. -1) to count down from a higher start to a lower end.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) **[[luau-language-and-types]]** Ensure the start value is not beyond the end value for the direction of counting, or the loop will not run at all.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) **[[luau-language-and-types]]** Use task.wait(1) inside loops that should pause between iterations; without a wait, all prints appear at once.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) Countdown iterations: **11 iterations for a loop from 10 to 0 inclusive** (Countdown example with control 10, end 0, increment -1)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/intro-to-for-loops) Minimum wait for visible countdown: **1 second (task.wait(1))** (Troubleshooting note on loops printing all at once)

## Tools
Roblox Studio, Luau, ServerScriptService

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
