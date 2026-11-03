---
title: xtb7-dev - How to make successful Roblox games
tags: [roblox, xtb7-dev, playbook]
videos: 7
generated: 2026-10-29
credibility: mixed
credibility_score: 7.3
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# xtb7-dev - How to make successful Roblox games

xtb7-dev makes short Luau scripting tutorials, not a game-business playbook. Across seven videos (2022-2023) the advice is technical: run input and camera code in a LocalScript, use the right service for each job (Animator for animations, ContextActionService for context-specific input, RaycastParams for filtered hits, TeleportAsync for teleports, MemoryStore for fast-changing shared data), and wrap async calls in pcall. The notes contain no guidance on game ideas, monetisation, marketing, retention, or live ops. Those phases are marked as not covered rather than filled in.

**Style:** Beginner-friendly, code-first tutorials that teach one Roblox service at a time, with exact property names and numbers. Suits developers learning a specific API or system. It gives no strategy for growth, monetisation, or live ops, so pair it with other sources for those phases.

## Playbook
1. **1. Idea (not covered)** [[game-ideas-and-genres]]: The seven videos contain no ideation, genre selection, or market validation advice. Choose the game concept from other sources before applying the technical steps below.
2. **2. Build: keep input and camera on the client** [[client-server-and-remotes]]: Put input-handling code in a LocalScript (e.g. StarterPlayerScripts). UserInputService and ContextActionService only work on the client. Camera control also runs in a LocalScript.
3. **3. Build: pick the right input API** [[scripting-and-performance]]: Use UserInputService.InputBegan with the gameProcessed boolean to ignore UI clicks. Use ContextActionService for context-specific input because its handler does not run on every input. Check inputState == Begin to act once per press.
4. **4. Build: share one handler across actions** [[code-architecture-and-frameworks]]: Bind several actions to one function and branch on actionName with if/elseif. BindAction accepts multiple KeyCodes or UserInputTypes. Set createTouchButton to true when the action needs a mobile button. Name actions descriptively, not after the key.
5. **5. Build: camera rig** [[ui-ux-design]]: Set the camera to Scriptable, position it with CFrame offsets from HumanoidRootPart, and orient it with math.rad and CFrame.Angles. Default FieldOfView is 70. Keep pitch small (around ±45 or less).
6. **6. Build: character animation** [[3d-modeling-rigging-and-animation]]: Copy the default walk animation from the Animate script into an Animator under the Humanoid. Load it with humanoid:LoadAnimation, play while moving, and stop after humanoid.MoveToFinished:Wait(). Swap in a custom animation by pasting its ID into AnimationId.
7. **7. Build: hit detection with raycasts** [[combat-and-gameplay-systems]]: Call workspace:Raycast with origin and direction (destination minus origin) and read the RaycastResult. Filter with RaycastParams (FilterType Exclude or Include, RespectCanCollide, CanQuery). Find the hit part's ancestor Humanoid to remove health. This is the base for gun systems.
8. **8. Build: non-blocking loops** [[luau-language-and-types]]: Create a coroutine with coroutine.create and start it with coroutine.resume, since creating alone does nothing. Use coroutine.yield to suspend, coroutine.close to stop, and status checks for dead, normal, running, or suspended. This stops a while-true loop from blocking other functions.
9. **9. Build: teleports** [[matchmaking-and-teleport]]: Use TeleportAsync with TeleportOptions and wrap it in pcall. Set only one of ShouldReserveServer, ReservedServerAccessCode, or ServerInstanceId. Reserved codes suit matchmaking; server instance IDs let friends join. Handle arrival in PlayerArrivedFromTeleport from a script in ReplicatedFirst.
10. **10. Build: fast shared data** [[data-persistence]]: Use MemoryStore queues or sorted maps for rapidly changing data such as matchmaking queues. Set an expiration on every item (seconds, maximum 3,888,000). Use priority to order queue items and UpdateAsync when the new value depends on the current one. Access from server Scripts only.
11. **11. Launch: pre-release checks** [[testing-debugging-and-qa]]: Publish the place before testing MemoryStore calls, since unpublished places return errors. Test teleports, input, and animations in Studio after publishing. Confirm every async call has pcall handling.
12. **12. Growth: friend joins (partial)** [[social-features-and-virality]]: The notes cover only the mechanics: friends can join each other through a server instance ID, while reserved servers block outside friends. No marketing, discovery, or social-growth advice appears in these videos.
13. **13. Live ops (not covered)** [[updates-live-ops]]: No updates, events, or post-launch maintenance advice appears in the seven videos. The only lifecycle note is MemoryStore expiration, which limits how long data persists.

## Key numbers
- 70: default Camera.FieldOfView; lower values zoom in (e.g. 60), higher zoom out (e.g. 80)
- ~57 degrees per radian; use math.rad to convert degrees
- ±45 degrees: suggested pitch clamp; larger pitch values look odd
- 10 uses: demo threshold before UnbindAction in the ContextActionService example
- 2 fires per key press: ContextActionService without an inputState filter fires on Begin and End
- 3,888,000 seconds (45 days): maximum MemoryStore expiration
- Seconds: unit for MemoryStore expiration on queue add and map set calls

