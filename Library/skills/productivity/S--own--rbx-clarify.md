---
id: "rbx-clarify"
type: skill
category: "productivity"
source: "own"
license: "first-party"
repo_path: "skills/productivity/rbx-clarify/SKILL.md"
description: "Asks 3-7 multiple-choice questions before building a vague request, then writes one spec with success criteria. Use when the request is vague or the user says grill me or do not assume."
orig_name: "rbx-clarify"
orig_argument_hint: "[the vague request]"
tags: [lib/skill, cat/productivity, src/own]
---

# rbx-clarify

> Asks 3-7 multiple-choice questions before building a vague request, then writes one spec with success criteria. Use when the request is vague or the user says grill me or do not assume.

Type: skill | Category: [[categories/cat-productivity|productivity]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/productivity/rbx-clarify/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--plan-then-build]]

---
# rbx-clarify

Caps questions, always offers a default, stops once the ambiguity is gone. For a one- or two-line request for a new skill, routine, automation, app or game system, or "I want X" without platform, scope, constraints or a finish check. Skip precise edits ("rename X to Y in file Z").

## Steps
1. Read the request and any project files named in it (CLAUDE.md, existing code). Do not ask what you can read.
2. List the unknowns that would change the build: goal and audience, scope (must / nice / out), platform and stack, inputs and outputs, constraints (budget, time, safety, existing code to reuse), and what done looks like (a check you can run).
3. Ask the top 3-7 questions in ONE message. Each question is multiple choice (2-4 options, plus "other") and marks a recommended default, e.g. `2) Platform: (a) browser [recommended] (b) desktop (c) Roblox Studio`. Order by how much the answer changes the build.
4. Take the answers. If a new blocking unknown appeared, ask at most one more round of 1-3 questions. Never more than two rounds in total.
5. When the user says "you pick" or does not answer, adopt the defaults and write them down as assumptions.
6. Output a consolidated spec (print it; save to the project only if asked):
   - Goal (one sentence)
   - Decisions (question -> chosen answer, defaults flagged)
   - Out of scope
   - Success criteria: 3-6 checks, each runnable or observable
   - Open risks
7. Ask once: "Build this?" Then hand off to plan-then-build or the relevant builder skill.

## Game / Roblox question bank
To score the idea afterwards use rbx-rate. [cold:rbx-clarify/game-question-bank.md] read only when the request is a Roblox game or game idea.
## Failure modes
- Question spam: more than 7 questions or open-ended essays. Cut to the ones that change the build.
- Asking things the repo already answers.
- Never converging: after round two, write assumptions and proceed.
- Silent defaults: every default must appear in the spec.

## Related
Longer interviews: rjmurillo/requirements-interview, addyosmani/interview-me (library imports). Companions: rbx-karpathy, plan-then-build.

## Sources

[cold:rbx-clarify/sources.md] read only to verify the source of this idea or its licence/attribution.
