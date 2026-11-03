---
type: research-source
id: gh-ifBars-blender-agent-studio-rel-gallery-scenes-2026-10-04
title: "ifBars/blender-agent-studio gallery-scenes-2026-10-04: Scene comparison gallery — October 4, 2026"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/releases/tag/gallery-scenes-2026-10-04"
published: "2026-10-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation"]
---
# gh-ifBars-blender-agent-studio-rel-gallery-scenes-2026-10-04

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for ifBars/blender-agent-studio gallery of AI-generated Blender scene comparisons (plugin-assisted vs isolated baseline). Covers 31 pairs across GPT 6 Astra, GPT 6.1 Sol, Opus 5.5, Sonnet 5.5, with one-generation-per-condition results. No Roblox export, MCP setup, or import content.

## Claims
- c1: Gallery comparisons state MCP is absent in both conditions; the variable is a pinned plugin with skills/scripts versus an isolated baseline. *(doc, high; claude-blender-mcp)*
- c2: Results are one generation per condition and are described as directional examples, not a general success rate. *(doc, high; other)*
- c3: Targets Blender 5.2.2 LTS; generation ran with a 30-minute budget per pair and shared 20% CPU cap for later pairs. *(doc, medium; bpy-scripting-headless)*
- c4: Repeated lathed props showed topology failures; a pole-sharing lathe helper removed zero-length pole edges on two profiles while preserving bounds and face counts. *(doc, medium; procedural-generation)*
- c5: Gallery technical gates fail some outputs (scores 93.5 to 96 on fail rows); the revised lathe helper is not shown to improve visuals in the unchanged outputs. *(doc, medium; common-mistakes-fixes)*
- c6: Votes on 8 Astra counterbalanced pairs: 4 favored baseline, 1 favored plugin, 3 split or tied; two market pairs had no valid reviews. *(data, medium; creator-workflows)*

## Numbers
- n1: **Gallery pairs**: 31 total, 10 added Preview gallery pairs; 21 historical rows retained
- n2: **Blender version**: 5.2.2 LTS Version used for all comparisons
- n3: **Generation budget**: 30 minutes Per pair, same task and model within pair
- n4: **CPU cap**: 20% Shared cap for four later pairs, Below Normal priority, one generation at a time
- n5: **Astra paired reviews**: 4 baseline / 1 plugin / 3 split or tie Eight pairs with two counterbalanced reviews

## Techniques
- t1: **Pole-sharing lathe helper with prototype validation**: Validate lathed prop topology on a prototype before duplicating; remove zero-length pole edges; check bounds and face counts preserved.

## Points to
- https://ifbars.github.io/blender-agent-studio/comparisons/
- https://github.com/ifBars/blender-agent-studio/releases/tag/gallery-scenes-2026-10-04
