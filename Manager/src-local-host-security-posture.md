---
tags: [manager-kb, source]
url: local probes on [host] (settings.json, boot-claude.ps1, run-as-system.ps1, tools\*.ps1, icacls), 2026-10-29
type: local-audit
author: F1 research worker
published: 2026-10-29
accessed: 2026-10-29
reliability: high (direct reads; read-only probes)
---
# Local audit: security posture of the manager host
## Key claims
- Master runs as elevated admin `[host]\roman` with `--dangerously-skip-permissions` (boot-claude.ps1 passes it; settings.json also has `skipDangerousModePermissionPrompt:true`, `defaultMode:auto`). No `hooks`, no `permissions.deny/ask` in ~/.claude/settings.json; settings.local.json only has allow rules (ineffective in bypass).
- Windows native: no Claude Code sandbox possible (docs). `wsl --status` exit 50 (WSL not usable), `HypervisorPresent=False`: no WSL2/Hyper-V/Windows Sandbox option on this box. Only one enabled local user (`roman`, admin); built-in Administrator disabled.
- Defender exclusions cover `~\.claude`, `~\.local\bin`, `...\Temp\claude`, `claude-host` (the places agent-written code and imported skills live are NOT scanned).
- `run-as-system.ps1` writes arbitrary text to `claude-host\system-cmd.ps1` and starts scheduled task `ClaudeSystemRun`, which runs it as SYSTEM. Anything that can write that file (any process of user roman) gets SYSTEM. Task `ClaudeHost` (elevated) restarts the master.
- Secrets at rest: `[private-path]` (ACL: Administrators, SYSTEM, roman); `[private-path]` (72 bytes, ACL roman+SYSTEM); gh token via `gh auth token` (repo, read:org, gist scopes). All readable by the bypass-mode agent; transcripts store tool output in plaintext 30 days.
- Inbound channels: Telegram plugin (see [[src-local-telegram-plugin-gate-audit]]); Discord voice bot `claude-host\discord-voice` (single `ownerId` gate on voice, text commands reject non-owner, logs utterances to a file); Remote Control (claude.ai account auth). Tailscale ACL "accept" for SSH to CachyOS; key `[private-path]` authorised there with passwordless sudo.
- The library holds ~5,600 imported third-party skills/agents (CLAUDE.md); Snyk found 13.4% of 3,984 public skills with a critical-level issue and 76 (1.9%) confirmed malicious; the USENIX study found 157 of 98,380 (0.16%) confirmed malicious ([[src-snyk-toxicskills]], [[src-arxiv-malicious-agent-skills]]). Rates differ by registry and method; the library's provenance (which source repos) decides its risk.
- Tools: `cachyos-run.ps1` (pipes arbitrary bash to `ssh cachyos`, plain-text output, `[stderr]` marker, `TIMED OUT` string, no exit code), `linux-power.ps1` (sleep/wake/status via ValidateSet, prose output), `send-telegram.ps1` (token read from .env, never printed; hard-coded chat id).

## Used by
[[topic-agent-security]], [[topic-tool-and-mcp-design]]
