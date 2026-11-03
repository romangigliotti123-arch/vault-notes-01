---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-code/security/advisories (+ GHSA-4p2j-qj3c-6x84, GHSA-fg94-h982-f3mm, GHSA-pq7j-f95f-qfcv)
type: advisory
author: Anthropic (GitHub Security Advisories)
published: 2026-05 .. 2026-10
accessed: 2026-10-29
reliability: high (vendor advisories; list page + 3 advisories opened)
---
# Claude Code security advisories, 2026 sample
## Key claims
- List page (10 shown): TOCTOU in Edit tool writes outside workspace (High, 2026-10-26, GHSA-5xjx-9qx6-jcrv); uncontrolled search path / malicious git executable (High, 2026-10-13); plugin commit-SHA pin bypass (High, 2026-10-09); write-time symlink TOCTOU arbitrary file write (High, 2026-10-05, GHSA-5j29-h97v-84ch); sandbox escape via git worktree path confusion (High, 2026-06-25); out-of-band exfil via pre-approved huggingface.co in WebFetch (Moderate, 2026-06-13); managed settings not applied when stored API key preferred (Low, 2026-09-29); Windows LPE via directory junction in CoworkVMService (High, 2026-05-06). Titles/dates from the list; bodies read only for the three below.
- GHSA-4p2j-qj3c-6x84 (CVE-2026-88066): WINDOWS-only (Claude Desktop). `git.exe` spawned without absolute path, so a malicious `git.exe` in an opened project dir runs; fixed in Desktop 1.8089.0. Lesson: never open untrusted repos/dirs as a working dir on Windows.
- GHSA-fg94-h982-f3mm (CVE-2026-54316): bare `huggingface.co` pre-approved for WebFetch; attacker-controlled repo URLs counted as downloads = covert exfil channel; needed injected content; fixed in 2.1.163.
- GHSA-pq7j-f95f-qfcv (CVE-2026-86063): plugin install verified the pinned SHA only by `git checkout` (a SHA-shaped branch could win); fixed in 2.1.179. Lesson: pinning plugin versions needs verification of HEAD.
- Pattern: the harness itself keeps having path/allowlist bugs; auto-update and a version floor matter; permission prompts are not a perfect boundary.

## Used by
[[topic-agent-security]]
