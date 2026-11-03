---
title: SimTekGameDevelopment - How to make successful Roblox games
tags: [roblox, simtekgamedevelopment, playbook]
videos: 25
generated: 2026-10-29
credibility: trusted
credibility_score: 8.2
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# SimTekGameDevelopment - How to make successful Roblox games

SimTekGameDevelopment teaches Roblox through short, code-first tutorials that each build one system: inventory, pathfinding, knockback, raycast weapons, FSM NPCs, DataStore saves. The method: isolate one mechanic, prototype it in a small test arena, keep logic in server ModuleScripts, use one RemoteEvent per action with exact names, prefer modern constraints over BodyMovers, wrap DataStore calls in pcall, and tune numbers by testing in a two-player test server or the real player. Growth and marketing coverage is thin; advice is almost entirely technical.

**Style:** Terse, hands-on Luau walkthroughs, one system per video, tested live in Studio with two-player test servers. Suits beginner-to-intermediate scripters who want copy-ready patterns (ModuleScripts, FSMs, constraints, metatables). Offers little on discovery, marketing, or retention strategy beyond gamepass setup and benefit persistence.

## Playbook
1. **Pick one isolated mechanic and prove it in a test arena** [[development-process-and-speed]]: Each video isolates one system (8QUJ_Qc6JTs inventory, lJktfRT2pbg pathfinding, -sQHMwuVAu4 knockback). Build the mechanic in a small test arena with a blocked path or trigger plate before adding real gameplay. Inspect existing public data (V65oLE0Wbuc) before coding against it.
2. **Model player state and pickups in server ModuleScripts** [[core-loops-and-game-design]]: Store counts in a table keyed by player and item name, incrementing the old value on pickup (8QUJ_Qc6JTs). Keep inventory logic in a server ModuleScript and require it from short item scripts. Drive pickups by part name so new resources need only a duplicated, renamed part (mrmB0hQGCXE, 10uZXhWd_Aw).
3. **Route all changes through RemoteEvents with exact names** [[client-server-and-remotes]]: Create one RemoteEvent per action in ReplicatedStorage (pickup, drop). Match WaitForChild strings exactly or the script yields forever. Send only the item name, not the whole table (bFoHE1qWe64). The client never changes inventory directly.
4. **Initialize and persist data with DataStoreService** [[data-persistence]]: Set up per-player data on PlayerAdded, keyed by UserId. Enable Studio API access first. Save on PlayerRemoving and run a periodic loop (60s live). Wrap calls in pcall and handle failed loads, which the 2025 leaderboard video does (10uZXhWd_Aw; the 2020 save video skipped pcall).
5. **Keep damage server-side and attribute kills** [[combat-and-gameplay-systems]]: The client sends only the hit target; the server applies Humanoid damage (BiaMIbrzo0Q, i2_7zT36Jeg). Before damage, remove old creator tags and add one pointing at the shooter, valid about 2s (_ANWj69QDms, DcLba0yVLHs). Guard Humanoid.Died with a canDie flag.
6. **Build NPCs with pathfinding and finite state machines** [[physics-pathfinding-and-npc-ai]]: Compute paths with PathfindingService ComputeAsync, check path.Status == Success, follow waypoints, and recompute on Blocked (lJktfRT2pbg, tjwI4b2ZRZk). Structure behaviour as an FSM with states, transitions and exit conditions (4tGM1Ac5fcI, 9rzgsXFPTjY).
7. **Use modern constraints for movement and knockback** [[genre-mechanics]]: Use LinearVelocity for constant speed, VectorForce for continuous acceleration, and AssemblyLinearVelocity for one-shot impulses (ArNJwChSU8Q). Prefer VectorForce and AngularVelocity over legacy BodyMovers for knockback (-sQHMwuVAu4). Use AlignOrientation to keep platforms level (6sgx1elbhwU).
8. **Use raycasts for hits, terrain and zones** [[physics-pathfinding-and-npc-ai]]: Raycast weapon hits with a RaycastParams blacklist and skip accessories (BiaMIbrzo0Q). Find terrain height by casting down from high above (mrmB0hQGCXE). Detect zones with GetPartBoundsInBox and play matching sound from a LocalScript (c1jFXwmRtzI, eDTbzVDm1aY).
9. **Give feedback through queued, tweened UI** [[ui-ux-design]]: Queue server messages in a FIFO table and show one tweened label per second (zmTsh66uxsI). Use a UIGridLayout with relative CellSize and numbered slots (8QUJ_Qc6JTs). Use TextChatService (H7sk_T1zrD8) with a RemoteEvent for chat-driven effects.
10. **Test each step immediately in multi-player sessions** [[testing-debugging-and-qa]]: Spawn, print and check Output after each small change rather than building the whole system first (q-kUXooTRd8). Test PVP tags and damage gating with two players in a Test Server (i2_7zT36Jeg). Use a short 5s debounce while testing.
11. **Set up a gamepass end to end** [[monetisation-gamepasses]]: Enable Allow third party sales, create the pass on the dashboard, prompt via MarketplaceService from a UI button, and grant the benefit on spawn (U22nZqDmTXI). Passing the owner ID is unnecessary; the marketplace pays the owner automatically.
12. **Price and test purchases in the real player** [[pricing]]: Use 1 Robux while testing (U22nZqDmTXI). Studio grants passes for free and does not keep them after death, so test in the Roblox player. Delete your own pass from inventory before testing, and confirm re-buy shows 'already own' with no charge.
13. **Make benefits survive respawn and rejoin** [[retention-d1-d7]]: Re-apply gamepass benefits on CharacterAdded so they survive death (U22nZqDmTXI). Reset per-character state on respawn: remove mode tags and re-add the default PVE tag so every life starts in a known state (i2_7zT36Jeg).
14. **Tune timers and save cadence for live play** [[updates-live-ops]]: Autosave every 60s, not 10s (10s was test-only in bFoHE1qWe64; 2025 recommends 60s, 30s max, 10uZXhWd_Aw). Set production mode-switch cooldowns to about 300s, WoW-style, so players can't spam shots (i2_7zT36Jeg). Clear growing accessory filter tables on long-running servers.

