---
title: BRicey - How to make successful Roblox games
tags: [roblox, bricey, playbook]
videos: 25
generated: 2026-10-29
credibility: trusted
credibility_score: 8.0
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BRicey - How to make successful Roblox games

BRicey's playbook is engineering-first. Keep scope small and ship a game that mostly works, then refactor as needed. Keep the server authoritative and treat every client request as untrusted. Centralise logic in small single-purpose ModuleScripts instead of per-part scripts. Store all player data in one UserId-keyed session table, saved through pcall-wrapped DataStore calls, with saves on PlayerRemoving and BindToClose. Prefer composition over inheritance, and clean up connections and parts with Trove, Maid, or Janitor. Design, marketing, monetisation, and live ops are not covered in these videos.

**Style:** Practical, code-architecture-focused tutorials from a working developer. Stresses YAGNI, refactoring, and shipping over perfection, with concrete Luau patterns and Studio demos. Best for intermediate scripters building systems-heavy games such as tycoons, combat, and plot-based building. Light on game design, marketing, and monetisation.

## Playbook
1. **Scope the idea to a shippable core** [[development-process-and-speed]]: Build only what you need now (YAGNI). Do not architect the full game upfront because ideas change during development. Fail fast rather than designing like NASA SLS. Example systems in these videos: tycoon, combat, and plot-based building.
2. **Set up tooling before building** [[version-control-and-tooling]]: Install Git, GitHub Desktop, VS Code, and the Rojo extension and plugin. Rojo syncs file-system scripts into Studio via a localhost server on default port 34872. Use production, alpha, and beta branches so test code does not break the main build.
3. **Keep the server thin and push logic into modules** [[code-architecture-and-frameworks]]: Keep the server script thin. Put logic in single-purpose ModuleScripts such as PlotManager, PlotSpawnPool, and ClientPlacer. Use module-per-class: Class.__index, Class.new returning setmetatable, colon methods. Add OOP only when state is needed.
4. **Assemble classes from has-a components** [[code-architecture-and-frameworks]]: Build reusable components (Engine, Wheel) and combine them per class. Avoid deep is-a trees such as Car/Plane/Boat. Do not inherit from Roblox Instances. Hold the model in the class table and pass it into Class.new so one class can drive many models.
5. **Centralise tagged behaviour with CollectionService** [[code-architecture-and-frameworks]]: Replace one script per part (e.g. landmines) with a single server script that handles every tagged part. Use GetInstanceAddedSignal and GetInstanceRemovedSignal to add or remove behaviour, and toggle tags at runtime to change it.
6. **Store all player data in one keyed table** [[data-persistence]]: Hold session data in one table keyed by UserId and store it under a single DataStore key. Set defaults on PlayerAdded. Overwrite session data only if the pcall succeeded and data exists. Expose ChangeValue(player, name, value) as the only write interface for other scripts.
7. **Save on exit and restore state safely** [[data-persistence]]: Save on PlayerRemoving and BindToClose. The 2024 method tracks a players-remaining counter so BindToClose waits for saves to finish. Connect handlers without parentheses. Create unlockable objects before replaying saved unlocks, or publishes are missed.
8. **Treat the client as hostile** [[anti-exploit-and-security]]: With FilteringEnabled, all client state changes must go through remotes in ReplicatedStorage. Re-check every request on the server, e.g. money >= cost before subtracting. OnServerEvent callbacks always receive the player as the first argument. Return a success boolean from purchase RemoteFunctions.
9. **Use promises and cleanup modules for async and lifetimes** [[scripting-and-performance]]: Chain round stages with Promise andThen, finally, and catch so one error does not kill the loop. Use Trove:Connect and Trove:Destroy (or Maid, Janitor) so connections and parts are released. Unreleased connections and parts cause memory leaks.
10. **Validate plot placement with bounds and re-check on the server** [[building-and-level-design]]: Transform the object's four corners into plot local space and check abs(x) and abs(z) against half the plot size (base plot 50 x 1 x 50 studs). Use OverlapParams with an include filter and GetPartBoundsInBox. Client shows blue or red preview; the server re-validates in place.
11. **Test saves in a published build** [[testing-debugging-and-qa]]: Test DataStore behaviour in a published build for accurate results. Disable Studio API access after DataStore testing to stop Studio lagging. Add catch blocks that warn with a clean stack trace, and warn on failed checks during debugging.
12. **Provision spawn points with a buffer** [[building-and-level-design]]: Provide at least 4 more spawn markers than max players, since Roblox can reallocate players and spawn extras. Make markers invisible debug parts with CanCollide off and Anchored on so they do not interfere with physics.
13. **Growth: not covered in these videos** [[mindset-and-strategy]]: None of the 12 videos cover discovery, titles, thumbnails, ads, or influencer marketing. The only growth-adjacent advice is to release a game that mostly works and that players enjoy, rather than polishing indefinitely.
14. **Live ops: refactor and ship continuously** [[development-process-and-speed]]: Refactor freely, since guessing a perfect structure up front costs more. Comment why you do something, not what the code does, and skip comments in solo codebases. Updates and events are not covered in these videos.

