---
name: social-proof-collector
description: "Collect quotes, clips and numbers from the community for the store page, trailer and pitches without inventing or misusing them: ask permission, keep the source, label measured versus self-reported numbers, avoid personal details of young players and drop stale items. Lints a proof log with a script. Use before marketing material that quotes players or cites traction."
category: community
tags: social-proof, quotes, clips, testimonials, permission, numbers, marketing, community, credit
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/social-features-and-virality.md
related: community-showcase-planner, press-kit-builder, trailer-script-writer, store-page-audit, creator-collab-planner, fan-art-contest-planner
---

# social-proof-collector

Players trust other players. Real quotes, clips and honest numbers beat adjectives, but only if they are real, permitted and current. The vault's contest and fan-art guidance is consistent: ask permission, credit the maker, never use content without it. Nothing here is invented: an item with no source does not go in the log.

## When to use
Before a store page refresh, trailer, press kit or sponsor pitch that cites players or traction. Not for: planning a showcase programme (`community-showcase-planner`), building the press kit (`press-kit-builder`), or creator deals (`creator-collab-planner`).

## Inputs (max 2)
1. Where the proof will appear (default: store page and press kit). 2. Where to look (default: Discord showcase, comments, creator videos, the game's own analytics).

## Procedure
1. Search real sources only: public comments, showcase posts, creator videos, group wall, and your own analytics. Do not write or edit quotes; trimming is allowed only with ellipses and the maker's agreement.
2. For each candidate ask permission in the same place it was posted (public reply or ticket, never a DM to a minor) with a plain sentence of where it will appear and how it will be credited; record the answer. No reply means no.
3. Strip personal details: no real names, ages, schools, photos of children or exact locations; use the handle or "a player" if the maker prefers. If the author sounds young (age-like statements), leave them out or get a guardian's agreement.
4. Log every item in `proof/log.csv` with columns `kind,text,source_url,permission,date,label`; numbers must be labelled `measured` (from your analytics) or `self-reported` (from a creator or player claim); never present a self-reported number as a fact.
5. Run `python scripts/proof_log.py proof/log.csv` (add `--today YYYY-MM-DD` if reproducing); fix every FAIL (no source, no permission, unlabelled number); read the WARNs (stale over 180 days, personal-detail leads); rerun to exit 0.
6. Choose the final set: 3-5 quotes, 2-3 clips, 2-3 numbers that match the audience of each surface; refresh every quarter.
7. Credit the makers where they asked; keep a permission record so withdrawn items can be removed fast.

## Studio MCP path
Not needed. Measured numbers come from Creator Hub analytics or the kit Analytics system, which the owner reads; no Studio call produces proof.

## Fallback
CSV, script and text. Contacting people and publishing is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (always ask permission and credit fan creators; thank engaged members; measure community by anticipation). `Roblox/roblox-kb/influencer-and-creator-marketing.md` (self-reported numbers must be labelled; judge influence holistically). `Roblox/roblox-kb/social-features-and-virality.md` (ask permission and credit fan artists).

## Output
`proof/log.csv` (lint-clean), a short list of chosen items per surface with credit lines, and the script output. Under 60 lines.

## Acceptance checks
- [ ] `proof_log.py` exit 0 on the log; output quoted.
- [ ] Every item has a source URL and a recorded permission (or is a measured number).
- [ ] Numbers carry `measured` or `self-reported` and the surface text says which.
- [ ] No personal details of players appear.
- [ ] Stale items were dropped or re-confirmed.

## Pitfalls
Invented or paraphrased testimonials. Using a clip without permission. Presenting a creator's claim as a measured fact. Publishing a child's personal details. Letting quotes age for a year.

## Related
`community-showcase-planner`, `press-kit-builder`, `trailer-script-writer`, `creator-collab-planner`.