## Key numbers
- Autosave interval: 60s recommended, 30s max (2025-05-17, 10uZXhWd_Aw); 10s was test-only (2020-12-29, bFoHE1qWe64)
- Production mode-switch cooldown ~300s; 5s used only for testing (2024-10-12, i2_7zT36Jeg)
- Gamepass test price: 1 Robux (2023-08-18, U22nZqDmTXI)
- Gamepass revenue split: source notes conflict (creator 70% vs Roblox takes 70%); verify on the dashboard before relying on it
- Knockback speed threshold 20 studs/s; VectorForce 10000; constraint lifetime 0.2s (2023-02-03, -sQHMwuVAu4) or 0.1s (2024-11-02, zimfV0QYV2w)
- Speed pellet WalkSpeed 16 to 50 (2024-11-02, zimfV0QYV2w); gamepass benefit +16 WalkSpeed (2023-08-18)
- Pathfinding jump cleared about 3.5 studs; an 11.5-stud wall was not cleared (2021-07-04, lJktfRT2pbg)
- Raycast shot range 300 studs (2022-12-04, BiaMIbrzo0Q); 30-stud range in 2023 demo (eDTbzVDm1aY)
- Terrain pickup: ray from Y=300 down to Y=-100, offset 3 studs above hit (2022-12-10, mrmB0hQGCXE)
- Message queue: poll every 1s, tween 1s, 2s read delay (2023-01-07, zmTsh66uxsI)
- Zombie walk speeds 3 (wander) and 6 (investigate); sight 30 studs; decision loop 0.5s; respawn 5s (2025-07-28, 9rzgsXFPTjY)
- Attack interval 0.2s; post-attack cooldown about 2s; creator tag lifetime 2s (2025-07-07, DcLba0yVLHs)
- Friend-score penalty for shooting an NPC: -5 shown in test, -10 suggested (2025-07-07, DcLba0yVLHs)
- Elevator speed 10 studs/s with floors 10 studs apart (2023-09-30, 6sgx1elbhwU)
- Debris TTL 10s for spawned projectiles (2023-09-22, ArNJwChSU8Q)

## Common mistakes
- Leaving 'Enable Studio Access to API Services' off, so DataStores fail in Studio (bFoHE1qWe64, 10uZXhWd_Aw)
- Creating a gamepass without enabling third-party sales first, so purchases fail (U22nZqDmTXI)
- Testing purchases in Studio, which grants passes free and drops them on death; test in the Roblox player (U22nZqDmTXI)
- Misspelling a RemoteEvent name so WaitForChild yields forever (8QUJ_Qc6JTs)
- Mismatched leaderstats stat names, which fail silently (_ANWj69QDms)
- Hard-coding Y positions for terrain-placed objects, which break when terrain changes (mrmB0hQGCXE)
- Touched on HumanoidRootPart missing fast walls; add a slightly larger invisible buffer part (zimfV0QYV2w)
- Follow or chase state with no exit condition, so NPCs keep following through death (9rzgsXFPTjY, DcLba0yVLHs)
- Reading path waypoints without checking path.Status, or using hard-coded waypoints (lJktfRT2pbg)
- Not deleting the player-specific emote chat hook from the copied Animate script on NPCs (tjwI4b2ZRZk)

