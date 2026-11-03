---
tags: [manager-kb, source]
url: https://man.openbsd.org/sshd.8
type: official-doc
author: OpenBSD / OpenSSH project
published: undated (man page)
accessed: 2026-10-29
reliability: high (upstream manual)
---
# sshd(8) AUTHORIZED_KEYS FILE FORMAT
## Key claims
- Per-key options usable to scope an agent key: `restrict` (disable port/agent/X11 forwarding, PTY allocation and ~/.ssh/rc; future restrictions included automatically), `command="..."` (forced command; client command ignored but available as `SSH_ORIGINAL_COMMAND`), `from="pattern-list"` (source address allow-list), `expiry-time="YYYYMMDD[Z]"`, `permitopen="host:port"`, `no-pty`, `verify-required` (FIDO keys, require PIN), `principals=` with `cert-authority` for CA-signed certificates.
- "Note that the client may specify TCP and/or X11 forwarding unless they are explicitly prohibited, e.g. using the restrict key option" - a forced command alone is not a sandbox.
- Certificates can embed restrictions; "If both certificate restrictions and key options are present, the most restrictive union of the two is applied."
- Example: `restrict,command="dump /home" ssh-rsa ...` for a backup-only key.
## Quotable
> Note that the client may specify TCP and/or X11 forwarding unless they are explicitly prohibited, e.g. using the restrict key option.

## Used by
[[topic-cross-device-agent-control]]
