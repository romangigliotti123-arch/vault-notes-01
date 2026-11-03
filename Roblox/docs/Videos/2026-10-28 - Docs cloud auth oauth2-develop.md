---
title: "Docs: cloud / auth / oauth2-develop"
url: https://create.roblox.com/docs/cloud/auth/oauth2-develop.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / auth / oauth2-develop

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/auth/oauth2-develop.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud OAuth 2.0 implementation guide: authorization code flow with PKCE (recommended for all, required for public clients), code verifier/challenge generation, authorization URL construction, callback handling, token exchange, and calling APIs with the access token.

## Tips
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) **[[anti-exploit-and-security]]** Store the client secret securely and never expose it publicly; bad actors can use it to impersonate your application.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) **[[anti-exploit-and-security]]** Use authorization code flow with PKCE for all clients; it is required for public clients (mobile, browser apps) and improves security over client secret.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) **[[anti-exploit-and-security]]** Generate state as an opaque secure random value and verify it on callback to maintain state and guard the request.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) **[[data-persistence]]** Store the refresh token server-side so you can obtain new access tokens later.

## Numbers
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) Access token lifetime: **15 minutes (expires_in ~899s in example)** (Access token validity period from token endpoint response)
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-develop) Code verifier length: **43 to 128 characters** (Required length range for PKCE code verifier)

## Tools
Roblox Open Cloud, OAuth 2.0, PKCE

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
