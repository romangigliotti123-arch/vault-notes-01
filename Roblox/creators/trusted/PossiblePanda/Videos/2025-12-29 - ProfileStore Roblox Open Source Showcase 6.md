---
title: "ProfileStore | Roblox Open Source Showcase #6"
url: https://youtu.be/0rmh0FpHBYM
creator: Possible Panda
official: false
advice_density: medium
date: 2025-12-29
views: 5805
transcript: auto-captions
confidence: medium
tags: [roblox, possiblepanda, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# ProfileStore | Roblox Open Source Showcase #6

[Watch](https://youtu.be/0rmh0FpHBYM) | PossiblePanda | 5,805 views | 2025-12-29

## Summary
Tutorial on ProfileStore, a DataStore wrapper handling autosave, session locking and reconciliation. Covers installing from the Roblox library, a data template with types, starting sessions per player, kicking on failed load, giving/getting money and items, and a helper to check data loaded. Replica is teased as the next video.

## Tips
- [0:00](https://youtu.be/0rmh0FpHBYM?t=0) **[[data-persistence]]** Use ProfileStore for new projects over ProfileService; ProfileService users have little reason to switch.
- [6:26](https://youtu.be/0rmh0FpHBYM?t=386) **[[data-persistence]]** Kick the player if profile fails to load, so they can't play and lose unsaved progress.
- [7:27](https://youtu.be/0rmh0FpHBYM?t=447) **[[data-persistence]]** Call profile:AddUserId(player.UserId) so Roblox GDPR deletions remove the DataStore entry automatically.
- [8:07](https://youtu.be/0rmh0FpHBYM?t=487) **[[data-persistence]]** Call profile:Reconcile() after loading so new template keys are added to existing player data automatically.
- [8:49](https://youtu.be/0rmh0FpHBYM?t=529) **[[data-persistence]]** Kick players when profile session ends (profile.OnSessionEnd) so they cannot keep playing unsaved.
- [10:07](https://youtu.be/0rmh0FpHBYM?t=607) **[[data-persistence]]** Enable Experience Settings > Security > Enable Studio Access to API Services before testing DataStores.
- [10:46](https://youtu.be/0rmh0FpHBYM?t=646) **[[data-persistence]]** Profile store autosaves; you don't need manual saves on disconnect, but end the session on leave as a backup.
- [13:00](https://youtu.be/0rmh0FpHBYM?t=780) **[[scripting-and-performance]]** Guard data access with an is-loaded check, or expose a per-player loaded signal, to avoid nil errors before profile loads.
- [15:19](https://youtu.be/0rmh0FpHBYM?t=919) **[[code-architecture-and-frameworks]]** Wrap data access in a manager module with helpers like GetData, GiveMoney, GetMoney, GiveItem, GetItems instead of raw profile access.
- [3:06](https://youtu.be/0rmh0FpHBYM?t=186) **[[luau-language-and-types]]** Define an exported player data type and type-cast the data template to it so data shape is checked.

## Numbers
- [10:07](https://youtu.be/0rmh0FpHBYM?t=607) DataStore access setting: **Enable Studio Access to API Services** (Required toggle in Security settings for DataStores in Studio)

## Tools
ProfileStore, ProfileService, Replica, Wally

## He points to
- ProfileStore GitHub
- Roblox Creator Store / toolbox model for ProfileService/ProfileStore
- Previous video on module loaders and signals (same channel)

## Quotes
- [0:00](https://youtu.be/0rmh0FpHBYM?t=0) "I would suggest profile store to almost anyone who needs to handle player data."
- [17:25](https://youtu.be/0rmh0FpHBYM?t=1045) "this is far better than profile store. I mean, it's pretty much just a newer version."

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[PossiblePanda - How to make successful Roblox games]]
