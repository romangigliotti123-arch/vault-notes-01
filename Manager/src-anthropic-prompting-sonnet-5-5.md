---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high (official; our default worker model)
---
# Prompting Claude Sonnet 5.5
Our `sonnet-worker` runs this model. Raw markdown fetched with curl (`.md` suffix).
## Key claims
- Effort recalibrated vs Sonnet 5: "Run a fresh sweep against your own evals". Start `high` unless agentic/latency-sensitive; agentic coding and multistep tool use: `medium` for well-specified tasks, `high` for harder/longer. Reserve `xhigh`/`max` for work with a measured quality gain.
- At `low` "it keeps its thinking short and can skip verifying a change"; at `low`/`medium` on long agentic tasks "it's more likely to stop and check in with the user before it completes its work".
- Asking in the system prompt to think less "doesn't reliably reduce its thinking"; lower effort instead.
- Carry-through snippet: "Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step. When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it."
- Unrequested additions (tests, docs, small files) at every effort level, more at higher; the second paragraph of the snippet limits that.
- At `xhigh`/`max` it starts its own review rounds, sometimes with reviewer subagents; snippet "don't launch reviewer sub-agents unless the user asked for a review" cut session cost by about a third on max effort with no quality change.
- Open-ended asks may trigger building; snippet: when asked for ideas/options/plan, give them and stop.
- Verification at `low`: sometimes "reports a change as done without running a check that exercises it". Snippet: run a real check (tests/type-check/build/changed command); a syntax-only check or one that failed to start does not count; install declared deps with the project's package manager; "Only if no real check can run here, say which one you did not run and why instead of reporting the change as done."
- Progress updates: between tool calls it writes notes; a harness can remind after ~5 silent tool steps; frequent harness text after tool results can be misread as prompt injection; never put user text inside tool_result.
- Knowledge work: may answer from training data; add "Use the search tool to check specifics that may have changed since your training...".
- JSON on reasoning tasks: may skip thinking; add "Think the problem through before you answer."; treat `stop_reason: max_tokens` as failed even if JSON valid; if JSON requested in plain prompt, parse the LAST JSON value.
## Quotable
> "At low, it keeps its thinking short and can skip verifying a change."
> "Only if no real check can run here, say which one you did not run and why instead of reporting the change as done."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
