---
tags: [manager-kb, source]
url: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
type: eng-blog
author: Jude Gao (Vercel)
published: 2026-01-27
accessed: 2026-10-29
reliability: med-high: primary, single task family (Next.js 16 APIs), small n
---
# AGENTS.md outperforms skills in our agent evals
## Key claims
- Pass rates: baseline (no docs) 53%; skill with default behaviour 53% (+0pp); skill with explicit instructions 79% (+26pp); AGENTS.md compressed docs index 100% (+47pp).
- "In 56% of eval cases, the skill was never invoked." The failure is the decision to retrieve, not the retrieval itself.
- Why passive context won: "No decision point", "Consistent availability" (AGENTS.md is in every turn), "No ordering issues" (skills force a read-docs-before-or-after-exploring choice).
- Search snippets (unverified here): wording of the invoke instruction changed results; a "MUST invoke" phrasing did worse than "explore first, then invoke". Community notes the result is specific to Vercel's tasks and model.
- Implication: for the few things that must happen on EVERY job (read PICKS, log the pick), put an index line in always-loaded context or a hook; do not rely on the model deciding to search.
## Quotable
> "In 56% of eval cases, the skill was never invoked."

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
