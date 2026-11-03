#!/usr/bin/env python3
"""ytwatch: low-cost "watching" of YouTube. Transcript first (captions via yt-dlp), optional local whisper fallback,
optional visual contact sheet (ffmpeg) only when the speaker keeps pointing at the screen. Nothing is sent to any model here.
  search <query> [--n 30]            flat search results (id, title, channel, views, duration)
  list <channel_url> [--tabs videos,streams] [--end N]   whole back-catalogue as JSON lines (no model)
  info <channel_url>                 channel signals for ranking (cadence, last post, followers) - 3 yt-dlp calls
  one <url|id> [--out DIR] [--visuals] [--whisper] [--lang en] [--sponsorblock]
                                     fetch + compress transcript; prints the compressed transcript path and a meta line
Requires yt-dlp. ffmpeg only for visuals / whisper. Be polite: requests are spaced and 429s back off.
"""
import argparse, json, re, subprocess, sys, time, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *  # noqa

CUE = re.compile(
    r"\b(look at (?:this|that|these|those)|as you can see|you can see|right here|over here|on (?:the |my |your )?screen|"
    r"this (?:graph|chart|screen|page|dashboard|diagram|slide|menu|tab|button|code|window)|let me show|i'll show|i will show|show you|"
    r"here'?s (?:the|an|a|my|what)|take a look|check (?:this|it) out|click (?:on|here)|scroll(?:ing)? down|"
    r"if we (?:go|look)|as (?:shown|seen)|pull up|on the left|on the right|top right|bottom left|in the diagram|this slide)\b", re.I)
FILLER = re.compile(r"\b(?:um+|uh+|erm|hmm+|mhm|ah)\b[,.]?\s*", re.I)
NOISE = re.compile(r"\[(?:music|applause|laughter|sighs?|cheering|noise)\]", re.I)
STUTTER = re.compile(r"\b((?:\w+['’]?\w*)(?: \w+['’]?\w*){0,2}) \1\b", re.I)


def yt(args, tries=4):
    base = tool_cmd("yt-dlp")
    if not base:
        raise Skip("yt-dlp not installed (run scripts/doctor.py)")
    r = None
    for i in range(tries):
        r = run(base + ["--sleep-requests", "1", "--sleep-subtitles", "2", "--no-warnings"] + args, timeout=900)
        if "429" in (r.stderr or "") and "Too Many Requests" in (r.stderr or "") and i < tries - 1:
            time.sleep(45 * (2 ** i))
            continue
        return r
    return r


def norm_channel(url):
    url = url.strip().rstrip("/")
    url = re.sub(r"/(videos|shorts|streams|featured|playlists|about)$", "", url)
    return url


def search(query, n=30):
    r = yt(["--flat-playlist", "--dump-json", f"ytsearch{n}:{query}"], tries=2)
    res = []
    for line in (r.stdout or "").splitlines():
        if line.startswith("{"):
            try:
                d = json.loads(line)
            except Exception:
                continue
            res.append({"id": d.get("id"), "title": d.get("title"), "channel": d.get("channel") or d.get("uploader"),
                        "channel_id": d.get("channel_id"), "channel_url": d.get("channel_url") or d.get("uploader_url"),
                        "views": d.get("view_count"), "duration": d.get("duration"), "description": (d.get("description") or "")[:200]})
    return res


def list_channel(url, tabs=("videos", "streams"), end=None):
    base = norm_channel(url)
    items, seen = [], set()
    for tab in tabs:
        args = ["--flat-playlist", "--dump-json"] + (["--playlist-end", str(end)] if end else []) + [f"{base}/{tab}"]
        r = yt(args, tries=3)
        n = 0
        for line in (r.stdout or "").splitlines():
            if not line.startswith("{"):
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("id") in seen:
                continue
            seen.add(d["id"])
            n += 1
            items.append({"id": d["id"], "title": d.get("title"), "duration": d.get("duration"),
                          "views": d.get("view_count"), "kind": "live" if tab == "streams" else "video", "newest_rank": n,
                          "date": d.get("upload_date")})
    by_views = sorted(items, key=lambda x: -(x["views"] or 0))
    vr = {x["id"]: i for i, x in enumerate(by_views)}
    for x in items:  # priority: union of newest-first and most-viewed-first (lower = earlier)
        x["priority"] = min(x["newest_rank"], vr[x["id"]] + 1) + 0.01 * (x["newest_rank"] + vr[x["id"]])
    items.sort(key=lambda x: x["priority"])
    return items


