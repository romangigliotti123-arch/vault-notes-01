---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2308.00352
type: paper
author: Hong et al. (MetaGPT)
published: 2023-08-01
accessed: 2026-10-29
reliability: med (abstract + repo README opened; 2023 models; MAST paper gives independent failure data)
---
# MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework
## Key claims
- Encodes human Standardized Operating Procedures (SOPs) into prompt sequences; agents with roles (product manager, architect, project manager, engineer) work on an "assembly line" and verify intermediate results to cut "cascading hallucinations" from naively chaining LLMs. Structured intermediate artifacts (PRD, design docs, interfaces) rather than free chat.
- Repo README tagline: "Code = SOP(Team)"; takes a one-line requirement and outputs user stories, competitive analysis, data structures, APIs, docs.
- Repo status (gh api 2026-10-29): 71,058 stars, MIT, last push 2026-01-21 (stale for 9 months); company pivoted to the MGX product (launched 2025-02-19).
- Independent evidence: MAST (arXiv 2503.13657) found MetaGPT has fewer system-design failures than ChatDev because adherence to task/role spec is enforced through SOPs; ChatDev had better verification. Both still fail often.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
