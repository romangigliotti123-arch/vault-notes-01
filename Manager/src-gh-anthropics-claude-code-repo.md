---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-code (CLAUDE.md, examples/hooks, .claude/commands, mods/README.md)
type: repo
author: Anthropic
published: undated (main branch read 2026-10-29)
accessed: 2026-10-29
reliability: high (first-party repo, raw files read)
---
# anthropics/claude-code repository (what Anthropic itself ships as examples)
## Key claims
- The repo's own `CLAUDE.md` is tiny and holds ONLY non-derivable, safety-critical rules (3 numbered CI hardening protections: egress-firewall runner, network allow list, `--permission-mode auto` in `claude_args`), not architecture or style. Concrete example of "short CLAUDE.md": ~40 lines.
- The only hook example shipped is `examples/hooks/bash_command_validator_example.py`: reads JSON on stdin, regex rules, `sys.exit(2)` to block and print stderr to Claude; comment in source: "Exit code 1 shows stderr to the user but not to Claude" / "Exit code 2 blocks tool call and shows stderr to Claude". Pattern = fail-open on malformed input (exit 1), block only on a rule hit.
- `.claude/commands/triage-issue.md` shows Anthropic's own least-privilege agent pattern: front-matter `allowed-tools: Bash(./scripts/gh.sh:*),Bash(./scripts/edit-issue-labels.sh:*)`, with `gh.sh` a WRAPPER that "only supports these subcommands and flags" (label list, issue view, search issues) and a prompt that states hard limits in prose ("Don't post any comments ... Your only actions are adding or removing labels", "You may ONLY use labels from this list. Never invent new labels."). Tool surface is restricted by wrapper script, not by trusting the prompt.
- `mods/` documents "Claude Mods": a mod is "a Claude Code plugin whose behaviour lives in a hooks module" (TypeScript `register(on, options)`), tested with `claude plugin test`; four mods ship built in (sec-default, diff, telemetry, agents-md). `sec-default` keeps an organization's hooks/managed settings out of reach of installed plugins.
- README: npm install deprecated; native installer / winget; plugins live in anthropics/claude-plugins-official.
## Quotable
> "Exit code 2 blocks tool call and shows stderr to Claude"
> "Only supports these subcommands and flags" (scripts/gh.sh wrapper description in triage-issue.md)

## Used by
[[topic-agent-security]], [[topic-claude-code-features]]
