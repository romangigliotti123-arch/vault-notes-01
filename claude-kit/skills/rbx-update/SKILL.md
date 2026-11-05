---
name: rbx-update
description: "Update the claudes-vault and the AI Library Vault on demand: self-healing git update (local changes saved to a patch), refresh the installed kit (skills and agents stay OFF in normal sessions), sync Assets (about 1 GB first time). Use for /rbx-update, 'update the vault', stale vault content."
---

# rbx-update

The vault no longer polls every 15 minutes: it updates at logon and when you run this. Run it now, without questions.

1. Find the vault (first existing wins): `$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`. None: follow the setup runbook instead: `curl -fsSL https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md` (Roman's own PCs: the same file from his private Tailscale share).
2. Run the script in the vault root:
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "<vault>\vault-update.ps1"`
   - macOS/Linux: `bash "<vault>/vault-update.sh"`
   Script missing: run `git -C <vault> fetch origin && git -C <vault> reset --hard origin/main` first (the vault is read-only), then retry.
   Full view: if the user asks for full view / to turn light mode off, add `-FullView on` (Windows) or `--full-view on` (macOS/Linux); `off` returns to light mode. It persists across updates. Full view is slower: Obsidian indexes about 14,000 more notes.
3. It runs a self-healing `git fetch` + fast-forward (if local changes or CRLF noise block it, real changes go to `local-changes-<timestamp>.patch` in the sync state folder and the vault is reset to origin/main, printing one line; it never fails), `claude-kit/kit-refresh.*` (installs new agents/skills) and `claude-kit/tools/assets-sync.py` (reads `repos.json`, downloads only new or changed asset zips into `<vault>/Assets`, follows redirects, verifies sha256, resumes interrupted downloads). The vault's `origin` is the public GitHub repo `vault-notes`; a clone still pointing at the old website address is moved automatically. A first run on a computer downloads about 1 GB and can take minutes: run it in the background if your tool has a time limit and check the output; never ask the user.
3b. The kit refresh also sends queued `/rbx-learn` notes to the vault-learnings inbox (silent when nothing is queued, offline or without write access; skip with env `CLAUDE_LEARN_SKIP=1`; `learn.py pr` is the opt-in route from a fork). [cold:rbx-update/kit-refresh-details.md] read only when the update output mentions queued learnings, the AI Library Vault or a kit migration and you need the exact behaviour.
4. `no asset source reachable` = the computer is offline (or, on the owner's PCs, the private share is unreachable): say so in one line; vault and kit still updated from GitHub. Do not retry in a loop.
   The script also updates the companion AI Library Vault (clone `ai-library-vault` next to the vault, same self-healing and protected My Research) via `ai-vault-sync.ps1`/`.sh`, cloning it the first time. Skip with `-NoAiVault` (Windows) or `--no-ai-vault` (macOS/Linux). `NEEDS_LOGIN` printed: say so in one line; the Roblox vault is unaffected.
4b-4c. The kit refresh also refreshes folders with Roblox dev mode loaded and moves an OLDER always-on kit install into the on-demand store (prints `vault-mode: moved N vault skills ...`; your own skills, agents and CLAUDE.md are untouched). If the output contains a `NOTICE FOR THE USER` line (commands renamed, UI mockups default notice, locally changed vault files kept), copy that notice into your report word for word and never run an old command name again (undo: `kit-rename.py migrate --revert` in `<config>/claude-kit/tools`). [cold:rbx-update/kit-refresh-details.md] read only when the update output mentions queued learnings, the AI Library Vault or a kit migration and you need the exact behaviour.
5. Mode status: `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" status`; add its first line (and any `kept vault files:` line) to your report (whether Roblox dev mode is ON in the current folder (`/rbx-load` turns it on) and how many folders have it loaded). `OLD LAYOUT` printed: run `vault-mode.py migrate` once and say so.
6. Report in two lines (add the patch path if local changes were saved, and which mode is active, light or full view): what changed (vault commits, kit line, assets line) and the Assets folder path. `N of your own files kept` printed: add that. Never edit, commit or push in the vault.
   Last line of your reply, verbatim: the update script's final line `Your vault is up to date as of <day and time> (local time)` (or `Your vault is up to date.`); nothing after it.

Two commands: `/rbx-update` (this one: safe, keeps everything of the user's; only tracked-file edits are patched and reset) and `/rbx-clean` (exact copy of the main vault, still keeps Games and My Research; asks once).

To only switch the Obsidian view without updating: `/rbx-light-on` or `/rbx-light-off` (`-SetView light|full` / `--set-view light|full`).
