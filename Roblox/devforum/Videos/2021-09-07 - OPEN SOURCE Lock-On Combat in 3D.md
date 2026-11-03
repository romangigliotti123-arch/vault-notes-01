---
title: "[OPEN SOURCE] Lock-On Combat in 3D"
url: https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-09-07
views: 132
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [OPEN SOURCE] Lock-On Combat in 3D

[Open](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) | Roblox DevForum | 132 views | 2021-09-07

## Summary
Open-source template walkthrough for a 3D lock-on melee combat system in Roblox. Explains the Zelda/For Honor-style targeting concept, contrasts it with shiftlock combat, lists template mechanics (guard via mouse, stamina, fake attacks, parries), known issues (1v1 bias, no NPC support, outdated RaycastHitbox V3), and optimization advice.

## Tips
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[combat-and-gameplay-systems]]** Lock-on targeting removes aim-by-camera skill, letting combat depth come from guard positioning, openings and timing instead of shiftlock positioning.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[core-loops-and-game-design]]** Lock-on enables slow, methodical combat that shiftlock combat makes hard to design, since shiftlock tends to reduce games to jump-position-attack.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[combat-and-gameplay-systems]]** Lock-on combat is inherently 1v1-oriented; teaming is very difficult or impossible to balance with this system, so plan modes around it.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[scripting-and-performance]]** Replace loop-based attack cooldowns with task.delay() or multithreading; loop-style cooldowns are very inefficient and can cause major lag.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[optimization-and-streaming]]** Render block animations via a custom system that updates on angle change rather than per-frame checks, the biggest optimization for lock-on combat.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[client-server-and-remotes]]** Mouse input events were sent every 0.1 seconds in the template; this is a possible optimization target to reduce remote traffic.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[testing-debugging-and-qa]]** For NPC combat, have testers play and record their strategies, then have NPCs imitate them; the template does not support NPCs out of the box.
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) **[[version-control-and-tooling]]** The template uses RaycastHitboxV3 by Swordphin123; upgrading to V4 may need rescripting.

## Numbers
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) Mouse input send interval: **0.1 seconds** (Template sends mouse input events every 0.1 s; flagged as optimization target)

## Games
- **The Legend of Zelda: Ocarina of Time**: Popularised the term Z-targeting/lock-on for guiding avatar strikes toward a chosen enemy in 3D.
- **For Honor**: Uses lock-on targeting; cited as a strong example of lock-on combat design.
- **Sword Fight on the Heights**: Linked-sword melee example the author cites as an older, limited melee design.

## Tools
RaycastHitboxV3 (Swordphin123), Roblox Studio

## He points to
- Lock-On demo place: roblox.com/games/7354346829
- Raycast Hitbox 4.01 DevForum post

## Quotes
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) "With a lock-on system, you remove that element entirely. This allows for numerous new design possibilities, and let's the concepts be more explored."
- [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506) "The loop style is extremely inefficient and will cause major lag throughout your game."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
