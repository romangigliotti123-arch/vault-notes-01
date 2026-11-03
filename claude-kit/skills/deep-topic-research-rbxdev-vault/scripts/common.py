#!/usr/bin/env python3
"""Shared helpers for deep-topic-research-rbxdev-vault. Standard library only. No secrets are read, stored or logged."""
import csv, hashlib, json, math, os, re, shutil, subprocess, sys, threading, time
from collections import Counter
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
UA = os.environ.get("DTR_USER_AGENT", "script:deep-topic-research-rbxdev-vault:1.0 (personal research tool; low request rate)")
LIMIT_PAT = re.compile(r"(usage|rate|session|weekly|5-hour|monthly)[ -]limit|limit (reached|exceeded)|hit your limit|"
                       r"resets? (at|in)|too many requests|\b429\b|overloaded|credit balance|quota", re.I)


class RateLimit(Exception):
    pass


class ClaudeError(Exception):
    pass


class Skip(Exception):
    pass


# ----------------------------------------------------------------------------- basics
def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def slugify(s, n=48):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return (s[:n].strip("-")) or "topic"


def safe_id(s, n=80):
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", str(s)).strip("-")[:n]


def jload(p, default=None):
    for i in range(6):  # Windows: reading a file at the instant another process replaces it can fail once or twice
        try:
            return json.loads(Path(p).read_text(encoding="utf-8"))
        except (PermissionError, BlockingIOError):
            time.sleep(0.05 * (i + 1))
        except Exception:
            return default
    return default


_SAVE_LOCK = threading.Lock()


def jsave(p, obj):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with _SAVE_LOCK:
        tmp = p.with_name(p.name + ".tmp%d" % os.getpid())
        tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
        for i in range(8):  # Windows: replacing a file another process is reading can raise PermissionError for a moment
            try:
                os.replace(tmp, p)
                break
            except PermissionError:
                if i == 7:
                    raise
                time.sleep(0.05 * (i + 1))


def fmt_t(sec):
    sec = int(sec or 0)
    return f"{sec // 60}:{sec % 60:02d}" if sec < 3600 else f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"


def est_tokens(s):
    return int(len(s) / 4)


def run(cmd, **kw):
    kw.setdefault("timeout", 600)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    except FileNotFoundError as e:
        return subprocess.CompletedProcess(cmd, 127, "", str(e))
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(cmd, 124, "", "timeout")


def out_paths(out):
    out = Path(out)
    return {"out": out, "state": out / "state.json", "manifest": out / "manifest.json", "costs": out / "costs.csv",
            "cache": out / ".cache", "taxonomy": out / "taxonomy.json", "creators": out / ".cache" / "creators.json"}


def load_state(out):
    s = jload(out_paths(out)["state"])
    if not s:
        sys.exit(f"no state.json in {out}; run rt.py init first")
    return s


def save_state(out, st):
    jsave(out_paths(out)["state"], st)


def load_manifest(out):
    return jload(out_paths(out)["manifest"], {"items": []})


def tool_cmd(name):
    """Return argv prefix for yt-dlp / claude, or None."""
    if name == "yt-dlp":
        p = shutil.which("yt-dlp")
        if p:
            return [p]
        r = run([sys.executable, "-m", "yt_dlp", "--version"], timeout=60)
        return [sys.executable, "-m", "yt_dlp"] if r.returncode == 0 else None
    p = shutil.which(name)
    return [p] if p else None


# ----------------------------------------------------------------------------- polite HTTP
_HOST_LOCK = threading.Lock()
_HOST_LAST = {}
MIN_INTERVAL = {"www.reddit.com": 4.0, "old.reddit.com": 4.0, "api.github.com": 0.5, "export.arxiv.org": 3.0,
                "hn.algolia.com": 0.5}
_ROBOTS = {}


