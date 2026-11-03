---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i8
title: "Roblox/roblox-blender-plugin#8 Dependency installation fails - Non-zero exit status 3221225781"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/8"
published: "2023-08-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 3
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #8 on Roblox/roblox-blender-plugin (2023-08-25). User installed the plugin from a GitHub zip as an addon; clicking "Install Dependencies" failed on Windows with subprocess CalledProcessError exit status 3221225781 running Blender's bundled python -m pip --version. Maintainers suggested: confirm button click, check system console, run Blender as admin, reinstall Blender 3.6.2 (3.2 minimum), and install the MS Visual C++ Redistributable (x64). Issue closed for inactivity without a confirmed fix.

## Claims
- c1: Roblox Blender plugin requires clicking 'Install Dependencies' once on first run (per README step 9); plugin needs Blender 3.2 minimum. *(doc, high; blender-roblox-export-import)*
- c2: On Windows, Install Dependencies failed with exit status 3221225781 when running Blender's bundled python -m pip --version; no confirmed fix in thread. *(experience, high; blender-roblox-export-import)*
- c3: Maintainer suggested checking Window > Toggle System Console on Windows to view dependency install output. *(doc, medium; blender-roblox-export-import)*
- c4: Suggested fix attempts: run Blender as administrator, reinstall Blender 3.6.2, install x64 Microsoft Visual C++ Redistributable (hypothesis of missing DLL dependency). *(opinion, low; blender-roblox-export-import)*
- c5: Issue closed for inactivity by maintainer without root cause or resolution recorded. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Exit status**: 3221225781 Non-zero exit from pip --version in bundled Blender 3.2 python on Windows
- n2: **Blender version**: 3.2 minimum, 3.6.2 suggested Plugin reported working on 3.5 and 3.6 per maintainer

## Techniques
- t1: **Diagnose dependency install via system console**: On Windows, open Window > Toggle System Console in Blender, click Install Dependencies, read traceback. Check that bundled python can run -m pip --version.
- t2: **Troubleshoot pip exit code on Windows**: Run Blender as administrator; reinstall Blender; install x64 VC++ Redistributable; retry one step at a time.

### Code: Failing call from plugin lib/install_dependencies.py
```text
subprocess.run([sys.executable, "-m", "pip", "--version"], check=True)
```

## Quotes (brief, for attribution)
> Click Install Dependencies. This is only required the first time the plugin runs  (Roblox)
> subprocess.CalledProcessError: Command returned non-zero exit status 3221225781.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin
- https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
- https://aka.ms/vs/17/release/vc_redist.x64.exe
