---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/managed-settings.md (+ settings.md, env-vars.md, data-usage.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Claude Code docs: managed settings, env scrub, local data
## Key claims
- Windows managed policy locations: file `C:\Program Files\ClaudeCode\managed-settings.json` (+ `managed-settings.d\`, `managed-mcp.json`) or `HKLM\SOFTWARE\Policies\ClaudeCode` value `Settings`; HKCU registry is user-writable and used only when no admin document exists. Managed settings beat every other level incl. CLI args. The files are only as tamper-proof as the account that can write them: an elevated-admin session can write both.
- `ConfigChange` hook can block a settings/skills change from taking effect (exit 2) except `policy_settings`.
- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips credentials (by variable name or value shape) from Bash/hook/stdio-MCP subprocess environments; "leaves GitHub tokens and proxy settings in place"; to be used "as one layer alongside narrow permission rules".
- `CLAUDE_CODE_SCRIPT_CAPS` limits how many times named scripts may run per session (substring match; defence in depth).
- Session transcripts are stored locally in plaintext under `~/.claude/projects/` for 30 days (`cleanupPeriodDays`); anything printed by a tool (including secrets) lands there. `/feedback` transcripts are kept 5 years; the optional "share transcript" upload redacts only known key patterns.
- Subagent frontmatter `tools` allowlist / `disallowedTools` denylist are the enforcement for per-worker tool access; `permissionMode` is ignored if the parent is bypassing (see [[src-ccdocs-permissions-precedence]]). Plugin subagents cannot use `hooks`, `mcpServers`, `permissionMode`.
## Quotable
> use it as one layer alongside narrow permission rules rather than as the only control

## Used by
[[topic-agent-security]]
