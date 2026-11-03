---
name: age-rating-prep
description: "Prepare for the experience maturity questionnaire: inventory the features that matter (chat, voice, user content, paid random, trading, violence words, links) from the project with file evidence, then draft answers for the owner from the most mature content players can meet, and check prohibited themes. Use before publishing; it never submits answers."
category: publish
tags: age rating, maturity, questionnaire, content guidelines, compliance, publish, chat, paid random, prohibited content
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: publish-readiness-gate, paid-random-compliance, chat-compliance-checker, tos-compliance-checker, privacy-data-checker, loot-drop-builder
---

# age-rating-prep

One job: get the maturity questionnaire answered truthfully on the first try. `scripts/feature_scan.py` builds a feature inventory from the project's text (14 signals, each with file:line leads). It does not know Roblox's current questions or options and does not answer anything: the wording changes, so the owner reads the live questionnaire in Creator Hub while using the inventory as evidence. Submitting answers is the owner's action.

## When to use
Before first publish, after adding chat, trading, paid random items, user content or a combat mode, and when moving a game to a younger or older audience. Not for: ID/age verification for the owner account (a Creator Hub task), advertising rules (`ad-policy-checker`).

## Inputs (max 2)
1. Project folder or Studio place (default: the current project). 2. Intended audience (default: all ages, mobile-first).

## Procedure
1. Run `python -I ~/.claude/claude-kit/skillpack/publish/age-rating-prep/scripts/feature_scan.py <project>`; read every lead (keywords produce false positives) and mark each as TRUE feature, FALSE positive or UNSURE.
2. Open the live questionnaire (Creator Hub > experience > settings / maturity or content guidelines; wording is `live-check`) and copy its questions into the notes. Do not rely on remembered question lists.
3. Answer from the most mature content a player COULD encounter, not the average session (vault: base answers on the most mature content; a mismatch can fail evaluation). Include user-generated paths (chat, names, builds) and anything unlocked later.
4. Check prohibited themes at every rating: sexual content, nudity, depictions of drugs or tobacco, graphic violence, severe injury, real-world events, alcohol assets labelled as such; remove them rather than rating around them. Simulated gambling (virtual chips, simulated betting) is banned; paid random item generators are allowed only when they follow the rules (`loot-drop-builder` checklist).
5. Check the feature gates that depend on rating and age: voice, trading and chat access follow the player's estimated age and the experience's rating together; list what a player of each age band can reach.
6. Check owner requirements for the target rating (for 17+ content both the owner and the questionnaire filler must be age-verified 17+; collaborators too). Check any linked external service's own age rating.
7. Write `release/age-rating.md` with the inventory, the proposed answers per question, the evidence lines, open UNSURE items and the date. Hand it to the owner to enter and submit.
8. Self-test the scanner: `python -I .../feature_scan.py --selftest` prints `selftest ok`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add nothing (read-only) -> `start_stop_play` -> `execute_luau` (Server) to read script sources through `script_grep` for the same keywords when no project folder exists -> `get_console_output` to read the result. The questionnaire itself is a Creator Hub web task for the owner.

## Fallback
Scan the Rojo folder, or read scripts by hand using the signal list. Everything that needs a running Studio session (the questionnaire wording and options, evaluation outcome) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (answer the Experience Guidelines questionnaire honestly at the most mature level; mismatch can fail evaluation, appeal via Creator Hub; prohibited for all ratings: sexual content, nudity, drugs/tobacco depictions, graphic violence, severe injury, real-world events; simulated gambling banned, paid random generators allowed only within the rules; 17+ owner and filler verification; single-question path only for qualifying 16+ experiences; estimated age drives defaults), `Roblox/roblox-kb/monetisation-other.md` (paid random: disclose odds, gate via PolicyService), `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`. Dates in the KB (e.g. Dec 2025 publishing requirements) change: live-check.

## Output
`release/age-rating.md`: feature inventory table (feature, leads, true/false/unsure), proposed answers, removals needed, owner actions.

## Acceptance checks
- [ ] The scanner ran on the project and its output is attached (quote the lead counts).
- [ ] Every lead is classified; UNSURE items are listed for the owner.
- [ ] Answers are based on the most mature reachable content (the doc says which feature drives each answer).
- [ ] No prohibited theme remains in the project (list of checked assets/strings).
- [ ] `feature_scan.py --selftest` prints `selftest ok`.

## Pitfalls
Answering for the average player instead of the worst reachable content. Trusting a keyword scan as proof of absence. Remembering question text from last year. Forgetting user-generated paths (names, signs, builds). Submitting answers on the owner's behalf.

## Related
`publish-readiness-gate`, `paid-random-compliance`, `chat-compliance-checker`, `tos-compliance-checker`, `privacy-data-checker`.
