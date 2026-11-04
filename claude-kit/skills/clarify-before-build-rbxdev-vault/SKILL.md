---
name: clarify-before-build-rbxdev-vault
description: "Asks 3-7 short multiple-choice clarifying questions (each with a recommended default) before building a vague request, loops until the definition of done is clear, then outputs one consolidated spec with success criteria. Use when the request is vague, before a new skill, project, automation or game system, or when the user says grill me or do not assume."
argument-hint: "[the vague request]"
---

# clarify-before-build-rbxdev-vault

Stops the agent from building on wrong assumptions. Short on purpose: it caps the number of questions, always offers a default, and stops asking once the ambiguity is gone. Not for trivial fixes where the request is already specific.

## When to use
- New skill, routine, automation, app, or game system and the request is one or two lines.
- The user says "I want X" without platform, scope, constraints or a way to tell it is finished.
- Skip when the task is a precise edit ("rename X to Y in file Z").

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
Genre and target player age; core loop in one sentence; solo or multiplayer; session length; monetisation allowed (passes, products, none); art source (own, free assets, blocks); data persistence needed; target platforms (PC, mobile, console); how a playtest decides "fun enough". To score the idea afterwards use game-dev-rate.

## Failure modes
- Question spam: more than 7 questions or open-ended essays. Cut to the ones that change the build.
- Asking things the repo already answers.
- Never converging: after round two, write assumptions and proceed.
- Silent defaults: every default must appear in the spec.

## Related
Longer product interviews: rjmurillo/requirements-interview and addyosmani/interview-me (library imports); this skill is the 2-minute gate. Companions: karpathy-coding-guidelines-rbxdev-vault (rule "think before coding"), plan-then-build.

## Sources
Idea from AI-creator research (catalogue ideas idea-0008, idea-0116). Credit and where it appears:
- Nate Herk, "Build & Sell with Claude Code (10+ Hour Course)" (2026-03-12) @ 8:00:49, https://www.youtube.com/watch?v=mpALXah_PBg&t=28849s. Seen there as: Ask-until-95%-confident pattern
- RoboNuggets (Jay E), "7 Claude Code skills I use every single day (Advanced Tutorial)" (2026-05-12) @ 8:48, https://www.youtube.com/watch?v=UpgjdQJShWg&t=528s. Seen there as: align
- Nate Herk, "How to Use Claude Code Better Than 98% of People" (2026-06-18) @ 21:49, https://www.youtube.com/watch?v=RzLV8sfFdMM&t=1309s. Seen there as: Grill-me skill (Matt Pocock)
- RoboNuggets (Jay E), "Claude Fable 5 Destroys Every Mobile App Designer" (2026-06-10) @ 6:31, https://www.youtube.com/watch?v=k2VtfRCgXJI&t=391s. Seen there as: align skill
- Nate Herk, "Build & Sell Grok Bots (2 Hour Course)" (2026-08-31) @ 34:04, https://www.youtube.com/watch?v=4hKJ9X6rGFo&t=2044s. Seen there as: Ask-until-clear interview prompt
- RoboNuggets (Jay E), "Fable + Sol is a CHEAT CODE for Claude Code (Cheaper, more Powerful)" (2026-07-15) @ 4:45, https://www.youtube.com/watch?v=4kRdt18_dFY&t=285s. Seen there as: /align
- Nate Herk, "18 Claude Code Token Hacks in 18 Minutes" (2026-04-02) @ 5:07, https://www.youtube.com/watch?v=49V-5Ock8LU&t=307s. Seen there as: Confidence-gate plan mode rule
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.


## Triggers (moved out of the description)

Use when the request is vague, before starting a new skill, project, automation, routine or Roblox/game system, or when the user says ask me questions first, grill me, interview me, clarify before you build, make sure you understand, or do not assume.
