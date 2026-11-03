---
title: "Docs: workspace / streaming"
url: https://create.roblox.com/docs/workspace/streaming.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / streaming

[Open](https://create.roblox.com/docs/workspace/streaming.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on instance streaming (Workspace.StreamingEnabled): what streams in/out, streaming properties and recommended values, replication foci, predictive streaming, model streaming modes (Nonatomic/Atomic/Persistent/PersistentPerPlayer), pause-screen customization, and runtime debugging tools.

## Tips
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Keep StreamingEnabled on (default for new places); it cuts memory use, join times and server bandwidth on lower-end devices.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Set ModelStreamingBehavior to Improved; it is the recommended, most efficient mode for models with BasePart descendants.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Set StreamOutBehavior to Opportunistic to aggressively garbage-collect content and reduce out-of-memory crashes.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Keep StreamingMinRadius at default 64 so the engine can scale down for low-end devices; larger values cost memory and bandwidth.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Keep StreamingTargetRadius at default 1024; smaller reduces server load but shortens the distance at which full detail is visible.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Keep StreamingTargetRadius larger than StreamingMinRadius; equal values remove the buffer and cause network pauses.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Set StreamingIntegrityMode to PauseOutsideLoadedArea to avoid gameplay issues when players enter unstreamed regions.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Enable PredictiveStreamingMode for fewer streaming pauses and pop-in with no code changes.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Use Atomic model streaming for models whose parts must arrive together; clients then need WaitForChild only on the model, not its parts.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Use Persistent models sparingly, only for a few parts client scripts must always access; overuse hurts performance.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Stream out client-created instances only if parented under server-created instances; client-created ones are exempt from streaming out.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Add replication foci (AddReplicationFocus) for home bases, hubs or distant viewpoints, but each extra focus adds server streaming load.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Keep assemblies small when moving; many instances streaming in together can cause network and CPU spikes.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Do not rely on instances in ReplicatedStorage for atomic replication; only Workspace descendants are streamed.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[optimization-and-streaming]]** Use the Network Stats overlay (Shift+F3, then Shift+1 to the fourth panel) and colored radius regions to debug streaming.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[client-server-and-remotes]]** Do not expect local-only property changes to survive streaming; they can be lost when an instance streams out and back in.
- [page](https://create.roblox.com/docs/workspace/streaming) **[[scripting-and-performance]]** Wait for Workspace.PersistentLoaded before accessing persistent models in client scripts; otherwise use WaitForChild and tolerate streaming.

## Numbers
- [page](https://create.roblox.com/docs/workspace/streaming) StreamingMinRadius default: **64** (Highest-priority streaming radius around replication foci; recommended default)
- [page](https://create.roblox.com/docs/workspace/streaming) StreamingTargetRadius default: **1024** (Max distance instances stream in; recommended default)
- [page](https://create.roblox.com/docs/workspace/streaming) Replication focus load: **9 moving foci ≈ 10 players** (Server streaming and networking workload comparison from docs)
- [page](https://create.roblox.com/docs/workspace/streaming) Debug radius colors: **red <64, yellow 64-1024, blue =1024, green >1024** (Network Stats streaming debug view region colors)

## Tools
Roblox Studio, Network Stats debug overlay, GuiService

## He points to
- SLIM guide (high-fidelity level of detail for models and avatars)
- Streaming techniques guide

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
