---
name: rbx-karpathy
description: "Installs and applies four coding-agent rules in a project CLAUDE.md: think before coding, simplicity first, surgical changes, goal-driven execution. Use for bloated or unrelated agent edits and smaller diffs."
argument-hint: "[install | check <diff>]"
---

# rbx-karpathy

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

[cold:rbx-karpathy/sources.md] read only to verify the source of this idea or its licence/attribution.