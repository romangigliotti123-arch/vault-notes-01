---
title: "Server Authority Studio Beta - Insights from Engineers!"
url: https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-12-09
views: 352
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Server Authority Studio Beta - Insights from Engineers!

[Open](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) | Roblox DevForum | 352 views | 2025-12-09

## Summary
Khanovich's Roblox DevForum post introducing the Server Authority Studio Beta: the minimal initial API set, required features (NextGenerationReplication, StreamingEnabled), known issues, and workarounds for instance creation, rollback-safe input/touch detection, seats, humanoid states and SetPredictionMode.

## Tips
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[scripting-and-performance]]** Create or destroy instances on the server outside the simulation loop, e.g. inside task.defer, since new instances can't be created inside BindToSimulation.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[client-server-and-remotes]]** Server only replicates changes. To force resync of an attribute holder, set an attribute each frame on the server (e.g. SetAttribute('Time', time())) in BindToSimulation.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[client-server-and-remotes]]** Avoid InputAction Changed/Pressed/Released under server authority; poll GetState() in BindToSimulation and compare to a stored last-state attribute to detect new presses.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[client-server-and-remotes]]** Avoid Touched/TouchEnded for gameplay under rollback; use GetTouchingParts() in BindToSimulation and track previous state in attributes to detect new contacts.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[anti-exploit-and-security]]** Default seats are client-authoritative and can be used to teleport; don't rely on default seat welds for server-synced vehicles or seating.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[scripting-and-performance]]** Sync Humanoid enabled states via attributes set every frame in BindToSimulation, since Humanoid:SetStateEnabled does not replicate.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[scripting-and-performance]]** Always nil-check the instance before RunService:SetPredictionMode; passing nil currently crashes.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[physics-pathfinding-and-npc-ai]]** Keep mechanisms simple (one assembly) under Server Authority; multi-assembly mechanisms like suspension cars will jitter more in this beta.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[optimization-and-streaming]]** Enable StreamingEnabled: NextGenerationReplication needs it for scalability and RunService:setPredictionMode depends on its atomic grouping.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[optimization-and-streaming]]** Server performance with 20+ player games is still weak in this beta; expect significant improvement before launch.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[client-server-and-remotes]]** Large/uncapped properties (strings, arrays) still use legacy replication, and property updates have no ordering guarantee relative to RemoteEvents.
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) **[[development-process-and-speed]]** Report API gaps with a detailed use-case description and repro; the team explicitly asks for this feedback before the early 2026 launch.

## Numbers
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) Attribute replication: **strict size limits (exact figures not stated)** (Attributes are capped to keep payloads within one MTU)
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) Target full launch: **early 2026** (Server Authority fully playable release timeline)

## Tools
RunService:BindToSimulation, RunService:SetPredictionMode, RunService:GetPredictionStatus, Workspace.AuthorityMode, Workspace.NextGenerationReplication, Workspace.StreamingEnabled, InputAction:GetState, BasePart:GetTouchingParts

## Quotes
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) "Clients can diverge from the server and not be resynchronized if a change only takes place on the client and no changes take place on the server."
- [page](https://devforum.roblox.com/t/server-authority-studio-beta-insights-from-engineers/4139321) "Seats and seat welds have client authority in Roblox. Players can exploit seats by sitting in them as a way to teleport."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
