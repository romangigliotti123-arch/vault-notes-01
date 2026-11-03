---
title: "Docs: cloud / auth / oauth2-reference"
url: https://create.roblox.com/docs/cloud/auth/oauth2-reference.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / auth / oauth2-reference

[Open](https://create.roblox.com/docs/cloud/auth/oauth2-reference.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Reference for Roblox Open Cloud OAuth 2.0 (beta) endpoints: authorize, token exchange and refresh, introspect, resources, revoke, userinfo, and the OIDC discovery document. Covers token lifetimes, client authentication methods, and identity claims.

## Tips
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[anti-exploit-and-security]]** Identify users by the userinfo sub (Roblox user ID), not name or display name, since users can change both.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[data-persistence]]** Refresh tokens are single-use: store the new refresh token returned on every refresh, or the session is lost.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[anti-exploit-and-security]]** Exchange authorization codes server-side with client_secret; codes expire after 1 minute and work only once.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[anti-exploit-and-security]]** Don't rely on introspect to detect revoked authorization; it reports revoked access tokens as valid until their lifetime ends.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[anti-exploit-and-security]]** Use token/resources for stateful checks of which resources a user granted; use introspect only for stateless validation of token claims.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[anti-exploit-and-security]]** Use PKCE (code_challenge with S256) on the authorize call, and pass a state value to prevent cross-site request forgery.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) **[[common-mistakes]]** Handle a null picture claim in userinfo; avatar headshots may not be generated yet or may have been moderated.

## Numbers
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) Authorization code lifetime: **1 minute, single use** (Redeemed once at token endpoint)
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) Access token lifetime: **15 minutes (expires_in 899)** (Usable multiple times until expiry or revocation)
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-reference) Refresh token lifetime: **90 days** (Single use before it expires, to refresh tokens)

## Tools
Roblox Open Cloud OAuth 2.0 API, OIDC discovery document (.well-known/openid-configuration)

## He points to
- Open Cloud OAuth 2.0 overview (sample app guide)
- https://create.roblox.com/docs/reference/cloud

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
