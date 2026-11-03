---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/auto-mode-config.md (+ permission-modes.md "what the classifier blocks by default")
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Configure auto mode; human checkpoints; what is blocked by default
## Key claims
- Model support for auto mode includes Haiku 5.5 (the manager's boot model), Sonnet 4.6+/5, Opus 4.6+/5, Fable.
- `permissions.ask` content-scoped rules "are evaluated before the classifier and always force a permission prompt, even in auto mode"; `permissions.deny` "blocks before the classifier is consulted. Neither the classifier nor user intent can override it". A boundary stated only in conversation "can be lost if context compaction removes the message that stated it. Use an ask or deny rule for a durable guarantee."
- `autoMode.environment` defines trusted repos/buckets/domains (default trusts only cwd + the repo's configured remotes); `autoMode.allow`, `soft_deny`, `hard_deny` (unconditional); setting a list without `"$defaults"` REPLACES the built-ins; `autoMode.classifyAllShell:true` suspends shell allow rules; `claude auto-mode defaults|config` prints rules.
- Default blocks include: curl|bash, sending sensitive data to external endpoints, production deploys, force push, merging unreviewed PRs, printing live credentials, WRITING to `~/.claude/projects/*.jsonl` transcripts, repointing base URLs/webhooks, `git remote set-url`, opening PRs to other orgs, sensitive local stores (SSH keys, browser profiles, shell history, transcripts) entering commits/pastes/publishes, `rm -rf $VAR` with an unresolvable variable, cloud-metadata credential requests, tunnels/reverse shells, sending keystrokes to Claude's own tmux pane.
- Bash rule limits: `Bash(git push *)` does NOT stop `git -C . push`, `/usr/bin/curl`, `sh -c '...'`; "a deny or ask rule covers the invocation Claude usually produces and isn't a security boundary around the program" - use sandbox for enforcement independent of command text or a PreToolUse hook that inspects the full text.
## Quotable
> Use an ask or deny rule for a durable guarantee.

## Used by
[[topic-agent-security]]
