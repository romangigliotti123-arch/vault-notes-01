---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-rel-v2.1.0
title: "HoldMyBeer-gg/blenderwright v2.1.0: v2.1.0"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v2.1.0"
published: "2026-10-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "other"]
---
# gh-HoldMyBeer-gg-blenderwright-rel-v2.1.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blenderwright v2.1.0, an MCP-style tool that lets LLM clients (including local Ollama models) drive Blender. Changes cover toolsets for small-context clients, vision-model screenshot handling, negative-scale fixes, bounded agent loops, sequencer tools, and a dimensions/world-bounds report. No Roblox-specific content.

## Claims
- c1: v2.1.0 adds toolsets so small-window clients load tools on demand instead of all at once. *(doc, high; claude-blender-mcp)*
- c2: Negative-scale error message now tells the user to rotate the object, not to add a Mirror modifier. *(doc, high; common-mistakes-fixes)*
- c3: Negative primitive scale is converted into rotation automatically. *(doc, high; common-mistakes-fixes)*
- c4: Screenshots are now passed to the vision model; a separate vision model answers and the chat model receives a critique. *(doc, medium; claude-blender-mcp)*
- c5: Ollama agent loop is bounded by the context window, and repeated calls are answered from cache. *(doc, medium; claude-blender-mcp)*
- c6: Thinking mode is left to the model by default; --think and --no-think flags override it; inline <think> tags are stripped. *(doc, medium; claude-blender-mcp)*
- c7: Create tool results now report object dimensions and world bounds. *(doc, medium; claude-blender-mcp)*
- c8: join_objects error now lists which object names no longer exist after joining. *(doc, medium; common-mistakes-fixes)*
- c9: Long creation names are truncated to fit limits. *(doc, low; claude-blender-mcp)*
- c10: Dependency lock upgraded past 64 known vulnerabilities, with an audit step added to CI. *(doc, medium; claude-blender-mcp)*
- c11: Release adds sequencer tools for image strips, sound, and video output; animated launch demo added to README. *(doc, medium; other)*

## Numbers
- n1: **known vulnerabilities cleared**: more than 64 (lock upgrade) Dependency lock upgraded past 64 known vulnerabilities; audited in CI
- n2: **release date**: 2026-10-07 v2.1.0 tag; previous version v2.0.1

## Techniques
- t1: **On-demand toolsets**: Group Blender tools into sets loaded only when needed, so clients with small context windows are not flooded with tool definitions.
- t2: **Negative scale to rotation**: Negative primitive scale is rewritten as an equivalent rotation instead of leaving a mirrored negative scale.

## Points to
- https://github.com/HoldMyBeer-gg/blenderwright/compare/v2.0.1...v2.1.0
- https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v2.1.0
