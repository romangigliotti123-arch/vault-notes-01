---
title: "Roblox Has Very Bad Hitboxes & It's Not Their Fault"
url: https://youtu.be/3rxZj5-Qx30
creator: ByteBlox
official: false
advice_density: medium
date: 2025-03-15
views: 478050
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Has Very Bad Hitboxes & It's Not Their Fault

[Watch](https://youtu.be/3rxZj5-Qx30) | byteblox100 | 478,050 views | 2025-03-15

## Summary
Explains how Roblox hitboxes work by default (character body parts via raycast name check), why custom enlarged hitboxes improve ability feel, and how client-server delay causes clunky hit registration. Demonstrates a welded, massless, transparent, non-colliding hitbox part and a simulated 0.2–0.5s delay. Mentions lag compensation and rollback as solutions.

## Tips
- [8:12](https://youtu.be/3rxZj5-Qx30?t=492) **[[combat-and-gameplay-systems]]** For big ability hits, create a separate invisible hitbox part sized larger than the character rather than relying on the default body-part hitboxes.
- [9:34](https://youtu.be/3rxZj5-Qx30?t=574) **[[combat-and-gameplay-systems]]** Make custom hitbox parts non-collidable, non-anchored, transparent, and massless; weld them to HumanoidRootPart so they follow movement without slowing the character.
- [10:14](https://youtu.be/3rxZj5-Qx30?t=614) **[[combat-and-gameplay-systems]]** Check hits by part name (e.g. 'hitbox') in the raycast handler so one hitbox works for any ability, instead of checking the character's body parts.
- [5:17](https://youtu.be/3rxZj5-Qx30?t=317) **[[combat-and-gameplay-systems]]** Use separate hitboxes per projectile type or weak point (e.g. head, back) so you can balance projectiles without changing their size or speed.
- [19:52](https://youtu.be/3rxZj5-Qx30?t=1192) **[[combat-and-gameplay-systems]]** Use larger hitboxes for ability-based or fighting games, since small avatar hitboxes feel unfair under network delay; reserve tight hitboxes for shooters where precision is expected.
- [21:14](https://youtu.be/3rxZj5-Qx30?t=1274) **[[core-loops-and-game-design]]** Look into lag compensation / rollback techniques if building precise combat, since the server must validate hits against where the target was in the past.
- [22:34](https://youtu.be/3rxZj5-Qx30?t=1354) **[[client-server-and-remotes]]** Let the client move freely for responsiveness, then have the server run security checks and correct (rubber-band) invalid movement, balancing smoothness with server authority.

## Numbers
- [4:37](https://youtu.be/3rxZj5-Qx30?t=277) Raycast damage per hit: **5 health** (Example damage script subtracts 5 health per laser hit)
- [8:53](https://youtu.be/3rxZj5-Qx30?t=533) Custom hitbox transparency: **0.8** (Hitbox made very transparent for an invisible ability hitbox)
- [17:08](https://youtu.be/3rxZj5-Qx30?t=1028) Simulated lag delay tested: **0.5s then 0.2s** (Demo delay of hitbox position; 0.5s judged too much, 0.2s more realistic)

## Games
- **Team Fortress 2** [0:41](https://youtu.be/3rxZj5-Qx30?t=41): Emotes keep the invisible hitbox in place, and arrows hit a separate bigger hitbox that ignores bullets, enabling per-projectile balancing.
- **Arsenal** [23:25](https://youtu.be/3rxZj5-Qx30?t=1405): 'Dead before shot registering' shows server delay can make a valid shot count for nothing; shooters need lag compensation.
- **Overwatch** [21:14](https://youtu.be/3rxZj5-Qx30?t=1274): Example of movement continuing after connection loss, showing client-side prediction in action.

## Tools
Roblox Studio, Luau

## He points to
- Roblox rollback / lag compensation (speaker suggests searching, not named precisely)
- Creator's paid courses (promotional, skipped)

## Quotes
- [11:38](https://youtu.be/3rxZj5-Qx30?t=698) "Big hitboxes make abilities feel good because you're not aiming precisely; you're just going in the general direction."
- [19:52](https://youtu.be/3rxZj5-Qx30?t=1192) "In a shooter every millisecond matters; with big hitboxes the delay still happens but is much less noticeable."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]]

Back to [[byteblox100 - How to make successful Roblox games]]
