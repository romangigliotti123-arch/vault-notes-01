---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/how-we-build-evals-for-deep-agents
type: eng-blog
author: Trivedy, Daugherty, Yurtsev, Chase (LangChain)
published: 2026-03-26
accessed: 2026-11-01
reliability: med (vendor practice, no controlled data)
---
# How we build evals for Deep Agents
## Key claims
- "More evals != better agents": hundreds of tests can give false progress if they do not reflect production behaviour; build targeted evals.
- Each kept eval exerts ongoing pressure on prompts and tool descriptions, so evals shape agent behaviour.
- Sources: dogfooded traces, adapted external benchmarks (Terminal Bench 2.0, BFCL), hand-written tests; seven categories; unit tests excluded from model scoring because any model passes them.
- Correctness first, then efficiency: step ratio, tool-call ratio, latency ratio, solve rate (0 if incorrect). Example: ideal 4 steps/4 calls/8 s vs correct-but-slow 6/5/14 s gives ratios 1.5/1.25/1.75 and solve rate 0.29.
- Run via pytest in CI; tags run subsets to control cost.
## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-skill-library-retrieval]]
