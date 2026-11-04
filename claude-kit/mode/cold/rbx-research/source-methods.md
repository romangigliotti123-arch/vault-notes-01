<!-- cold: rbx-research/source-methods.md | read when: read only when a source is blocked or you need the exact find/enumerate/fetch method of one source. -->

## From skills/rbx-research/references/sources.md :: YouTube (needs yt-dlp; ffmpeg optional)

- Find: `yt-dlp ytsearch<N>:<query> --flat-playlist` for each query variant, grouped by channel (hits, average views, typical length). The top candidates are enriched with follower count, last upload date and upload cadence (3 yt-dlp calls each).
- Enumerate: `/videos` and `/streams` tabs (flat), shorts under 90 s are skipped. Priority = union of newest-first and most-viewed-first.
- Fetch: manual captions, else auto-captions (json3), cached under `.cache/yt/<id>/`; no captions means skip unless the user allowed the local whisper fallback and faster-whisper and ffmpeg exist (videos over 50 minutes are skipped). Transcripts are compressed (fillers, stutters, music tags removed; timestamp marker every 40 s; chapters kept).
- Visuals: only when the speaker points at the screen at least 6 times, at most 12 frames in one contact sheet from a 360p download that is deleted. Off in the Light tier; capped by `max_visuals`.
- 429 from YouTube: yt-dlp backs off 45/90/180 s; if it persists the item is retried on the next run.

## From skills/rbx-research/references/sources.md :: GitHub (gh logged in is best; anonymous REST works at 60 requests/hour)

- Find: `search/repositories` by stars and by recent update for each query, plus the best "awesome-<topic>" list (its linked repos credit their owners). Aggregated per owner (user or organisation). Top owners are enriched with followers; maintainer blog URLs are printed, feed them to `find web --urls`.
- Enumerate per owner: the most relevant repos (3 / 8 / 25 by depth) with their README, every release with notes, up to 25 markdown docs (docs first, by relevance), and the 12 most-discussed issues. Discussions need GraphQL and a login, so they are not included by default.
- Raw files come from raw.githubusercontent.com, which does not use the API quota.

## From skills/rbx-research/references/sources.md :: Reddit (no API key)

- Public JSON endpoints (`/search.json`, `/r/<sub>/top.json`, thread `.json`) with the honest User-Agent and a 4 s spacing. Reddit often answers 403 to scripts. When that happens the scripts switch to the Atom/RSS feeds (`/search.rss`, `/r/<sub>/top/.rss`, thread `.rss`), which carry titles, authors and comment text but no scores, and say so. If both fail the source is marked unreachable. Alternative inside Claude Code: WebSearch with `site:reddit.com <topic>` and WebFetch on the best threads; add their URLs through `find web --urls` or note them as leads.
- Creators on Reddit are subreddits (r/name) and repeat authors (u/name). Enumeration takes top-all-time, top-of-year, newest, and a topic search inside the subreddit; threads under 3 points are skipped.
- Never log in; skip NSFW.

## From skills/rbx-research/references/sources.md :: Blogs, newsletters, official docs (web)

- Use WebSearch yourself for "best blogs/newsletters/docs for <topic>" and collect publisher home pages. Also Hacker News (Algolia API, no key): publishers whose stories on the topic got traction.
- Enumerate: auto-discovered RSS/Atom feed, plus the sitemap archive (feeds usually hold only the latest 10-50 posts), plus post links on the page if neither exists. Each post is fetched as plain text (robots.txt respected, 48k characters max, scripts/menus removed, code blocks kept).
