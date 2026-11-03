---
title: "The Basics of Combat Games: Health and Damage"
url: https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-05-29
views: 70
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Basics of Combat Games: Health and Damage

[Open](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) | Roblox DevForum | 70 views | 2024-05-29

## Summary
Tutorial on building a custom health/damage and status-effect system for combat games using ModuleScripts: storing stats in a module, a TakeDamage function with defense, piercing and blocking, and stun/status effects using newproxy() tokens to handle interruption.

## Tips
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[combat-and-gameplay-systems]]** Store player stats (Health, MaxHealth, WalkSpeed, JumpPower) in a ModuleScript inside the character model and require() it from server scripts.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[combat-and-gameplay-systems]]** Put damage logic in a TakeDamage function in the module that takes an AttackInfo dictionary, so new attack parameters don't require copy-pasted code.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[combat-and-gameplay-systems]]** Use math.clamp on (Defense - Piercing) so armor never goes negative, and use 'or 0' so a missing Piercing value doesn't error.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[combat-and-gameplay-systems]]** Use newproxy() as unique tokens to detect interrupted timed effects; compare the stored token to the local one after task.wait instead of using a counter.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[combat-and-gameplay-systems]]** Define status effects in a dictionary (Info and State tables) and apply them through one generic function, rather than writing a separate function per status.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[scripting-and-performance]]** Do all damage and status calculations in a server Script; ModuleScript state does not replicate between client and server, so keep authoritative stats on the server.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) **[[client-server-and-remotes]]** Remember that a ModuleScript cannot require another ModuleScript one-way only; design module dependencies accordingly, since modules cannot access each other.

## Numbers
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) Starting health: **100 (MaxHealth 100)** (Example StatManager defaults in the module)
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) Defense example: **15, attack Damage 30 deals 15 after defense, 20 with 10 piercing** (Example TakeDamage calculation; blocked attacks deal 0)

## Tools
ModuleScript, newproxy(), math.clamp, task.wait

## Quotes
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-health-and-damage/2994963) "changes on one client/the server do not replicate to the others, and two modulescripts cannot access each other, only a one-way connection is allowed."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
