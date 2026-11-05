<!-- cold: rbx-thumbnail/protocol.md | read when: planning or reading a thumbnail personalization test, recording its results, or asking which features win for a genre. -->

# Variant test protocol (Roblox thumbnail personalization) and the result ledger

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
4. At the end (or daily, if the numbers will expire), read each thumbnail's impressions, qualified plays, qPTR, average playtime and winning segment, and the first-half and second-half qPTR from the two graphs. Record every variant:
   `python -I ~/.claude/claude-kit/tools/thumb_record.py add --test <id> --genre <genre> --variant <A> [--control] --impressions N --qualified-plays N --avg-playtime MIN --date-start D --date-end D --qptr-first-half F --qptr-second-half F --feature emotion=fear --feature hero_size_pct=45 --varies emotion [--rubric-score N --gates-ok yes]`
5. `thumb_record.py decide --test <id> --write` applies the decision rule; `thumb_record.py summary` shows which features win per genre.
6. Ship the winner, keep the control for the next round, and refresh the set with the next real update rather than swapping often.

## Decision rule (ASSUMPTION: the vault's own, Roblox publishes no threshold; tune from your data)
- Ignore a thumbnail with fewer than about 1000 impressions (arbitrary starting value).
- WINNER only if its qPTR beats the control by at least 10% relative over at least 7 days, AND the gap holds in both halves of the run, AND average playtime per qualified play is not worse (a click that bounces is bait).
- LOSER is the mirror: at least 10% lower, behind in both halves.
- Everything else is INCONCLUSIVE (also when the half-by-half numbers or the playtime were not recorded: persistence cannot be shown).

## What the ledger keeps
Local file `<claude config dir>/claude-kit/state/thumbnails/results.jsonl` (survives updates; registered in `tools/user-state.json`). One JSON line per variant per test, same test and variant id replaces the line:
`test_id, game, genre, asset (thumbnail|icon|ad), variant_id, is_control, features {hero, hero_size_pct, emotion, gaze_target, palette, value_contrast, text, text_words, element_count, action_pose, style, twist}, varies [feature keys this variant changed vs the control], rubric_score, rubric_gates_ok, impressions, qualified_plays, qptr, ctr, avg_playtime_min, qptr_first_half, qptr_second_half, winning_segment, date_start, date_end, days, context (update|event|none), verdict (winner|loser|inconclusive), verdict_by (user|rule|none), notes`.
`varies`, the two half-run qPTR fields and `verdict_by` extend the research schema so the decision rule can run. qPTR is stored as a fraction (4.5% = 0.045) and computed from qualified plays and impressions when not given.

## Summary minimums (ASSUMPTIONS)
Per genre: at least 10 decided (winner or loser) non-control variants, else `not enough data`. Per feature value: at least 3 decided variants to be listed, with its win rate. Treat results below 20 decided variants per genre as leads; from 20 on, compare each feature's win rate with the rubric weights and raise or lower a weight by hand (rubric.md), with the evidence in the commit or note.

## Sharing (opt-in, off by default)
`thumb_record.py share on` lets `thumb_record.py queue` write ONE note per genre that has enough data: feature-value tallies only (for example "emotion: fear won 4 of 5"), no game names, no variant or test ids, no notes. It goes through the normal `learn.py` redaction and the `learn.py flush` path to the untrusted inbox; the vault owner decides what becomes knowledge. Nothing is sent unless sharing is on and a flush runs.

## Optional: ad creative test (costs money, needs the owner's yes)
A small ad per creative gives a cleaner click comparison; creator reports suggest a lifetime minimum of about $25 and 7 days per arm (self-reported, grade C). Never start an ad: write the plan and let the owner run it (`rbx-ads`).
