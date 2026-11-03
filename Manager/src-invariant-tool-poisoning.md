---
tags: [manager-kb, source]
url: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
type: eng-blog
author: Invariant Labs
published: 2025-04-01
accessed: 2026-10-29
reliability: high (original disclosure; PoC in Cursor; vendor sells scanner)
---
# MCP Security Notification: Tool Poisoning Attacks
## Key claims
- Tool poisoning: malicious instructions hidden in an MCP tool DESCRIPTION are visible to the model but not to the user; a form of indirect prompt injection. PoC: an `add` tool told the model to read `~/.cursor/mcp.json` and `~/.ssh/id_rsa` and pass them via a parameter, while hiding this.
- Rug pull: "a malicious server can change the tool description after the client has already approved it".
- Tool shadowing: one server's description alters how the agent uses ANOTHER server's trusted tool (e.g. redirect all `send_email` to the attacker) without appearing in the user-facing log.
- Clients often show only a simplified tool name and hide arguments in confirmation dialogs.
- Recommendations: show full descriptions (separating model-only text), pin server/tool versions and verify by hash, enforce cross-server isolation/dataflow controls.
## Quotable
> a malicious server can change the tool description after the client has already approved it

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
