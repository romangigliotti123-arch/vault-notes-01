# Skill pack quality bar

Every built skill is scored against this before it is marked `built`. Machine part: `python tools/skillpack.py lint` (frontmatter, required sections, minimum length, referenced scripts exist, KB paths exist in the vault when `CLAUDES_VAULT` is set). Judgement part: the rubric below, scored 0-2 per row (max 20). Built = at least 16/20 and no row at 0; the score and the date go in `skillpack/REVIEW.md`.

## Required shape (`SKILL.md`)
Frontmatter: `name` (= folder), `description` (one or two sentences: the job, the output, when to reach for it), `category` (= parent folder), `tags`, `kb` (vault-relative KB paths, comma separated), `related` (comma separated skill names, kit skills or pack skills). Body sections, in this order, with these words in the heading: **When to use** (and when not), **Inputs** (what to ask for; defaults for the rest, never more than three questions), **Procedure** (numbered, each step an action with a stop condition), **Studio MCP path** (tool names from `rbx-studio`) and **Fallback** (command-bar Luau, Rojo files, or hand steps; says what stays `untested`), **Evidence** (KB links with the trust label: only official or TRUSTED sources are authorities; indie numbers are labelled indie), **Output** (exact files or sections produced), **Acceptance checks** (a pass/fail list the skill runs on its own output), **Pitfalls**, **Related**. Substantive Luau lives in `scripts/*.luau` and passes `tools/roblox-project-template/luau-check.sh` (stylua, selene, luau-lsp).

## Rubric (0 = missing, 1 = present but thin, 2 = solid)
1. Trigger: says when to use and when not; distinct from every other pack skill and every installed kit skill (no near-duplicate).
2. Inputs: minimal questions, sensible defaults, asks only what changes the result.
3. Procedure: concrete steps another AI can follow without guessing; each has a stop condition or check.
4. Studio MCP path: names real tools and the order of calls; does not assume a connection.
5. Fallback: complete without Studio (Rojo files, command bar, hand steps); marks what is untested.
6. Evidence: real vault paths that exist, trust labels, no invented numbers; fast-moving facts say "live-check".
7. Output: a defined deliverable format, small enough to read.
8. Acceptance checks: pass/fail list that would catch a bad result; at least one check that is executed, not asserted.
9. Code: scripts pass luau-check and carry no comments (rbx-luau, Comments; `comment_scan.py` counts them); secure by default (server authority, no secrets, no client trust); or "no code" is correct for the job.
10. Pitfalls and related: real failure modes from the KB or experience; related skills named, not duplicated.

## Rules for content
- One job per skill. If two skills share more than half their steps, merge them.
- Patterns, never copied content; never invent asset ids, pass ids, product ids or prices without a source (use `0` / `SET IN CREATOR HUB`).
- Publishing, spending Robux or money, posting as the user and changes to a live place are the user's actions: the skill prepares, the user does.
- Output must stay short: under about 150 lines for a typical run unless the deliverable is a file.
- Anything that needs a running Studio and was not run is reported `untested`.
