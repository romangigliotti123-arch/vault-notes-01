<!-- cold: rbx-weekly/open-cloud-analytics.md | read when: the user asks how to set up the Open Cloud analytics key or which metrics and breakdowns the Analytics Query API offers. -->

## From skills/rbx-weekly/SKILL.md :: Open Cloud Analytics Query API details

Roblox has an Analytics Query API (beta, checked 2026-11-01): `POST https://apis.roblox.com/analytics-query-api/v1/universes/{UniverseId}/metrics` with header `x-api-key`; the key needs `universe.analytics:read` (system `universe-analytics`) for that experience; metrics such as `DailyActiveUsers`, `ForwardD1Retention`, `DailyRevenue`, `PayingUsersCVR`, plus funnels, with breakdowns (Platform, Country, ...) and granularities OneDay/OneWeek/...; standard metrics reach back 4 years. Setup steps (only if the user asks): Creator Dashboard > Open Cloud > API Keys > create, add the experience, grant `universe.analytics:read`.
