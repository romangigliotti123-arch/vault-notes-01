---
tags: [manager-kb, source]
url: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
type: official-doc
author: Dave Chismon, UK NCSC
published: 2025-12-08
accessed: 2026-10-29
reliability: high (national cyber agency)
---
# Prompt injection is not SQL injection (it may be worse)
## Key claims
- SQL injection is fixed by separating code from data (parameterised queries); LLMs have no such separation, so "prompt injection attacks may never be totally mitigated". Treat the LLM as an inherently confusable deputy; manage risk (likelihood x impact).
- Secure design: assume the model can be manipulated; "focus more on deterministic (non-LLM) safeguards that constrain the actions of the system".
- When an LLM processes input from an untrusted party, reduce its privileges to match that party; keep privileged tools away from it.
- Mark untrusted data as data; avoid deny-list filters (easy to rephrase around); log inputs, outputs, tool calls and failed actions; align with ETSI TS 104 223.
- If residual risk is intolerable, an LLM may be the wrong tool.
## Quotable
> focus more on deterministic (non-LLM) safeguards that constrain the actions of the system

## Used by
[[topic-agent-security]], [[topic-observability]]
