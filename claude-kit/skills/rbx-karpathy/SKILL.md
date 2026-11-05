---
name: rbx-karpathy
description: "Installs and applies four coding-agent rules in a project CLAUDE.md: think before coding, simplicity first, surgical changes, goal-driven execution. Use for bloated or unrelated agent edits and smaller diffs."
argument-hint: "[install | check <diff>]"
---

# rbx-karpathy

Four rules that target the most common agent mistakes, popularised as a single CLAUDE.md file after Andrej Karpathy's observations about LLM coding agents. Under one page, testable with demo prompts, easy to extend with project conventions.

## The rules (paste block)
1. **Think before coding.** State assumptions. If the request has more than one reasonable reading or an inconsistency, surface it and ask instead of picking silently. Say what is unclear.
2. **Simplicity first.** Write the minimum code that solves the stated problem. No speculative features, abstractions for one use, config for things nobody asked for, or defensive code for impossible cases. If you wrote 200 lines and 50 would do, rewrite.
3. **Surgical changes.** Change only what the request needs. Do not reformat, rename, delete existing comments (your own new code gets none: rbx-luau, Comments), or "improve" neighbouring code. Match the existing style. Mention unrelated problems instead of fixing them. Remove only the dead code your own change created.
4. **Goal-driven execution.** Turn the task into verifiable success criteria ("write a test that reproduces the bug, then make it pass"), then loop until the checks pass. Declare the end state, not the steps.

## Install mode
1. Read the project CLAUDE.md (create via claude-md-project-bootstrap if absent).
2. Append the block above under `## Coding behaviour` unless an equivalent exists; if the file already has similar rules, merge and show the diff.
3. Keep it short; link project conventions rather than inlining.

## Check mode (review a diff against the rules)
For each hunk: is it required by the request (rule 3)? Is there a simpler version (rule 2)? Were assumptions stated (rule 1)? Is there a check that proves it works (rule 4)? Output a table: hunk | rule broken | smaller alternative. Mark clean diffs clean.

## Demo to verify the install
Ask for a one-line UI change (a colour or a toggle). Expect: an assumption note or question first, a diff of a few lines, no unrelated edits, a stated check.

## Failure modes
- Rule 1 turns into question spam: only ask when the answer changes the result.
- Rule 3 blocks a needed refactor: the user can say "refactor allowed" for the task.

## Related
rbx-clarify, plan-then-build, code-review-checklist.

## Sources
Idea from AI-creator research (catalogue ideas idea-0046). Credit and where it appears:
- Nate Herk, "Build ANYTHING with Claude Code & n8n (Beginner's Guide)" (2026-01-16) @ 5:00-9:10, https://www.youtube.com/watch?v=OCO3aq3G0mk&t=300s. Seen there as: claude.md project system prompt
- RoboNuggets (Jay E), "The Karpathy CLAUDE.md File That 43,000 Developers Installed in 1 Week (Full Breakdown)" (2026-04-16) @ 1:20, https://www.youtube.com/watch?v=d8BGxfW3Vj4&t=80s. Seen there as: Karpathy CLAUDE.md four-principle guideline file
- RoboNuggets (Jay E), "Claude Web Design just got a MAJOR upgrade (Impeccable v3)" (2026-05-08) @ 4:19, https://www.youtube.com/watch?v=hicdJVLnp-Q&t=259s. Seen there as: Personalized Impeccable setup skill
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
