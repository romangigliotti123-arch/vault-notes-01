---
title: "Docs: scripting / events / remote"
url: https://create.roblox.com/docs/scripting/events/remote.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / events / remote

[Open](https://create.roblox.com/docs/scripting/events/remote.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on remote events and remote functions: client-server communication patterns, delivery guarantees (RemoteEvent reliable/ordered, UnreliableRemoteEvent best-effort), and argument serialization limits (functions, metatables, non-replicated instances, table keys).

## Tips
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Make the server the source of truth: client fires a RemoteEvent, server verifies (e.g. does the player own the potion) before granting benefits.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Use RemoteEvents for UI updates and one-way notifications; avoid RemoteFunction:InvokeClient because it can error, throw if client disconnects, or yield forever.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Assign only one OnServerInvoke/OnClientInvoke callback per RemoteFunction; only the last definition runs.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Place remotes in ReplicatedStorage so both server and client can access them.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Use UnreliableRemoteEvent for continuously changing, non-critical data; payloads over 1,000 bytes may be dropped.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Include a timestamp or sequence number in unreliable/out-of-order-sensitive messages and ignore messages older than the latest handled.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** If order matters across remote types, send related messages through the same remote type or add your own sequence number.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Connect handlers before firing; RemoteEvent queues messages with no handler (limited queue), but UnreliableRemoteEvent discards them immediately.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Do not pass functions, metatable-based objects (metatables are lost), or ServerStorage/client-created instances in remote arguments; they arrive as nil.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Do not mix numeric and string keys in one table sent via remotes; non-string indices are converted to strings. Avoid nil values in tables.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Tables sent through remotes are copied, so compare contents rather than table identity.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Be aware that a yielding handler does not block the next message from starting; ordering applies to handler start, not completion.
- [page](https://create.roblox.com/docs/scripting/events/remote) **[[client-server-and-remotes]]** Remote traffic from clients is throttled per remote type across all instances; excess RemoteEvent messages are delayed, excess Unreliable ones are dropped.

## Numbers
- [page](https://create.roblox.com/docs/scripting/events/remote) UnreliableRemoteEvent max payload: **1,000 bytes** (larger payloads may be dropped)
- [page](https://create.roblox.com/docs/scripting/events/remote) Remote event queue limit: **limited by count and memory** (messages discarded with 'Remote event invocation' error when full)

## Tools
RemoteEvent, UnreliableRemoteEvent, RemoteFunction

## He points to
- Class.RemoteEvent throttling section
- Class.UnreliableRemoteEvent payload limits
- Prompt subscription purchases docs

## Topics
[[client-server-and-remotes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
