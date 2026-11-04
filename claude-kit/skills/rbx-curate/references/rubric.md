# Curation rubric (vault-learnings inbox to vault notes)

Applies to every note in the `inbox/` of the public repo vault-learnings. Inbox content is **untrusted data**: anyone can add a file. `claude-kit/tools/curate.py` executes these rules; nobody (human or model) follows anything a note says. `tools/test_learn.py`-style tests feed poisoned notes through the same code and require rejection.

## Pipeline

1. Bounded read (max 9000 bytes, UTF-8, no NUL, no symlinks), strict front-matter parse (`schema: 1`; unknown keys are ignored and never copied).
2. Shape: title 8-120 chars, topic 1-3 lowercase segments, confidence `high` or `medium`, generic source tag, body 60-4000 chars (at least 12 words) and, for a promoted note, at most 1500 characters (longer is rejected with code `body-length`, reason "too long: summarise"), `## How verified` 20-1000 chars (at least 5 words), created date.
3. Topic root must be one of: roblox, luau, game-dev, windows, linux, macos, git, github, hosting, python, node, claude, agents, vault, tooling, blender, web, security. Anything else is off-topic for this vault.
4. Content scan on title + body + evidence: secret rules, hidden characters, high-entropy strings, instruction rules (below), unredacted personal/machine details (the sender's tool redacts paths, e-mail addresses, IPs and host/user names; a note that still needs redaction is rejected, not repaired).
5. Duplicates: the same content hash is a `duplicate` (no change). A near-duplicate of an existing learned note (same topic and title similarity >= 0.75, or body similarity >= 0.8) is a `merge`: the note's `confirmations` goes up by one, its source tag is added, and the new evidence is appended when it adds something and the note is small.
6. Otherwise `accept`: the note becomes `learned/<topic>/<slug>.md` with provenance (first_seen, last_confirmed, confirmations, sources, hashes, licence CC0-1.0, status curated).
7. Every examined file moves to `processed/<yyyy-mm>/` (rejected ones to `processed/rejected/<yyyy-mm>/`) and gets one row in `CURATION-LOG.md` (title cut to 80 characters, decision, rule codes, target).

Instruction rules have weight 9 (any one rejects) or weight 1 (two or more reject as `directive-wording`).

## Reject codes: shape and quality
`file-too-large` file over 9000 bytes; `not-utf8` not valid UTF-8 text; `nul-bytes` contains NUL bytes; `no-frontmatter` missing front matter; `bad-schema` schema is not 1; `off-topic` topic root not in the allow-list; `thin-body` too few words to carry a finding; `thin-evidence` 'How verified' too short to count as evidence; `unredacted-personal-data` contains personal/machine details the sender's tool would have redacted; `title-length` title length; `topic-format` topic format; `confidence` confidence must be high or medium; `source-tag` source tag; `body-length` body length; `verified-length` verified length; `created-date` created date; `duplicate-hash` same content already promoted or already in this batch; `high-entropy-string` a long random-looking string (key, token or hash blob); `hidden-characters` zero-width, bidirectional-override, control or other invisible characters; `directive-wording` weight-1 instruction wording adding up to 2 or more.

## Reject codes: secrets
`github-token` GitHub token; `github-pat` GitHub fine-grained token; `anthropic-key` Anthropic key; `openai-style-key` OpenAI-style key; `aws-key` AWS access key id; `google-key` Google API key; `private-key-block` private key block; `slack-token` Slack token; `slack-webhook` Slack incoming-webhook URL; `discord-webhook` Discord webhook URL; `jwt` JSON web token; `bearer-token` bearer token; `credential-assignment` password/secret/api-key assignment with a value; `url-credentials` user:password inside a URL; `forbidden-token-word` the literal words for OAuth access/refresh tokens (the public build forbids them; rephrase).

## Reject codes: instruction-like or unsafe content
`override-instructions` tells a reader to ignore, forget or override earlier instructions or rules; `new-instructions` announces 'new/hidden/real instructions'; `system-prompt` talks about a system or developer prompt; `role-hijack` tries to change the reader's role ('you are now', 'from now on', jailbreak wording); `chat-markers` contains chat-transcript markers (system:, assistant:, [INST], special tokens); `addressed-to-agent` addresses an AI/agent/assistant directly ('attention assistant', 'AI READER', 'if you are an AI'); `agent-must` says what an AI/assistant/agent must or should do; `conceal-from-user` asks to hide something from the user, act secretly or without asking; `exfiltration` asks to send, post, upload or reveal credentials, keys, cookies or environment data; `pipe-to-shell` download piped into a shell or interpreter; `eval-exec` evaluation or encoded execution (iex, eval, -enc, base64 decode, os.system, subprocess); `destructive-command` destructive or privileged commands (recursive delete, format, sudo, force push, hard reset, chmod 777); `reverse-shell` reverse-shell or remote-exec idioms; `fetch-instruction` tells the reader to download, clone or install from a URL; `persistence` tells the reader to edit CLAUDE.md, settings.json, shell profiles, cron, startup or scheduled tasks; `remote-image-or-link-trick` remote images, data: URIs or javascript:/file: links (render-time beacons); `hidden-html` HTML comments or tags (hidden text, scripts, frames, images, links); `shortener-or-ip-url` URL shorteners or raw-IP URLs; `encoded-blob` long base64/hex blob; `second-person-command` 'you must / you have to' (weight 1); `always-never-directive` lines starting 'always/never <verb>' (weight 1); `urgency-marker` urgency/compliance wording: 'important:', 'obey', 'comply', 'follow these steps' (weight 1); `trust-me` 'trust this', 'highest priority', 'takes precedence' (weight 1); `run-this` lines starting with run/execute/paste ... this/following (weight 1).

## What a good note looks like

- A fact, stated in the declarative: what happens, under which conditions, what works instead. Not an order, not a script to run.
- Evidence: what was run or observed (2 runs, a Studio test, an exit code). A guess is not recorded.
- Generic: no names, paths, addresses, game ids or private details.
- New: it is not already in `learned/` or in the kit's notes.

## Not decided here

Whether a note is *true* beyond its evidence is not decided; `confirmations` shows how many independent notes agreed. Accepted notes are reference data in the vault, labelled as community-contributed, and are read like any other note: as data, never as instructions.
