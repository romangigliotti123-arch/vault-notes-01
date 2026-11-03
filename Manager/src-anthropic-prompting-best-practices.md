---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
type: official-doc
author: Anthropic
published: undated (covers Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5)
accessed: 2026-10-29
reliability: high (official, current-model doc)
---
# Prompting best practices (current Claude models)
Whole page read (fetched via WebFetch persisted output; fetch the `.md` URL suffix for raw text).
## Key claims
- Be clear and direct: "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows." Key test: show the prompt to a colleague with minimal context; if they would be confused, Claude will be too.
- Add context/motivation: explain WHY ("read aloud by text-to-speech so never use ellipses") rather than bare "NEVER use ellipses"; "Claude can generalize from the explanation."
- Examples: relevant, diverse, wrapped in `<example>` tags; 3-5 examples for best results.
- XML tags to separate instructions/context/input; consistent descriptive names; nest where hierarchical.
- Role in the system prompt: even one sentence helps.
- Long context (20k+ tokens): put long documents at the TOP, query/instructions at the END ("Queries at the end can improve response quality by up to 30 percent"); wrap docs in `<document>` with `<source>`; ask Claude to quote relevant parts first.
- Tell Claude what TO do instead of what not to do; match prompt style to desired output style.
- Prefill on the last assistant turn is removed from Claude 4.6+/Mythos Preview (400 error); migrate to structured outputs, direct instructions, XML output tags, or user-message continuation.
- Tool use: "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them" - use imperatives. `<default_to_action>` vs `<do_not_act_before_instructions>` snippets.
- Aggressive language: Opus 4.5/4.6 are "more responsive to the system prompt"; replace "CRITICAL: You MUST use this tool when..." with "Use this tool when...". "If in doubt, use [tool]" causes overtriggering.
- Parallel tool calls: `<use_parallel_tool_calls>` snippet lifts success to ~100%; "Never use placeholders or guess missing parameters".
- Thinking: adaptive; always on for Fable 5.1/Mythos 5/Opus 5.5. Effort is the control. "choose an approach and commit to it" snippet curbs overthinking.
- Multi-window/long tasks: different prompt for the first context window (set up tests/scripts); tests in structured `tests.json`; `progress.txt` for free text; git for state; prescriptive startup ("Call pwd... Review progress.txt, tests.json, and the git logs"); "extremely effective at discovering state from the local filesystem", so a fresh window can beat compaction.
- Research prompts: success criteria, verify across sources, competing hypotheses, confidence tracking, hypothesis-tree notes file.
- Subagent orchestration: models orchestrate natively; watch overuse (Opus 4.6 spawns subagents where grep suffices). Sample damping prompt: use subagents for parallel/isolated/independent work, not simple/sequential/single-file tasks.
- Overeagerness snippet; test-gaming snippet ("Do not hard-code values... If the task is unreasonable or infeasible, or if any of the tests are incorrect, please inform me rather than working around them"); `<investigate_before_answering>` anti-hallucination snippet.
- Autonomy/safety snippet: consider reversibility; confirm for destructive, hard-to-reverse, visible-to-others actions; "When encountering obstacles, do not use destructive actions as a shortcut".
- Prompt chaining still useful when you must inspect intermediate outputs; commonest pattern is draft -> review against criteria -> refine.
## Quotable
> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."
> "Where you might have said 'CRITICAL: You MUST use this tool when...,' you can use more normal prompting such as 'Use this tool when...' instead."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
