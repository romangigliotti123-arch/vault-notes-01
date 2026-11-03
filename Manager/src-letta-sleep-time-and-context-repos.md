---
tags: [manager-kb, source]
url: https://letta.com/blog/sleep-time-compute ; https://www.letta.com/blog/context-repositories
type: eng-blog
author: Letta
published: 2025-04-21 (sleep-time compute); 2026-02-12 (context repositories)
accessed: 2026-10-29
reliability: med (vendor posts, no benchmark numbers in the pages as fetched via summary)
---
# Letta: sleep-time compute and context repositories
## Key claims
- Sleep-time compute: "using their downtime to reorganize information and reason through the information they have available in advance" via a separate background agent; "fundamentally requires stateful AI agents". Suggests a fast primary model plus a larger slower model for the sleep-time agent. More frequent runs cost more tokens. Page gives no figures.
- Context repositories (MemFS): agent context stored as files in a git-backed directory; `system/` files are always loaded into the prompt, the file tree is always visible, other files are loaded by progressive disclosure using per-file frontmatter descriptions; "Every change to memory is automatically versioned with informative commit messages"; subagents work in worktrees and merge back. Defragmentation target "a clean hierarchy of 15-25 focused files" (design target, no results reported).
- Search-snippet only: Letta's "next phase" post says server-side sleep-time agents are being replaced by client-side subagents and legacy memory tools by filesystem operations.
- Reading for us: this is the same shape as our setup (files + progressive disclosure + background subagent that consolidates notes). Supports a "memory curator" subagent run at low cost, not a new framework.
## Quotable
> "Every change to memory is automatically versioned with informative commit messages."

## Used by
[[topic-context-window-management]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
