---
tags: [manager-kb, source]
url: https://snyk.io/articles/clawdbot-ai-assistant/
type: eng-blog
author: Snyk
published: 2026-01-27
accessed: 2026-10-29
reliability: med-high (vendor, but concrete; same product class as this host)
---
# Your Clawdbot (OpenClaw) assistant has shell access and is one prompt injection away from disaster
## Key claims
- Product class: personal assistant wired to WhatsApp/Telegram/Discord/Slack/Signal with shell, files, browser, email, calendar. Three attack paths: direct messages, untrusted content the agent reads, an exposed gateway.
- Concrete risks: publicly reachable gateways (Shodan scans), gateway token = admin; `clawdbot.json` holds API keys/tokens/gateway token in plaintext (a spoofed email asked for that file); injection via email/web/docs/logs; community skills are context and can point at packages to install. "Sandboxing limits where the agent can act, not how it uses access it already has."
- Hardening list: token/password on gateway, localhost bind; DM pairing/allowlists and @mention required in groups; security audit command; Docker sandbox with per-tool allow/deny; human approval for outgoing messages; treat skills as trusted code ("Treat skill folders as trusted code and restrict who can modify them"); rotate secrets after suspected exposure; runtime guardrails.
## Quotable
> Treat skill folders as trusted code and restrict who can modify them.

## Used by
[[topic-agent-security]], [[topic-personal-assistant-agents]]
