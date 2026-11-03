---
title: "Docs: cloud-services / data-stores / right-to-be-forgotten"
url: https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / right-to-be-forgotten

[Open](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Hub docs on Right to be Forgotten (RTBF) for data stores. Explains deletion templates using {UserId} tokens, eligibility rules, configuring templates via Data Stores Manager or the Open Cloud Configs API, and publishing steps and best practices.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Define RTBF deletion templates for every data store/key holding user data; automated RTBF only removes data matching templates. Up to 100 templates allowed.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Use only standard data stores or ordered data stores for user data; whole-store deletion is supported for standard data stores only.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Include the user ID in the data store Name or Scope using a static pattern like User_{UserId}, so it can be matched.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** The {UserId} token is case-sensitive; variants like {userId} are rejected. Match the exact token.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Set scope_pattern to "global" when the data store uses the default scope; blank or omitted scope defaults to global.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Compare template patterns against live Luau usage in Data Stores Manager before publishing, to catch mismatches.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** Test RTBF end-to-end on a test game with a dummy account populated with data, request deletion, and confirm the data is removed.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[data-persistence]]** After going live, verify that data for each RTBF request is removed within 30 days of the request appearing in your Roblox messages.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[ab-testing-and-experiments]]** Publishing a config draft is irreversible except by restoring a previous version; verify the draft with GET before POST publish.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) **[[common-mistakes]]** Do not rely on RTBF automation if user ID is absent from key names or scopes; such entries are ineligible for automated deletion.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) Max RTBF deletion templates: **100** (Up to 100 templates to identify a game's user data)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten) RTBF deletion window: **30 days** (Verify data removed within 30 days of RTBF request)

## Tools
Data Stores Manager (Creator Hub), Open Cloud Configs API, curl

## He points to
- Manage API keys (Creator Hub)
- Cloud API reference
- Experience configs guide

## Topics
[[ab-testing-and-experiments]] [[common-mistakes]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
