---
title: "Docs: tutorials / fundamentals / coding-3 / traps-with-if-statements"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-3/traps-with-if-statements.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-3 / traps-with-if-statements

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/traps-with-if-statements.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs lesson on building a damage trap part. Uses Touched event, FindFirstChildWhichIsA("Humanoid"), and an if statement to set a player's Humanoid.Health to 0 only when a Humanoid is touched. Notes flaws: NPCs also have Humanoids, and setting health to 0 is all-or-nothing.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/traps-with-if-statements) **[[core-loops-and-game-design]]** Check for a Humanoid before acting on a touched part so decor is ignored; touched parts may be a limb or accessory, so check otherPart.Parent for the Humanoid.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/traps-with-if-statements) **[[client-server-and-remotes]]** Note that Humanoids also exist on NPCs, so a Humanoid check alone will also affect non-player characters; filter further if only players should be hit.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/traps-with-if-statements) **[[scripting-and-performance]]** Use FindFirstChildWhichIsA("Humanoid") to locate a Humanoid by class rather than by name.

## Tools
Roblox Studio, Luau

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
