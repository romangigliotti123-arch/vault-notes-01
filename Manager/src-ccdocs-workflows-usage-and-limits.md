---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/workflows
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (research preview announced 2026-05-28 per secondary reports; page mentions v2.1.269-2.1.305)
accessed: 2026-11-01
reliability: high (official; full page read). Supplements src-ccdocs-workflows-durability.
---
# Dynamic workflows: when to use, sizing, limits, cost
## Key claims
- Distinction by who holds the plan: with subagents, skills and agent teams Claude decides turn by turn and results land in its context; in a workflow a script holds the loop, branching and intermediate results, so Claude's context holds only the final answer. Scale: subagents "a few delegated tasks per turn", teams "a handful of long-running peers", workflows "dozens to hundreds of agents per run".
- Repeatable quality patterns live in the script: independent agents adversarially review each other's findings before reporting; claims verifiers cannot check are listed as unverified, not refuted; bundled `/deep-research` votes on claims.
- Limits: 16 concurrent agents by default (1-256 via env), 4,096 items per parallel()/pipeline(), 1,000 agents per run; `schema` output is validated (5 retries); no mid-run user input (run each stage as its own workflow for sign-off).
- Cost: advisory "Large workflow" warning above 25 agents or 1.5M projected tokens; size guideline `small` (<5 agents), `medium` (<10, default), `large` (<50), `unrestricted`; default `small` on Pro; try a small slice first. The `ultracode` keyword/effort makes Claude plan workflows for every substantive task (more tokens, limits reached sooner) and skips the large-run warning and subagent concurrency cap; the keyword only works in human-typed prompts, not -p, scheduled tasks or relayed webhooks.
- Usage-limit pause and auto-resume only in interactive claude.ai-subscription sessions (not -p, background sessions, Remote Control, teammates), max twice per run, limit must reset within 24 h.
- Fan-out cache: matching sibling agents read a shared prompt-cache prefix (first agent holds the rest up to 5 s); workflow agents' cache TTL is 5 min unless `subagentPromptCacheTtl` is 1h.
## Used by
[[topic-orchestration-patterns]], [[topic-model-effort-routing-cost]], [[topic-long-running-always-on-agents]]
