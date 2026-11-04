# Per-source methods

For every source: find candidates (cheap), rank them (`scoring.md`), enumerate the whole back-catalogue of the selected ones, process in value order. If a source is unreachable, record it (the scripts do this in `.cache/unreachable.json`), say what was lost, and continue.

## YouTube (needs yt-dlp; ffmpeg optional)

Needs yt-dlp (ffmpeg optional). No captions = skip unless the user allowed the local whisper fallback (videos over 50 min skipped); visuals are off in Light; shorts under 90 s skipped. [cold:rbx-research/source-methods.md] read only when a source is blocked or you need the exact find/enumerate/fetch method of one source.

## GitHub (gh logged in is best; anonymous REST works at 60 requests/hour)

`gh` logged in is best (anonymous REST = 60 requests/hour); maintainer blog URLs it prints go to `find web --urls`; Discussions are not included. [cold:rbx-research/source-methods.md] read only when a source is blocked or you need the exact find/enumerate/fetch method of one source.

## Reddit (no API key)

Public JSON endpoints, honest User-Agent, 4 s spacing; on 403 the scripts fall back to RSS feeds (no scores), and if both fail the source is unreachable (alternative: WebSearch `site:reddit.com <topic>` plus WebFetch, URLs via `find web --urls`). Never log in; skip NSFW. [cold:rbx-research/source-methods.md] read only when a source is blocked or you need the exact find/enumerate/fetch method of one source.

## Blogs, newsletters, official docs (web)

WebSearch yourself for the best publishers; posts are fetched as plain text (robots.txt respected, 48k characters max, code blocks kept). [cold:rbx-research/source-methods.md] read only when a source is blocked or you need the exact find/enumerate/fetch method of one source.

## Papers
- arXiv API (no key, 3 s spacing): relevance-ranked abstracts for each query. Items are the abstract pages (the PDF itself is not read). For paywalled or PDF-only material rely on abstracts and say so.

## X/Twitter and other walled gardens
- Not scraped. If the user cares, they paste URLs or text; otherwise list it under "not reachable".
