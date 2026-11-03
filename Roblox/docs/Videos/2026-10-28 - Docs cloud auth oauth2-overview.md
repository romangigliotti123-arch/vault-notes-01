---
title: "Docs: cloud / auth / oauth2-overview"
url: https://create.roblox.com/docs/cloud/auth/oauth2-overview.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / auth / oauth2-overview

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/auth/oauth2-overview.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud OAuth 2.0 overview: who can use it (13+ account to authorize, ID verification to register/publish apps), roles, authorization code flow and PKCE, OpenID Connect identity layer, and steps to register and implement an app.

## Tips
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) **[[ai-and-tools]]** Use the OAuth 2.0 grant to let third-party tools access your games without sharing your password or personal credentials; you choose the permitted resources.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) **[[anti-exploit-and-security]]** Use PKCE with the authorization code flow to reduce risk of leaking the authorization code and to prevent CSRF attacks.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) **[[anti-exploit-and-security]]** Generate a unique, cryptographically random code verifier for every authorization request and hash it with SHA-256 to make the code challenge.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) **[[anti-exploit-and-security]]** Confidential clients should send client ID, secret and code challenge; public clients pass client ID and code challenge without a client secret.

## Numbers
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) Minimum account age to authorize OAuth 2.0 apps: **13+** (Required for users authorizing OAuth 2.0 apps)
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview) Developer requirement to register/publish OAuth apps: **ID verified** (Required to register and publish OAuth 2.0 apps)

## Tools
Open Cloud APIs, Creator Dashboard

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
