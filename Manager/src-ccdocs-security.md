---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/security.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Claude Code docs: Security
## Key claims
- Permission architecture: Auto mode (separate classifier) and Manual mode; deny rules and explicit asks still apply.
- "The boundary is a permission prompt, so a Bash command you approve can still write anywhere your user account can" (working-directory boundary is not an OS boundary).
- Prompt-injection safeguards listed: permission system, curl/wget not auto-approved, WebFetch runs a separate model call over the page (Claude receives that answer, not the raw page), trust dialog, command-injection detection, fail-closed matching, credential storage (Windows: a file inheriting profile ACLs).
- Best practices for untrusted content: review commands, avoid piping untrusted content to Claude, use VMs for scripts/tool calls "especially when interacting with external web services".
- MCP: use servers you wrote or trust; Anthropic does not security-audit MCP servers; project `.mcp.json` has its own approval but user-scope servers, claude.ai connectors and plugins are outside the repo so reviewing `.mcp.json` does not show every server.
- Remote Control: execution stays local; "No cloud VMs or sandboxing are involved"; multiple short-lived narrowly scoped credentials.
- For additional isolation run the whole process in the sandbox runtime or a dev container; audit/block settings changes with `ConfigChange` hooks; Windows WebDAV/UNC warning (network requests bypassing the permission system).
- "no system is completely immune to all attacks".
## Quotable
> The boundary is a permission prompt, so a Bash command you approve can still write anywhere your user account can

## Used by
[[topic-agent-security]]
