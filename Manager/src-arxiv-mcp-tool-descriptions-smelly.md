---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2602.14878
type: paper
author: Hasan, Li, Rajbahadur, Adams, Hassan
published: 2026-02-16 (v3 2026-05-31)
accessed: 2026-10-29
reliability: med-high (empirical SE paper; abstract page opened)
---
# MCP Tool Descriptions Are Smelly!
## Key claims
- 856 tools from 103 MCP servers; six description components and a scoring rubric. 97.1% of descriptions have at least one "smell"; 56% do not clearly state purpose. Most common smells (per search snippet of the paper): unstated limitations 89.8%, missing usage guidelines 89.3%, opaque parameters 84.3%.
- Augmenting descriptions with all six components raised task success by a MEDIAN +5.85 percentage points and partial goal completion +15.12%, but execution steps rose +67.46% and 16.67% of cases regressed. Compact component combinations often kept reliability at lower token cost.
- Companion study (snippet only, not opened): arXiv 2602.18914 reports smells measurably change LLM tool selection (functionality +11.6%, accuracy +8.8% for fixes).
- Takeaway: description quality matters, but "more text" is not free; measure with evals.
## Quotable
> 97.1% of the analyzed tool descriptions contain at least one smell

## Used by
[[topic-tool-and-mcp-design]]
