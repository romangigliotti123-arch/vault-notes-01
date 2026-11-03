---
tags: [manager-kb, source]
url: https://github.com/trailofbits/claude-code-config
type: repo
author: Trail of Bits
published: undated (README read raw 2026-10-29)
accessed: 2026-10-29
reliability: high (security firm's own working config; opinionated)
---
# Trail of Bits claude-code-config (sandboxing, permissions, hooks)
## Key claims
- ToB run Claude Code with `--dangerously-skip-permissions` but only "paired with sandboxing"; "the sandbox is what keeps it from doing damage".
- Native sandbox default: writes limited to cwd, READS unrestricted (agent can still read ~/.ssh, ~/.aws), network limited to allowed domains. They ship Read/Edit deny rules for SSH/GPG keys, cloud creds, package tokens, `~/.git-credentials`, `~/.config/gh/**`; "Without `/sandbox`, deny rules only block Claude's built-in tools -- Bash commands bypass them. With `/sandbox` enabled, the same rules are enforced at the OS level".
- Devcontainer for full read+write isolation (separate repo claude-code-devcontainer; its README says filesystem isolation but not complete sandboxing, DNS still resolves unless blocked).
- Hooks: "Hooks are not a security boundary -- a prompt injection can work around them. They are structured prompt injection at opportune times ... Guardrails, not walls." Only two blocking hooks recommended as defaults: block `rm -rf` and direct push to main. Rule of thumb: "anything that must hold regardless of what Claude decides belongs in a hook", CLAUDE.md for unconditional guidance.
- Prompt-based Stop hook "anti-rationalization gate" using Haiku; must instruct raw JSON only.
## Quotable
> Hooks are not a security boundary -- a prompt injection can work around them.

## Used by
[[topic-agent-security]]
