---
tags: [manager-kb, source]
url: https://stripe.com/blog/idempotency
type: eng-blog
author: Stripe Engineering
published: 2017-02-22
accessed: 2026-10-29
reliability: high (canonical reference; old but foundational)
---
# Designing robust and predictable APIs with idempotency
## Key claims
- Network failures leave the caller unsure whether a mutation happened; retrying a non-idempotent call risks duplicate side effects.
- Client sends a unique key per logical operation; server ties it to request state: first run executes, retry of unfinished work resumes, retry of finished work returns the cached result.
- Clients retry with exponential backoff plus random jitter to avoid thundering herds.
- For agent tools: make every mutating script safe to re-run (`ensure`-style or key/lock file) because agents retry after timeouts. See also [[src-aws-timeouts-retries-jitter]].
## Quotable
> allow clients to pass a unique value and retry requests as needed

## Used by
[[topic-tool-and-mcp-design]]
