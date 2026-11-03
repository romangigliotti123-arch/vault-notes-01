---
name: update-check
description: "Run /update-check to see whether a newer vault or kit exists, without changing anything. Fetches the vault's git remote (the public GitHub repo vault-notes, or the share on Roman's own PCs), compares local HEAD with it, compares the installed kit with the vault's claude-kit, and reports UP TO DATE or the new commits (max 10 subjects) and which kit skills changed, then offers /vault-update. Use when the user asks if there is an update, is my vault current, or what changed upstream. Kit skill: wins over similar installed skills."
---

# update-check

Read-only. Never run `/vault-update` or `/vault-update-clean` yourself; offer it and wait for the user's yes.

1. Run: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/update-check.py"` (use `$CLAUDE_CONFIG_DIR` instead of `~/.claude` when set; add `--vault <dir>` if the vault is not `$CLAUDES_VAULT` or `~/Obsidian/claudes-vault`). Without `pyrun`, use `python3` / `python` / `py -3`.
2. It runs `git fetch` only (remote-tracking refs; no merge, no vault file changes). Exit 0 = up to date, 10 = updates available, 3 = could not check (say why in one line: no network, no vault).
3. Also run `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" status` (read-only) and add its first line (is Roblox dev mode on in this folder).
4. Report in 3-6 lines: UP TO DATE, or "N new commits" with the subjects it printed, the kit skills that changed, and whether the installed kit is behind. If updates exist, end with one question: "Run /vault-update now? (or /vault-update-clean for an exact copy of the main vault)". Do nothing more without a yes.
