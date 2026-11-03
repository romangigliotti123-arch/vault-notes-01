---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2503.18813
type: paper
author: Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis, Tramer (Google DeepMind / ETH)
published: 2025-03-24 (v2 2025-06-24)
accessed: 2026-10-29
reliability: high (academic, code released)
---
# Defeating Prompt Injections by Design (CaMeL)
## Key claims
- CaMeL wraps the LLM in a protective system layer: control flow and data flow are extracted from the TRUSTED user query, so untrusted retrieved data cannot change the program's flow.
- Uses capabilities (tags on values) to stop private data flowing to unauthorised sinks; policies are enforced at tool-call time.
- AgentDojo: solves 77% of tasks with provable security vs 84% for an undefended system (~7 point utility cost).
- Code released publicly. Prompt injection not claimed fully solved.
## Quotable
> CaMeL, a robust defense that creates a protective system layer around the LLM

## Used by
[[topic-agent-security]]
