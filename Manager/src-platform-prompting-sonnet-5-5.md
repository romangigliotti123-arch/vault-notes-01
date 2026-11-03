---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (current)
accessed: 2026-10-29
reliability: high (official; measured claims)
---
# Prompting Claude Sonnet 5.5 (the default worker model)
## Key claims
- "For the hardest long-horizon work, an Opus model is the better choice."
- Effort: recalibrated vs Sonnet 5, start `high` (API default) unless agentic/latency-sensitive; agentic coding: `medium` for well-specified, `high` for harder/longer; `xhigh`/`max` only where measured gain. At `low`/`medium` on long tasks it "is more likely to stop and check in with the user before it completes its work"; at `low` it can skip verification.
- Carrying work through (add to system prompt): "Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step. When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it." Makes low/medium sessions longer and costlier; does not replace your own rules on risky actions.
- xhigh/max: self-started review rounds and reviewer subagents. Fix: "Don't start extra rounds of review or hardening on your own, and don't launch reviewer sub-agents unless the user asked for a review." Measured: at max effort this stopped reviewer-subagent launches and cut session cost by about a third with no quality change.
- Open-ended asks ("show me what you can do") can trigger building; prompt "When the user asks for ideas, options or a plan, give them that and stop. Don't start building or changing anything until they say to go ahead."
- Progress updates: long tool turns look silent unless `display: "updates"`; harness can nudge after ~5 silent tool steps with a one-turn reminder: "The user hasn't heard from you in a while — say in a few words what you're doing, then continue." Remove older "hold all findings for the final response" lines. Frequent harness text after tool results can be misread as prompt injection.
- Mid-turn messages: never inside tool_result; as a user text block after the last tool_result; do not add your own per-tool token countdowns.
- Coding verification at low effort: same "run a real check" paragraph as Haiku 5.5.
- Tool-call tolerance: accept unambiguous case-mismatch tool names or return is_error with the exact expected name.
## Quotable
> "At `low` and `medium`, on long agentic tasks, it's more likely to stop and check in with the user before it completes its work."
> "Don't start extra rounds of review or hardening on your own, and don't launch reviewer sub-agents unless the user asked for a review."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
