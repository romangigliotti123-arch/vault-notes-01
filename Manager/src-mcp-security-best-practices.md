---
tags: [manager-kb, source]
url: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices
type: spec
author: Model Context Protocol project
published: undated (draft spec, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (normative spec text, draft version)
---
# MCP Security Best Practices (draft spec)
## Key claims
- Attacks covered: confused deputy (MCP proxy with static client ID + dynamic registration + consent cookie; mitigated by per-client consent, exact redirect_uri match, state validation), token passthrough, SSRF during OAuth discovery, state-handle hijacking, local MCP server compromise, OAuth authorization URL validation (javascript:, shell-open), stdio proxy escalation, mix-up attacks, localhost redirect impersonation, scope minimization.
- Token passthrough is explicitly forbidden: "MCP servers MUST NOT accept any tokens that were not explicitly issued for the MCP server." Risks: bypasses rate-limit/validation controls, destroys audit trail, trust-boundary breakage.
- Local servers: one-click local config MUST show the exact command un-truncated, flag dangerous patterns (sudo, rm -rf, network, sensitive paths), and require explicit approval; SHOULD sandbox with minimal privileges; use `stdio` or restricted IPC for local servers.
- SSRF: block private/link-local ranges (incl. 169.254.169.254), HTTPS only, validate redirects, consider egress proxy.
- Scope minimization: start with minimal scopes, step-up on demand; avoid wildcard/omnibus scopes; log elevation events.
## Quotable
> MCP servers MUST NOT accept any tokens that were not explicitly issued for the MCP server.

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
