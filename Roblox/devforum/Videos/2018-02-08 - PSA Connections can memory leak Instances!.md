---
title: "PSA: Connections can memory leak Instances!"
url: https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082
creator: Roblox DevForum
official: false
advice_density: medium
date: 2018-02-08
views: 623
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# PSA: Connections can memory leak Instances!

[Open](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) | Roblox DevForum | 623 views | 2018-02-08

## Summary
Dev post by stravant warning that Roblox event connections can keep Instances (and anything they reference) alive after they are unreferenced, causing memory leaks. Explains the cycle cause, recommends Destroy() and explicit disconnects, and flags custom Signal classes built on BindableEvents as a risk.

## Tips
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[scripting-and-performance]]** Call :Destroy() on Instances you no longer need; Destroy recursively breaks their event connections so they can be garbage collected.
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[scripting-and-performance]]** Store connection objects and call :Disconnect() on them when done; a connection that is never disconnected keeps the closure and its upvalues alive.
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[common-mistakes]]** Don't assume Lua's GC will free cycles through Instance events; connections are held in C++ and invisible to Lua, so a part referenced indirectly via a table still leaks.
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[code-architecture-and-frameworks]]** If a custom Signal class uses a BindableEvent internally, ensure every connection made on it is disconnected before the owning object's lifetime ends, or give objects a Destroy method.
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[code-architecture-and-frameworks]]** Use a cleanup pattern such as a Maid class to track and disconnect connections in bulk.
- [page](https://devforum.roblox.com/t/psa-connections-can-memory-leak-instances/90082) **[[scripting-and-performance]]** Prioritise leak checks on the server, since long-running server processes accumulate leaks while short client sessions rarely hit a problematic level.

## He points to
- Quenty's Maid class pattern
- GoodSignal pure Lua Signal implementation by stravant (2021 edit, uses task library)

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
