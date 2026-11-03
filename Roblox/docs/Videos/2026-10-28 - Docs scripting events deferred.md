---
title: "Docs: scripting / events / deferred"
url: https://create.roblox.com/docs/scripting/events/deferred.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / events / deferred

[Open](https://create.roblox.com/docs/scripting/events/deferred.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on deferred engine events via Workspace.SignalBehavior. Explains Immediate vs Deferred event firing, the performance and correctness benefits, the list of resumption points, and code patterns that break under deferred behavior (mid-execution triggers, one-shot listeners, ancestry/property change events).

## Tips
- [page](https://create.roblox.com/docs/scripting/events/deferred) **[[scripting-and-performance]]** Set Workspace.SignalBehavior to Enum.SignalBehavior.Deferred; it is recommended for engine performance and correctness. Template places already default to it.
- [page](https://create.roblox.com/docs/scripting/events/deferred) **[[scripting-and-performance]]** Don't rely on an event firing synchronously. Under deferred behavior, handlers run only at the next resumption point, so yield before checking results set by callbacks.
- [page](https://create.roblox.com/docs/scripting/events/deferred) **[[scripting-and-performance]]** For one-shot listeners, use Event:Once() or call Connection:Disconnect() inside the handler. Destroy() on the instance does not drop pending handler calls and still runs them.
- [page](https://create.roblox.com/docs/scripting/events/deferred) **[[common-mistakes]]** Don't assume Destroying or ancestry/property-change handlers see the state at the moment of change; by the time they run, the instance may already be destroyed or changed.
- [page](https://create.roblox.com/docs/scripting/events/deferred) **[[scripting-and-performance]]** Avoid relying on Default SignalBehavior; it currently equals Immediate and will eventually switch to Deferred, so set the value explicitly.

## Numbers
- [page](https://create.roblox.com/docs/scripting/events/deferred) Re-entrancy depth limit: **10** (Max depth before events stop firing one another continuously)
- [page](https://create.roblox.com/docs/scripting/events/deferred) Property changes example: **1,000** (Immediate mode can run Luau after each of 1,000 property changes)

## Tools
Workspace.SignalBehavior, RunService, task library, Event:Once()

## He points to
- Class.Instance.Destroying
- Class.UserInputService
- Datatype.RBXScriptSignal.Once()

## Topics
[[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
