---
title: "Docs: education / adventure-game-series / selling-items"
url: https://create.roblox.com/docs/education/adventure-game-series/selling-items.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / adventure-game-series / selling-items

[Open](https://create.roblox.com/docs/education/adventure-game-series/selling-items.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial for the Adventure Game series: building a sell platform part with a Touched-event script that reads a player's leaderstats Items and Gold values, converts items to gold at 100 per item, and resets items to 0.

## Tips
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) **[[first-session-onboarding]]** Make sure names in FindFirstChild() exactly match the names used in your PlayerSetup script (e.g. 'Rubies' vs 'Gold') or lookups silently return nil.
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) **[[scripting-and-performance]]** Always reset the items value to 0 after paying out; otherwise the touch script keeps granting gold on every touch.
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) **[[scripting-and-performance]]** Guard each level of lookups with an if-check (player, leaderstats, items/gold) before reading or modifying values to avoid nil errors.
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) **[[scripting-and-performance]]** Use GetPlayerFromCharacter() on partTouched.Parent to map a touched character part back to its Player before changing leaderstats.
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) **[[testing-debugging-and-qa]]** Add a temporary print statement inside the touch handler to confirm the Touched event fires before adding logic.

## Numbers
- [page](https://create.roblox.com/docs/education/adventure-game-series/selling-items) Gold per item sold: **100** (Sell platform pays 100 Gold for each carried item in the tutorial game)

## Tools
Roblox Studio, Luau, leaderstats

## He points to
- Roblox Creator Docs: Adventure Game series (education)

## Topics
[[first-session-onboarding]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
