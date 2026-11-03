---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop
type: repo
author: Anthropic (claude-plugins-official)
published: undated
accessed: 2026-10-29
reliability: high (official plugin README)
---
# ralph-loop plugin (Stop-hook Ralph)
## Key claims
- Implements Ralph inside the session with a **Stop hook** (`hooks/stop-hook.sh`) that blocks exit and feeds the same prompt back; `/ralph-loop "task" --completion-promise "DONE" --max-iterations N`; `/cancel-ralph`.
- "Always rely on --max-iterations as your primary safety mechanism" (completion promise is exact-string match). Suggests a stuck-state fallback in the prompt ("After 15 iterations, if not complete: document what's blocking...").
- README's poor-fit list: tasks needing human judgment or design decisions, one-shot operations, unclear success criteria, production debugging.
- The same-session loop accumulates context; the external bash loop (fresh process per iteration) does not. For a manager the fresh-process variant (`claude -p` per job) is the safer analogue.

## Used by
[[topic-long-running-always-on-agents]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
