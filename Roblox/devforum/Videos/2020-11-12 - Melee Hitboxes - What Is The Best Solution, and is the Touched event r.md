---
title: "Melee Hitboxes - What Is The Best Solution, and is the Touched event really that bad?"
url: https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-11-12
views: 114
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Melee Hitboxes - What Is The Best Solution, and is the Touched event really that bad?

[Open](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) | Roblox DevForum | 114 views | 2020-11-12

## Summary
DevForum post by PysephDEV arguing for a client-authoritative melee hitbox using the Touched event on the server, with a 5-stud distance check against exploits. Covers why GetTouchingParts, Region3 and raycasting were rejected, the Touched/ping tradeoff, and weapon network-ownership pitfalls (Motor6D/Weld deletion, teleporting weapons).

## Tips
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) **[[combat-and-gameplay-systems]]** For melee hitboxes, connect Touched on the server and set the weapon's network owner to the client (parent to character or SetNetworkOwner) so hits register despite ping.
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) **[[anti-exploit-and-security]]** Validate Touched hits server-side by rejecting any touched part farther than about 5 studs from the weapon or player.
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) **[[anti-exploit-and-security]]** Kick players who delete the Motor6D/Weld rigging the weapon, and check whether the weapon is still parented to the character when that happens.
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) **[[client-server-and-remotes]]** Touched fires based on client-controlled physics, so server-side Touched can be exploited; it is a tradeoff for ping compensation, not a free solution.
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) **[[scripting-and-performance]]** GetTouchingParts only detects CanCollide parts; Region3 is costly and unrotated; raycasting is lightweight and gives hit position, but needs a module for ease of use.

## Numbers
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) max hit distance check: **5 studs** (Server rejects Touched hits where part is farther than this from weapon)
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) client ping delay for server data: **0 to 5000ms** (Range of delay the author cites for client data reaching server)

## Tools
Touched event, GetTouchingParts, Raycasting, Region3, @EgoMoose Rotated Region3 module, Motor6D, SetNetworkOwner

## He points to
- @EgoMoose Rotated Region3 module
- @avozzo

## Quotes
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) "The client tells the server when it's collided with something - the server doesn't calculate it, the client does!"
- [page](https://devforum.roblox.com/t/melee-hitboxes-what-is-the-best-solution-and-is-the-touched-event-really-that-bad/867477) "you can just check if the touched part is less than 5 studs away from the sword / player."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
