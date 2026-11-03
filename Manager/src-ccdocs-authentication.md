---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/authentication.md
type: official-doc
author: Anthropic
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc, grep-read)
---
# Claude Code docs: authentication (credential storage, expiry, setup-token)
## Key claims
- Credential storage: Linux `~/.claude/.credentials.json` mode 0600; Windows `%USERPROFILE%\.claude\.credentials.json` (inherits profile ACLs); macOS Keychain, falling back to the same file when the Keychain is locked "in an SSH session". `CLAUDE_CONFIG_DIR` moves the file and keys the Keychain entry to that directory.
- A `/login` credential expires: warning at startup within 3 days ("Your login expires in 3 days - run /login to renew"); after expiry "each model request fails with Login expired"; `/status` shows a `Login` row `Expired - log in again` (v2.1.210+). "A background session in agent view or a Remote Control session that outlives the login stops making progress once the credential expires and can't recover until you sign in again." (always-on hazard for the master and for the CachyOS claude-rc.service)
- Precedence: ... `apiKeyHelper` output (for rotating/vault tokens), then `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token` ("generate a one-year OAuth token"; the command prints it, "does not save the token anywhere"; set per machine as an env var). `apiKeyHelper` slower than 10 s shows a warning; failing helper => request failures within three attempts.
- Per-device model: each device holds its own credential (own file or env var); there is no central login. Desktop/cloud sessions use OAuth only.
## Quotable
> A background session in agent view or a Remote Control session that outlives the login stops making progress once the credential expires and can't recover until you sign in again.

## Used by
[[topic-cross-device-agent-control]], [[topic-long-running-always-on-agents]]
