---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-luau-scope.md
title: "Roblox/creator-docs/content/en-us/luau/scope.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/luau/scope.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0192
relevance: 0
density: low
tags: ["research-source", "github", "other"]
---
# gh-Roblox-creator-docs-f-content-en-us-luau-scope.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Luau scope documentation (global vs local, capture, shadowing). Nothing about Blender, Claude, MCP, bpy, or asset pipelines. Only tangential value: Luau scripting performance advice for Roblox scripts.

## Claims
- c1: Luau accesses globals via hash lookup; a global in a time-critical loop can be over 10% slower than a local. Prefer the local keyword. *(doc, medium; other)*
- c2: Scripts cannot share globals or locals; use ModuleScripts to share values and functions between scripts. *(doc, high; other)*

## Numbers
- n1: **global vs local loop slowdown**: >10% global variable in time-critical loop vs local
