---
tags: [manager-kb, source]
url: https://docs.openclaw.ai/gateway/security.md ; https://dev.to/lars_winstand/my-openclaw-agent-looked-idle-overnight-and-still-burned-through-tokens-4ikj ; search snippets (Koi Security "ClawHavoc", SecurityScorecard, JFrog, incidentdatabase.ai)
type: mixed (official doc + practitioner blog + snippets)
author: OpenClaw docs; Lars Winstand (dev.to, 2026-05-12); others
published: 2026-01 to 2026-05
accessed: 2026-10-29
reliability: low-med (docs opened; incident numbers are snippet-only from secondary sites; Koi/THN pages blocked 403/redirected)
---
# OpenClaw security incidents and cost reports (what went wrong at scale)
## Key claims
- Project history: Clawdbot (Nov 2025) -> Moltbot (2026-01-27, after Anthropic trademark contact) -> OpenClaw (2026-01-30); abandoned social accounts were hijacked by scammers during renames (snippet-level, several press sites agree).
- Docs (opened): default install binds the Gateway to loopback; unknown DM senders get a pairing code; groups allowlisted; "One trust boundary per gateway"; OpenClaw "is not a hostile multi-tenant security boundary"; ships `openclaw security audit` (checkIds, auto-fix) and an operator incident-response page; "Agents with message-tool access can send across conversations and channel providers by default" unless restricted.
- Snippet-only third-party numbers (unverified here): Koi Security audited 2,857 ClawHub skills and flagged 341 malicious (335 one campaign "ClawHavoc" delivering macOS stealer AMOS via fake prerequisites), later 824 of 10,700; exposure scans found 40,000 to 135,000 internet-exposed instances; one-click RCE CVE-2026-25253 (CVSS 8.8, reported); "ClawJacked" browser-to-localhost hijack. Pattern: marketplace skills + broad credentials + exposed gateway = supply-chain compromise.
- Cost (practitioner blog opened, low reliability): "heartbeats that keep resending a fat conversation history back through the model" made an apparently idle agent burn the budget overnight; fixes suggested: longer heartbeat intervals, bounded sessions with handoff files, cron for repetitive work, model tiering. Anecdotes (snippets): a $126 bill that made a developer kill their setup; "$623 in a month from 5-minute health checks"; no framework default cost cap or kill switch. A widely repeated "$1.3M API bill" for the creator is secondary only.
## Quotable
> heartbeats that keep resending a fat conversation history back through the model

## Used by
[[topic-agent-security]], [[topic-long-running-always-on-agents]], [[topic-personal-assistant-agents]]
