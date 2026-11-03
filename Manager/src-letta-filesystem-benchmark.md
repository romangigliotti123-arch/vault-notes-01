---
tags: [manager-kb, source]
url: https://www.letta.com/blog/benchmarking-ai-agent-memory
type: eng-blog
author: Letta
published: 2025-08-12
accessed: 2026-10-29
reliability: med: vendor, disputed comparison
---
# Benchmarking AI Agent Memory: Is a Filesystem All You Need?
## Key claims
- Letta agent on gpt-4o-mini reached 74.0% on LoCoMo by storing conversation history in files with four tools (grep, search_files, open, close), vs Mem0's reported 68.5% for its top graph variant.
- Claim: whether an agent "remembers" depends on its skill at using the retrieval tool more than on the retrieval mechanism.
- Caveats from commentary (search snippets only): LoCoMo does not score knowledge updates; Mem0 later reports 92.5 on its own page; Letta has not re-run. Benchmark dispute unresolved.
## Quotable
> "Agent Capabilities Matter More Than the Tools" (section heading)

## Used by
[[topic-context-engineering]], [[topic-knowledge-management-rag]]
