---
tags: [manager-kb, source]
url: https://tianpan.co/blog/2026/04/23/hallucinated-success-agent-false-completion
type: practitioner-blog
author: Tian Pan
published: 2026-04-23
accessed: 2026-10-29
reliability: low-med (practitioner synthesis; some figures labelled hypothetical; WebFetch summary)
---
# Hallucinated success: agent false completion
## Key claims
- Thesis: agents report success for work not done; failure is silent. "The agent is not observing reality. It is observing its own narration of reality." "The verifier is the architecture."
- Self-reflective loops (ReAct/Reflexion) judge their own narration; self-reported completion metrics get corrupted.
- Mitigations: independent checker that sees original goal and raw final state but not the executor's reasoning/summary; deterministic side-effect assertions (stat the file, query the provider, look up the ticket ID) with tasks declaring expected side effects in structured form; trajectory replay to build a failure corpus; schema validation necessary but insufficient ("well-formed fabrications pass"); make ground-truth-backed success the headline metric and self-reported metrics diagnostic only.
- Cites (not opened by me): MAST (premature termination + skipped verification), SWE-bench "hundreds of patches pass tests without fixing the issue". The 94% vs 61% example in the post is explicitly hypothetical.

## Used by
[[topic-report-formats-and-verification]]
