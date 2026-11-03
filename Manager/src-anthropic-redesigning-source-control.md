---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/redesigning-source-control
type: eng-blog
author: Nick G. and the Anthropic source control team
published: 2026-10-13 (updated 2026-10-15)
accessed: 2026-10-29
reliability: med-high (own figures, unverified externally)
---
# Redesigning source control at Anthropic (newest engineering post found)
## Key claims
- "The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI." Daily merges rose from ~2,500 (May 2026) to >30,000 (Sept); CI ~25M checkouts/day.
- Built Scion: server-first VCS, changesets, no packfiles, lock-free compare-and-swap refs; infra CPU/memory ~200x smaller than git mirrors.
- Merge conflicts at agent scale: no global merge-queue lock; rely on post-merge/pre-deploy automated tests; "Claude can typically fix these conflicts faster than humans can even identify them."
- Verification stance: hermetic simulation, fuzzing, rate limiting, Claude as adversarial reviewer, "engineers reviewed the intent of each change rather than every line"; "Superfan" Claude agents watch telemetry beside traditional alerts.
- Implication for a manager: when agent output volume rises, review shifts from line-level to intent-level plus automated checks; infrastructure built for human cadence becomes the constraint.
## Quotable
> "The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI."

## Used by
[[topic-anthropic-agent-guidance]]
