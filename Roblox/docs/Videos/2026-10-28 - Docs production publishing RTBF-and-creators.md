---
title: "Docs: production / publishing / RTBF-and-creators"
url: https://create.roblox.com/docs/production/publishing/RTBF-and-creators.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / RTBF-and-creators

[Open](https://create.roblox.com/docs/production/publishing/RTBF-and-creators.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on right-to-be-forgotten (RTBF) obligations for creators. Explains that creators are responsible for permanently deleting personal data when a user deletes their account; covers daily Roblox RTBF messages, automated data store deletion via templates, and Right to Erasure creator webhooks for complex cases.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) **[[common-mistakes]]** Don't rely only on Roblox's notifications: you remain responsible for permanently deleting all personal data covered by an RTBF request, even when automation runs.
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) **[[common-mistakes]]** Verify that personal data stored outside configured RTBF templates or custom automation is also deleted; review the daily RTBF message against your data.
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) **[[scripting-and-performance]]** Configure RTBF deletion templates for each game's data stores so Roblox auto-deletes matching keys when processing a request; use this first for supported data.
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) **[[scripting-and-performance]]** Use a creator webhook with the Right to Erasure Request trigger for complex cases: custom deletion logic, unsupported data store schemas, or personal data stored outside data stores.
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) **[[analytics-metrics]]** Check your inbox daily for Roblox RTBF messages, which list pending requests requiring action and the affected games.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) RTBF notification frequency: **Daily message to creator inbox** (Roblox sends automated daily message listing RTBF requests and affected games)

## Tools
Roblox RTBF deletion templates (data stores), Creator webhooks (Right to Erasure Request trigger)

## He points to
- Data store right to be forgotten (RTBF) docs
- Automate right to erasure using webhooks docs

## Quotes
- [page](https://create.roblox.com/docs/production/publishing/RTBF-and-creators) "You remain responsible for permanently deleting all personal data covered by an RTBF request."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
