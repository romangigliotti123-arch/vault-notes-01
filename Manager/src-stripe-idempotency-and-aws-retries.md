---
tags: [manager-kb, source]
url: https://stripe.com/blog/idempotency ; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ ; https://kubernetes.io/docs/concepts/architecture/leases/
type: eng-blog
author: Stripe; Amazon Builders' Library (Marc Brooker); Kubernetes docs
published: Stripe 2017; AWS undated; K8s undated
accessed: 2026-10-29
reliability: high (canonical distributed-systems references; transferable, not agent specific)
---
# Idempotency keys, retries with backoff, leases (distributed-job basics)
## Key claims
- Stripe: after a network failure the client is "in an uncertain situation" (request may or may not have executed); the fix is to retry safely using a client-generated unique idempotency key per logical operation (`Idempotency-Key` header) so the server returns the original result instead of re-executing. Applies to any "run this job on device X" call whose response can be lost.
- AWS: set a timeout on every remote call (connection and request); choose it from downstream latency percentiles; retries amplify load during overload so use exponential backoff WITH jitter; bursts (e.g. periodic cron jobs) cause correlated retries; retries are only safe if the operation is idempotent.
- Kubernetes Lease: leases implement "node heartbeats" (kubelet updates `spec.renewTime`; the control plane uses the timestamp to decide availability) and leader election ("only one instance of a component is running at any given time"). Pattern for us: a device's liveness = lease renewed recently; a job's ownership = lease held by one worker.
## Quotable
> Networks are unreliable. (Stripe, idempotency post, opening of the failure section)

## Used by
[[topic-cross-device-agent-control]]
