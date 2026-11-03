---
title: "Docs: projects / server-authority"
url: https://create.roblox.com/docs/projects/server-authority.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / server-authority

[Open](https://create.roblox.com/docs/projects/server-authority.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the server authority model: the server is the source of truth and clients predict inputs, rolling back and resimulating on misprediction. Covers required Workspace settings, BindToSimulation, time() vs tick(), attribute limits, input actions, instance create/remove rules, animations, and rendering effects separately.

## Tips
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Enable AuthorityMode Server, NextGenerationReplication, PlayerScriptsUseInputActionSystem, SignalBehavior Deferred, UseFixedSimulation and StreamingEnabled on Workspace before using server authority.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Put core simulation logic in a ModuleScript in ReplicatedStorage, initialised by a server Script and a client LocalScript, using RunService:BindToSimulation.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[scripting-and-performance]]** Use RobloxGlobals time() inside simulation code; tick(), os.time() and os.clock() are local clocks that do not roll back and cause desync.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Use InputActions, not UserInputService.InputBegan, for any input affecting the core simulation, and sanity-check inputs on the server.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Remove instances by writing an attribute inside the simulation, then calling Destroy in a server PostSimulation connection; Destroy and Parent changes error inside bound functions.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Do not cache AnimationTrack references across frames during rollback; look up the live track each frame with Animator:GetTrackByAnimationId().
- [page](https://create.roblox.com/docs/projects/server-authority) **[[vfx-and-particles]]** Render sounds and effects in RenderStepped, separate from simulation, and be ready to hide or undo mispredicted effects.
- [page](https://create.roblox.com/docs/projects/server-authority) **[[client-server-and-remotes]]** Avoid relying on RemoteEvents for state ordering: they may arrive out of order relative to property and attribute changes.

## Numbers
- [page](https://create.roblox.com/docs/projects/server-authority) Attribute replication limit: **first 64 attributes per instance**
- [page](https://create.roblox.com/docs/projects/server-authority) Attribute name length limit: **max 50 characters**
- [page](https://create.roblox.com/docs/projects/server-authority) String attribute value length limit: **max 50 characters**

## Tools
RunService:BindToSimulation, RunService:SetPredictionMode, RunService:GetPredictionStatus, InputAction / InputContext

## He points to
- Roblox docs: replication order
- Roblox docs: predictive instance creation
- Roblox docs: playing sounds and visual effects
- Roblox docs: writing animation code

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