class Resp:
    def __init__(self, status, body, headers, err=""):
        self.status, self.body, self.headers, self.err = status, body, headers or {}, err

    def text(self):
        return (self.body or b"").decode("utf-8", errors="replace")

    def json(self):
        try:
            return json.loads(self.text())
        except Exception:
            return None


def http_get(url, headers=None, retries=2, timeout=25, max_bytes=3_000_000):
    """GET with a proper User-Agent, per-host rate limit, Retry-After handling. Never raises."""
    host = urllib.parse.urlparse(url).netloc
    hdr = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "identity"}
    hdr.update(headers or {})
    last = Resp(0, b"", {}, "no attempt")
    for i in range(retries + 1):
        with _HOST_LOCK:
            wait = MIN_INTERVAL.get(host, 1.0) - (time.time() - _HOST_LAST.get(host, 0))
            _HOST_LAST[host] = time.time() + max(0, wait)
        if wait > 0:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=timeout) as r:
                return Resp(r.status, r.read(max_bytes), dict(r.headers))
        except urllib.error.HTTPError as e:
            last = Resp(e.code, e.read(2000) if hasattr(e, "read") else b"", dict(e.headers or {}), f"HTTP {e.code}")
            if e.code in (429, 503) and i < retries:
                try:
                    ra = float(e.headers.get("Retry-After", 0))
                except Exception:
                    ra = 0
                time.sleep(min(max(ra, 5 * (2 ** i)), 60))
                continue
            return last
        except Exception as e:  # network down, DNS, TLS, timeout
            last = Resp(0, b"", {}, f"{type(e).__name__}: {e}"[:200])
            if i < retries:
                time.sleep(2 * (i + 1))
    return last


def robots_ok(url):
    """True if robots.txt allows our UA to fetch url (or robots.txt is unreachable). Used for generic web pages."""
    u = urllib.parse.urlparse(url)
    base = f"{u.scheme}://{u.netloc}"
    rp = _ROBOTS.get(base)
    if rp is None:
        rp = urllib.robotparser.RobotFileParser()
        r = http_get(base + "/robots.txt", retries=0, timeout=10)
        if r.status == 200:
            rp.parse(r.text().splitlines())
        elif r.status in (401, 403):
            rp.disallow_all = True
        else:
            rp.parse([])
        _ROBOTS[base] = rp
    return rp.can_fetch(UA, url) or rp.can_fetch("*", url)


# ----------------------------------------------------------------------------- cost log + limits
_COST_LOCK = threading.Lock()
_SPENT = {}


def _spent_from_csv(out):
    p = out_paths(out)["costs"]
    if not p.exists():
        return 0.0
    tot = 0.0
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                tot += float(r.get("cost_usd") or 0)
            except ValueError:
                pass  # a duplicated header line from a concurrent first write
    return tot


def spent(out):
    with _COST_LOCK:
        if str(out) not in _SPENT:
            _SPENT[str(out)] = _spent_from_csv(out)
        return _SPENT[str(out)]


