---
title: "How to use Badges in Roblox! (Plus some scripting tips)"
url: https://youtu.be/T0xqkYODIl0
creator: B Ricey
official: false
advice_density: medium
date: 2022-05-28
views: 15482
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to use Badges in Roblox! (Plus some scripting tips)

[Watch](https://youtu.be/T0xqkYODIl0) | BRicey | 15,482 views | 2022-05-28

## Summary
Tutorial on implementing Roblox badges: creating a badge in Studio (free, zero Robux), awarding via BadgeService:AwardBadge, a tag-based touch-detector system using CollectionService and a badge ID attribute, and decoupling badge logic from core game code via a BindableEvent observer pattern.

## Tips
- [1:05](https://youtu.be/T0xqkYODIl0?t=65) **[[player-psychology-and-game-feel]]** Use badges for achievements and milestones; they add replayability and give hunters something to collect beyond the core loop.
- [2:26](https://youtu.be/T0xqkYODIl0?t=146) **[[monetisation-other]]** Create badges at zero Robux price; the speaker says badge creation should always be zero cost, with possible charges only above very high creation rates.
- [3:39](https://youtu.be/T0xqkYODIl0?t=219) **[[scripting-and-performance]]** Call BadgeService:AwardBadge with player.UserId, not the Player object, when awarding a badge; passing the Player is a common mistake.
- [5:06](https://youtu.be/T0xqkYODIl0?t=306) **[[scripting-and-performance]]** Keep badge logic separate from core mechanics so changes to gameplay don't require editing badge code.
- [6:27](https://youtu.be/T0xqkYODIl0?t=387) **[[building-and-level-design]]** Tag invisible detector parts with CollectionService (e.g. 'badge contact') and store the badge ID in an attribute so one script can handle every badge trigger on the map.
- [10:07](https://youtu.be/T0xqkYODIl0?t=607) **[[common-mistakes]]** Assert that the badge ID attribute exists on each tagged part so a forgotten attribute gives a clear error instead of a confusing one.
- [11:29](https://youtu.be/T0xqkYODIl0?t=689) **[[client-server-and-remotes]]** Use BadgeService:UserHasBadgeAsync to check ownership before awarding; the speaker notes Studio testing stopped awarding badges after a recent update.
- [12:25](https://youtu.be/T0xqkYODIl0?t=745) **[[code-architecture-and-frameworks]]** Award badges through an observer pattern (BindableEvent or signal library) fired from the player manager, so the badge system never gets coupled to player code.
- [13:05](https://youtu.be/T0xqkYODIl0?t=785) **[[code-architecture-and-frameworks]]** Put all badge logic in one script or module so the team always knows where achievements are awarded and why.
- [15:09](https://youtu.be/T0xqkYODIl0?t=909) **[[code-architecture-and-frameworks]]** Keep the achievement domain separate from player and data domains so badge code cannot break other systems.

## Numbers
- [2:26](https://youtu.be/T0xqkYODIl0?t=146) Badge creation price: **0 Robux** (Speaker says badge purchase should always be zero Robux)
- [2:26](https://youtu.be/T0xqkYODIl0?t=146) Badge creation rate note: **~100 per hour** (Speaker's uncertain recollection of a charge threshold)

## Tools
Roblox Studio, BadgeService, CollectionService, Tag plugin (Tag Manager), BindableEvent

## He points to
- Game Programming Patterns (book, observer pattern article)
- Speaker's CollectionService and tagging video

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[monetisation-other]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
