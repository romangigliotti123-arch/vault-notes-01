---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/sandboxing.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Claude Code docs: Sandboxing
## Key claims
- OS-enforced boundary around Bash/PowerShell/Monitor commands and children. Off by default. macOS Seatbelt; Linux and WSL2 bubblewrap+socat; WSL1 unsupported.
- NATIVE WINDOWS: "On native Windows, Claude Code runs commands unsandboxed." Sandboxing needs WSL2. (This host is native Windows, no hypervisor present per local probe.)
- Default FS policy: writes to working dir + temp; READS most of the machine including ~/.ssh and ~/.aws; protect credentials explicitly (`sandbox.credentials`, `filesystem.denyRead`).
- Protected paths (settings, hooks, skills, `.mcp.json`, shell startup, `.git` hooks/config) are write-denied so a command cannot grant itself permissions or add an unsandboxed hook.
- Network: all traffic via proxy with allowed domains (starts empty). In `bypassPermissions` mode non-listed hosts are allowed WITHOUT prompt unless `strictAllowlist`/`allowManagedDomainsOnly`.
- Escape hatch `dangerouslyDisableSandbox` retries unsandboxed; disable with `allowUnsandboxedCommands:false`. `excludedCommands` run with full access.
- Not sandboxed: Read/Edit/WebFetch tools, hooks, local MCP servers, LSP, status line. Fail-open by default if sandbox cannot start; set `failIfUnavailable:true` for a hard guarantee.
## Quotable
> By default, if the sandbox can't start because a dependency is missing or the platform is unsupported, Claude Code runs commands without sandboxing.

## Used by
[[topic-agent-security]]
