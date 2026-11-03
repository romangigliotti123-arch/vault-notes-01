---
tags: [manager-kb, source]
url: https://github.com/automazeio/ccpm
type: repo
author: automazeio; AndyMik90; nwiizo; BeehiveInnovations; mikeyobrien
published: undated (READMEs + gh api metadata read 2026-10-29)
accessed: 2026-10-29
reliability: med (READMEs; claims unverified)
---
# Five more Claude-Code-adjacent orchestrators (one note)
- **CCPM** (automazeio/ccpm): 8,423 stars, MIT, created 2025-08-18, pushed 2026-10-19, 6 open issues. Now an Agent Skill (works with any Agent-Skills harness). Spec-driven flow PRD -> epic -> tasks -> GitHub issues -> parallel execution with worktrees; "No vibe coding"; GitHub issues as the shared source of truth. README claims "89% less time lost to context switching", "75% reduction in bug rates", "up to 3x faster" and a skill benchmark "100% vs 27.7%" - the benchmark is 11 scenario checks (4/4, 4/4, 3/3 vs 2/4, 0/4, 1/3) of whether the agent followed CCPM's own procedure, not a code-quality outcome; the first claims are unsourced "teams report". Idea worth stealing: PRD-first decomposition into parallelizable task files with explicit dependencies, plus a standup report generated from files.
- **Auto-Claude -> Aperant** (AndyMik90/Aperant): 14,588 stars, AGPL-3.0, created 2025-12-04, last push 2026-06-14. README: "Autonomous multi-agent coding framework that plans, builds, and validates software"; 2.x desktop app (Electron; Windows/macOS/Linux installers) is in maintenance mode, "Aperant 3.0" being rebuilt privately, PRs paused. Stale and AGPL.
- **ccswarm** (nwiizo/ccswarm): 154 stars, MIT, Rust, pushed 2026-10-13. Honest README: "Sangha" workflow engine (plan -> quorum of reviewers -> implement -> review -> fix); "Evidence-bound acceptance, objection resolution, and checkpoint recovery are the next design, not shipped guarantees"; "undo currently reports commits rather than rolling them back". Tiny adoption; interesting only for the quorum-of-reviewers idea.
- **PAL MCP server** (BeehiveInnovations/pal-mcp-server, was zen-mcp-server): 11,810 stars, licence NOASSERTION (custom file), created 2025-06-08, last push **2025-12-15** (10+ months stale), 152 open issues. MCP server letting Claude Code call other models/CLIs ("clink" CLI-to-CLI bridge: spawn Gemini/Codex/Claude subagents with roles like planner, codereviewer; "consensus" tool polls multiple models). Idea: cross-model review for diversity. Risk: stale, sends code to third-party model APIs.
- **Ralph Orchestrator** (mikeyobrien/ralph-orchestrator): 3,190 stars, MIT, Rust, created 2025-09-07, pushed 2026-10-15. "Hat-based orchestration framework that keeps AI agents in a loop until the task is done": personas ("hats") coordinating via events, "Backpressure - gates that reject incomplete work (tests, lint, typecheck)", persistent memories and tasks, Telegram bot (`/status`, `/tasks`, `/restart`). Ralph loop family: see [[src-ghuntley-ralph]], [[src-claude-plugins-ralph-loop]], Anthropic's C-compiler harness [[src-anthropic-building-c-compiler]].

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
