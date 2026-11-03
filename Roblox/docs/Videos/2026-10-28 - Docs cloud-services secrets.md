---
title: "Docs: cloud-services / secrets"
url: https://create.roblox.com/docs/cloud-services/secrets.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / secrets

[Open](https://create.roblox.com/docs/cloud-services/secrets.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Secrets store: how to add per-game secrets (owner-only, up to 500 per game, 1,024-character limit, domain wildcards), local testing via Local Secrets, and using GetSecret with AddPrefix/AddSuffix in server scripts for HTTP requests.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[anti-exploit-and-security]]** Store API keys and tokens in the Secrets store instead of pasting them into scripts or DataStores, since those approaches carry unnecessary security risks.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[anti-exploit-and-security]]** Scope each secret to a specific domain (e.g. my.example.com) rather than '*', which the docs say is not recommended.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[anti-exploit-and-security]]** Call HttpService:GetSecret() only from server scripts; client scripts get a 'Can't find secret' error.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[anti-exploit-and-security]]** Secret values print as Secret(name), so you cannot accidentally leak the value via print.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[testing-debugging-and-qa]]** Secrets are unavailable in local playtesting; define test values under File > Experience Settings > Security > Local Secrets.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[client-server-and-remotes]]** Make HTTP requests with secrets only on the server; secrets can go in URLs and headers, not in request bodies.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[scripting-and-performance]]** Enable 'Allow HTTP Requests' in Experience Settings > Security before using GetSecret or RequestAsync.
- [page](https://create.roblox.com/docs/cloud-services/secrets) **[[ai-and-tools]]** Open Cloud can also manage secrets programmatically if you prefer automation over the dashboard.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/secrets) Secrets per game limit: **500** (Maximum number of secrets allowed per game)
- [page](https://create.roblox.com/docs/cloud-services/secrets) Secret max length: **1,024 characters** (Maximum character length of a single secret value)

## Tools
Creator Dashboard, Roblox Studio, HttpService:GetSecret, Datatype.Secret (AddPrefix/AddSuffix), HttpService:RequestAsync, Open Cloud

## He points to
- Open Cloud secrets reference documentation and guide

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
