---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/permission-modes.md (+ auto-mode-config.md, permissions.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# Permission modes, auto mode and auto-mode configuration
## Key claims
- Modes: default(Manual), acceptEdits, plan, auto, dontAsk, bypassPermissions. "Deny rules block in every mode, including `bypassPermissions`. ... Allow rules have no effect in `bypassPermissions`." Explicit `permissions.ask` rules still prompt even in bypass ("Actions no mode auto-approves": tools matched by an explicit ask rule, AskUserQuestion, recognized `rm`/`rmdir` critical-path removals, cross-session messaging safeguards, PowerShell Remove-Item denies).
- bypassPermissions "offers no protection against prompt injection or unintended actions"; docs table: "Isolated containers and VMs only". Alternative for fewer prompts: auto mode. Refuses to start as root on Linux/macOS.
- Auto mode: separate classifier model reviews each action; built-in start mode for interactive sessions since v2.1.283 on all plans; supports Opus 4.6+/Sonnet 4.6+/Haiku 5.5/Fable. Fixed decision order: allow/ask/deny rules first; read-only + working-dir edits auto-approved; everything else to classifier. Classifier sees user messages, tool calls and CLAUDE.md content; tool RESULTS are stripped (injection resistance). Broad allow rules (`Bash(*)`, `Agent`, interpreters) are dropped on entering auto mode.
- Default classifier blocks include: curl|bash, sending sensitive data externally, production deploys/migrations, force push, irreversible destruction of pre-existing files, `git reset --hard`/`clean -fd`, merging an unapproved PR, disabling CI, granting IAM/repo permissions, DNS/TLS changes, printing live credentials, posting content containing sensitive details to shared/public systems, Claude-in-Chrome actions sending page content off-origin, launching autonomous agent loops with `--dangerously-skip-permissions`.
- Boundaries stated in conversation ("don't push") are block signals but "can be lost if context compaction removes the message that stated it. For a hard guarantee, add a deny rule." Approvals must name the action and the specific danger; cover one action.
- Fallback: 3 blocks in a row or 20 total pauses auto mode and prompts again (not configurable); in `-p` without prompt tool the action is just denied and Claude continues.
- Auto mode and subagents: task description evaluated at spawn; each subagent action goes through same order (subagent `permissionMode` ignored); at finish the classifier reviews the subagent's work and final report before parent reads it (warning prepended if flagged). SendMessage content is also classifier-reviewed (2.1.222+).
- `autoMode` settings (read only from `~/.claude/settings.json`, managed, `--settings`; NOT project settings): `environment`, `allow`, `soft_deny`, `hard_deny` = arrays of PROSE rules; include literal `"$defaults"` or you REPLACE the built-in list. `claude auto-mode defaults` prints built-ins. `autoMode.classifyAllShell:true` routes every shell command through classifier. Precedence: hard_deny > soft_deny > allow > explicit user intent. `permissions.ask` with content-scoped rules (`Bash(git push *)`, `Bash(gh pr create *)`) is "the most direct mechanism" for a human checkpoint; `git -C dir push` evades the pattern, so use a PreToolUse hook for full-text inspection.
- Critical-path `rm` prompts have a 2-minute countdown in bypass/auto terminal sessions; away from a terminal (VS Code, desktop, `-p`) bypass DENIES unless a `PermissionRequest` hook allows; `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` changes this. (Remote Control behaviour for these prompts not stated in the page.)
- PreToolUse hook decisions never override deny/ask rules; a hook exit 2 stops the call before permission rules are evaluated, "so the block applies even when an allow rule would otherwise let the call proceed" (permissions.md "Precedence among rules, hooks, and mods").
- Cost: with server-side classifier review (direct Anthropic API connection; interactive sessions on Pro/Max/Team need Claude Code 2.1.271+, `-p`/SDK 2.1.281+) the checks happen inside the session's own model requests at no charge; `/status` row `Auto mode server: Enabled` confirms. If the server does not review (gateway/proxy in path), Claude Code's own classifier requests (default model Sonnet 5; `CLAUDE_CODE_AUTO_MODE_MODEL`, 2.1.302+) count as token usage on API/Enterprise accounts; "Pro, Max, and Team plans never show the notice" (auto-mode-classifier-billing.md). `CLAUDE_CODE_AUTO_MODE_SERVER=0` forces client-side requests.
## Quotable
> "Deny rules block in every mode, including `bypassPermissions`. ... Allow rules have no effect in `bypassPermissions`."
> "Boundaries are not stored as rules. The classifier re-reads them from the transcript on each check, so a boundary can be lost if context compaction removes the message that stated it."
> "Setting any of `environment`, `allow`, `soft_deny`, or `hard_deny` without `\"$defaults\"` replaces the entire default list for that section."

## Used by
[[topic-agent-security]], [[topic-claude-code-features]]
