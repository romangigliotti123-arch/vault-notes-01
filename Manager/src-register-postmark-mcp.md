---
tags: [manager-kb, source]
url: https://www.theregister.com/2025/09/29/postmark_mcp_server_code_hijacked/
type: news
author: The Register (reporting Koi Security's find)
published: 2025-09-29
accessed: 2026-10-29
reliability: med-high (news citing vendor research)
---
# postmark-mcp: the first malicious MCP server in the wild
## Key claims
- Fake npm package `postmark-mcp` impersonated Postmark's MCP server. After 15 apparently legitimate versions, v1.0.16 added ONE line BCC-ing every outgoing email to an attacker address.
- ~1,500 downloads in a week; Koi estimates ~20% in real use (~300 orgs) and 3,000-15,000 emails/day diverted (password resets, invoices, MFA codes).
- Postmark warned users 2025-09-25; the package was removed before the article. Koi's co-founder: "a warning shot about the MCP ecosystem itself."
- Lesson: trust earned over many clean versions can be flipped in one update (rug pull); pin versions, review diffs, prefer first-party or self-written MCP servers; rotate anything sent through a suspect tool.
## Quotable
> a warning shot about the MCP ecosystem itself

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
