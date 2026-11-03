---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2606.09863
type: paper
author: Laksh Advani (ICML 2026 listing per search result)
published: 2026-06-01
accessed: 2026-10-29
reliability: med-high (large trajectory sets; single author, preprint)
---
# From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents
## Key claims
- False success = agent asserts completion while environment state shows otherwise. 9,876 tau2-bench trajectories (8 model families) and 1,879 AppWorld trajectories (4 families) with text-independent ground truth.
- False success is 45-48% of failures in single-control tau2-bench domains, 3% in dual-control telecom (where a second party can check state), and 75.8% among AppWorld self-assessing coding-agent trajectories with explicit status claims. Per-model rate on tau2 failures ranges 13% (GPT-5.2) to 79% (a Qwen variant); two Anthropic models about 30-35%.
- LLM judges fail: no configuration over 5 judges, 5 prompt strategies, full task specification exceeds AUROC 0.65 on tau2-bench; 0.54 on AppWorld API-call traces. Judges rely on surface proxies (confident closing language, action-sequence volume) not verified state changes.
- Lightweight TF-IDF detectors reach AUROC 0.83 (tau2) and 0.95 (AppWorld), recovering 4-8x more false successes than the best judge at the same flag rate, with 3,300x lower latency; judge and detector are partly complementary (75/25 ensemble 0.834 -> 0.855). Use as triage signal, not autonomous monitor.
## Quotable
> "LLM agents can fail silently by asserting task completion when the environment state shows otherwise."

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
