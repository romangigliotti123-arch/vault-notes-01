---
tags: [manager-kb, source]
url: https://github.com/microsoft/autogen
type: repo
author: Microsoft / AG2 community
published: undated (AutoGen created 2023-08-18; READMEs read 2026-10-29)
accessed: 2026-10-29
reliability: high (READMEs + gh api metadata; note the AutoGen archived banner vs gh archived=false flag)
---
# AutoGen (61,609 stars) -> AG2 (5,026) and Microsoft Agent Framework (14,366) + Semantic Kernel (28,711)
## Key claims
- microsoft/autogen README banner: "Project archived and no longer maintained ... Microsoft is not providing bug fixes, security fixes, new features, or support ... advise against production use." (gh api still reported archived=false and pushed 2026-10-28; treat the README as authoritative about intent.) Badge links to microsoft/agent-framework.
- Microsoft Agent Framework (MAF): "open, multi-language framework for building production-grade AI agents and multi-agent workflows in .NET and Python" (also a Go SDK repo). MIT, pushed 2026-10-28, created 2025-04-28, 829 open issues. Graph-based workflows with "sequential, concurrent, handoff, and group collaboration patterns; includes checkpointing, streaming, human-in-the-loop, and time-travel"; DevUI; A2A hosting. README for Semantic Kernel: "Semantic Kernel is now Microsoft Agent Framework! ... MAF is now available at version 1.0 as a production-ready release".
- AG2 (ag2ai/ag2, Apache-2.0, pushed 2026-10-28, volunteer-maintained fork by AutoGen's original authors): as of v1.0 the protocol-driven framework is top-level package `ag2`; the classic AutoGen-derived API (ConversableAgent, GroupChat, swarms) moved to ag2ai/ag2-classic.
- Pattern lineage: Magentic-One (orchestrator + ledgers) and GroupChat came from AutoGen; the research prototype was archived in favour of MAF.

## Used by
[[topic-multi-agent-frameworks]]
