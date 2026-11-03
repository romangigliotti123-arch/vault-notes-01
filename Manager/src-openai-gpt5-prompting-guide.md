---
tags: [manager-kb, source]
url: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
type: official-doc
author: OpenAI cookbook (page marked "archived and may reference outdated models")
published: undated (GPT-5 launch era, 2025)
accessed: 2026-10-29
reliability: med (vendor guide for another model family, archived; WebFetch summary)
---
# GPT-5 prompting guide (OpenAI cookbook)
## Key claims (relevant cross-vendor parallels)
- Agentic eagerness is tuned by effort and by prompt: lower eagerness -> lower `reasoning_effort`, a tool-call budget with an escape hatch ("even if it might not be fully correct"); higher eagerness -> persistence prompt ("Never stop or hand back to the user when you encounter uncertainty") and "clearly state the stop conditions of the agentic tasks".
- "contradictory or vague instructions can be more damaging to GPT-5 than to other models" because it "expends reasoning tokens searching for a way to reconcile the contradictions".
- Meta-prompting: "early testers have found great success using GPT-5 as a meta-prompter for itself"; ask for "minimal edits/additions that you would make" to fix undesired behaviour.
- Cursor lesson: all-caps/maximising thoroughness language ("Be THOROUGH") backfired on a model already proactive; softening fixed it. (Matches Anthropic's advice to drop CRITICAL/MUST on newer models.)
- Tool preambles: restate the goal, then plan, then progress notes.
- Caveat: the page states it is archived; treat specifics as dated.

## Used by
[[topic-brief-prompt-engineering]]
