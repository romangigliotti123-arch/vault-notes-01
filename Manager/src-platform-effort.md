---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/effort.md
type: official-doc
author: Anthropic (Claude Platform docs)
published: undated (covers Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5)
accessed: 2026-10-29
reliability: high (raw .md fetched)
---
# Effort parameter (API docs)
## Key claims
- Effort affects ALL output tokens: text, tool calls and arguments, thinking. "Lower effort also means fewer and terser tool calls." It is "a behavioral signal, not a strict token budget".
- Defaults on the API: `medium` for Opus 5.5 and Haiku 5.5, `high` for other models incl. Sonnet 5.5 (note: Claude Code docs say Sonnet 5.5 defaults to medium in Claude Code, see [[src-ccdocs-model-config]]). Setting the default explicitly equals omitting it.
- Level table: low = "Simpler tasks that need the best speed and lowest costs, such as subagents"; medium = "Agentic tasks that require a balance of speed, cost, and performance"; high = complex reasoning/difficult coding/agentic; xhigh = "Long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions"; max = deepest reasoning, no constraints.
- Opus 5.5: `medium` default; "Run an effort sweep on your own evals rather than carrying settings over". Sonnet 5.5: "Start with high unless your workload is agentic or latency-sensitive. For agentic coding and multistep tool use, start with medium for well-specified tasks and move to high for harder or longer ones... Use xhigh or max only where your evals show a quality gain." Haiku 5.5: "Start with medium... Use low... for chat, short tool tasks, and simple, high-volume requests. In long agent prompts, the model is more likely to skip a search, stop early, or skip a check at low." Haiku 5.5 described as "for high-volume, latency-sensitive tasks such as classification, extraction, and routing"; compare xhigh/max with Sonnet 5.5.
- Opus 4.7 guidance (older): "On most workloads max adds significant cost for relatively small quality gains, and on some structured-output or less intelligence-sensitive tasks it can lead to overthinking."
- Best practice 5: "Hold top-level effort constant within cached conversations: Changing the top-level effort value between requests invalidates prompt caching"; on Fable 5.1/Opus 5.5/Sonnet 5.5/Haiku 5.5/Opus 5 use **per-message effort (beta) `output_config`, which preserves the prompt cache**.
## Quotable
> "Use xhigh or max only where your evals show a quality gain."
> "Simpler tasks that need the best speed and lowest costs, such as subagents"

## Used by
[[topic-model-effort-routing-cost]]
