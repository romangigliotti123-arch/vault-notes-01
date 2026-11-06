<!-- cold: rbx-thumbnail/protocol.md | read when: planning or reading a thumbnail personalization test and deciding its winner. -->

# Variant test protocol (Roblox thumbnail personalization)

Source of the facts: https://create.roblox.com/docs/production/publishing/thumbnails and the staff posts https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689 , https://devforum.roblox.com/t/get-your-thumbnails-ready-for-thumbnail-personalization/3226599 (read 2026-11-05; re-check, the feature changes).

## What the platform does
- Needs 2 to 5 active thumbnails (one active = everyone sees it). Set up in Creator Hub: Home Page tab, Edit active thumbnails, Save, Start.
- It is a bandit, not a classic A/B test: each thumbnail first goes to random users to measure qPTR (qualified plays per Home impression) per user group, then the leader per group gets more impressions while the others keep minimal traffic. Impression counts are therefore unequal and say nothing about demand.
- The table shows status, impressions, qualified plays, average playtime per qualified play, qPTR and a winning segment (age group only). It fills after a few hours. There is no sample-size guidance, no confidence interval and no raw CTR.
- Official effect: an average +8.5% qPTR in testing, some thumbnails +50%. Staff advice: wait at least 7 days or until the next content update before changing the set; a short qPTR dip after a Home traffic spike is normal.
- Per-thumbnail impressions and qualified PTR are also available as Open Cloud analytics metrics, which Roblox keeps for a limited time (the vault notes say 30 days): export or record the numbers before they expire.

## Steps
1. Design 3 to 5 variants from the rubric-passing candidates (`thumb_score.py score`): one CONTROL (the current thumbnail or the best-scoring one) and variants that each change ONE feature group (hero size, emotion, palette, text, motion, twist). With five slots you can compare four feature groups per round. Keep them clearly different from each other, as staff advise.
2. The user uploads and starts the test in Creator Hub (the agent never touches the account). Do not edit while it runs.
3. Hold at least 7 days, or until the next content update. Note any update, event or traffic spike in the window (`--context`).
4. At the end (or daily, if the numbers will expire), read each thumbnail's impressions, qualified plays, qPTR, average playtime and winning segment, and the first-half and second-half qPTR from the two graphs, and write them down in the game's notes.
5. Apply the decision rule below by hand to each variant against the control.
6. Ship the winner, keep the control for the next round, and refresh the set with the next real update rather than swapping often.

## Decision rule (ASSUMPTION: the vault's own, Roblox publishes no threshold; tune from your data)
- Ignore a thumbnail with fewer than about 1000 impressions (arbitrary starting value).
- WINNER only if its qPTR beats the control by at least 10% relative over at least 7 days, AND the gap holds in both halves of the run, AND average playtime per qualified play is not worse (a click that bounces is bait).
- LOSER is the mirror: at least 10% lower, behind in both halves.
- Everything else is INCONCLUSIVE (also when the half-by-half numbers or the playtime were not recorded: persistence cannot be shown).

## Optional: ad creative test (costs money, needs the owner's yes)
A small ad per creative gives a cleaner click comparison; creator reports suggest a lifetime minimum of about $25 and 7 days per arm (self-reported, grade C). Never start an ad: write the plan and let the owner run it (`rbx-ads`).
