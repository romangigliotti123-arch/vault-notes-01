---
title: "Docs: cloud / guides / experiments"
url: https://create.roblox.com/docs/cloud/guides/experiments.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / experiments

[Open](https://create.roblox.com/docs/cloud/guides/experiments.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API guide for managing in-experience experiments programmatically: create drafts with baseline/treatment variants and a goal metric, start or schedule, poll async operations, pull stats after 24h, complete with a winning variant, and list experiments. Includes goal metric list and limits.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Exactly one variant must have isBaseline true; the productType discriminator must match the populated configuration block (inGameConfigExperimentConfiguration or matchmakingExperimentConfiguration).
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Experiment configuration becomes immutable once started or scheduled; edit duration, rollout and variants while still in draft.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Wait at least 24 hours after starting an experiment before pulling /stats diagnostics.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Check isSrmDetected in stats; a true value signals sample ratio mismatch, so the split may be unreliable.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Omit variantId when calling :complete to stop without a winner; the config reverts to its previous value.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[ab-testing-and-experiments]]** Pick a goal metric matching the hypothesis, e.g. DAY_1_RETENTION for a boss-health change, and keep the test tied to it.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[updates-live-ops]]** Mutating endpoints (create, update, discard, start, schedule, complete) return async operations; poll until done is true before reading the result.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[scripting-and-performance]]** Use x-api-key with the Open Cloud creator-configs API and store keys outside source code; OAuth 2.0 apps are an alternative.
- [page](https://create.roblox.com/docs/cloud/guides/experiments) **[[analytics-metrics]]** Read operations need universe:read scope; write operations need universe:write, so issue keys with least privilege.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/experiments) Experiment duration: **14–60 days** (Allowed range for an experiment's durationSeconds)
- [page](https://create.roblox.com/docs/cloud/guides/experiments) Variants per in-experience experiment: **1 baseline + up to 2 treatments** (Maximum variant count for in-experience config experiments)
- [page](https://create.roblox.com/docs/cloud/guides/experiments) Concurrent matchmaking experiments: **1 running per universe** (Limit on running matchmaking experiments)
- [page](https://create.roblox.com/docs/cloud/guides/experiments) Stats availability: **after 24 hours running** (Minimum runtime before /stats can be requested)
- [page](https://create.roblox.com/docs/cloud/guides/experiments) Example exposurePercent / weights: **40% exposure, 50/50 weights** (Example create payload values, not recommendations)

## Tools
Roblox Open Cloud creator-configs API, Python requests, cURL, Creator Hub Experiments page

## He points to
- Cloud API reference
- Metrics in the experiments guide
- Creator Dashboard (Copy Universe ID)

## Topics
[[ab-testing-and-experiments]] [[analytics-metrics]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
