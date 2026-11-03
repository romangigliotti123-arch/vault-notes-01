---
title: "HttpQueue - Forget about rate limiting, focus on the rest!"
url: https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-05-03
views: 69
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# HttpQueue - Forget about rate limiting, focus on the rest!

[Open](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) | Roblox DevForum | 69 views | 2020-05-03

## Summary
Documentation for HttpQueue, a Roblox library (by davness, v1.0.0 RC) that queues HttpService requests to respect rate limits. Covers creating requests, queues with retryAfter cooldowns and concurrency caps, priority levels for Push, type guards, and changelog.

## Tips
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[scripting-and-performance]]** Route external HTTP calls through a queue instead of raw HttpService so rate-limited (429) requests are retried automatically rather than lost.
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[scripting-and-performance]]** Set maxSimultaneousSendOperations no higher than the service's rate limit, per the author's guidance.
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[scripting-and-performance]]** Use retryAfter cooldown matching the service's rate-limit window (example: Trello 10 requests/10 seconds, cooldown 10).
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[scripting-and-performance]]** Use HttpRequestPriority.Prioritary or First sparingly; default first-come-first-serve covers most cases.
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[scripting-and-performance]]** Append a trailing slash to URLs when using query options; library normalizes this from v1.0.0 onward.
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) **[[testing-debugging-and-qa]]** Report bugs; library is a Release Candidate and may not be fully stable.

## Numbers
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) Trello rate limit: **10 requests per 10 seconds per token (Roblox clients)** (Example limit used to configure queue cooldown)
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) Example queue config: **retryAfter cooldown 10s, maxSimultaneousSendOperations 10** (Trello example from docs)
- [page](https://devforum.roblox.com/t/httpqueue-forget-about-rate-limiting-focus-on-the-rest/555587) Library version: **1.0.0 (Release Candidate)** (Current version listed on page; changelog through 1.1.0)

## Tools
HttpQueue (roblox-http-queue library), HttpService, Promise (evaera), t typechecking (Osyris), ProbableAI Documentation Reader plugin, roblox-ts (@rbxts/http-queue)

## He points to
- github.com/ddavness/roblox-http-queue
- ProbableAI Documentation Reader plugin
- evaera Promise implementation
- Osyris t typechecking library

## Topics
[[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
