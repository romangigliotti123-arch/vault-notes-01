---
tags: [manager-kb, source]
url: https://brave.com/blog/comet-prompt-injection/
type: eng-blog (security research)
author: Artem Chaikin, Shivan Kaul Sahib (Brave)
published: 2025-08-20
accessed: 2026-10-29
reliability: high (vendor-competitor researchers with PoC; fix status disputed in later coverage)
---
# Agentic browser security: indirect prompt injection in Perplexity Comet
## Key claims
- Comet's "Summarize this webpage" fed page content to the LLM "without distinguishing between the user's instructions and untrusted content from the webpage". PoC: hidden instructions in a Reddit comment (behind a spoiler tag) made the agent open the user's account page, read the email address, trigger an OTP login (using a look-alike domain with a trailing dot) and leak it.
- Lesson: an assistant that can act in logged-in sessions turns any readable text (web page, comment, PDF, email) into a potential command channel; separation of user intent from untrusted content must be structural.
- Follow-ups (snippets only): Brave disclosed more Comet issues on 2025-10-21 (instructions hidden in screenshots); Perplexity's published stance "Malicious Prompt injection remains an unsolved problem across the industry".
## Quotable
> feeds a part of the webpage directly to its LLM without distinguishing between the user's instructions and untrusted content from the webpage

## Used by
[[topic-agent-security]], [[topic-personal-assistant-agents]]
