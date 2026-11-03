---
type: research-source
id: gh-ifBars-blender-agent-studio-rel-gallery-scenes-hd-2026-10-04
title: "ifBars/blender-agent-studio gallery-scenes-hd-2026-10-04: HD scene comparison previews — October 4, 2026"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/releases/tag/gallery-scenes-hd-2026-10-04"
published: "2026-10-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-rel-gallery-scenes-hd-2026-10-04

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release note for ifBars/blender-agent-studio gallery of agent-driven Blender scene comparisons (plugin-with-skills vs isolated baseline, MCP absent in both). Covers 10 new pairs across GPT/Opus/Sonnet models, HD preview renders, CPU-capped benchmark runs, and a lathe-helper topology fix. No Roblox-specific content.

## Claims
- c1: Comparison design explicitly excludes MCP: plugin condition uses pinned skills/scripts versus an isolated baseline, with MCP absent in both arms. *(doc, high; claude-blender-mcp)*
- c2: Eight pairs had two counterbalanced reviews: 4 favored baseline, 1 favored plugin, 3 split or tied; 2 market pairs had no valid reviews. Authors call these directional, not a success rate. *(data, high; claude-blender-mcp)*
- c3: Benchmarks run on Blender 5.2.2 LTS; later jobs capped at 20% CPU, Below Normal priority, one generation at a time. *(doc, high; bpy-scripting-headless)*
- c4: Repeated lathed props showed topology failures; a pole-sharing lathe helper removed zero-length pole edges on two profiles while preserving bounds and face counts. Authors state outputs do not show visual improvement. *(doc, medium; procedural-generation)*
- c5: HD previews render at 1536-pixel longest edge; Cycles prefers OptiX with GPU OpenImageDenoise, Eevee scenes keep their engine. *(doc, medium; texturing-baking-uv)*
- c6: Scorer calibration permits finite render-only scene bounds and recognizes ordinary food names, but geometry and export gates remain enforced. *(doc, medium; creator-workflows)*
- c7: A missing preview view previously stretched a one-pixel placeholder; the viewer now disables the slider and shows the available image in full. *(doc, low; common-mistakes-fixes)*

## Numbers
- n1: **Blender version**: 5.2.2 LTS 
- n2: **Paired comparison count**: 31 pairs total; 10 added 
- n3: **HD preview longest edge**: 1536 px 
- n4: **CPU cap for benchmark jobs**: 20%, Below Normal priority 
- n5: **Authored camera views rendered for new pairs**: 60 
- n6: **Planned pairs with no complete evaluator results**: 14 

## Techniques
- t1: **Pole-sharing lathe helper**: Generate lathed props with shared pole vertices; remove zero-length pole edges; verify bounds and face counts preserved before duplicating props.
- t2: **Resource-capped sequential benchmark jobs**: Run one generation at a time at 20% CPU cap with Below Normal priority; record resource policy in pair metadata.

## Points to
- https://ifbars.github.io/blender-agent-studio/comparisons/
- https://github.com/ifBars/blender-agent-studio/releases/tag/gallery-scenes-hd-2026-10-04
