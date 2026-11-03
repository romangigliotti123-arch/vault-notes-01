---
title: "Docs: education / adventure-game-series / buying-upgrades"
url: https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / adventure-game-series / buying-upgrades

[Open](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial for the final stage of an adventure/harvest game loop: build a SurfaceGUI shop sign with a ClickDetector, then deduct gold and increase the player's Spaces (item bag capacity) via leaderstats IntValues with a server script.

## Tips
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[scripting-and-performance]]** Use FindFirstChild with exact string names matching the PlayerSetup leaderstats IntValues (e.g. "Gold", "Spaces"); mismatched names silently break upgrades.
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[scripting-and-performance]]** Check that both currency and capacity values exist and that gold is at least the cost before subtracting, to avoid negative balances.
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[ui-ux-design]]** For SurfaceGUI sign text, set TextScaled on, use 0.5 scale and 0.5 anchor/position to center the label, and include the price in the text.
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[ui-ux-design]]** Set ClickDetector MaxActivationDistance on buttons so players can interact from a sensible distance.
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[client-server-and-remotes]]** Keep purchase logic in a server Script attached to the button; the ClickDetector MouseClick event passes the player who clicked.
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) **[[core-loops-and-game-design]]** Close the core loop with a purchasable upgrade (bigger bag) that increases harvest per trip and therefore gold earned.

## Numbers
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) Upgrade cost (tutorial value): **100 gold** (Example upgrade price in the tutorial script)
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) Spaces added per upgrade (tutorial value): **10** (Example newSpaces value in the tutorial script)
- [page](https://create.roblox.com/docs/education/adventure-game-series/buying-upgrades) SurfaceGUI label scale: **0.5 X and Y** (Scale used to size and center the sign text label)

## Tools
Roblox Studio, SurfaceGUI, ClickDetector, Luau script, leaderstats IntValues

## He points to
- PlayerSetup script (referenced tutorial step, not linked)

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
