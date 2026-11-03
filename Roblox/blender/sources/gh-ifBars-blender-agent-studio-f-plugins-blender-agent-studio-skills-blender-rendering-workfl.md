---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-rendering-workfl
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-rendering-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-rendering-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0032
relevance: 1
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-rendering-workfl

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill doc for Blender rendering: stills, turntables, sequences, and denoise/color/output policy. Covers a Claude-facing MCP render tool and a headless background render CLI. Nothing on Roblox import, export, or mesh limits. Useful only as a reference for headless Blender render invocation.

## Claims
- c1: blender_render_scene tool: call with inspectOnly true first; select cameras by exact name and optional frames; max 12 camera/frame combinations. *(doc, high; claude-blender-mcp)*
- c2: blender_render_scene defaults: active camera/frame, longest edge capped at 1280, Cycles samples capped at 64, GPU auto-selected with recorded CPU fallback. *(doc, high; claude-blender-mcp)*
- c3: blender_render_evidence replaces cameras and lighting, so it is for standardized geometry checks, not final interior images. *(doc, high; claude-blender-mcp)*
- c4: Standalone render runs headless via Blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python render_scene.py, with --max-edge and --samples flags. *(doc, high; bpy-scripting-headless)*
- c5: render_scene.py writes render-manifest.json with camera/frame image paths; render_evidence.py writes evidence.json and contact_sheet.png. Use a fresh output directory per run. *(doc, high; bpy-scripting-headless)*
- c6: --render-edge 1536 renders at that longest edge above authored size, while --max-edge alone only caps resolution. *(doc, high; bpy-scripting-headless)*
- c7: Denoise policy: preview uses low samples (16-32) at 512-800px; final uses OIDN High with Accurate prefilter and Color+Albedo+Normal; use one denoising stage only. *(doc, medium; creator-workflows)*
- c8: If no OpenImageDenoise or OptiX is available, the render proceeds with denoising off and manifest records effectivePolicy off with reason. *(doc, high; bpy-scripting-headless)*

## Numbers
- n1: **max camera/frame combinations**: 12 blender_render_scene camera+frame selection limit
- n2: **default longest edge**: 1280 px blender_render_scene default cap
- n3: **default Cycles samples**: 64 blender_render_scene default cap
- n4: **preview sample cap**: 16-32 samples at 512-800 px look-dev preview denoise guidance
- n5: **--render-edge example**: 1536 renders above authored size, aspect preserved

## Techniques
- t1: **Headless standalone render**: Run Blender with --background --factory-startup --disable-autoexec --python-exit-code 1 --python render_scene.py -- with --input, fresh --output-dir, --max-edge and --samples. Inspect render-manifest.json for image paths.
- t2: **Inspect-then-render via MCP**: Call blender_render_scene with inspectOnly true to learn camera names and settings, then select cameras and frames explicitly for the render.

### Code: Headless standalone Blender render with bundled skill script
```powershell
& $env:BLENDER_EXECUTABLE --background --factory-startup --disable-autoexec `
  --python-exit-code 1 --python "<skill-root>/scripts/render_scene.py" -- `
  --input scene.blend --output-dir renders/preview-01 --max-edge 1280 --samples 64
```

## Points to
- https://docs.blender.org/manual/en/latest/render/cycles/render_settings/sampling.html
- ../blender-signage-workflow/references/surface-integration.md
- ../blender-modeling-workflow/references/whole-scene-workflow.md
