---
title: "Programming Rarity is Harder Than You Think"
url: https://youtu.be/UUgj-hmX2LM
creator: ByteBlox
official: false
advice_density: medium
date: 2024-05-11
views: 344308
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Programming Rarity is Harder Than You Think

[Watch](https://youtu.be/UUgj-hmX2LM) | byteblox100 | 344,308 views | 2024-05-11

## Summary
Tutorial building a weighted rarity system for a pet-simulator-style Roblox game. Covers storing pet models in ReplicatedStorage, spawning them with a loop, a ModuleScript holding Parts and Rarities tables, and a weighted random selection function (common 50, rare 30, epic 19, legendary 1). Ends with a note on table ordering.

## Tips
- [1:37](https://youtu.be/UUgj-hmX2LM?t=97) **[[scripting-and-performance]]** Spawn test objects with a loop (task.wait 0.1) rather than manual clicks, but remove or raise the wait if it causes lag; spawning every frame clogs Workspace.
- [2:17](https://youtu.be/UUgj-hmX2LM?t=137) **[[scripting-and-performance]]** Parent spawned clones to a dedicated folder (e.g. spawnedParts) instead of Workspace root to keep Workspace organised.
- [3:09](https://youtu.be/UUgj-hmX2LM?t=189) **[[code-architecture-and-frameworks]]** Put reusable logic such as rarity selection in a ModuleScript and require it from other scripts.
- [4:32](https://youtu.be/UUgj-hmX2LM?t=272) **[[luau-language-and-types]]** Every key in a Lua table constructor using brackets must be assigned a value; map each rarity name to its actual item reference.
- [5:07](https://youtu.be/UUgj-hmX2LM?t=307) **[[core-loops-and-game-design]]** Define rarity as weights summing to 100 (e.g. legendary 1, epic 19, rare 30, common 50) so the odds are easy to read and tune.
- [7:53](https://youtu.be/UUgj-hmX2LM?t=473) **[[scripting-and-performance]]** Return immediately once the cumulative weight reaches the random roll so the loop exits early instead of checking every rarity.
- [9:13](https://youtu.be/UUgj-hmX2LM?t=553) **[[core-loops-and-game-design]]** Removing the spawn delay produced several legendaries quickly in testing; a spawn-rate change visibly alters how often rare items appear.
- [9:54](https://youtu.be/UUgj-hmX2LM?t=594) **[[scripting-and-performance]]** Do not assume pairs() iterates in insertion order; table iteration is unordered, so the weighted selection must not depend on order when the rarities are read.
- [10:35](https://youtu.be/UUgj-hmX2LM?t=635) **[[scripting-and-performance]]** Pick the random roll first and then accumulate weights; this avoids biased results from order-dependent comparisons.

## Numbers
- [5:07](https://youtu.be/UUgj-hmX2LM?t=307) Legendary drop chance: **1%** (Example weight in the rarity table out of 100)
- [5:07](https://youtu.be/UUgj-hmX2LM?t=307) Epic drop chance: **19%** (Example weight in the rarity table out of 100)
- [5:07](https://youtu.be/UUgj-hmX2LM?t=307) Rare drop chance: **30%** (Example weight in the rarity table out of 100)
- [5:07](https://youtu.be/UUgj-hmX2LM?t=307) Common drop chance: **50%** (Example weight in the rarity table out of 100)
- [1:37](https://youtu.be/UUgj-hmX2LM?t=97) Spawn loop interval: **0.1 seconds** (Demo spawn loop interval used to avoid lag)

## Games
- **Pet Simulator** [0:00](https://youtu.be/UUgj-hmX2LM?t=0): Referenced as an example of a game using a rarity system; the video builds a mini version of it.

## Tools
Roblox Studio, Luau, ModuleScript

## Quotes
- [0:00](https://youtu.be/UUgj-hmX2LM?t=0) "Pet simulator and AAA games have rarity systems in common."
- [9:13](https://youtu.be/UUgj-hmX2LM?t=553) "This is literally gambling bro."

## Topics
[[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[byteblox100 - How to make successful Roblox games]]