## Launch checklist
- [ ] Enable Game Settings > Security > Enable Studio Access to API Services before testing DataStores
- [ ] Enable Allow third party sales before creating any gamepass
- [ ] Create the gamepass on the creator dashboard and set price to 1 Robux while testing
- [ ] Delete your own gamepass from inventory before testing the purchase flow
- [ ] Test purchases in the Roblox player, not Studio
- [ ] Verify re-buying an owned pass shows 'already own' with no charge
- [ ] Verify the pass benefit persists after rejoin and after death
- [ ] Re-apply gamepass benefits on PlayerAdded and CharacterAdded
- [ ] Confirm every RemoteEvent name matches its WaitForChild string exactly
- [ ] Wrap all DataStore calls in pcall and handle failed loads (kick or retry)
- [ ] Save on PlayerRemoving and run an autosave loop at 60s (30s max)
- [ ] Set production mode-switch cooldowns to about 300s; keep 5s only for testing
- [ ] Confirm all damage is applied on the server; client sends only the target
- [ ] Check path.Status == Success before reading waypoints; handle no-path
- [ ] Verify leaderstats stat names match the strings used in scripts
- [ ] Check Touched handlers verify Humanoid and GetPlayerFromCharacter first
- [ ] Remove the emote chat hook from any Animate script copied onto NPCs
- [ ] Check TextChatService ChatVersion in Explorer for new projects

## How the advice changed over time
- Data saving: 2020 save tutorial skipped pcall and called it risky; 2025 leaderboard tutorial wraps DataStore calls in pcall. Prefer the 2025 approach.
- Autosave: 2020 used 10s for testing with about 60s for live; 2025 recommends 60s with 30s max. Prefer 2025 numbers.
- Knockback: 2021 talk about BodyMovers was replaced in 2023 by VectorForce and AngularVelocity; 2023-09 says LinearVelocity suits constant speed and VectorForce suits continuous acceleration.
- Chat: 2024 says new projects default to TextChatService and LegacyChat is only for old code.
- Kill credit: 2021 creator tag persisted; 2025 scripts use a roughly 2-second tag lifetime window. Prefer the 2025 window.
- Pathfinding: 2021 video had no ladder handling; 2023 adds PathfindingLinks for ladders and notes swimming needs no link.
- Cooldown guidance: 2024 contrasts 5s testing with 300s production; use the production value for launch.

