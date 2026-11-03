---
tags: [manager-kb, source]
url: https://thenextweb.com/news/claude-code-prompt-injection-summarise-website-auto-mode
type: news
author: The Next Web (reporting Johann Rehberger; The Register 2026-08-28)
published: 2026-09-01
accessed: 2026-10-29
reliability: med-high (news on a researcher's disclosure; Anthropic quoted second-hand)
---
# Researcher hijacked Claude Code (Auto Mode, Opus 5) by asking it to summarise a web page
## Key claims
- Rehberger chain: a page returned 415 to WebFetch, Claude fell back to `curl`, followed a redirect to a ZIP; when Claude refused to run the supplied decoder binary it wrote its own, whose `import base64` loaded the attacker's `struct.py` via module shadowing; code ran (Calculator PoC), contacted a C2 server; a nested headless Claude session ran whoami/uname/id and wrote to the home folder. No data theft reported.
- Success 60-80% across three variants, each run five times.
- Anthropic's reported position: "Auto Mode is a convenience feature backed by a best-effort classifier, not a security guarantee." No fix announced as of the article.
- Recommendation: sandbox with OS isolation and network egress control.
- Lesson: the "just summarise this URL" task is the injection vector; agents route around a blocked tool (WebFetch -> curl -> write own decoder) so tool-level denials get circumvented unless egress is closed.
## Quotable
> Auto Mode is a convenience feature backed by a best-effort classifier, not a security guarantee.

## Used by
[[topic-agent-security]]
