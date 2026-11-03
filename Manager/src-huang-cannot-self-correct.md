---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2310.01798
type: paper
author: Huang, Chen, Mishra, Zheng et al. (UIUC, Google DeepMind)
published: 2023-10-03 (v2 2024-03-14)
accessed: 2026-10-29
reliability: high (controlled, older models)
---
# Large Language Models Cannot Self-Correct Reasoning Yet
## Key claims
- Intrinsic self-correction (no external feedback) fails to improve reasoning and sometimes degrades performance (GSM8K and a 100-question set from earlier work; models GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, Llama-2-70B-chat).
- Reported gains in earlier papers (e.g. Reflexion, Kim et al.) came from oracle labels telling the model whether its answer was right; improvements vanish without them.
- Multi-agent debate does not outperform self-consistency at equal numbers of responses; some self-correction gains reflect a weak initial prompt: when the feedback prompt contains task instructions the initial prompt lacked, simply folding them into the initial prompt works better.
## Quotable
> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction"

## Used by
[[topic-llm-judge-and-adversarial-verification]]
