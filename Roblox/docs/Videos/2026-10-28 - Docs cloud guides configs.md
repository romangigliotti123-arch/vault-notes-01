---
title: "Docs: cloud / guides / configs"
url: https://create.roblox.com/docs/cloud/guides/configs.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / configs

[Open](https://create.roblox.com/docs/cloud/guides/configs.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API docs for Experience Configs: create/overwrite/patch drafts, publish with deployment strategy, read published values, list revisions and roll back via restore plus publish. Covers draft hashes for optimistic concurrency and key limits.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[development-process-and-speed]]** Use configs to tune live values (e.g. boss health) without republishing the game; stage in drafts, then publish.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[ab-testing-and-experiments]]** Publish with GradualRollout (15-minute rollout) instead of Immediate when changing live gameplay values, to limit blast radius.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[team-and-budget]]** Send previousDraftHash on updates and publishes so a stale write fails instead of silently overwriting a teammate's changes; re-read and merge.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[common-mistakes]]** Restore does not publish. After restoring a revision you must call publish with the returned draftHash or the rollback never goes live.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[development-process-and-speed]]** Use PATCH on /draft to change a few keys; use draft:overwrite only for full state, since omitted keys are removed.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[version-control-and-tooling]]** Write a meaningful publish message; revisions record message, publishedBy and per-key before/after values for auditing and rollback.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[scripting-and-performance]]** Read configs in server scripts via ConfigService and react to changes with UpdateAvailable/Refresh or GetValueChangedSignal.
- [page](https://create.roblox.com/docs/cloud/guides/configs) **[[data-persistence]]** Keep config keys within limits: 100 keys per repository and 256 characters per key length.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/configs) Gradual rollout duration: **15 minutes** (GradualRollout deployment strategy for published configs)
- [page](https://create.roblox.com/docs/cloud/guides/configs) Keys per repository limit: **100** (Maximum config keys in InExperienceConfig repository)
- [page](https://create.roblox.com/docs/cloud/guides/configs) Key length limit: **256 characters** (Maximum length of a config key)

## Tools
Roblox Cloud API (creator-configs-public-api), ConfigService (Luau), Creator Hub / Studio (alternative config UI)

## He points to
- Cloud API reference
- Add configs to your code (Roblox guide)
- Refresh snapshots in the experience configs guide

## Topics
[[ab-testing-and-experiments]] [[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[scripting-and-performance]] [[team-and-budget]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
