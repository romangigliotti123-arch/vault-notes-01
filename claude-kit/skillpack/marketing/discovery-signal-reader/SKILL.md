---
name: discovery-signal-reader
description: "Read a Roblox game's organic discovery numbers (impressions, CTR, play-through rate, first-play bounce, D1, D7, session length, payer conversion, likes) and order what to fix first with signal_read.py, using the vault's decision tree and the 2026 recommendation signal set. Use when impressions or plays stall, before spending on ads, or after a packaging change."
category: marketing
tags: discovery, recommendations, impressions, ctr, ptr, qptr, bounce, d1, d7, home, recommended for you, signals
kb: Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/ads-stats-monetisation-playbook.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/analytics-metrics.md
related: sponsored-ad-reviewer, retention-diagnoser, thumbnail-maker, store-page-audit, first-minute-designer, ctr-ab-test-planner, roblox-analytics-review
---

# discovery-signal-reader

Roblox's recommendations optimise for engagement, retention and monetisation together, and creators are told not to game individual signals. The vault records the June 2026 change: QPTR was replaced by PTR plus First Play Bounce Rate (0-60 s and 61-180 s), and the lookback grew from 7 to 28 days. This skill turns your Creator Hub numbers into a fix order. Paid traffic is read by `sponsored-ad-reviewer`; deep retention is `retention-diagnoser`.

## When to use
Home impressions are low or flat, plays are low, or you need to decide between packaging, onboarding and content work. Not for: ad campaigns, monetisation tuning on its own.

## Inputs (max 3)
1. Creator Hub numbers for the last 7 and 28 days: impressions and trend, CTR, PTR, first-play bounce (both windows if shown), D1, D7, average session, payer conversion, like ratio. 2. Genre and the game's age (new games are tested in stages). 3. Whether Exclude from Recommendations and genre are set (read the settings page).

## Procedure
1. Live-check the current signal names and what Creator Hub shows (the algorithm and analytics pages changed in 2025-2026); record the date. Prefer the newer signal set over six-signal advice.
2. Settings first: custom thumbnail present, genre set, Exclude from Recommendations OFF, access public. Any failure here explains zero Home traffic; fix and wait for propagation (genre can take days).
3. Run: `python -I ~/.claude/claude-kit/skillpack/marketing/discovery-signal-reader/scripts/signal_read.py --ctr X --ptr X --bounce60 X --bounce180 X --d1 X --d7 X --session MIN [--payer X --likes X --impressions-trend down]`. Floors are the playbook's rough guides (D1 10%+, D7 2-3%, PTR over 1%, ad-CTR drop line 1%, session 10+ min, payer 1-2%, likes about 80%), which come from indie or third-party sources; override with `--floor` after checking your own Analytics similar-experience benchmarks. First-play bounce has no published target, so compare trends and genre peers.
4. Fix in the printed order: packaging (CTR, PTR) -> first minute (bounce) -> D1 -> D7 -> session -> monetisation -> sentiment. Vault: weak packaging means no impressions whatever the game quality, but clickbait raises bounce and now hurts ranking, so packaging fixes must stay honest.
5. Context rules: only organic Home recommendation plays feed ranking signals (ads, search, friend and direct-link plays do not); the playtime benefit is capped at 60 minutes per user per day; expect a burst then normalisation after distribution changes; do not judge on a single day; weekly seasonality peaks Saturday; new games get small staged tests (about 5 then 100 CCU in one account) and old games can re-enter.
6. Pick one fix, one metric and a re-read date at least 7 days later (28-day signals need longer). Hand packaging to `thumbnail-maker` and `ctr-ab-test-planner`, onboarding to `first-minute-designer`.
7. If ads are being considered: check the readiness gate in the ads playbook (D1 and bounce first); ads seed data but do not fix a leaky game.

## Studio MCP path
Not needed. Optional `get_studio_state` to confirm the place. Numbers come from Creator Hub, pasted by the owner.

## Fallback
Same. Missing numbers are listed as "not provided" by the tool; do not estimate them.

## Evidence
`Roblox/roblox-kb/discovery-algorithm.md` (signal set 2026; bounce windows; 28-day retention; only organic RFY plays count; 60 minute cap; custom thumbnail required; genre and Exclude from Recommendations; staged testing; Highly Engaged Player thresholds for younger audiences, live-check), `Roblox/roblox-kb/ads-stats-monetisation-playbook.md` (stat targets with trust labels; decision tree "if X is low, do Y"; thin spots: no official D30, like-ratio or favourites targets), `Roblox/roblox-kb/thumbnails-icons.md` (fix low PTR with packaging first), `Roblox/roblox-kb/retention-d1-d7.md`, `Roblox/roblox-kb/analytics-metrics.md`. Algorithm behaviour changes often: live-check.

## Output
`marketing/discovery-read-<date>.md`: settings check, the tool output, the chosen fix and metric with the re-read date, and what is deliberately not changed.

## Acceptance checks
- [ ] Settings checklist done before the numbers.
- [ ] `signal_read.py` output quoted with the inputs used.
- [ ] Exactly one fix is chosen with a re-read date of 7+ days.
- [ ] Floors overridden or accepted explicitly, with the label "indie/third-party heuristic".
- [ ] No claim about Roblox's internals beyond the vault's cited statements.

## Pitfalls
Optimising a single metric. Judging a day. Treating ad-driven CTR as organic. Making the thumbnail more clickable at the cost of bounce. Ignoring Exclude from Recommendations during a long beta.

## Related
`sponsored-ad-reviewer`, `retention-diagnoser`, `thumbnail-maker`, `store-page-audit`, `first-minute-designer`, `ctr-ab-test-planner`.
