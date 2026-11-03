---
title: "The Basics of Combat Games: Hitboxes"
url: https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930
creator: Roblox DevForum
official: false
advice_density: high
date: 2024-06-03
views: 129
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Basics of Combat Games: Hitboxes

[Open](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) | Roblox DevForum | 129 views | 2024-06-03

## Summary
Tutorial on hit detection for Roblox combat games. Argues against .Touched() for melee, explains client-side hit detection via remote events with server validation, early attack signaling to offset latency, and compares magnitude, GetPartsInBox, and raycast hitboxes plus projectile handling and exploit sanity checks.

## Tips
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[combat-and-gameplay-systems]]** Avoid .Touched() for melee hitboxes; it is inaccurate on moving parts and misses parts already inside the hitbox. Reserve it for anchored triggers like landmines.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[client-server-and-remotes]]** Use client-side hit detection: server fires the hitbox data to the client, client reports hits back. This smooths latency at the cost of slight input delay.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[client-server-and-remotes]]** Use RemoteEvents rather than RemoteFunctions for hit reporting so one attack can hit multiple targets, and for security reasons.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[client-server-and-remotes]]** Early attack signaling: send the hitbox event during a windup, include os.clock() timestamp, and have the client wait (DelayTime minus elapsed) before activating so hitbox appears in sync.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[combat-and-gameplay-systems]]** Magnitude hitboxes (distance to a radius) are cheap and usually precise enough; prefer them unless precision is required.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[scripting-and-performance]]** GetPartsInBox supports varied shapes but costs more than magnitude checks; use it for wider or box-shaped attacks.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[scripting-and-performance]]** Raycast between last-frame and current positions of attachments on the weapon for precise swings; note it requires animation-tied sizing.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[combat-and-gameplay-systems]]** For fast projectiles, raycast between last recorded and current position each interval; use GetPartsInBox for large boxy projectiles, sized to travel distance plus projectile size.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[anti-exploit-and-security]]** Treat all client-reported hits as untrusted: validate that the target is not hit twice, the attack has not expired, and run a lenient server-side magnitude check.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[anti-exploit-and-security]]** Increase sanity-check strictness for clients that submit suspicious data.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) **[[combat-and-gameplay-systems]]** Keep a table of already-hit targets per attack and filter them out so a single swing does not damage the same character repeatedly.

## Numbers
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) CheckInterval (magnitude): **0.05 s** (Example interval for magnitude hitbox loop in article)
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) CheckInterval (GetPartsInBox, raycast): **0.1 s** (Example interval for box and raycast hitbox loops)
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-hitboxes/3002930) Client wait for early signaling: **DelayTime - (os.clock() - OriginalTime), clamped to >=0** (Formula to sync client hitbox with windup timing)

## Tools
Roblox Studio, RemoteEvent, workspace:GetPartBoundsInBox, workspace:Raycast, OverlapParams, RaycastParams, os.clock, task.wait

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
