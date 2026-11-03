---
title: "Get a BUY AND SELL system like Dead Rails!"
url: https://youtu.be/kVtEBqvw5F4
creator: PineappleDev
official: false
advice_density: medium
date: 2025-04-11
views: 6414
transcript: auto-captions
confidence: medium
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Get a BUY AND SELL system like Dead Rails!

[Watch](https://youtu.be/kVtEBqvw5F4) | pineappledevv | 6,414 views | 2025-04-11

## Summary
Tutorial on building a Dead Rails-style buy and sell system using a plugin's shop system. Covers importing the module/folders into ReplicatedStorage, ServerScriptService and Workspace, setting up sell tables (sellable items drop money bags), adding buy tables (purchase name must match item name, price set in shop data), and disabling auto-spawn. Requires the carry/weld item system tutorial first.

## Tips
- [0:14](https://youtu.be/kVtEBqvw5F4?t=14) **[[development-process-and-speed]]** Install the item drag/weld system first; the buy/sell system depends on the carry weld system from the previous tutorial.
- [1:25](https://youtu.be/kVtEBqvw5F4?t=85) **[[scripting-and-performance]]** Delete the plugin's default item setup script and replace it with the custom one so money bags and coal get set up correctly.
- [3:15](https://youtu.be/kVtEBqvw5F4?t=195) **[[building-and-level-design]]** Sell tables work via hitboxes; place hitboxes where the sell area should be. Tables can be duplicated freely.
- [3:15](https://youtu.be/kVtEBqvw5F4?t=195) **[[scripting-and-performance]]** To sell an item, set its Sellable attribute/value to true and give it a value; sold items drop a money bag worth that value.
- [4:34](https://youtu.be/kVtEBqvw5F4?t=274) **[[scripting-and-performance]]** Buy-table purchase names must exactly match the item name in ReplicatedStorage, and the shop data entry key must match too.
- [5:14](https://youtu.be/kVtEBqvw5F4?t=314) **[[monetisation-other]]** Set each buyable item's price in the shop data module (example used: apple at $10, resold for $50 showing the margin loop).
- [6:37](https://youtu.be/kVtEBqvw5F4?t=397) **[[development-process-and-speed]]** When adding a new item, call the item setup function with its data and object so it works with the buy/sell system.
- [6:37](https://youtu.be/kVtEBqvw5F4?t=397) **[[development-process-and-speed]]** Duplicate buy tables to add more shops; they work immediately when the purchase name and shop data are correct.

## Numbers
- [1:56](https://youtu.be/kVtEBqvw5F4?t=116) Sell payout example: **$20 money bag for sold coal test item** (Sold item drops money bag claimable for 20 money)
- [5:54](https://youtu.be/kVtEBqvw5F4?t=354) Buy price example: **$10 apple** (Shop data price set to 10, apple resold for $50 in video)

## Games
- **Dead Rails** [0:00](https://youtu.be/kVtEBqvw5F4?t=0): Inspiration for the buy and sell mechanic: sell items at a station, then buy items from shop tables.

## Tools
Roblox Studio, plugin with item system, shop system, and sell system

## He points to
- Previous video on carry weld/item dragging system (linked in description)

## Topics
[[building-and-level-design]] [[development-process-and-speed]] [[monetisation-other]] [[scripting-and-performance]]

Back to [[pineappledevv - How to make successful Roblox games]]
