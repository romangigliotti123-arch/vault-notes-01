---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/prompt-caching.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.2xx-2.1.311 era)
accessed: 2026-10-29
reliability: high (primary vendor docs, fetched raw .md)
---
# Claude Code docs: How Claude Code uses prompt caching
## Key claims
- Request layout: system prompt+tool defs, then project context (CLAUDE.md, auto memory, unscoped rules), then conversation. Exact prefix match; a change anywhere invalidates everything after it.
- Each **model** has its own cache. Switching models recomputes the whole request. `opusplan` toggles = model switches. Skill/command frontmatter `model:` = a model switch for that turn.
- Effort change: on most models invalidates cache; on Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1 (API key or subscription) "changing effort keeps the cache".
- Invalidators: switching model, fast mode toggle, adding/removing MCP tools (not when tool search defers them), plugin MCP changes, deny rule on whole tool (when no tool search), compaction (by design), accumulating many images (batch of oldest removed), upgrading Claude Code. Cache-safe: editing CLAUDE.md mid-session (but edit not applied until /clear, /compact or restart), changing permission mode, output style, invoking skills, `/recap`, `/rewind`, spawning a subagent, toggling `/advisor`.
- **/compact economics**: the summarization request repeats system prompt+tools+history. Warm cache => reads prefix from cache, "costs a fraction". After a break > TTL => "reprocesses that history as uncached input... why /compact costs the most when you resume an old session". Run `/compact` at natural breaks; `/rewind` to abandon a path (hits an earlier cache entry).
- **Idle compaction**: "If you leave a long conversation idle while it is on the one-hour TTL, Claude Code can compact it" ; disable with `idleCompaction: false` (v2.1.290+).
- **TTL**: 5 min or 1 h (1 h costs more per cache write). Default: subscription within plan usage => main conversation 1 h; everything else (subagents, workflows, forks, teammates, compaction, session titles) 5 min except server-controlled helpers; API key/credits => 5 min everywhere. Over plan limit (usage credits) the main conversation drops to 5 min. Controls: `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL` (main), `subagentPromptCacheTtl` / `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` (others), per-subagent `cacheTtl` under `experimental` frontmatter (v2.1.248+), `ENABLE_PROMPT_CACHING_1H=1`, `FORCE_PROMPT_CACHING_5M=1`. Verify: `claude -p "hello" --output-format json` -> `usage.cache_creation.ephemeral_1h_input_tokens` vs `ephemeral_5m_input_tokens`.
- **Subagents and cache**: a subagent's first request does not read the parent's cache (different system prompt/tools); it warms its own, 5 min TTL on subscription. A **fork** inherits system prompt, tools and history exactly so its first request reads the parent's cache. Resumed subagents can read the cache the original run warmed. Workflow fan-outs hold all but the first agent up to 5 s so they hit the first agent's cache.
- **Cache scope**: effectively per machine + directory (system prompt embeds auto-memory paths; conversation opens with cwd/platform/shell/OS). Parallel sessions in the same directory can share cache; different directories cannot.
- Resumed session keeps its original system prompt until compacted.
## Quotable
> "Pick your model and effort level at the top of a session, then save /compact for natural breaks between tasks."
> "After a break longer than the cache lifetime, there is no cache left to read, so the summarization request reprocesses that history as uncached input."

## Used by
[[topic-context-engineering]], [[topic-context-window-management]], [[topic-model-effort-routing-cost]]
