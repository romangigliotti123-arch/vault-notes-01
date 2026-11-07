---
name: launch-day-planner
description: "Plan a Roblox launch or big-update day hour by hour: freeze and page checks the day before, a fixed launch time, announcement order, what to watch in the first hours, the ad readiness gate, and the day-2-to-4 thumbnail swap window, generated with calendar_gen.py. Use within a week of launching a game or major update."
category: marketing
tags: launch, launch day, release plan, checklist, monitoring, hour by hour, friday, ads gate, hotfix, first 48 hours
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/thumbnails-icons.md
related: social-post-calendar, launch-teaser-planner, update-announcement-writer, rbx-launch-check, sponsored-ad-reviewer, discovery-signal-reader, influencer-outreach-writer
---

# launch-day-planner

A launch is a checklist with a clock. Vault: pick a fixed launch time so the community arrives together, prefer Friday with dev cutoff Wednesday and avoid Tuesday, keep the first post-launch release a bug-fix and polish update, do not judge on one day, and use ads only after retention is proven. Pre-launch prep is `rbx-launch-check`; this skill owns the day itself.

## When to use
The date is chosen and within about a week. Not for: months of promotion (`social-post-calendar`), the post text (`update-announcement-writer`).

## Inputs (max 3)
1. Launch date and hour with time zone, game or update. 2. Team size and who is on call. 3. Whether ads or creators are planned (default: none; see step 6).

## Procedure
1. Choose the slot with the vault's rule set: a Friday (momentum built Wednesday, cutoff Wednesday night or Thursday midday), same hour as past releases, an hour when your main audience is awake (live-check where players are from in Creator Hub). A non-Friday date is allowed, say why.
2. Generate the clock: `python -I .rbx/claude-kit/skillpack/marketing/social-post-calendar/scripts/calendar_gen.py launch --launch "YYYY-MM-DD HH:MM" --hours-before 24 --hours-after 48`. Replace the generic lines with your real tasks and owners.
3. T-24 h to T-3 h: freeze code, smoke test on a phone-size client, confirm thumbnails, icon, title and description are final (`store-page-audit`), genre set, Exclude from Recommendations OFF, access public, support channel open, rollback plan written (previous version restorable), server-sync event time set in UTC.
4. T-1 h to T0: heads-up post, then publish on time, then the announcement post with the Details Page URL on the group, Discord and X; creators with early access post their videos on their own schedule.
5. T+1 h to T+24 h: watch CCU, errors, first-play bounce, join failures; answer players in one visible place; schedule the first hotfix window; do not rush feature changes. Vault: expect fluctuation and an initial impression burst then normalisation; do not judge on a single day, weekly seasonality peaks Saturday.
6. Ads gate (only if planned): launch ads only when the readiness gate passes (D1 and bounce known to be healthy, one working monetisation item); budgets, objectives and learning period follow the ads playbook and `sponsored-ad-reviewer`; never exceed what the owner can lose; the owner starts and funds the campaign.
7. Day 2 to 4: read CTR and PTR per thumbnail and swap poor performers before the algorithm decides (indie, single source: aim for CTR above 2.5%).
8. T+48 h: recap post, list of fixes, next-update date. First post-launch release is a bug-fix and polish update.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `get_console_output` after `start_stop_play` for a pre-launch smoke test; nothing is published by this skill (publishing is the owner's action).

## Fallback
The generated table and checklists on paper; the owner runs every step. Smoke test results are `untested` unless a client was actually played.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md` (release Friday, cutoff Wednesday, avoid Tuesday; fixed launch time; countdowns and cross-channel announcements; first post-launch bug-fix update; server-synced UTC time), `Roblox/roblox-kb/ads-stats-monetisation-playbook.md` (ads are retrieval and seed, fix D1 first; ladder gates; learning period 24-48 h), `Roblox/roblox-kb/community-and-discord.md` (announce publicly; be visibly active), `Roblox/roblox-kb/discovery-algorithm.md` (expect fluctuation; do not judge on one day), `Roblox/roblox-kb/thumbnails-icons.md` (early swap window; one indie source). Day-of platform behaviour changes: live-check.

## Output
`marketing/launch-day.md`: the dated table (time, owner, task, done), the ads gate decision, the watch list with the exact metrics to read, the rollback plan, the day-2-to-4 swap rule.

## Acceptance checks
- [ ] The table came from `calendar_gen.py launch` (command and first lines quoted).
- [ ] Every row has an owner and a time.
- [ ] A rollback plan and an on-call name exist.
- [ ] The ads gate is a written yes or no with the numbers behind it.
- [ ] No row publishes, spends or posts without the owner's action.
- [ ] Ad plan: prerequisites confirmed first (eligibility, stable build, working onboarding funnel, age-rating settings); campaign runs 1-2 weeks and is judged only after 3-5 days, never a 1-2 day burst (official/mixed; Roblox/roblox-kb/_tools/DECISION-RULES.md, ads-and-sponsored-experiences).

## Pitfalls
Launching Tuesday night with nobody on call. Starting ads on a leaky game. Reading day-1 numbers as the verdict. Shipping features in the hotfix window. Announcing in Discord only.

## Related
`social-post-calendar`, `launch-teaser-planner`, `update-announcement-writer`, `sponsored-ad-reviewer`, `discovery-signal-reader`.
