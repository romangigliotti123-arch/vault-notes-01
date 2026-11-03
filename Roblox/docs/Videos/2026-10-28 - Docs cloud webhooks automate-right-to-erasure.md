---
title: "Docs: cloud / webhooks / automate-right-to-erasure"
url: https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / webhooks / automate-right-to-erasure

[Open](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on automating right-to-erasure (RTBF) requests. Recommends RTBF deletion templates for data store data; otherwise describes a webhook workflow where a locally run Python Discord bot receives Roblox RTBF webhooks, verifies HMAC signatures, and deletes user entries via Open Cloud data store APIs.

## Tips
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[ugc-and-avatar-economy]]** For personal data in data stores, prefer configuring RTBF deletion templates; Roblox deletes matching standard or ordered entries automatically without custom code.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[anti-exploit-and-security]]** Set a custom webhook Secret so you can verify requests are from Roblox; leaking the webhook URL lets attackers send fake messages and trigger deletions.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[anti-exploit-and-security]]** Keep the Discord channel private and restrict webhook URL access to trusted team members only.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[data-persistence]]** Make data store keys identifiable by User ID (e.g. containing user ID as a substring) so the deletion script can find PII, or modify scripts to match your schema.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[data-persistence]]** Create Open Cloud API key with Delete Entry permission for data stores; add Ordered Data Stores Write permission if PII is in ordered data stores.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[anti-exploit-and-security]]** Validate webhook signatures and reject timestamps outside a 300-second window to prevent replay attacks.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[testing-debugging-and-qa]]** Send a test POST with a correctly HMAC-SHA256-signed footer to verify your bot handles erasure requests before going live.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[development-process-and-speed]]** Run the bot locally only and keep the machine on at all times; manually handle missed messages during downtime per the retry policy.
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) **[[ugc-and-avatar-economy]]** Currently only group owners receive RTBF requests for group-owned games, so the group owner must configure the webhook.

## Numbers
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) Webhook replay window: **300 seconds** (Timestamp tolerance for validating Roblox webhook requests)
- [page](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) Python dependency pin: **urllib3==1.26.6** (Pinned in setup for the Discord RTBF bot scripts)

## Tools
Discord (webhook integration, bot application), Python 3 with discord, requests, urllib3 libraries, Open Cloud Data Stores API, Open Cloud Ordered Data Stores API, Creator Dashboard webhooks

## He points to
- Data store right to be forgotten (RTBF)
- RTBF and creators
- Verify webhook security

## Topics
[[anti-exploit-and-security]] [[data-persistence]] [[development-process-and-speed]] [[testing-debugging-and-qa]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
