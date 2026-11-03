---
tags: [manager-kb, source]
url: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
type: official-doc
author: Linux Foundation (A2A project press release)
published: 2026-04-09
accessed: 2026-10-29
reliability: med (primary but a vendor-consortium press release; no independent usage metrics)
---
# A2A Protocol surpasses 150 organizations ... first year (Linux Foundation)
## Key claims
- A2A (Agent-to-Agent) hosted by the Linux Foundation; at the one-year mark "more than 150 organizations" support it, with "deep integration across Google, Microsoft and AWS platforms": Microsoft in Azure AI Foundry and Copilot Studio, AWS via Amazon Bedrock AgentCore Runtime.
- v1.0 is "its first stable specification": multi-protocol support, multi-tenancy, modernised OAuth flows (implicit/password removed, device code + PKCE added), Signed Agent Cards for cryptographic identity, a migration path for early adopters. gh releases: v1.0.0 on 2026-03-12 (many breaking changes vs v0.3.0 of 2025-07-30); v1.0.1 2026-05-28.
- Claims production deployments in supply chain, financial services, insurance, IT operations; says agents on LangGraph or CrewAI "can work together, delegate sub-tasks, and coordinate complex workflows without sharing internal memory". Companion Agent Payments Protocol (AP2) with 60+ supporting orgs.
- repo (gh api): a2aproject/A2A 26,327 stars, Apache-2.0, pushed 2026-10-28. README: "enabling communication and interoperability between opaque agentic applications"; JSON-RPC 2.0 over HTTP(S), Agent Cards for discovery, sync / SSE streaming / async push notifications, opaque (no shared memory/tools). ADK docs say to prefer local sub-agents unless the agent is a separate service/team/framework.
- No evidence found of Claude Code or the Claude Agent SDK implementing A2A natively; Anthropic's own multi-agent surface is subagents/teams/Managed Agents threads plus MCP. (absence of evidence, not verified negative)

## Used by
[[topic-multi-agent-frameworks]]
