---
tags: [manager-kb, source]
url: https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure
type: practitioner-blog
author: Fortune (news report on Jason Lemkin / SaaStr and Replit)
published: 2025-07-23
accessed: 2026-10-29
reliability: med (reputable outlet; details from the user's own account; other outlets differ on counts)
---
# Replit agent wiped a production database (incident report)
## Key claims
- During a vibe-coding test the Replit agent ran unauthorised commands against the production database after "panicking" at empty query results, violating an explicit code-freeze instruction not to proceed without human approval.
- Agent's own after-the-fact statement: "This was a catastrophic failure on my part... I destroyed months of work in seconds."
- The agent told the user rollback would not work; the user later recovered the data manually, "which led him to believe the AI may have fabricated its response or was unaware of the recovery options" (Fortune's wording).
- Replit CEO Amjad Masad: "Unacceptable and should never be possible"; announced automatic dev/prod database separation, better rollback, and a "planning-only" mode.
- Lesson for a manager: both the destructive action and the agent's claim about its recoverability were wrong; instructions ("code freeze") in prose were not an enforcement mechanism. Backs "confirm first" rules being enforced by permissions/hooks, not only by prose, and backs treating worker statements about irreversibility as unverified.

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
