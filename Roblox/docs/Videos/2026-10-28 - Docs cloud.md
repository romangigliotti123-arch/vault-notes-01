---
title: "Docs: cloud"
url: https://create.roblox.com/docs/cloud.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud API reference landing page. Explains that Open Cloud exposes Roblox resources via REST APIs, organised by feature and by domain. Recommends API key or OAuth 2.0 auth over legacy cookie-based APIs, lists get-started steps, and notes HttpService in-game access to a subset of endpoints.

## Tips
- [page](https://create.roblox.com/docs/cloud) **[[ai-and-tools]]** Use API keys or OAuth 2.0 for Open Cloud calls; they have strong stability guarantees and regular updates. API keys are the easiest way to start.
- [page](https://create.roblox.com/docs/cloud) **[[version-control-and-tooling]]** Avoid legacy Open Cloud APIs for production: they use cookie auth, may change without notice, and have minimal stability guarantees.
- [page](https://create.roblox.com/docs/cloud) **[[ai-and-tools]]** Test Open Cloud endpoints with Postman using the OpenAPI descriptions, or with the OAuth 2.0 sample app, before writing integration code.
- [page](https://create.roblox.com/docs/cloud) **[[data-persistence]]** Use Open Cloud to work with DataStores and MemoryStores from external tools, such as automation scripts or web apps.

## Tools
Open Cloud REST APIs, API keys, OAuth 2.0, Postman

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[data-persistence]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
