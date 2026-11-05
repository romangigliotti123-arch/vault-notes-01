---
name: rbx-update
description: "Update the claudes-vault and the AI Library Vault on demand: self-healing git update (local changes saved to a patch), refresh the installed kit (skills and agents stay OFF in normal sessions), sync Assets (about 1 GB first time). Use for /rbx-update, 'update the vault', stale vault content."
---

# rbx-update

The vault no longer polls every 15 minutes: it updates at logon and when you run this. Run it now, without questions.

1. Find the vault (first existing wins): `$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`. If none exists, follow the setup runbook instead: `curl -fsSL https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md` (Roman's own PCs: the same file from his private Tailscale share).
2. Run the script in the vault root:
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "<vault>\vault-update.ps1"`
   - macOS/Linux: `bash "<vault>/vault-update.sh"`
   If the script is missing, run `git -C <vault> fetch origin && git -C <vault> reset --hard origin/main` first (the vault is read-only), then retry.
   Full view: if the user asks for full view / to turn light mode off, add `-FullView on` (Windows) or `--full-view on` (macOS/Linux); `off` goes back to light mode. The choice persists across updates. Full view is slower: it makes Obsidian index about 14,000 more notes.
3. It runs a self-healing `git fetch` + fast-forward (if local changes or CRLF noise block it, real changes go to `local-changes-<timestamp>.patch` in the sync state folder and the vault is reset to origin/main, printing one line; it never fails), `claude-kit/kit-refresh.*` (installs new agents/skills) and `claude-kit/tools/assets-sync.py` (reads `repos.json`, downloads only new or changed asset zips into `<vault>/Assets`, follows redirects, verifies sha256, resumes interrupted downloads). The vault's `origin` is the public GitHub repo `vault-notes`; a clone that still points at the old website address is moved to it automatically on the first run. A first run on a computer downloads about 1 GB and can take several minutes: run it in the background if your tool has a time limit and check the output, never ask the user.
3b. The kit refresh also sends notes queued by `/rbx-learn` to the public vault-learnings inbox (`learn.py flush --quiet`): silent when nothing is queued, offline, or the machine has no write access (the notes then stay queued; `learn.py pr` is the explicit, opt-in way to contribute from a fork). Skip it with env `CLAUDE_LEARN_SKIP=1`.
4. If it prints `no asset source reachable`, the computer is offline (or, on the owner's own PCs, the private share is unreachable): say that in one line; the vault and kit still updated from GitHub. Do not retry in a loop.
   The script also updates the companion AI Library Vault (clone `ai-library-vault` next to the vault, same self-healing and protected My Research) via `ai-vault-sync.ps1`/`.sh`; it clones it the first time. Skip it with `-NoAiVault` (Windows) or `--no-ai-vault` (macOS/Linux). If it prints `NEEDS_LOGIN`, say so in one line; the Roblox vault itself is unaffected.
4b. The kit refresh also (a) refreshes the folders that have Roblox dev mode loaded (`/rbx-load`), and (b) moves an OLDER always-on kit install (vault skills/agents directly in `~/.claude/skills` and `/agents`) into the on-demand store with a backup, printing a `vault-mode: moved N vault skills ...` line. Your own skills, agents and CLAUDE.md are not touched.
4c. Command rename (one time): if the output contains a `NOTICE FOR THE USER` line (commands renamed, UI mockups default notice, locally changed vault files kept), copy that notice into your report word for word (old name -> new name). The kit installer removed the OLD generic command names (the notice lists them) of this vault and installed the vault-suffixed ones; your own skills with those old names were left alone. Undo: `kit-rename.py migrate --revert` (in `<config>/claude-kit/tools`). Do not run any old name again.
5. Mode status: run `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" status` and add its first line (and any `kept vault files:` line) to your report: whether Roblox dev mode is ON in the current folder (type `/rbx-load` to turn it on) and how many folders have it loaded. If it prints `OLD LAYOUT`, run `vault-mode.py migrate` once and say so.
6. Report in two lines (add the patch path if a line said local changes were saved, and which mode is active, light or full view): what changed (vault commits, kit line, assets line) and the Assets folder path. If it printed `N of your own files kept`, add that. Never edit, commit or push in the vault.
   Last two lines of your reply, verbatim: the script's `Vault: <folder> | Kit: <folder>` line (where the vault and kit are on this computer), then its final line `Your vault is up to date as of <day and time> (local time)` (or `Your vault is up to date.`); nothing after it.

Two commands: `/rbx-update` (this one: safe, keeps everything of the user's; only tracked-file edits are patched and reset) and `/rbx-clean` (exact copy of the main vault, still keeps Games and My Research; asks once).

To only switch the Obsidian view without updating, use `/rbx-light-on` or `/rbx-light-off` (`-SetView light|full` / `--set-view light|full`).
