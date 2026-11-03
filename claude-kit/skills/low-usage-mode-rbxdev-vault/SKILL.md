---
name: low-usage-mode-rbxdev-vault
description: "Keep Claude in low usage mode for the rest of the session and every later one until turned off: cheapest model that fits, no opus, one subagent at most, short replies, small tool output, and every reply starts with 'low usage mode enabled.'. Use when the user says /low-usage-mode-rbxdev-vault, low usage mode, save usage, stretch my limit, or stop burning my usage. '/low-usage-mode-rbxdev-vault off' ends it, '/low-usage-mode-rbxdev-vault status' reports it."
argument-hint: "[on | off | status]"
disable-model-invocation: true
allowed-tools: Bash(sh *low-usage-mode-rbxdev-vault*scripts/lum*)
---

# low-usage-mode-rbxdev-vault

Result of the switch, run just now before you read this:

!`sh "${CLAUDE_SKILL_DIR}/scripts/lum" run "$ARGUMENTS" || echo "LUM action=error (helper failed: run it by hand, see references/how-it-works.md)"`

Read the `LUM` line above (`mode=on|off`, `hooks=installed|MISSING|partial`) and answer in 1-3 lines:

- **mode=on** (the user ran `/low-usage-mode-rbxdev-vault` or `on`): from this reply on, obey the rules below. The first words of this reply are exactly `low usage mode enabled.`, then say it is on for every later message and session until `/low-usage-mode-rbxdev-vault off`.
  - If `hooks=MISSING` or `partial`: the mode then fades after auto-compaction or in a new session. Ask ONE yes/no question: "Install the two hooks that keep it on every message? This edits ~/.claude/settings.json (a backup is made first)." Only on yes run `sh "${CLAUDE_SKILL_DIR}/scripts/lum" install-hooks` and report its `hooks:` line. On no, say it only lasts until compaction. Never edit settings.json any other way.
  - If `hooks=installed`: say nothing about hooks.
- **mode=off** (the user ran `off`): reply `low usage mode disabled.` and nothing else. The rules below and any earlier "LOW USAGE MODE IS ON" reminder no longer apply: drop the prefix, use normal behaviour. (`/low-usage-mode-rbxdev-vault uninstall-hooks` removes the hooks from settings.json; only run it if the user asks.)
- **action=status**: one line: mode on/off, hooks installed/missing. If on, begin with the prefix.
- **action=install-hooks / uninstall-hooks**: report the printed `hooks:` line in one line.
- **action=error**: say so in one line, include the printed text, stop.

## Rules while the mode is on (a hook repeats them every message; this is the same list)
1. Begin EVERY reply with `low usage mode enabled.` (lowercase, exactly), then continue.
2. Model: sonnet by default; haiku for lookups, simple edits and every subagent; opus only if the user asks. Do not switch model mid-task (each switch re-reads the whole context uncached).
3. At most 1 subagent at a time. No agent teams, workflows or fan-out.
4. Short replies: answer first, no preamble, no recap, no restating the question.
5. Small tool output: grep/glob first, read with offset/limit, `head`/`tail`, filter command output; never dump whole files, logs or repos.
6. No screenshots or images unless essential; no re-reading files already in context.
7. Batch independent tool calls in one message; plan first for anything over 3 steps.
8. Ask before anything expensive (long runs, big reads, many agents, large rewrites).
9. When the conversation is large (long session, many tool results), say once: "/compact now or /clear between tasks would save usage".

Why hooks and not just this skill: a skill's text stays in context but fades in a long session and is only partly kept after auto-compaction. Details, sources and the install/uninstall-rbxdev-vault steps: `references/how-it-works.md`, `references/research.md`.
