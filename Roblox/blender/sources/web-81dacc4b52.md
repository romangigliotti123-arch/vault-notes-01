---
type: research-source
id: web-81dacc4b52
title: "Roblox docs: studio/optimization/memory-usage"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/studio/optimization/memory-usage.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "web", "mesh-texture-limits", "other"]
---
# web-81dacc4b52

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on the Developer Console Memory and LuauHeap tools for monitoring in-game memory. Covers PlaceMemory/CoreMemory categories, Luau heap snapshots, and Graph, Object Tags, Memory Categories, Object Classes and Unique References views. Does not cover Blender, bpy, blender-mcp, or the Blender-to-Roblox asset pipeline.

## Claims
- c1: Roblox docs state memory usage in the Developer Console is shown in MB per category, with a chart over time; this is a runtime profiling tool, not a Blender export tool. *(doc, high; other)*
- c2: PlaceMemory includes GraphicsMeshParts, GraphicsTexture and HttpCache categories, giving a way to see mesh and texture memory cost in a running place. *(doc, medium; mesh-texture-limits)*

## Numbers
- n1: **Memory display unit**: MB per category Memory tool shows usage in MB per category with a time chart
- n2: **Graph view hides small nodes**: < 2 KB collapsed to '…' Luau heap Graph view threshold

## Techniques
- t1: **Luau heap snapshot comparison**: Open Developer Console, select LuauHeap, pick Client or Server, click Create Snapshot. Take multiple snapshots and compare to find growth over time.
- t2: **Find unparented instances**: Open Unique References or Unparented Instances view; check Count and Total Instances, then inspect pinning paths and disconnect unneeded references.

## Quotes (brief, for attribution)
> When memory usage reaches engine limits, the user's device or server may crash, so you need to actively monitor usage.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/performance-optimization/improve#memory-usage
- https://create.roblox.com/docs/luau/scope#capture
