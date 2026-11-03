---
tags: [manager-kb, source]
url: https://developers.openai.com/api/docs/guides/function-calling
type: official-doc
author: OpenAI
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc; different vendor, shows convergence)
---
# OpenAI function-calling guide (tool-design advice)
## Key claims
- "Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion"; test with different counts; use tool search to defer large/rare tools.
- Clear names, parameter descriptions, say when to use / not use each function in the system prompt; examples help but "may hurt reasoning models".
- Strict mode: `additionalProperties:false`, all properties required, optional = nullable.
- "Don't make the model fill arguments you already know" (pass IDs from app state); combine functions always called in sequence; enums/structured objects prevent invalid states.
- "Intern test": could someone use the function correctly using only what the model sees?
## Quotable
> Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion.

## Used by
[[topic-tool-and-mcp-design]]
