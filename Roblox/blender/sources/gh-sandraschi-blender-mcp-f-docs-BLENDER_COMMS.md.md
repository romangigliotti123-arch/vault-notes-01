---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-BLENDER_COMMS.md
title: "sandraschi/blender-mcp/docs/BLENDER_COMMS.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/BLENDER_COMMS.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "other"]
---
# gh-sandraschi-blender-mcp-f-docs-BLENDER_COMMS.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Describes how the sandraschi blender-mcp webapp runs Blender: no persistent connection; each "Execute in Blender" spawns a fresh headless `blender --background --factory-startup --python` process via BlenderExecutor, captures stdout/stderr, then deletes the temp script. Covers BLENDER_EXECUTABLE/PATH requirements, failure modes, and Ollama-based script generation. Says nothing about Roblox export.

## Claims
- c1: Blender MCP webapp has no persistent connection to Blender: no socket, no add-on, no live instance; each run is a fresh process. *(doc, high; claude-blender-ai)*
- c2: Script execution runs `blender --background --factory-startup --python <temp_script.py>`, captures stdout/stderr, then deletes the temp file. *(doc, high; claude-blender-ai)*
- c3: Blender must be on PATH or set via BLENDER_EXECUTABLE (env or config); validate_blender_executable() failure yields 'Blender not found' and all script runs error. *(doc, high; claude-blender-ai)*
- c4: Script errors such as a missing add-on operator (e.g. primitive_solid_add for dodecahedron) make Blender exit non-zero with the error in output. *(doc, high; claude-blender-ai)*
- c5: Because each run is headless and fresh, you cannot sync or inspect a running Blender UI; no shared state between runs. *(doc, high; claude-blender-ai)*
- c6: BlenderExecutor(headless=False) would run one script with GUI; webapp defaults to headless. *(doc, medium; claude-blender-ai)*
- c7: Natural-language-to-bpy generation uses a local Ollama model (default URL http://localhost:11434, default model llama3.2) via backend tool generate_blender_script; model list from /api/tags and LM Studio /v1/models. *(doc, medium; claude-blender-ai)*
- c8: Webapp talks only to the backend on port 10849 by default; no separate bridge on port 8000. *(doc, medium; other)*
- c9: The document does not cover Roblox export, FBX/glTF settings, scale, or MeshPart import. *(doc, high; blender-roblox-export-import)*

## Numbers
- n1: **Default Ollama URL**: http://localhost:11434 Settings > LLM Provider default
- n2: **Default backend port**: 10849 Webapp to MCP backend
- n3: **Default LLM model**: llama3.2 Used if no model selected in Settings

## Techniques
- t1: **Subprocess-per-script execution**: Write code to temp file, run blender --background --factory-startup --python on it, capture stdout/stderr, delete file. Each call is an isolated process.
- t2: **Headless by default**: Run Blender without GUI; optionally set headless=False on BlenderExecutor for a windowed run.

### Code: Command the backend runs per script execution
```shell
blender --background --factory-startup --python <temp_script.py>
```

### Code: Pull model for Ollama script generation
```shell
ollama pull llama3.2
```

## Quotes (brief, for attribution)
> There is no persistent connection to Blender. No socket, no add-on, no live Blender instance.  (sandraschi)
> So every "Execute in Blender" = spawn a new Blender process, run the script, process exits.  (sandraschi)

## Points to
- src/blender_mcp/config.py
- BlenderExecutor
- Ollama /api/tags
- LM Studio /v1/models
