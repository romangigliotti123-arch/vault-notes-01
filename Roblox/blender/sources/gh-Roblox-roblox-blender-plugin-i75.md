---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i75
title: "Roblox/roblox-blender-plugin#75 \"Install dependencies\" button didn't show; thus weird behaviour"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/75"
published: "2025-01-16"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0255
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows"]
---
# gh-Roblox-roblox-blender-plugin-i75

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on the Roblox Blender plugin (Roblox/roblox-blender-plugin#75). Installing from Releases never prompted for dependency install, causing odd OAuth login errors. The reporter hit no errors when installing from the repo's latest version. Maintainer explains some errors and links related issues (#80, #81), including a 429 rate-limit case that is mishandled. Limited relevance to Claude/blender-mcp.

## Claims
- c1: Installing the Roblox Blender plugin from GitHub Releases never showed the 'Install dependencies' button/prompt, leading to odd login behaviour; installing the latest version directly from the repo prompted for dependencies and worked. *(experience, medium; automation-and-creator-workflows)*
- c2: Login (OAuth) failed with a 400 'Bad status line HTTP/1.1 200' from apis.roblox.com/oauth/v1/token; the maintainer suspected the HTTP client rejecting the trailing space in the status line, but could not reproduce it. *(experience, low; automation-and-creator-workflows)*
- c3: Error 'No creators were authorized during login' is expected when no account is selected on the OAuth page, since the add-on would have nowhere to upload. *(doc, high; automation-and-creator-workflows)*
- c4: Error text "'userFacingMessage'" is a bug: that string is a key for looking up the error message in an error object (lib/request_login_details.py), but it was shown literally. Tracked in issue #81. *(doc, medium; automation-and-creator-workflows)*
- c5: Logging in again too quickly after a previous login can make Roblox's API return 429 Too Many Requests while fetching group names; poor error handling then surfaces the same confusing error. Tracked in issue #80. *(experience, medium; automation-and-creator-workflows)*
- c6: Selecting only the user's own account on the OAuth page left the local login web server seemingly offline with no response; cause not determined. *(experience, low; automation-and-creator-workflows)*
- c7: The reporter speculated that dependencies had changed after an earlier install/uninstall of the add-on (possibly after a Blender version change), which may have caused the missing prompt. *(opinion, low; automation-and-creator-workflows)*

## Numbers
- n1: **HTTP status from token endpoint error**: 400 (Bad status line 'HTTP/1.1 200 ') Login failure at https://apis.roblox.com/oauth/v1/token
- n2: **Rate-limit status during login**: 429 Fetching group names after rapid repeat login

## Techniques
- t1: **Install Roblox Blender plugin from repo if Releases build skips dependency prompt**: If the release zip never shows 'Install dependencies', install the latest version from the repo instead. It then prompts for dependencies and login works.
- t2: **Avoid rapid repeat logins**: Wait between login attempts in the plugin to avoid a 429 on the group-name fetch. Select at least one creator/account on the OAuth page to avoid 'No creators were authorized'.

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/80
- https://github.com/Roblox/roblox-blender-plugin/issues/81
- https://github.com/Roblox/roblox-blender-plugin/blob/2eee79ca79bc853b09ebc80bd6df645311ff7704/lib/request_login_details.py
