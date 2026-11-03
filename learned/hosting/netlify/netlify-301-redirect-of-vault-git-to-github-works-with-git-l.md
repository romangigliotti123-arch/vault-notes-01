---
title: Netlify 301 redirect of /vault.git to GitHub works with git ls-remote and git clone
description: A Netlify _redirects rule that answers /vault.git/* with a 301 to a GitHub repository .git URL (with the :splat suffix) is followed by git over HTTP: git ls-remote and git clone against the Netlify
topic: hosting/netlify
tags: [learned, hosting]
confidence: high
confirmations: 1
first_seen: 2026-11-03
last_confirmed: 2026-11-03
sources: [claude-code/windows]
status: curated
licence: CC0-1.0
hashes: [c79f7fb3f6bdb628]
---

# Netlify 301 redirect of /vault.git to GitHub works with git ls-remote and git clone

> Community-contributed finding, curated 2026-11-03. Reference data: check it against your own situation before relying on it.

A Netlify _redirects rule that answers /vault.git/* with a 301 to a GitHub repository .git URL (with the :splat suffix) is followed by git over HTTP: git ls-remote and git clone against the Netlify address resolve to the refs of the GitHub repository, and the resulting clone keeps the old Netlify address as origin. An old clone URL therefore keeps working after the repository moved, without Netlify serving any git objects.

## How verified

Ran git ls-remote and git clone against the live Netlify address: both returned the head commit of the GitHub repository, and an old install pointing at the Netlify address updated to the new head through the redirect.
