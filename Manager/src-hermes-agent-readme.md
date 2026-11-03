---
tags: [manager-kb, source]
url: https://github.com/NousResearch/hermes-agent (README raw)
type: repo
author: Nous Research
published: undated (MIT, active 2026)
accessed: 2026-10-29
reliability: med (README marketing claims; no code read)
---
# Hermes Agent (Nous Research) README
## Key claims
- Positioned as "the self-improving AI agent": closed learning loop = agent-curated memory with periodic nudges, autonomous skill creation after complex tasks, skills that self-improve during use, FTS5 session search with LLM summarisation, Honcho "dialectic user modeling", compatible with agentskills.io open standard.
- Single gateway process serves Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI; voice-memo transcription; built-in cron with delivery to any platform.
- Chat control commands shared across CLI and messaging: `/new /reset /model /personality /retry /undo /compress /usage /insights /skills`, `/stop` (interrupt current work) or "send a new message", `/status`, `/sethome`.
- Six terminal backends: local, Docker, SSH, Modal, Daytona, Vercel Sandbox (+ Singularity plugin); serverless backends hibernate when idle.
- Subagents with configurable provider/model/limits; scripts calling tools over RPC to "collapse multi-step pipelines into zero-context-cost turns".
- Third-party write-ups (search snippets only, unverified): memory = MEMORY.md + USER.md injected as frozen snapshot at session start; skills created after 5+ tool-call tasks; "agents with 20+ self-created skills complete similar future tasks 40% faster" (unverified).
## Quotable
> a closed learning loop... It creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations

## Used by
[[topic-personal-assistant-agents]], [[topic-remote-mobile-ux]]
