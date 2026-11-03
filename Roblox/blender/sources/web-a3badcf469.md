---
type: research-source
id: web-a3badcf469
title: "Claude Code + Blender MCP"
source_type: "web"
creator: "hydroxide.dev"
url: "https://hydroxide.dev/articles/blender-mcp-claude-code/"
published: "2026-05-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 3
density: medium
tags: ["research-source", "web", "claude-blender-mcp"]
---
# web-a3badcf469

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short install guide for the official Blender Lab MCP add-on (blender-mcp) with Blender 5.1 and Claude Code. Covers installing the add-on via drag-and-drop from blender.org/lab/mcp-server, cloning the blender_mcp repo, and registering it with `claude mcp add` (project or user scope), plus removing a prior version. Nothing on Roblox export or bpy workflows.

## Claims
- c1: Official Blender Lab MCP add-on replaced an unofficial blender-mcp add-on; author says official one is likely better supported going forward (opinion). *(opinion, medium; claude-blender-mcp)*
- c2: Install add-on by dragging the file from blender.org/lab/mcp-server into running Blender twice: first adds Blender Lab repository, second installs the add-on. *(demo, medium; claude-blender-mcp)*
- c3: Server is cloned from projects.blender.org/lab/blender_mcp.git and run via uv with --directory pointing to the mcp subfolder. *(demo, high; claude-blender-mcp)*
- c4: Register with Claude Code using `claude mcp add blender -- uv --directory $HOME/blender_mcp/mcp run blender-mcp` from the project folder; add `--scope user` to make it available in all projects. *(demo, high; claude-blender-mcp)*
- c5: Before re-adding, remove any previous version with `claude mcp remove blender` (or `--scope user`). *(demo, high; claude-blender-mcp)*

## Numbers
- n1: **Blender version**: 5.1 

## Techniques
- t1: **Two-step drag-and-drop add-on install**: Drop add-on file from blender.org/lab/mcp-server into running Blender twice: first registers Blender Lab repo, second installs add-on.
- t2: **Register MCP server with Claude Code**: git clone projects.blender.org/lab/blender_mcp.git, then claude mcp add blender -- uv --directory <path>/mcp run blender-mcp; use --scope user for all projects.

### Code: Clone the official blender_mcp repo
```bash
cd $HOME
git clone https://projects.blender.org/lab/blender_mcp.git
```

### Code: Register the MCP server with Claude Code (project scope)
```bash
claude mcp add blender -- uv --directory $HOME/blender_mcp/mcp run blender-mcp
```

### Code: Register the MCP server for all projects (user scope)
```bash
claude mcp add --scope user blender -- uv --directory $HOME/blender_mcp/mcp run blender-mcp
```

### Code: Remove a previously installed blender MCP entry
```bash
claude mcp remove blender
claude mcp remove --scope user blender
```

## Points to
- https://www.blender.org/lab/mcp-server/
- https://projects.blender.org/lab/blender_mcp.git
