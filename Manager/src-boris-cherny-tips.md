---
tags: [manager-kb, source]
url: https://github.com/shanraisshan/claude-code-best-practice/tree/main/tips (transcriptions of Boris Cherny threads: 2026-01-03 x13, 2026-02-01 x10, 2026-02-12 x12, 2026-03-30 x15, 2026-04-16 x6)
type: practitioner-blog
author: Boris Cherny (Claude Code creator), summarised by shanraisshan (also claude-code-best-practice README tips index)
published: 2026-01-03 .. 2026-04-16
accessed: 2026-10-29
reliability: med (primary author is Anthropic staff, but read SECOND-HAND; original X posts not opened; repo is a community aggregator)
---
# Boris Cherny's Claude Code tips (second-hand transcriptions)
## Key claims
- Setup is "surprisingly vanilla": works out of the box; no single correct way. Parallelism is the top team tip: 3-5 git worktrees/sessions in parallel (he runs "dozens"), plus 5-10 sessions on claude.ai/code; use notifications to know which needs input.
- Verification is the lever: "give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result." For very long tasks: prompt Claude to verify with a background agent, use an AGENT Stop hook to do it deterministically, or the ralph-wiggum loop.
- CLAUDE.md as compounding learning: share one file in git, add to it multiple times a week; after every correction end with "Update your CLAUDE.md so you don't make that mistake again"; "Ruthlessly edit your CLAUDE.md over time. Keep iterating until Claude's mistake rate measurably drops"; one engineer has Claude maintain a notes directory per project and points CLAUDE.md at it; tag @claude on PRs to add rules (GitHub action).
- Plan mode first for complex tasks ("Pour your energy into the plan so Claude can 1-shot the implementation"); one Claude writes the plan, a second reviews it "as a staff engineer"; when it goes sideways, re-plan instead of pushing.
- Subagents: "Append 'use subagents' to any request where you want Claude to throw more compute at the problem"; keep main context clean; `code-simplifier` and `verify-app` subagents automate common workflows; route permission requests to Opus via a hook that scans for attacks and auto-approves safe ones; "use commands for your workflows instead of sub-agents" (inner-loop workflows as slash commands/skills).
- Permissions: do not use `--dangerously-skip-permissions`; pre-allow with wildcard rules (`Bash(bun run *)`, `Edit(/docs/**)`), sandbox (`/sandbox`, cited as 84% fewer permission prompts internally), then auto mode ("instead of dangerously-skip-permissions"), and the `/fewer-permission-prompts` skill that scans history for safe repeated commands.
- Feb 12 customization list: effort level; plugins/LSPs/MCPs/skills; custom agents via `.claude/agents` and the `agent` setting / `--agent`; status line; keybindings; hooks; spinner verbs; output styles; "37 settings and 84 environment variables (use the 'env' field in settings.json to avoid wrapper scripts)"; check `settings.json` into git.
- Mar 30 list: Claude Code mobile app; `/remote-control` and `--teleport`; "/loop and /schedule - two of the most powerful features" for up to a week, "turning workflows into skills + loops"; hooks; fork session; `/btw` side queries; `/batch` for massive changesets; `--bare` "to speed up SDK startup by up to 10x"; `--add-dir`; `--agent` for custom system prompt and tools; `/voice`.
- Apr 16 list (Opus 4.7 era): auto mode; recaps for returning to long sessions; `/focus` mode ("hides all the intermediate work to just focus on the final result"); effort tuning (low..max).
- Search: "agentic search (glob + grep) beats RAG" because code drifts out of sync with an index and permissions are complex (see also [[src-cherny-agentic-search-officechai]]).
## Quotable
> "Update your CLAUDE.md so you don't make that mistake again." (Boris, Feb 1 thread, via summary)
> "give Claude a way to verify its work" (Boris, Jan 3 thread, via summary)

## Used by
[[topic-claude-code-features]]
