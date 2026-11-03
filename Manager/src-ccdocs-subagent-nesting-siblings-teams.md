---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/sub-agents.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs fetched 2026-10-29; also agent-teams.md)
accessed: 2026-10-29
reliability: high (primary docs, grep-read; complements [[src-ccdocs-sub-agents]] and [[src-ccdocs-subagents]])
---
# Claude Code docs: nesting, concurrency, sibling messaging, background results, agent teams (details verified for orchestration-pattern design)
## Key claims
- **Depth**: "a subagent can spawn subagents of its own, up to three layers below the main conversation. At the depth limit, Claude Code withholds the `Agent` tool from every subagent except a fork." `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` changes it (1 = nesting off). Omit `Agent` from a subagent's `tools` to stop it spawning. In an interactive session a spawning subagent waits for nested subagents' reports so only the top-level subagent's summary returns to the main thread; in `claude -p`/SDK it waits only if fork mode is on, otherwise nested ones start in the background and report to the main conversation if they outlast the parent.
- **Concurrency**: at 20 running subagents, spawning another fails with `Concurrent subagent limit reached` (error tells Claude not to retry); `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` changes it; no cap on total count.
- **Background by default**: a subagent Claude spawns from the main conversation starts in the background (interactive: fork mode on by default means Claude cannot wait inline). "A background subagent's results reach Claude as a completion notification in a later turn." Background subagents get a smaller built-in tool set and surface every permission prompt in the main session. API errors: foreground returns partial output with a note; background marks failed and includes last output.
- **Context at start**: a non-fork subagent sees only its system prompt, the task message the parent writes, the CLAUDE.md hierarchy (unless `omitClaudeMd`), git status, preloaded skills, and a **sibling roster**. It does not see the conversation, the parent's skills, auto memory, or output style. "The main conversation still has your full CLAUDE.md ... restate it in the prompt you give Claude when delegating."
- **Siblings CAN message each other (nuance to the 'workers cannot talk' assumption)**: "Sibling roster: a system reminder listing `main` and every other named agent in the session, each a valid `to` value for `SendMessage`. The roster appears only when the subagent's tools include `SendMessage` and at least one other agent has a name." Snapshot at subagent start (later-named agents do not appear). So peer messaging is technically possible for named agents given SendMessage; it is not the default and no doc recommends it for coordination.
- **Resume**: `SendMessage` with agent ID/name resumes a finished subagent with full history; Explore and Plan are one-shot (no ID); a subagent stopped at `maxTurns` returns partial output and can be resumed.
- **Output scanning**: every subagent report is scanned before the parent reads it; text imitating system tags or `Human:` lines gets a backslash inserted. Relevant to injection from worker-read web pages.
- **Agent teams** (experimental, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`): teammates are separate instances with a shared task list (with dependencies), mailbox JSON files at `~/.claude/teams/{team}/inboxes/{agent}.json`, direct teammate messaging. Limits: one team per session, no nested teams (teammates cannot spawn teammates), no resume of in-process teammates after `/resume`. "Agent teams add coordination overhead and use significantly more tokens than a single session ... For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective." Gotcha: with teams enabled, a named subagent spawned from the main conversation launches as a teammate instead.

## Used by
[[topic-claude-code-features]], [[topic-orchestration-patterns]]
