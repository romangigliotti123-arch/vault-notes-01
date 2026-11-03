---
type: research-source
id: gh-ahujasid-ableton-mcp-readme
title: "ahujasid/ableton-mcp README: Control Ableton Live with any LLM: create tracks, arrange clips & compose music via MCP"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp"
published: "2026-09-22"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0389
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-ahujasid-ableton-mcp-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for ableton-mcp, an MCP server and Remote Script that lets Claude drive Ableton Live. It is off-topic for Blender/Roblox. It is only useful as an architecture analogue for blender-mcp: a socket server inside the host app, a separate MCP server, a JSON/TCP protocol, a version handshake, telemetry opt-outs, and setup via uvx.

## Claims
- c1: Architecture is two parts: an in-app addon/script running a socket server, plus a Python MCP server that talks to it. This is the same pattern blender-mcp is generally understood to use; this source does not mention Blender. *(doc, medium; claude-blender-mcp)*
- c2: Wire protocol is JSON over TCP sockets. Commands carry a `type` and optional `params`. Responses carry a `status` and either `result` or `message`. *(doc, high; claude-blender-mcp)*
- c3: Setup uses uvx for the MCP server (`uvx ableton-mcp`). Claude Desktop uses the mcpServers config, and Claude Code uses `claude mcp add AbletonMCP uvx ableton-mcp`. Only one client instance should run at a time (Cursor or Claude Desktop, not both). *(doc, high; claude-blender-mcp)*
- c4: A version handshake (`get_remote_script_info`) between server and in-app script warns on mismatch, and newer tools degrade gracefully until the host app is restarted. The server does not auto-install the script; installation is an explicit command. *(doc, high; claude-blender-mcp)*
- c5: Troubleshooting advice: timeouts mean you should break requests into smaller steps. Connection errors mean you should restart both Claude and the host app. Complex tasks need to be split up. *(doc, medium; claude-blender-mcp)*
- c6: Anonymous telemetry is on by default (install ID, session ID, tools run, success, duration). Opt-out uses env vars such as ABLETON_MCP_DISABLE_TELEMETRY=true, set in the Claude Desktop config `env` block. Dataset recording of prompts and content is opt-in. This is a privacy consideration for any MCP server. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **Minimum Ableton Live version**: 10 (Remote Script User Library scanning from 10.1.13+) Prerequisite; Python 3.8+ also required

## Techniques
- t1: **uvx-based MCP server config**: Add an mcpServers entry with command `uvx` and args [package-name] in claude_desktop_config.json. Alternatively run `claude mcp add <name> uvx <package>` in Claude Code. A similar config would apply to blender-mcp.

### Code: Claude Desktop MCP config pattern with telemetry disabled
```json
{
    "mcpServers": {
        "AbletonMCP": {
            "command": "uvx",
            "args": ["ableton-mcp"],
            "env": {
                "ABLETON_MCP_DISABLE_TELEMETRY": "true"
            }
        }
    }
}
```

## Points to
- https://github.com/ahujasid/ableton-mcp
- https://docs.astral.sh/uv/getting-started/installation/
- https://youtu.be/iJWJqyVuPS8
