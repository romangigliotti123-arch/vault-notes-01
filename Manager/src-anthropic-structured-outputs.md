---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high (official; relevant parts grepped, not read end to end)
---
# Structured outputs (API) - facts relevant to worker reports
## Key claims
- "Structured outputs guarantee schema-compliant responses through constrained decoding": always valid JSON, correct types and required fields. Compliance is syntactic: nothing guarantees the field CONTENT is true.
- Supported: basic types, string enums, `const`, `anyOf`/`allOf` (limited), `$ref` internal, `required`, `additionalProperties:false`, string formats, `minItems` of 0 or 1.
- Not supported: recursive schemas, numeric/string length constraints (`minimum`, `maxLength`, ...), external `$ref`; unsupported features return a 400 (SDKs can move constraints into descriptions and validate client-side).
- `claude -p --json-schema` is the CLI face of this (see [[src-ccdocs-headless]]): `structured_output` field absent if the run ended without valid structured output (e.g. refusal).
- Sonnet 5.5 note ([[src-anthropic-prompting-sonnet-5-5]]): with structured outputs the model may skip thinking on tasks needing working-out; nudge "Think the problem through before you answer." and treat `stop_reason: max_tokens` as failed even if JSON is valid.

## Used by
[[topic-report-formats-and-verification]]
