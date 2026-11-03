---
id: "publish-now"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/publish-now/SKILL.md"
description: "Last step of any task that adds or changes a skill, agent, library item, vault note or setup doc: run publish-now.ps1 to index, secret-scan, commit, push the library, rebuild the Obsidian vault and push it to GitHub and the Tailscale share."
orig_name: "publish-now"
tags: [lib/skill, cat/orchestration, src/own]
---

# publish-now

> Last step of any task that adds or changes a skill, agent, library item, vault note or setup doc: run publish-now.ps1 to index, secret-scan, commit, push the library, rebuild the Obsidian vault and push it to GitHub and the Tailscale share.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/publish-now/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# publish-now

Roman pulls everything from any computer, so changes must be published immediately, not left local.

Run as the LAST step of a task that touched claude-library, the vault, or a setup doc:
```
powershell -File ~\claude-host\tools\publish-now.ps1 [-Message "<commit msg>"] [-Force] [-SkipVault] [-SkipLibrary]
```
- Library: build-index, `git add -A`, secret scan of added lines (GitHub tokens, private-key headers, github​_pat_, Anthropic and AWS key prefixes, .env files; aborts and lists file + pattern, never the match), commit, `pull --rebase` if behind, push.
- Vault: sync-vault.ps1 only if the library changed or `-Force` (about 4 min); then push-vault.ps1 (private repo claudes-vault, mirrored to S:\share\vault.git when S: is present). Waits up to 3 min for a fresh `vault-sync.lock`; only deletes locks older than 30 min.
- Output: library commit, vault commit, share HEAD, what ran, `ERROR:` lines; exit 1 on failure. Running it twice is a no-op the second time (about 1 min, mostly the vault mirror copy).
- The task ClaudeVaultPush also pushes the vault every 15 min with no end date; publish-now just does it right now.
- On a secret hit: remove the secret from the file, run again. Do not bypass the scan.
