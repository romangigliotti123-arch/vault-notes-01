---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-SECURITY.md
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/SECURITY.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/SECURITY.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0007
relevance: 2
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "other"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-SECURITY.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Security policy for Blender Agent Studio plugin. Covers running a local Blender executable with Python scripts, restricting the bundled MCP to version checks, asset inspection and evidence renders (no generic arbitrary-Python tool), trusting only the BLENDER_EXECUTABLE install, caution with untrusted .blend auto-script execution, and treatment of generated artifacts as possibly private. Does not address Roblox export or import.

## Claims
- c1: Bundled MCP is intentionally limited to version checks, asset inspection, and evidence renders; it does not expose a generic arbitrary-Python tool. *(doc, high; claude-blender-mcp)*
- c2: Plugin invokes a local Blender executable and runs Python scripts inside Blender; users should review untrusted scripts before execution. *(doc, high; bpy-scripting-headless)*
- c3: BLENDER_EXECUTABLE should be set only to a trusted Blender installation. *(doc, high; claude-blender-mcp)*
- c4: Avoid running untrusted .blend files with automatic script execution enabled. *(doc, high; bpy-scripting-headless)*
- c5: Models, exports, renders, benchmark prompts, agent traces and evaluation output may contain private source material; they are git-ignored by default and should be reviewed before sharing. *(doc, high; other)*

### Code: Env var for trusted Blender path
```text
BLENDER_EXECUTABLE
```

## Quotes (brief, for attribution)
> The bundled MCP is intentionally limited to version checks, asset inspection, and evidence renders; it does not expose a generic arbitrary-Python tool.  (ifBars)

## Points to
- https://github.com/ifBars/blender-agent-studio
