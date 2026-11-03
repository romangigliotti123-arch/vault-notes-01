---
title: "NPC Attack Mode using Finite State Machines"
url: https://youtu.be/DcLba0yVLHs
creator: SimTek Game Development
official: false
advice_density: medium
date: 2025-07-07
views: 17151
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# NPC Attack Mode using Finite State Machines

[Watch](https://youtu.be/DcLba0yVLHs) | SimTekGameDevelopment | 17,151 views | 2025-07-07

## Summary
Tutorial extending a social NPC class into a defensive NPC using Lua metatable inheritance and a finite state machine with attack and cooldown states. Covers health-based attacker detection via the creator tag, a gun built into the NPC, and overriding set_state to break following when attacking.

## Tips
- [0:00](https://youtu.be/DcLba0yVLHs?t=0) **[[code-architecture-and-frameworks]]** Extend NPC behaviour with subclasses: require the parent module and set metatables so the child reuses parent methods instead of duplicating code.
- [9:41](https://youtu.be/DcLba0yVLHs?t=581) **[[luau-language-and-types]]** Use a __index metamethod on a class and a states table whose metatable falls back to the parent's states, so child classes inherit state functions.
- [11:07](https://youtu.be/DcLba0yVLHs?t=667) **[[code-architecture-and-frameworks]]** Keep a static instances table keyed by model to track every object created from a class.
- [15:14](https://youtu.be/DcLba0yVLHs?t=914) **[[testing-debugging-and-qa]]** Test each small step immediately (spawn, print, check output for errors) rather than building the whole system before running it.
- [16:37](https://youtu.be/DcLba0yVLHs?t=997) **[[combat-and-gameplay-systems]]** Attribute damage with a creator tag: untag the humanoid, then tag it with the attacker before damage, so kills credit the right player; tag lasts about 2 seconds.
- [30:17](https://youtu.be/DcLba0yVLHs?t=1817) **[[combat-and-gameplay-systems]]** Apply a negative friend-score penalty (he suggests about -5 to -10) when an NPC is shot, so the player cannot easily recover friendship.
- [42:01](https://youtu.be/DcLba0yVLHs?t=2521) **[[combat-and-gameplay-systems]]** Fire NPC weapons directly inside the NPC script instead of messaging a separate weapon script; fewer moving parts, though less flexible.
- [44:45](https://youtu.be/DcLba0yVLHs?t=2685) **[[core-loops-and-game-design]]** Decouple the attack loop from the AI decision tick: run firing in a task.spawn while loop gated by state, checking target and self health each shot, with about 0.2 s between shots.
- [48:14](https://youtu.be/DcLba0yVLHs?t=2894) **[[core-loops-and-game-design]]** Use a debounce flag in cooldown so the speech bubble and state transition run only once, then reset the flag after a short task.delay (about 2 s).
- [52:16](https://youtu.be/DcLba0yVLHs?t=3136) **[[code-architecture-and-frameworks]]** Override set_state and compare previous and new state to clear flags such as following and attack target when the NPC changes state, avoiding conflicting behaviour.
- [0:40](https://youtu.be/DcLba0yVLHs?t=40) **[[version-control-and-tooling]]** Set a model's Humanoid DisplayDistanceType to None to hide overhead name labels that clutter NPC speech bubbles.
- [55:45](https://youtu.be/DcLba0yVLHs?t=3345) **[[common-mistakes]]** Avoid mixing follow and attack behaviour: an NPC following one target while attacking another produces odd facing results, so clear the follow flag on attack.

## Numbers
- [44:45](https://youtu.be/DcLba0yVLHs?t=2685) attack interval: **0.2 seconds between shots** (rapid-fire loop for defensive NPC pistol, suggested config value)
- [49:34](https://youtu.be/DcLba0yVLHs?t=2974) cooldown duration: **about 2 seconds** (time in cooldown state before returning to idle)
- [19:20](https://youtu.be/DcLba0yVLHs?t=1160) creator tag lifetime: **2 seconds** (kill credit window after damage in sword and pistol scripts)
- [30:17](https://youtu.be/DcLba0yVLHs?t=1817) friend score penalty: **-5 shown in test; -10 suggested** (applied when player shoots the NPC)

## Tools
Roblox Studio, Tag Editor plugin, Toolbox, Output window

## He points to
- Creator tag / assists video by the same creator (linked, not named)

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[luau-language-and-types]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
