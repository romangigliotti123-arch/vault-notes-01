---
tags: [manager-kb, source]
url: https://github.com/Yeachan-Heo/oh-my-claudecode
type: repo
author: Yeachan Heo
published: undated (created 2026-01-09; pushed 2026-10-28; latest release v5.7.19 on 2026-10-27)
accessed: 2026-10-29
reliability: med (README read in part; no independent evaluation found)
---
# oh-my-claudecode (OMC): "Teams-first multi-agent orchestration for Claude Code"
## Key claims
- 40,363 stars, 3,602 forks, MIT, only 10 open issues (small relative to stars). Install: `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` then `/plugin install oh-my-claudecode`, or npm `oh-my-claude-sisyphus`.
- In-session skills: `/autopilot` (single lead agent, end-to-end), `/ralph`, `/execute` (verified single-agent completion), `/deep-interview` (Socratic requirement clarification before code), `/team N:executor "..."` = native Claude Code agent teams pipeline `team-plan -> team-prd -> team-exec -> team-verify -> team-fix (loop)`; terminal `omc team N:codex|gemini|claude "..."` spawns real tmux worker panes. Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` for in-session teams. tmux needed (Windows: psmux).
- Features: smart model routing ("saves 30-50% on tokens" - an unsupported claim), analytics and cost tracking, rate-limit wait/auto-resume (needs tmux), Telegram/Discord stop callbacks, `omc lookout scan` pre-flight danger scan of a task briefing before an unattended run (advisory).
- README says "Use only one primary loop authority in a session": warns against stacking Claude `/goal`, Execute, Team, Verify loops. It also promotes a lighter fork ("gajae-code ... faster, cheaper, simpler") for people who found OMC "a bit overkill".
- Notable: it is largely prompts + skills + hooks layered on Claude Code's own agent teams; the 'swarm' alias was removed in favour of 'team'.
## Critical read
- Zero-learning-curve branding hides a large prompt/skill surface that loads into context; no controlled comparison with vanilla Claude Code; relies on an experimental Claude Code feature (agent teams) whose docs say ~7x tokens and limitations. Worth reading for the staged team pipeline and the pre-flight scan; not worth installing over native subagents.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
