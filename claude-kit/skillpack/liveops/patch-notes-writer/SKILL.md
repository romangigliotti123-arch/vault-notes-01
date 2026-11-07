---
name: patch-notes-writer
description: "Write player-facing patch notes from a changelog or git diff: a short headline, New / Changed / Fixed sections, concrete numbers for balance changes, honest paid-item labels, plus the 60-character update text and notification line. Lints the draft with a script. Use for every update and hotfix announcement."
category: liveops
tags: patch notes, changelog, update log, announcement, release notes, events and updates, communication
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/titles-descriptions.md
related: update-announcement-writer, update-cadence-planner, event-planner, hotfix-playbook, rollback-planner, discord-server-setup, rbx-game-update
---

# patch-notes-writer

Players read the first line and the headings. Vague notes ("bug fixes") tell them nothing and the vault says so; a public changelog of fixed items builds trust. This skill writes the notes themselves. The marketing post, thumbnail and teaser beats are `update-announcement-writer`; this is the factual log that sits behind it.

## When to use
Any shipped update, hotfix or balance change. Not for: marketing copy and hype (`update-announcement-writer`), store-page text (`game-description-writer`), or incident write-ups (`hotfix-playbook` record).

## Inputs (max 2)
1. The raw changes: a changelog, commit list or your own notes (paste it). 2. Version or update number and release date; whether anything is paid (default: assume nothing is, ask if unclear).

## Procedure
1. Sort every change into New, Changed or Fixed; drop internal-only items (refactors, tooling). Merge near-duplicates. Stop condition: if you cannot say what a player sees differently, the line goes.
2. Rewrite each line for players: what changed and where, with the number for balance changes ("Sled costs 350 coins, was 500"). Buffs and nerfs always carry the numbers; vault advises buffing underused items rather than nerfing popular ones, so say why when you nerf.
3. Label paid content as paid (gamepass, Robux item) and keep the notes from reading like an ad. Announce monetisation in update logs (vault) but not hidden among fixes.
4. Headline: version or update number plus the theme, within 60 characters (the Events and Updates entry text limit in the vault; notification strings 99). Write both strings now.
5. Fixed section: list the real bugs players reported (this is the trust line). Add known issues you have not fixed yet.
6. Write the file, then lint it: `python -I .rbx/claude-kit/skillpack/liveops/patch-notes-writer/scripts/patchlint.py notes.md`. Fix every ERROR; read each warning (balance without a number, code-like words, paid item not labelled, missing Fixed or New). Exit 1 means do not publish.
7. Post order: in-game update list or shop panel (vault: a visible changelog in the shop), Discord, then the platform entry. Keep a stats and drop-rate reference page updated with each balance change.
8. For a rollback or a silent hotfix: add the fix to the next notes (vault: same-day silent patch, then include it in the changelog) and say it is already live.

## Studio MCP path
If the changelog lives in the project: `script_grep` for a Changelog ModuleScript or `multi_edit` to add the new entry to the in-game update panel. Needs a connected Studio (`list_roblox_studios`).

## Fallback
Plain Markdown plus the Python linter; the player-facing in-game panel is hand-edited.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: write specific announcements, not vague ones; update text within 60 characters and notification strings within 99 (Roblox Creator Docs 2026-10, live-check); publish a changelog of completed and fixed items; keep a stats and drop-rate reference; ship a visible update list in the shop; announce paid items in update logs; roll back severe regressions and note silent patches in the log. `community-and-discord.md` for channels.

## Output
`liveops/patch-notes-<version>.md`: headline, New, Changed, Fixed, Known issues, a "paid items" line if any, plus the 60-character update text and the 99-character notification line.

## Acceptance checks
- [ ] `patchlint.py --selftest` prints "selftest ok (4 checks)" and the real notes exit 0.
- [ ] Headline and update text are 60 characters or fewer; notification string 99 or fewer.
- [ ] Every balance line has a number; paid items are labelled.
- [ ] Fixed lists specific bugs, not "bug fixes".
- [ ] Nothing in the notes promises a date or feature the team has not committed to.

## Pitfalls
Announcing content you may not ship (vault: cancelled content frustrates players). Hiding nerfs. Changelog written in code terms. One huge list with 200 lines and no structure; group it. Forgetting that batched fixes after a rough period work best as one large changelog.

## Related
`update-announcement-writer`, `update-cadence-planner`, `hotfix-playbook`, `rollback-planner`, `discord-server-setup`.
