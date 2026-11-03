---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/agent-evaluation-readiness-checklist
type: eng-blog
author: Victor Moreira (LangChain)
published: 2026-03-27
accessed: 2026-11-01
reliability: med (practitioner checklist, numbers are rules of thumb)
---
# Agent Evaluation Readiness Checklist
## Key claims
- Read 20-50 real traces by hand (about 30 min) before building eval infrastructure; spend 60-80% of eval effort on error analysis.
- Start with a few end-to-end trace-level evals; add run- and thread-level later.
- Calibrate LLM judges on 20+ labelled examples, growing to about 100; prefer binary pass/fail to numeric scales.
- Run multiple trials (pass@k / pass^k) for non-deterministic agents; capability evals start at low pass rates, regression evals sit near 100%.
- Track efficiency (steps, tool calls, latency vs ideal); check the data pipeline before blaming the agent (a Witan Labs extraction bug moved a benchmark from 50% to 73%).
## Quotable
> 20-50 hand-reviewed examples you're confident in will outperform hundreds of synthetic examples you haven't verified.
## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-skill-library-retrieval]]
