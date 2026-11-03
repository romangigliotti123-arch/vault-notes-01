---
type: research-source
id: gh-ifBars-schedule-one-blender-f-CONTRIBUTING.md
title: "ifBars/schedule-one-blender/CONTRIBUTING.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/CONTRIBUTING.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0006
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "other"]
---
# gh-ifBars-schedule-one-blender-f-CONTRIBUTING.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
CONTRIBUTING.md for ifBars/schedule-one-blender, a Blender project tied to a Unity game. Rules: submit only original scripts, docs and synthetic tests; never commit game assemblies, decompiled code, textures, meshes or generated scenes. Keep changes narrow, add tests for contracts, run AGENTS.md audits. Compatibility reports need game, Unity and Blender versions and Mono vs IL2CPP. No Roblox, bpy-MCP, or FBX/glTF pipeline content.

## Claims
- c1: Repo accepts only original scripts, docs and synthetic tests; game assets and decompiled code must never be committed. *(doc, high; other)*
- c2: CI has no game access and uploads no artifacts; tests and tracked-file audit are listed in AGENTS.md. *(doc, high; automation-and-creator-workflows)*
- c3: Compatibility reports must state game, Unity and Blender versions, Mono vs IL2CPP, failing phase and redacted exception. *(doc, high; other)*

## Points to
- AGENTS.md
