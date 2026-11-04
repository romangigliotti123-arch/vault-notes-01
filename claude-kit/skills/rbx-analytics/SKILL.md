---
name: rbx-analytics
description: "Weekly review of a Roblox experience's Creator Dashboard analytics (retention, session length, funnel, monetisation, ad return) ending in a ranked list of changes to test. Use when asked how a game is doing or what to change next."
---

# Roblox analytics review

Input: exported or screenshot data from the Creator Dashboard (Analytics tab: Engagement, Retention, Monetization, Acquisition, Performance), plus the changes shipped in the period. If no data is given, ask for it; never invent numbers.

## Method
1. State the period and what changed (updates, ads, events). Compare to the previous equal period, not to a guess.
2. Acquisition: impressions, click-through (impressions to visits), new vs returning, traffic sources. A low click-through means icon/thumbnail/title; high click-through but poor retention means the first minute or the promise is wrong.
3. First session: D1 retention, average session length, drop-off in the first minutes (use a custom funnel event log: spawned, first action, first reward, tutorial done). Find the single biggest drop.
4. Retention: D1, D7, D30 by cohort; look at trend, not one day. Small sample (few hundred visits) means treat differences as noise.
5. Monetisation: payer conversion, ARPPU, revenue per visit, top products, share from passes vs products vs Premium payouts. Cross-check against rbx-monetize rules (no pay-to-win).
6. Ads (if used): Robux spent vs visits gained and how many returned on D1; compute cost per retained visit. Pause creatives with worse cost per retained visit.
7. Performance: crash rate, memory, client FPS, server heartbeat by device class; flag anything that hits low-end phones.
8. Output the changes ranked by (expected impact x ease), each with a metric to watch and a threshold that counts as success after a defined time. Mark which are cheap A/B tests (icon, thumbnail, first-minute reward, price).

## Report format
Period | headline (one sentence) | table of metrics with change vs previous | top 3 problems with evidence | ranked experiments | what data is missing.
Say plainly when data is too thin to conclude.

## Vault evidence (official first; full list in `Roblox/roblox-kb/analytics-metrics.md`)

Instrument funnels before closed beta or launch; D1/D7/D30 retention is the core health metric; read monetisation through conversion, ARPPU and ARPDAU together; change one thing per test and slice by platform, device, source and cohort. Full list: `Roblox/roblox-kb/analytics-metrics.md`. [cold:rbx-analytics/vault-evidence.md] read only to cite or verify the vault evidence behind a metric recommendation.