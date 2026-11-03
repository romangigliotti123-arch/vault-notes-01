---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/settings-reference.md (+ cli-reference.md)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.290-2.1.311 era)
accessed: 2026-10-29
reliability: high (raw .md)
---
# Settings reference: idleCompaction; CLI reference: --max-budget-usd / --max-turns / --fallback-model
## Key claims
- `idleCompaction` (default true, v2.1.290+): compacts a long conversation you left idle so your next message sends a summary. Conditions (all): interactive terminal / VS Code / desktop session; auto-compact enabled; **conversation on the 1-hour cache TTL**; context >= threshold (default 200,000; change with env `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`, minimum 100000); about an hour idle. Notice: "Compacted while idle, before the prompt cache expired". Turned off by `DISABLE_AUTO_COMPACT` or `idleCompaction: false`.
- CLI (print mode only): `--max-budget-usd` stops the run at an estimated client-side spend (subagent spend counts; "Spend can pass the cap, so leave headroom"; totals restored by --resume do not count; once reached, spawning another subagent fails with `Budget limit reached` and background subagents are stopped). `--max-turns N` exits with an error at the limit (no limit by default). `--fallback-model a,b` tries models in order on overload/unavailable.
- `autoContinueAtUsageLimit`: unattended wait-and-continue after a limit reset; "the setting grants unattended execution".
- `maxEffortLevel` caps effort; `modelSettings.<model>.effortLevel|autoCompactWindow` are per-model.

## Used by
[[topic-context-engineering]], [[topic-context-window-management]], [[topic-model-effort-routing-cost]]
