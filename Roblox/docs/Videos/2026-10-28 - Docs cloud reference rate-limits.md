---
title: "Docs: cloud / reference / rate-limits"
url: https://create.roblox.com/docs/cloud/reference/rate-limits.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / reference / rate-limits

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/reference/rate-limits.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API rate-limit reference: how to discover limits (docs Limits section, x-ratelimit headers), how limits differ for API keys (per owner, shared across keys) vs OAuth 2.0 (per access token), in-game HttpService cap, and how to handle HTTP 429 with retry-after or exponential backoff.

## Tips
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) **[[data-persistence]]** Handle HTTP 429 in all code calling Roblox Cloud endpoints; undocumented limits may also apply for DDoS protection and stability.
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) **[[scripting-and-performance]]** On HTTP 429, honour the retry-after header as the retry guideline; if absent, use exponential backoff.
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) **[[scripting-and-performance]]** Monitor x-ratelimit-remaining and x-ratelimit-reset response headers to pace requests before hitting 429s.
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) **[[scripting-and-performance]]** In-game HttpService calls also count toward the fixed 500 HTTP requests per minute limit per game server.

## Numbers
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) In-game HttpService limit: **500 HTTP requests per minute per Roblox game server** (Fixed cap; Cloud API calls from HttpService count toward it)
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) Example x-ratelimit-limit: **1000, 1000;w=60, 1000;w=60** (Example header; multiple values for different time windows)
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) Example x-ratelimit-remaining: **998** (Example header value)
- [page](https://create.roblox.com/docs/cloud/reference/rate-limits) Example x-ratelimit-reset: **20 seconds** (Example: seconds until quota resets to full limit)

## Tools
Roblox Cloud API, HttpService, Developer Forum

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[development-process-and-speed]] [[scripting-and-performance]] [[team-and-budget]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