## Key numbers
- Rojo default server port: 34872 (localhost)
- Tag demo timing: 5 s before AddTag, 5 s before RemoveTag
- Moving-part demo: every 10 s, 2 studs
- Cleanup demo: object destroyed after 3 s
- Tool script cited as a mistake: ~1000 lines
- PlotSpawnPool implementation: about 23 lines
- Spawn points: at least 4 more than max players
- Base plot template: 50 x 1 x 50 studs
- Placement bounds: abs(x) and abs(z) checked against half plot size
- Plot series part 4 views at upload (NK8VHcNHJG4): 9414
- Series span: 12 videos from 2020-05 to 2024-04

## Common mistakes
- Putting a copy of a script in every part; behaviour changes then require editing each copy (Vi2FckNJv9w).
- Forgetting connections and parts after an object is done, causing leaks and ongoing work (2Msrw5w5cTs).
- Running a round loop as a bare while-true, so one runtime error stops the whole loop (TeMGAqzZrDc).
- Calling PlayerAdded or PlayerRemoving handlers with parentheses instead of passing the function (eMKYqdSvoMs, TgZI48DTNqE).
- Trusting the client: an unprotected RemoteEvent accepts arbitrary values such as millions of currency (Zh-Jd4xEc2g).
- Overwriting session data when a DataStore call failed instead of falling back to defaults (eMKYqdSvoMs).
- Using a deep is-a inheritance tree (Car, Plane, Boat) for varied objects (KNT-vjqB_qI).
- Writing a single ~1000-line tool script instead of splitting into modules (MyK4o2pIpQw).
- Relying on the client placement preview alone; exploiters can bypass it (1XJRZ1x2x4g).
- Replaying saved unlocks before unlockable objects exist, so publishes are missed (TgZI48DTNqE).

## Launch checklist
- [ ] Cut scope to a playable core and defer extra features (YAGNI).
- [ ] Set up Git branches production, alpha, and beta.
- [ ] Install Rojo and sync file-system scripts into Studio.
- [ ] Keep the project folder in a stable location such as Documents.
- [ ] Store all player data in one UserId-keyed table under a single DataStore key.
- [ ] Wrap GetAsync and SetAsync in pcall; set defaults on PlayerAdded.
- [ ] Save on PlayerRemoving and BindToClose, using a players-remaining counter.
- [ ] Put RemoteEvents and RemoteFunctions in ReplicatedStorage.
- [ ] Re-check every remote request on the server before applying it.
- [ ] Centralise tagged or shared logic; avoid per-part script copies.
- [ ] Chain async stages with promises and end each chain with catch.
- [ ] Release connections and parts with Trove, Maid, or Janitor.
- [ ] Re-validate plot placement on the server.
- [ ] Provide at least 4 spawn points above max players.
- [ ] Make spawn markers CanCollide off and Anchored on.
- [ ] Test DataStore saves in a published build, then disable Studio API access.
- [ ] Pivot models before parenting them into Workspace.
- [ ] Ship once the game mostly works and players enjoy it.

