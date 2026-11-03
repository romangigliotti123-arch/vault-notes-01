---
title: "Docs: cloud / auth / oauth2-sample"
url: https://create.roblox.com/docs/cloud/auth/oauth2-sample.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / auth / oauth2-sample

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/auth/oauth2-sample.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on a Node.js OAuth 2.0 sample app. Covers registering an app with openid/profile/universe-messaging-service:publish scopes, setting client ID/secret and port via environment variables, installing with npm ci, running it, and how index.js handles the OIDC flow. Authorization code flow without PKCE, so confidential clients only.

## Tips
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample) **[[client-server-and-remotes]]** Use the authorization code flow without PKCE only for confidential clients such as private servers; it is not suitable for public clients.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample) **[[anti-exploit-and-security]]** Store OAuth client ID and secret in environment variables rather than in code, since hardcoding credentials is not recommended.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample) **[[matchmaking-and-teleport]]** If using a non-default port, specify it in the registered redirect URL and set ROBLOX_PORT to match, or the callback will fail.
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample) **[[version-control-and-tooling]]** Environment variables set in a terminal only last for that session; add them to .zshrc or .bashrc to persist them.

## Numbers
- [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample) Default port: **3000** (Default port for the sample app and its redirect URL http://localhost:3000/oauth/callback)

## Tools
Node.js, express, openid-client, npm

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[matchmaking-and-teleport]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
