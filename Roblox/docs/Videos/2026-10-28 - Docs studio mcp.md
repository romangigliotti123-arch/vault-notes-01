---
title: "Docs: studio / mcp"
url: https://create.roblox.com/docs/studio/mcp.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / mcp

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/studio/mcp.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page on connecting AI clients to the built-in Studio MCP server. Covers enabling it in Assistant settings, connection methods (quick connect, JSON config, CLI), the tool catalogue (scripts, asset generation, data model, Luau execution, playtesting, input simulation), multi-instance use via studio_id, and troubleshooting.

## Tips
- [page](https://create.roblox.com/docs/studio/mcp) **[[ai-and-tools]]** Only connect MCP clients you trust: they can read and modify content in your open Roblox places.
- [page](https://create.roblox.com/docs/studio/mcp) **[[version-control-and-tooling]]** Use list_roblox_studios to get studio_id and place ID when multiple Studio windows are open; same-named instances are told apart by place ID.
- [page](https://create.roblox.com/docs/studio/mcp) **[[ai-and-tools]]** Verify the connection by checking for the green connected-client indicator under Manage MCP Servers after setup.
- [page](https://create.roblox.com/docs/studio/mcp) **[[testing-debugging-and-qa]]** If tools are missing, restart both Roblox Studio and the MCP client, verify the command/binary path exists, and check JSON syntax for missing commas or brackets.

## Numbers
- [page](https://create.roblox.com/docs/studio/mcp) script_search results cap: **10 results** (Fuzzy name search for scripts in the Studio MCP server)
- [page](https://create.roblox.com/docs/studio/mcp) script_grep results cap: **50 matches** (String pattern search across all game scripts)
- [page](https://create.roblox.com/docs/studio/mcp) Quick connect supported clients: **7** (Antigravity, Codex CLI, Claude Code, Claude Desktop, Cursor, Gemini CLI, VS Code)

## Tools
Roblox Studio MCP server, Assistant, execute_luau, script_read

## Topics
[[ai-and-tools]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
