---
title: "How to make a Weighted RNG system in Roblox!"
url: https://youtu.be/QRkRk-FHN4s
creator: PineappleDev
official: false
advice_density: medium
date: 2025-07-15
views: 24759
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Weighted RNG system in Roblox!

[Watch](https://youtu.be/QRkRk-FHN4s) | pineappledevv | 24,759 views | 2025-07-15

## Summary
Builds a weighted RNG system in Roblox Studio: a Rarities ModuleScript holds weights and colors, an RNG module picks a rarity by cumulative weight, and an optional luck boost multiplies the roll. Tested via a RemoteEvent, a server script that spawns a colored part, and a client button.

## Tips
- [0:22](https://youtu.be/QRkRk-FHN4s?t=22) **[[core-loops-and-game-design]]** Store rarity weights as arbitrary integers (e.g. 800/150/45/5) rather than percentages; no need to sum to 100 or 1000.
- [1:33](https://youtu.be/QRkRk-FHN4s?t=93) **[[combat-and-gameplay-systems]]** Implement weighted picking by summing all weights, rolling math.random scaled to total, then walking cumulative weights until the roll is covered.
- [1:33](https://youtu.be/QRkRk-FHN4s?t=93) **[[player-psychology-and-game-feel]]** Apply luck boosts by multiplying the roll by a boost value below 1 (e.g. 0.1 gives 10x effective luck) so boosts stay compatible with weighted tables.
- [1:33](https://youtu.be/QRkRk-FHN4s?t=93) **[[scripting-and-performance]]** Clamp the scaled roll to [0, totalWeight] so a roll can never fall outside the valid weight range.
- [3:27](https://youtu.be/QRkRk-FHN4s?t=207) **[[client-server-and-remotes]]** Run the RNG roll on the server and have the client only fire a RemoteEvent, so players cannot choose their own result.
- [4:49](https://youtu.be/QRkRk-FHN4s?t=289) **[[anti-exploit-and-security]]** Keep rarity tables in ReplicatedStorage for shared access, but make sure the authoritative roll and any boost are decided server-side.

## Numbers
- [0:22](https://youtu.be/QRkRk-FHN4s?t=22) Example rarity weights: **Common 800, Rare 150, Epic 45, Legendary 5** (Example weights in tutorial; totals 1000, chosen by speaker)
- [6:21](https://youtu.be/QRkRk-FHN4s?t=381) Boost example: **0.1 boost = 10x luck** (Lower boost multiplier means higher effective luck)

## Tools
Roblox Studio, Luau ModuleScript, RemoteEvent, math.random, math.clamp

## He points to
- Model link in video description (not named)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[pineappledevv - How to make successful Roblox games]]
