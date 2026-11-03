---
title: "Docs: cloud / webhooks / webhook-notifications"
url: https://create.roblox.com/docs/cloud/webhooks/webhook-notifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / webhooks / webhook-notifications

[Open](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on webhook notifications: supported triggers (subscriptions, RTBF/erasure, commerce orders, transaction refunds, experiment harm), configuring webhooks in Creator Hub, endpoint requirements, retry policy, testing, and roblox-signature verification with HMAC-SHA256.

## Tips
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[client-server-and-remotes]]** Webhook endpoints must be public HTTPS, accept POST, and return a 2XX within 5 seconds or the delivery counts as failed.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[data-persistence]]** On Transaction Refunded for developer products, manually remove the granted currency or boosts from player save data; Roblox only revokes passes and avatar items.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[anti-exploit-and-security]]** Set a webhook secret and verify roblox-signature: HMAC-SHA256 of 'timestamp.body' in Base64, and reject timestamps outside a window (docs suggest 5 or 10 minutes).
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[anti-exploit-and-security]]** Deduplicate events by NotificationId, and for Commerce Product Order Paid also by the unique commerce order ID, since duplicates are possible.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[common-mistakes]]** Don't rely on third-party tools beyond Discord and Slack for webhooks; Roblox says other tools risk missing notifications.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[data-persistence]]** If you store PII such as user IDs in data stores, handle Right to Erasure requests by deleting that data using the payload's UserId and GameIds.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[development-process-and-speed]]** After 5 failed delivery attempts, Roblox stops retrying and treats the URL as invalid; update the webhook with a reachable URL to resume.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[testing-debugging-and-qa]]** Use the Test Response button on the webhook config page to send a SampleNotification and confirm the endpoint receives requests.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[community-and-discord]]** Discord and Slack webhooks are the officially supported targets for routing Roblox notifications to your team.
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) **[[team-and-budget]]** For group-owned games, only group owners can configure and receive webhook notifications.

## Numbers
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) Max webhooks per experience: **5** (Currently, you can configure up to 5 webhooks in total.)
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) Early Harm Detection window: **24 hours** (Experiment critical harm alert covers the first 24 hours.)
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) Endpoint response timeout: **5 seconds** (Endpoint must return 2XX within 5 seconds.)
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) Delivery retries: **5 attempts, fixed window** (Then Roblox stops and assumes URL invalid.)
- [page](https://create.roblox.com/docs/cloud/webhooks/webhook-notifications) Replay-attack window (code sample): **300 seconds** (Sample server rejects requests with timestamp older than 300s.)

## Tools
Creator Hub webhook configuration, Discord webhooks, Slack webhooks, Open Cloud API (data stores), Express.js sample server

## He points to
- RTBF and Creators
- Automating Right to Erasure Requests Deletion
- Subscription reference
- Payload Schema
- Verify webhook security
- Test webhooks

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[community-and-discord]] [[data-persistence]] [[development-process-and-speed]] [[team-and-budget]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
