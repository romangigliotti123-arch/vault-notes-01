---
title: "Mastering Server Authority to Build Competitive Multiplayer Games | RDC 2026"
url: https://youtu.be/9IqNHhYXK0s
creator: Roblox
official: true
advice_density: high
date: 2026-10-12
views: 2136
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Mastering Server Authority to Build Competitive Multiplayer Games | RDC 2026

[Watch](https://youtu.be/9IqNHhYXK0s) | MustWatch | 2,136 views | 2026-10-12

## Summary
Roblox engine team (Brian Neer, Jason Knight) and C Games' Drew Hamilton explain server authority: enabling it via a toggle, writing client-predicted scripts with shared modules, bind to simulation and synchronized data, debugging with the visualizer, and porting an existing game (Global Anarchy) with common pitfalls and roadmap.

## Tips
- [8:35](https://youtu.be/9IqNHhYXK0s?t=515) **[[scripting-and-performance]]** Under server authority, read/write only synchronized data: input actions under the player and attributes on the humanoid root part. Unsynced Lua data corrupts on rollback.
- [7:53](https://youtu.be/9IqNHhYXK0s?t=473) **[[scripting-and-performance]]** Put simulation logic in bind to simulation, not RenderStepped or Heartbeat, since simulation callbacks re-run during reimulation.
- [7:13](https://youtu.be/9IqNHhYXK0s?t=433) **[[scripting-and-performance]]** Share simulation code via a ModuleScript called from both a client and a server script; local scripts can no longer drive a server-authoritative humanoid.
- [22:26](https://youtu.be/9IqNHhYXK0s?t=1346) **[[common-mistakes]]** Don't play sound effects or particles inside bind to simulation; rollbacks replay them repeatedly and stack the sounds. Use task.defer for visual effects.
- [23:07](https://youtu.be/9IqNHhYXK0s?t=1387) **[[common-mistakes]]** Keep the predicted simulation small; around 10,000 predicted instances lagged the system and forced input latency, causing death loops.
- [5:47](https://youtu.be/9IqNHhYXK0s?t=347) **[[scripting-and-performance]]** Enable server authority for just the humanoid by setting Workspace authority mode to Server; no code needed for movement anti-speed/fly hacks.
- [10:05](https://youtu.be/9IqNHhYXK0s?t=605) **[[analytics-metrics]]** Use Ctrl+Shift+F6 in Studio to open the server authority visualizer; check misprediction rate and predicted frames ahead.
- [10:47](https://youtu.be/9IqNHhYXK0s?t=647) **[[scripting-and-performance]]** Test under simulated latency (Studio network simulation, e.g. 60ms latency, 10ms jitter) before trusting prediction results.
- [11:27](https://youtu.be/9IqNHhYXK0s?t=687) **[[scripting-and-performance]]** Create projectiles on both client and server with server authority rather than hacking fake invisible rockets to hide latency.
- [16:25](https://youtu.be/9IqNHhYXK0s?t=985) **[[development-process-and-speed]]** When porting a live game, build a proof-of-concept character controller first, then port into the engine, then into the game; expect the whole game to break mid-migration.
- [16:57](https://youtu.be/9IqNHhYXK0s?t=1017) **[[development-process-and-speed]]** Enable deferred signal behavior and next-generation replication before server authority; it also cut Global Anarchy's frame time from ~6-8ms to ~4-5ms.
- [15:03](https://youtu.be/9IqNHhYXK0s?t=903) **[[building-art-and-assets]]** Back state with instances already used client-side (e.g. ValueBase objects) to cut refactoring when porting an existing codebase.
- [21:03](https://youtu.be/9IqNHhYXK0s?t=1263) **[[development-process-and-speed]]** Server authority can make anti-cheat code redundant; Aftermath's ~1000-line anti-fly script could be removed after adoption.
- [23:48](https://youtu.be/9IqNHhYXK0s?t=1428) **[[common-mistakes]]** Some misprediction is normal, especially with remote players; janky character motion on your own character is not and should be fixed.
- [27:01](https://youtu.be/9IqNHhYXK0s?t=1621) **[[scripting-and-performance]]** Use the CCL character controller library (V2 adds crouch and sprint) for server-authoritative abilities instead of hand-rolling them.

## Numbers
- [10:05](https://youtu.be/9IqNHhYXK0s?t=605) Instance prediction success rate: **100% (Studio, with and without 60ms latency)** (Jetpack demo in Studio under simulated network latency)
- [10:05](https://youtu.be/9IqNHhYXK0s?t=605) Predicted frames ahead of server: **12 frames (rises with latency)** (Server authority visualizer in Studio)
- [17:38](https://youtu.be/9IqNHhYXK0s?t=1058) Frame time after deferred signal behavior: **from ~6-8 ms/frame to ~4-5 ms/frame** (Global Anarchy engine, per Drew Hamilton)
- [23:07](https://youtu.be/9IqNHhYXK0s?t=1387) Predicted instances that lagged the system: **~10,000** (Overprediction example from visualizer screenshot)
- [21:03](https://youtu.be/9IqNHhYXK0s?t=1263) Aftermath anti-fly script size: **~1000 lines** (Made redundant by server authority)
- [10:47](https://youtu.be/9IqNHhYXK0s?t=647) Simulated network conditions: **60 ms latency, 10 ms jitter** (Studio network simulation test)

## Games
- **Global Anarchy** [2:28](https://youtu.be/9IqNHhYXK0s?t=148): C Games' FPS being ported to server authority; speed and teleport hacks stopped, fly hacks were still possible before the port.
- **Aftermath** [21:03](https://youtu.be/9IqNHhYXK0s?t=1263): Had a large flying exploit; server authority made its ~1000-line anti-fly script redundant.
- **Golf Frenzy** [0:43](https://youtu.be/9IqNHhYXK0s?t=43): Another C Games title mentioned; no lesson given in the talk.
- **Crossroads rocket launcher demo** [11:27](https://youtu.be/9IqNHhYXK0s?t=687): Non-server-authoritative rocket freezes a frame and lags; server-authoritative version fires instantly and feels responsive.

## Tools
Roblox Studio, Server authority visualizer (Ctrl+Shift+F6), Studio network simulation, Attributes, Input actions, ValueBase objects, CCL (character controller library)

## He points to
- Creator support booth / engine booth (Q&A)
- Ask me about net code shirt (Brian/Drew)
- QR code for slides and code
- Upcoming studio build skill for best-practice code review

## Quotes
- [2:28](https://youtu.be/9IqNHhYXK0s?t=148) "If you play a sound effect inside bind to simulation, when the system rolls back and reimulates, it's going to play that sound effect many times."
- [16:57](https://youtu.be/9IqNHhYXK0s?t=1017) "It's a lot of work, but it's totally worth it."

## On screen
Contact sheet shows the server authority visualizer is not clearly readable; Studio screens show a soccer ball and jetpack character in a street map, a Workspace authority mode setting, and the Explorer tree with ServerScriptService/ReplicatedStorage modules. Global Anarchy before/after comparison shows cheater POV flying versus innocent player POV.

## Topics
[[analytics-metrics]] [[building-art-and-assets]] [[common-mistakes]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[MustWatch - How to make successful Roblox games]]
