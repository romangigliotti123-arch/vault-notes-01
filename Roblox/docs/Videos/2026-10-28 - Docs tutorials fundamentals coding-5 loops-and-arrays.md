---
title: "Docs: tutorials / fundamentals / coding-5 / loops-and-arrays"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-5 / loops-and-arrays

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs tutorial on combining arrays with loops. Covers for loops over hard-coded part arrays with timed CanCollide/Transparency changes, wrapping in while true for repetition, and using GetChildren() with ipairs() to apply operations to every child of a folder.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) **[[scripting-and-performance]]** Use constants in ALL_CAPS at the top of the script (e.g. VANISH_RATE) so tunable values are easy to find and adjust.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) **[[testing-debugging-and-qa]]** Keep test delays small (e.g. 1.5s) while testing, then tune for final gameplay.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) **[[building-and-level-design]]** Anchor parts that are toggled CanCollide=false; unanchored parts fall through the baseplate.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) **[[testing-debugging-and-qa]]** If first parts vanish before the player loads, add a small initial task.wait(2) at script start.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) Example VANISH_RATE: **1.5 seconds (testing); 1.0 in finished version** (Delay between each part disappearing in the sample bridge script)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/loops-and-arrays) Example reset wait: **1 second** (Pause before the path reappears in the sample loop)

## Tools
Roblox Studio, Luau

## Topics
[[building-and-level-design]] [[luau-language-and-types]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
