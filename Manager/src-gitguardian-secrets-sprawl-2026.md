---
tags: [manager-kb, source]
url: https://gitguardian.com/state-of-secrets-sprawl-report-2026
type: eng-blog
author: GitGuardian
published: 2026-03 (report page; press release dated 2026-03-17 per search snippet)
accessed: 2026-10-29
reliability: med-high (vendor telemetry on public GitHub; page text opened)
---
# State of Secrets Sprawl 2026
## Key claims
- 28,649,024 new secrets detected in public GitHub commits in 2025; 1,275,105 AI-service secrets, +81% YoY.
- "Claude Code co-authored commits leak secrets at ~2x the baseline" (press snippets say 3.2% vs 1.5%; the page itself gave only "~2x").
- MCP configuration files: 24,008 unique secrets exposed (14% were PostgreSQL connection strings; top valid types Google API key, Postgres string, Firecrawl, Perplexity, Brave Search keys).
- Remediation lag: of valid secrets from 2022, 64% were still valid four years later (rising to 77% for the 2025 cohort), because teams avoid rotating for fear of outages.
- Lesson: keys pasted into MCP config / agent configs are a leading leak path; rotate and use short-lived or brokered credentials.
## Quotable
> Claude Code co-authored commits leak secrets at ~2x the baseline.

## Used by
[[topic-agent-security]]
