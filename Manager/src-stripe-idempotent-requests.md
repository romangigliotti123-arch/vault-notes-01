---
tags: [manager-kb, source]
url: https://docs.stripe.com/api/idempotent_requests
type: official-doc
author: Stripe
published: undated
accessed: 2026-10-29
reliability: high (canonical idempotency-key reference)
---
# Stripe: idempotent requests
## Key claims
- Client generates a unique key (UUID v4); server saves status code and body of the first request with that key and returns it for retries ("including 500 errors" in API v1). Keys up to 255 chars, pruned after >= 24 h. Server compares incoming params to the original and errors if they differ (misuse guard). All POSTs accept keys; GET/DELETE are idempotent by definition.
- Results are saved only once endpoint execution begins; validation failures or concurrent conflicts are not saved and can be retried.
- Transfer to an agent manager: one `job_id` + `step` key per outward side effect (Telegram reply, git push, PR, email), stored before sending; check the ledger before re-sending after a crash.

## Used by
[[topic-long-running-always-on-agents]]
