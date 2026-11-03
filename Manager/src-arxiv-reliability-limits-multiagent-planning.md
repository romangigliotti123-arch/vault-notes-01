---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2603.26993
type: paper
author: (authors not extracted)
published: 2026-03-27
accessed: 2026-10-29
reliability: med (abstract opened; the relay-length MMLU numbers come from a search snippet of the PDF figure caption, not verified in full text)
---
# On the Reliability Limits of LLM-Based Multi-Agent Planning
## Key claims
- Theory note: model a multi-agent LLM system as a finite acyclic decision network communicating through language interfaces of limited capacity. Result: "without new exogenous signals, any delegated network is decision-theoretically dominated by a centralized Bayes decision maker with access to the same information". Communication/compression loss has a closed-form representation (conditional mutual information under log loss; squared posterior error under Brier).
- Practical reading: delegation only pays when it adds new signals (tools, verification, fresh context) or relieves a capacity limit; pure relaying/re-summarising only loses information. Each hop is lossy.
- Snippet-only (unverified here): in a relay-chain experiment on MMLU a single agent scored ~90% and accuracy fell with each added stage, to 22.5% at five stages on one model.
- Supports: shallow hierarchies, passing facts/artifacts by file path rather than re-summarising, verifying with real tool output.

## Used by
[[topic-orchestration-patterns]]
