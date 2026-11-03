---
tags: [manager-kb, source]
url: https://cline.bot/blog/why-cline-doesnt-index-your-codebase-and-why-thats-a-good-thing
type: eng-blog
author: Nick Baumann (Cline)
published: 2025-05-27
accessed: 2026-10-29
reliability: med: product rationale, no benchmark
---
# Why Cline Doesn't Index Your Codebase
## Key claims
- Chunking "literally tears apart" code logic; index is a frozen snapshot that goes stale after refactors/merges; embeddings are a second copy of sensitive code (security surface).
- Alternative: explore like a senior engineer, follow imports and structure; "No index or embeddings."
- HN critics said this is still retrieval (filesystem/AST traversal), just not vector retrieval (from search snippets only).
## Quotable
> "An index, by definition, is a snapshot frozen in time."

## Used by
[[topic-knowledge-management-rag]]
