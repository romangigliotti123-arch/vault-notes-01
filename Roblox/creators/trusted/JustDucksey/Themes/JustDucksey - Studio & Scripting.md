---
title: JustDucksey - Studio & Scripting
creator: JustDucksey
tags: [roblox, justducksey, theme]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# JustDucksey: Studio & Scripting

All JustDucksey tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2025-01-29 [2:09](https://youtu.be/jKyzG9HPrRM?t=129) Roblox Touched events can be unreliable for pickups or tools; expect to debug them and consider alternative detection methods. ([[2025-01-29 - I Turned YOUR IDEAS into a Farming Game|I Turned YOUR IDEAS into a Farming Game]])
- 2025-05-12 [1:23](https://youtu.be/tSWHABNX2bU?t=83) Stop animating distant objects: freeze wind-shake on far props using a configurable range; the creator says a test with many objects stayed performant. ([[2025-05-12 - We FINALLY added a MAP to our Roblox Game|We FINALLY added a MAP to our Roblox Game...]])
- 2025-05-21 [0:42](https://youtu.be/qVkYbVHWI1I?t=42) Set starting cash for new players in the player-join server script so it is easy to tune. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])

## [[building-art-and-assets]]
- 2025-01-29 [2:51](https://youtu.be/jKyzG9HPrRM?t=171) Welding parts to tween models is awkward on Roblox; use welds/constraints and animate the assembled tool rather than tweening individual models. ([[2025-01-29 - I Turned YOUR IDEAS into a Farming Game|I Turned YOUR IDEAS into a Farming Game]])
- 2025-04-10 [1:23](https://youtu.be/BbNlDGBROdg?t=83) Test whether models visually communicate function (e.g. wheels appear to turn); a plain static model may need a simple texture or animation to read as moving. ([[2025-04-10 - We made a ROAD TRIP game on Roblox Devlog 1|We made a ROAD TRIP game on Roblox | Devlog #1]])
- 2025-04-10 [1:23](https://youtu.be/BbNlDGBROdg?t=83) Keep asset style consistent: choose one visual style (here bubbly/plastic) and make all parts match so the game looks cohesive. ([[2025-04-10 - We made a ROAD TRIP game on Roblox Devlog 1|We made a ROAD TRIP game on Roblox | Devlog #1]])
- 2025-04-10 [3:29](https://youtu.be/BbNlDGBROdg?t=209) Create multiple variants of key parts (e.g. basic and gold engines) to give players progression and collection, planned across all parts. ([[2025-04-10 - We made a ROAD TRIP game on Roblox Devlog 1|We made a ROAD TRIP game on Roblox | Devlog #1]])
- 2025-05-21 [1:22](https://youtu.be/qVkYbVHWI1I?t=82) Name crop growth stages exactly as STAGE_1, STAGE_2 etc. and weld all parts to an anchored main part so the model grows correctly. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])
- 2025-05-21 [4:45](https://youtu.be/qVkYbVHWI1I?t=285) Set each crop model's pivot to its bottom using Model > Edit Pivot so it grows up from the ground. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])
- 2025-05-21 [2:43](https://youtu.be/qVkYbVHWI1I?t=163) For regrowable plants, add a SpawnPositions folder of invisible parts marking where crops can grow; the crop needs default value, growth type, and is full attributes. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])

## [[ai-and-tools]]
- 2025-04-10 [1:23](https://youtu.be/BbNlDGBROdg?t=83) Roblox AI texture generation crashed for the creator; have a fallback texture plan rather than relying on AI tools. ([[2025-04-10 - We made a ROAD TRIP game on Roblox Devlog 1|We made a ROAD TRIP game on Roblox | Devlog #1]])

## [[data-persistence]]
- 2025-04-19 [2:09](https://youtu.be/qxE7JhikvwY?t=129) Build saving alongside gameplay systems early, e.g. a farming system that saves player data, rather than retrofitting it later. ([[2025-04-19 - I spent 500 DAYS learning ROBLOX STUDIO, here's what I learned|I spent 500 DAYS learning ROBLOX STUDIO, here's wh]])

## [[combat-and-gameplay-systems]]
- 2025-04-19 [4:52](https://youtu.be/qxE7JhikvwY?t=292) Build gameplay systems like crop breaking, inventory and shop selling as separate pieces that connect to each other. ([[2025-04-19 - I spent 500 DAYS learning ROBLOX STUDIO, here's what I learned|I spent 500 DAYS learning ROBLOX STUDIO, here's wh]])
- 2025-05-07 [2:47](https://youtu.be/o-8KX6XgC7s?t=167) Use a timed shop reset (every 5 minutes) with randomized stock per crop to create scarcity. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-07 [3:27](https://youtu.be/o-8KX6XgC7s?t=207) Use the built-in Roblox inventory system to save time on item storage. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-07 [4:48](https://youtu.be/o-8KX6XgC7s?t=288) Add rarity variants (gold, rainbow) as a multiplier layer on the base crop rather than separate items. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-21 [3:23](https://youtu.be/qVkYbVHWI1I?t=203) Store the crop tool in a Regrowables folder with a selling price attribute and its own growth stages, separate from seed tools. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])
- 2025-05-21 [4:03](https://youtu.be/qVkYbVHWI1I?t=243) Control seed stock with a per-seed in-stock chance out of 100 and a stock amount reset each shop restock cycle in the seed shop manager. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])
- 2025-05-21 [4:45](https://youtu.be/qVkYbVHWI1I?t=285) Set shop restock interval in seconds in the seed shop manager; 300 seconds matches the real game's 5-minute restock. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])

## [[building-and-level-design]]
- 2025-05-07 [0:42](https://youtu.be/o-8KX6XgC7s?t=42) Build one complete plot, then duplicate it (six plots here) to match the original layout quickly. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-07 [4:08](https://youtu.be/o-8KX6XgC7s?t=248) Tag soil blocks and restrict planting to the owner's plot so players cannot plant on others' land. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])

## [[3d-modeling-rigging-and-animation]]
- 2025-01-29 [4:15](https://youtu.be/jKyzG9HPrRM?t=255) Check animations in-game before polishing; the dev's duck-head animation played backwards and only showed up after testing. ([[2025-01-29 - I Turned YOUR IDEAS into a Farming Game|I Turned YOUR IDEAS into a Farming Game]])

## [[ui-ux-design]]
- 2025-01-29 [4:55](https://youtu.be/jKyzG9HPrRM?t=295) Icons taken from screenshots with backgrounds removed are hard to read on dark backgrounds; design custom icons per item and test contrast. ([[2025-01-29 - I Turned YOUR IDEAS into a Farming Game|I Turned YOUR IDEAS into a Farming Game]])
- 2025-01-29 [0:47](https://youtu.be/jKyzG9HPrRM?t=47) Replace generic simulator-style sell pads with a diegetic NPC merchant that has dialogue, which makes selling feel less generic. ([[2025-01-29 - I Turned YOUR IDEAS into a Farming Game|I Turned YOUR IDEAS into a Farming Game]])
- 2025-05-07 [1:23](https://youtu.be/o-8KX6XgC7s?t=83) Use a screenshot of a reference UI as a placeholder background to mock up shop layouts fast. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-07 [2:47](https://youtu.be/o-8KX6XgC7s?t=167) Duplicate one item UI into a scrolling frame, then rename and reprice each entry. ([[2025-05-07 - I remade GROW A GARDEN in 8 HOURS|I remade GROW A GARDEN in 8 HOURS...]])
- 2025-05-21 [5:25](https://youtu.be/qVkYbVHWI1I?t=325) Duplicate an existing shop frame, update its attributes and price, and set the buy button text to match the crop cost. ([[2025-05-21 - I made a FREE Grow a Garden KIT that YOU can use|I made a FREE Grow a Garden KIT that YOU can use..]])
- 2025-10-09 [1:24](https://youtu.be/XZKHQPObHgw?t=84) Switch from third person to first person when third person is too hard to control for the core interaction. ([[2025-10-09 - I Joined My FIRST Game Jam for $250,000 ROBUX|I Joined My FIRST Game Jam for $250,000 ROBUX...]])

## [[optimization-and-streaming]]
- 2025-05-12 [1:23](https://youtu.be/tSWHABNX2bU?t=83) Auto-remove debris that flew off after about 30 seconds to prevent lag from accumulating physics objects. ([[2025-05-12 - We FINALLY added a MAP to our Roblox Game|We FINALLY added a MAP to our Roblox Game...]])
- 2025-05-12 [3:26](https://youtu.be/tSWHABNX2bU?t=206) Gate wind-driven object flight by wind speed threshold (around 200 wind) with a random chance, so only strong gusts launch props. ([[2025-05-12 - We FINALLY added a MAP to our Roblox Game|We FINALLY added a MAP to our Roblox Game...]])

Up: [[JustDucksey - How to make successful Roblox games]]
