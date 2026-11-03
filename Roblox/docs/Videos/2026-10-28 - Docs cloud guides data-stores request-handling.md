---
title: "Docs: cloud / guides / data-stores / request-handling"
url: https://create.roblox.com/docs/cloud/guides/data-stores/request-handling.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / data-stores / request-handling

[Open](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page on handling Open Cloud data store API requests: auth headers and error codes, pagination, list filters, allow_missing flag on PATCH, scopes vs prefixes, and Content-MD5 checksums for v1 API.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[client-server-and-remotes]]** Include x-api-key header on all Open Cloud data store requests; missing or incorrect key returns 401, valid key lacking permissions returns 403.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[data-persistence]]** Include Content-Type: application/json and Content-Length headers on create/update requests with bodies; most clients add them automatically.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[data-persistence]]** Handle pagination when calling List Data Store Entries, since results are capped per page and large stores need multiple pages.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[data-persistence]]** Use prefixes in entry names and filter List calls with id.startsWith(); filter syntax is very limited, so check the reference for supported filters.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[data-persistence]]** Leave allow_missing at default false on PATCH updates; updating a never-created entry usually signals a programming logic error.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[data-persistence]]** Prefer key name prefixes over creating non-default scopes to organise data store entries; docs strongly recommend this.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) **[[testing-debugging-and-qa]]** With Open Cloud v1 API, optionally send base64 MD5 content-md5 header to catch data integrity issues; encode body as UTF-8 first if checksum fails.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling) HTTP error codes: **401 = missing/incorrect API key; 403 = valid key lacks permissions** (Open Cloud data store requests with API key auth)

## Tools
Open Cloud API, Python requests, Python hashlib/base64 (MD5 checksum)

## He points to
- Manage API keys (Open Cloud docs)
- Pagination (Open Cloud docs)
- Listing and prefixes (Open Cloud docs)
- Data store filter reference (standard and ordered)

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
