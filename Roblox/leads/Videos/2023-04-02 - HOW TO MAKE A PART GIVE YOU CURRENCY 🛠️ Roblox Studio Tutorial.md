---
title: "HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Studio Tutorial"
url: https://youtu.be/H6LsbS_SA2w
creator: Itz_FloppyFish
official: false
advice_density: low
date: 2023-04-02
views: 135852
transcript: auto-captions
confidence: high
tags: [roblox, leads, youtube-learn]
---

# HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Studio Tutorial

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/H6LsbS_SA2w) | leads | 135,852 views | 2023-04-02

## Summary
Beginner Roblox Studio tutorial: creates a leaderstats currency via a ServerScriptService script, then builds a touchable coin part whose script awards currency and respawns after a set delay. Covers setup, value tuning, and testing with CanCollide disabled.

## Tips
- [0:28](https://youtu.be/H6LsbS_SA2w?t=28) **[[code-architecture-and-frameworks]]** Put the leaderstats-creating script in ServerScriptService so it runs on the server and sets up currency for every joining player.
- [1:44](https://youtu.be/H6LsbS_SA2w?t=104) **[[combat-and-gameplay-systems]]** Anchor the coin part and add a Script inside it; the script handles the touch pickup, currency award, and respawn timer.
- [2:26](https://youtu.be/H6LsbS_SA2w?t=146) **[[core-loops-and-game-design]]** Tune the respawn delay per coin (e.g. 5 seconds, or 120 for two minutes) to control how often the same collectible reappears.
- [3:04](https://youtu.be/H6LsbS_SA2w?t=184) **[[core-loops-and-game-design]]** Vary the reward value by area (e.g. 1 currency in area one, 10 in area two) to scale rewards as players progress.

## Numbers
- [2:26](https://youtu.be/H6LsbS_SA2w?t=146) Coin respawn time: **5 seconds (example); 120 seconds for two minutes** (Tutorial's example respawn delay setting in coin script)
- [3:04](https://youtu.be/H6LsbS_SA2w?t=184) Currency per coin: **1 (area one example); 10 (area two example)** (Reward value changed per area in the coin script)

## Tools
Roblox Studio, Explorer, Properties, ServerScriptService

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[testing-debugging-and-qa]]

Back to [[leads - How to make successful Roblox games]]
