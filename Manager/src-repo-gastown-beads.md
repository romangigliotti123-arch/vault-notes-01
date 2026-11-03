---
tags: [manager-kb, source]
url: https://github.com/gastownhall/gastown
type: repo
author: Steve Yegge (gastownhall org)
published: undated (created 2025-12-16; pushed 2026-10-28; v1.2.1 release 2026-06-06)
accessed: 2026-10-29
reliability: med-high (README read in full; no independent benchmark exists)
---
# Gas Town (18,597 stars, MIT, 513 open issues) and Beads (28,271 stars, MIT, 1,585 open issues)
## Key claims
- "Multi-agent orchestration system for Claude Code, GitHub Copilot, and other AI agents with persistent work tracking". Problem table: agents lose context on restart -> "work persists in git-backed hooks"; manual coordination -> mailboxes, identities, handoffs; "4-10 agents become chaotic" -> "scale comfortably to 20-30 agents"; work state lost in agent memory -> Beads ledger.
- Roles: **Mayor** (the primary AI coordinator: a Claude Code instance you talk to), **Rigs** (project containers wrapping a git repo), **Polecats** (worker agents with persistent identity but ephemeral sessions), **Crew** (human workspace), **Hooks** (git-worktree persistent storage that survives crashes), **Convoys** (work-tracking bundles), **Molecules/Formulas** (TOML workflow templates with checkpoint recovery), **Witness** (per-rig lifecycle watchdog) + **Deacon** (cross-rig patrol supervisor) + **Dogs**, **Refinery** (per-rig Bors-style bisecting merge queue that runs verification gates), **Escalation** (severity-routed via Deacon/Mayor/Overseer), **Scheduler** (`scheduler.max_polecats` caps concurrency to avoid API rate-limit exhaustion), **Seance** (query predecessor sessions via `.events.jsonl`), **Wasteland** (federated work network via DoltHub).
- Requirements: Git 2.20+, Go 1.26+, Beads `bd` 0.57+, Dolt, sqlite3, tmux 3+, Claude Code CLI. "For full tmux-backed workflows on Windows, use WSL or another Linux environment. Native Windows shells are best treated as minimal CLI-only environments." A Docker path exists.
- **Beads** (`bd`): "Distributed graph issue tracker for AI agents, powered by Dolt": dependency-aware task graph (`bd create`, `bd ready`, `bd update --claim`, `bd close`), syncs across machines via `bd dolt push/pull`. Replaces markdown plans with a graph so agents on long-horizon tasks keep context.
## Critical read
- Heavy: Go + Dolt + tmux + many role processes; designed for tens of parallel writers on code repos, which is Cursor/Cognition territory. Our setup has few parallel writers. The reusable ideas are small: persistent work ledger separate from chat context, a watchdog role, a merge-queue with verification gates, severity-routed escalation.
- Cost/rate-limit exposure is explicit in the design (scheduler). Third-party commentary (search snippet only, not verified) says running ~20 concurrent Claude instances can burn hundreds of dollars a weekend; irrelevant to subscription users but relevant to usage limits.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
