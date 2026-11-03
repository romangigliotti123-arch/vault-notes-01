---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-sdk/overview.md (+ custom-tools.md, subagents.md, secure-deployment.md, quickstart.md; https://github.com/anthropics/claude-agent-sdk-python README)
type: official-doc
author: Anthropic
published: undated (current docs/README read 2026-10-29)
accessed: 2026-10-29
reliability: high (official; README and docs raw)
---
# Claude Agent SDK (TypeScript/Python): what it adds over `claude -p`
## Key claims
- The SDK "runs the Claude Code binary" and exposes the same tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory loading and plugins "programmable in Python and TypeScript". The Python package bundles the CLI (`cli_path` overrides). To drive the loop from another language "run the CLI as a subprocess with the `-p` flag and `--output-format json`" - i.e. what Roman's SSH pattern already does.
- Licensing/auth warning on both overview and quickstart: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods". So SDK programs are API-key/billing oriented; subscription use is the CLI/`-p` path.
- SDK-only capabilities: in-process custom tools (`@tool` / `tool()` + `create_sdk_mcp_server`; handlers return `content`, optional `structuredContent`, `isError:true` to control the error text Claude sees; `readOnlyHint` lets tools run in parallel; TS `permission_policy` for require-approval/block), hook CALLBACK functions (Python/TS functions as hooks, `HookMatcher`), `canUseTool` callback for programmatic approvals, `ClaudeSDKClient` for bidirectional sessions, `max_budget_usd` / `maxBudgetUsd` (enforced: refuses new subagents, stops background subagents, ends with `error_max_budget_usd`), `listSessions/renameSession/tagSession`, `agents` option (programmatic `AgentDefinition` with `description`, `prompt`, `tools`, `disallowedTools`, `model`, `skills`, `memory`, `mcpServers`, `maxTurns`, `effort`, `background`, `permissionMode`; Python SDK lacks `autoCompactWindow` and `omitClaudeMd`).
- SDK subagent guidance: depth, concurrency, spend caps via env (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) and `maxBudgetUsd`. "Claude Opus 5 delegates to subagents more readily than earlier models, so the depth, concurrency, and spend limits matter most"; with the `claude_code` preset on Opus 5 Claude Code adds a system-prompt line not to call Agent unless asked; with a custom prompt that line is absent, so add the delegation instruction yourself; "Either instruction only steers Claude, so set the limits as well."
- System prompt snapshot (Python README): Claude Code builds the system prompt on the first request, records it and reuses it on resume, so a changed custom/append prompt has no effect until compaction or a new session (`snapshot: False` rebuilds it every request; CLI 2.1.257+).
- Secure deployment: "defense in depth", containers/gVisor/VMs, read-only code mounts, and the proxy pattern for credentials ("The agent sends requests without credentials, the proxy adds them ... The agent never sees the actual credentials"; the proxy can allowlist endpoints and log all requests). Bash permission gate "is a permission gate, not a sandbox".
## Quotable
> "Either instruction only steers Claude, so set the limits as well. Claude Code enforces them however Claude decides to delegate."
> "The agent sends requests without credentials, the proxy adds them, and forwards the request to its destination."

## Used by
[[topic-agent-security]], [[topic-claude-code-features]]
