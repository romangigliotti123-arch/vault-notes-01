---
tags: [manager-kb, source]
url: https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter
type: eng-blog
author: Marc Brooker (AWS Builders' Library; page shows "Marc")
published: 2019-12-05
accessed: 2026-10-29
reliability: high (canonical AWS engineering article)
---
# Timeouts, retries, and backoff with jitter
## Key claims
- "When failures are caused by overload, retries that increase load can make matters significantly worse."
- Exponential backoff; "Jitter adds some amount of randomness to the backoff to spread the retries around in time."
- Token bucket limits retries: retry freely while tokens remain, then at a fixed rate.
- "APIs with side effects aren't safe to retry unless they provide idempotency."
- Choose timeouts from downstream latency percentiles (accept e.g. 0.1% false timeouts).
- Retry at a single layer of the stack (avoid multiplicative retries across layers).

## Used by
[[topic-long-running-always-on-agents]]
