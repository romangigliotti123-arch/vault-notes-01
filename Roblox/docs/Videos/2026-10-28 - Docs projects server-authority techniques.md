---
title: "Docs: projects / server-authority / techniques"
url: https://create.roblox.com/docs/projects/server-authority/techniques.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / server-authority / techniques

[Open](https://create.roblox.com/docs/projects/server-authority/techniques.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on server-authority techniques: predictive instance stitching via BindToSimulation, position smoothing of mispredicted objects, animation handling under rollback (avoid track caching, query Animator), predicted effects via state machines, and simulation radius visualization.

## Tips
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[scripting-and-performance]]** Put simulation logic in a ModuleScript required on both client and server so BindToSimulation code produces matching results and avoids mispredictions.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[client-server-and-remotes]]** Use instance stitching (Instance.new, Clone, fromExisting inside BindToSimulation) for instances needing instant client visibility, e.g. rockets or physics constraints, to avoid a server round-trip.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[common-mistakes]]** Do not hold references to speculative instances and parent them in a later frame; parent them into the DataModel before the frame ends.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[common-mistakes]]** Do not cache AnimationTrack objects under server authority; rollback invalidates them. Store animation IDs and fetch tracks via Animator:GetTrackByAnimationId.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[optimization-and-streaming]]** Use Animator:GetPlayingAnimationTracks to iterate all active tracks when stopping or filtering animations.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[physics-pathfinding-and-npc-ai]]** Smooth mispredicted objects by rendering a massless, non-colliding, anchored visual clone that tracks an invisible simulated part with TweenService:SmoothDamp (smoothTime about 0.07).
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[player-psychology-and-game-feel]]** Only smooth position when the simulated object jumps far from the rendered one, as Soccer does, so normal play has no visual latency.
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[vfx-and-particles]]** Drive predicted effects from synchronized state-machine attributes in simulation and render them in RenderStepped; undo effects when the state reverts (e.g. defused grenade hides explosion).
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) **[[testing-debugging-and-qa]]** Enable Are Regions Enabled in Studio settings (Alt+S / Option+S) to visualize the automatic prediction radius around your character.

## Numbers
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) Position smoothing smoothTime: **0.07 (smaller = faster)**
- [page](https://create.roblox.com/docs/projects/server-authority/techniques) Latency cost without stitching: **At least one server round-trip**

## Games
- **Soccer**: Smooths ball position only when simulated ball jumps far from rendered ball, giving no visual latency normally.

## Tools
RunService:BindToSimulation, TweenService:SmoothDamp, Animator:GetTrackByAnimationId, Animator:GetPlayingAnimationTracks, Highlight

## He points to
- Roblox docs: simulation sync

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
