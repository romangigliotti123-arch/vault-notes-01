---
tags: [manager-kb, source]
url: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files/
type: eng-blog
author: Check Point Research (Aviv Donenfeld, Oded Vanunu)
published: 2026-02-25
accessed: 2026-10-29
reliability: med (SNIPPET ONLY: direct fetch returned HTTP 429; facts from search snippets + secondary mirrors)
---
# Caught in the Hook: RCE and API token exfiltration through Claude Code project files
## Key claims (snippet level)
- CVE-2025-59536: repository-controlled `.claude/settings.json` hooks (e.g. SessionStart) and MCP settings could run shell commands before/without the trust prompt. CVE-2026-21852: project-level `ANTHROPIC_BASE_URL` override sent API traffic, including the API key, to an attacker before the trust dialog was accepted. Secondary sources give fix versions 1.0.111 and 2.0.65 (unverified).
- Search results also show a `claude-cli://` deep-link RCE patched in 2.1.118 (title only).
- Relevance: config files in a cloned or imported directory are executable surface. This host's `claude -p` workers "skip the workspace trust dialog" ([[src-ccdocs-security]]), so a worker started with cwd inside an untrusted repo could load that repo's hooks/MCP.

## Used by
[[topic-agent-security]]
