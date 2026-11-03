---
title: "Get an Item System like DEAD RAILS! (Welding, Item Data, UI)"
url: https://youtu.be/ntHgQBEVERE
creator: PineappleDev
official: false
advice_density: medium
date: 2025-03-29
views: 15951
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Get an Item System like DEAD RAILS! (Welding, Item Data, UI)

[Watch](https://youtu.be/ntHgQBEVERE) | pineappledevv | 15,951 views | 2025-03-29

## Summary
Tutorial on building a Dead Rails-style item drag/carry system in Roblox Studio: importing a carry plugin, setting up folders, creating welded item models with item data, adding item UI tags, and detecting items via hitbox touch to implement fuel/train mechanics. Works on mobile via tap-to-pick/tap-to-drop.

## Tips
- [0:31](https://youtu.be/ntHgQBEVERE?t=31) **[[building-art-and-assets]]** Use the carry/weld plugin from the description via Insert Model; move the setup folders into ReplicatedStorage, StarterPlayerScripts, Workspace and ServerScriptService as instructed.
- [1:27](https://youtu.be/ntHgQBEVERE?t=87) **[[building-art-and-assets]]** Build new items as a Model with all parts parented directly to it, set a PrimaryPart, unanchor parts and weld them to the primary part before storing in ReplicatedStorage.
- [2:49](https://youtu.be/ntHgQBEVERE?t=169) **[[building-art-and-assets]]** Keep the server-owner BuValue inside item models; do not remove it.
- [3:31](https://youtu.be/ntHgQBEVERE?t=211) **[[scripting-and-performance]]** Define per-item data by duplicating the test data module in the item data template; defaults are value 5, sellable true, usable false, fuel 5, so override only what differs.
- [4:13](https://youtu.be/ntHgQBEVERE?t=253) **[[code-architecture-and-frameworks]]** Add custom item fields (e.g. weight) to the data template default and to each item's data module so every item has the key.
- [4:55](https://youtu.be/ntHgQBEVERE?t=295) **[[scripting-and-performance]]** On the server, require the item data module, call setup with the item's data module and model, then clone the model into Workspace to spawn items.
- [6:29](https://youtu.be/ntHgQBEVERE?t=389) **[[code-architecture-and-frameworks]]** Do not mutate the shared data table at runtime; it is shared by every item created from it, so changes affect all items.
- [7:09](https://youtu.be/ntHgQBEVERE?t=429) **[[ui-ux-design]]** Customise the hover highlight, item UI text labels and fonts in the item UI templates; return edited UI to ReplicatedStorage afterwards.
- [7:50](https://youtu.be/ntHgQBEVERE?t=470) **[[combat-and-gameplay-systems]]** Tune range, carry distance, max carry distance, carry smoothness and throw boost in the interactable handler settings to tune pickup feel.
- [8:30](https://youtu.be/ntHgQBEVERE?t=510) **[[building-and-level-design]]** Place any part that should be weldable inside the weldable folder under train; grouping in folders or models still works.
- [9:13](https://youtu.be/ntHgQBEVERE?t=553) **[[ui-ux-design]]** Item tags (valuable, fuel, usable, heavy) are conditional on item data; add new tags by copying a tag template and changing its condition and text.
- [10:11](https://youtu.be/ntHgQBEVERE?t=611) **[[combat-and-gameplay-systems]]** Detect items on a hitbox by connecting Touched and checking other.Parent for ItemData, then require its ItemData value to read the data table.
- [11:35](https://youtu.be/ntHgQBEVERE?t=695) **[[combat-and-gameplay-systems]]** Implement fuel by checking item data.fuel on touch, adding the fuel amount, then destroying the item parent.

## Numbers
- [4:13](https://youtu.be/ntHgQBEVERE?t=253) Default item value: **5** (Item data template defaults: value 5, fuel 5, sellable true, usable false)
- [9:13](https://youtu.be/ntHgQBEVERE?t=553) Valuable tag threshold: **value > 15** (Example threshold in the item UI tag logic (heavy example uses weight > 2))

## Games
- **Dead Rails** [0:00](https://youtu.be/ntHgQBEVERE?t=0): Reference for the item drag/weld/valuable-tag mechanics the tutorial recreates; carry-to-train fuel loop.
- **Dead Rails (train fuel)** [10:11](https://youtu.be/ntHgQBEVERE?t=611): Train hitbox collects fuel items; the tutorial models this with a Touched-based hitbox.

## Tools
Roblox Studio, Welding plugin (Insert Model), Carry/weld system plugin from the description

## He points to
- Creator's Discord
- Upcoming video adding Dead Rails-style Q system to the plugin

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[pineappledevv - How to make successful Roblox games]]
