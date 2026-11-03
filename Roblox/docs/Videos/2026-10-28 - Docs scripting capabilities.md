---
title: "Docs: scripting / capabilities"
url: https://create.roblox.com/docs/scripting/capabilities.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / capabilities

[Open](https://create.roblox.com/docs/scripting/capabilities.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Script capabilities (experimental, client beta): per-container Sandboxed property and Capabilities set to restrict what scripts can access in DataModel. Covers execution control, instance access, script functionality, Engine API capabilities, nested containers, bindable/remote communication, module require, and instance movement rules.

## Tips
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[anti-exploit-and-security]]** Restrict scripts in toolbox models or UGC to the smallest capability set they need, so they cannot access outside instances or unneeded APIs.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[anti-exploit-and-security]]** Avoid granting AccessOutsideWrite; sandboxing guarantees weaken when scripts can interact with any instance in the game.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[client-server-and-remotes]]** Use BindableEvent or BindableFunction to communicate with a sandboxed container rather than sharing mutable references or modules.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[code-architecture-and-frameworks]]** Share libraries with minimal capabilities so other developers don't need to audit the entire codebase for malicious code.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[scripting-and-performance]]** Use HttpService JSONEncode/JSONDecode/GenerateGUID freely; they need no capabilities beyond script execution.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[common-mistakes]]** Disabling a script or setting Sandboxed=false on a caller weakens security; only do it when strictly necessary.
- [page](https://create.roblox.com/docs/scripting/capabilities) **[[scripting-and-performance]]** Do not rely on getfenv/setfenv in sandboxed scripts; they are unavailable and throw errors.

## Tools
Workspace.SandboxedInstanceMode (set to Experimental), Instance.Sandboxed property, Instance.Capabilities property

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
