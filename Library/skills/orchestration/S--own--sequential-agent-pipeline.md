---
id: "sequential-agent-pipeline"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/sequential-agent-pipeline/SKILL.md"
description: "Runs a multi-stage task as separate small agents or sessions in order (for example research, then draft, then polish, then send), passing only the previous stage's output forward, with a per-stage prompt and model and a clear between phases; reduces tool-calling errors and hallucination compared with one agent doing everything. Use when one agent keeps making tool errors or inventing facts on a long task, or when the user says chain these steps, pipeline, stage by stage, research then draft then edit, or break this into stages."
orig_name: "sequential-agent-pipeline"
orig_argument_hint: "<the task and its stages>"
tags: [lib/skill, cat/orchestration, src/own]
---

# sequential-agent-pipeline

> Runs a multi-stage task as separate small agents or sessions in order (for example research, then draft, then polish, then send), passing only the previous stage's output forward, with a per-stage prompt and model and a clear between phases; reduces tool-calling errors and hallucination compared with one agent doing everything. Use when one agent keeps making tool errors or inventing facts on a long task, or when the user says chain these steps, pipeline, stage by stage, research then draft then edit, or break this into stages.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/sequential-agent-pipeline/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--phased-build-orchestrator]], [[S--own--confidence-escalation-router]]

Creator videos (notes are in the AI Library Vault, Creators/videos): 2025-02-01-openai-fires-back-at-deepseek-with-a-new-reasoning-model-o3, 2025-02-10-4-agentic-frameworks-for-more-efficient-workflows-in-n8n, 2026-06-10-i-turned-claude-into-the-ultimate-second-brain

---
# sequential-agent-pipeline

One agent with many tools and a long task drifts. A chain of narrow stages is smaller, checkable and cheaper.

## When to use
- The task has natural stages with distinct tools (search, write, format, send).
- A single agent has produced tool-calling errors or fabricated details.
- Not when stages need to talk back and forth many times (use a single agent or a team).

## Steps
1. **Define stages**: for each, a name, its single job, input (the previous stage's file), output (file path + format), tools allowed, model (cheap for mechanical, stronger for judgment), and a check.
2. **Create a work folder** (e.g. `pipeline/<run-id>/`) with `01-research.md`, `02-draft.md`, ... Each stage reads only the previous file plus the original request.
3. **Run in order**. Per stage: spawn a subagent (or start a fresh session / `/clear`), give it the stage prompt and input file, require it to write the output file and a 3-line status. Check the output against the stage check before moving on. On failure retry once with the failure text; then stop and report which stage failed.
4. **Side effects last**: anything that sends, posts, pays or deletes is its own final stage and needs the user's confirmation unless pre-authorised.
5. **Deliver**: final artifact path, plus the intermediate files so any stage can be rerun alone.

## Example stage table
| # | Stage | Input | Output | Model | Check |
|---|-------|-------|--------|-------|-------|
| 1 | Research | request | 01-research.md with sources | cheap | every claim has a link |
| 2 | Draft | 01 | 02-draft.md | stronger | covers all asked points |
| 3 | Polish | 02 | 03-final.md | cheap | length and tone limits |
| 4 | Send | 03 | sent log | cheap | user confirmed |

## Failure modes
- Information loss between stages: put required facts into the output file explicitly.
- Stage creep: a stage that needs a tool from another stage means the split is wrong.
- Silent failures: never pass an unchecked output forward.

## Related
confidence-escalation-router, phased-build-orchestrator (parallel build), automation-design-framework (decide which stages are plain code).

## Sources
Idea from AI-creator research (catalogue ideas idea-0097). Credit and where it appears:
- Nate Herk, "OpenAI Fires Back at DeepSeek With a New Reasoning Model: o3-mini (n8n AI Agent)" (2025-02-01) @ 8:46, https://www.youtube.com/watch?v=IBaT-XQm_wE&t=526s. Seen there as: Linear multi-agent travel planner (suggested future build)
- Nate Herk, "4 Agentic Frameworks for More Efficient Workflows in n8n" (2025-02-10) @ 1:42, https://www.youtube.com/watch?v=nSQnJoqK4DQ&t=102s. Seen there as: Prompt chaining pattern
- Nate Herk, "I Turned Claude Into the Ultimate Second Brain" (2026-06-10) @ 18:52, https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1132s. Seen there as: Specialized assembly-line agents
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
