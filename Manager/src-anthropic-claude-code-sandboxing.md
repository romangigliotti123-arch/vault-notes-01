---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/claude-code-sandboxing
type: eng-blog
author: David Dworken, Oliver Weller-Davies (+ others)
published: 2025-10-20
accessed: 2026-10-29
reliability: high (primary)
---
# Beyond permission prompts: making Claude Code more secure and autonomous
## Key claims
- Permission prompts cause approval fatigue; prompt injection is the main risk with broad access.
- Sandbox = OS-level boundaries (bubblewrap on Linux, seatbelt on macOS): filesystem isolation (only designated dirs) AND network isolation (approved hosts through an external proxy; new domains require confirmation). Both are needed: network-only leaves SSH keys readable; filesystem-only lets a compromised agent reach the network.
- Internal usage: sandboxing safely reduces permission prompts by 84%.
- Open-sourced sandbox runtime (beta) for arbitrary processes/agents/MCP servers; `/sandbox` enables it.
- Claude Code on the web: each session in an isolated cloud sandbox; git credentials/signing keys never inside it; a proxy checks scoped credential + git operation (e.g. only the configured branch) before attaching the real token.
## Quotable
> "In our internal usage, we've found that sandboxing safely reduces permission prompts by 84%."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]]
