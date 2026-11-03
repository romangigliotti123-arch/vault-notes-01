---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md
type: official-doc
author: Anthropic
published: undated (computer_toolset_20260801 revision, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official API doc)
---
# Computer use tool (Claude API)
## Key claims
- Client-side toolset: you run the loop; screenshots/files stay in your environment. One `computer_toolset_20260801` entry exposes 17 member tools (screenshot, clicks, type, zoom, ...). Claude may return a BATCH of actions (e.g. click, type, screenshot) in one response; every tool_use block must be answered with a tool_result carrying `toolset_name: "computer"` or the request is rejected; Claude "typically finishes a batch with screenshot".
- Reference environment = virtual X11 display (Xvfb) + desktop + tool implementations + agent loop. (Wayland is not what the reference uses; our CachyOS box uses ydotool + spectacle instead.)
- Safety recommendations: dedicated VM/container with minimal privileges; ask a human to confirm decisions with real-world consequences or requiring affirmative consent (cookies, financial transactions, ToS); prompt injection from web pages/images is possible, classifiers scan returned screenshots.
- Prompting tips: "Claude sometimes acts as if its actions succeeded without explicitly checking their results" - instruct "After each step, take a screenshot and carefully evaluate if you have achieved the right outcome"; give example screenshots for repeatable UI tasks; if credentials are needed, pass them in tagged blocks (but logins raise risk).
## Quotable
> Claude sometimes acts as if its actions succeeded without explicitly checking their results.

## Used by
[[topic-cross-device-agent-control]], [[topic-remote-mobile-ux]]
