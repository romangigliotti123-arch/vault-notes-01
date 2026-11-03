---
tags: [manager-kb, source]
url: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
type: standard
author: OWASP GenAI Security Project
published: 2025 (LLM Top 10 2025 edition)
accessed: 2026-10-29
reliability: high (OWASP primary page)
---
# OWASP LLM06:2025 Excessive Agency (+ LLM Top 10 2025 titles)
## Key claims
- Root causes: excessive functionality (tools not needed), excessive permissions (more downstream access than needed), excessive autonomy (high-impact actions without verification).
- Prevention: offer only needed extensions; limit each to needed functions; prefer narrow granular tools over open-ended ones (a file-writer instead of general shell); restrict downstream permissions (read-only DB); run under the user's identity with minimum-scope credentials; require human approval for high-impact actions; "enforce authorization in downstream systems instead of relying on the LLM's judgment"; sanitize I/O.
- Logging, monitoring and rate limiting do not prevent excessive agency but limit damage.
- LLM Top 10 2025: LLM01 Prompt Injection, 02 Sensitive Information Disclosure, 03 Supply Chain, 04 Data and Model Poisoning, 05 Improper Output Handling, 06 Excessive Agency, 07 System Prompt Leakage, 08 Vector and Embedding Weaknesses, 09 Misinformation, 10 Unbounded Consumption.
## Quotable
> Enforce authorization in downstream systems instead of relying on the LLM's judgment

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
