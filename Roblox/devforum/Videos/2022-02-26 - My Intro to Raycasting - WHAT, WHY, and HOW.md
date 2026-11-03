---
title: "My Intro to Raycasting - WHAT, WHY, and HOW"
url: https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-02-26
views: 176
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# My Intro to Raycasting - WHAT, WHY, and HOW

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977) | Roblox DevForum | 176 views | 2022-02-26

## Summary
Intro tutorial on raycasting in Roblox: what it is (workspace:Raycast from origin along direction returning RaycastResult), common uses (guns, NPC line-of-sight, wall checks, knives), and RaycastParams usage with Whitelist/Blacklist FilterType and FilterDescendantsInstances.

## Tips
- [page](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977) **[[combat-and-gameplay-systems]]** Use workspace:Raycast for hitscan weapons; the speaker says it gives extra accuracy and is the basis for FastCast-style bullet physics.
- [page](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977) **[[scripting-and-performance]]** Pass a RaycastParams object as the third argument to workspace:Raycast to control which instances are hit.
- [page](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977) **[[scripting-and-performance]]** Set RaycastParams.FilterType to Whitelist with FilterDescendantsInstances to hit only specific objects, or Blacklist to ignore them.
- [page](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977) **[[ai-and-tools]]** Use raycasts for NPC line-of-sight checks, asking whether a player is visible before the NPC reacts.

## Tools
workspace:Raycast, RaycastParams, RaycastResult

## Topics
[[ai-and-tools]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
