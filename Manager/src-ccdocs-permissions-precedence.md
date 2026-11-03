---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/permissions.md (+ permission-modes.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29 raw .md)
accessed: 2026-10-29
reliability: high (official doc; also verified empirically, see [[src-local-enforcement-test]])
---
# Claude Code docs: permissions precedence, bypassPermissions, hooks vs rules
## Key claims
- "Deny rules block in every mode, including `bypassPermissions`." Allow rules have NO effect in bypassPermissions. Explicit `ask` rules still prompt in every mode ("actions no mode auto-approves").
- bypassPermissions "offers no protection against prompt injection or unintended actions"; "Only use this mode in isolated environments like containers, VMs, or dev containers without internet access." Writes to protected paths (`.git`, `.claude`, `.bashrc`) are auto-approved ONLY in bypass.
- Deny > ask > allow regardless of specificity. A PreToolUse hook that exits 2 "stops the tool call before permission rules are evaluated"; a hook cannot override deny/ask rules.
- Recommended pattern for "everything except a few things": allow `Bash`, add a PreToolUse hook rejecting specific commands.
- Built-in always-on checks even in bypass: critical-path `rm`/`rmdir` prompts (can be disabled in bypass); PowerShell `Remove-Item` on system paths or bare wildcards denied in every mode; `cmd /c rd|del` on system paths denied (v2.1.283+); UNC network paths prompt (credential leak risk).
- Cross-session messaging safeguards still apply in bypass (`isolatePeerMachines`, `crossSessionInbound`).
- `permissions.disableBypassPermissionsMode` / `disableAutoMode` exist for managed settings.
- PowerShell rules: AST-parsed, aliases canonicalized, each subcommand of a compound command checked independently; `Bash(command:...)`-style content matching is ignored.
- Symlinks: both requested path and resolved target are checked.
## Quotable
> bypassPermissions offers no protection against prompt injection or unintended actions.

## Used by
[[topic-agent-security]]
