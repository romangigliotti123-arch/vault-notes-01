---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i112
title: "Roblox/roblox-blender-plugin#112 Can't Login - Receiving error \"Login request failed. Cannot connect to host apis.roblox.com:443 ssl:default"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/112"
published: "2026-04-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows"]
---
# gh-Roblox-roblox-blender-plugin-i112

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on the Roblox Blender plugin: login fails after Roblox authorization with "Cannot connect to host apis.roblox.com:443 ... [Could not contact DNS servers]". Reporter's workaround: delete the bundled aiodns folder in the add-on's dependencies-public directory and restart Blender. Commenters report it worked, and that on Blender 5.2 the folder is named dependencies_public. One 5.2.0 LTS user says it still fails. Unofficial, no maintainer response shown.

## Claims
- c1: Roblox Blender plugin login fails after authorize with 'Cannot connect to host apis.roblox.com:443 ssl:default [Could not contact DNS servers]' on Windows; reported on Blender 5.1 and 4.5.8. *(experience, high; automation-and-creator-workflows)*
- c2: Reporter's workaround: delete the bundled aiodns folder in the plugin's dependencies-public directory, restart Blender, retry login. Two commenters say it worked. *(experience, medium; automation-and-creator-workflows)*
- c3: Downgrading Blender 5.1 to 4.5.8 and installing all requirements.txt packages did not fix the login error (reporter). *(experience, medium; automation-and-creator-workflows)*
- c4: On Blender 5.2, the add-on folder is named dependencies_public (underscore), not dependencies-public; the aiodns deletion must target that path. *(experience, medium; automation-and-creator-workflows)*
- c5: Blender 5.2.0 LTS user reports the login error persists even after the aiodns workaround. *(experience, medium; automation-and-creator-workflows)*
- c6: After the workaround, the plugin's Login button still shows on Blender startup; clicking it logs in automatically without reauthorization (commenter). *(experience, low; automation-and-creator-workflows)*
- c7: Reporter's cause guess that aiohttp or Blender has problems with aiodns is opinion; no maintainer confirmation appears in the thread. *(opinion, low; automation-and-creator-workflows)*
- c8: Reporter spent about 4.5 hours troubleshooting; another commenter spent almost 5 hours. *(experience, low; automation-and-creator-workflows)*

## Numbers
- n1: **Failing host and port**: apis.roblox.com:443 
- n2: **Blender versions tested**: 5.1 (failed), 4.5.8 (failed per reporter), 5.2.0 LTS (failed per dbaccello) 
- n3: **Time spent troubleshooting**: ~4.5 h (reporter), ~5 h (commenter) 
- n4: **Dependency folder names**: dependencies-public (pre-5.2), dependencies_public (5.2) 

## Techniques
- t1: **Delete bundled aiodns to fix plugin login**: Open Blender config addons folder: %APPDATA%\Blender Foundation\Blender\<version>\scripts\addons\roblox-blender-plugin\dependencies-public (or dependencies_public on 5.2). Delete the aiodns folder. Restart Blender. Click Login again.

### Code: Path to the bundled dependencies folder where the reporter deleted aiodns (5.2 uses underscore name)
```text
C:\Users\(your username)\AppData\Roaming\Blender Foundation\Blender\5.2\scripts\addons\roblox-blender-plugin\dependencies_public
# delete the 'aiodns' folder inside, then restart Blender
```

## Quotes (brief, for attribution)
> I figured out how to fix the issue... then your pc or blender is having issues with using aiohttp. Find the folder named aiodns and delete it.  (Roblox)
> For Blender 5.2, I think they renamed "dependencies-public" to "dependencies_public"  (Roblox)
> Does not work with Blender 5.2.0 LTS  (Roblox)

## Contradictions flagged
- Deleting aiodns in dependencies-public fixes the login error. (vs On Blender 5.2 the folder is dependencies_public, and a 5.2.0 LTS user reports the error persists (possibly wrong path or a separate 5.2 issue, per cavxvac).)
- Downgrading to Blender 4.5.8 was tried as a fix path. (vs Reporter says the error occurred on 5.1 and downgrading alone didn't help, so the aiodns deletion, not the version, is what the thread credits.)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/112
- https://github.com/Roblox/roblox-blender-plugin
- authorize.roblox.com
- apis.roblox.com
- aiohttp
- aiodns
- requirements.txt
