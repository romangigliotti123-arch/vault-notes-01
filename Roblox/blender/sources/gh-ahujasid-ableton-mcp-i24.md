---
type: research-source
id: gh-ahujasid-ableton-mcp-i24
title: "ahujasid/ableton-mcp#24 Remote Script Errors in macOS"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/24"
published: "2025-04-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 0
density: low
tags: ["research-source", "github", "other"]
---
# gh-ahujasid-ableton-mcp-i24

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue about ahujasid/ableton-mcp (Ableton Live, not Blender or Roblox). Covers a macOS Remote Script SyntaxError caused by an erroneous "import Ableton MCP" line, and an install-folder name with a space. Fixes: import from _Framework.ControlSurface, rename folder to AbletonMCP, reset the MCP JSON config. Little relevance to the Blender-Roblox topic.

## Claims
- c1: Source concerns Ableton Live MCP integration, not Blender, blender-mcp, bpy, or Roblox. No Blender-to-Roblox content present. *(doc, high; other)*
- c2: Live 12.1.11 Remote Script raised SyntaxError 'invalid syntax' because the script contained 'import Ableton MCP' (a space in the module name). *(experience, high; other)*
- c3: Commenter fix: replace the bad import with 'from _Framework.ControlSurface import ControlSurface'. *(experience, medium; other)*
- c4: Remote Script folder must be named without a space (AbletonMCP, not 'Ableton MCP') inside Ableton's MIDI Remote Scripts folder; this fixed the reporter's issue. *(experience, high; other)*
- c5: Full reset of the MCP JSON config file, rather than merging entries, resolved the duplicate-server problem. *(experience, medium; other)*

## Numbers
- n1: **Ableton Live version**: 12.1.11 

## Techniques
- t1: **Remote Script folder check**: Verify the script folder name has no spaces and sits in the MIDI Remote Scripts directory; read Ableton's log for RemoteScriptError lines.

### Code: Corrected import line for an Ableton Remote Script (per commenter)
```python
from _Framework.ControlSurface import ControlSurface
```

## Points to
- https://github.com/ahujasid/ableton-mcp/issues/24
