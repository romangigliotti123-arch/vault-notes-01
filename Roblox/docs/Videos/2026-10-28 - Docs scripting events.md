---
title: "Docs: scripting / events"
url: https://create.roblox.com/docs/scripting/events.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / events

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/scripting/events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the event-driven model: connecting functions to events with Connect(), disconnecting connections, one-shot listening with Once(), yielding with Wait(), and the three kinds of event mechanisms (bindable, remote, deferred engine events).

## Tips
- [page](https://create.roblox.com/docs/scripting/events) **[[client-server-and-remotes]]** Disconnect connections you no longer need; it's recommended for performance. Non-deferred connections auto-disconnect when their object is destroyed.
- [page](https://create.roblox.com/docs/scripting/events) **[[code-architecture-and-frameworks]]** Use Deferred events for more performant and consistent event handling, since they defer handlers until engine resumption points.
- [page](https://create.roblox.com/docs/scripting/events) **[[code-architecture-and-frameworks]]** Use BindableEvents for communication between scripts on the same side of the client-server boundary; use RemoteEvents to cross it.
- [page](https://create.roblox.com/docs/scripting/events) **[[luau-language-and-types]]** Use signal:Once() instead of manually connecting then disconnecting when a function should only run the first time an event fires.

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
