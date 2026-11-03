---
tags: [manager-kb, source]
url: https://martinfowler.com/bliki/CircuitBreaker.html
type: practitioner-blog
author: Martin Fowler
published: 2014-03-06
accessed: 2026-10-29
reliability: high (canonical pattern description)
---
# Circuit Breaker
## Key claims
- Wrap a call, count failures, trip open after a threshold (example 5), reject calls immediately while open, after a reset timeout allow one trial call (half-open); success closes, failure reopens.
- "Any change in breaker state should be logged and breakers should reveal details of their state for deeper monitoring."
- "Usually you'll also want some kind of monitor alert if the circuit breaker trips." Operators should be able to trip/reset manually.

## Used by
[[topic-long-running-always-on-agents]]
