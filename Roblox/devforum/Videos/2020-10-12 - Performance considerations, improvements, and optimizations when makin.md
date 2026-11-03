---
title: "Performance considerations, improvements, and optimizations when making a game"
url: https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-10-12
views: 266
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Performance considerations, improvements, and optimizations when making a game

[Open](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) | Roblox DevForum | 266 views | 2020-10-12

## Summary
DevForum resource (Mystifine, 2020) on Roblox performance: particles (:Emit ignores automatic quality scaling), instance count, multiple places, lighting, memory, scripting (remotes, loops, localizing, memory leaks, PartCaching), building (BasePart properties, triangles, LevelOfDetail/RenderFidelity), and GUI (visibility, static GUI, tweens).

## Tips
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[vfx-and-particles]]** Scale :Emit() counts by the player's SavedQualityLevel, since :Emit() bypasses Roblox's automatic particle optimisation.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[vfx-and-particles]]** Avoid extremely high ParticleEmitter rates; they hurt lower-end devices notably.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Reduce instance count; avoid converting whole data tables into Folders and Value objects. Use RemoteFunctions or compact strings instead.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Consider splitting heavy content across multiple places with TeleportService to reduce instances, maps, meshes and running scripts.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Lighting choice matters for low-end users; ShadowMap and Future are the most expensive options.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Check memory by joining a similar game and pressing F9; use it as a benchmark for your own target.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Offer a low-graphics option: locally switch materials to SmoothPlastic, disable CastShadow, and use cheaper lighting.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Keep data sent between server and client minimal; large tables in remote arguments cause latency-like lag.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[client-server-and-remotes]]** Remote queues are per player, so one spamming exploiter only affects their own requests. Still debounce and sanity-check before expensive server work.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Run visual effects (tweens, particles) on the client and replicate only when needed, rather than on the server.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Use built-in events (.Changed, GetPropertyChangedSignal) instead of while loops that poll, e.g. for updating a TextLabel.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Parent instances last, after setting all properties, so changes replicate once instead of many times.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Destroy unused instances and disconnect connections to prevent memory leaks; consider Quenty's Maid class.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[scripting-and-performance]]** Use PartCaching/PartPooling to reuse parts instead of constantly creating new ones.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[luau-language-and-types]]** Localize variables and library functions; the gain is small, so prioritise other optimisations first. Use table.clear() over manual clearing.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Minimise part count: combine parts where possible and use greedy meshing for block-based games.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Apply textures only to faces that players can see; skip hidden faces.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Anchor parts, use SmoothPlastic, CollisionFidelity Box, and disable CastShadow where detail is not needed; set Transparency to 0 or 1.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Use the lowest triangle count that achieves the look; a cube needs 12 triangles.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Set Model LevelOfDetail to Automatic or Disabled with StreamingEnabled, and RenderFidelity to Automatic, to help lower-end devices.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[building-art-and-assets]]** Copy and transform identical models rather than individually editing them, to share memory.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[ui-ux-design]]** Set GUI Visible to false instead of tweening UI off-screen; hidden GUIs stop rendering and input.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[ui-ux-design]]** Reduce tweens on GUI; dynamic GUI costs more draw time than static GUI, visible in MicroProfiler.
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) **[[optimization-and-streaming]]** Avoid unnecessary unique assets (images, meshes, textures, animations, sounds); keep sound music loaded only when needed.

## Numbers
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) Triangle count for a cube: **12 triangles** (Developer-cited good count for a cube; fewest for the desired look otherwise)
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) Streaming radius example: **256 studs** (Small workspace streaming radius for Studio playsolo testing)
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) Representative mesh distance: **1024 studs** (Representative meshes are designed to be seen at this distance)
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) Instances for nested inventory example: **7 instances vs 1 StringValue** (Nested Folder/Value structure versus compacted string for two items)
- [page](https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499) Player instances from data as Values: **200+** (Beginner pattern of storing whole data tables as instances)

## Tools
F9 developer console, MicroProfiler, Quenty's Maid class, Roblox Packages, StreamingEnabled, LevelOfDetail property, RenderFidelity property, PartCaching/PartPooling modules

## He points to
- DevForum: Limits of RemoteEvents
- DevForum: What are bad programming habits that you see often by scripters
- Mariofly5 building optimization post
- Greedy meshing post
- Roblox LevelOfDetail beta feature post
- Medium: Don't use 'next' instead of 'pairs'

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[luau-language-and-types]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
