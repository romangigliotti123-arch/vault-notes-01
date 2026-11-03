---
type: research-source
id: gh-ifBars-schedule-one-blender-f-AGENTS.md
title: "ifBars/schedule-one-blender/AGENTS.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/AGENTS.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: medium
tags: ["research-source", "github", "blender-roblox-export-import", "other"]
---
# gh-ifBars-schedule-one-blender-f-AGENTS.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
AGENTS.md for ifBars/schedule-one-blender, a bring-your-own-game-copy tool that converts Unity scenes to Blender. It covers repo hygiene (no game assets in Git), Unity-to-Blender axis mapping (x,y,z to x,z,y, 1 unit = 1 m), and validation rules. It does not cover Roblox, blender-mcp, or Claude-driven Blender workflows.

## Claims
- c1: Unity (x,y,z) maps to Blender (x,z,y) with one unit = one metre and reflected winding; this is a Unity-to-Blender convention, not a Roblox export rule. *(doc, high; blender-roblox-export-import)*
- c2: Repo policy forbids committing game files, extracted meshes/textures, .blend files or generated reports; generated content goes in ignored builds/ directory. *(doc, high; other)*
- c3: Source/test success is explicitly stated as not proof of in-game or visual parity; validation requires fresh Blender processes and inspecting a textured preview. *(doc, high; other)*

## Numbers
- n1: **coordinate unit scale**: 1 unit = 1 metre 
- n2: **editor texture proxy budget**: 512px 

## Points to
- https://github.com/ifBars/schedule-one-blender
