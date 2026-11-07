---
name: rbx-clean
description: "Make this computer's claudes-vault an EXACT copy of the main vault, removing stray or changed files, while keeping Games, My Research and other protected folders. DESTRUCTIVE: prints a dry run and asks one confirmation question. Explicit command only. For a normal safe update that keeps everything of the user's, use /rbx-update."
disable-model-invocation: true
---

# rbx-clean

Exact copy of the host's vault: `git fetch`, `reset --hard origin/main`, `git clean -fd` (never `-x`), then the kit refresh and the Assets sync (which also deletes assets no longer on the host). Never touched: `Games/` (your game communities and Games/_Reusable), `My Research/`, any folder containing `PROTECTED-RESEARCH.md`, `Assets/` (synced separately), `.full-view`, `.obsidian/workspace*`. Before deleting anything it saves a patch of the user's tracked edits and copies the untracked files it removes to a backup in the sync state folder (newest 3 backups, max 500 MB; a bigger one is skipped and the output says so).

> Games protection needs the current updater: if this vault's `rbx-update` script is older than the one that lists `Games` among the kept folders (the dry run prints `Kept untouched: My Research/, Games/ ...`), run a normal `/rbx-update` once first, then `/rbx-clean`. Read the dry run's `Kept untouched` line before saying yes.

1. Find the vault (first existing wins): `$CLAUDES_VAULT`, `~/Obsidian/rbx-dev-vault`, `~/Obsidian/claudes-vault` (or where the pointer file `~/.claude/rbx-dev-vault.path` says). If none exists, follow `SETUP-FOR-CLAUDE.md` instead.
2. Dry run first (changes nothing):
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "<vault>\vault-update.ps1" -Clean`
   - macOS/Linux: `bash "<vault>/vault-update.sh" --clean`
   It prints: tracked edits that would be reset, files that would change to match the main vault, the user's own untracked files that would be deleted, and what is kept.
3. Show the user that list in a few lines and ask ONE question: "This makes your vault an exact copy of the main vault. The files above are removed (a backup is saved first). My Research and your protected folders are kept. Apply?" This is the only question this skill asks. Skip it only if the user already said `--yes`/"no questions"/"just do it" in the same request.
4. On yes, run the same command with `-Yes` (Windows) or `--yes` (macOS/Linux). Report the final `rbx-clean:` line (commit, how many items removed, backup path, patch path) and the Assets line.
5. `-IncludeMine` / `--include-mine` additionally deletes `My Research/` (a backup is made first; if the backup is skipped or fails, My Research is kept). Use it ONLY if the user explicitly typed that option or said in plain words that My Research should be deleted too. The dry run then prints a second warning line listing what would be lost; mention it in your question.
6. If it prints `fetch failed (offline?)`, nothing was changed: say so in one line. Never run `git clean`/`git reset` by hand, never edit, commit or push in the vault.
