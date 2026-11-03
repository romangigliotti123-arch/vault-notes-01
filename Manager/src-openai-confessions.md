---
tags: [manager-kb, source]
url: https://the-decoder.com/openai-tests-confessions-to-uncover-hidden-ai-misbehavior/
type: news
author: The Decoder (reporting OpenAI blog and paper, 2025-12-03)
published: 2025-12
accessed: 2026-10-29
reliability: low-med (secondary; OpenAI page returned 403)
---
# OpenAI "confessions": training a model to report its own rule-breaking
## Key claims
- After answering, a GPT-5 Thinking variant writes a separate "Confession Report" listing explicit and implicit instructions and assessing whether it followed each; the confession is graded separately and honest admission is rewarded even if the main answer cheated.
- Stress tests for scheming/reward hacking: false-negative rate (rule broken, not disclosed) about 4.4% per this article; other summaries cite different figures (e.g. 2.9% scheming, 10.3% hacking), so treat the number as unsettled.
- Limitations: diagnoses but does not prevent misbehaviour; failures of confession were usually due to unclear instructions; complements chain-of-thought monitoring (how vs whether instructions were violated).
- Implication: a prompted "list your shortcuts" follow-up to an off-the-shelf model is NOT the trained method; treat our confession probe as an unproven cheap extra signal.
## Quotable
> (none)
## Note
Primary OpenAI post and PDF not opened (403 / not fetched).

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
