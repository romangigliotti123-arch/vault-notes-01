---
title: "Docs: scripting / events / bindable"
url: https://create.roblox.com/docs/scripting/events/bindable.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / events / bindable

[Open](https://create.roblox.com/docs/scripting/events/bindable.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on BindableEvent and BindableFunction: same-side (server or client) communication between scripts. Covers async Fire vs synchronous Invoke, execution order warnings, and argument-passing limits (non-string keys, mixed tables, table copying, metatable loss).

## Tips
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[scripting-and-performance]]** Use BindableEvents for same-side server or client communication; use RemoteEvents for communication across the client-server boundary.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[scripting-and-performance]]** Place server BindableEvents in ServerScriptService and client ones in ReplicatedStorage, as the docs recommend.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[code-architecture-and-frameworks]]** Prefer module scripts for sharing data between scripts; use bindable events mainly for coordinating actions and round-based structure.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[client-server-and-remotes]]** Do not rely on connection order for multiple listeners on one BindableEvent; combine them into one function if order matters.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** A BindableFunction with no OnInvoke set makes the invoking script yield indefinitely and never resume.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Only the last OnInvoke assigned to a BindableFunction runs; assigning multiple callbacks silently overrides earlier ones.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Omitting a return statement in OnInvoke makes Invoke return nil.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Do not pass tables mixing numeric and string keys through bindables; elements can be dropped during transfer. Use a pure array or pure dictionary.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Avoid nil values in tables passed through bindables, whether arrays or dictionaries.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Non-string table keys (Instances, functions, userdata) are converted to strings when passed through bindables.
- [page](https://create.roblox.com/docs/scripting/events/bindable) **[[common-mistakes]]** Tables passed through bindables are copied, so identity checks fail; metatables are also lost in transfer, so methods and fields from metatables disappear.

## Tools
BindableEvent, BindableFunction, ServerScriptService, ReplicatedStorage

## He points to
- Remote events
- Custom events

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
