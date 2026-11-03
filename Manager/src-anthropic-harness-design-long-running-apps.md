---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/harness-design-long-running-apps
type: eng-blog
author: Prithvi Rajasekaran (Anthropic Labs)
published: 2026-03-24
accessed: 2026-10-29
reliability: high (primary; small number of anecdotal runs)
---
# Harness design for long-running application development
## Key claims
- Problems: agents lose coherence as context fills; some models (Sonnet 4.5) wrap up early near perceived context limit ("context anxiety"); agents overrate their own output.
- Architecture (full-stack): Planner (short prompt -> product spec, deliverable-focused not over-specific) -> Generator (builds in sprints, uses git) -> Evaluator (drives the live app with Playwright, fails a sprint that misses a hard threshold). Generator and evaluator negotiate a "sprint contract" (definition of done) before each sprint; agents communicate through files.
- Frontend variant: GAN-like generator/evaluator loop, 5-15 iterations, up to 4 h; four criteria (design quality, originality, craft, functionality); evaluator calibrated with few-shot score examples to stop drift.
- Resets (clear window + structured handoff) vs compaction (in-place summary): resets needed with Sonnet 4.5; Opus 4.5 largely removed the anxiety so later harness dropped resets and used auto compaction.
- Self-evaluation: "agents reliably skew positive when grading their own work"; a separate evaluator is much more tractable to tune skeptical. Out of the box Claude was a weak QA agent (talked itself into approving real bugs); the author tuned the QA prompt by reading logs where its judgment diverged from his own.
- Cost data: retro game maker: solo 20 min / $9 (core game did not work) vs full harness 6 h / $200 (playable). DAW (Opus 4.6, simplified harness): ~3 h 50 min / $124.70.
- Simplify as models improve: each harness component "encodes an assumption about what the model can't do on its own"; with Opus 4.6 sprint construct removed, planner kept (generator under-scoped without it), evaluator moved to one end-of-run pass and is worth it only when the task is beyond the model's reliable solo ability. Remove one component at a time; re-examine each new model.
## Quotable
> "agents reliably skew positive when grading their own work"
> "every component in a harness encodes an assumption about what the model can't do on its own"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
