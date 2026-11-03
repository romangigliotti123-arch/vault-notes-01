---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2602.06547
type: paper
author: Yi Liu, Zhihao Chen, Yanjun Zhang, Gelei Deng, Yuekang Li, Jianting Ning, Leo Yu Zhang
published: 2026-02-06 (v4 2026-06-10; accepted USENIX Security 2026)
accessed: 2026-10-29
reliability: high (peer-reviewed venue; abstract page opened, full text not)
---
# "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild
## Key claims
- Studied 98,380 third-party skills from two community registries: 157 confirmed malicious, 632 vulnerabilities across 13 attack techniques, avg 4.03 vulnerabilities per malicious skill (multi-phase, deliberate).
- Two dominant strategies, negatively correlated: credential theft via remote code execution, and agent manipulation (hostile instructions hidden in documentation).
- One threat actor accounted for over half of confirmed cases using templated brand impersonation at scale; advanced skills used undocumented capabilities and platform-native trust mechanisms.
- After disclosure maintainers removed all 157 skills.
- Snippet only (search result, not opened): arXiv 2603.16572 (Holzbauer et al., 2026-03) reports the malicious share differs hugely by marketplace and that scanners over-flag; repository-aware analysis cut non-benign flags to 0.52%. Treat as "scanner noise is high" evidence, unverified.
## Quotable
> each malicious skill contains an average of 4.03 vulnerabilities spanning multiple attack phases

## Used by
[[topic-agent-security]], [[topic-skill-library-retrieval]]
