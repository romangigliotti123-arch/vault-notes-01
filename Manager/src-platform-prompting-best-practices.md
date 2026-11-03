---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (current; covers Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, 4.x)
accessed: 2026-10-29
reliability: high (official, current-model era)
---
# Prompting best practices (Claude 5-era), agentic sections
## Key claims
- Be clear and direct; "Think of Claude as a brilliant but new employee who lacks context"; key test: show the prompt to a colleague with minimal context. Explain WHY behind a rule (Claude generalises from the reason; example: TTS engine => no ellipses). 3-5 diverse examples in <example> tags; XML tags for sections.
- Long-horizon: Claude "maintains orientation across extended sessions by focusing on incremental progress". Multi-context-window workflow: different prompt for first window (set up tests, init script), tests in structured JSON (`tests.json`) with "It is unacceptable to remove or edit tests", convenience scripts (init.sh), "consider starting with a brand new context window rather than using compaction" because latest models "are extremely effective at discovering state from the local filesystem" - and be prescriptive on restart ("Call pwd; Review progress.txt, tests.json, and the git logs; run a fundamental integration test first").
- State management: JSON for structured state, unstructured text for progress notes, git for checkpoints, explicit incremental progress.
- If the harness compacts: tell the model so ("do not stop tasks early due to token budget concerns... save your current progress and state to memory before the context window refreshes") or it may wrap up near the limit.
- Autonomy vs safety: sample prompt "Consider the reversibility and potential impact of your actions... for actions that are hard to reverse, affect shared systems, or could be destructive, ask the user before proceeding" with examples (rm -rf, force push, pushing, commenting on PRs, sending messages); "do not use destructive actions as a shortcut".
- Research: clear success criteria, verify across sources, hypothesis tree/notes file for complex research.
- Subagent orchestration: latest models orchestrate natively and "might spawn them in situations where a simpler, direct approach would suffice"; damping prompt: "Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks, sequential operations, single-file edits, or tasks where you need to maintain context across steps, work directly".
- Overeagerness: sample "Avoid over-engineering. Only make changes that are directly requested". Test-gaming: "Tests are there to verify correctness, not to define the solution... inform me rather than working around them." Hallucination guard: "Never speculate about code you have not opened."
- Migration: tune down anti-laziness prompting (4.6+ more proactive, overtriggers); keep conversation history append-only (thinking blocks must be passed back unchanged; editing earlier turns or summarising in place invalidates later thinking blocks).
## Quotable
> "consider starting with a brand new context window rather than using compaction. Claude's latest models are extremely effective at discovering state from the local filesystem."
> "Tune anti-laziness prompting: If your prompts previously encouraged the model to be more thorough or use tools more aggressively, reduce that guidance."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
