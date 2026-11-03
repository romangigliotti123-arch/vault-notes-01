---
tags: [manager-kb, source]
url: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
type: practitioner-blog
author: Mario Zechner
published: 2025-11-30
accessed: 2026-10-29
reliability: med-high (detailed first-hand build log; opinionated, minimal benchmarking)
---
# What I learned building an opinionated and minimal coding agent (pi)
## Key claims
- Motivation: Claude Code became "a spaceship with 80% of functionality I have no use for"; "The system prompt and tools also change on every release, which breaks my workflows". Harnesses inject content "behind your back that isn't even surfaced in the UI"; he wants "context engineering is paramount" with full inspectability and a documented session format.
- Minimal design: 4 tools (read, bash, edit, write), tiny system prompt, YOLO by default ("security measures in other coding agents... are mostly security theater" because of the lethal trifecta: read private data + run code + network).
- No built-in to-dos or plan mode: use externally stateful files (TODO.md, PLAN.md) "shared across sessions, versioned with your code" and fully observable.
- No MCP: Playwright MCP 21 tools = 13.7k tokens, Chrome DevTools MCP 26 tools = 18k tokens (7-9% of context before work starts); prefer CLI tools + README read on demand (progressive disclosure).
- No background bash: use tmux ("Tmux also gives you a CLI argument to list all active sessions... you could hop into that session and co-debug with the agent").
- No sub-agents: sub-agents are "a black box within a black box" with poor context transfer; context gathering mid-session "is a sign you didn't plan ahead" - gather in its own session and write an artifact. Valid use: spawn itself via bash (`pi --print`) for code review.
- Models read parts of files and miss context: "we trust our agents too much".
## Quotable
> Using a sub-agent mid-session for context gathering is a sign you didn't plan ahead.
> The system prompt and tools also change on every release, which breaks my workflows and changes model behavior.

## Used by
[[topic-cross-device-agent-control]], [[topic-personal-assistant-agents]]