## How the advice changed over time
- 2020 tutorials (eMKYqdSvoMs, Zh-Jd4xEc2g) covered basic single-table saving and remotes with saves on PlayerRemoving only.
- 2021 tycoon save video (TgZI48DTNqE) added BindToClose and replaying unlocks on rejoin.
- 2021-2022 shifted to architecture: composition over inheritance, CollectionService, Trove/Maid/Janitor, Promises, Rojo and Git.
- 2022 code-style video (MyK4o2pIpQw) stressed YAGNI, refactoring freely, and shipping over perfection.
- 2024 plot series (NK8VHcNHJG4) refined shutdown handling with a players-remaining counter; where it conflicts with the 2020 PlayerRemoving-only advice, prefer the 2024 method.
- Remote and sanity-check advice from 2020 has not changed; later videos reinforce server re-validation.

## Theme notes
- [[BRicey - Retention|Retention]]
- [[BRicey - Monetisation|Monetisation]]
- [[BRicey - Game Ideas|Game Ideas]]
- [[BRicey - Studio & Scripting|Studio & Scripting]]
- [[BRicey - Mindset & Process|Mindset & Process]]
- [[BRicey - Games Mentioned]]
- [[BRicey - Numbers & Benchmarks]]
- [[BRicey - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2020-04-10 - OOP in Roblox 4 - Metatables in Module Scripts|OOP in Roblox #4 - Metatables in Module Scripts]] (22,406 views, 2020-04-10): Tutorial on combining module scripts with metatables for OOP in Roblox. Shows a Base class with a Ne
- [[2020-05-13 - Advanced Datastore Tutorial - Roblox Studio|Advanced Datastore Tutorial - Roblox Studio]] (15,499 views, 2020-05-13): Builds a ModuleScript save system keyed by UserId with pcall-wrapped DataStore calls and a ChangeValue API.
- [[2020-09-27 - All about the NEW Raycasting Functions in Roblox Studio (workspaceRayc|All about the NEW Raycasting Functions in Roblox S]] (30,299 views, 2020-09-27): Tutorial on Roblox's newer raycasting API: workspace:Raycast(origin, direction, optional RaycastPara
- [[2020-12-21 - Intro to Remote Events & Functions (and Sanity Checks)|Intro to Remote Events & Functions (and Sanity Che]] (17,341 views, 2020-12-21): RemoteEvent and RemoteFunction basics, player-first arguments, and server sanity checks against exploiters.
- [[2020-12-23 - My CUSTOM Remote Event & Function Module in Roblox Studio|My CUSTOM Remote Event & Function Module in Roblox]] (10,706 views, 2020-12-23): Showcase and explanation of a custom "Remote Messenger" module that replaces many RemoteEvents/Remot
- [[2021-01-04 - Using Knit & Roact to COMPLETELY Rework my Roblox Game! - Tallest Towe|Using Knit & Roact to COMPLETELY Rework my Roblox ]] (20,306 views, 2021-01-04): Devlog for Tallest Tower: the creator reworked the project using Knit (services/controllers/componen
- [[2021-01-17 - How to use Attributes to create CUSTOM properties in Roblox Studio|How to use Attributes to create CUSTOM properties ]] (12,845 views, 2021-01-17): Tutorial on Roblox Studio Attributes (beta at the time): adding custom typed properties to instances
- [[2021-01-24 - How to make a REALISTIC Gun with FastCast Travel Time, Bullet Drop, an|How to make a REALISTIC Gun with FastCast: Travel ]] (114,586 views, 2021-01-24): Tutorial on building a realistic gun in Roblox Studio using the FastCast: Redux module. Covers tool 
- [[2021-03-21 - How to setup Rojo, VSCode, and Git for professional Roblox Studio Deve|How to setup Rojo, VSCode, and Git for professiona]] (69,183 views, 2021-03-21): Sets up Git, VS Code, and Rojo to sync file-system scripts into Studio professionally.
- [[2021-04-03 - Composition Over Inheritance - OOP in Roblox Studio|Composition Over Inheritance - OOP in Roblox Studi]] (35,218 views, 2021-04-03): Uses has-a components like Engine and Wheel instead of deep is-a inheritance for scalable vehicles.
- [[2021-06-12 - Organizing your Game with Tags and CollectionService - Roblox Studio|Organizing your Game with Tags and CollectionServi]] (36,237 views, 2021-06-12): Replaces per-part landmine scripts with one CollectionService tag-driven server script.
- [[2021-06-29 - How to make a Tycoon in Roblox 2 - Component Organization System|How to make a Tycoon in Roblox #2 - Component Orga]] (84,830 views, 2021-06-29): Part 2 of a Roblox tycoon series: implements the component pattern using CollectionService tags. Cov
- [[2021-08-09 - How to make a Tycoon in Roblox 8 - Saving Player Data READ PINNED COMM|How to make a Tycoon in Roblox #8 - Saving Player ]] (29,971 views, 2021-08-09): Tycoon save system with session data, BindToClose, and replaying purchased unlocks on rejoin.
- [[2022-04-16 - How to make a Tycoon in Roblox 11 - Gamepasses|How to make a Tycoon in Roblox #11 - Gamepasses]] (15,934 views, 2022-04-16): Tutorial on adding a gamepass to a Roblox tycoon: creating the pass on the Creator Dashboard, a reus
- [[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]] (14,667 views, 2022-04-30): Tutorial on adding Roblox developer products (repeatable purchases) to a tycoon: creating the produc
- [[2022-05-28 - How to use Badges in Roblox! (Plus some scripting tips)|How to use Badges in Roblox! (Plus some scripting ]] (15,482 views, 2022-05-28): Tutorial on implementing Roblox badges: creating a badge in Studio (free, zero Robux), awarding via 
- [[2022-06-19 - How to use Promises (and why you should) in Roblox Development|How to use Promises (and why you should) in Roblox]] (46,283 views, 2022-06-19): Promises keep round loops alive through errors and make cancellable delays and tweens manageable.
- [[2022-08-21 - Maid, Trove, Janitor - Cleanup Modules you never knew you needed in Ro|Maid, Trove, Janitor - Cleanup Modules you never k]] (37,233 views, 2022-08-21): Trove, Maid, and Janitor clean up connections and parts so your game stops leaking memory.
- [[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]] (96,308 views, 2022-09-23): Organise scripts, use OOP only when state exists, refactor often, and ship before perfect.
- [[2023-04-14 - Creating an Intelligent Delivery Drone with Finite State Machines 1 -|Creating an Intelligent Delivery Drone with Finite]] (13,447 views, 2023-04-14): Part 1 of a Roblox tutorial building an autonomous delivery drone using a finite state machine (FSM)
- [[2023-06-10 - How to make an AI LASER TURRET in Roblox Studio 1 - Turret Setup and K|How to make an AI LASER TURRET in Roblox Studio #1]] (17,688 views, 2023-06-10): Part 1 of a two-part series building an AI laser turret in Roblox Studio. Covers model setup (anchor
- [[2024-02-17 - How to create a Plot Placement System in Roblox 1 - Plots & Players|How to create a Plot Placement System in Roblox #1]] (56,099 views, 2024-02-17): Plot building part 1: plot templates, per-player cloning, spawn pool, and a B-key placer.
- [[2024-03-02 - How to create a Plot Placement System in Roblox 2 - Placing stuff!|How to create a Plot Placement System in Roblox #2]] (18,265 views, 2024-03-02): Part 2 of a Roblox plot placement tutorial. Builds a client-side ghost preview of a model (raycast f
- [[2024-03-30 - How to create a Plot Placement System in Roblox 3 - Validation|How to create a Plot Placement System in Roblox #3]] (9,547 views, 2024-03-30): Bounding-box placement validation with blue and red previews, re-checked on the server.
- [[2024-04-14 - How to create a Plot Placement System in Roblox 4 - Data Saving and Se|How to create a Plot Placement System in Roblox #4]] (9,414 views, 2024-04-14): Serialises plot objects into a UserId DataStore key and restores them safely around shutdown.
