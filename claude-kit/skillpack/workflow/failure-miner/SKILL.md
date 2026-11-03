---
name: failure-miner
description: "Mine recent Claude Code session transcripts for the tool failures and mistakes an AI worker repeats, then fix each one at the cheapest rung of the fix ladder (remove the cause, add a check, add CI, only then add a rule or skill). Use when workers keep tripping on the same thing, before adding lines to CLAUDE.md, or after switching model."
category: workflow
tags: failures, transcripts, claude-md, lint, rules, audit, history, recurring, mistakes, steering
kb: Manager/topic-multi-agent-failure-modes.md, Manager/topic-observability.md, Manager/src-arxiv-evaluating-agentsmd.md, Manager/src-boris-cherny-tips.md, Manager/topic-context-engineering.md, Mentor/Combined-Brain.md
related: ai-brief-writer, worker-verifier, code-style-guide-writer, ci-check-setter, eval-bank, decision-log-writer, game-dev-workflow
---

# failure-miner

Workers repeat the same mistake until the cause is removed. The reflex fix is a new line in CLAUDE.md, but rule files cost tokens on every turn and a study of AGENTS.md files found generated ones do not raise success and add over 20% cost (`Manager/src-arxiv-evaluating-agentsmd.md`). This skill counts what actually fails, then fixes it at the cheapest rung that works. Method source: Theo (t3.gg, MIXED, opinion) quoting Lauren (Cursor); the "move fixes into code, add a mistake to CLAUDE.md only after a correction" part matches Boris Cherny (`Manager/src-boris-cherny-tips.md`). The ladder order is opinion, the counting is measurement.

## When to use
The same error appears in several sessions; a worker "keeps forgetting" a project rule; CLAUDE.md is growing; a new model started failing differently. Not for a one-off bug (`crash-log-reader`) or for judging a finished task (`worker-verifier`).

## Inputs (max 2)
1. Transcript folder (default: the project's folder under `~/.claude/projects/`, newest 20 sessions). 2. Optional: the model name to compare against.

## Procedure
1. Count: `python failure-miner/scripts/minefail.py <folder> --last 20 --top 15`. Read-only; transcripts are plaintext and can hold secrets, so quote only the signature line, never paste a transcript.
2. Keep the top 3 signatures that repeat in 2 or more sessions. Ignore harness blocks you cannot change (permission denials) and one-offs.
3. For each, ask the worker or read one transcript: what was it trying, what did it expect, which instruction or tool shape misled it? A tool that returns a confusing shape is a bug in the tool, not in the worker.
4. Pick the lowest rung that removes it (stop at the first that works): (1) remove the cause: rename, restructure, change the API or Rojo layout so the wrong move is hard; (2) a check that fails loudly: selene/stylua rule, Lune test, `luau-check` step, pre-commit; (3) CI or the project check script (`ci-check-setter`); (4) one line in CLAUDE.md or a skill, written as what to do, not a long "never" list; (5) a human gate. Write the ladder choice and why.
5. Apply the fix. Do not add a rule for something the worker finds by reading code in a minute.
6. Re-run step 1 on the sessions after the fix (next week); the signature count must drop. Remove a rule that no longer fires.
7. Write `docs/agent-failures.md` with headings Findings, Ladder, Next; run the check.

## Studio MCP path
None. If the top failure is an MCP call, record the tool name and the exact error; the fix is usually a call-order rule in `studio-mcp-session-planner`.

## Fallback
Without transcripts: ask the worker "list the 3 things that slowed you most and the instruction that caused each", and treat the answer as a hypothesis (`untested`).

## Evidence
`Manager/src-arxiv-evaluating-agentsmd.md` (research: context files add cost, overviews not helpful), `Manager/src-boris-cherny-tips.md` (official creator: correct, then update CLAUDE.md; edit it ruthlessly), `Manager/topic-observability.md` (transcripts are the free trace store; plaintext, sensitive), `Manager/topic-multi-agent-failure-modes.md`, creator note `theo-t3gg` "Turn off Claude Code's Memory" and "Delete your CLAUDE.md" (MIXED: audit method and ladder are his opinion, measured on his own repo only).

## Output
`docs/agent-failures.md`: Findings (signature, count, sessions), Ladder (rung chosen, why, change made), Next (date to re-count).

## Acceptance checks
- [ ] Executed: `python failure-miner/scripts/minefail.py --selftest` prints `selftest ok`.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/agent-failures.md --require "Findings,Ladder,Next" --max-lines 60 --need-evidence` prints PASS.
- [ ] Each fix names a rung number and a re-count date.
- [ ] No transcript text beyond the signature line is quoted.

## Pitfalls
Adding a rule per failure (the file grows, cost rises). Counting harness blocks as worker mistakes. Reading the model's explanation as fact (it can invent a reason; check against the transcript). Leaving the rule after the cause is gone. Comparing models on single runs.

## Related
`ai-brief-writer`, `worker-verifier`, `code-style-guide-writer`, `ci-check-setter`, `eval-bank`, `decision-log-writer`.