def log_cost(out, item_id, stage, model, usage, cost, secs):
    p = out_paths(out)["costs"]
    p.parent.mkdir(parents=True, exist_ok=True)
    with _COST_LOCK:
        row = [now_iso(), item_id, stage, model, usage.get("input_tokens", 0), usage.get("cache_creation_input_tokens", 0),
               usage.get("cache_read_input_tokens", 0), usage.get("output_tokens", 0), f"{cost:.5f}", f"{secs:.1f}"]
        head = ["ts", "item_id", "stage", "model", "input_tokens", "cache_create", "cache_read", "output_tokens", "cost_usd", "secs"]
        try:  # O_EXCL makes exactly one process write the header, even when several workers log at the same moment
            fd = os.open(str(p), os.O_CREAT | os.O_EXCL | os.O_WRONLY | getattr(os, "O_BINARY", 0))
            os.write(fd, (",".join(head) + "\r\n").encode())
            os.close(fd)
        except FileExistsError:
            pass
        with open(p, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(row)
        _SPENT[str(out)] = _spent_from_csv(out)


def check_limits(out, st, phase="extract"):
    """Return a stop reason string, or None. phase: extract stops earlier than synth to keep a reserve."""
    lim = st["limits"]
    now = time.time()
    t_frac = 0.8 if phase == "extract" else 1.0
    start, deadline = st["started_ts"], lim["deadline_ts"]
    if now >= start + (deadline - start) * t_frac:
        return "time-limit"
    b_frac = lim.get("extract_budget_share", 0.75) if phase == "extract" else 1.0
    if spent(out) >= lim["budget_usd"] * b_frac:
        return "budget"
    return None


# ----------------------------------------------------------------------------- claude -p
_HELP = {}


def _claude_flags(cmd0):
    if "h" not in _HELP:
        r = run([cmd0, "--help"], timeout=60)
        _HELP["h"] = r.stdout + r.stderr
    return _HELP["h"]


def price_for(model):
    pr = jload(SKILL_DIR / "scripts" / "prices.json", {})
    return pr.get(model, pr.get("sonnet", {"in": 3.0, "out": 15.0}))


def call_claude(out, prompt, schema, model, effort, system, item_id="-", stage="x", image_path=None, budget=0.5):
    """One headless call with no tools / MCP / settings / session persistence. Returns (obj, cost).
    Counts as ONE concurrent worker against the user's subagent cap (callers enforce the pool size).
    DTR_STUB=1 swaps in the offline stand-in from stub.py (tests only, costs nothing)."""
    if os.environ.get("DTR_STUB"):
        import stub
        obj = stub.stub_call(stage, prompt, schema, model)
        log_cost(out, item_id, stage, "stub-" + model, {}, 0.0, 0.0)
        return obj, 0.0
    c = tool_cmd("claude")
    if not c:
        raise ClaudeError("claude CLI not on PATH (use subagent mode, see SKILL.md)")
    help_txt = _claude_flags(c[0])
    cwd = out_paths(out)["cache"] / "_cwd"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = c + ["-p", "--model", model]
    opt = lambda flag, *vals: cmd.extend([flag, *vals]) if flag in help_txt else None
    opt("--effort", effort)
    cmd += ["--output-format", "stream-json", "--input-format", "stream-json", "--verbose"] if image_path else ["--output-format", "json"]
    opt("--json-schema", json.dumps(schema))
    for fl in ("--no-session-persistence", "--strict-mcp-config", "--disable-slash-commands"):
        opt(fl)
    opt("--mcp-config", '{"mcpServers":{}}')
    opt("--tools", "")
    opt("--setting-sources", "")
    opt("--system-prompt", system)
    opt("--max-budget-usd", str(budget))
    stdin = prompt
    if image_path:
        import base64
        b64 = base64.b64encode(Path(image_path).read_bytes()).decode()
        stdin = json.dumps({"type": "user", "message": {"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}},
            {"type": "text", "text": prompt}]}}) + "\n"
    last = None
    for attempt in range(2):
        t0 = time.time()
        r = run(cmd, input=stdin, cwd=str(cwd), timeout=1500, env={**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "32000"})
        secs = time.time() - t0
        blob = (r.stdout or "") + (r.stderr or "")
        res = None
        try:
            if image_path:
                for line in r.stdout.splitlines():
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    if o.get("type") == "result":
                        res = o
            else:
                res = json.loads(r.stdout)
        except Exception:
            res = None
        if res is None:
            if LIMIT_PAT.search(blob):
                raise RateLimit(blob[:200])
            last = ClaudeError(f"no result json rc={r.returncode}: {blob[:200]}")
            continue
        usage = res.get("usage", {}) or {}
        cost = res.get("total_cost_usd")
        if cost is None:
            p = price_for(model)
            cost = (usage.get("input_tokens", 0) * p["in"] + usage.get("output_tokens", 0) * p["out"]) / 1e6
        cost = float(cost)
        log_cost(out, item_id, stage, model, usage, cost, secs)
        txt = res.get("result") or ""
        if res.get("is_error") or res.get("api_error_status"):
            if LIMIT_PAT.search(txt + blob) or res.get("api_error_status") in (429, 529):
                raise RateLimit(txt[:200])
            last = ClaudeError(f"is_error: {txt[:200]}")
            continue
        obj = res.get("structured_output")
        if obj is None:
            try:
                obj = json.loads(txt)
            except Exception:
                last = ClaudeError(f"no structured output: {txt[:150]}")
                continue
        return obj, cost
    raise last or ClaudeError("unknown")


