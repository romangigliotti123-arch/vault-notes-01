---
name: changelog-writer
description: "Keep a developer changelog from commit subjects: group conventional commits into Added, Fixed, Changed and Internal with changelog.py, flag unsorted commits, and hand the Added and Fixed lists to the player-facing update post. Use at each release or weekly, from a git tag range."
category: workflow
tags: changelog, commits, release notes, version, history, conventional commits, update log
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/development-process-and-speed.md, Manager/topic-observability.md, Mentor/Combined-Brain.md
related: git-workflow-setter, release-checklist-builder, update-announcement-writer, devlog-writer, rbx-game-update, version-history-keeper
---

# changelog-writer

Developer-facing history, generated from commit subjects so it costs no memory. The player-facing text is `update-announcement-writer` and `rbx-game-update`; the public build-in-progress story is `devlog-writer`. This skill only turns `git log` into `docs/CHANGELOG.md` sections and shows which commits were too vague to sort.

## When to use
A release is being cut, or a week of commits needs a record. Not for: player announcements, or projects whose commits are not in git (then write entries by hand from `docs/PROGRESS.md`).

## Inputs (max 2)
1. The range (default: last tag to HEAD: `git describe --tags --abbrev=0`; if no tag, the last 30 commits). 2. Version label and date (default: `Unreleased` and today).

## Procedure
1. Get the subjects: `git log <range> --pretty=%s > commits.txt`. If git is missing, stop and use the PROGRESS file.
2. Run `python changelog-writer/scripts/changelog.py commits.txt --version 1.3 --date 2026-11-02 > section.md`. Conventional subjects (`feat`, `fix`, `perf`, `refactor`, `docs`, `chore`, `test`, `exp`) are sorted; a `!` marks Breaking; anything else lands under Unsorted.
3. Review Unsorted: reword nothing in history; instead write the correct line by hand under the right heading and note the commit hashes. If more than a quarter of commits are Unsorted, point at `git-workflow-setter` (commit rule) for next time.
4. Read each Added and Fixed line as a player would: does it describe a visible change? Split visible changes (for the update post) from internal ones; keep Internal in the changelog only.
5. Prepend the section to `docs/CHANGELOG.md` (newest first; never edit old sections). Mention data-affecting or monetisation-affecting lines explicitly so the release checklist sees them.
6. Hand the visible lines to `update-announcement-writer`; do not publish or post anything.

## Studio MCP path
None.

## Fallback
Hand-written list under the same four headings. The script uses only Python; `git log` is plain git.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md` (regular updates and clear communication keep players returning), `Roblox/roblox-kb/version-control-and-tooling.md` (meaningful messages for audit and rollback; revisions record publish messages), `Roblox/roblox-kb/development-process-and-speed.md`, `Manager/topic-observability.md` (an append-only event/log file is the cheapest durable record), `Mentor/Combined-Brain.md`.

## Output
A new top section in `docs/CHANGELOG.md` and a short list of visible changes for the post.

## Acceptance checks
- [ ] Executed: `python changelog-writer/scripts/changelog.py --selftest` prints `selftest ok`.
- [ ] Executed: the project run produced a section whose line count matches the commit count minus merges (`wc -l commits.txt` compared).
- [ ] Unsorted is empty or each entry was handled by hand.
- [ ] Executed: `grep -c "^## " docs/CHANGELOG.md` before and after the edit differs by exactly one.

## Pitfalls
Commit subjects like "fix stuff" produce a useless log. Putting internal refactors in the player post. Rewriting past sections. Letting a worker's commit messages claim more than the diff does (check `git show --stat`).

## Related
`git-workflow-setter`, `release-checklist-builder`, `update-announcement-writer`, `devlog-writer`, `rbx-game-update`.
