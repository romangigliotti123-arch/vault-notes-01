---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/topoteretes/cognee/main/README.md
type: repo
author: topoteretes (Cognee)
published: undated
accessed: 2026-10-29
reliability: med: vendor README, small benchmark
---
# Cognee README (AI memory knowledge graph)
## Key claims
- Four operations: remember, recall (auto-routing among search strategies), improve (apply feedback, move session knowledge into the graph), forget. Text becomes entities, relationships and chunks; code becomes a symbol/dependency graph.
- Runs locally without API key (GLiNER extractor, local embeddings) or with OpenAI/Ollama; single Postgres (PGVector + graph state) is a demo feature, production is licensed. Integrations: Claude Code, MCP.
- BEAM eval (LLM-judged): 0.79 at 100K tokens (20 questions, one conversation) and 0.67 at 10M tokens ("Exploratory"); the two are not comparable per the README.
## Quotable
> "a self-hosted knowledge graph your agents can search and reuse"

## Used by
[[topic-knowledge-management-rag]]
