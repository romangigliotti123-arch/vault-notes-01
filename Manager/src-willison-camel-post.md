---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Apr/11/camel/
type: practitioner-blog
author: Simon Willison
published: 2025-04-11
accessed: 2026-10-29
reliability: high
---
# Willison on CaMeL and the Dual LLM pattern
## Key claims
- Dual LLM (his 2023 proposal): privileged LLM (P-LLM) has tools but never sees untrusted text; quarantined LLM (Q-LLM) reads untrusted text, has no tools, returns references like `$email-summary-1`.
- Flaw: the Q-LLM itself can be manipulated (injected text can change an extracted email address), so data values can still be attacker-controlled.
- CaMeL adds: custom interpreter running P-LLM-written code in a restricted Python subset; capability tags on every variable (source, allowed readers); policies (e.g. "send_email only if recipient trusted", else ask user).
- Weaknesses: users must define/maintain policies ("Anything that requires end users to think about security policies also makes me deeply nervous"); approval fatigue.
- Against AI-based detection: "The job of an adversarial attacker is to find the 1% of attacks that get through."
- Calls CaMeL the first credible mitigation that does not just add more AI.
## Quotable
> The job of an adversarial attacker is to find the 1% of attacks that get through.

## Used by
[[topic-agent-security]]
