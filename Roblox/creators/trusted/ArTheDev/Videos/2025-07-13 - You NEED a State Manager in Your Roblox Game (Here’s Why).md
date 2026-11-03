---
title: "You NEED a State Manager in Your Roblox Game (Here’s Why)"
url: https://youtu.be/WImDkrf3sAo
creator: ArTheDev
official: false
advice_density: high
date: 2025-07-13
views: 97732
transcript: auto-captions
confidence: medium
tags: [roblox, arthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# You NEED a State Manager in Your Roblox Game (Here’s Why)

[Watch](https://youtu.be/WImDkrf3sAo) | ArTheDev | 97,732 views | 2025-07-13

## Summary
Tutorial for a reusable player state manager ModuleScript in Roblox (ReplicatedStorage). Tracks per-player states with timed durations, auto-expiring via delayed tasks, plus a stun system that sets walk speed and uses coroutine timers. Shows usage via ProximityPrompt and a combat example using attributes for NPCs.

## Tips
- [0:00](https://youtu.be/WImDkrf3sAo?t=0) **[[combat-and-gameplay-systems]]** Build a central state manager module tracking per-player states (parrying, blocking, dashing, stunned) so other scripts can check state before allowing actions.
- [15:44](https://youtu.be/WImDkrf3sAo?t=944) **[[combat-and-gameplay-systems]]** Use ProximityPrompt instead of ClickDetector for interactions, since ClickDetector doesn't work on mobile.
- [5:18](https://youtu.be/WImDkrf3sAo?t=318) **[[scripting-and-performance]]** Auto-expire states with a delayed task after the duration, and nil the state when it ends, so you never need manual cleanup logic.
- [10:08](https://youtu.be/WImDkrf3sAo?t=608) **[[data-persistence]]** Clear the player's entries from state tables on PlayerRemoving; otherwise the tables keep growing and the server eventually lags.
- [11:29](https://youtu.be/WImDkrf3sAo?t=689) **[[combat-and-gameplay-systems]]** Implement stun with a stored end time and a coroutine loop that restores original walk speed when the stun ends; overlapping hits extend via math.max.
- [14:56](https://youtu.be/WImDkrf3sAo?t=896) **[[combat-and-gameplay-systems]]** To manually remove a stun, call the stun function with value false; use remove-states only if you also clear the stun timer entry.
- [5:18](https://youtu.be/WImDkrf3sAo?t=318) **[[scripting-and-performance]]** Guard state setters with type checks on duration and existence checks on player tables to avoid errors from typos or missing entries.
- [18:28](https://youtu.be/WImDkrf3sAo?t=1108) **[[client-server-and-remotes]]** Keep state logic on the server (ServerScriptService) and call it from server-side handlers so clients cannot set states themselves.
- [21:18](https://youtu.be/WImDkrf3sAo?t=1278) **[[combat-and-gameplay-systems]]** For NPCs or non-player characters, store state in attributes on the character model instead of player-keyed tables, so combat checks work on enemies.
- [20:32](https://youtu.be/WImDkrf3sAo?t=1232) **[[combat-and-gameplay-systems]]** Ignore repeated set-state calls while a state is already active; spamming an action does not stack states.

## Numbers
- [19:52](https://youtu.be/WImDkrf3sAo?t=1192) Example state duration: **4 seconds (clicked=true), 1.5 seconds in demo** (ProximityPrompt demo state timers)

## Tools
Roblox Studio, ModuleScript, ProximityPrompt, ServerScriptService

## He points to
- Combat system video (promised, linked in description)

## Quotes
- [0:00](https://youtu.be/WImDkrf3sAo?t=0) "If you are making a Roblox game, doesn't matter if it's a fighting game, a simulator, an RPG, or anything in between, you need to have a state manager."
- [10:08](https://youtu.be/WImDkrf3sAo?t=608) "If the player leaves and you don't do this, then this table will just keep getting filled and filled until eventually the game will be extremely laggy."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[data-persistence]] [[scripting-and-performance]]

Back to [[ArTheDev - How to make successful Roblox games]]
