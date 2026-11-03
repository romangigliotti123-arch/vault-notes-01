---
title: "Docs: scripting / locations"
url: https://create.roblox.com/docs/scripting/locations.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / locations

[Open](https://create.roblox.com/docs/scripting/locations.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on script types (Script, LocalScript, ModuleScript), RunContext behaviour, and which containers run which script types. Recommends a single entry Script per side, ModuleScripts for most code, and LocalScripts only in starter containers.

## Tips
- [page](https://create.roblox.com/docs/scripting/locations) **[[code-architecture-and-frameworks]]** Put most client and server code in ModuleScripts; require them from one thin client script and one thin server script as single entry points.
- [page](https://create.roblox.com/docs/scripting/locations) **[[code-architecture-and-frameworks]]** Give each ModuleScript a start() function so all modules load before code executes.
- [page](https://create.roblox.com/docs/scripting/locations) **[[code-architecture-and-frameworks]]** Share code via ModuleScripts in ReplicatedStorage, required from both client and server scripts.
- [page](https://create.roblox.com/docs/scripting/locations) **[[client-server-and-remotes]]** Put a single Script with RunContext Client in ReplicatedStorage; put a single Script with RunContext Server in ServerScriptService.
- [page](https://create.roblox.com/docs/scripting/locations) **[[client-server-and-remotes]]** Never put server scripts in ReplicatedStorage; its contents replicate to clients, exposing server logic.
- [page](https://create.roblox.com/docs/scripting/locations) **[[common-mistakes]]** Avoid Starter containers for client code with Script RunContext Client; the original and the cloned copy both run, causing duplicate behaviour.
- [page](https://create.roblox.com/docs/scripting/locations) **[[common-mistakes]]** Default Script RunContext is Legacy: it runs server-side only inside server containers like ServerScriptService or Workspace.
- [page](https://create.roblox.com/docs/scripting/locations) **[[testing-debugging-and-qa]]** Keep client code in ReplicatedStorage so Output errors link to a stable path, not a per-player cloned copy.
- [page](https://create.roblox.com/docs/scripting/locations) **[[code-architecture-and-frameworks]]** Avoid attaching scripts to Workspace instances; tag instances with CollectionService and handle them from one ModuleScript.
- [page](https://create.roblox.com/docs/scripting/locations) **[[code-architecture-and-frameworks]]** Use LocalScripts sparingly; if needed, place them in StarterCharacterScripts, StarterPlayerScripts, StarterGui or StarterPack.
- [page](https://create.roblox.com/docs/scripting/locations) **[[building-and-level-design]]** When publishing models or packages on the Creator Store, set RunContext explicitly on each included script so they work across locations.

## Tools
Roblox Studio Explorer, Properties window, Output window, CollectionService

## He points to
- Plant reference project
- Replication order documentation

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
