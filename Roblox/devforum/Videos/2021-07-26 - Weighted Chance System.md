---
title: "Weighted Chance System"
url: https://devforum.roblox.com/t/weighted-chance-system/1373953
creator: Roblox DevForum
official: false
advice_density: low
date: 2021-07-26
views: 700
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Weighted Chance System

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/weighted-chance-system/1373953) | Roblox DevForum | 700 views | 2021-07-26

## Summary
Tutorial on building a weighted chance system in Luau for prize selection. Explains storing prizes with chances from 0-1 in a table, summing weights, scaling by 10 for math.random, then walking the table again to find the matching prize.

## Tips
- [page](https://devforum.roblox.com/t/weighted-chance-system/1373953) **[[core-loops-and-game-design]]** Weighted chance system: store prize chances in a table (0-1), sum them into Weight, roll math.random over that total, then iterate again to find the matching prize.
- [page](https://devforum.roblox.com/t/weighted-chance-system/1373953) **[[luau-language-and-types]]** Scale float chances by 10 (or a suitable multiplier) before calling math.random, since math.random only accepts integers.
- [page](https://devforum.roblox.com/t/weighted-chance-system/1373953) **[[player-psychology-and-game-feel]]** Higher chance values make a prize proportionally more likely to be rolled; weights are relative, so they need not sum to exactly 1.

## Numbers
- [page](https://devforum.roblox.com/t/weighted-chance-system/1373953) Scaling multiplier for math.random: **10** (Multiply float weights by 10 before math.random to produce integer range)

## Tools
Roblox Studio, Luau

## Topics
[[core-loops-and-game-design]] [[luau-language-and-types]] [[player-psychology-and-game-feel]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
