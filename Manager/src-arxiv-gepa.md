---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2507.19457
type: paper
author: Agrawal et al. (GEPA; DSPy ecosystem)
published: 2025-07-25
accessed: 2026-10-29
reliability: med-high (preprint, strong ablations; first ~100k chars of HTML read)
---
# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
## Key claims
- Mechanism: sample trajectories (reasoning, tool calls, tool outputs) + a feedback function returning a score AND text (compiler errors, failed rubric items); a reflection LM sees "(current prompt, language program trajectory, score, feedback)" and is asked to "reflectively attribute successes or failures to prompt elements and propose revised instructions"; candidate kept if it improves; Pareto frontier of candidates merged.
- Results: beats GRPO by 6% on average (up to 20%) with up to 35x fewer rollouts; beats MIPROv2 by over 10%; best IFBench prompt after 678 rollouts (38.61%) vs GRPO 35.88% at 24,000.
- Learned prompts are "detailed declarative instructions" with sections like "Key Observations and Lessons"; prompts up to 9.2x shorter than MIPROv2's.
- Adversarial caution: an evolved adversarial prompt dropped AIME-2025 pass@1 from 76% to 10%.
- Take-away: failure post-mortems (trace + textual feedback -> rule edits) are a cheap way to improve standing briefs without model training; keep the feedback textual and specific.

## Used by
[[topic-brief-prompt-engineering]]
