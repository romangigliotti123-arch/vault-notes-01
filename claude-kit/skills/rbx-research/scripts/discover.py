#!/usr/bin/env python3
"""discover.py: find candidate creators/publishers per source, then enumerate their whole back-catalogue into manifest.json.
No API keys. Reddit uses public JSON/RSS with a proper User-Agent and a polite rate; GitHub uses `gh` if logged in, else anonymous REST.
Blocked or unreachable sources are recorded in <out>/.cache/unreachable.json and the run goes on.

  find youtube|github|reddit|web|papers --out DIR --q "query" [--q ...] [--urls u1 u2] [--enrich 12]
  enumerate youtube|github|reddit|feed|papers --out DIR --creator ID --target <url|owner|r/sub|u/name> [--max N]
"""
import argparse, base64, html, json, re, shutil, sys, time, urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *  # noqa
import ytwatch  # noqa


# ----------------------------------------------------------------------------- bookkeeping
def unreachable(out, source, what, why):
    p = out_paths(out)["cache"] / "unreachable.json"
    cur = jload(p, [])
    if not any(c["source"] == source and c["what"] == what for c in cur):
        cur.append({"source": source, "what": what, "why": str(why)[:160], "ts": now_iso()})
        jsave(p, cur)
    print(f"  unreachable: {source} {what}: {str(why)[:100]}")


def save_candidates(out, source, cands):
    d = out_paths(out)["cache"] / "candidates"
    old = jload(d / f"{source}.json", [])
    by = {c["id"]: c for c in old}
    for c in cands:
        by[c["id"]] = c
    jsave(d / f"{source}.json", list(by.values()))


def norm_key(it):
    u = re.sub(r"^https?://(www\.)?", "", (it.get("url") or "").lower()).split("#")[0].rstrip("/")
    return u or re.sub(r"\W+", "", (it.get("title") or "").lower())


def assign_priority(items):
    """lower = earlier. Union of newest-first and most-engaged-first, divided by relevance."""
    by_date = sorted(items, key=lambda x: x.get("date") or "", reverse=True)
    dr = {id(x): i + 1 for i, x in enumerate(by_date)}
    by_eng = sorted(items, key=lambda x: -(x.get("eng") or 0))
    er = {id(x): i + 1 for i, x in enumerate(by_eng)}
    for x in items:
        base = min(dr[id(x)], er[id(x)]) + 0.01 * (dr[id(x)] + er[id(x)])
        x["priority"] = round(base / (0.4 + x.get("rel", 0.5)), 3)


def add_items(out, items, kws):
    p = out_paths(out)["manifest"]
    man = jload(p, {"items": []})
    have = {i["id"] for i in man["items"]}
    keys = {norm_key(i) for i in man["items"]}
    added = 0
    for it in items:
        it.setdefault("status", "pending")
        it["rel"] = round(title_rel(it.get("title"), kws, it.get("desc", "")), 2)
    assign_priority(items)
    for it in items:
        if it["id"] in have or norm_key(it) in keys:
            continue
        it.pop("desc", None)
        man["items"].append(it)
        have.add(it["id"])
        keys.add(norm_key(it))
        added += 1
    jsave(p, man)
    return added, len(man["items"])


def iso(ts):
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return None


def days_since(d):
    try:
        return (datetime.now(timezone.utc) - datetime.fromisoformat(d[:10]).replace(tzinfo=timezone.utc)).days
    except Exception:
        return None


# ----------------------------------------------------------------------------- GitHub access
_GH = {}


def gh_mode():
    if "m" not in _GH:
        gh = shutil.which("gh")
        _GH["m"] = "gh" if gh and run([gh, "auth", "status"], timeout=30).returncode == 0 else "anon"
        _GH["bin"] = gh
    return _GH["m"]


def gh_get(path, raw=False):
    """Returns parsed JSON (or text if raw). None on failure. path like 'search/repositories?q=x'."""
    if gh_mode() == "gh":
        args = [_GH["bin"], "api", path] + (["-H", "Accept: application/vnd.github.raw"] if raw else [])
        r = run(args, timeout=60)
        if r.returncode == 0:
            if raw:
                return r.stdout
            try:
                return json.loads(r.stdout)
            except Exception:
                return None
        return None
    r = http_get("https://api.github.com/" + path, headers={"Accept": "application/vnd.github.raw" if raw else "application/vnd.github+json"})
    if r.status == 403 and r.headers.get("X-RateLimit-Remaining") == "0":
        print("  github anonymous rate limit hit (60/h); log in with `gh auth login` for 5000/h")
        return None
    if r.status != 200:
        return None
    return r.text() if raw else r.json()


