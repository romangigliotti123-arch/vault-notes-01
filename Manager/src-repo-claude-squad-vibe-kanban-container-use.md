---
tags: [manager-kb, source]
url: https://github.com/smtg-ai/claude-squad
type: repo
author: smtg-ai; BloopAI; Dagger
published: undated (READMEs + gh api metadata read 2026-10-29)
accessed: 2026-10-29
reliability: high (metadata), med (README claims)
---
# Parallel-worktree session managers (human-in-the-loop dashboards, not autonomous orchestrators)
- **claude-squad** (smtg-ai/claude-squad): 8,691 stars, AGPL-3.0, created 2025-03-09, last push 2026-08-20. "Terminal app that manages multiple Claude Code, Codex, Gemini (and other) agents in separate workspaces." Each task gets its own isolated git workspace (worktree) in tmux; review before applying; `-y` autoyes flag is "[experimental]". Needs tmux + gh. AGPL licence is a blocker for embedding/redistribution.
- **Vibe Kanban** (BloopAI/vibe-kanban): 28,490 stars, Apache-2.0, created 2025-06-14. README banner now: "**Vibe Kanban is sunsetting.**" Company announcement (2026-04-10): bloop is shutting down, "couldn't find a business model", project continues "open source and community maintained"; remote services (kanban issues, comments, projects) removed after 30 days, local workspaces keep working. Features: kanban planning, workspaces with branch + terminal + dev server, diff review with inline comments sent to the agent, 10+ agents, PR creation. Rust + Node app (`npx vibe-kanban`).
- **container-use** (dagger/container-use): 4,079 stars, Apache-2.0, created 2025-05-23, last push 2026-09-21, "early development". MCP server giving each agent a fresh container on its own git branch; "See complete command history and logs of what agents actually did, not just what they claim"; drop into any agent's terminal. Needs Docker/Dagger.
- **Conductor** (conductor.build, Melty Labs): closed-source macOS/iOS app (+ API, + "Conductor Cloud" Firecracker microVM sandboxes); each workspace is a git worktree; runs first-party Claude Code, Codex, Cursor, OpenCode agents with your own subscriptions. Opened homepage only; not available for Windows/Linux, cannot run on this host.
- Common idea: isolate every writer in its own worktree/branch/container, review diffs before merge - this is what makes parallel writers safe, regardless of tool.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
