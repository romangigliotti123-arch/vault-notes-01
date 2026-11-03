---
title: "QueryAuth | Roblox Open Source Showcase #4"
url: https://youtu.be/Xi--YI0Hk7M
creator: Possible Panda
official: false
advice_density: medium
date: 2025-11-09
views: 5125
transcript: auto-captions
confidence: high
tags: [roblox, possiblepanda, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# QueryAuth | Roblox Open Source Showcase #4

[Watch](https://youtu.be/Xi--YI0Hk7M) | PossiblePanda | 5,125 views | 2025-11-09

## Summary
Creator showcases QueryAuth, his open-source Roblox package for permission checks. Explains installing via release .rbxm or Wally/Pesta, building composable conditions (one/all, chaining), using team/rank/premium/account-age checks on doors, and writing custom condition modules. No formal docs yet.

## Tips
- [1:07](https://youtu.be/Xi--YI0Hk7M?t=67) **[[version-control-and-tooling]]** Install QueryAuth by downloading query author.rbxm from the GitHub releases tab and dragging it into ReplicatedStorage, or use Wally/Pesta.
- [3:00](https://youtu.be/Xi--YI0Hk7M?t=180) **[[code-architecture-and-frameworks]]** Build permission checks as composable functions that take a player and return a boolean, then chain them with one/all operators for reusable access rules.
- [10:19](https://youtu.be/Xi--YI0Hk7M?t=619) **[[code-architecture-and-frameworks]]** Put permission modules under each door and use a central manager script to scale access control instead of hardcoding logic per object.
- [11:06](https://youtu.be/Xi--YI0Hk7M?t=666) **[[code-architecture-and-frameworks]]** Save commonly reused permission combinations as shared ReplicatedStorage modules so multiple objects can reference one rule set.
- [11:46](https://youtu.be/Xi--YI0Hk7M?t=706) **[[code-architecture-and-frameworks]]** Create custom conditions by returning a function that takes a Player and returns a boolean; the library is extensible this way.

## Numbers
- [0:00](https://youtu.be/Xi--YI0Hk7M?t=0) Development time: **About 1 day to build the package** (Creator's own statement about QueryAuth build time)
- [12:27](https://youtu.be/Xi--YI0Hk7M?t=747) Views: **5125** (Video view count at time of listing)

## Games
- **SCPF (roleplay game, in development)** [12:27](https://youtu.be/Xi--YI0Hk7M?t=747): Creator plans to use QueryAuth in an SCP-style roleplay game, which he says suits this kind of permission system.

## Tools
QueryAuth (Roblox open-source permission package), Roblox Studio, Wally, Pesta, Roblox Toolbox

## He points to
- QueryAuth GitHub (linked in video description)
- Lat Latiel (contributor, Discord linked on screen)

## Quotes
- [0:00](https://youtu.be/Xi--YI0Hk7M?t=0) "This package is mainly for seeing if a player can do a specific action."
- [4:24](https://youtu.be/Xi--YI0Hk7M?t=264) "Everything is a lambda. Everything is a function that takes in a player and returns a boolean."

## Topics
[[code-architecture-and-frameworks]] [[version-control-and-tooling]]

Back to [[PossiblePanda - How to make successful Roblox games]]
