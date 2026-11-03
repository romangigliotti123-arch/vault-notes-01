---
title: "Docs: projects / data-model"
url: https://create.roblox.com/docs/projects/data-model.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / data-model

[Open](https://create.roblox.com/docs/projects/data-model.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on the data model: the hierarchy of objects (Instances) that defines a place. Covers 3D building blocks (BasePart, Part, MeshPart, TrussPart), script types (Script, LocalScript, ModuleScript), container services (Workspace, Lighting, Replication, Server, Client, Chat), and folders vs models for organization.

## Tips
- [page](https://create.roblox.com/docs/projects/data-model) **[[scripting-and-performance]]** Place scripts in the correct containers: Script in ServerScriptService, LocalScript in StarterPlayerScripts/StarterGui, ModuleScript in ReplicatedStorage if shared. Wrong container means the script won't run or runs in the wrong place.
- [page](https://create.roblox.com/docs/projects/data-model) **[[anti-exploit-and-security]]** Put server-only logic in ServerScriptService, which is never replicated to clients, to keep it secure.
- [page](https://create.roblox.com/docs/projects/data-model) **[[optimization-and-streaming]]** Store large maps in ServerStorage and move them into Workspace only when needed to decrease client network traffic on initial join.
- [page](https://create.roblox.com/docs/projects/data-model) **[[client-server-and-remotes]]** Use RemoteEvents and RemoteFunctions for client-to-server communication rather than placing shared logic in the wrong container.
- [page](https://create.roblox.com/docs/projects/data-model) **[[code-architecture-and-frameworks]]** Put ModuleScripts used by both server and client in ReplicatedStorage; put server-only modules in ServerScriptService or ServerStorage.
- [page](https://create.roblox.com/docs/projects/data-model) **[[building-and-level-design]]** Use Folders for environment sections (lobby, combat arena) and Models for sets of related objects (desk with chair, table, lamp); nest models for complex sets.
- [page](https://create.roblox.com/docs/projects/data-model) **[[common-mistakes]]** Do not add Player objects to the Players container manually; the engine creates them automatically on join.
- [page](https://create.roblox.com/docs/projects/data-model) **[[common-mistakes]]** Name objects descriptively so they are easy to find and modify later.
- [page](https://create.roblox.com/docs/projects/data-model) **[[building-art-and-assets]]** Import meshes (MeshPart) and combine primitive parts via solid modeling for complex structures rather than relying only on simple parts.
- [page](https://create.roblox.com/docs/projects/data-model) **[[client-server-and-remotes]]** Objects in ReplicatedFirst replicate to the client only once; use it for essentials needed to initialize a player.
- [page](https://create.roblox.com/docs/projects/data-model) **[[optimization-and-streaming]]** Remember that clients render only what is inside Workspace; objects elsewhere are not rendered.

## Tools
Roblox Studio, Luau

## He points to
- Client-Server Runtime
- Customize the camera
- Environmental terrain
- Text chat overview
- Voice chat

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
