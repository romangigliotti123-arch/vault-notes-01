---
title: xtb7-dev - Studio & Scripting
creator: xtb7-dev
tags: [roblox, xtb7-dev, theme]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# xtb7-dev: Studio & Scripting

All xtb7-dev tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2022-11-17 [2:56](https://youtu.be/k2p9KMrlSAA?t=176) Use humanoid.MoveToFinished:Wait() before stopping the animation so the animation stops when the character arrives. ([[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]])
- 2023-01-07 [0:28](https://youtu.be/DIz1Nk7YOUo?t=28) Put input-handling code in a LocalScript (e.g. StarterPlayerScripts); UserInputService and ContextActionService only work on the client. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [1:08](https://youtu.be/DIz1Nk7YOUo?t=68) Use UserInputService.InputBegan with the gameProcessed boolean to ignore inputs already handled by the game, such as UI clicks. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [4:20](https://youtu.be/DIz1Nk7YOUo?t=260) Name ContextActionService actions descriptively (e.g. 'change part colour'), not after the key used to trigger them. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [5:43](https://youtu.be/DIz1Nk7YOUo?t=343) BindAction accepts multiple KeyCodes or UserInputTypes, so one action can respond to several inputs. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [6:25](https://youtu.be/DIz1Nk7YOUo?t=385) ContextActionService fires on Begin, Change and End states; check inputState == Enum.UserInputState.Begin to act once per press. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [9:19](https://youtu.be/DIz1Nk7YOUo?t=559) Call ContextActionService:UnbindAction(name) to stop an action once it is no longer needed; unbound actions cost nothing when inputs occur. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-01-07 [12:24](https://youtu.be/DIz1Nk7YOUo?t=744) Prefer ContextActionService over UserInputService for input only valid in certain states; UserInputService handler runs on every InputBegan, hurting performance as logic grows. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-02-11 [1:23](https://youtu.be/0TpwPpULXxU?t=83) Use RunService:BindToRenderStep with Enum.RenderPriority.Camera.Value + 1 (or 201) so your camera changes aren't overridden by Roblox. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-02-11 [2:50](https://youtu.be/0TpwPpULXxU?t=170) Set camera.CameraType to Scriptable, otherwise custom camera changes won't take effect. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-02-11 [3:31](https://youtu.be/0TpwPpULXxU?t=211) Combine CFrames with multiplication (*), not addition; adding offsets every frame with + causes runaway drift. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-02-11 [4:32](https://youtu.be/0TpwPpULXxU?t=272) Put the camera LocalScript in StarterCharacterScripts so it doesn't error when the character dies and no character exists. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-02-11 [8:01](https://youtu.be/0TpwPpULXxU?t=481) CFrame.Angles axes are not intuitive: X tilts up/down, Y turns left/right, Z tilts/rolls; use math.rad to convert degrees. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-07-07 [0:00](https://youtu.be/WfZhGsivpBM?t=0) Always check that Raycast returned a result before indexing it; an unsuccessful raycast returns nil and will error otherwise. ([[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]])
- 2023-07-07 [1:22](https://youtu.be/WfZhGsivpBM?t=82) Raycast direction must be destination minus origin (target position - origin), not the target position itself. ([[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]])
- 2023-07-07 [5:30](https://youtu.be/WfZhGsivpBM?t=330) Use RaycastParams FilterDescendantsInstances with Exclude to ignore parts; be careful not to filter out things the ray should hit. ([[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]])
- 2023-07-07 [7:33](https://youtu.be/WfZhGsivpBM?t=453) Set CanQuery to false on a part to make raycasts ignore it; simpler than using RaycastParams RespectCanCollide. ([[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]])
- 2023-10-30 [4:31](https://youtu.be/o0S_8fFCsfA?t=271) Do not store sensitive data (e.g. currency) in teleport settings; they are client-accessible and can be manipulated by exploiters. Validate on the server. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-31 [8:26](https://youtu.be/EpF5oWNS-Pk?t=506) Wrap all MemoryStore async calls in pcall in production; they fail more often than DataStore calls. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])

## [[building-art-and-assets]]
- 2022-11-17 [0:18](https://youtu.be/k2p9KMrlSAA?t=18) Add an Animator object under the Humanoid before loading animations; animations only play through an Animator. ([[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]])

## [[luau-language-and-types]]
- 2023-10-28 [0:51](https://youtu.be/nEVaMJpd1Ag?t=51) Use coroutines so a looping function does not block the thread; otherwise a while-true loop in one function prevents other functions from running. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [2:16](https://youtu.be/nEVaMJpd1Ag?t=136) Create a coroutine with coroutine.create(fn), then start it with coroutine.resume(co). Creating alone does nothing. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [3:18](https://youtu.be/nEVaMJpd1Ag?t=198) Stop a coroutine with coroutine.close(co) instead of relying on globals or leaving infinite loops running. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [4:26](https://youtu.be/nEVaMJpd1Ag?t=266) Use coroutine.yield() inside a coroutine to suspend it; it resumes from that point on the next coroutine.resume call. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [5:06](https://youtu.be/nEVaMJpd1Ag?t=306) coroutine.yield can pass values out: coroutine.resume returns success flag plus yielded/returned value. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [6:28](https://youtu.be/nEVaMJpd1Ag?t=388) Check coroutine.isyieldable() before yielding, and use coroutine.status() to read dead, normal, running, or suspended. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])
- 2023-10-28 [7:00](https://youtu.be/nEVaMJpd1Ag?t=420) Use coroutine.wrap(fn) to get a function that resumes a coroutine on each call, which is shorter than create plus resume. ([[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]])

## [[code-architecture-and-frameworks]]
- 2023-01-07 [7:07](https://youtu.be/DIz1Nk7YOUo?t=427) Bind several actions to the same handler function and branch on actionName with if/elseif to keep one shared handler. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])

## [[client-server-and-remotes]]
- 2022-11-17 [2:15](https://youtu.be/k2p9KMrlSAA?t=135) Put the animation script inside the model being animated so script.Parent points to the character. ([[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]])
- 2023-10-31 [0:00](https://youtu.be/EpF5oWNS-Pk?t=0) MemoryStoreService can only be accessed from the server, so call it from a server Script only. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])

## [[data-persistence]]
- 2023-10-31 [0:00](https://youtu.be/EpF5oWNS-Pk?t=0) Use MemoryStore for rapidly changing data like matchmaking queues; it is faster than DataStore but data expires (max 45 days). ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])
- 2023-10-31 [1:15](https://youtu.be/EpF5oWNS-Pk?t=75) Set an expiration on every queue item and map entry; maximum is 3,888,000 seconds (45 days). ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])
- 2023-10-31 [2:38](https://youtu.be/EpF5oWNS-Pk?t=158) Publish the place before testing MemoryStore calls; unpublished places return errors. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])
- 2023-10-31 [2:38](https://youtu.be/EpF5oWNS-Pk?t=158) Use a higher numeric priority to place items later in a queue; equal priority returns in insertion order. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])
- 2023-10-31 [1:56](https://youtu.be/EpF5oWNS-Pk?t=116) Set AllOrNothing to true when you need an exact count from a queue; default false returns fewer items if fewer exist. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])
- 2023-10-31 [3:40](https://youtu.be/EpF5oWNS-Pk?t=220) Use UpdateAsync with a transform function when the new value depends on the current value, to avoid overwriting concurrent changes. ([[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]])

## [[matchmaking-and-teleport]]
- 2023-10-30 [0:00](https://youtu.be/o0S_8fFCsfA?t=0) Wrap every asynchronous call (TeleportAsync, ReserveServer, GetPlayerPlaceInstanceAsync) in pcall so failures are handled. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [0:17](https://youtu.be/o0S_8fFCsfA?t=17) Use TeleportAsync; older teleport functions are deprecated. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [1:21](https://youtu.be/o0S_8fFCsfA?t=81) Use a reserved server access code for matchmaking; the server is not joinable from outside, so friends cannot follow players in. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [1:21](https://youtu.be/o0S_8fFCsfA?t=81) Use a server instance (job) ID to let friends join each other's servers; the target server need not be reserved. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [2:05](https://youtu.be/o0S_8fFCsfA?t=125) Set only one of ShouldReserveServer, ReservedServerAccessCode, or ServerInstanceId in TeleportOptions; they are mutually exclusive or an error is thrown. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [3:20](https://youtu.be/o0S_8fFCsfA?t=200) Put the TeleportService PlayerArrivedFromTeleport handler in a script in ReplicatedFirst so it loads early and works reliably. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [3:20](https://youtu.be/o0S_8fFCsfA?t=200) Use TeleportService:GetArrivingTeleportGui() on the client to access the custom loading GUI set via TeleportGui. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [5:24](https://youtu.be/o0S_8fFCsfA?t=324) Use GetPlayerPlaceInstanceAsync(userId) to get a player's place ID and job ID, then pass the job ID as ServerInstanceId to let others join them. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])
- 2023-10-30 [5:46](https://youtu.be/o0S_8fFCsfA?t=346) Handle teleport failures with pcall rather than the TeleportInitFailed event, which the speaker personally avoids. ([[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]])

## [[combat-and-gameplay-systems]]
- 2023-07-07 [4:06](https://youtu.be/WfZhGsivpBM?t=246) Raycasting is the basis for weapon hit detection: the hit part's ancestor Humanoid can be found to remove health. ([[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]])

## [[building-and-level-design]]
- 2023-02-11 [5:56](https://youtu.be/0TpwPpULXxU?t=356) Offset the camera along Z (e.g. 0,2,8 backwards and sideways) so it doesn't sit inside the character; tune values per game. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])

## [[3d-modeling-rigging-and-animation]]
- 2022-11-17 [1:24](https://youtu.be/k2p9KMrlSAA?t=84) Copy default animations from the Animate script of a character model to reuse Roblox's built-in walk animation. ([[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]])
- 2022-11-17 [3:34](https://youtu.be/k2p9KMrlSAA?t=214) Paste a Roblox animation ID into the Animation's AnimationId property to apply a custom animation; Roblox resolves the asset automatically. ([[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]])

## [[ui-ux-design]]
- 2023-01-07 [5:01](https://youtu.be/DIz1Nk7YOUo?t=301) Set the BindAction createTouchButton argument to true when you need a mobile touch button for the action; false otherwise. ([[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]])
- 2023-02-11 [9:27](https://youtu.be/0TpwPpULXxU?t=567) Keep pitch angles small (clamp around ±45 or less); large pitch values look odd. ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])
- 2023-02-11 [10:41](https://youtu.be/0TpwPpULXxU?t=641) Zoom via camera.FieldOfView: default 70; lower values zoom in (60), higher zoom out (80). ([[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]])

Up: [[xtb7-dev - How to make successful Roblox games]]
