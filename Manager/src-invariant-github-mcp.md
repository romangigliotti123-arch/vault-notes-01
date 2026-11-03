---
tags: [manager-kb, source]
url: https://invariantlabs.ai/blog/mcp-github-vulnerability
type: eng-blog
author: Invariant Labs
published: 2025-05-26
accessed: 2026-10-29
reliability: high (original disclosure; vendor sells guardrails)
---
# GitHub MCP exploited: private repo data leaked via a malicious public issue
## Key claims
- Chain: attacker files an issue with an injection on the victim's PUBLIC repo; victim asks agent to "review open issues"; agent reads the issue, pulls data from PRIVATE repos into context, then publishes it in a PR on the public repo.
- Preconditions: GitHub MCP connected with account-wide access; both public and private repos; user had "Always Allow" on tool calls. Demo used Claude 4 Opus ("still susceptible").
- Authors: "not a flaw in the GitHub MCP server code itself"; it is "a fundamental architectural issue that must be addressed at the agent system level", so GitHub cannot patch it server-side.
- Mitigations proposed: least-privilege tokens limited to needed repos, runtime policies such as one repository per session, continuous monitoring/audit of agent-MCP calls (their products).
- Secondary reports (not opened): Repello says separate sessions for public vs private work remove a required property; a read-only token removes the convenient exfil channel but not the exposure.
## Quotable
> a fundamental architectural issue that must be addressed at the agent system level

## Used by
[[topic-agent-security]]
