---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2309.03409
type: paper
author: Yang, Wang, Lu, Liu, Le, Zhou, Chen (Google DeepMind)
published: 2023-09-07
accessed: 2026-10-29
reliability: med-high (peer-reviewed ICLR; old models PaLM 2/GPT-3.5/4; first ~100k chars of HTML read)
---
# Large Language Models as Optimizers (OPRO)
## Key claims
- Meta-prompt holds previous instructions with their scores (sorted ascending, best last; best-last ordering converged faster, authors hypothesise recency bias) plus a task description and exemplars (3 random training examples by default) plus meta-instructions on goal/format.
- Best prompts beat human-designed ones "by up to 8% on GSM8K, and by up to 50% on Big-Bench Hard tasks".
- GSM8K (PaLM 2-L scorer): "Take a deep breath and work on this problem step-by-step." 80.2 vs "Let's think step by step." 71.8 vs empty string 34.0. Instruction style found differs by optimizer model (PaLM concise, GPT long).
- Limits: needs a training set of tens of samples; training accuracy runs 5-20% above test (overfitting); error cases in the meta-prompt did not help much.
- Take-away for managers: a brief wording that wins on one model need not transfer; measure per worker model.

## Used by
[[topic-brief-prompt-engineering]]
