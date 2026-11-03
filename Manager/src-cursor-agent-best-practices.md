---
tags: [manager-kb, source]
url: https://cursor.com/blog/agent-best-practices
type: eng-blog
author: Lee Robinson (Cursor)
published: 2026-01-09
accessed: 2026-10-29
reliability: med (vendor practitioner guidance; WebFetch summary with quotes)
---
# Best practices for coding with agents (Cursor)
## Key claims
- "The agent's success rate improves significantly with specific instructions" (name the file, the edge case, the pattern to follow).
- Verification is the lever: "Agents can't fix what they don't know about. Use typed languages, configure linters, and write tests." "Give the agent clear signals for whether changes are correct." "Agents perform best when they have a clear target to iterate against."
- Planning: "The most impactful change you can make is planning before coding"; to redo work "go back to the plan" rather than patching through follow-up prompts; "Not every task needs a detailed plan."
- Context: don't over-include files ("Including irrelevant files can confuse the agent"); "If you notice the effectiveness of the agent decreasing, it's time to start a new conversation."
- Rules files: always-on context; "Start simple. Add rules only when you notice the agent making the same mistake repeatedly"; reference files instead of copying their contents.
- Review: "AI-generated code can look right while being subtly wrong." "Read the diffs and carefully review." "The faster the agent works, the more important your review process becomes."
- Parallel agents: each in its own worktree; several models on the same problem then pick the best.

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
