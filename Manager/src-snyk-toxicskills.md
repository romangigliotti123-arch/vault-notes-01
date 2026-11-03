---
tags: [manager-kb, source]
url: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub
type: eng-blog
author: Snyk
published: 2026-02-05
accessed: 2026-10-29
reliability: med-high: security vendor, human-reviewed sample
---
# ToxicSkills: Snyk study of malicious agent skills
## Key claims
- Scanned 3,984 skills from ClawHub and skills.sh as of 2026-02-05.
- 36.82% (1,467) have at least one security flaw; 13.4% (534) at least one critical issue; 76 confirmed malicious payloads (human review: credential theft, backdoors, exfiltration).
- 91% of confirmed malicious skills also use prompt injection; prompt injection appears in 2.6% of all ClawHub skills; 8 malicious skills were still live at publication.
- Curated skills.sh top-100 baseline: 0% false positives on CRITICAL detectors.
- Defender advice: scan with "uvx mcp-scan@latest --skills", rotate credentials, check SOUL.md and MEMORY.md for unauthorised edits (malicious skills persist through memory), keep an AI-BOM inventory.
## Quotable
> "36.82% (1,467 skills) have at least one security flaw."

## Used by
[[topic-agent-security]], [[topic-knowledge-management-rag]], [[topic-personal-assistant-agents]], [[topic-skill-library-retrieval]]
