---
tags: [manager-kb, source]
url: https://github.com/hesreallyhim/awesome-claude-code
type: repo
author: hesreallyhim
published: undated (README read 2026-10-29, 243 KB; linked projects themselves NOT opened - descriptions only)
accessed: 2026-10-29
reliability: med (curated index; third-party tools unvetted, descriptions are the list author's)
---
# awesome-claude-code (curated index): categories and tools relevant to an always-on manager
## Key claims
- Categories present: Remote Control/Notifications/Voice I/O, Status Lines, Mods, Agent Orchestration (Ralph Wiggum, Dynamic Workflows, SDLC), Skills, Memory, Observability (Session Monitors, Usage & Cost), Security, Configuration. Start Here items include Anthropic's "A Field Guide to Claude Fable 5" (Thariq Shihipar) and HumanLayer's "Writing a Good CLAUDE.md".
- Security/guard hooks (descriptions only): Claude Code Safety Net ("hook that acts as a safety net, catching destructive git and filesystem commands before they execute"), Dippy (auto-approve safe bash via AST parsing, prompt for destructive ones - "solves permission fatigue without disabling safety"), Gryph (YAML policy rules that block/warn/guide in real time + local SQLite audit log of every event), GouvernAI ("auto-approve what's safe, gate what's risky, block what's dangerous. Dual enforcement, full audit trail"), Agent Guard (secret-leak guardrails), authsome (credential gateway: agents never see credentials), sandboxes for bypass mode (aicontainer, Cleat, Container Use, Code on Incus, Brood Box microVMs).
- Cost/waste tools: ccusage (reads local JSONL logs: daily/monthly/per-session/5-hour-block), Codeburn ("identifies token waste, including unused MCP servers, verbose CLAUDE.md, repeated file reads"), context-tax (prices what is sent every turn before the first prompt: system prompt, MCP tool names, skill listing, instruction files), cc-probeline (prices every turn incl. subagents and cache rebuilds), ccxray (transparent HTTP proxy dashboard of every request).
- Session monitors: cctop (TUI of all sessions with sub-agent tree and orphaned ports), Claude Code Agent Monitor (self-hosted dashboard fed by native hooks: subagent orchestration trees, tool-call timelines).
- Remote/phone: Claude CLI <-> Telegram bot, WhatsApp channel plugin (remote tool approval, voice transcription), anotifier (free phone push via ntfy when Claude finishes or needs input), Airut (run Claude Code tasks from email/Slack with container isolation).
- Configuration: "Fixing Opus 5" (disler): single appendable system prompt (`--append-system-prompt-file`) that cuts verbal tics/heading theater/output-token bloat - evidence that output verbosity is commonly tuned via system-prompt append rather than CLAUDE.md.
## Quotable
> "Auto-approve safe bash commands using AST-based parsing, while prompting for destructive operations." (Dippy entry)

## Used by
[[topic-claude-code-features]]
