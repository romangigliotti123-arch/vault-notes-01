---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-studio-mcp.md
title: "Roblox/creator-docs/content/en-us/studio/mcp.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/studio/mcp.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0394
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-import-pipeline"]
---
# gh-Roblox-creator-docs-f-content-en-us-studio-mcp.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for the built-in Studio MCP server (stdio). It lets Claude Code/Desktop and other clients read the data model, edit scripts, run Luau, insert assets, generate meshes, and playtest. It covers enabling, quick connect, JSON/CLI config, multi-instance use, and troubleshooting. It has nothing on Blender, bpy, or FBX/glTF import; it only offers a Roblox-side counterpart to blender-mcp.

## Claims
- c1: Roblox Studio has a built-in MCP server using stdio transport, so Claude can drive Studio directly (Roblox side, not Blender). *(doc, high; claude-blender-mcp)*
- c2: Quick connect supports Claude Code and Claude Desktop, plus Antigravity, Codex CLI, Cursor, Gemini CLI and VS Code. Enable via Assistant > … > Manage MCP Servers > Enable Studio as MCP server. *(doc, high; claude-blender-mcp)*
- c3: Security warning: MCP clients can read and modify content in open places, so connect only trusted clients. *(doc, high; claude-blender-mcp)*
- c4: insert_asset inserts by numeric asset ID (models, meshes, images, audio, video, animations, packages). This could place Blender-exported meshes after they are uploaded. *(doc, medium; roblox-import-pipeline)*
- c5: generate_mesh makes a textured 3D mesh from a text prompt. generate_procedural_model builds primitive-part models (blocks, spheres, cylinders, wedges) with attributes and reference images. wait_job_finished polls the job. *(doc, high; procedural-generation)*
- c6: Every tool call takes a studio_id; list_roblox_studios returns names, instance IDs and place IDs so one client can target several Studio windows. *(doc, high; creator-workflows)*
- c7: Playtest tools (start_stop_play, get_console_output, screen_capture, character_navigation, keyboard/mouse input) let an agent verify imported assets in play mode. execute_luau requires datamodel_type Edit, Client or Server. *(doc, high; creator-workflows)*
- c8: Troubleshooting: restart Studio and the client, verify the binary path, and check JSON syntax. A missing comma between mcpServers entries breaks loading. *(doc, high; common-mistakes-fixes)*

## Numbers
- n1: **script_search max results**: 10 fuzzy script name search
- n2: **script_grep max matches**: 50 pattern search across all scripts

## Techniques
- t1: **Connect Claude to Studio MCP**: Enable Studio as MCP server in Assistant > Manage MCP Servers. Turn on Claude Code or Desktop under Quick connect. Otherwise add the Roblox_Studio JSON entry or run the CLI command. Restart the client. Check for the green indicator.

### Code: Windows MCP config for Roblox Studio
```json
{
  "mcpServers": {
    "Roblox_Studio": {
      "command": "cmd.exe",
      "args": [
        "/c",
        "%LOCALAPPDATA%\\Roblox\\mcp.bat"
      ]
    }
  }
}
```

### Code: macOS MCP config for Roblox Studio
```json
{
  "mcpServers": {
    "Roblox_Studio": {
      "command": "/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"
    }
  }
}
```

## Points to
- https://modelcontextprotocol.io/docs/getting-started/intro
