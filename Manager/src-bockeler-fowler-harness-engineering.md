---
tags: [manager-kb, source]
url: https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html
type: practitioner-blog
author: Birgitta Bockeler (Thoughtworks), on martinfowler.com
published: 2026-04-02
accessed: 2026-11-01
reliability: med-high (credible practitioner, conceptual, no measurements)
---
# Harness engineering for coding-agent users
## Key claims
- Harness = the outer controls around the model: guides (feedforward, steer before acting) and sensors (feedback, let the agent self-correct); humans improve the harness whenever the same problem recurs.
- Mix computational controls (linters, type checkers, structural tests: fast, deterministic) with inferential ones (LLM review: slower, less consistent). Shift cheap checks left, expensive ones (mutation testing) after integration.
- Sensor messages should tell the agent how to fix the issue; continuous sensors watch for drift.
- Caveats: verifying functional behaviour is unsolved; AI-generated tests are not trustworthy alone; a silent sensor may mean good quality or weak detection; legacy code is hard to harness.
## Quotable
> (paraphrase of the conclusion, not verbatim) a harness should direct human effort toward where judgment matters most, not eliminate it.
## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-managing-ai-agents-for-roblox-game-dev]]
