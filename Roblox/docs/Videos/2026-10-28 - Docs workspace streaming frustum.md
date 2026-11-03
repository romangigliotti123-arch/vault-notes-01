---
title: "Docs: workspace / streaming / frustum"
url: https://create.roblox.com/docs/workspace/streaming/frustum.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / streaming / frustum

[Open](https://create.roblox.com/docs/workspace/streaming/frustum.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Frustum Streaming: an opt-in, server-controlled system that additionally streams instances inside the player's camera frustum beyond the normal streaming radius. Covers the FrustumStreaming modes (Default, Disabled, Automatic, Enabled), stream-out behavior, performance cost, and limitations.

## Tips
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[scripting-and-performance]]** Set Player.FrustumStreaming only on the server; client-side assignments have no effect, so relay requests via RemoteEvent and validate them server-side.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Frustum streaming adds instances and full-quality terrain to the client, raising memory and possibly CPU use. Enable it only for games needing long-range visibility.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Automatic mode has a short activation delay; use manual Enabled mode during an equip animation so a scope is ready when the player looks through it.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Frustum streaming needs draw distance greater than the normal streaming target radius; low-end devices may have it disabled automatically.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Frustum has no occlusion culling; walls and terrain do not block candidate instances, so streamed volume can exceed what is visible.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Fast camera rotation invalidates the frustum and causes churn at extreme range; expect instances to stream in and out during rapid turns.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Opportunistic stream-out keeps out-of-view frustum instances for 1.5 seconds before GC; LowMemory keeps them until client memory runs low.
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) **[[optimization-and-streaming]]** Frustum streams to the lesser of client draw distance and an engine maximum range; the engine disables it for a client when draw distance drops to or below the streaming target radius.

## Numbers
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) Opportunistic stream-out linger time: **1.5 seconds** (Out-of-view frustum instances outside normal radius are GC'd after this)
- [page](https://create.roblox.com/docs/workspace/streaming/frustum) Frustum instance budget: **Same as a replication focus** (Instance count and bandwidth budget shared with replication foci)

## Tools
Class.Player.FrustumStreaming, Enum.FrustumStreamingMode, Class.Player:AddReplicationFocus(), Class.RemoteEvent

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
