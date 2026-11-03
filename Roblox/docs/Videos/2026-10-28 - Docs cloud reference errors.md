---
title: "Docs: cloud / reference / errors"
url: https://create.roblox.com/docs/cloud/reference/errors.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / reference / errors

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/reference/errors.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference page for Open Cloud API error responses. Covers the gateway error format shared by v1 and v2, the v2 standard error shape and code table (HTTP status mapping), and the three inconsistent v1 error formats with their code table.

## Tips
- [page](https://create.roblox.com/docs/cloud/reference/errors) **[[common-mistakes]]** Don't assume one error shape: v1 endpoints return three different formats, so parse both 'error' and 'code' keys and the validation-style 'errors' object.
- [page](https://create.roblox.com/docs/cloud/reference/errors) **[[anti-exploit-and-security]]** Gateway errors with code 0 (e.g. 'Invalid API Key') mean auth/routing failed before the endpoint ran; check the key and its scopes first.
- [page](https://create.roblox.com/docs/cloud/reference/errors) **[[testing-debugging-and-qa]]** Use the HTTP status and code string to branch handling: retry RESOURCE_EXHAUSTED (429) with backoff, and treat UNAVAILABLE (503) and INTERNAL (500) as transient server-side failures.
- [page](https://create.roblox.com/docs/cloud/reference/errors) **[[data-persistence]]** DataStore calls can fail with NOT_FOUND (404) for missing entries and ABORTED (409) on conflicts; handle both explicitly rather than treating them as fatal.

## Numbers
- [page](https://create.roblox.com/docs/cloud/reference/errors) v2 error codes mapped to HTTP status: **INVALID_ARGUMENT 400, PERMISSION_DENIED 403, NOT_FOUND 404, ABORTED 409, RESOURCE_EXHAUSTED 429, CANCELLED 499, INTERNAL 500, NOT_IMPLEMENTED 501, UNAVAILABLE 503** (Open Cloud v2 standard error code table)
- [page](https://create.roblox.com/docs/cloud/reference/errors) v1 error codes with extra INSUFFICIENT_SCOPE: **INVALID_ARGUMENT 400, INSUFFICIENT_SCOPE 403, PERMISSION_DENIED 403, NOT_FOUND 404, ABORTED 409, RESOURCE_EXHAUSTED 429, CANCELLED 499, INTERNAL 500, NOT_IMPLEMENTED 501, UNAVAILABLE 503** (Open Cloud v1 error table; same statuses as v2 plus a 403 variant)

## Tools
Open Cloud v1 API, Open Cloud v2 API

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[data-persistence]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
