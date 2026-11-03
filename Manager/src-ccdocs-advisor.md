---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/advisor.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (experimental feature, v2.1.260+)
accessed: 2026-10-29
reliability: high (primary vendor docs)
---
# Claude Code docs: Escalate hard decisions with the advisor tool
## Key claims
- Experimental, Anthropic API only (not Bedrock/Vertex/Foundry). Main model consults a stronger "advisor" server-side at decision points (before committing to approach, recurring error, before declaring done). Advisor receives the FULL conversation incl. tool calls/results.
- Enable: `/advisor opus`, `advisorModel` setting, `--advisor` flag. Works in `-p`, Remote Control (v2.1.260+). `/advisor off`. `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`.
- Pairing rule: advisor must rank >= main model. Haiku 5.5 or Sonnet 5 main -> Fable, Opus 4.7+, Sonnet 5+, Haiku 5.5. Sonnet 5.5 main -> Fable, Opus 5+, Sonnet 5.5. Opus 5/5.5 main -> Fable, Opus 5+. Subagents inherit the advisor (pairing checked against their own model).
- Pairing table: "Haiku main + Opus advisor: Lowest-cost main model with strong planning. Expect higher cost than Haiku alone but lower than switching the main model to Sonnet or Opus." "Sonnet main + Opus advisor: escalates planning, ambiguous failures, completion checks to Opus."
- Cost: advisor tokens counted at the advisor model's rates; subscription: counts toward plan limits. "The advisor model's own read of the conversation is not cached. Each advisor call processes the full transcript anew." So advisor cost grows with manager context size - another reason to keep a 24/7 manager's context small.
- Toggling `/advisor` mid-session does NOT invalidate the main cache.
- Timing is model-driven; "There is no setting to cap or force advisor calls"; can ask in prompt ("consult the advisor before you continue").
- Compared with opusplan (plan mode only), subagents with `model` (whole subtask), `/model` (from next request on).
## Quotable
> "Haiku main + Opus advisor | Lowest-cost main model with strong planning. Expect higher cost than Haiku alone but lower than switching the main model to Sonnet or Opus"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-model-effort-routing-cost]]
