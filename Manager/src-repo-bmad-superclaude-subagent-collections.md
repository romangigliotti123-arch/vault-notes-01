---
tags: [manager-kb, source]
url: https://github.com/bmad-code-org/BMAD-METHOD
type: repo
author: bmad-code-org; SuperClaude-Org; VoltAgent; wshobson; eyaltoledano; ParadevAI
published: undated (READMEs/metadata read 2026-10-29)
accessed: 2026-10-29
reliability: med (metadata solid; README claims not tested)
---
# Role-play method kits and subagent collections (the most-starred "orchestration" repos are mostly prompts)
- **BMAD-METHOD**: 54,687 stars, licence NOASSERTION, created 2025-04-13, pushed 2026-10-27, 92 open issues. "Agile AI Driven Development": analyst / PM / architect / developer / QA style personas and staged documents (briefs, specs, architecture). Stable v6.12 via `npx bmad-method install`; V7 preview is being rebuilt as skills ("an AI coding tool that supports skills"), also a Claude Code plugin marketplace. Role-per-phase decomposition = the "problem-centric" split Anthropic warns about, mitigated by writing explicit artifacts between phases.
- **SuperClaude Framework**: 23,917 stars, MIT, pushed 2026-09-27: slash commands, personas and MCP config bundle for Claude Code; prompt engineering, not orchestration.
- **VoltAgent/awesome-claude-code-subagents**: 26,148 stars, MIT: 100+ subagent definition files (a catalogue). **wshobson/agents**: 41,934 stars, MIT: 94 plugins, 202 agents, 185 skills, 105 commands across Claude Code, Codex, Cursor, etc. (see [[src-gh-wshobson-agents]]). Catalogues, useful as prompt sources; loading many descriptions burns context (15k-token subagent description warning in manager-setup.md).
- **claude-task-master**: 28,277 stars, licence NOASSERTION, last push 2026-04-28: task decomposition/management MCP for AI IDEs.
- **Paradev (formerly Superset)**: 15,682 stars, NOASSERTION, pushed 2026-10-28: "agentic IDE to orchestrate 100+ coding agents" (worktree dashboard family, with claude-squad / Conductor / Emdash (6,104 stars, Apache-2.0) / coder/xum).
- Pattern across the field: star counts are dominated by prompt/config packs and dashboards; very few repos publish task-success measurements versus plain Claude Code.

## Used by
[[topic-multi-agent-frameworks]]