## Common mistakes
- Playing animations with no Animator under the Humanoid; animations only play through an Animator.
- Running UserInputService or ContextActionService on the server; they only work on the client.
- Calling MemoryStoreService from a LocalScript; it is server-only.
- Calling coroutine.create without coroutine.resume; nothing runs.
- Setting more than one of ShouldReserveServer, ReservedServerAccessCode, or ServerInstanceId; they are mutually exclusive and throw an error.
- Using ContextActionService without an inputState check, so the handler fires for both Begin and End.
- Leaving MemoryStore queue items or map entries without an expiration.
- Overwriting concurrent changes by setting values directly instead of using UpdateAsync with a transform function.
- Leaving teleport or GetPlayerPlaceInstanceAsync calls without pcall, so failures are unhandled.
- Using large camera pitch values, which look odd.

## Launch checklist
- [ ] Publish the place before testing MemoryStore calls.
- [ ] Confirm input-handling code is in a LocalScript.
- [ ] Confirm MemoryStoreService is called only from server Scripts.
- [ ] Confirm an Animator exists under the Humanoid before LoadAnimation.
- [ ] Confirm each animation stops after humanoid.MoveToFinished:Wait().
- [ ] Confirm every TeleportAsync, ReserveServer, and GetPlayerPlaceInstanceAsync call is wrapped in pcall.
- [ ] Confirm only one of ShouldReserveServer, ReservedServerAccessCode, or ServerInstanceId is set.
- [ ] Confirm the PlayerArrivedFromTeleport handler is in a script in ReplicatedFirst.
- [ ] Confirm TeleportInitFailed is handled.
- [ ] Confirm each MemoryStore item and map entry has an expiration at or below 3,888,000 seconds.
- [ ] Confirm AllOrNothing is true where an exact queue count is needed.
- [ ] Confirm UpdateAsync is used where the new value depends on the current value.
- [ ] Confirm ContextActionService handlers check inputState == Begin.
- [ ] Confirm createTouchButton is true for actions that need mobile buttons.
- [ ] Confirm camera FieldOfView and pitch are within the intended range (FOV default 70, pitch around ±45).
- [ ] Confirm raycast RaycastParams filters exclude the character and effects.
- [ ] Confirm coroutines that loop forever are stopped with coroutine.close when not needed.
- [ ] Decide whether matchmaking uses a reserved access code or friends join by server instance ID.

## How the advice changed over time
- No explicit reversal of advice appears across the seven videos; the notes contain no conflicting recommendations.
- The animation video (2022-11-17) is titled 'WORKING 2024', and the camera video (2023-02-11) is titled '2025'. This suggests the tutorials were re-checked against later Studio versions, but the notes do not say which steps changed.
- The teleport guidance states TeleportAsync is current and older teleport functions are deprecated, so use TeleportAsync rather than older methods.

## Theme notes
- [[xtb7-dev - Studio & Scripting|Studio & Scripting]]
- xtb7-dev - Games Mentioned
- [[xtb7-dev - Numbers & Benchmarks]]
- [[xtb7-dev - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2022-11-17 - How to Use Animations in Roblox Studio! - Scripting WORKING 2024|How to Use Animations in Roblox Studio! - Scriptin]] (3,279 views, 2022-11-17): Copy the default walk animation into an Animator, play it with LoadAnimation, and stop on MoveToFinished.
- [[2023-01-07 - ROBLOX Detect User Input w UserInputService or ContextActionService (H|ROBLOX: Detect User Input w/ UserInputService or C]] (1,907 views, 2023-01-07): Compare UserInputService and ContextActionService, bind several actions to one handler, and unbind after use.
- [[2023-02-11 - Roblox Scripting Tutorial Camera Manipulation (Position, Orientation,|Roblox Scripting Tutorial: Camera Manipulation (Po]] (27,986 views, 2023-02-11): Control the camera with a LocalScript using Scriptable mode, CFrame offsets, CFrame.Angles, and FieldOfView.
- [[2023-07-07 - Roblox Scripting How to Raycast (Roblox Studio Raycasting - Working 20|Roblox Scripting: How to Raycast (Roblox Studio Ra]] (1,311 views, 2023-07-07): Beginner raycasting: set origin and direction, read RaycastResult, and filter hits with RaycastParams.
- [[2023-10-28 - How to Use Coroutines in Roblox (Studio)|How to Use Coroutines in Roblox (Studio)]] (1,336 views, 2023-10-28): Luau coroutines explained: create, resume, yield, close, check status, and wrap functions to pause them.
- [[2023-10-30 - Master the TeleportService Roblox Studio Scripting Tutorial|Master the TeleportService: Roblox Studio Scriptin]] (977 views, 2023-10-30): TeleportAsync with TeleportOptions, reserved servers, arrival handling, and pcall-wrapped teleport calls.
- [[2023-10-31 - Advanced Roblox Studio Tutorial Memory Stores (MemoryStoreService)|Advanced Roblox Studio Tutorial: Memory Stores (Me]] (8,433 views, 2023-10-31): MemoryStore queues and sorted maps: faster than DataStore, server-only, with a 45-day expiration limit.
