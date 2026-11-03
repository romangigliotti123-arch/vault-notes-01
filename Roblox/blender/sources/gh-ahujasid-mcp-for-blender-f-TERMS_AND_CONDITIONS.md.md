---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-TERMS_AND_CONDITIONS.md
title: "ahujasid/mcp-for-blender/TERMS_AND_CONDITIONS.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/TERMS_AND_CONDITIONS.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "creator-workflows"]
---
# gh-ahujasid-mcp-for-blender-f-TERMS_AND_CONDITIONS.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Terms and privacy policy for the blender-mcp addon (ahujasid, Aug 2026). Covers opt-in telemetry: prompts, generated code, screenshots, scene metadata and manual Blender operator names are collected only when consent is enabled in addon preferences and the MCP server runs. Minimal anonymous usage record is sent by default; DISABLE_TELEMETRY=true disables it. Data may be retained indefinitely and used for AI training. Nothing on Roblox export.

## Claims
- c1: Telemetry consent is disabled by default in the Blender MCP addon preferences; prompts, code, screenshots and scene metadata are collected only after explicit opt-in. *(doc, high; claude-blender-mcp)*
- c2: Without opt-in, only a minimal anonymous usage record is sent: random install ID, session ID, tool name, success, duration, Blender MCP and Blender versions, OS, timestamp. *(doc, high; claude-blender-mcp)*
- c3: Setting DISABLE_TELEMETRY=true in the MCP server environment disables all telemetry, including the anonymous usage record. *(doc, high; claude-blender-mcp)*
- c4: When opted in, manual Blender edits are recorded as operator names (e.g. object.delete, transform.translate) and undo/redo; undo shortly after an AI action is treated as rejecting it. *(doc, high; claude-blender-mcp)*
- c5: Trajectory, screenshot and manual-edit collection requires both telemetry consent enabled and the MCP server running; stopping the server removes the edit observers. *(doc, high; claude-blender-mcp)*
- c6: File paths and filenames from operator settings are filtered out before sending; full .blend files and raw mesh geometry are not collected unless in compact metadata. *(doc, medium; claude-blender-mcp)*
- c7: Collected data may be retained indefinitely, used to train future AI models, and released in open datasets; once trained or published it may not be fully removable. *(doc, high; creator-workflows)*
- c8: Users must be 16 or older to opt in; the project is a solo open-source project with no guaranteed security. *(doc, medium; claude-blender-mcp)*
- c9: AI-generated code is provided as-is with no warranty; the user is responsible for reviewing it before use. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **Minimum age for telemetry opt-in**: 16 
- n2: **Telemetry default state**: off (opt-in) 

## Techniques
- t1: **Disable telemetry**: Set DISABLE_TELEMETRY=true in the MCP server's environment to stop all usage records. Telemetry consent can be withdrawn by unchecking the addon preference.

### Code: Disable all Blender MCP telemetry
```env
DISABLE_TELEMETRY=true
```

## Quotes (brief, for attribution)
> Telemetry is off by default; nothing in this section applies unless you opt in.  (ahujasid)

## Points to
- mailto:[email]
