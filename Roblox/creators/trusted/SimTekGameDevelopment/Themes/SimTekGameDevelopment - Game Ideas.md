---
title: SimTekGameDevelopment - Game Ideas
creator: SimTekGameDevelopment
tags: [roblox, simtekgamedevelopment, theme]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# SimTekGameDevelopment: Game Ideas

All SimTekGameDevelopment tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[trend-research-and-validation]]
- 2024-02-10 [2:55](https://youtu.be/V65oLE0Wbuc?t=175) Use Roblox's public games API docs (Swagger UI) to explore endpoints before writing code; test requests manually first. ([[2024-02-10 - Roblox API Tutorial|Roblox API Tutorial]])

## [[core-loops-and-game-design]]
- 2020-12-11 [7:48](https://youtu.be/8QUJ_Qc6JTs?t=468) Store per-player item counts in a table keyed by player and item name, incrementing the old value on pickup. ([[2020-12-11 - How to Make an Inventory System in Roblox (Part 1)|How to Make an Inventory System in Roblox (Part 1)]])
- 2024-11-02 [0:00](https://youtu.be/zimfV0QYV2w?t=0) Gate a mechanic on player speed (linear velocity magnitude > ~20 studs/s) so knockback only triggers when running fast, not during normal movement. ([[2024-11-02 - How to Add Knockback to Walls for Players|How to Add Knockback to Walls for Players]])
- 2024-11-02 [4:09](https://youtu.be/zimfV0QYV2w?t=249) Make a speed pellet using a neon, anchored, non-collidable part with CanTouch and CanQuery on, then destroy it on touch after setting WalkSpeed (e.g. 16 to 50). ([[2024-11-02 - How to Add Knockback to Walls for Players|How to Add Knockback to Walls for Players]])
- 2025-05-17 [1:02](https://youtu.be/10uZXhWd_Aw?t=62) Build a generic pickup script driven by part name so new resources (wood, grass, stone) are added by duplicating a part and renaming it. ([[2025-05-17 - Datastore - Save Your Leaderboard!|Datastore - Save Your Leaderboard!]])
- 2025-07-07 [44:45](https://youtu.be/DcLba0yVLHs?t=2685) Decouple the attack loop from the AI decision tick: run firing in a task.spawn while loop gated by state, checking target and self health each shot, with about 0.2 s between shots. ([[2025-07-07 - NPC Attack Mode using Finite State Machines|NPC Attack Mode using Finite State Machines]])
- 2025-07-07 [48:14](https://youtu.be/DcLba0yVLHs?t=2894) Use a debounce flag in cooldown so the speech bubble and state transition run only once, then reset the flag after a short task.delay (about 2 s). ([[2025-07-07 - NPC Attack Mode using Finite State Machines|NPC Attack Mode using Finite State Machines]])

## [[genre-mechanics]]
- 2021-07-04 [18:13](https://youtu.be/lJktfRT2pbg?t=1093) Pathfinding jump only clears about 3.5 studs in the speaker's test even though the character can jump higher; keep jumpable obstacles low or expect NPCs to get stuck. ([[2021-07-04 - Path Finding For NPCs - Handling Blocked Paths In Roblox|Path Finding For NPCs - Handling Blocked Paths In ]])
- 2023-02-03 [0:00](https://youtu.be/-sQHMwuVAu4?t=0) Use VectorForce and AngularVelocity constraints for knockback rather than legacy BodyMovers; both need an Attachment on the target's HumanoidRootPart. ([[2023-02-03 - Knockback Vector Force and Angular Force Roblox Studio 2023|Knockback: Vector Force and Angular Force | Roblox]])
- 2023-09-30 [0:00](https://youtu.be/6sgx1elbhwU?t=0) Use physics constraints (LinearVelocity) instead of tweening for moving platforms; forces are more realistic but can misbehave if parts are heavy or oriented oddly. ([[2023-09-30 - Roblox Studio Tutorial How to Make Elevators with Linear Velocity & Al|Roblox Studio Tutorial: How to Make Elevators with]])

Up: [[SimTekGameDevelopment - How to make successful Roblox games]]
