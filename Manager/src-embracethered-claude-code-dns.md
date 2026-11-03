---
tags: [manager-kb, source]
url: https://embracethered.com/blog/posts/2025/claude-code-exfiltration-via-dns-requests
type: practitioner-blog
author: Johann Rehberger (wunderwuzzi)
published: 2025 (disclosed 2025-05-26, fixed 2025-06-06, CVE-2025-55284)
accessed: 2026-10-29
reliability: high (original researcher; fixed in v1.0.4)
---
# Claude Code: data exfiltration with DNS (CVE-2025-55284)
## Key claims
- Chain: hidden text in an analysed source file hijacked Claude; Bash ran with auto-approved commands, read `.env`, and put the secret in a `ping` subdomain => DNS query leaks it to the attacker's server.
- Allowlisted "safe" commands (`whoami`, `ping`, `nslookup`, `host`, `dig`) ran without approval; model-side refusals were bypassed by obfuscating (`strings`/`grep`) and by using an ordinary domain rather than known test domains.
- Triaged CVSS 7.1; fixed in v1.0.4. Proposed fix: remove ping/nslookup/dig/host from the allowlist (human validation).
- Injection sources can be files, MCP servers, web search, PRs. The researcher used Claude itself to find the allowlist bypasses.
- Lesson: allowlists of "harmless" commands are exfil channels (DNS, URLs); only egress control closes them.
## Quotable
> some commands are on an allowlist and run without approval, even when triggered by prompt injection

## Used by
[[topic-agent-security]]