# ----------------------------------------------------------------------------- topic keywords
_STOP = set("the a an and or of for to in on with how what why is are be do does using use from by at as it its this that "
            "best guide intro introduction tutorial about vs into your you".split())


def keywords(text, extra=None):
    toks = [t for t in re.findall(r"[a-z0-9+#]+", (text or "").lower()) if len(t) >= 3 and t not in _STOP]
    toks += [t.lower() for t in (extra or [])]
    return list(dict.fromkeys(toks))


def title_rel(title, kws, desc=""):
    """0..1 share of topic keywords present in title (+ half weight for description)."""
    if not kws:
        return 0.5
    t, d = (title or "").lower(), (desc or "").lower()
    hit = sum(1 for k in kws if k in t) + 0.5 * sum(1 for k in kws if k in d and k not in t)
    return min(1.0, hit / max(1, min(len(kws), 3)))


# ----------------------------------------------------------------------------- trust-layer helpers (shared by trust.py, cred.py, synth.py)
LABELS = ["OFFICIAL", "CORROBORATED", "SINGLE-SOURCE", "OUTDATED-UNSURE", "CONTRADICTED"]  # strongest to weakest
LABEL_RANK = {l: i for i, l in enumerate(LABELS)}
_STOPW = set("the and for with that this from are not use into you your can will has have was were but all any its they them then than when "
             "what which how also more most some such only over very just like about".split())
_TOK = re.compile(r"[a-z0-9_.#+]{3,}")


def toks(s):
    return {w.strip(".") for w in _TOK.findall((s or "").lower()) if w.strip(".") not in _STOPW and len(w.strip(".")) >= 3}


def parse_date(s):
    m = re.match(r"(\d{4})-?(\d{2})-?(\d{2})", str(s or ""))  # YYYYMMDD or YYYY-MM-DD
    try:
        return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3))).date()
    except Exception:
        return None


def today():
    return datetime.now().date()


class Index:
    """Tiny IDF-weighted keyword retrieval over (ref, text) pairs. No model, no dependencies."""
    def __init__(self, docs):
        self.docs = docs
        self.t = [toks(t) for _, t in docs]
        self.df = Counter()
        for ts in self.t:
            self.df.update(ts)

    def top(self, query, n=10, min_overlap=2):
        q, N, sc = toks(query), max(1, len(self.docs)), []
        for i, ts in enumerate(self.t):
            common = ts & q
            if len(common) >= min_overlap:
                sc.append((sum(math.log(1 + N / self.df[w]) for w in common), i))
        sc.sort(reverse=True)
        return [(self.docs[i][0], self.docs[i][1], s) for s, i in sc[:n]]


def load_extracts(out):
    d = out_paths(out)["cache"] / "extracts"
    return {p.stem: jload(p) for p in sorted(d.glob("*.json"))} if d.exists() else {}


def official_ids(out):
    """Creator ids treated as official (docs, manual, maintainers' repo): creators.json signals.official plus OUT/official.json."""
    ids = {cid for cid, c in jload(out_paths(out)["creators"], {}).items() if (c.get("signals") or {}).get("official")}
    ids |= set((jload(Path(out) / "official.json", {}) or {}).get("creators", []))
    return ids


def claim_lines(e):
    for c in e.get("claims", []):
        yield c.get("claim", "")
    for c in e.get("numbers", []):
        yield f"{c.get('metric')} = {c.get('value')} {c.get('context', '')}".strip()
    for c in e.get("techniques", []):
        yield f"{c.get('name')}: {c.get('how')}"


