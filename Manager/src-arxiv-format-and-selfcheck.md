---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2408.02442 ; https://arxiv.org/abs/2310.01798 ; https://arxiv.org/abs/2309.11495 ; https://arxiv.org/abs/2303.17651
type: paper
author: Tam et al. (format restrictions); Huang et al. (self-correct); Dhuliawala et al. (CoVe); Madaan et al. (Self-Refine)
published: 2024-08-05; 2023-10-03; 2023-09-20; 2023-03-30
accessed: 2026-10-29
reliability: med (abstracts only via arXiv API; 2023-24 models; results may have shifted with 2026 models)
---
# Format restrictions and self-checking (abstracts)
## Key claims
- Let Me Speak Freely?: "we observe a significant decline in LLMs reasoning abilities under format restrictions... stricter format constraints generally lead to greater performance degradation in reasoning tasks." (Disputed by structured-output vendors; see [[src-arxiv-prompt-report]] note on the disagreement; Anthropic's own docs say structured outputs can make Sonnet 5.5 skip thinking: [[src-anthropic-prompting-sonnet-5-5]].) For reports: let the worker do its work in free text, then fill a small schema.
- LLMs Cannot Self-Correct Reasoning Yet: "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." Self-verification needs an external signal (tool output, tests, another context).
- Self-Refine: same LLM gives feedback and refines; ~20% absolute average improvement across 7 tasks (older GPT models) - works when the feedback criteria are concrete; conflicts in spirit with Huang et al. unless external feedback exists.
- Chain-of-Verification: draft -> plan verification questions -> answer them "independently so the answers are not biased by other responses" -> final verified response; reduces hallucination in list/long-form tasks. The independence step is the transferable idea: the verifier should not see the claim's justification.

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
