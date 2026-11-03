---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/memory/README.md
type: repo
author: Model Context Protocol maintainers
published: undated
accessed: 2026-10-29
reliability: high: reference server README
---
# MCP memory server (knowledge graph memory)
## Key claims
- Data model: entities (unique name, type, observations), directed relations in active voice, observations that should be atomic (one fact each).
- Tools: create_entities, create_relations, add_observations, delete_*, read_graph, search_nodes, open_nodes. Stored as JSONL (MEMORY_FILE_PATH), lock file for shared use.
- Suggested prompt is chat personalisation (default_user, remember identity/preferences/goals). Note: no timestamps, no provenance, no staleness handling in the data model.
## Quotable
> "Should be atomic (one fact per observation)"

## Used by
[[topic-knowledge-management-rag]]
