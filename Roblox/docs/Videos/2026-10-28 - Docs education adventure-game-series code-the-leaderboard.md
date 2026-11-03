---
title: "Docs: education / adventure-game-series / code-the-leaderboard"
url: https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / adventure-game-series / code-the-leaderboard

[Open](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox education docs tutorial on building a basic leaderboard via a server script in ServerScriptService. Covers creating a leaderstats Folder on PlayerAdded, and adding Gold, Items, and Spaces IntValues with starting values. Notes that data isn't saved between sessions (requires DataStores).

## Tips
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[scripting-and-performance]]** Name the leaderboard container exactly "leaderstats" (case-sensitive); other names like "leaderboard" won't create a built-in leaderboard.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[scripting-and-performance]]** Create the leaderstats Folder and parent it to the player inside a Players.PlayerAdded handler so every joining player gets a leaderboard.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[scripting-and-performance]]** Use IntValue objects parented to leaderstats for each stat; the IntValue Name is what players see on the leaderboard.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[scripting-and-performance]]** Set IntValue numbers via .Value (e.g. gold.Value = 10), not by reassigning the object.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[data-persistence]]** Leaderboard stats created this way are not saved between sessions; use DataStores to persist player data.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[combat-and-gameplay-systems]]** Start limiting resources low (e.g. bag Spaces = 2) so players are motivated to buy upgrades early.
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) **[[first-session-onboarding]]** Keep the stat names and spelling exact and documented in the game design doc, since other scripts reference them.

## Numbers
- [page](https://create.roblox.com/docs/education/adventure-game-series/code-the-leaderboard) Starting Spaces value: **2** (Bag capacity at game start, encouraging early bag purchase)

## Tools
Roblox Studio, Luau, Players service, IntValue, Folder

## He points to
- Roblox Creator Docs: DataStores (mentioned as advanced topic)

## Topics
[[combat-and-gameplay-systems]] [[data-persistence]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
