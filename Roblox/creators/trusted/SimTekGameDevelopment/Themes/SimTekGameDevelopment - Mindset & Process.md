---
title: SimTekGameDevelopment - Mindset & Process
creator: SimTekGameDevelopment
tags: [roblox, simtekgamedevelopment, theme]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# SimTekGameDevelopment: Mindset & Process

All SimTekGameDevelopment tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[development-process-and-speed]]
- 2023-01-28 [12:26](https://youtu.be/tjwI4b2ZRZk?t=746) Build a simple test arena with a blocked path and a trigger plate to verify recomputation before adding real gameplay. ([[2023-01-28 - NPC AI Advanced PathFinding - Run, Climb, Swim|NPC AI: Advanced PathFinding - Run, Climb, Swim]])
- 2024-03-09 [0:00](https://youtu.be/H7sk_T1zrD8?t=0) Check TextChatService's ChatVersion property in Explorer; new projects default to TextChatService, switch to Legacy only for old code. ([[2024-03-09 - How To Use the Text Chat Service in Roblox Studio 2024|How To Use the Text Chat Service in Roblox Studio ]])

## [[common-mistakes]]
- 2022-12-10 [4:52](https://youtu.be/mrmB0hQGCXE?t=292) Don't hard-code Y positions for terrain-placed objects; terrain height changes and hard-coded values break silently. ([[2022-12-10 - Find Terrain Height with Ray Casting Roblox Studio|Find Terrain Height with Ray Casting | Roblox Stud]])
- 2023-01-28 [3:12](https://youtu.be/tjwI4b2ZRZk?t=192) Delete the setup emote chat hook block in the copied Animate script; it causes output errors on NPCs because it is player-specific. ([[2023-01-28 - NPC AI Advanced PathFinding - Run, Climb, Swim|NPC AI: Advanced PathFinding - Run, Climb, Swim]])
- 2023-08-18 [3:27](https://youtu.be/U22nZqDmTXI?t=207) Creating a gamepass makes you own it, so delete it from your inventory before testing the purchase flow. ([[2023-08-18 - How to Make a Game Pass|How to Make a Game Pass]])
- 2024-10-12 [6:01](https://youtu.be/i2_7zT36Jeg?t=361) Use a debounce on mode switching during testing (5s), but use a long cooldown in production (~300s, as in WoW) so players can't rapidly toggle to take shots. ([[2024-10-12 - How to Create PVP and PVE Environments in Roblox Studio|How to Create PVP and PVE Environments in Roblox S]])
- 2024-11-02 [13:22](https://youtu.be/zimfV0QYV2w?t=802) Touched events on HumanoidRootPart miss by a small gap; add an invisible, non-collidable buffer part slightly larger than the wall to fire the trigger earlier. ([[2024-11-02 - How to Add Knockback to Walls for Players|How to Add Knockback to Walls for Players]])
- 2025-06-24 [22:03](https://youtu.be/4tGM1Ac5fcI?t=1323) Don't leave a follow state without an exit condition; add a timeout or distance check, since the NPC otherwise keeps following through death and respawn. ([[2025-06-24 - NPC AI - How to Create a Finite State Machine for AI|NPC AI - How to Create a Finite State Machine for ]])
- 2025-07-07 [55:45](https://youtu.be/DcLba0yVLHs?t=3345) Avoid mixing follow and attack behaviour: an NPC following one target while attacking another produces odd facing results, so clear the follow flag on attack. ([[2025-07-07 - NPC Attack Mode using Finite State Machines|NPC Attack Mode using Finite State Machines]])

## [[testing-debugging-and-qa]]
- 2021-02-15 [9:42](https://youtu.be/_ANWj69QDms?t=582) If Humanoid.Died fires multiple times, guard with a boolean flag (canDie) so the kill is only counted once. ([[2021-02-15 - Roblox Weapons System - Add Creator Tags for Kills!|Roblox Weapons System - Add Creator Tags for Kills]])
- 2023-08-18 [14:08](https://youtu.be/U22nZqDmTXI?t=848) Test the real purchase flow in the Roblox player, since Studio grants passes for free and does not keep them after death. ([[2023-08-18 - How to Make a Game Pass|How to Make a Game Pass]])
- 2023-08-18 [16:13](https://youtu.be/U22nZqDmTXI?t=973) Verify that re-buying an owned pass shows 'already own this item' with no charge, and that the pass persists after reset and rejoin. ([[2023-08-18 - How to Make a Game Pass|How to Make a Game Pass]])
- 2025-05-25 [12:42](https://youtu.be/PByZNBuob4g?t=762) Test incrementally after each small change; forgetting to return the object from a constructor is an easy-to-miss bug. ([[2025-05-25 - Object Oriented Programming in Roblox Studio|Object Oriented Programming in Roblox Studio]])
- 2025-07-07 [15:14](https://youtu.be/DcLba0yVLHs?t=914) Test each small step immediately (spawn, print, check output for errors) rather than building the whole system before running it. ([[2025-07-07 - NPC Attack Mode using Finite State Machines|NPC Attack Mode using Finite State Machines]])

Up: [[SimTekGameDevelopment - How to make successful Roblox games]]
