---
title: "NPC AI - How to Create a Finite State Machine for AI"
url: https://youtu.be/4tGM1Ac5fcI
creator: SimTek Game Development
official: false
advice_density: medium
date: 2025-06-24
views: 18863
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# NPC AI - How to Create a Finite State Machine for AI

[Watch](https://youtu.be/4tGM1Ac5fcI) | SimTekGameDevelopment | 18,863 views | 2025-06-24

## Summary
Builds a finite state machine for a Roblox NPC in Luau using OOP. Covers a states table, a set_state function that resets flags, per-state functions (idle, greet, follow), a dispatch loop, and event-driven transitions from player chat. The NPC greets a player once friendship is reached, then follows them.

## Tips
- [4:09](https://youtu.be/4tGM1Ac5fcI?t=249) **[[code-architecture-and-frameworks]]** Route every state change through one set_state function so transitions and resets happen in a single place.
- [5:35](https://youtu.be/4tGM1Ac5fcI?t=335) **[[code-architecture-and-frameworks]]** In set_state, return early if the new state equals the current state so re-entering the same state runs no code.
- [6:15](https://youtu.be/4tGM1Ac5fcI?t=375) **[[code-architecture-and-frameworks]]** Reset state-specific flags inside set_state on every transition so stale flags don't carry into the next state.
- [7:36](https://youtu.be/4tGM1Ac5fcI?t=456) **[[luau-language-and-types]]** When state functions sit in a nested table, pass self explicitly with dot-calls; colon syntax gets confusing at deeper levels.
- [15:12](https://youtu.be/4tGM1Ac5fcI?t=912) **[[code-architecture-and-frameworks]]** Dispatch the current state via a lookup table of state functions, guard for nil, and warn on unknown states as the machine grows.
- [16:34](https://youtu.be/4tGM1Ac5fcI?t=994) **[[code-architecture-and-frameworks]]** Keep the periodic decide loop dispatch-only; let states and external events trigger transitions, not the loop itself.
- [17:16](https://youtu.be/4tGM1Ac5fcI?t=1036) **[[physics-pathfinding-and-npc-ai]]** Drive NPC transitions from external events like chat by comparing friendship before and after the event (was friend vs is friend).
- [20:01](https://youtu.be/4tGM1Ac5fcI?t=1201) **[[physics-pathfinding-and-npc-ai]]** Use a one-time flag for repeated dialogue lines so the NPC doesn't re-speak every tick while in the same state.
- [22:03](https://youtu.be/4tGM1Ac5fcI?t=1323) **[[common-mistakes]]** Don't leave a follow state without an exit condition; add a timeout or distance check, since the NPC otherwise keeps following through death and respawn.
- [0:00](https://youtu.be/4tGM1Ac5fcI?t=0) **[[scripting-and-performance]]** Remove debug print statements from the output window once the system works; spammed prints bury real errors.

## Numbers
- [0:00](https://youtu.be/4tGM1Ac5fcI?t=0) NPC states in example FSM: **3 (idle, greet, follow)**
- [13:48](https://youtu.be/4tGM1Ac5fcI?t=828) Greet state delay: **2 seconds**
- [14:31](https://youtu.be/4tGM1Ac5fcI?t=871) Original decide-action loop interval: **every 3 seconds**
- [17:57](https://youtu.be/4tGM1Ac5fcI?t=1077) Friend score increase per chat: **+1 per talk**

## Tools
Roblox Studio, Luau, Output window, Explorer, Global search (Ctrl+Shift+F)

## He points to
- Previous videos in NPC series (base NPC, social NPC)

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
