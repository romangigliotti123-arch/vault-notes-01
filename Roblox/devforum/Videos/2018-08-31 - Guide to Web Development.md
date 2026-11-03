---
title: "Guide to Web Development"
url: https://devforum.roblox.com/t/guide-to-web-development/173780
creator: Roblox DevForum
official: false
advice_density: low
date: 2018-08-31
views: 373
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Guide to Web Development

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/guide-to-web-development/173780) | Roblox DevForum | 373 views | 2018-08-31

## Summary
TechSpectrum's web-dev tutorial for Roblox users: setting up Node.js, Git, and Express with MongoDB (mLab) to build a custom REST API that talks to Roblox and Discord. Covers HTTP methods and status codes, SQL vs NoSQL tradeoffs, and security middleware (rate limit, sanitizer, Helmet). Mostly backend tooling, not game-design advice.

## Tips
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) **[[anti-exploit-and-security]]** Add express-rate-limit to your API; without it, attackers can brute-force your auth token. Tune max requests per window to your traffic.
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) **[[anti-exploit-and-security]]** Sanitize incoming request data with express-sanitizer and set security headers with helmet to block basic attacks.
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) **[[anti-exploit-and-security]]** Keep secrets like database URIs and API secrets in environment variables (process.env), not hardcoded in source.
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) **[[anti-exploit-and-security]]** Develop with security in mind and keep up with current attack methods (DoS, CSRF, XSS, MITM, brute force, social engineering).

## Numbers
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) Free database storage: **500 MB per mLab sandbox database (unlimited databases)** (mLab free MongoDB hosting used in the tutorial)
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) Rate limit example: **max 500 requests per window** (express-rate-limit config; windowMs written as 15*10000 but described as 15 minutes)
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) Default new user cash: **100** (Mongoose User schema default in example)
- [page](https://devforum.roblox.com/t/guide-to-web-development/173780) Clans hosted by author: **over 40 clans, 100 to 300,000 users** (author's clan database hosting experience)

## Tools
Node.js, Express, MongoDB, Mongoose

## Topics
[[anti-exploit-and-security]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[luau-language-and-types]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
