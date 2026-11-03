---
title: "Docs: education / adventure-game-series / collect-items"
url: https://create.roblox.com/docs/education/adventure-game-series/collect-items.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / adventure-game-series / collect-items

[Open](https://create.roblox.com/docs/education/adventure-game-series/collect-items.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs lesson on building a harvestable 3D item (crystal) with a CanHarvest BoolValue, adding a starter tool via StarterPack, and scripting Touched-based harvesting that increments a leaderboard Items stat, then resets the item after a wait.

## Tips
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[building-art-and-assets]]** Group multi-part items into a Model and anchor all parts so the harvestable item stays in place.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[scripting-and-performance]]** Use a BoolValue named CanHarvest inside the item as a state flag; check it with FindFirstChild before awarding anything.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[scripting-and-performance]]** Set canHarvest.Value = false immediately on harvest so one tool swing cannot award more than one item.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[combat-and-gameplay-systems]]** Cap collection with a check like playerItems.Value < playerSpaces.Value so players cannot exceed bag capacity.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[core-loops-and-game-design]]** Make harvested items disappear for a few seconds so players explore for more instead of re-clicking one object.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[client-server-and-remotes]]** Keep the item-awarding logic in a server Script inside the tool; the docs place it in the tool's Script, which runs on the server.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[common-mistakes]]** Ensure CanHarvest is a child of the touched part; the script only works if the flag sits directly under that part.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[common-mistakes]]** Put the tool in StarterPack, not Workspace, or it will not be equipped on spawn.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[common-mistakes]]** Use canHarvest.Value, not canHarvest = true; spell Transparency and CanCollide exactly.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[common-mistakes]]** The leaderstats names in FindFirstChild must match the IntValue names used in PlayerSetup exactly.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[development-process-and-speed]]** Start with a print statement to confirm Touched fires before writing the harvesting logic.
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) **[[optimization-and-streaming]]** Use task.wait for respawn timing; the docs suggest 5 seconds as a starting value to tune per game.

## Numbers
- [page](https://create.roblox.com/docs/education/adventure-game-series/collect-items) Harvest respawn delay: **5 seconds (suggested task.wait(5))** (Item disappears and becomes unharvestable, then reappears after the wait)

## Tools
Roblox Studio, Explorer, Output window, Luau, Marketplace, Insert from File

## He points to
- Roblox Creator Docs: Adventure game series, Collect items lesson

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