def official_corpus(out, ex=None):
    """[(ref, text)] from extractions of official creators plus cached official pages (.cache/official/*.txt)."""
    ex = ex if ex is not None else load_extracts(out)
    off, docs = official_ids(out), []
    for sid, e in ex.items():
        if (e.get("_meta") or {}).get("creator") in off:
            docs += [(sid, t[:320]) for t in claim_lines(e) if len(t) > 20]
    d = out_paths(out)["cache"] / "official"
    for p in sorted(d.glob("*.txt")) if d.exists() else []:
        for k, para in enumerate(x.strip() for x in re.split(r"\n\s*\n", p.read_text(encoding="utf-8", errors="replace"))):
            if len(para) >= 40:
                docs.append((f"{p.stem}#{k}", para[:500]))
    return docs


def cred_rows(out):
    """{creator_id: row} from the credibility stage, or {}."""
    rows = jload(out_paths(out)["cache"] / "cred" / "rows.json", [])
    return {r["c"]: r for r in rows} if isinstance(rows, list) else {}


# ----------------------------------------------------------------------------- default output location + protection marker
VERSION = "2.0"
RESEARCH_DIR = "My Research"
MARKER = "PROTECTED-RESEARCH.md"
NEVER_WRITE = {"library", "roblox", "manager", "imported", "assets"}  # vault folders owned by the sync; research must never land there


def find_vault():
    """A claudes-vault clone: $CLAUDES_VAULT, else ~/Obsidian/claudes-vault (Windows: the same under the user profile folder). None if absent."""
    cands = []
    if os.environ.get("CLAUDES_VAULT"):
        cands.append(Path(os.environ["CLAUDES_VAULT"]).expanduser())
    cands.append(Path.home() / "Obsidian" / "claudes-vault")
    if os.environ.get("USERPROFILE"):
        cands.append(Path(os.environ["USERPROFILE"]) / "Obsidian" / "claudes-vault")
    for c in cands:
        try:
            if c.is_dir():
                return c.resolve()
        except OSError:
            pass
    return None


def default_out(slug):
    """<vault>/My Research/<slug> when a vault clone exists, else ./research/<slug>."""
    v = find_vault()
    return (v / RESEARCH_DIR / slug) if v else (Path("research") / slug).resolve()


def check_out_allowed(out):
    """Refuse output inside the vault folders that the vault sync owns (Library/, Roblox/, Manager/, Imported/, Assets/)."""
    v = find_vault()
    if not v:
        return
    try:
        rel = Path(out).resolve().relative_to(v)
    except ValueError:
        return
    if rel.parts and rel.parts[0].lower() in NEVER_WRITE:
        sys.exit(f"refusing to write research into the vault folder '{rel.parts[0]}/' (owned by the vault sync). Use '{RESEARCH_DIR}/' or another folder.")


def write_marker(out, topic):
    """PROTECTED-RESEARCH.md in the research folder; also My Research/README.md once when the parent folder is My Research."""
    out = Path(out)
    m = out / MARKER
    if not m.exists():
        m.write_text(f'---\nprotected: true\ntopic: "{topic}"\ncreated: {now_iso()}\ntool: deep-topic-research-rbxdev-vault {VERSION}\n---\n'
                     "This research was made on this machine. update-rbxdev-vault never deletes it; do not delete.\n", encoding="utf-8")
    if out.parent.name == RESEARCH_DIR:
        r = out.parent / "README.md"
        if not r.exists():
            r.write_text("# My Research\n\nResearch folders made on this computer by the deep-topic-research-rbxdev-vault skill, one folder per topic. "
                         "They are local and private: this folder is not tracked by git and update-rbxdev-vault never changes or deletes it. "
                         f"Each folder holds a `{MARKER}` marker. Back it up yourself if it matters; do not delete a folder unless you are done with that topic.\n", encoding="utf-8")
