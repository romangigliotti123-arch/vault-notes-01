---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
type: practitioner-blog
author: Simon Willison
published: 2025-06-16
accessed: 2026-10-29
reliability: med-high (widely cited practitioner)
---
# The lethal trifecta for AI agents
## Key claims
- High risk when an agent combines access to private data, exposure to untrusted content, and the ability to communicate externally. LLMs cannot reliably tell where an instruction came from; guardrail products claiming ~95% are a failing grade in web security.
- Only reliable protection for users: avoid the trifecta combination; constrain what an agent can do after reading untrusted input (design patterns, CaMeL).
- For a manager: text returned by a worker that read the web/email is untrusted data, and a manager that holds private data and can send externally completes the trifecta.
## Quotable
> "we still don't know how to 100% reliably prevent this from happening"

## Used by
[[topic-multi-agent-failure-modes]]
