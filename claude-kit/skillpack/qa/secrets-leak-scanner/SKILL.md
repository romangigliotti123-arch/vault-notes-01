---
name: secrets-leak-scanner
description: "Scan a project folder or exported place text for API keys, Open Cloud keys, webhook URLs, tokens, passwords, private keys, secrets in TeleportData and admin UserId lists in client-readable scripts, with redacted output. Use before pushing a repo, publishing a place or sharing a project, and after any suspected leak."
category: qa
tags: secrets, api key, open cloud, webhook, token, password, leak, repo, security scan, redaction, teleportdata
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md, Mentor/Combined-Brain.md
related: exploit-audit, server-authority-checker, publish-readiness-gate, asset-license-checker, rbx-remote-sec
---

# secrets-leak-scanner

Anything in a client-readable container, a public repo or a shared file is public. This skill scans text for secrets and server-only data using `scripts/SecretScan.luau` (pattern rules with placeholder filtering, tested) and a folder runner `scripts/scan_folder.luau`. Findings are REDACTED (first three characters plus length): the scan never prints a real secret, and neither may you.

## When to use
Before `git push`, publishing, sharing a place file or project zip, handing work to a collaborator, or after an incident. Not for: code-level exploit audits (`exploit-audit`), asset ownership (`asset-license-checker`), or scanning credentials stores outside the project (never read credential files).

## Inputs (max 2)
1. The folder to scan (default: the project root, excluding `.git`, `Packages`, `node_modules`). 2. Whether it will be public (default: assume yes).

## Procedure
1. Run `lune run ../skillpack/qa/secrets-leak-scanner/scripts/scan_folder.luau <folder>` from `claude-kit/systems` (Lune finds its tools there; give the folder as a full path). It walks text files (`.luau .lua .json .toml .yml .yaml .md .txt .env .ini .rbxlx .rbxmx`), prints `scanned N files` and a redacted findings list, and exits 1 on any CRITICAL or HIGH finding.
2. Read each finding with its file:line. Rules: Discord webhook URL, bearer token, private key block, `x-api-key` literal (CRITICAL); `?key=` in a URL, secret/token/apikey/password assignments to long non-placeholder strings (HIGH); `SetTeleportData` with secret-looking field names (MEDIUM: TeleportData is visible to clients and unencrypted); admin/owner/banned UserId lists in client-readable scripts (MEDIUM).
3. Real secret found: ROTATE it first (revoke the key/webhook, create a new one), then remove it from the code and, if committed, from history (that rewrite is the owner's action). Removing a leaked secret without rotating it does nothing.
4. Fix pattern: server-side only. Open Cloud keys and webhooks live in server scripts or an external backend; use Roblox Secrets (live-check availability) or environment variables for backends; scope Open Cloud keys narrowly (separate create from update, restrict by data store, set an expiry); never put a key in `ReplicatedStorage`, `StarterGui`, `Workspace` or a LocalScript; do not pass secure data through TeleportData.
5. Move client-readable admin lists to a server-only module; compare `UserId` on the server for every admin action.
6. Place and model files: also open `.rbxlx` exports as text, search free models for `require(<number>)`, `loadstring` and HTTP calls to unknown hosts (a backdoor is a secret leak in reverse; see `exploit-audit`).
7. Re-run until clean; add the scan to the pre-push checklist. A clean scan is NOT proof (heuristics): say so.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) iterating `GetDescendants()` for `LuaSourceContainer`s, passing `(GetFullName(), Source)` to `SecretScan.scanText` and `scanClientVisible` pasted inline -> report redacted findings only -> `multi_edit` to remove literals.

## Fallback
Rojo/file projects: the folder runner above. Without Lune: `grep -rnE "x-api-key|webhooks/|BEGIN .*PRIV​ATE KEY|[Ss]ecret *= *[\"']" .` and read results locally, redacting before you report. Binary place files are not scanned.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: keep secrets out of client-visible channels (never pass secure data in TeleportData: visible to clients, unencrypted); lock down Open Cloud and API credentials (server-side only, key in the `x-api-key` header, minimal scopes, restrict by data store); secure webhooks with signature, timestamp and dedupe; keep authoritative logic in server-only containers; assume anything on the client is exposed. Trust: official docs and DevForum, labelled.

## Output
```
SECRETS SCAN <folder> <date>: files N, findings M (values redacted)
| severity | rule | file:line | preview |
Rotation needed: yes/no (list which key/webhook)   Unchecked: binary files, history, other machines
```

## Acceptance checks
- [ ] `lune run` of the SecretScan test prints "8 passed, 0 failed".
- [ ] The folder scan ran and printed `scanned N files` with N > 0.
- [ ] No finding or report contains a full secret value.
- [ ] Every real secret has a rotation note; removal alone is not accepted.
- [ ] Clean-scan claims say "heuristic, not proof" and list what was not scanned.

## Pitfalls
Fixing the file but not rotating the key. Pasting the secret into the report. Treating `ReplicatedStorage` as private. Trusting obfuscation. Scanning only the working tree while the key sits in git history. Printing credential files from the machine "to check".

## Related
`exploit-audit`, `server-authority-checker`, `publish-readiness-gate`, `asset-license-checker`.
