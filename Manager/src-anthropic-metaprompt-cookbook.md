---
tags: [manager-kb, source]
url: https://github.com/anthropics/anthropic-cookbook/blob/main/misc/metaprompt.ipynb
type: repo
author: Anthropic cookbook
published: undated (Claude 3 era notebook)
accessed: 2026-10-29
reliability: med (official but old; read raw notebook cell, not run)
---
# Anthropic metaprompt (prompt generator) notebook
## Key claims
- Framing of the writer: "Today you will be writing instructions to an eager, helpful, but inexperienced and unworldly AI assistant who needs careful instruction and examples to understand how best to behave."
- Each in-prompt example has `<Task>`, `<Inputs>` (with `{$VARIABLE}` placeholders) and `<Instructions>`: i.e. a brief template separates the stable instruction from per-run variables.
- Examples show the standard moves: rules list, "first find exact quotes... write them inside <thinking> tags", answer in `<answer>` tags, "If the question cannot be answered by the document, say so" (an explicit not-possible path), "Answer immediately without preamble", and an in-prompt format example.
- Third-party summaries (not opened): same technique powers the Console "Generate a prompt" feature. The older "prompt improver" docs URL now redirects to the prompting best-practices page.

## Used by
[[topic-brief-prompt-engineering]]