def video_info(vid):
    r = yt(["--skip-download", "--dump-single-json", "--no-playlist", f"https://www.youtube.com/watch?v={vid}"])
    try:
        return json.loads(r.stdout)
    except Exception:
        raise Skip("yt-dlp info failed: " + ((r.stderr or r.stdout or "")[-200:]))


def channel_info(url):
    """Signals for creator ranking. Uses the newest and the 40th video for date/cadence."""
    its = list_channel(url, tabs=("videos",), end=40)
    if not its:
        return None
    newest = min(its, key=lambda x: x["newest_rank"])
    oldest = max(its, key=lambda x: x["newest_rank"])
    di = video_info(newest["id"])
    d_new = di.get("upload_date")
    d_old = None
    if oldest["id"] != newest["id"]:
        try:
            d_old = video_info(oldest["id"]).get("upload_date")
        except Skip:
            pass
    fmt = lambda d: f"{d[:4]}-{d[4:6]}-{d[6:8]}" if d and len(d) == 8 else None
    ppm = None
    if d_new and d_old and d_new != d_old:
        days = max(1, (datetime.strptime(d_new, "%Y%m%d") - datetime.strptime(d_old, "%Y%m%d")).days)
        ppm = round(len(its) / (days / 30.0), 2)
    views = [x["views"] for x in its if x.get("views")]
    return {"channel": di.get("channel"), "channel_id": di.get("channel_id"), "url": norm_channel(url),
            "followers": di.get("channel_follower_count"), "last_post": fmt(d_new), "posts_per_month": ppm,
            "avg_views": int(sum(views) / len(views)) if views else None, "n_sampled": len(its),
            "sample_titles": [x["title"] for x in its[:10]],
            "avg_duration": int(sum(x["duration"] or 0 for x in its) / len(its))}


from datetime import datetime  # noqa: E402


def parse_json3(p):
    j = jload(p, {})
    segs, prev = [], None
    for ev in j.get("events", []):
        if "segs" not in ev:
            continue
        txt = "".join(s.get("utf8", "") for s in ev["segs"]).replace(" ", " ").replace("\n", " ").strip()
        if not txt or txt == prev:
            continue
        prev = txt
        segs.append([round(ev.get("tStartMs", 0) / 1000, 1), txt])
    return segs


def whisper_segments(vid, d):
    """Local transcription fallback. Audio never leaves this machine. Needs ffmpeg + faster-whisper + user consent."""
    try:
        from faster_whisper import WhisperModel
    except Exception:
        raise Skip("no captions and faster-whisper not installed")
    if not tool_cmd("ffmpeg"):
        raise Skip("no captions and ffmpeg missing")
    yt(["-f", "ba[ext=m4a]/ba", "--no-playlist", "-o", str(d / "audio.%(ext)s"), f"https://www.youtube.com/watch?v={vid}"])
    audio = next(d.glob("audio.*"), None)
    if not audio:
        raise Skip("audio download failed")
    wav = d / "audio.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(audio), "-ac", "1", "-ar", "16000", str(wav)], check=True)
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs = [[round(s.start, 1), s.text.strip()] for s in model.transcribe(str(wav), vad_filter=True)[0] if s.text.strip()]
    for f in (audio, wav):
        f.unlink(missing_ok=True)
    return segs


