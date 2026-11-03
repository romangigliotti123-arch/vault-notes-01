---
title: "Emilio's ragdoll module (Easy ahh ragdolls R15 and R6)"
url: https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426
creator: Roblox DevForum
official: false
advice_density: low
date: 2024-03-04
views: 120
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Emilio's ragdoll module (Easy ahh ragdolls R15 and R6)

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) | Roblox DevForum | 120 views | 2024-03-04

## Summary
DevForum tutorial for Emilio's open-source-style ragdoll module for R15 and R6 characters. Covers installing into ReplicatedStorage, the four functions (Ragdoll, Unragdoll, TimedRagdoll, NpcRagdoll), a touch-triggered example script with debounce, and a changelog from V1.2 to V1.9.

## Tips
- [page](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) **[[code-architecture-and-frameworks]]** Store shared modules like the ragdoll module in ReplicatedStorage so both server and client scripts can require them.
- [page](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) **[[combat-and-gameplay-systems]]** Call TimedRagdoll(char, seconds) from a server Script for touch-triggered knockdowns; pass the character model and a duration.
- [page](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) **[[scripting-and-performance]]** Wrap Touched handlers in a debounce flag and check Humanoid.Health > 0 before ragdolling to avoid repeated triggers.
- [page](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) **[[combat-and-gameplay-systems]]** Use NpcRagdoll for NPCs and put a debounce on it; the author notes NPC ragdoll fixes required this in V1.7.

## Numbers
- [page](https://devforum.roblox.com/t/emilios-ragdoll-module-easy-ahh-ragdolls-r15-and-r6/2865426) Module version: **V1.9 latest listed** (Changelog lists versions 1.2 through 1.9)

## Tools
Emilio's Ragdoll Module

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
