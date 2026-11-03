---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/mcp.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29 raw .md, 155 KB)
accessed: 2026-10-29
reliability: high (official doc)
---
# Claude Code docs: MCP (tool search, output limits, description limits, auth)
## Key claims
- Tool search is ON by default: MCP tools are deferred; only tool NAMES and server instructions load at session start. "Claude Code doesn't impose a fixed per-server tool cap; the practical limit is your context window budget."
- Output limits: warning above 10,000 tokens, default cap 25,000 (`MAX_MCP_OUTPUT_TOKENS`); text results over 50,000 chars are saved to a file unless the tool declares `anthropic/maxResultSizeChars`.
- Description limits: server instructions and upfront tool descriptions 4,096 chars; tools loaded via search 16,384 chars (`CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`). "Keep descriptions and instructions concise, and put critical details near the start"; the search matcher reads only the shorter part, so put the words Claude would search for first.
- Per-tool `anthropic/alwaysLoad` in `_meta`; user config can override.
- `headersHelper` (dynamic auth header from a command) exists for HTTP/WS servers; `claude -p` cannot run an OAuth flow (sign in interactively first).
- "Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection."
- Subagents can scope MCP via `mcpServers:` and `tools:`/`disallowedTools: mcp__server__*`.
## Quotable
> Keep descriptions and instructions concise, and put critical details near the start.

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