def fetch(d, vid, lang="en", allow_whisper=False, max_whisper_sec=3000):
    """Cache dir d. Returns meta dict (also saved). Raises Skip for videos that should not be processed."""
    d.mkdir(parents=True, exist_ok=True)
    if (d / "segments.json").exists() and (d / "meta.json").exists():
        return jload(d / "meta.json")
    if not (d / "meta.json").exists():
        info = video_info(vid)
        meta = {k: info.get(k) for k in ("id", "title", "upload_date", "view_count", "like_count", "duration", "chapters", "tags", "channel")}
        meta["description"] = (info.get("description") or "")[:1200]
        manual = [k for k in (info.get("subtitles") or {}) if k.startswith(lang)]
        auto = [k for k in (info.get("automatic_captions") or {}) if k.startswith(lang)]
        meta["has_manual_subs"] = bool(manual)
        meta["sub_lang"] = manual[0] if manual else (f"{lang}-orig" if f"{lang}-orig" in auto else (auto[0] if auto else None))
        jsave(d / "meta.json", meta)
    meta = jload(d / "meta.json")
    segs = None
    if meta.get("sub_lang"):
        if not list(d.glob("*.json3")):
            yt(["--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", meta["sub_lang"], "--sub-format", "json3",
                "--no-playlist", "-o", str(d / "%(id)s"), f"https://www.youtube.com/watch?v={vid}"])
        subs = sorted(d.glob("*.json3"))
        if subs:
            segs = parse_json3(subs[0])
            meta["transcript_source"] = "manual-subs" if meta.get("has_manual_subs") else "auto-captions"
    if not segs:
        if not allow_whisper:
            raise Skip("no captions and whisper fallback not allowed")
        if (meta.get("duration") or 0) > max_whisper_sec:
            raise Skip("no captions and longer than 50 min (whisper too slow)")
        segs = whisper_segments(vid, d)
        meta["transcript_source"] = "whisper-small"
    jsave(d / "segments.json", segs)
    jsave(d / "meta.json", meta)
    return meta


def clean_text(s):
    s = NOISE.sub(" ", s).replace("[ __ ]", "…").replace("[__]", "…")
    s = re.sub(r"(?:^|\s)(?:>>|&gt;&gt;)\s*", " ", s)
    s = FILLER.sub(" ", s)
    for _ in range(2):
        s = STUTTER.sub(r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def sponsor_segments(vid):
    r = http_get("https://sponsor.ajay.app/api/skipSegments?videoID=%s&categories=%s" % (
        vid, urllib.parse.quote(json.dumps(["sponsor", "selfpromo", "interaction"]))), retries=0, timeout=15)
    j = r.json() if r.status == 200 else None
    return [tuple(x["segment"]) for x in j] if j else []


def compress(d, vid, marker_every=40, sponsorblock=False):
    out = d / "transcript.txt"
    if out.exists():
        return out
    meta, segs = jload(d / "meta.json"), jload(d / "segments.json")
    spons = sponsor_segments(vid) if sponsorblock else []
    pending_ch = sorted({int(c["start_time"]): c["title"] for c in (meta.get("chapters") or [])}.items())
    lines, cur, last_mark = [], [], -999

    def flush():
        if cur:
            lines.append(" ".join(cur))
            cur.clear()

    for t, txt in segs:
        if any(a <= t < b for a, b in spons):
            continue
        txt = clean_text(txt)
        if not txt:
            continue
        while pending_ch and pending_ch[0][0] <= t:
            flush()
            lines.append(f"## {pending_ch.pop(0)[1]}")
            last_mark = -999
        if t - last_mark >= marker_every:
            flush()
            cur.append(f"[{fmt_t(t)}]")
            last_mark = t
        cur.append(txt)
    flush()
    head = (f"TITLE: {meta['title']}\nCHANNEL: {meta.get('channel')}  DATE: {meta.get('upload_date')}  VIEWS: {meta.get('view_count')}  "
            f"LENGTH: {fmt_t(meta.get('duration') or 0)}\n")
    out.write_text(head + "TRANSCRIPT:\n" + "\n".join(lines) + "\n", encoding="utf-8")
    meta["transcript_tokens_est"] = est_tokens(head + "\n".join(lines))
    jsave(d / "meta.json", meta)
    return out


def pick_visual_times(segs, max_frames=12, gap=25):
    hits = [t for t, txt in segs if CUE.search(txt)]
    clusters = []
    for t in hits:
        if clusters and t - clusters[-1][0] < gap:
            clusters[-1][1] += 1
        else:
            clusters.append([t, 1])
    return len(hits), sorted(c[0] for c in sorted(clusters, key=lambda c: -c[1])[:max_frames])


def make_sheet(d, vid, mode="auto", min_cues=6, max_frames=12):
    """Contact sheet of up to 12 frames (ffmpeg only, low-res download, deleted afterwards). Returns path or None."""
    sheet, meta = d / "sheet.jpg", jload(d / "meta.json")
    if sheet.exists():
        return sheet
    if mode == "off" or meta.get("visuals") in ("skipped", "download-failed") or not tool_cmd("ffmpeg"):
        return None
    n_cues, times = pick_visual_times(jload(d / "segments.json"), max_frames)
    meta["visual_cues"] = n_cues
    if (mode == "auto" and n_cues < min_cues) or not times:
        meta["visuals"] = "skipped"
        jsave(d / "meta.json", meta)
        return None
    vf = next(iter(d.glob("video.*")), None)
    if not vf:
        yt(["-f", "bv*[height<=360][ext=mp4]/bv*[height<=360]/worst", "--no-playlist", "-o", str(d / "video.%(ext)s"),
            f"https://www.youtube.com/watch?v={vid}"])
        vf = next(iter(d.glob("video.*")), None)
        if not vf:
            meta["visuals"] = "download-failed"
            jsave(d / "meta.json", meta)
            return None
    frames = []
    for t in times[:max_frames]:
        f = d / f"_f{len(frames):02d}.jpg"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t + 1), "-i", str(vf), "-frames:v", "1", "-vf",
                        "scale=480:270:force_original_aspect_ratio=decrease,pad=480:270:(ow-iw)/2:(oh-ih)/2", str(f)], check=False)
        if f.exists():
            frames.append((t, f))
    ok = len(frames) >= 2
    if ok:
        cols = 3 if len(frames) <= 9 else 4
        rows = (len(frames) + cols - 1) // cols
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(d / "_f%02d.jpg"), "-vf", f"tile={cols}x{rows}",
                        "-frames:v", "1", "-q:v", "5", str(sheet)], check=False)
        ok = sheet.exists()
    for _, f in frames:
        f.unlink(missing_ok=True)
    vf.unlink(missing_ok=True)
    meta["visuals"] = "sheet" if ok else "skipped"
    meta["sheet_times"] = [fmt_t(t) for t, _ in frames] if ok else []
    jsave(d / "meta.json", meta)
    return sheet if ok else None


