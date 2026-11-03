---
title: "Docs: cloud / guides / secrets-store"
url: https://create.roblox.com/docs/cloud/guides/secrets-store.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / secrets-store

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/guides/secrets-store.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Open Cloud docs on managing game secrets via the secrets store API. Covers API key/OAuth setup, encrypting values with LibSodium sealed boxes using the universe's public key, and creating, updating, and deleting secrets.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/secrets-store) **[[data-persistence]]** Secrets store API requires an API key with the secret-store system or an OAuth 2.0 app with universe.secret scope before any calls.
- [page](https://create.roblox.com/docs/cloud/guides/secrets-store) **[[anti-exploit-and-security]]** Encrypt secret values with a LibSodium sealed box using the universe public key, then base64-encode, before sending to the API.
- [page](https://create.roblox.com/docs/cloud/guides/secrets-store) **[[anti-exploit-and-security]]** Keep third-party API keys in the Open Cloud secrets store rather than hardcoding them in game scripts, where exploiters could read them.
- [page](https://create.roblox.com/docs/cloud/guides/secrets-store) **[[updates-live-ops]]** Use PATCH with the current key_id to rotate a secret's value without recreating it; delete unused secrets to clean up.

## Tools
Open Cloud secrets store API, LibSodium sealed box, PyNaCl (Python), curl

## Topics
[[anti-exploit-and-security]] [[data-persistence]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
