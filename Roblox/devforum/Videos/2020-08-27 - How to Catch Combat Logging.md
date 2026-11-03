---
title: "How to Catch Combat Logging"
url: https://devforum.roblox.com/t/how-to-catch-combat-logging/743912
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-08-27
views: 86
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Catch Combat Logging

[Open](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) | Roblox DevForum | 86 views | 2020-08-27

## Summary
Tutorial on catching combat loggers in Roblox PvP games. Covers tagging attackers with ObjectValue creator tags on the server, using a timed StringValue tag folder in ServerStorage (15s window), and checking that tag on PlayerRemoving to punish combat logging. Advises moderate punishment.

## Tips
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Only build an anti-combat-log if dying carries a punishment (e.g. inventory loss); otherwise leaving mid-fight has no benefit to exploit.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[anti-exploit-and-security]]** Do all damage and combat-tag tracking on the server; the server-only approach cannot be spoofed by clients.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Tag the victim with the attacker's Player object (ObjectValue 'creator') immediately after server-side damage, clearing old tags first so only one exists.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Use Debris:AddItem on tag instances to auto-expire them; instances are easier to clean up than tables.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Store combat-log tags as named children in a ServerStorage folder; reset the timer by destroying and recreating the tag on each hit.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[data-persistence]]** On PlayerRemoving, check for a combat-log tag by player name before saving data, and apply the penalty before saving.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[player-psychology-and-game-feel]]** Keep punishment moderate: treat a leaver as having lost the fight, not harsher, since disconnects (crashes, net issues, misclicks) are common and harsh penalties drive players away.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Choose a combat-log window (the example uses 15 seconds) and make it the minimum time a tagged player must stay after being hit.
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) **[[combat-and-gameplay-systems]]** Wrap the combat-log tagging in a module and call it wherever the server applies damage, right after humanoid:TakeDamage.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) combat log tag window: **15 seconds** (Example timer; leaver must stay this long after last hit to avoid being flagged)
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) creator tag lifetime: **4 seconds** (Example Debris lifetime for ObjectValue kill-credit tag)

## Tools
Debris service, ServerStorage, PlayerRemoving event, ObjectValue, StringValue

## He points to
- BanTech (quoted forum advice on not over-punishing leavers)

## Quotes
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) "try not to punish too harshly - i.e. don't over-punish beyond what would happen if they lost the battle."
- [page](https://devforum.roblox.com/t/how-to-catch-combat-logging/743912) "As long as you're tracking this on the server, it can't be spoofed in any way, since all the tracking is on the server."

## Topics
[[anti-exploit-and-security]] [[combat-and-gameplay-systems]] [[data-persistence]] [[player-psychology-and-game-feel]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
