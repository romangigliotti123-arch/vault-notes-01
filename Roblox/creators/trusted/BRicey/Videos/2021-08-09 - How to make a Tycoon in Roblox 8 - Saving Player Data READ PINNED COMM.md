---
title: "How to make a Tycoon in Roblox #8 - Saving Player Data [READ PINNED COMMENT]"
url: https://youtu.be/TgZI48DTNqE
creator: B Ricey
official: false
advice_density: medium
date: 2021-08-09
views: 29971
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Tycoon in Roblox #8 - Saving Player Data [READ PINNED COMMENT]

[Watch](https://youtu.be/TgZI48DTNqE) | BRicey | 29,971 views | 2021-08-09

## Summary
Tutorial on saving player data in a Roblox tycoon using DataStoreService: load/save functions with pcall, a session data table keyed by user ID, saving on PlayerRemoving and BindToClose, and persisting tycoon unlocks by replaying saved unlock IDs on rejoin. Includes a DSpawn component to remove purchased buttons.

## Tips
- [1:02](https://youtu.be/TgZI48DTNqE?t=62) **[[data-persistence]]** Publish the game and enable 'Studio Access to API Services' in Game Settings > Security before DataStores work in Studio.
- [2:19](https://youtu.be/TgZI48DTNqE?t=139) **[[data-persistence]]** Wrap DataStore GetAsync/SetAsync in pcall; warn on failure and return success plus result so errors are visible.
- [5:07](https://youtu.be/TgZI48DTNqE?t=307) **[[data-persistence]]** Use SetAsync for simple overwrite saves; UpdateAsync is optional and unnecessary when you don't need the previous value.
- [6:28](https://youtu.be/TgZI48DTNqE?t=388) **[[data-persistence]]** Keep a session data table keyed by UserId and give new players default values (money 0, unlock ids empty table) when no save exists.
- [8:17](https://youtu.be/TgZI48DTNqE?t=497) **[[data-persistence]]** Route all money get/set through a PlayerManager function that also updates session data, so other scripts need no changes.
- [10:02](https://youtu.be/TgZI48DTNqE?t=602) **[[data-persistence]]** Save on PlayerRemoving and also bind game:BindToClose to save all players, since PlayerRemoving may not fire when the server shuts down.
- [12:45](https://youtu.be/TgZI48DTNqE?t=765) **[[data-persistence]]** Studio testing of save-on-leave is unreliable; skip saving when RunService:IsStudio() during tests, but verify in a published build.
- [14:19](https://youtu.be/TgZI48DTNqE?t=859) **[[data-persistence]]** Persist tycoon progress by saving unique unlock IDs, then replay them by publishing button topics on rejoin to rebuild state quickly.
- [15:39](https://youtu.be/TgZI48DTNqE?t=939) **[[data-persistence]]** Check for duplicates with table.find before inserting unlock IDs so shared IDs from multiple parts don't pile up in saved data.
- [19:06](https://youtu.be/TgZI48DTNqE?t=1146) **[[scripting-and-performance]]** Create unlockables before replaying saved unlocks, otherwise publishes are missed; call LoadUnlocks after the unlock setup in init.
- [20:13](https://youtu.be/TgZI48DTNqE?t=1213) **[[code-architecture-and-frameworks]]** Use a small reusable component (e.g. DSpawn) that listens to a topic and destroys its part; tag parts with CollectionService and avoid per-button destroy logic.
- [22:20](https://youtu.be/TgZI48DTNqE?t=1340) **[[testing-debugging-and-qa]]** Disable Studio API access after testing DataStores to keep Studio from lagging, and test in a published build for accurate save behaviour.

## Tools
Roblox Studio, DataStoreService, Tag Editor plugin, Server Storage, RunService:IsStudio

## He points to
- Advanced DataStore tutorial by the same creator (linked in video card)
- Creator's Discord server (linked in description)

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[BRicey - How to make successful Roblox games]]
