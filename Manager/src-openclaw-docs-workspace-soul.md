---
tags: [manager-kb, source]
url: https://docs.openclaw.ai/concepts/agent-workspace.md ; /concepts/soul.md ; /reference/templates/SOUL.md ; /automation/standing-orders.md ; /reference/templates/HEARTBEAT.md ; /gateway/heartbeat.md
type: official-doc
author: OpenClaw project (formerly Clawdbot, Moltbot)
published: undated (docs fetched 2026-10-29; heartbeat retired in current docs)
accessed: 2026-10-29
reliability: high (project's own docs, raw markdown; may be AI-assisted prose)
---
# OpenClaw docs: workspace files, SOUL.md, standing orders, heartbeat
## Key claims
- Workspace = plain Markdown files the model sees: AGENTS.md (operating rules, "Human only" writes, injected every session), SOUL.md (persona/tone/boundaries, every session), USER.md (user model; "dated active or superseded directives"; own 4,000-char budget), IDENTITY.md, BOOT.md (startup checklist), BOOTSTRAP.md (first-run ritual, delete after), MEMORY.md (curated long-term, main private session only), memory/YYYY-MM-DD.md daily logs (read today+yesterday), skills/. Injection truncation: `bootstrapMaxChars` 20,000 per file, `bootstrapTotalMaxChars` 60,000. Docs advise making the workspace a private git repo. Workspace is "the default cwd, not a hard sandbox".
- SOUL.md guide: "Short beats long. Sharp beats vague." Do NOT make it "a life story, a changelog, a security policy dump, or a wall of vibes with no behavioral effect". Good rules: have a take, skip filler, be funny when it fits, call out bad ideas early. Bad: "maintain professionalism at all times". Warning: "Personality is not permission to be sloppy. Keep AGENTS.md for operating rules; keep SOUL.md for voice, stance, and style."
- SOUL.md template: "Be resourceful before asking. Read the file, check the context, search for it. Come back with answers, not questions." "Earn trust through competence... Check before public or outbound actions nobody asked for." "Never send half-baked replies to messaging surfaces." "If you change this file, tell the user - it's your soul, and they should know." "Each session, you wake up fresh. These files are your memory."
- Standing orders: permanent operating authority per "program" with Scope, Trigger, Approval gate, Escalation, plus "What NOT to do". Put in AGENTS.md. Pair with scheduled automations ("standing orders without triggers become suggestions"). Execute-Verify-Report loop: "'Done' without verification is not acceptable. Prove it." "retry once... 3 attempts max, then escalate." Best practice: "Start with narrow authority and expand as trust builds"; "Review agent logs weekly".
- Heartbeat: formerly a 30-minute poll with a HEARTBEAT.md checklist (agent answers HEARTBEAT_OK when nothing to do; skipped if the file is effectively empty). In current docs HEARTBEAT.md is RETIRED: monitoring is now ordinary scheduled "automation jobs" with their own schedule, prompt, scratch notes, delivery settings and run history; `openclaw doctor --fix` migrates. Migration note: heartbeat-specific duplicate suppression was removed.
## Quotable
> Short beats long. Sharp beats vague.
> "Done" without verification is not acceptable. Prove it.
> standing orders without triggers become suggestions

## Used by
[[topic-personal-assistant-agents]]
