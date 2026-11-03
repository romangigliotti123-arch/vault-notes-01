---
title: "Creating A Furniture Placement System"
url: https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509
creator: Roblox DevForum
official: false
advice_density: medium
date: 2018-11-26
views: 1997
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating A Furniture Placement System

[Open](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) | Roblox DevForum | 1,997 views | 2018-11-26

## Summary
EgoMoose's guide on building a Roblox furniture/decoration placement system using OOP in Luau. Covers class/constructor/metatable basics, FE-friendly client/server "twin" objects via RunService:IsServer(), surface-constrained placement on a canvas part with grid snapping, overlap checks via GetTouchingParts, surface selection, and DataStore save/load by serializing object-space CFrames.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[scripting-and-performance]]** Use RunService:IsServer() inside a shared class so one module handles both server and client logic without duplicated code.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[client-server-and-remotes]]** For filtering-enabled placement, have the client preview locally and fire the server to finalize; the server holds the authoritative object list.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[client-server-and-remotes]]** Only send minimal data (action name, model, CFrame) to the server; the server already holds the same state in its twin object.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[anti-exploit-and-security]]** Validate placements on the server (collision check and constraints) before cloning the model, since clients can send arbitrary CFrames.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[physics-pathfinding-and-npc-ai]]** Set a Touched connection before calling GetTouchingParts(), since parts need a touch interest for GetTouchingParts to return results.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[data-persistence]]** Serialize placed items as object-space CFrame strings mapped to item names, and only call DataStore from the server inside pcall.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[data-persistence]]** Handle load failures by warning the error; return saved data only on success to avoid overwriting saves with empty data.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[building-and-level-design]]** Give each placeable model a transparent, non-collidable PrimaryPart as its bounding box so placement math uses consistent sizes.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[building-and-level-design]]** Snap placement to a grid by rounding constrained x/y to GridUnit multiples, offset by half-size remainder, to keep objects aligned.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[code-architecture-and-frameworks]]** Use OOP classes with metatables and separate constructors (new, fromSerialization) to keep reusable, modular systems.
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) **[[common-mistakes]]** Avoid defining methods with a custom self parameter name; it hurts readability for others, so keep the conventional self.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-furniture-placement-system/205509) GridUnit: **2 (locks placement to a 2x2 grid example)** (Grid snapping example in placement class)

## Tools
RunService, ContextActionService, DataStoreService, Roblox Studio Touched/GetTouchingParts

## He points to
- scriptinghelpers original post
- DevForum post on OOP in Lua (linked, not named)
- EgoMoose blog (future post mentioned)

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
