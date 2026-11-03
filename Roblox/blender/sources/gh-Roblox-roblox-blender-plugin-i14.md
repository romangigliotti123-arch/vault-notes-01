---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i14
title: "Roblox/roblox-blender-plugin#14 Internal client error. No module named 'pyjwt_key_fetcher'"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/14"
published: "2023-08-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i14

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #14 on Roblox/roblox-blender-plugin (2023-08-29). Users hit "Internal client error: No module named 'pyjwt_key_fetcher'" right after clicking CONFIRM AND GIVE ACCESS in login. Maintainer says the dependency should install via "Install dependencies" on first run; advises reinstall and watching the Blender console. Root cause per reporter: antivirus blocking pyjwt-key-fetcher during dependency install. Maintainer confirms it is a legitimate dependency used to verify id-token signatures via kid lookup.

## Claims
- c1: Roblox Blender plugin login fails with 'Internal client error: No module named pyjwt_key_fetcher' right after CONFIRM AND GIVE ACCESS step. *(doc, high; blender-roblox-export-import)*
- c2: Dependencies for the Roblox Blender plugin are installed via the 'Install dependencies' button on first plugin run; missing module indicates install did not complete. *(doc, high; blender-roblox-export-import)*
- c3: Antivirus blocking pyjwt-key-fetcher during dependency install caused the failure; reporter fixed it by fully disabling antivirus during install, exclusions did not help. *(experience, medium; blender-roblox-export-import)*
- c4: Maintainer states pyjwt-key-fetcher is a legitimate dependency, used to pick the public key by id-token kid from Roblox's certificate endpoint to verify token signature. *(doc, high; blender-roblox-export-import)*
- c5: Debugging tip: on Windows enable Window > Toggle System Console; on macOS start Blender from a terminal to view install errors. *(doc, high; automation-and-creator-workflows)*

## Techniques
- t1: **Fix login dependency error**: Click Install dependencies in plugin; if error persists, uninstall and reinstall plugin, watch Blender console during install for errors; temporarily disable antivirus during install.

## Quotes (brief, for attribution)
> pyjwt-key-fetcher is not malicious - it is a valid required dependency of the plugin that is supposed to be installed when the plugin first runs.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/blob/85baac63f2343a97065ed4dc35b53cbe82a15cc5/lib/request_login_details.py#L133C1-L134C48
- https://www.rfc-editor.org/rfc/rfc7515.html#section-4.1.4
