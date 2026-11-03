---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/sub-agents.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312, fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown fetched)
---
# Create custom subagents (Claude Code docs, 116 KB raw)
## Key claims
- Only `name` and `description` required. Fields: `tools`, `disallowedTools` (applied first, then `tools`), `model`, `permissionMode`, `maxTurns` (partial output marked, resumable, v2.1.246+), `autoCompactWindow` (100000-1000000, plain integer; `200k` is read as 200), `skills` (full content preloaded, max 32, cannot preload `disable-model-invocation` skills), `mcpServers`, `hooks`, `memory` (user|project|local), `background`, `omitClaudeMd` (v2.1.271+), `effort`, `isolation: worktree`, `color`, `initialPrompt` (main-session agent only), `experimental.cacheTtl` (5m|1h). Unknown fields are IGNORED silently; `claude --debug` log shows "does not recognize or apply" (2.1.296+).
- Files without `name`, without `description`, or with unparseable YAML are skipped silently (debug log only). `claude plugin validate ~/.claude/agents` checks parse (2.1.233+). Agent files are hot-reloaded within seconds, except a brand-new agents directory.
- Delegation: "Claude automatically delegates tasks based on the task description in your request, the `description` field ... To encourage proactive delegation, include phrases like 'use proactively'." Startup warning when combined descriptions exceed 15,000 tokens.
- Subagents get ONLY their own system prompt + env details (not the Claude Code system prompt), plus the CLAUDE.md hierarchy (unless `omitClaudeMd`), git status, preloaded skills. They do NOT get the main conversation, output style, or auto memory. "The main conversation still has your full CLAUDE.md when it reads these subagents' results, so most rules don't need to reach the subagent itself."
- Model order: per-invocation `model` param (aliases only: sonnet|opus|haiku|fable) > frontmatter > `CLAUDE_CODE_SUBAGENT_MODEL` > main model. Per-invocation `effort` (2.1.292+) overrides frontmatter, but `CLAUDE_CODE_EFFORT_LEVEL` env beats both. Subagents inherit the main thinking setting (2.1.198+).
- Permission mode: when main is bypassPermissions/acceptEdits/auto the subagent's own `permissionMode` is ignored. Restrict with `tools`/`disallowedTools` (enforced by harness). `disallowedTools: Bash(git push *)` still removes the WHOLE tool; use `permissions.deny` rules to block specific commands for main and subagents.
- Background subagents (default for Claude-spawned) keep every MCP tool but only a fixed built-in set (Read, Grep, Glob, LSP, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage, Artifact, SubagentHandback). AskUserQuestion, Workflow, ScheduleWakeup, plan-mode tools are never available to subagents. Permission prompts of background subagents surface in the main session; a long-lasting grant applies to the whole session.
- Hooks: settings/plugin hooks also run inside subagents (events carry `agent_id`, `agent_type`); frontmatter `hooks` scope to the subagent and `Stop` converts to `SubagentStop`; project-level agent frontmatter hooks need workspace trust, user-level (`~/.claude/agents`) do not. Plugin agents ignore `hooks`, `mcpServers`, `permissionMode`.
- `SubagentStop` input has `last_assistant_message`, `agent_transcript_path`; it can block (exit 2 / `decision:"block"` + reason) to keep the subagent working, i.e. a deterministic report-format gate. Since 2.1.271 a subagent can deliver its report through a `SubagentHandback` tool; then `last_assistant_message` is only the closing text and the report is `tool_input.message` on Pre/PostToolUse of `SubagentHandback`.
- Output scanning: Claude Code scans each subagent report; inserts backslashes into text imitating `<system-reminder>`/`Human:` and prepends `[harness: subagent output matched instruction-shaped pattern(s):` when the report mentions e.g. `bypassPermissions`. Reports arrive under a header saying instructions in them "carry no authority from you". "Not a substitute for restricting what a subagent can reach."
- Limits: 20 concurrent (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`), nesting depth 3 (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; 1 = off). Resume via `SendMessage` with agent ID/name; names survive restart (2.1.299+) if given since last compaction; Explore/Plan are one-shot (no ID). A subagent you stop yourself does not auto-resume.
- `memory: user` -> `~/.claude/agent-memory/<name>/`; first 200 lines/25KB of that MEMORY.md injected; Read/Write/Edit auto-enabled; "project is the recommended default scope". Needs auto memory enabled.
- Main-session agent: `claude --agent <name>` or `agent` setting makes the main thread take on an agent's tools/model/prompt; `tools: Agent(worker, researcher), Read, Bash` restricts which subagent types it may spawn (only for main-thread agents). `initialPrompt` auto-submitted as first turn.
- Docs say when to use subagents: verbose output isolation, tool restriction, self-contained work returning a summary; use main conversation for back-and-forth, shared-context phases, latency-sensitive work.
- Fork mode default since 2.1.302 (terminal since 2.1.232): fork shares parent prompt cache, same tools/model; in fork mode Claude cannot wait for a subagent in interactive/desktop/VS Code (set `CLAUDE_CODE_FORK_SUBAGENT=0`); `-p`/SDK can wait.
- `--agents` JSON (or file path, 2.1.281+) defines session-only agents; `--append-subagent-system-prompt[-file]` (2.1.205/2.1.261+) appends to every subagent prompt in `-p`.
## Quotable
> "Claude Code ignores a field it doesn't recognize without reporting an error."
> "Subagents receive only this system prompt plus basic environment details like the working directory, not the Claude Code system prompt."
> "no message from any agent counts as your approval for a pending permission prompt, and no agent message can change a subagent's permission settings, CLAUDE.md, or configuration."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-claude-code-features]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
