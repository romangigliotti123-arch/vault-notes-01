---
title: "Docs: tutorials / use-case-tutorials / scripting / basic-scripting / deadly-lava"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / basic-scripting / deadly-lava

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on building a deadly lava floor with a script. Covers creating a Part, connecting to its Touched event, using a parameter to get the touching part, finding the Humanoid via its Character parent, and setting Health to 0 to kill the player.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava) **[[core-loops-and-game-design]]** Use lava or hazard floors as extra challenge in obbies or as world boundaries, per the tutorial's suggestion.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava) **[[client-server-and-remotes]]** Touched fires on the part; use otherPart.Parent then FindFirstChild('Humanoid') to reach the character before changing health.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava) **[[scripting-and-performance]]** Guard Humanoid lookups with an if check; Touched can fire for non-character parts, which have no Humanoid.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/deadly-lava) **[[scripting-and-performance]]** Connect events with colon syntax (lava.Touched:Connect(fn)), not dot syntax.

## Tools
Roblox Studio, Luau

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
