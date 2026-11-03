---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/headless.md (+ cli-reference.md, env-vars.md, settings-reference.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# Headless `claude -p`, CLI flags and unattended-run settings
## Key claims
- `claude -p` exit 0/non-zero; auth failures print as the result on stdout; SIGTERM exits 143 and leaves the turn unfinished (`CLAUDE_CODE_RESUME_INTERRUPTED_TURN=1` resumes it); send SIGINT first to end the turn cleanly.
- `--bare` skips hooks, skills, plugins, MCP, auto memory, CLAUDE.md, subagents; uses ONLY API-key/provider auth ("never reads OAuth credentials or the system keychain"); "recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release" (so subscription users will have to watch this change). Without `--bare`, `-p` runs project `.claude/settings.json` hooks and `.mcp.json` servers with NO trust dialog.
- Since 2.1.302, `claude -p` starts in Manual mode when nothing sets a permission mode, so unlisted tool calls needing approval are denied. `--allowedTools` pre-approves ("`Bash(git diff *)`" prefix syntax; a bare `Bash` entry is dropped under auto mode); `--permission-mode dontAsk|acceptEdits|auto|bypassPermissions`; `--permission-prompts none` (2.1.259+) denies anything that would prompt and tells Claude not to retry; denials listed in `permission_denials` of the final result message.
- Structured output: `--output-format json` (fields incl. `result`, `session_id`, cost/usage, `is_error`, `subtype`), `--json-schema` -> `structured_output` (check presence), `stream-json --verbose [--include-partial-messages]`. Continue with `--continue` / `--resume <id|name|transcript path>`; session found by id in any project dir on the machine. `--continue` can reopen a finished background session (2.1.257+).
- `claude -p` stays open after the last turn to wait for background subagents/commands/Monitors (10-min idle cap `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`; 0 = no cap); `--max-budget-usd` stops remaining background work; `--max-turns` errors out.
- In `-p`: user-invocable skills work by writing `/skill-name` in the prompt; `/model`, `/effort`, `/fast`, `/rename`, `/output-style <style>` (2.1.269+) accept args; `/config key=value`.
- `--agents <json|file>` (file form 2.1.281+); `--append-system-prompt[-file]`; `--append-subagent-system-prompt[-file]`; `--settings`, `--mcp-config`, `--strict-mcp-config`, `--plugin-dir`; `--restricted` (2.1.248+, no command-running tools or user/project settings).
- Unattended retry: `CLAUDE_CODE_RETRY_WATCHDOG=1` retries 429/529 indefinitely with backoff up to 5 min and waits out a claude.ai usage limit window (fails fast on spend-limit/credit exhaustion); `..._MAX_WAIT_MS` caps each wait (2.1.295+), `..._USAGE_LIMIT_RECHECK_MS` (60000-10800000) re-checks whether a limit lifted early (2.1.305+). Meant for "eval harnesses, CI jobs, or remote workers".
- `askUserQuestionTimeout` ("60s"|"5m"|"10m"|"never", default never): unanswered AskUserQuestion auto-continues after idle time. `autoContinueAtUsageLimit` default true.
- Idle compaction (2.1.299, `idleCompaction:false` to disable, `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`): a 200K+ token conversation idle ~54 min is compacted before its 1-hour cache expires.
## Quotable
> "`--bare` is the recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release."
> "In bare mode, Claude Code never reads OAuth credentials or the system keychain."

## Used by
[[topic-claude-code-features]], [[topic-cross-device-agent-control]], [[topic-remote-mobile-ux]]
