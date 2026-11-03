---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/plugins/mods/overview.md (+ plugins/mods/events.md; remote-control.md limitations)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (Claude Mods introduced v2.1.287, Oct 2026; fetched raw .md)
accessed: 2026-10-29
reliability: high (official; newest and least battle-tested feature)
---
# Claude Mods (in-process plugin hooks) and what Remote Control forwards
## Key claims
- A mod is "a plugin that changes how Claude Code looks and behaves", made of JS/TS event handlers (`register(on, options)`) running INSIDE Claude Code with the user's permissions ("code that runs with your permissions. It can read and write your files, start processes, and make network requests"). Install like any plugin (`/plugin install x@marketplace`, `claude plugin install`); `/reload-plugins` after a shell install. Anthropic sample mods in `anthropics/claude-code-playground/claude-code/mods`: `token-weather` (context forecast), `blast-radius` ("holds a risky shell command, such as `rm -rf` or a force push, and shows what it would change, with buttons to proceed or cancel"), `replay-theater`.
- Capabilities beyond settings hooks: hold a tool call and ask the user (`$.ui.ask`) before calling `next(e)`, rewrite arguments, retry, answer a call without running it, withhold results, redirect a request to another model, run `/commands` with no Claude turn, share state across hooks. `tool.call` fires for subagent and MCP calls too; `tool.check` fires after PreToolUse hooks and before permission prompt / classifier. Failure semantics: a throwing or timing-out mod hook is SKIPPED (fail-open) unless a `.catch` handler is added.
- Official guidance on when NOT to use code: "For a fixed command or path, use a permission rule such as `Bash(npm test)`, which takes no code. Handle `tool.check` when the decision depends on what's true at that moment, such as the current Git branch".
- Where mods run: hooks run in terminal, Desktop, VS Code, `claude -p` and Agent SDK, and Remote Control ("Yes, in the session on your machine"); drawing appears in the terminal on the host machine only, not on the phone. Not in WSL Desktop sessions or (without reaching the cloud) cloud sessions.
- Remote Control forwards permission prompts and `AskUserQuestion` to the phone/web and keeps them open until answered (other forwarded dialogs expire after 5 min, `dialogExpiry`); phone push for "actions required" is enabled via `/config` ("Push when actions required"); push skipped while typing at the terminal unless `CLAUDE_CLIENT_PRESENCE_FILE` marker exists. Commands like `/plugin`, `/resume`, `/skill-doctor`, `/claude-api` are local-only.
- Managed settings can block/govern mods (`sec-default` built-in mod keeps org hooks out of reach of installed plugins); third-party mod bundles (e.g. ruflo-mods) are unreviewed code with account permissions.
## Quotable
> "A mod is code that runs with your permissions."
> "Handle `tool.check` when the decision depends on what's true at that moment"

## Used by
[[topic-claude-code-features]]
