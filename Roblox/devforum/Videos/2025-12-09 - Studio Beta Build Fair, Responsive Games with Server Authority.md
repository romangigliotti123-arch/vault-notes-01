---
title: "[Studio Beta] Build Fair, Responsive Games with Server Authority"
url: https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-12-09
views: 948
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Studio Beta] Build Fair, Responsive Games with Server Authority

[Open](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) | Roblox DevForum | 948 views | 2025-12-09

## Summary
Roblox DevForum announcement launching Server Authority (with Latency Compensation) into Studio Beta. Explains server-authoritative simulation with client prediction, rollback and resimulation, how to enable it (Beta Features + five Workspace settings), known issues, and that it must not be published yet. Targeted GA early 2026.

## Tips
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[development-process-and-speed]]** Enable Server Authority in Studio via File > Beta Features, then set NextGenerationReplication, UseFixedSimulation, StreamingEnabled, PlayerScriptsUseInputActionSystem on, SignalBehavior to Deferred, then AuthorityMode to Server.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[client-server-and-remotes]]** Put core game logic in a ModuleScript in ReplicatedStorage and connect its update loop to RunService:BindToSimulation on both client and server to keep them in sync.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[client-server-and-remotes]]** Use InputAction for all player inputs affecting the simulation; these are the only client data the server trusts.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[data-persistence]]** Store synchronized game state (health, ammo) in Attributes on predicted Instances so it rolls back on misprediction; plain Luau variables are not rolled back.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[client-server-and-remotes]]** Create new Instances only on the server, wrapping creation logic in an if RunService:IsServer() block, during the beta.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[anti-exploit-and-security]]** Server Authority prevents client exploits like speed/fly hacks by having the server validate actions and reject rule-breaking ones, reducing custom anti-cheat work.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[optimization-and-streaming]]** Keep Instance Streaming enabled; Server Authority relies on the client simulating only locally loaded content and streaming also reduces join time and memory.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[common-mistakes]]** Do not publish a Server Authority-enabled game; player clients lack support and the game will not work correctly. Studio Beta changes only apply to local Studio play.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[common-mistakes]]** Avoid relying on BasePart.Touched/TouchEnded and InputAction.StateChanged for gameplay; use GetTouchingParts() and InputAction:GetState() instead, since rollbacks can fire them inaccurately.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[ab-testing-and-experiments]]** Avoid Team Create and Team Test during the Studio Beta; they are unavailable with Server Authority Studio Beta enabled.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[development-process-and-speed]]** Start by enabling only Workspace.AuthorityMode for simple default-avatar physics; complex custom gameplay needs adapting scripts to BindToSimulation and InputAction.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[optimization-and-streaming]]** Expect higher server costs and extra client work for prediction and resimulation; budget for it, as optimization is ongoing.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[combat-and-gameplay-systems]]** Note Attribute limit: max 64 attributes per Instance with limited string size; minimise instance payload sizes for efficient sync.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[scripting-and-performance]]** Avoid frame-rate-dependent scripts when predicting; use the consistent-rate BindToSimulation callback so client and server state stay in sync. Replaces FixedHeartbeat.
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) **[[development-process-and-speed]]** Reference the official example places (Laser Tag, Soccer, Racing) and the Server Authority docs to learn the pattern before adopting it.

## Numbers
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) Attributes per Instance: **64 max** (Server Authority known limit on attributes per Instance)
- [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157) General Availability target: **early 2026** (Roblox goal for generally releasing Server Authority)

## Games
- **Laser Tag**: Official Server Authority example place for learning the pattern.
- **Soccer**: Official Server Authority example place for learning the pattern.
- **Racing**: Official Server Authority example place for learning the pattern.

## Tools
Roblox Studio, Server Authority Core API (Beta Features), RunService:BindToSimulation, InputAction, Attributes

## He points to
- Server Authority documentation (Roblox Creator Docs)
- RDC 25 breakout session on Server Authority
- Server Authority example places: Laser Tag, Soccer, Racing

## Topics
[[ab-testing-and-experiments]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
