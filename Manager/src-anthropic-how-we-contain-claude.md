---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/how-we-contain-claude
type: eng-blog
author: Anthropic Engineering
published: 2026-05-25
accessed: 2026-10-29
reliability: high (primary)
---
# How we contain Claude across products
## Key claims
- Frame: cap the blast radius (what the agent can reach), not only supervise what it does. Environment first, then model behaviour.
- Layers: claude.ai = ephemeral gVisor container; Claude Code = OS sandbox (Seatbelt/bubblewrap), writes inside workspace, network denied by default, reference devcontainer for unattended runs; Cowork = local VM with own kernel, workspace-only mounts (read-only / read-write / read-write-no-delete), credentials in host keychain.
- Telemetry: users approved ~93% of permission prompts -> approval fatigue -> classifier auto mode. Egress allowlists are capability grants: "Every function reachable through any domain on an allowlist is now an attack surface"; exfiltration worked via an approved domain until an in-VM proxy was added.
- Subagents: can isolate untrusted content and return structured facts instead of raw text; but trusting subagent output more than raw tool results creates an injection path. Persistent memory/state can carry injections across sessions (startup classifiers suggested).
- Red-team phish made Claude exfiltrate credentials in 24 of 25 attempts; only egress + filesystem controls stop that. Parse project config only after trust consent. "the software you build yourself is often the weakest" (custom components caused the worst failures).
## Quotable
> "The engineering question becomes how to cap the blast radius."
> "The deterministic boundary is what gets hit when everything probabilistic misses."

## Used by
[[topic-anthropic-agent-guidance]]
