---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/tools-reference.md (+ commands.md, sandboxing.md, whats-new/index.md, changelog.md 2.1.270-2.1.312)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs; changelog head 2.1.312 = 2026-10-27)
accessed: 2026-10-29
reliability: high (official raw markdown; changelog grep of "Added" bullets)
---
# Tools reference, slash commands, sandbox platform support, recent changelog features
## Key claims
- Tools useful to a phone-driven manager: `PushNotification` (desktop notification AND phone push when Remote Control is connected, for long tasks / scheduled tasks), `SendUserFile` (sends files from the session to the device; `display: render|attach`), `SendMessage`/`ListAgents` (resume subagents; message other sessions), `Monitor` (background script whose output lines are fed back to Claude; watch deadline 5 min default, max 30; on Windows needs Git Bash), `TaskStop`, `ScheduleWakeup`, `CronCreate/List/Delete`, `Workflow`, `RemoteTrigger` (cloud scheduled tasks), `SubagentHandback` (subagent delivers its final report through a tool; "Provided only in auto mode", classifier reviews the report before delivery; 2.1.271+).
- Slash commands relevant to introspection and maintenance: `/context` (grid + suggestions for context-heavy tools and memory bloat), `/usage` (= `/cost`, `/stats`; per skill/subagent/plugin/MCP breakdown on subscription plans), `/doctor` and `/doctor prompt-audit`, `/insights` (HTML report analysing recent sessions: projects, how you use Claude Code, where things go wrong, features to try), `/skill-doctor`, `/recap`, `/tasks`, `/hooks`, `/permissions` (incl. recent auto-mode denials, press r to retry), `/auto-mode-setup`, `/fewer-permission-prompts`, `/autocompact`, `/background`, `/fork`, `/subtask`, `/btw`, `/batch`, `/import [codex|gemini|cursor]`, `/team-onboarding`, `/reload-skills`, `/reload-plugins`, `/powerup`.
- Sandbox: "The sandbox runs on macOS, Linux, and WSL2. On native Windows, Claude Code runs commands unsandboxed." So the Windows host has no sandbox; the CachyOS box (Linux) can use it. Sandbox covers Bash/PowerShell/Monitor commands only, not file tools, MCP or hooks.
- whats-new index: weekly digests stop at week 37 (Sept 7-11, 2026); newer features are only in the changelog. Notable recent items: `claude plugin eval` (w37, 2.1.269); `maxEffortLevel` setting (w37); `--restricted` (w35); `/skill-doctor` (w36); fork mode default (w33); auto mode default permission mode on Pro/Max/Team from Aug 14 (w32); cross-session messaging (w32); subagents run in the background by default (w27, June 29-July 3, 2026).
- Changelog 2.1.270-2.1.312 "Added" highlights (all dates before 2026-10-28): idle compaction (2.1.299); `autoCompactWindow` in subagent frontmatter (2.1.296); `omitClaudeMd` (2.1.271); `onFailure:"block"` for hooks (2.1.295); Agent tool `effort` parameter (2.1.292); `CLAUDE_CODE_RETRY_WATCHDOG` family (2.1.295/301/305); `/doctor prompt-audit` (2.1.283); `/auto-mode-setup` (2.1.304); `CLAUDE_CODE_AUTO_MODE_MODEL` (2.1.302); `claude attach|logs <name>` partial-name match (2.1.290); AGENTS.md support (2.1.277); "Claude Mods" (2.1.287, plugin hooks modules, `tool.check` can approve/refuse tool calls); built-in mod "You should know" side-agent (2.1.287); `syncClaudeAiPlugins`/`syncClaudeAiSkills` opt-out (2.1.275); fork of a Remote Control session from the app runs as a background session (2.1.273); `claude_code.safety_event` OTel event added (2.1.307) then removed (2.1.312); ultrathink raises a turn to xhigh on 5.5 models (2.1.311); prompt/agent hooks max 24 concurrent (2.1.312).
## Quotable
> "On native Windows, Claude Code runs commands unsandboxed."
> "Provided only in auto mode, to subagents that the Agent tool runs locally other than forks" (SubagentHandback tool entry)

## Used by
[[topic-claude-code-features]]
