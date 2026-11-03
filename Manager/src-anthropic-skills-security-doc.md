---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
type: official-doc
author: Anthropic
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Agent Skills overview: "Security considerations"
## Key claims
- "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic."
- A malicious Skill can direct Claude to call tools or run code that does not match its stated purpose; audit ALL bundled files (SKILL.md, scripts, images, resources) for unexpected network calls or file access.
- "External sources are risky": skills that fetch URLs can pull in malicious instructions; "even trustworthy Skills can be compromised if their external dependencies change over time" (rug-pull-style drift).
- Treat like installing software, especially with access to sensitive data.
- In Claude Code skills have "the same network access as any other program on the user's computer" (no sandbox). Enterprise-only skill content scanning exists for claude.ai uploads, not for the API/Console, and does not apply to local Claude Code skills.
## Quotable
> Use Skills only from trusted sources: those you created yourself or obtained from Anthropic.

## Used by
[[topic-agent-security]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
