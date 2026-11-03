---
title: "How to create a Plot Placement System in Roblox #2 - Placing stuff!"
url: https://youtu.be/SVBmZ3yIMRo
creator: B Ricey
official: false
advice_density: medium
date: 2024-03-02
views: 18265
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to create a Plot Placement System in Roblox #2 - Placing stuff!

[Watch](https://youtu.be/SVBmZ3yIMRo) | BRicey | 18,265 views | 2024-03-02

## Summary
Part 2 of a Roblox plot placement tutorial. Builds a client-side ghost preview of a model (raycast from mouse, pivot at bottom, transparency 0.5, no collision) bound to RenderStepped-style render step, then a RemoteFunction sends the object name and CFrame to the server, which clones it into the player's plot. Validation is deferred to a later video.

## Tips
- [1:29](https://youtu.be/SVBmZ3yIMRo?t=89) **[[building-and-level-design]]** Set the model's pivot at the bottom center so raycast hit positions sit flush on the ground without Y offsets.
- [2:44](https://youtu.be/SVBmZ3yIMRo?t=164) **[[building-art-and-assets]]** Anchor all parts in placeable models; the placement system relies on anchored objects.
- [4:06](https://youtu.be/SVBmZ3yIMRo?t=246) **[[client-server-and-remotes]]** Render the preview only on the client by cloning the model, disabling CanCollide and CanQuery, and setting transparency to 0.5 for a ghost look.
- [11:09](https://youtu.be/SVBmZ3yIMRo?t=669) **[[scripting-and-performance]]** Store bind and action names in constants so the same string is used to bind and unbind, and typos are caught by the compiler.
- [16:25](https://youtu.be/SVBmZ3yIMRo?t=985) **[[client-server-and-remotes]]** Send only the object name and target CFrame to the server; the client can't be trusted, so the server must look up the object itself.
- [16:25](https://youtu.be/SVBmZ3yIMRo?t=985) **[[client-server-and-remotes]]** Use a RemoteFunction returning a boolean when the client needs to know whether placement succeeded.
- [19:30](https://youtu.be/SVBmZ3yIMRo?t=1170) **[[anti-exploit-and-security]]** Validate server input with FindFirstChild and nil checks before cloning; exploiters can send junk names.
- [22:17](https://youtu.be/SVBmZ3yIMRo?t=1337) **[[development-process-and-speed]]** Always clean up in the destroy path (unbind render step and input actions) or the build tool leaks behaviour after toggling off.

## Numbers
- [9:51](https://youtu.be/SVBmZ3yIMRo?t=591) Raycast max distance: **1000 studs** (Placement ray scaled by 1000 for rendering; validation deferred)
- [4:06](https://youtu.be/SVBmZ3yIMRo?t=246) Preview transparency: **0.5** (Ghost preview part transparency)

## Tools
Roblox Studio, Luau, RemoteFunction, RunService:BindToRenderStep, ContextActionService, UserInputService, Workspace:Raycast

## He points to
- Author's Minecraft-style placement series (earlier video)
- Author's plot setup video (part 1)

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
