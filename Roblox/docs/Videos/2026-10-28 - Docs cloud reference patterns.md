---
title: "Docs: cloud / reference / patterns"
url: https://create.roblox.com/docs/cloud/reference/patterns.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / reference / patterns

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/reference/patterns.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Open Cloud API patterns reference: how to form request URLs with path and query parameters, Content-Length/Content-Type headers, pagination via maxPageSize/nextPageToken/pageToken, multiple resource paths, long-running Operation objects polled with exponential backoff, and inventory-items filter syntax.

## Tips
- [page](https://create.roblox.com/docs/cloud/reference/patterns) **[[code-architecture-and-frameworks]]** Use maxPageSize and follow nextPageToken until it is empty or omitted to retrieve all pages of results.
- [page](https://create.roblox.com/docs/cloud/reference/patterns) **[[code-architecture-and-frameworks]]** Keep the same query parameters (apart from pageToken) across paginated requests; changing any filter returns a 400 error.
- [page](https://create.roblox.com/docs/cloud/reference/patterns) **[[code-architecture-and-frameworks]]** Include Content-Length and Content-Type headers on requests with JSON bodies; most HTTP clients add them automatically.
- [page](https://create.roblox.com/docs/cloud/reference/patterns) **[[code-architecture-and-frameworks]]** For long-running operations, poll the Operation path with exponential backoff (e.g. 1s, 2s, 4s) until done is true.

## Numbers
- [page](https://create.roblox.com/docs/cloud/reference/patterns) Example maxPageSize: **25 (docs examples); 100 in inventory example** (Page size parameter used in pagination examples)
- [page](https://create.roblox.com/docs/cloud/reference/patterns) Polling backoff example: **maxRetries 10, initial delay 1s, multiplier 2** (Example PollForResults exponential backoff settings)

## Tools
Open Cloud API

## Topics
[[code-architecture-and-frameworks]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
