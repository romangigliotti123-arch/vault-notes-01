---
name: rbx-new-skill
description: "Make your own skill or agent for this vault folder: asks the goal in one line, checks no vault skill already does it, writes My-Skills/my-<name>/SKILL.md or My-Agents/my-<name>.md, validates it, shows its token cost and runs a 3+2 trigger self-test. Use for 'make my own skill', 'create a skill', 'make me an agent'. Updates never touch your files."
argument-hint: "[skill|agent] [what it should do]"
---

# rbx-new-skill

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Makes a skill or an agent that belongs to the USER, not to the vault. Your files live in the vault folder: `My-Skills/<name>/SKILL.md` and `My-Agents/<name>.md`. Names start with `my-` (the vault's start with `rbx-`, so they never collide). Updates, sync and uninstall never delete or overwrite them (uninstall copies them to the keep folder), they are git-excluded like `Games/`, and each is copied into `<vault>/.claude/skills|agents` so sessions in the vault see it. This skill never edits a vault-owned file.

Run the helper as `M="bash .rbx/claude-kit/tools/pyrun <this skill's folder>/scripts/my_skill.py"` (every Bash call is a fresh shell; add `--vault <folder>` only if it cannot find the vault).

## Steps
1. Goal: one line of what it should do and when. Skill or agent? Default skill (instructions Claude follows in the main chat). Agent only for a separate worker with its own tools and context (a reviewer, a checker). Ask once if unclear.
2. Overlap: `$M overlap "<goal>"` shows the 3 closest vault and own items. If one already does the job (it says OVERLAP: probably), tell the user to use that skill and stop unless they still want their own. Also glance at `/rbx-list`.
3. Research, only if the skill depends on facts: `rbx-kb` first, then official docs (create.roblox.com/docs, code.claude.com/docs), at most 3 pages. Write down nothing you did not read.
4. Start from the template: `$M new skill my-<name>` (or `new agent my-<name>`). Names: lowercase, digits, hyphens, short (`my-patch-notes`). Fill every FILL-IN marker:
   - description: at most 400 characters, key use first, concrete trigger words the user really says; different from every other description.
   - body: numbered steps with exact files and commands, short rules, no long copied text (put big reference in a second file next to it). Anything computable goes in a script, not prose. Ends with the bold footer `**Done**` / `**You**` / `**Next**`.
   - agent: `tools:` as few as possible, read-only (`Read, Grep, Glob`) unless the job truly writes; `model: sonnet` (haiku for plain lookups), `effort: medium`.
5. Validate: `$M check <path>` prints PASS/WARN/FAIL lines: frontmatter, name rule, description length, distinct triggers, bold footer, no secrets, no vault paths, tokens. It shows what this item adds to EVERY session and the session total against the 10,000 token limit (a skill costs its name and description in every chat). Fix every FAIL; tell the user about WARNs.
6. Trigger self-test: write 3 prompts that should use it and 2 that should not (near misses) and run `$M selftest <path> --yes "..." --yes "..." --yes "..." --no "..." --no "..."`. It is a word-overlap estimate; if a line FAILs, change the description and rerun.
7. Load: `$M sync` copies it into `<vault>/.claude`. Tell the user: it usually shows at once; if not, type `/reload-skills` (agents: restart the session) or start a new Claude session in the vault folder.
8. Reply (Reply format): the file path, how to call it (`/my-<name>` or by describing the job), the token cost line, the self-test result, how to change it later (edit the file in `My-Skills/`, rerun `check` and `sync`). Bold footer.

## Rules
- Never edit, copy over or delete vault-owned files (`rbx-*` skills and agents, `.claude/CLAUDE.md`, tools, rules). A wish to change a vault skill is a vault matter: say so, point to `/rbx-update` for the latest version, and offer a `my-` item of their own instead. Nothing here improves itself.
- Edit only `My-Skills/`, `My-Agents/` and their copies via `sync`. Remove an item only when the user asks: `$M remove my-<name> --yes`.
- No secrets, keys, cookies or personal data in a skill. More items cost every session; say so when the total gets above 9,000 tokens.
