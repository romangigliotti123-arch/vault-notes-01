---
title: "Docs: cloud-services / http-service"
url: https://create.roblox.com/docs/cloud-services/http-service.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / http-service

[Open](https://create.roblox.com/docs/cloud-services/http-service.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on HttpService: enabling HTTP requests in Studio, using it in plugins, calling a subset of Open Cloud endpoints with an API key stored in Secrets, limits (2500 Open Cloud requests/min per server), allowed headers and ports, best practices (pcall, exponential backoff, batching, HTTP/2), and the Observability Dashboard.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[scripting-and-performance]]** Enable 'Allow HTTP Requests' under File > Experience Settings > Security before GetAsync, PostAsync or RequestAsync will work; it is off by default.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[anti-exploit-and-security]]** Store Open Cloud API keys in the Creator Hub secrets store and read them with HttpService:GetSecret; the x-api-key header must be a Secret.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[anti-exploit-and-security]]** Use a secure pre-shared secret or similar auth on your own endpoints so bad actors cannot pose as your Roblox servers.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[client-server-and-remotes]]** Make HTTP calls only from the server; wrap them in pcall and plan for failure, validating and sanitising all external data.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[optimization-and-streaming]]** Stay under 2500 Open Cloud requests per minute per game server; exceeding it stalls request methods for about 30 seconds.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[development-process-and-speed]]** Retry recoverable errors with exponential backoff: wait 2s, then 4s, 8s, and so on between attempts.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[optimization-and-streaming]]** Batch data into one request where the API offers a bulk endpoint, instead of one request per player; use RequestAsync to put data in the body.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[optimization-and-streaming]]** Send header names in lowercase, since HTTP/2 requires it; HttpService uses HTTP/2 automatically when available.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[common-mistakes]]** Only x-api-key and content-type headers are allowed; only HTTPS works, and ports below 1024 (except 80 and 443) plus port 1194 are blocked.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[common-mistakes]]** Do not use '..' in URL path parameters; data stores or entries containing that string are inaccessible from HttpService.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[analytics-metrics]]** Use the Observability Dashboard to track request count and response time per request type and status to diagnose failing endpoints.
- [page](https://create.roblox.com/docs/cloud-services/http-service) **[[trend-research-and-validation]]** Plugins need user permission per web address; users can revoke it anytime in Plugin Management, so design plugin fallbacks for denied access.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/http-service) Open Cloud requests per minute per game server: **2500** (Exceeding it stalls request methods for around 30 seconds)
- [page](https://create.roblox.com/docs/cloud-services/http-service) Non-Open Cloud HTTP requests per minute: **500** (Open Cloud requests do not count toward this shared limit)
- [page](https://create.roblox.com/docs/cloud-services/http-service) Exponential backoff intervals: **2s, 4s, 8s, ...** (Wait between retries of recoverable errors)
- [page](https://create.roblox.com/docs/cloud-services/http-service) Blocked ports: **1194 and all ports below 1024 except 80 and 443** (Blocked ports return 403 Forbidden or ERR_ACCESS_DENIED)

## Tools
Roblox Studio, Creator Hub secrets store, Open Cloud API, Observability Dashboard, Plugin Management window

## He points to
- Rate Limits (Open Cloud documentation)
- Secrets stores (Creator Hub documentation)

## Topics
[[analytics-metrics]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[development-process-and-speed]] [[optimization-and-streaming]] [[scripting-and-performance]] [[trend-research-and-validation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
