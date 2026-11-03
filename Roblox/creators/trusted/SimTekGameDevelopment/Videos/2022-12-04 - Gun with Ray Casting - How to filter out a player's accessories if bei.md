---
title: "Gun with Ray Casting - How to filter out a player's accessories if being shot"
url: https://youtu.be/BiaMIbrzo0Q
creator: SimTek Game Development
official: false
advice_density: medium
date: 2022-12-04
views: 7853
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Gun with Ray Casting - How to filter out a player's accessories if being shot

[Watch](https://youtu.be/BiaMIbrzo0Q) | SimTekGameDevelopment | 7,853 views | 2022-12-04

## Summary
Tutorial on implementing raycast-based weapon hits in Roblox instead of click-target damage. Covers a client shoot script sending the hit to a server damage script, RaycastParams with a blacklist filter, a 300-stud range, recursively skipping accessories (hats, hair, glasses, backpacks) and passing through characters so armor-piercing shots hit multiple targets. Tested in a two-player test server.

## Tips
- [2:06](https://youtu.be/BiaMIbrzo0Q?t=126) **[[scripting-and-performance]]** Cap raycast distance (e.g. 300 studs) so shots have a range limit; raycasts otherwise reach infinitely, unlike click-based damage.
- [4:57](https://youtu.be/BiaMIbrzo0Q?t=297) **[[scripting-and-performance]]** Use RaycastFilterType Blacklist with a table of excluded instances (own character, accessories) so the ray ignores them.
- [8:10](https://youtu.be/BiaMIbrzo0Q?t=490) **[[scripting-and-performance]]** When a raycast hits an accessory, add it to the filter and recast recursively until a body part or non-accessory is hit.
- [10:10](https://youtu.be/BiaMIbrzo0Q?t=610) **[[combat-and-gameplay-systems]]** Add hit body parts to the filter and recast to enable piercing shots through multiple characters, e.g. armor-piercing rounds.
- [2:06](https://youtu.be/BiaMIbrzo0Q?t=126) **[[anti-exploit-and-security]]** Keep damage application in a server Script; the client only sends the hit target and the server applies Humanoid damage.

## Numbers
- [2:06](https://youtu.be/BiaMIbrzo0Q?t=126) raycast range: **300 studs** (Max shot distance in the example script)
- [8:10](https://youtu.be/BiaMIbrzo0Q?t=490) accessory depth: **~3 accessories** (Speaker estimates max accessories stacked on one hit point)

## Tools
Roblox Studio, Workspace:Raycast, RaycastParams, Toolbox simple gun

## He points to
- Simple gun model from Toolbox (linked in description)

## Topics
[[anti-exploit-and-security]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