def q(s):
    return urllib.parse.quote(s)


# ----------------------------------------------------------------------------- find: youtube
def find_youtube(a, st, kws):
    agg = {}
    for query in a.q:
        for v in ytwatch.search(query, a.n):
            cid = v.get("channel_id")
            if not cid:
                continue
            c = agg.setdefault(cid, {"source": "youtube", "id": cid, "name": v.get("channel"), "url": v.get("channel_url"),
                                      "titles": [], "views": [], "durs": [], "rels": []})
            c["titles"].append(v["title"])
            c["views"].append(v.get("views") or 0)
            c["durs"].append(v.get("duration") or 0)
            c["rels"].append(title_rel(v["title"], kws, v.get("description", "")))
    if not agg:
        unreachable(a.out, "youtube", "search", "no results (yt-dlp missing, blocked, or no match)")
        return
    cands = []
    for c in agg.values():
        n = len(c["titles"])
        cands.append({"source": "youtube", "id": c["id"], "name": c["name"], "url": c["url"], "sample_titles": c["titles"][:10],
                      "signals": {"hits": n, "title_match": round(sum(c["rels"]) / n, 2), "engagement": int(sum(c["views"]) / n),
                                  "depth_proxy": round(min(1.0, sum(c["durs"]) / n / 1500), 2), "followers": None,
                                  "last_post": None, "posts_per_month": None, "official": False}})
    cands.sort(key=lambda c: -(c["signals"]["hits"] * (0.3 + c["signals"]["title_match"])))
    for c in cands[: a.enrich]:
        try:
            info = ytwatch.channel_info(c["url"]) if c.get("url") else None
        except Skip as e:
            info = None
            print("  channel info failed:", str(e)[:80])
        if info:
            s = c["signals"]
            s.update({"followers": info.get("followers"), "last_post": info.get("last_post"), "posts_per_month": info.get("posts_per_month")})
            s["engagement"] = info.get("avg_views") or s["engagement"]
            c["sample_titles"] = [t for t in (info.get("sample_titles") or []) if t][:10] or c["sample_titles"]
            c["url"] = info.get("url") or c["url"]
    save_candidates(a.out, "youtube", cands)
    print(f"youtube: {len(cands)} channels found, top {min(a.enrich, len(cands))} enriched")


# ----------------------------------------------------------------------------- find: github
def find_github(a, st, kws):
    agg = {}

    def add(repo, extra_hit=1):
        o = repo["owner"]["login"]
        c = agg.setdefault(o, {"source": "github", "id": o, "name": o, "url": f"https://github.com/{o}", "repos": [],
                                "stars": 0, "pushed": "", "org": repo["owner"].get("type") == "Organization"})
        if repo["full_name"] not in [r["full_name"] for r in c["repos"]]:
            c["repos"].append({"full_name": repo["full_name"], "stars": repo.get("stargazers_count", 0),
                               "desc": repo.get("description") or ""})
            c["stars"] += repo.get("stargazers_count", 0)
        c["pushed"] = max(c["pushed"], (repo.get("pushed_at") or "")[:10])

    got = 0
    for query in a.q:
        for sort in ("stars", "updated"):
            j = gh_get(f"search/repositories?q={q(query)}&sort={sort}&per_page=30")
            if j is None:
                unreachable(a.out, "github", f"repo search '{query}'", "gh/REST failed or rate-limited")
                break
            for r in j.get("items", []):
                add(r)
                got += 1
        # awesome lists: read the best one and credit linked repos
        j = gh_get(f"search/repositories?q={q(query + ' awesome in:name,description')}&sort=stars&per_page=2")
        for r in (j or {}).get("items", [])[:1]:
            md = gh_get(f"repos/{r['full_name']}/readme", raw=True) or ""
            for full in list(dict.fromkeys(re.findall(r"github\.com/([\w.-]+/[\w.-]+)", md)))[:40]:
                rr = gh_get(f"repos/{full.rstrip('.')}")
                if rr and rr.get("owner"):
                    add(rr)
    cands = []
    for o, c in agg.items():
        c["repos"].sort(key=lambda r: -r["stars"])
        titles = [f"{r['full_name']}: {r['desc']}"[:140] for r in c["repos"][:10]]
        rels = [title_rel(t, kws) for t in titles]
        cands.append({"source": "github", "id": o, "name": o, "url": c["url"], "sample_titles": titles,
                      "signals": {"hits": len(c["repos"]), "title_match": round(sum(rels) / len(rels), 2), "engagement": c["stars"],
                                  "depth_proxy": 0.5, "followers": None, "last_post": c["pushed"] or None, "posts_per_month": None,
                                  "official": c["org"]}})
    cands.sort(key=lambda c: -(c["signals"]["hits"] * (0.3 + c["signals"]["title_match"]) + c["signals"]["engagement"] / 5000))
    for c in cands[: a.enrich]:
        u = gh_get(f"users/{c['id']}")
        if u:
            c["signals"]["followers"] = u.get("followers")
            c["blog"] = u.get("blog") or ""
    save_candidates(a.out, "github", cands)
    print(f"github: {len(cands)} owners from {got} repo hits (mode={gh_mode()})")
    blogs = [c["blog"] for c in cands[: a.enrich] if c.get("blog")]
    if blogs:
        print("  maintainer blogs (feed candidates for `find web --urls`): " + " ".join(blogs[:8]))


