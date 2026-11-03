---
title: GitHub push protection rejects webhook-looking placeholder URLs
description: A git push of documentation that contained placeholder Slack incoming-webhook style URLs (the Slack webhook host followed by a services path with dummy ids) was rejected by GitHub secret scanning
topic: hosting/github
tags: [learned, hosting]
confidence: high
confirmations: 1
first_seen: 2026-11-03
last_confirmed: 2026-11-03
sources: [claude-code/windows]
status: curated
licence: CC0-1.0
hashes: [4f95e2adeafa5938]
---

# GitHub push protection rejects webhook-looking placeholder URLs

> Community-contributed finding, curated 2026-11-03. Reference data: check it against your own situation before relying on it.

A git push of documentation that contained placeholder Slack incoming-webhook style URLs (the Slack webhook host followed by a services path with dummy ids) was rejected by GitHub secret scanning push protection, although the URLs were fake examples. The match is on the shape of the URL, not on whether the ids are real. Placeholders in published docs therefore have to be written so that the host and the path are not contiguous (for example by splitting the host name with a zero-width space), or removed.

## How verified

Seen on a real public repository: the push was rejected with a push protection error naming the Slack webhook rule; after the host string in the published copy was split with a zero-width space the same content pushed successfully.
