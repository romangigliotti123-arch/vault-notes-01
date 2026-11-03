# Install: deep-topic-research-rbxdev-vault

A Claude Code skill. Give it a topic; it asks for a usage budget, time limit and worker cap, then researches GitHub, YouTube, Reddit, blogs/docs and papers, ranks the best creators, reads what they published (within your limits), checks the claims against official sources, optionally rates how credible each creator is, and writes a cited knowledge base, playbook and cheat sheet.

## 1. Copy the folder
Put the folder so that `SKILL.md` sits directly inside a folder named `deep-topic-research-rbxdev-vault`:
- All your projects: `~/.claude/skills/deep-topic-research-rbxdev-vault/` (Windows: `%USERPROFILE%\.claude\skills\deep-topic-research-rbxdev-vault\`)
- One project only: `<project>/.claude/skills/deep-topic-research-rbxdev-vault/`

From a zip: unzip into `~/.claude/skills/` (the zip already contains the `deep-topic-research-rbxdev-vault` folder). Start a new Claude Code session so the skill is picked up. It then works as the slash command `/deep-topic-research-rbxdev-vault`, or just ask in plain words ("research luau type checking").

## 2. Check your machine (free, installs nothing)
- macOS/Linux: `sh ~/.claude/skills/deep-topic-research-rbxdev-vault/scripts/doctor.sh`
- Windows: `powershell -NoProfile -File "$env:USERPROFILE\.claude\skills\deep-topic-research-rbxdev-vault\scripts\doctor.ps1"`
It prints what is present, what is missing, the exact install command for your OS, and the python command to use. Needs Python 3.8+ and Claude Code; yt-dlp (YouTube), `gh` logged in (GitHub rate limit) and ffmpeg (video frames) are optional. On Windows `python3` can be a Microsoft Store stub: use the command the doctor prints, or `py -3`. No API keys, accounts or logins are needed. Nothing is installed unless you say yes.
Optional self-test, no cost, no network: `python scripts/selftest.py` (ends with `SELFTEST PASSED`).

## 3. Use it
- "Research Rust async runtimes."  /  "Use deep-topic-research-rbxdev-vault on sourdough hydration. Light budget."  /  "Find the best creators for learning Blender geometry nodes."
- Resume: "Resume the deep-topic-research-rbxdev-vault run for rust-async-runtimes with 2 more hours."
It asks four things first: usage budget, time limit, worker cap, depth (with the optional creator-credibility check). "Just go" uses the safest Light defaults: about $1, 30 minutes, 1 worker, quick scan, credibility off.

## 4. Where your research is saved
- If you have a `claudes-vault` clone (`$CLAUDES_VAULT`, else `~/Obsidian/claudes-vault`): `<vault>/My Research/<topic-slug>/`. That folder is local and private, is never changed or deleted by vault updates, and each topic folder has a `PROTECTED-RESEARCH.md` marker. Do not delete it.
- Otherwise: `./research/<topic-slug>/` in the folder where you ran it.
- `--out DIR` overrides (never into the vault's Library/, Roblox/, Manager/, Imported/ or Assets/ folders). Claude tells you the path at the end of every run.

## 5. Expected cost
API-equivalent dollars (on a subscription this uses your normal allowance, not extra money). Rough window share is about 5% of a 5-hour window per dollar from one measured run; it varies a lot by plan.
- Light about $1: ~100 sources with haiku, a few theme notes, the trust layer, one playbook.
- Moderate about $5: a few hundred sources, sonnet for dense technical items, creator credibility on the top 10, more themes.
- Heavy about $15: several hundred to a thousand sources, credibility on all creators; Opus for the final synthesis only if you allow it.
The plan prints a cost range per stage before anything runs. Real spend is logged per call in `costs.csv`; the run stops when the budget, the time limit or your usage limit is reached, and can be resumed.

## 6. Privacy and respectful use
Public pages only, robots.txt and rate limits respected, no logins, no credentials, nothing uploaded. Notes summarise other people's work for your own use: do not republish them. See `references/safety.md`.

## Uninstall
Delete the `deep-topic-research-rbxdev-vault` folder. Research folders are yours to keep or delete.
