---
tags: [manager-kb, source]
url: https://www.wiz.io/blog/s1ngularity-supply-chain-attack
type: eng-blog
author: Wiz Research
published: 2025-08-27 (attack on 2025-08-26)
accessed: 2026-10-29
reliability: high (incident write-up; counts differ between vendors)
---
# s1ngularity: Nx npm compromise weaponised local AI CLIs
## Key claims
- 2025-08-26 malicious `nx` / `@nx/*` versions on npm ran a postinstall script that invoked installed AI CLIs (Claude, Gemini, Q) with `--dangerously-skip-permissions`, `--yolo`, `--trust-all-tools` to hunt for secrets on the filesystem.
- Targets: crypto wallets, `.env`, SSH keys, GitHub/npm tokens, `gh auth` tokens, `.npmrc`. Exfil: public repos created in the victim's GitHub account (`s1ngularity-repository*`) with base64 data ("trivially decodable ... effectively public").
- Impact (Wiz): >1,000 valid GitHub tokens, dozens of cloud/npm creds, ~20,000 files; second phase made private repos public (>400 users/orgs, >5,500 repos). Other vendors give different counts; AI-mediated theft succeeded in a minority of cases because provider guardrails sometimes refused.
- Persistence/side effect: `sudo shutdown -h 0` appended to ~/.bashrc and ~/.zshrc.
- Lesson for hosts that run AI CLIs with elevated rights: any malicious package or skill can reuse the host's own agent (and its bypass flag) as the exfil tool.
## Quotable
> base64-encoding is trivially decodable, meaning that this data should be treated as effectively public.

## Used by
[[topic-agent-security]]