def vid_from(s):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})", s)
    return m.group(1) if m else s.strip()


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("query"); s.add_argument("--n", type=int, default=30)
    l = sp.add_parser("list"); l.add_argument("url"); l.add_argument("--tabs", default="videos,streams"); l.add_argument("--end", type=int)
    i = sp.add_parser("info"); i.add_argument("url")
    o = sp.add_parser("one"); o.add_argument("target"); o.add_argument("--out", default="research/_youtube")
    o.add_argument("--visuals", action="store_true"); o.add_argument("--whisper", action="store_true")
    o.add_argument("--lang", default="en"); o.add_argument("--sponsorblock", action="store_true")
    a = ap.parse_args()
    try:
        if a.cmd == "search":
            print(json.dumps(search(a.query, a.n), ensure_ascii=False))
        elif a.cmd == "list":
            for x in list_channel(a.url, tuple(a.tabs.split(",")), a.end):
                print(json.dumps(x, ensure_ascii=False))
        elif a.cmd == "info":
            print(json.dumps(channel_info(a.url), ensure_ascii=False))
        else:
            vid = vid_from(a.target)
            d = Path(a.out) / vid
            meta = fetch(d, vid, a.lang, a.whisper)
            tp = compress(d, vid, sponsorblock=a.sponsorblock)
            meta = jload(d / "meta.json")
            sheet = make_sheet(d, vid, "on" if a.visuals else "off") if a.visuals else None
            print(f"transcript: {tp}\nsource={meta.get('transcript_source')} tokens~{meta.get('transcript_tokens_est')} "
                  f"title={meta.get('title')!r}" + (f"\nsheet: {sheet}" if sheet else ""))
    except Skip as e:
        print(f"SKIP: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()
