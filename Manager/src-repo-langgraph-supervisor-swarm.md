---
tags: [manager-kb, source]
url: https://github.com/langchain-ai/langgraph-supervisor-py
type: repo
author: LangChain
published: undated (repo; supervisor lib last push 2026-07-15, ARCHIVED)
accessed: 2026-10-29
reliability: high (README + gh api metadata read)
---
# LangGraph (44,060 stars, MIT, pushed 2026-10-28) with langgraph-supervisor-py and langgraph-swarm-py
## Key claims
- langgraph-supervisor-py: 1,655 stars, MIT, **archived** (gh api archived=true, last push 2026-07-15). README banner: "We now recommend using the **supervisor pattern directly via tools** rather than this library for most use cases. The tool-calling approach gives you more control over context engineering."
- langgraph-swarm-py: 1,585 stars, MIT, not archived, pushed 2026-10-28. Swarm = "agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent."
- LangChain's current multi-agent doc (docs.langchain.com/oss/python/langchain/multi-agent) names five patterns: Subagents (supervisor-as-tools), Handoffs, Skills, Router, Custom workflow (LangGraph). See [[src-langchain-docs-multi-agent]].
- Takeaway: the vendor that popularised the "supervisor" and "swarm" libraries now steers users to plain tool-calling supervisors plus skills. The abstractions were thin wrappers over what the model does natively.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
