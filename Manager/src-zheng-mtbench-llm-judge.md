---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2306.05685
type: paper
author: Zheng, Chiang, Sheng, Zhuang et al. (LMSYS/UC Berkeley)
published: 2023-06-09 (v4 2023-12-24)
accessed: 2026-10-29
reliability: high (foundational, full text skimmed)
---
# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
## Key claims
- Strong LLM judges (GPT-4) agree with human preferences over 80%, the same level as human-human agreement (3K expert votes, 3K crowdsourced votes).
- Documented biases: position bias, verbosity bias, self-enhancement bias, limited reasoning/math grading ability.
- Position bias test with near-identical answers: only GPT-4 gave consistent results (swap-order consistency) in more than 60% of cases; Claude-v1 also showed a name bias favouring "Assistant A".
- Verbosity "repetitive list" attack (padding a numbered list with rephrased items): all judges are prone; GPT-4 defends best. Identical answers are correctly tied.
- Self-enhancement: data too limited to confirm in this paper (later work, see [[src-panickssery-self-preference]], confirms self-preference).
- Math/reasoning grading: judge failure rate when grading 20 math questions: 14/20 default prompt, 6/20 with chain-of-thought, 3/20 with reference-guided (judge sees a reference solution).
- Mitigations: swap positions and declare a win only if the answer wins in both orders (else tie); randomise positions at scale; chain-of-thought judging; reference-guided judging.
## Quotable
> "Only GPT-4 outputs consistent results in more than 60% of cases" (position-bias test on near-identical answers)
## Note
Numbers read from arxiv.org/html/2306.05685.

## Used by
[[topic-llm-judge-and-adversarial-verification]]
