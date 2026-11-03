---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/github/github-mcp-server/main/docs/server-configuration.md
type: repo
author: GitHub
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official server docs)
---
# GitHub MCP server: toolsets, read-only, lockdown mode
## Key claims
- Toolsets (default: context, issues, pull_requests, repos, users) via `X-MCP-Toolsets` header or `/x/{toolset}` path; individual `X-MCP-Tools`; excluded tools win.
- Read-only mode (`X-MCP-Readonly` header or `/readonly` path) "overrides other settings" and removes every non-read-only tool; stronger control against unwanted changes.
- Lockdown mode (`X-MCP-Lockdown: true`, or `--lockdown-mode`): "only surfaces content in public repositories from users with push access" to reduce injection from untrusted issue authors. Docs call it a "best-effort filter, not a security boundary": it does not limit what the credential can read/write, and withheld content may be reachable via other tools or direct API calls with the same credential.
- Direct counter-measure to the attack in [[src-invariant-github-mcp]].

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
