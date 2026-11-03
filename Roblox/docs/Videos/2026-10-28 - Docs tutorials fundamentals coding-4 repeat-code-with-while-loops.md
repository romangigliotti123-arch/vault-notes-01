---
title: "Docs: tutorials / fundamentals / coding-4 / repeat-code-with-while-loops"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-4 / repeat-code-with-while-loops

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on while loops in Luau. Walks through creating a LoopingPart, storing it in a local variable, writing a while true do loop that alternates Color3.fromRGB values with task.wait(3), and troubleshooting common issues. Covers loop syntax, scope, and indentation.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) **[[luau-language-and-types]]** Store frequently used references like workspace.LoopingPart in a local variable instead of retyping the full path each time.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) **[[luau-language-and-types]]** Indent instructions inside loops always; it makes code easier to read and keeps scope clear.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) **[[scripting-and-performance]]** Put a task.wait() between repeated actions in a loop; without it, changes happen too fast to see and the loop can run without yielding.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) **[[scripting-and-performance]]** Make sure wait values are greater than 1 second in visual loops, since very short waits can hide intermediate states.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) RGB range: **0 to 255 per channel** (Color3.fromRGB accepts whole or decimal values in this range)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/repeat-code-with-while-loops) Example wait duration: **3 seconds** (task.wait(3) used between color changes in the tutorial)

## Tools
Roblox Studio, Luau, task library

## Topics
[[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
