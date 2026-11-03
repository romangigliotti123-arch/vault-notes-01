---
title: "How to make a LOBBY TELEPORT system in Roblox Studio! (2024)"
url: https://youtu.be/5wudgfIoTwo
creator: PineappleDev
official: false
advice_density: medium
date: 2024-08-22
views: 147443
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a LOBBY TELEPORT system in Roblox Studio! (2024)

[Watch](https://youtu.be/5wudgfIoTwo) | pineappledevv | 147,443 views | 2024-08-22

## Summary
Tutorial building a lobby/queue teleport system in Roblox Studio: queue area with enter/exit hitboxes, a BillboardGui showing player count and countdown, a server script that teleports queued players to a reserved server via TeleportService, and a LocalScript that locks/unlocks the camera.

## Tips
- [0:11](https://youtu.be/5wudgfIoTwo?t=11) **[[building-and-level-design]]** Group all queue-area parts into one folder so a single script can loop over multiple queue rooms and duplicates work automatically.
- [3:30](https://youtu.be/5wudgfIoTwo?t=210) **[[matchmaking-and-teleport]]** Use TeleportService:ReserveServer and TeleportToPrivateServer, passing the queued player list as teleport data, to move a lobby group together.
- [8:21](https://youtu.be/5wudgfIoTwo?t=501) **[[scripting-and-performance]]** Add a debounce flag to touch handlers so a player touching a hitbox doesn't join the queue multiple times.
- [8:21](https://youtu.be/5wudgfIoTwo?t=501) **[[matchmaking-and-teleport]]** Check that the player isn't already in the queue folder before adding them, and cap queue size at the player limit.
- [12:27](https://youtu.be/5wudgfIoTwo?t=747) **[[matchmaking-and-teleport]]** When the last player leaves, cancel the countdown coroutine and reset the timer UI text to the default countdown value.
- [15:55](https://youtu.be/5wudgfIoTwo?t=955) **[[matchmaking-and-teleport]]** After teleporting, clear the queue folder entries and reset the billboard counter so the next group starts clean.
- [11:06](https://youtu.be/5wudgfIoTwo?t=666) **[[client-server-and-remotes]]** Fire a RemoteEvent to the client on join to lock the camera to a scriptable exit position, and restore CustomCamera on leave.
- [4:12](https://youtu.be/5wudgfIoTwo?t=252) **[[client-server-and-remotes]]** Create JoinQ and LeftQ RemoteEvents in ReplicatedStorage and wire them to the server queue logic.
- [2:14](https://youtu.be/5wudgfIoTwo?t=134) **[[ui-ux-design]]** Show queue status with a BillboardGui above the queue area: player count out of limit and a countdown timer text.

## Numbers
- [4:12](https://youtu.be/5wudgfIoTwo?t=252) Player limit per queue: **4** (Example queue size set in tutorial script)
- [4:12](https://youtu.be/5wudgfIoTwo?t=252) Countdown before teleport: **10 seconds** (Example countdown length in tutorial script)

## Tools
Roblox Studio, Luau, TeleportService, RemoteEvents, BillboardGui

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[pineappledevv - How to make successful Roblox games]]
