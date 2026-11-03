---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/remote-control.md#connection-and-security
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Remote Control: connection and security
## Key claims
- The local session makes outbound HTTPS only, opens no inbound ports; multiple short-lived, single-purpose credentials.
- While connected, the session transcript "including your messages, Claude's responses, and tool activity" is stored on Anthropic servers to sync devices. Secrets printed by tools are therefore also stored there, not only in local jsonl.
- `disableRemoteControl` turns the feature off. Trusted Devices (device enrolment gate) is Team/Enterprise beta; individual accounts rely on claude.ai login security.
- Implication: whoever controls Roman's claude.ai session (phone, Google account, session cookie) can issue instructions to a bypass-mode, elevated-admin shell. The account is the root of trust; its 2FA/passkey and phone lock matter more than any prompt rule.
## Quotable
> Your local Claude Code session makes outbound HTTPS requests only and never opens inbound ports on your machine.

## Used by
[[topic-agent-security]]
