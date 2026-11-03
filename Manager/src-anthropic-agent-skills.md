---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
type: eng-blog
author: Barry Zhang, Keith Lazuka, Mahesh Murag
published: 2025-10-16 (update 2025-12-18: published as open standard, agentskills.io)
accessed: 2026-10-29
reliability: high (primary)
---
# Equipping agents for the real world with Agent Skills
## Key claims
- Skill = folder with SKILL.md (YAML name + description) + optional files/scripts. Progressive disclosure in 3 levels: (1) name+description of all skills in the system prompt at start; (2) full SKILL.md when relevant; (3) bundled files only when needed.
- Scripts in skills run as tools without loading code or data into context (deterministic code beats token generation).
- Best practices: build evals first (find gaps, then write skills); split a big SKILL.md into referenced files; watch real usage, name+description drive triggering; have Claude capture its own successful approaches and mistakes into the skill.
- Security: install skills only from trusted sources; audit bundled code and network instructions.
## Quotable
> "it provides just enough information for Claude to know when each skill should be used"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