## Theme notes
- [[SimTekGameDevelopment - Retention|Retention]]
- [[SimTekGameDevelopment - Monetisation|Monetisation]]
- [[SimTekGameDevelopment - Game Ideas|Game Ideas]]
- [[SimTekGameDevelopment - Studio & Scripting|Studio & Scripting]]
- [[SimTekGameDevelopment - Mindset & Process|Mindset & Process]]
- [[SimTekGameDevelopment - Games Mentioned]]
- [[SimTekGameDevelopment - Numbers & Benchmarks]]
- [[SimTekGameDevelopment - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2020-12-11 - How to Make an Inventory System in Roblox (Part 1)|How to Make an Inventory System in Roblox (Part 1)]] (3,982 views, 2020-12-11): Builds a tab-toggled bag GUI and server PickupManager ModuleScript with RemoteEvents and Touched-based pickup.
- [[2020-12-29 - How to Save Your Inventory in Roblox|How to Save Your Inventory in Roblox]] (6,380 views, 2020-12-29): Saves the inventory bag with DataStoreService on leave and on a timer, then reloads items on join.
- [[2021-02-15 - Roblox Weapons System - Add Creator Tags for Kills!|Roblox Weapons System - Add Creator Tags for Kills]] (15,183 views, 2021-02-15): Adds a creator tag so the last attacker gets kill credit, incrementing leaderstats Kills on zombie death.
- [[2021-07-04 - Path Finding For NPCs - Handling Blocked Paths In Roblox|Path Finding For NPCs - Handling Blocked Paths In ]] (7,383 views, 2021-07-04): Recomputes NPC paths with ComputeAsync when new walls trigger Blocked, and handles the no-path case.
- [[2021-07-18 - Use the HTTP Service in Roblox to Connect Your Game to External Data S|Use the HTTP Service in Roblox to Connect Your Gam]] (11,575 views, 2021-07-18): Calls a free cat-fact API from the server with HttpService and relays the result to a client via RemoteEvent.
- [[2022-12-04 - Gun with Ray Casting - How to filter out a player's accessories if bei|Gun with Ray Casting - How to filter out a player']] (7,853 views, 2022-12-04): Replaces click-target damage with RaycastParams hits that skip accessories and pass through for armor-piercing shots.
- [[2022-12-10 - Find Terrain Height with Ray Casting Roblox Studio|Find Terrain Height with Ray Casting | Roblox Stud]] (1,880 views, 2022-12-10): Places parts on uneven terrain by raycasting down from Y=300 and offsetting pickups 3 studs above the hit.
- [[2022-12-25 - Background Sound for Regions (GetPartBoundsInBox)|Background Sound for Regions (GetPartBoundsInBox)]] (3,982 views, 2022-12-25): Uses GetPartBoundsInBox to detect zone regions and plays matching ambient sound and zone name on the client.
- [[2023-01-07 - Simple Message Queue for Server to Client Messages|Simple Message Queue for Server to Client Messages]] (1,716 views, 2023-01-07): Builds a FIFO message queue where a client thread shows one tweened label per second, sliding off screen.
- [[2023-01-28 - NPC AI Advanced PathFinding - Run, Climb, Swim|NPC AI: Advanced PathFinding - Run, Climb, Swim]] (33,217 views, 2023-01-28): Covers R15 NPC pathfinding with jumps, blocked-path recompute, PathfindingLinks for ladders, and swimming.
- [[2023-02-03 - Knockback Vector Force and Angular Force Roblox Studio 2023|Knockback: Vector Force and Angular Force | Roblox]] (40,905 views, 2023-02-03): Adds pistol knockback with VectorForce and AngularVelocity constraints instead of legacy BodyMovers.
- [[2023-08-18 - How to Make a Game Pass|How to Make a Game Pass]] (1,995 views, 2023-08-18): End-to-end speed gamepass: third-party sales, dashboard setup, MarketplaceService prompt, and grant on spawn.
- [[2023-09-22 - LinearVelocity vs. VectorForce vs. AssemblyLinearVelocity in Roblox|LinearVelocity vs. VectorForce vs. AssemblyLinearV]] (62,326 views, 2023-09-22): Compares LinearVelocity, VectorForce and AssemblyLinearVelocity for projectile motion in a ball-thrower demo.
- [[2023-09-30 - Roblox Studio Tutorial How to Make Elevators with Linear Velocity & Al|Roblox Studio Tutorial: How to Make Elevators with]] (1,951 views, 2023-09-30): Builds a multi-floor elevator with LinearVelocity movement and AlignOrientation to keep the platform level.
- [[2023-12-30 - Raycasting Fundamentals in Roblox Studio Essential Tips & Techniques|Raycasting Fundamentals in Roblox Studio: Essentia]] (1,564 views, 2023-12-30): Covers raycasting basics: Beam visualization, exclude lists, CollectionService tag filters and cone sweeps.
- [[2024-02-10 - Roblox API Tutorial|Roblox API Tutorial]] (18,532 views, 2024-02-10): Uses Roblox games and game-pass APIs via HttpService and warns against unknown third-party proxies.
- [[2024-02-19 - Metadata and Metamethod Fundamentals in Roblox Studio (Lua)|Metadata and Metamethod Fundamentals in Roblox Stu]] (800 views, 2024-02-19): Explains metatables and metamethods (__add, __lt, __index, __newindex), moved into a required ModuleScript.
- [[2024-03-09 - How To Use the Text Chat Service in Roblox Studio 2024|How To Use the Text Chat Service in Roblox Studio ]] (8,360 views, 2024-03-09): Switches to TextChatService, passes chat to the server via RemoteEvent, and recolors messages with rich text.
- [[2024-10-12 - How to Create PVP and PVE Environments in Roblox Studio|How to Create PVP and PVE Environments in Roblox S]] (36,539 views, 2024-10-12): Builds a PVP/PVE toggle with a client cooldown, CollectionService state tags, and tag-gated weapon damage.
- [[2024-11-02 - How to Add Knockback to Walls for Players|How to Add Knockback to Walls for Players]] (31,636 views, 2024-11-02): Knocks back fast runners into walls using a speed pellet, a buffer part, and constraint-based forces.
- [[2025-05-17 - Datastore - Save Your Leaderboard!|Datastore - Save Your Leaderboard!]] (8,294 views, 2025-05-17): Builds a leaderboard with leaderstats, pcall DataStore save and load, autosave and save on leave.
- [[2025-05-25 - Object Oriented Programming in Roblox Studio|Object Oriented Programming in Roblox Studio]] (25,374 views, 2025-05-25): Teaches OOP in Luau with metatable inheritance and Dog, GuardDog and Puppy module-script classes.
- [[2025-06-24 - NPC AI - How to Create a Finite State Machine for AI|NPC AI - How to Create a Finite State Machine for ]] (18,863 views, 2025-06-24): Builds an NPC finite state machine (idle, greet, follow) driven by chat-based friendship points.
- [[2025-07-07 - NPC Attack Mode using Finite State Machines|NPC Attack Mode using Finite State Machines]] (17,151 views, 2025-07-07): Turns a social NPC into a defensive attacker with attack and cooldown FSM states and a built-in gun.
- [[2025-07-28 - Zombie AI and Finite State Machines with Transition Hooks|Zombie AI and Finite State Machines with Transitio]] (18,428 views, 2025-07-28): Builds a zombie FSM (wander, investigate, chase) with on-enter and on-exit transition hooks and sight raycasts.
