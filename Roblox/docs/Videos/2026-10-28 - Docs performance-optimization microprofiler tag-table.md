---
title: "Docs: performance-optimization / microprofiler / tag-table"
url: https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / microprofiler / tag-table

[Open](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference table of common MicroProfiler tags grouped by subsystem (navigation, animation/humanoids, audio, networking, rendering, scripts, simulation, UI), each with a description and performance advice for reducing cost.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Reduce pathfinding tile invalidations; they force paths to be recomputed. Invalidations are caused by non-navigable parts moving.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[physics-pathfinding-and-npc-ai]]** Reduce the number of Path:ComputeAsync() calls and their world extents. Reuse paths for multiple agents starting and ending in similar locations.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[genre-mechanics]]** Disable unneeded Humanoid states (e.g. Climbing, Swimming) on NPCs that don't need them to cut stepHumanoid cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[scripting-and-performance]]** Reduce callbacks to Humanoid.StateChanged, Running, Died, and AnimationTrack KeyframeReached/Ended; they add per-step cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[scripting-and-performance]]** Keep functions connected to RunService.Stepped, Heartbeat and RenderStepped as light as possible; delay or spread expensive work across frames.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[ui-ux-design]]** Keep work in UpdateInput minimal; push larger computations to later steps. Reduce tween counts and keep TweenService callbacks light.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[client-server-and-remotes]]** Replicate fewer objects or events, and reduce the size or count of property changes and remote invocations to lower network receive and dispatch cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[client-server-and-remotes]]** Set network ownership of parts to the current player to reduce interpolation cost, but expect more physics work on that client.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[client-server-and-remotes]]** Avoid frequently changing network ownership of parts; it inflates Distributed Physics Ownership and filterStep cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Reduce minimum and target streaming radii to lower StreamJob dispatch cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[building-and-level-design]]** Cubes are cheaper than complex meshes for collisions; use simpler collision boxes to reduce contact-solving cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[physics-pathfinding-and-npc-ai]]** Reduce joints created or destroyed at runtime to lower assemble cost; keep parts far apart so islands simulate separately.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Lower FallenPartsDestroyHeight, or reduce parts falling to it, to cut handleFallenParts cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[ui-ux-design]]** Avoid frequently changing parent or ZIndex of UI elements in LayerCollectors; keep element counts low before first render. Use fixed sizes for BillboardGuis.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Use CanvasGroups to reduce UI rendering cost at the expense of more memory. Reduce UIGradient and UICorner on text labels.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[building-art-and-assets]]** Use fewer, larger meshes instead of many small pieces to reduce frustum culling cost. Reduce visible Beams, ParticleEmitters and Humanoids.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[vfx-and-particles]]** Reduce ParticleEmitter count, emission rate and lifetime; limit emitter movement to cut particle update cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[building-art-and-assets]]** Disable CastShadow on complex meshes, highly transparent parts, and unimportant instances; fully transparent parts without decals should have it disabled.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Reduce the number of lights and shadow-casting geometry; use non-shadow-casting geometry for moving objects. Shadows are not computed below quality level 4.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[scripting-and-performance]]** Pool tables and reduce temporary table creation to lower Luau GC cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[scripting-and-performance]]** Break large property-update batches across frames to reduce updateInvalidParts cost.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[building-art-and-assets]]** Reduce visual changes to models with Humanoids or skinned MeshParts; use Bone.Transform over CFrame/Size changes to avoid bounding box updates.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** If waitUntilCompleted is high, too much is rendered; reduce scene complexity and use the Frame Rate Manager. If Present is high, you may be GPU-limited.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) **[[optimization-and-streaming]]** Reduce the number of BillboardGuis and Humanoid name/health labels that are visible to lower Pass3dAdorn cost.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) WaitingHybridScriptJob frequency: **Usually 30 times per second** (Resumes scripts waiting on WaitForChild or wait; throttled if overloaded)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) Shadow computation threshold: **Not performed at quality levels below 4** (ShadowMapSystem and Scene/Shadows steps)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table) Transparency bucket boundary: **Opaque: 0.01 or lower; Transparent: between 0.01 and 1** (Scene/Id_Opaque vs Id_Transparent MicroProfiler tags)

## Tools
MicroProfiler, LibMP

## He points to
- LibMP documentation on GitHub (complete MicroProfiler tag list)
- Improve performance (Roblox docs, linked from shadow advice)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[genre-mechanics]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
