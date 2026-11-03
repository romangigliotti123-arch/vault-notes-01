---
name: eval-bank
description: "Keep a small bank of your own real, already-solved problems (frozen code state, the info a worker would need, the known correct fix, a pass/fail check) and rerun it when the AI model, CLAUDE.md or skills change, so you learn whether the setup got better or worse on your game. Use when a new model or big instruction change lands, or before trusting a model with riskier jobs."
category: workflow
tags: eval, benchmark, regression, model-change, repro, held-out, bank, private-benchmark
kb: Manager/topic-llm-judge-and-adversarial-verification.md, Manager/src-anthropic-demystifying-evals.md, Manager/src-anthropic-ai-resistant-evals.md, Manager/topic-model-effort-routing-cost.md, Mentor/Combined-Brain.md
related: failure-miner, worker-verifier, repro-step-writer, regression-checklist-builder, usage-budgeter, game-dev-workflow
---

# eval-bank

Public benchmarks say little about your Luau project. Your own solved bugs are a better test: you know the answer and can check it. The bank is a folder of cases; a rerun tells you whether a new model or a changed instruction file helps. Method source: Theo (MIXED, opinion; he keeps a private held-out set because labs train on public ones) and the official eval guidance in `Manager/src-anthropic-demystifying-evals.md`. Keep it tiny: 5 cases beat 50 stale ones.

## When to use
A new model is released, you cut or rewrote CLAUDE.md or skills, or you plan to hand a model a riskier job. Not for QA of the game itself (`regression-checklist-builder`) or judging one task (`worker-verifier`).

## Inputs (max 2)
1. A bug or task you already fixed (default: the last three from `docs/decisions.md` or git log). 2. Which setups to compare (default: current vs changed).

## Procedure
1. For one solved problem create `evals/<id>/` with: `state` (git commit or tag BEFORE the fix; never the fixed one), `info.md` (exactly what you knew when you started: error text, log lines, the thing you tried), `check` (one command that fails before the fix and passes after: a Lune test, a script exit code), `answer.md` (your fix, for the grader only, never shown to the worker).
2. Keep cases that are real, small (under 10 minutes for you), deterministic and not too easy. Drop a case if the check is flaky.
3. Run: for each setup, check out `state` in a clean worktree, give the worker `info.md` only, cap steps and spend, then run `check`. Record pass/fail, tool calls, cost and wall time in `evals/results.md`.
4. Run each case at least twice per setup; one run proves nothing (the same prompt varies in time and result).
5. Compare per case: pass rate, then cost. Do not average across different difficulty. A change that passes fewer cases is rolled back; one that passes the same and costs less is kept.
6. Never put `answer.md`, the case ids or the check text in CLAUDE.md or a skill (the setup would be tuned to the test); rotate in a new case each month.
7. Add a case whenever a new real failure is solved (`failure-miner` feeds this).

## Studio MCP path
Cases that need Studio are marked `needs-studio` and run serially; prefer cases checkable from files and Lune.

## Fallback
No worktree support: copy the project at the `state` commit into a temp folder. No automated check: the grader runs the manual steps from `answer.md` and records `untested` for automation.

## Evidence
`Manager/src-anthropic-demystifying-evals.md` (official: task, graders, repeat runs), `Manager/src-anthropic-ai-resistant-evals.md`, `Manager/topic-llm-judge-and-adversarial-verification.md` (held-out checks against gaming), creator notes `theo-t3gg` "AI mistakes you're probably making" and "How to give Claude unlimited usage" (MIXED: personal practice, no measured outcome).

## Output
`evals/results.md`: one row per case and setup with pass/fail, runs, cost, notes; one line of verdict.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py evals/results.md --require "Setup,Case,Verdict" --max-lines 60 --need-evidence` prints PASS.
- [ ] Each case has a check that fails on `state` and passes on the fix (both runs recorded).
- [ ] Each case ran at least twice per setup.
- [ ] No answer text appears in any instruction file.

## Pitfalls
Using the fixed commit as `state`. Leaking the answer into CLAUDE.md. Cases that are really about luck. Comparing single runs. Treating a small bank as a ranking of models: it measures your setup on your game only.

## Related
`failure-miner`, `worker-verifier`, `repro-step-writer`, `usage-budgeter`.
