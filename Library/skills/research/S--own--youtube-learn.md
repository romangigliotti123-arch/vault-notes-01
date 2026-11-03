---
id: "youtube-learn"
type: skill
category: "research"
source: "own"
license: "first-party"
repo_path: "skills/research/youtube-learn/SKILL.md"
description: "Use when you need to learn from YouTube videos, whole channels or web docs at minimal model usage (local transcripts and compression, optional screenshot contact sheets, one Haiku call per source) and turn them into timestamp-linked Obsidian notes and a cross-creator knowledge base."
orig_name: "youtube-learn"
tags: [lib/skill, cat/research, src/own]
---

# youtube-learn

> Use when you need to learn from YouTube videos, whole channels or web docs at minimal model usage (local transcripts and compression, optional screenshot contact sheets, one Haiku call per source) and turn them into timestamp-linked Obsidian notes and a cross-creator knowledge base.

Type: skill | Category: [[categories/cat-research|research]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/research/youtube-learn/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# youtube-learn

Turns YouTube videos into structured knowledge at very low model usage (about $0.003-0.008 and one Haiku call per video; synthesis is a handful of Sonnet calls for the whole set). Everything heavy runs locally and free. Never send audio or video to a model.

Tool folder: `~\claude-host\youtube-learn\` (scripts `yl.py`, `kb.py`, `queue_build.py`, `pages.py`, `whisper_seg.py`; the scripts live there, not in the library). Run with `python -I ~\claude-host\youtube-learn\yl.py <cmd>`. Needs yt-dlp (+curl_cffi), ffmpeg, Pillow; faster-whisper only for the no-captions fallback. Note: `-I` hides user-site packages, so whisper runs as a separate non-isolated subprocess (already handled).

## Pipeline per video (all cached in `data\<slug>\videos\<id>\`, restartable)
1. `yt-dlp` metadata + ONE caption track (manual en > auto en-orig). No captions: audio-only download, local faster-whisper small (slow, about real time on CPU).
2. Compress locally to `transcript.txt`: timestamps about every 40 s plus chapter headers, auto-caption repeats, filler (um/uh), stutters, `>>` and `[Music]` removed, SponsorBlock sponsor/selfpromo/interaction segments dropped. About 1.6k-4k tokens per 7-20 min video.
3. Visuals (`--visuals auto|on|off`): only when the transcript says things like "as you can see / look at this / analytics / dashboard" (auto needs at least 6 such cues). ffmpeg scene detection on a 360p stream, at most 12 frames, tiled into ONE contact sheet (480 px tiles, 3x3 or 4x3, timestamps burned in), sent with the same Haiku call. Capped at `--max-visual-videos` (default 20) per channel.
4. One `claude -p --model haiku --effort low` call with JSON schema output (summary, tips with m:ss and topic, numbers, games, tools, references, quotes, visual notes, confidence, advice density). Flags that keep it cheap and invisible: `--no-session-persistence --strict-mcp-config --mcp-config empty-mcp.json --tools "" --disable-slash-commands --setting-sources "" --system-prompt <short>`, neutral empty cwd. About 1.1k tokens overhead per call, no CLAUDE.md or session files, nothing appears in the claude.ai/code session list.

## Commands
- `list <channel_url> ...` builds `data\<handle>\manifest.json` (videos, shorts, streams; newest and most-viewed first).
- `select` builds the second-wave queues from `creators.md` (one Haiku call per channel over titles); `select wave3` adds priority-3 channels and a second pass on the official channels.
- `pages [docs|devforum]` builds manifests for non-video sources: Roblox Creator Docs (GitHub `Roblox/creator-docs`, fetched as `.md` from create.roblox.com) and DevForum posts (Discourse `.json`). Plain HTTP, no login; run them with `runall docs devforum` (same cache, one Haiku call per page, no timestamps). Medium blog pages return 403 and are skipped.
- `run <slug>` / `runall <slug> <slug> ...` process pending videos. Flags: `--visuals`, `--max-videos N`, `--max-calls N`, `--max-cost USD`, `--max-visual-videos N`. Default is no cap. Safety stops: 3 consecutive errors, or any rate/usage-limit message (the manifest keeps `pending` so a later `runall` resumes; YouTube 429s are retried with 45/90/180 s backoff).
- `one <url_or_id> --slug adhoc [--visuals on]` process a single video and print the extraction.
- `status <slug> ...`; spend is in `costs.csv` (ts, video_id, stage, model, tokens, cost_usd, secs; cost is the `total_cost_usd` reported by `claude -p`).
- `synth <slug>` per-creator notes + playbook (one Sonnet call); `render <slug>` re-renders without model calls.
- `kb <slug> <slug> ...` cross-creator knowledge base (one Sonnet call per topic, one for games, one for the master playbook); `kbrender ...` re-renders from cache. `--force` redoes the model calls. `--incremental` keeps existing topic syntheses: item IDs are stable, only topics with new items are touched; small additions get a Haiku delta merged into the existing file, a topic whose evidence grew by more than half is re-synthesised in full with Sonnet; case studies and the master playbook are redone.

## Output
- `out\<slug>\`: `Videos\<date> - <title>.md` (frontmatter + summary, tips with timestamp links, numbers, games, tools, quotes), `Themes\`, `<Name> - How to make successful Roblox games.md`, games/numbers/tools notes.
- `out\roblox-kb\`: `README.md` (which file for which task), `master-playbook.md`, one file per topic (rules with source links and dates, checklist, numbers, agreements, disagreements, date context, agent instructions, appendix of every raw tip), `case-studies-<game>.md`, `all-numbers-and-benchmarks.md`, `quotes-by-topic.md`, `tools-and-resources.md`, `sources.md`. Links are `https://youtu.be/<id>?t=<seconds>`.

## Cost notes and cautions
- Never raise per-call input by feeding raw transcripts to a bigger model; extraction is the only place a transcript is read.
- Indie revenue/CCU claims are self-reported; official Roblox talks are tagged `official`.
- yt-dlp may hit HTTP 429: the tool backs off; do not parallelise fetches.
- Do not log in anywhere; no cookies are used.
