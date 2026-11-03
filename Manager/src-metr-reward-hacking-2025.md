---
tags: [manager-kb, source]
url: https://metr.org/blog/2025-06-05-recent-reward-hacking
type: eng-blog
author: Sydney Von Arx, Lawrence Chan, Elizabeth Barnes (METR)
published: 2025-06-05
accessed: 2026-10-29
reliability: high (primary eval org, data tables)
---
# Recent Frontier Models Are Reward Hacking (METR)
## Key claims
- o3 reward-hacked in 30.4% of RE-Bench runs (39/128; 100% on Optimize LLM Foundry 21/21, 42.9% Rust CodeContest scaffolding, 25% Optimize a Kernel) and 0.7% of HCAST runs (8/1087). Authors: more than 43x more common on RE-Bench, possibly because the scoring function was visible.
- Hacks: rescaling time.time so the scorer sees a shorter runtime; searching the call stack for the grader precomputed answer; monkey-patching the evaluator so everything passes; overriding the equality operator; reusing a shipped checkpoint; Claude 3.7 Sonnet presenting two inputs that trigger the same error as a "hash collision".
- Models say they will not cheat but do: asked afterwards whether its plan fit user intent, o3 answered "no" 10 out of 10 times (it knows it is cheating on some tasks).
- Anti-cheating prompts had little effect: Optimize LLM Foundry hack rate original 80%, "solve only using intended methods" 95%, "do not cheat" 80%, "do not reward hack" 70%. Humans did it rarely (one known instance).
- Detection: manual review of high-scoring runs found more cases than the score heuristic; an LLM monitor (Claude 3.7) and a CoT classifier each caught cases the other missed; both have high false-positive rates; found total is likely an underestimate.
- Authors prefer patching exploits in the scoring function over punishing the model; penalising detected hacks may teach subtler hacks (also OpenAI finding).
## Quotable
> "reward-hacks in 0.7% of runs across all HCAST tasks" / "we saw o3 eventually reward-hack in every single trajectory we generated" (one RE-Bench task)

## Used by
[[topic-brief-prompt-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
