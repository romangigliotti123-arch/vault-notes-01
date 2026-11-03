---
type: research-source
id: gh-sandraschi-blender-mcp-f-CLAUDE.md
title: "sandraschi/blender-mcp/CLAUDE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/CLAUDE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-sandraschi-blender-mcp-f-CLAUDE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Developer instruction file (CLAUDE.md) for sandraschi/blender-mcp, an MCP server that lets Claude control Blender via natural language. Lists uv-based dev, test, lint, format and mypy commands, the src layout (FastMCP server, handlers, utils, optional webapp), and code standards: Portmanteau handler pattern, async tools, docstrings, full type hints. Says nothing about Roblox, bpy specifics or export settings.

## Claims
- c1: blender-mcp is built on FastMCP; core server defined in src/blender_mcp/server.py with handlers in src/blender_mcp/handlers/ (scene, object, render, etc.). *(doc, high; claude-blender-ai)*
- c2: Project is run and tested with uv: dev server via 'uv run python run_server.py', tests via 'uv run pytest'. *(doc, high; claude-blender-ai)*
- c3: Tool handlers must follow the 'Portmanteau Pattern'; all tools must be async with comprehensive docstrings and mandatory type hints. *(doc, high; claude-blender-ai)*
- c4: Quality tooling: ruff for lint and format ('uv run ruff check .', 'uv run ruff format .'), mypy type check on src ('uv run mypy src'). *(doc, high; automation-and-creator-workflows)*
- c5: Optional webapp/ dashboard exists for fleet visibility, if present in the repo. *(doc, medium; claude-blender-ai)*
- c6: Tool registration rules are defined in an external central docs file (mcp_registration.md), referenced by a local Windows path; the file itself is not included. *(doc, high; other)*

## Techniques
- t1: **Portmanteau handler pattern**: Group related tools into context-specific handler modules (scene, object, render) under src/blender_mcp/handlers/; per the file, tool handlers follow this pattern. Specifics not described in the source.

### Code: Dev commands for blender-mcp (from CLAUDE.md)
```bash
uv run python run_server.py
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy src
```

## Quotes (brief, for attribution)
> Follow the Portmanteau Pattern for tool handlers. All tools must be async with comprehensive docstrings. Mandatory type hints for all function signatures.  (sandraschi)

## Points to
- https://github.com/sandraschi/blender-mcp
