---
tags: [manager-kb, source]
url: https://aider.chat/2023/10/22/repomap.html
type: eng-blog
author: Paul Gauthier (aider)
published: 2023-10-22
accessed: 2026-10-29
reliability: high: primary source, older
---
# Building a better repository map with tree-sitter (aider)
## Key claims
- Repo map built automatically with tree-sitter, extracting symbol definitions.
- Graph ranking: files are nodes, dependency edges; selects the most relevant parts to fit the --map-tokens budget (default 1k).
- Pattern: compact always-available structural index (names and signatures) plus on-demand full content. Equivalent to our NAMES.txt and PICKS idea.
## Quotable
> "fit into the token budget assigned by the user"

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
