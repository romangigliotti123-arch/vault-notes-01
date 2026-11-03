---
title: "State machines // In-Depth Tutorial"
url: https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-09-13
views: 58
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# State machines // In-Depth Tutorial

[Open](https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190) | Roblox DevForum | 58 views | 2024-09-13

## Summary
Web tutorial on using state machines in Roblox Studio scripts. Explains what a state machine is (states plus transitions), suggests sketching core states first, and shows a combat example that gates attacks by current state. Cites Elden Ring boss AI and stealth-game enemy AI as examples.

## Tips
- [page](https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190) **[[code-architecture-and-frameworks]]** Sketch the core states (e.g. Idle, Walk, Attack, Jump) and transitions on paper before coding; it keeps script logic organized and predictable.
- [page](https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190) **[[code-architecture-and-frameworks]]** Use a state variable to gate actions: check whether the character is in a disallowed state and return early instead of scattering checks across scripts.
- [page](https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190) **[[combat-and-gameplay-systems]]** Only allow attacks in states where they make sense (e.g. Idle or Walk); block attacks in other states such as stunned or jumping.
- [page](https://devforum.roblox.com/t/state-machines-in-depth-tutorial/3157190) **[[code-architecture-and-frameworks]]** Reuse the state approach for NPC and boss AI: switch behaviour by distance or boss phase rather than rewriting tangled conditionals.

## Tools
Roblox Studio

## He points to
- Elden Ring (boss state logic, cited as example)
- Metal Gear (enemy AI state logic, cited as example)
- Assassin's Creed (enemy AI state logic, cited as example)

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
