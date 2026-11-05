---
name: sponsored-ad-reviewer
description: "Review a Roblox sponsored-experience (or search-ad) campaign's results: compute CTR, cost per play, click-to-play and ROAS with ad_read.py, apply the playbook's stop and scale rules, compare the ad cohort with organic, and choose exactly one next test. Use after a campaign has run through its learning period; planning a campaign is rbx-ads."
category: marketing
tags: ads, sponsored, ads manager, ctr, cpp, roas, creative test, campaign review, search ads, budget, learning period
kb: Roblox/roblox-kb/ads-stats-monetisation-playbook.md, Roblox/roblox-kb/ads-and-sponsored-experiences.md, Roblox/roblox-kb/_tools/AD-PLAYBOOK.md, Roblox/roblox-kb/_tools/BENCHMARKS.md, Roblox/roblox-kb/discovery-algorithm.md
related: rbx-ads, rbx-thumb-brief, discovery-signal-reader, ctr-ab-test-planner, retention-diagnoser, thumbnail-maker, rbx-ads
---

# sponsored-ad-reviewer

Ads are retrieval and a data seed, not a ranking hack: ad-acquired players are excluded from Recommended-For-You ranking signals, and ads on a leaky game burn money (vault playbook rule 0). This skill reads a finished or running campaign and decides the next single change. It never spends, starts, pauses or edits a campaign; the owner does. Spending is the owner's decision and only with money they can lose.

## When to use
At least about 48 hours of data (the learning period restarts on each pause or edit), ideally 7 days. Not for: designing a first campaign (`rbx-ads`), organic discovery (`discovery-signal-reader`).

## Inputs (max 3)
1. Campaign numbers from Ads Manager: spend, impressions, clicks, plays, hours run, objective and audience, creatives with per-creative CTR. 2. Game numbers: D1 and D7 of the ad cohort vs organic, payer conversion, attributed earnings if the objective is Earnings. 3. The owner's budget limit and goal.

## Procedure
1. Live-check Ads Manager's current objectives, audiences, creative limits, learning-period text and benchmarks; names and limits have changed several times (the vault lists Plays, Earnings (Limited), Engagement as of 2026-11-01). Record them with the date.
2. Run the numbers: `python -I ~/.claude/claude-kit/skillpack/marketing/sponsored-ad-reviewer/scripts/ad_read.py --spend <USD> --impressions N --clicks N --plays N --hours H [--earnings <USD>] [--cohort-d1 0.xx --organic-d1 0.xx]`. Defaults are the playbook's: CTR below 1% is bad, about 2.5% a day-one target, CPP benchmark $0.008 (Plays), ROAS 100% is break-even, learning about 24-48 hours. Pass the live values with the override flags if they differ. Quote the output.
3. Walk the playbook's decision tree in this order and stop at the first failing step: (a) too early? change nothing; (b) CTR low: packaging (`thumbnail-maker`, `ctr-ab-test-planner`); (c) CTR fine, CPP bad: thumbnail-to-game mismatch or join friction; (d) ad-cohort D1 well under organic: fix the game, do not scale (`retention-diagnoser`); (e) ROAS under 100% after the attribution window (earnings finalise up to 30 days): do not scale; (f) all fine: scale in modest steps.
4. Per-creative read: keep creatives above the CTR floor, retire those under 1%, never judge a creative on a few hundred impressions. Creative caps have grown over time (5, 10, 15-25 reported): live-check.
5. Stop rules: ROAS under 100% over the window, collapsing ad-user D1, organic Home recommendations now exceeding sponsored impressions (shrink or stop), or CPP double the benchmark with a good CTR.
6. Choose exactly one next test with one variable, a budget cap the owner approves, a hold time of at least 3-5 days, and a decision rule written in advance (`ctr-ab-test-planner`).
7. Honesty notes: the lift figures Roblox cites (median impression lift, incrementality) are upper bounds for a small indie game; indie ROAS stories are self-reported.

## Studio MCP path
Not needed: the numbers come from Ads Manager and Creator Hub analytics, exported or pasted by the owner. No Studio tool reads or changes a campaign.

## Fallback
Same. If the owner cannot paste numbers, list the cells to copy and stop; do not estimate.

## Evidence
`Roblox/roblox-kb/ads-stats-monetisation-playbook.md` (rules that override everything; stat targets with trust labels; objectives resolved 2026-11-01; spend ladder gates and stop rules; CPP benchmarks official; learning 24-48 h, restarts on pause; ROAS counts earnings up to 30 days), `Roblox/roblox-kb/ads-and-sponsored-experiences.md` (fix retention first; run 1-2 weeks; broad targeting; ads excluded from RFY signals; use ads at key moments), `Roblox/roblox-kb/_tools/AD-PLAYBOOK.md` and `BENCHMARKS.md` (if-then rules, numbers), `Roblox/roblox-kb/discovery-algorithm.md` (only organic RFY plays count for ranking; stop ads once Home recs sustain). Most targets are indie or third-party: live-check Ads Manager before acting.

## Output
`marketing/ad-review-<date>.md`: live settings with date, the `ad_read.py` output, decision-tree walk (step, pass/fail), per-creative table, the one next test and the owner's budget cap.

## Acceptance checks
- [ ] `ad_read.py` output is quoted with the exact command and inputs.
- [ ] The decision tree is walked in order and stops at the first failing step.
- [ ] Live Ads Manager values (objective names, learning period, caps) have a date from this run.
- [ ] Exactly one variable changes in the next test; the decision rule has numbers.
- [ ] No spend, start, pause or edit was made by the skill.

## Pitfalls
Judging inside the learning period. Editing or pausing daily (it restarts). Scaling a leaky game out of trouble. Comparing ROAS before earnings are final. Treating a thumbnail win as a retention win. Mixing the old Maximize Plays names with the new objectives.

## Related
`rbx-ads`, `rbx-thumb-brief`, `discovery-signal-reader`, `ctr-ab-test-planner`, `retention-diagnoser`.
