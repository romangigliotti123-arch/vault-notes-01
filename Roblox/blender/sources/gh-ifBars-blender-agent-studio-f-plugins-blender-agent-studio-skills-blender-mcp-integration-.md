---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-mcp-integration-
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-mcp-integration/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-mcp-integration/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 3
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "other", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-mcp-integration-

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent Studio skill doc for choosing a Blender MCP layer. Covers the bundled Agent Studio Live addon and blender_open_viewport, Blender's official Lab MCP, the bundled batch and render tools, and ahujasid/blender-mcp as a fallback. Also covers Mixamo and Pixabay browser handoffs, the optional Rust scene analyzer, and reproducibility and benchmarking rules. No Roblox-specific content.

## Claims
- c1: Use the narrowest MCP layer that improves the task; bundled tools and Blender CLI cover ordinary scripted builds, inspection and rendering. *(doc, high; claude-blender-mcp)*
- c2: Agent Studio Live addon is the inline viewport option: install addon/blender_agent_studio_live.py, enable it, press Connect Agent Studio in the 3D View sidebar. Needs an interactive session and GPU context. *(doc, high; claude-blender-mcp)*
- c3: Agent Studio Live bridge does not execute arbitrary Python or mutate geometry; general live authoring needs a separate integration. *(doc, high; claude-blender-mcp)*
- c4: Add Blender's official Lab MCP only when live interaction with an open session is needed, and only on a supported Blender version. *(doc, high; claude-blender-mcp)*
- c5: Consider ahujasid/blender-mcp only for remote-host, Poly Haven, Sketchfab or external 3D-generation needs, accepting extra install, network, credential and telemetry exposure. *(doc, high; claude-blender-mcp)*
- c6: Do not run multiple add-on socket servers on the same host and port. *(doc, high; claude-blender-mcp)*
- c7: If no live Blender session exists, offer to open Blender and ask first, unless the user already authorized it; preserve existing sessions and unsaved work. *(doc, high; claude-blender-mcp)*
- c8: blender_render_scene preserves cameras, lights, volumes and color management and returns the first image inline; inspectOnly discovers scene settings before rendering. *(doc, high; bpy-scripting-headless)*
- c9: Bundled Poly Haven search/download tools fetch verified CC0 textures and HDRIs with no extra add-on or API key. *(doc, high; texturing-baking-uv)*
- c10: blender_compare_reference gives a camera-matched reference/silhouette/overlay board without Rust; projection metrics need a reviewed white-on-black mask, otherwise visual comparison only. *(doc, high; bpy-scripting-headless)*
- c11: blender_describe_scene, blender_quality_report and blender_compare_scenes need the bundled Rust SceneIR analyzer; setup via bun run setup:runtime with a stable Rust toolchain or BAS_RUNTIME_EXECUTABLE. Rebuild after updates. *(doc, high; bpy-scripting-headless)*
- c12: Semantic roles come only from authored bas_role properties; ground checks require named objects and groundZ; AABB relations are candidates, not exact mesh intersections. *(doc, high; bpy-scripting-headless)*
- c13: Keep the durable model in a Python source file even when using live MCP execution; save a new .blend before risky arbitrary-code operations. *(doc, high; creator-workflows)*
- c14: Benchmark MCP value by comparing skills with MCP unavailable vs enabled, same task, model, effort, time budget and evaluator; retain only if outcomes or reliable completion cost improve. *(doc, high; creator-workflows)*
- c15: blender_prepare_mixamo_search returns a browser search URL and workflow, not catalog results; host browser tools do search, preview and download, then blender_import_mixamo_animation creates a new standalone animated .blend. Adobe sign-in stays in browser. *(doc, high; claude-blender-mcp)*
- c16: blender_prepare_pixabay_sound_search returns a search URL only; it does not use an audio API, does not scrape, and does not import audio into Blender. Record title, creator, duration and source page with the file. *(doc, high; other)*
- c17: Use blender-asset-validation for final clean-process inspection and fixed evidence cameras; record which MCP tools were used in benchmark runs. *(doc, medium; creator-workflows)*

## Numbers
- n1: **Socket servers per host/port**: 1 (do not run multiple on same host/port) 
- n2: **Rust runtime requirement**: stable Rust toolchain, or prebuilt BAS_RUNTIME_EXECUTABLE 
- n3: **Poly Haven assets**: verified CC0 textures and HDRIs, no API key 

## Techniques
- t1: **Layered MCP selection**: Start with bundled tools/CLI; add Lab MCP only for live session interaction; use ahujasid/blender-mcp only for its extra remote or generation integrations.
- t2: **Scene inspection before render**: Run blender_render_scene with inspectOnly to discover scene settings, then render with cameras, lights and colour management preserved.
- t3: **Scene analysis gating**: Describe scene, query exact objectId and descendants, supply constraints from brief, then compare preserved vs regenerated assets with invariantObjects excluding edited parts.
- t4: **Reproducibility loop**: Keep model in Python source, save .blend before risky arbitrary code, use MCP screenshots for iteration, final validation in a clean process.

### Code: Set up the optional Rust scene-analysis runtime in the installed plugin root
```shell
bun run setup:runtime
```

## Quotes (brief, for attribution)
> The bridge does not execute arbitrary Python or mutate geometry. General live authoring can still use a separate integration as described below.  (ifBars)
> Retain an MCP dependency only when it improves outcomes or materially reduces reliable completion cost.  (ifBars)

## Points to
- https://github.com/ifBars/blender-agent-studio/blob/main/docs/live-viewport.md
- https://github.com/ahujasid/blender-mcp
- https://pixabay.com/service/license-summary/
- https://pixabay.com/api/docs/
- references/mcp-options.md
- references/astra-workflow.md