# ----------------------------------------------------------------------------- find: reddit
ANCHOR_RE = re.compile(r"""<a[^>]+href=["']([^"'#]+)["'][^>]*>(.*?)</a>""", re.S | re.I)
_RD = {"json_blocked": False}


def reddit_get(out, path, params="", record=True):
    """Public JSON with fallback host; returns parsed JSON or None (and records unreachable)."""
    why = ""
    if _RD["json_blocked"]:
        return None
    for host in ("www.reddit.com", "old.reddit.com"):
        r = http_get(f"https://{host}{path}.json?raw_json=1{params}", headers={"Accept": "application/json"}, retries=1)
        if r.status == 200 and r.json() is not None:
            return r.json()
        why = r.err or f"HTTP {r.status}"
        if r.status in (403, 429):
            _RD["json_blocked"] = r.status == 403  # blocked for this machine/IP: stop trying JSON this session
            break  # do not hammer the second host
    if record:
        unreachable(out, "reddit", "public JSON endpoints", why + "; using Atom/RSS fallback")
    return None


def reddit_rss(out, path, params=""):
    """Atom fallback (no scores). Returns list of dicts {id,title,link,author,sub,date,text} or []."""
    url = "https://www.reddit.com" + (path + ".rss" if path.endswith("/search") or path.endswith(".rss") else path.rstrip("/") + "/.rss") + "?" + params.lstrip("&")
    if time.time() < _RD.get("rss_blocked_until", 0):
        return []  # recently rate limited: leave Reddit alone for a while instead of retrying
    r = http_get(url, retries=1)
    if r.status != 200:
        _RD["rss_blocked_until"] = time.time() + 600
        unreachable(out, "reddit", "Atom/RSS feeds (rate limited or blocked)", (r.err or f"HTTP {r.status}") + "; paused Reddit for 10 minutes")
        return []
    try:
        root = ET.fromstring(r.body)
    except Exception:
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    res = []
    for e in root.findall("a:entry", ns):
        le = e.find("a:link", ns)
        cat = e.find("a:category", ns)
        au = (e.findtext("a:author/a:name", namespaces=ns) or "").replace("/u/", "")
        res.append({"id": (e.findtext("a:id", namespaces=ns) or "").replace("t3_", ""), "title": (e.findtext("a:title", namespaces=ns) or "").strip(),
                    "link": le.get("href") if le is not None else "", "author": au, "sub": cat.get("term") if cat is not None else "",
                    "date": (e.findtext("a:updated", namespaces=ns) or "")[:10],
                    "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(e.findtext("a:content", namespaces=ns) or "")))[:6000]})
    return res


def find_reddit(a, st, kws):
    subs, authors = {}, {}
    for query in a.q:
        j = reddit_get(a.out, "/subreddits/search", f"&q={q(query)}&limit=15")
        for ch in (j or {}).get("data", {}).get("children", []):
            d = ch["data"]
            if d.get("over18"):
                continue
            subs.setdefault(d["display_name"], {"subs": d.get("subscribers") or 0, "desc": d.get("public_description") or "", "hits": 0, "titles": [], "scores": [], "last": 0})
        j = reddit_get(a.out, "/search", f"&q={q(query)}&sort=top&t=all&limit=60")
        for ch in (j or {}).get("data", {}).get("children", []):
            d = ch["data"]
            if d.get("over_18"):
                continue
            s = subs.setdefault(d["subreddit"], {"subs": d.get("subreddit_subscribers") or 0, "desc": "", "hits": 0, "titles": [], "scores": [], "last": 0})
            s["hits"] += 1; s["titles"].append(d["title"]); s["scores"].append(d["score"]); s["last"] = max(s["last"], d["created_utc"])
            au = d.get("author")
            if au and au not in ("[deleted]", "AutoModerator"):
                u = authors.setdefault(au, {"hits": 0, "titles": [], "scores": [], "last": 0})
                u["hits"] += 1; u["titles"].append(d["title"]); u["scores"].append(d["score"]); u["last"] = max(u["last"], d["created_utc"])
    if not subs and not authors:  # JSON blocked: Atom search feed still works without scores
        for query in a.q:
            for e in reddit_rss(a.out, "/search", f"&q={q(query)}&sort=top&t=all&limit=100"):
                if not e["sub"]:
                    continue
                s = subs.setdefault(e["sub"], {"subs": None, "desc": "", "hits": 0, "titles": [], "scores": [], "last": 0})
                s["hits"] += 1; s["titles"].append(e["title"])
                u = authors.setdefault(e["author"], {"hits": 0, "titles": [], "scores": [], "last": 0}) if e["author"] else None
                if u:
                    u["hits"] += 1; u["titles"].append(e["title"])
        if subs:
            print("  reddit JSON blocked; used the RSS search feed (no scores or subscriber counts)")
    cands = []
    for name, s in subs.items():
        rels = [title_rel(t, kws) for t in s["titles"]] or [title_rel(s["desc"], kws)]
        cands.append({"source": "reddit", "id": f"r/{name}", "name": f"r/{name}", "url": f"https://www.reddit.com/r/{name}",
                      "sample_titles": s["titles"][:10],
                      "signals": {"hits": s["hits"], "title_match": round(sum(rels) / len(rels), 2),
                                  "engagement": int(sum(s["scores"]) / len(s["scores"])) if s["scores"] else 0, "depth_proxy": 0.4,
                                  "followers": s["subs"] or None, "last_post": iso(s["last"]) if s["last"] else None, "posts_per_month": None, "official": False}})
    for name, u in authors.items():
        if u["hits"] < 2:
            continue
        rels = [title_rel(t, kws) for t in u["titles"]]
        cands.append({"source": "reddit", "id": f"u/{name}", "name": f"u/{name}", "url": f"https://www.reddit.com/user/{name}",
                      "sample_titles": u["titles"][:10],
                      "signals": {"hits": u["hits"], "title_match": round(sum(rels) / len(rels), 2),
                                  "engagement": int(sum(u["scores"]) / len(u["scores"])) if u["scores"] else 0, "depth_proxy": 0.5, "followers": None,
                                  "last_post": iso(u["last"]) if u["last"] else None, "posts_per_month": None, "official": False}})
    if cands:
        save_candidates(a.out, "reddit", cands)
    print(f"reddit: {len(cands)} candidates ({len(subs)} subreddits, {sum(1 for u in authors.values() if u['hits'] >= 2)} repeat authors)")


# ----------------------------------------------------------------------------- feeds / web / hn / papers
def parse_date(s):
    if not s:
        return None
    try:
        return parsedate_to_datetime(s).strftime("%Y-%m-%d")
    except Exception:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", s.strip())
        return m.group(1) if m else None


def parse_feed(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except Exception:
        return None, []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    title = (root.findtext("channel/title") or root.findtext("a:title", namespaces=ns) or "").strip()
    out = []
    for it in root.findall("channel/item") + root.findall("a:entry", ns):
        t = (it.findtext("title") or it.findtext("a:title", namespaces=ns) or "").strip()
        link = it.findtext("link")
        if not link:
            le = it.find("a:link", ns)
            link = le.get("href") if le is not None else ""
        d = parse_date(it.findtext("pubDate") or it.findtext("a:published", namespaces=ns) or it.findtext("a:updated", namespaces=ns) or it.findtext("{http://purl.org/dc/elements/1.1/}date"))
        desc = it.findtext("description") or it.findtext("a:summary", namespaces=ns) or ""
        out.append({"title": html.unescape(t), "url": (link or "").strip(), "date": d, "desc": re.sub(r"<[^>]+>", " ", html.unescape(desc))[:300]})
    return title, out


def discover_feed(url):
    r = http_get(url)
    if r.status == 200 and (b"<rss" in r.body[:2000] or b"<feed" in r.body[:2000]):
        return url, r.body
    cands = []
    if r.status == 200:
        for m in re.finditer(r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]*>', r.text(), re.I):
            h = re.search(r'href=["\']([^"\']+)', m.group(0))
            if h:
                cands.append(urllib.parse.urljoin(url, h.group(1)))
    base = f"{urllib.parse.urlparse(url).scheme}://{urllib.parse.urlparse(url).netloc}"
    cands += [base + p for p in ("/feed", "/rss.xml", "/feed.xml", "/atom.xml", "/index.xml", "/rss", "/blog/rss.xml")]
    for c in dict.fromkeys(cands):
        rr = http_get(c, retries=0, timeout=15)
        if rr.status == 200 and (b"<rss" in rr.body[:2000] or b"<feed" in rr.body[:2000]):
            return c, rr.body
    return None, None


def sitemap_urls(url, limit=400):
    base = f"{urllib.parse.urlparse(url).scheme}://{urllib.parse.urlparse(url).netloc}"
    r = http_get(base + "/sitemap.xml", retries=0)
    if r.status != 200:
        return []
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text())
    subs = [u for u in urls if u.endswith(".xml")][:5]
    for s in subs:
        rr = http_get(s, retries=0)
        if rr.status == 200:
            urls += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", rr.text())
    return [u for u in urls if not u.endswith(".xml")][:limit]


def find_web(a, st, kws):
    cands = []
    for u in (a.urls or []):
        fu, body = discover_feed(u)
        dom = urllib.parse.urlparse(u).netloc
        if not body:
            unreachable(a.out, "web", dom, "no RSS/Atom feed found; will use sitemap if present")
            su = sitemap_urls(u, 50)
            if not su:
                continue
            cands.append({"source": "web", "id": dom, "name": dom, "url": u, "sample_titles": su[:8],
                          "signals": {"hits": 1, "title_match": round(sum(title_rel(x, kws) for x in su) / len(su), 2), "engagement": 0,
                                      "depth_proxy": 0.5, "followers": None, "last_post": None, "posts_per_month": None,
                                      "official": bool(re.search(r"docs?\.|developer|\.dev$|\.org$", dom))}, "feed": None})
            continue
        title, ents = parse_feed(body)
        dates = sorted([e["date"] for e in ents if e["date"]], reverse=True)
        ppm = None
        if len(dates) >= 2 and dates[0] != dates[-1]:
            span = max(1, (datetime.fromisoformat(dates[0]) - datetime.fromisoformat(dates[-1])).days)
            ppm = round(len(dates) / (span / 30.0), 2)
        rels = [title_rel(e["title"], kws, e["desc"]) for e in ents] or [0]
        cands.append({"source": "web", "id": dom, "name": title or dom, "url": u, "feed": fu, "sample_titles": [e["title"] for e in ents[:10]],
                      "signals": {"hits": sum(1 for r in rels if r > 0.3), "title_match": round(sum(rels) / len(rels), 2), "engagement": 0,
                                  "depth_proxy": round(min(1.0, sum(len(e["desc"]) for e in ents) / max(1, len(ents)) / 300), 2),
                                  "followers": None, "last_post": dates[0] if dates else None, "posts_per_month": ppm,
                                  "official": bool(re.search(r"docs?\.|developer|\.dev$|\.org$", dom))}})
    for query in a.q:  # Hacker News: publishers whose stories on this topic got traction (free API)
        r = http_get(f"https://hn.algolia.com/api/v1/search?query={q(query)}&tags=story&hitsPerPage=100")
        j = r.json() if r.status == 200 else None
        if not j:
            unreachable(a.out, "web", "hn.algolia.com", r.err or r.status)
            continue
        by = {}
        for h in j.get("hits", []):
            if not h.get("url"):
                continue
            dom = urllib.parse.urlparse(h["url"]).netloc.replace("www.", "")
            if dom in ("github.com", "youtube.com", "twitter.com", "x.com", "reddit.com", "medium.com", "arxiv.org"):
                continue
            b = by.setdefault(dom, {"t": [], "p": [], "d": 0})
            b["t"].append(h["title"]); b["p"].append(h.get("points") or 0); b["d"] = max(b["d"], h.get("created_at_i") or 0)
        for dom, b in by.items():
            cands.append({"source": "web", "id": dom, "name": dom, "url": "https://" + dom, "sample_titles": b["t"][:10],
                          "signals": {"hits": len(b["t"]), "title_match": round(sum(title_rel(t, kws) for t in b["t"]) / len(b["t"]), 2),
                                      "engagement": int(sum(b["p"]) / len(b["p"])), "depth_proxy": 0.5, "followers": None,
                                      "last_post": iso(b["d"]), "posts_per_month": None, "official": False}, "feed": None, "via": "hn"})
    if cands:
        save_candidates(a.out, "web", cands)
    print(f"web: {len(cands)} publishers")


def find_papers(a, st, kws):
    items = []
    for query in a.q:
        r = http_get(f"https://export.arxiv.org/api/query?search_query=all:{q(query)}&sortBy=relevance&max_results=40")
        if r.status != 200:
            unreachable(a.out, "papers", "arxiv", r.err or r.status)
            continue
        root = ET.fromstring(r.body)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        for e in root.findall("a:entry", ns):
            items.append({"title": " ".join((e.findtext("a:title", namespaces=ns) or "").split()), "url": e.findtext("a:id", namespaces=ns),
                          "date": (e.findtext("a:published", namespaces=ns) or "")[:10],
                          "desc": " ".join((e.findtext("a:summary", namespaces=ns) or "").split())[:300]})
    if items:
        cands = [{"source": "papers", "id": "arxiv", "name": "arXiv (relevance-ranked)", "url": "https://arxiv.org",
                  "sample_titles": [i["title"] for i in items[:10]],
                  "signals": {"hits": len(items), "title_match": round(sum(title_rel(i["title"], kws, i["desc"]) for i in items) / len(items), 2),
                              "engagement": 0, "depth_proxy": 0.9, "followers": None, "last_post": max(i["date"] for i in items),
                              "posts_per_month": None, "official": True}, "papers": items}]
        save_candidates(a.out, "papers", cands)
    print(f"papers: {len(items)} arXiv hits")


# ----------------------------------------------------------------------------- enumerate
def enum_youtube(a, st, kws):
    its = ytwatch.list_channel(a.target, end=a.max if a.max and a.max < 5000 else None)
    out = []
    for x in its:
        if (x.get("duration") or 0) and x["duration"] < 90:  # shorts: skip (little extractable content)
            continue
        out.append({"id": "yt-" + x["id"], "source": "youtube", "creator": a.creator, "kind": x["kind"], "title": x["title"],
                    "date": x.get("date"), "url": f"https://www.youtube.com/watch?v={x['id']}", "eng": x.get("views") or 0,
                    "fetch": {"t": "yt", "vid": x["id"]}})
    return out


def enum_github(a, st, kws):
    owner = a.target.split("/")[0]
    repos = []
    for page in (1, 2, 3):
        j = gh_get(f"users/{owner}/repos?per_page=100&sort=pushed&page={page}") or gh_get(f"orgs/{owner}/repos?per_page=100&page={page}") or []
        repos += [r for r in j if not r.get("fork") and not r.get("archived") or r.get("stargazers_count", 0) > 500]
        if len(j) < 100:
            break
    if "/" in a.target:
        repos = [r for r in repos if r["full_name"].lower() == a.target.lower()] or (gh_get(f"repos/{a.target}") and [gh_get(f"repos/{a.target}")]) or []
    for r in repos:
        r["_v"] = (r.get("stargazers_count", 0) + 5) * (0.2 + title_rel(r["full_name"] + " " + (r.get("description") or ""), kws))
    repos.sort(key=lambda r: -r["_v"])
    nrep = max(1, min(len(repos), a.max_repos))
    out = []
    for r in repos[:nrep]:
        fn, stars = r["full_name"], r.get("stargazers_count", 0)
        base = {"source": "github", "creator": a.creator, "eng": stars}
        out.append({**base, "id": f"gh-{safe_id(fn)}-readme", "kind": "readme", "title": f"{fn} README: {r.get('description') or ''}"[:140],
                    "date": (r.get("pushed_at") or "")[:10], "url": f"https://github.com/{fn}", "fetch": {"t": "gh", "kind": "readme", "repo": fn}})
        rel = gh_get(f"repos/{fn}/releases?per_page=30") or []
        for x in rel[:30]:
            if x.get("body"):
                out.append({**base, "id": f"gh-{safe_id(fn)}-rel-{safe_id(x['tag_name'])}", "kind": "release", "title": f"{fn} {x['tag_name']}: {x.get('name') or ''}"[:140],
                            "date": (x.get("published_at") or "")[:10], "url": x["html_url"], "fetch": {"t": "gh", "kind": "release", "repo": fn, "id": x["id"]}})
        tree = gh_get(f"repos/{fn}/git/trees/HEAD?recursive=1") or {}
        mds = [t["path"] for t in tree.get("tree", []) if t["path"].lower().endswith((".md", ".mdx", ".rst")) and t.get("size", 0) > 800
               and not re.search(r"(^|/)(node_modules|vendor|\.github|test|tests|changelog|license)", t["path"], re.I)
               and t["path"].lower() not in ("readme.md",)]
        mds.sort(key=lambda p: (-title_rel(p, kws), p.count("/")))
        for pth in mds[:25]:
            out.append({**base, "id": f"gh-{safe_id(fn)}-f-{safe_id(pth, 60)}", "kind": "doc", "title": f"{fn}/{pth}", "date": (r.get("pushed_at") or "")[:10],
                        "url": f"https://github.com/{fn}/blob/HEAD/{pth}", "fetch": {"t": "gh", "kind": "file", "repo": fn, "path": pth}})
        iss = gh_get(f"search/issues?q={q('repo:' + fn + ' is:issue')}&sort=comments&per_page=12") or {}
        for x in iss.get("items", []):
            out.append({**base, "id": f"gh-{safe_id(fn)}-i{x['number']}", "kind": "issue", "title": f"{fn}#{x['number']} {x['title']}"[:140],
                        "date": (x.get("created_at") or "")[:10], "url": x["html_url"], "eng": x.get("comments", 0) * 10,
                        "fetch": {"t": "gh", "kind": "issue", "repo": fn, "num": x["number"]}})
    return out


def enum_reddit(a, st, kws):
    t = a.target
    pages = []
    if t.startswith("u/"):
        paths = [(f"/user/{t[2:]}/submitted", "&sort=top&t=all"), (f"/user/{t[2:]}/submitted", "&sort=new")]
    else:
        nm = t[2:] if t.startswith("r/") else t
        paths = [(f"/r/{nm}/top", "&t=all"), (f"/r/{nm}/top", "&t=year"), (f"/r/{nm}/new", "")]
        if kws:
            paths.append((f"/r/{nm}/search", f"&q={q(' '.join(kws[:4]))}&restrict_sr=1&sort=top&t=all"))
    seen, out = set(), []
    for path, prm in paths:
        after = ""
        for _ in range(max(1, min(10, (a.max or 100) // 100))):
            j = reddit_get(a.out, path, f"{prm}&limit=100" + (f"&after={after}" if after else ""))
            if not j:
                for e in reddit_rss(a.out, path, f"{prm}&limit=100"):
                    if e["id"] and e["id"] not in seen:
                        seen.add(e["id"])
                        out.append({"id": f"rd-{e['id']}", "source": "reddit", "creator": a.creator, "kind": "thread", "title": e["title"],
                                    "date": e["date"], "url": e["link"], "eng": 0, "desc": e["text"][:200],
                                    "fetch": {"t": "reddit", "permalink": urllib.parse.urlparse(e["link"]).path}})
                break
            ch = j["data"]["children"]
            for c in ch:
                d = c["data"]
                if d["id"] in seen or d.get("over_18") or d.get("score", 0) < 3 or (d.get("is_self") and not d.get("selftext") and d.get("num_comments", 0) < 3):
                    continue
                seen.add(d["id"])
                out.append({"id": f"rd-{d['id']}", "source": "reddit", "creator": a.creator, "kind": "thread", "title": d["title"],
                            "date": iso(d["created_utc"]), "url": "https://www.reddit.com" + d["permalink"], "eng": d["score"] + 2 * d["num_comments"],
                            "desc": (d.get("selftext") or "")[:200], "fetch": {"t": "reddit", "permalink": d["permalink"]}})
            after = j["data"].get("after")
            if not after or not ch:
                break
    return out


def enum_feed(a, st, kws):
    fu, body = discover_feed(a.target)
    out = []
    if body:
        _, ents = parse_feed(body)
        for e in ents:
            if e["url"]:
                out.append({"id": "web-" + hashlib.sha1(e["url"].encode()).hexdigest()[:10], "source": "web", "creator": a.creator, "kind": "post",
                            "title": e["title"], "date": e["date"], "url": e["url"], "eng": 0, "desc": e["desc"], "fetch": {"t": "url"}})
    if len(out) < 20 or a.max_archive:  # feeds usually only hold the latest 10-50 posts: add the archive from the sitemap
        have = {o["url"] for o in out}
        for u in sitemap_urls(a.target, 600):
            if u in have or re.search(r"/(tag|tags|category|author|page|search)/", u) or u.rstrip("/") == a.target.rstrip("/"):
                continue
            if re.search(r"/(blog|posts?|articles?|docs?|guides?|\d{4})/", u):
                slug = u.rstrip("/").rsplit("/", 1)[-1].replace("-", " ").replace("_", " ")
                out.append({"id": "web-" + hashlib.sha1(u.encode()).hexdigest()[:10], "source": "web", "creator": a.creator, "kind": "post",
                            "title": slug, "date": None, "url": u, "eng": 0, "fetch": {"t": "url"}})
    if not out:  # no feed and no sitemap: use the post links visible on the page itself (same domain only)
        r = http_get(a.target)
        if r.status == 200 and robots_ok(a.target):
            dom = urllib.parse.urlparse(a.target).netloc
            seen = set()
            for m in ANCHOR_RE.finditer(r.text()):
                u = urllib.parse.urljoin(a.target, m.group(1))
                t = html.unescape(re.sub(r"<[^>]+>", " ", m.group(2))).strip()
                pu = urllib.parse.urlparse(u)
                if pu.netloc != dom or u in seen or len(pu.path) < 6 or len(t) < 8 or re.search(r"\.(png|jpg|css|js|zip)$", u):
                    continue
                seen.add(u)
                out.append({"id": "web-" + hashlib.sha1(u.encode()).hexdigest()[:10], "source": "web", "creator": a.creator, "kind": "post",
                            "title": t[:140], "date": None, "url": u, "eng": 0, "fetch": {"t": "url"}})
                if len(out) >= 80:
                    break
    return out


def enum_papers(a, st, kws):
    c = [x for x in jload(out_paths(a.out)["cache"] / "candidates" / "papers.json", []) if x["id"] == "arxiv"]
    out = []
    for p in (c[0]["papers"] if c else []):
        out.append({"id": "pp-" + safe_id(p["url"].rsplit("/", 1)[-1]), "source": "papers", "creator": "arxiv", "kind": "paper", "title": p["title"],
                    "date": p["date"], "url": p["url"].replace("/abs/", "/abs/"), "eng": 0, "desc": p["desc"], "fetch": {"t": "url"}})
    return out


import hashlib  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    f = sp.add_parser("find")
    f.add_argument("source", choices=["youtube", "github", "reddit", "web", "papers"])
    f.add_argument("--out", required=True)
    f.add_argument("--q", action="append", default=[])
    f.add_argument("--urls", nargs="*")
    f.add_argument("--n", type=int, default=30)
    f.add_argument("--enrich", type=int, default=12)
    e = sp.add_parser("enumerate")
    e.add_argument("source", choices=["youtube", "github", "reddit", "feed", "papers"])
    e.add_argument("--out", required=True)
    e.add_argument("--creator", required=True)
    e.add_argument("--target", required=True)
    e.add_argument("--max", type=int, default=0)
    e.add_argument("--max-repos", type=int, default=5)
    e.add_argument("--max-archive", action="store_true")
    a = ap.parse_args()
    st = load_state(a.out)
    kws = st["keywords"]
    if a.cmd == "find":
        if not a.q:
            a.q = [st["topic"]]
        {"youtube": find_youtube, "github": find_github, "reddit": find_reddit, "web": find_web, "papers": find_papers}[a.source](a, st, kws)
    else:
        try:
            items = {"youtube": enum_youtube, "github": enum_github, "reddit": enum_reddit, "feed": enum_feed, "papers": enum_papers}[a.source](a, st, kws)
        except Skip as ex:
            unreachable(a.out, a.source, a.target, ex)
            return
        added, total = add_items(a.out, items, kws)
        print(f"enumerate {a.source} {a.creator}: {len(items)} found, {added} new, manifest total {total}")


if __name__ == "__main__":
    main()
