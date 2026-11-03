---
tags: [manager-kb, source]
url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (list taken from Giskard summary https://www.giskard.ai/knowledge/owasp-top-10-for-agentic-application-2026)
type: standard
author: OWASP GenAI Security Project
published: 2025-12-09
accessed: 2026-10-29
reliability: med-high (OWASP page opened but list was in a download; names via third-party summary)
---
# OWASP Top 10 for Agentic Applications 2026
## Key claims
- Published 2025-12-09. The official page links a PDF download; the ten names below come from the Giskard summary (the OWASP HTML page did not contain them).
- ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution (RCE); ASI06 Memory & Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents.
- Mapping to this host: ASI01 (Telegram/web content), ASI02/03 (admin token for every worker), ASI04 (5,500 imported skills), ASI05 (PowerShell with admin), ASI06 (CLAUDE.md/memory/vault are writable memory), ASI07 (SendMessage between sessions, RC), ASI08 (nested subagents), ASI09 (reports the manager trusts), ASI10.
- Specific mitigation text was NOT retrieved (snippet-level for this list).

## Used by
[[topic-agent-security]]
