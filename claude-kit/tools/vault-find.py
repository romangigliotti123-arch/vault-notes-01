#!/usr/bin/env python3
"""vault-find - ranked search over the notes of BOTH vaults (Roblox Dev Mastery Vault + AI Library Vault). Stdlib only.

  python vault-find.py "<what you need>" [-n 10] [--type skill|agent|creator|video|manager|kb|brain|game|reusable|system|skillpack|learned|any] [--side ai|roblox|both]
                       [--vault PATH ...] [--paths] [--json] [--reindex] [--all]

Searches note titles (item names), frontmatter descriptions and tags (skills, agents, creator hubs/videos, Manager topics,
Roblox KB topic files); ranks by word match (names > tags > description), rarer words count more, curated PICKS and own
items get a boost. Prints rank, [side:type], name, vault-relative path and a one-line description. Read the top hit's
note, then follow it. Vaults are found via --vault (repeatable), env CLAUDES_VAULT / AI_LIBRARY_VAULT, then
~/Obsidian/claudes-vault and ~/Obsidian/ai-library-vault. The index is cached (rebuilt when the vault's git HEAD changes).
Kit systems (claude-kit/systems/<Name>/README.md, type "system") are scanned live too.
Kit skill pack (claude-kit/skillpack, type "skillpack": the /rbx skills, built and planned) is scanned live too.
Games/ (the user's per-game notes and Games/_Reusable/<name>/README.md building blocks) is scanned live, never cached, and reusable items rank first.
--all also indexes Imported/ and Roblox/creators/<tier>/<creator>/ notes by title only (slower, larger).
"""
import argparse, hashlib, importlib.util, json, math, os, re, sys, time

STOP = set("a an the and or of for to in on with by is are be it its this that i me my we you your do does need want how what which when where can could should would please use using make get from as at into about any all some new".split())


def stem(w):
    for suf in ("ing", "ers", "er", "ies", "es", "ed", "s"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            w = w[: -len(suf)] + ("y" if suf == "ies" else "")
            break
    return w


def toks(text):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", (text or "").lower()) if w not in STOP and len(w) > 1]


def home():
    return os.path.expanduser("~")


def find_vaults(explicit):
    cands = []
    for p in explicit:
        cands.append(p)
    for env in ("CLAUDES_VAULT", "AI_LIBRARY_VAULT"):
        if os.environ.get(env):
            cands.append(os.environ[env])
    cands += [os.path.join(home(), "Obsidian", "claudes-vault"), os.path.join(home(), "Obsidian", "ai-library-vault")]
    out, seen = [], set()
    for c in cands:
        c = os.path.abspath(os.path.expanduser(c))
        if c in seen or not os.path.isdir(c):
            continue
        seen.add(c)
        side = "roblox" if os.path.isdir(os.path.join(c, "Roblox")) or os.path.isdir(os.path.join(c, "Manager")) else "ai"
        out.append((side, c))
    return out


def head_stamp(v):
    g = os.path.join(v, ".git")
    try:
        head = open(os.path.join(g, "HEAD"), encoding="utf-8").read().strip()
        if head.startswith("ref:"):
            ref = head[4:].strip()
            rp = os.path.join(g, *ref.split("/"))
            if os.path.isfile(rp):
                return open(rp, encoding="utf-8").read().strip()
            pr = os.path.join(g, "packed-refs")
            if os.path.isfile(pr):
                for ln in open(pr, encoding="utf-8"):
                    if ln.strip().endswith(ref):
                        return ln.split()[0]
        return head
    except OSError:
        pass
    try:
        st = os.stat(os.path.join(v, "CAPABILITIES.md"))
        return "m%d-%d" % (st.st_mtime, st.st_size)
    except OSError:
        return "nostamp"


def parse_fm(text):
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    fm = {}
    for ln in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
        if m and m.group(2).strip() not in ("", ">", "|", ">-", "|-"):
            v = m.group(2).strip()
            if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[m.group(1)] = v
    return fm, text[end + 4:]


def h1(body):
    for ln in body.split("\n", 40):
        if ln.startswith("# "):
            return ln[2:].strip()
    return ""


def first_para(body):
    for ln in body.split("\n"):
        s = ln.strip()
        if s and not s.startswith(("#", ">", "|", "-", "*", "[")) and len(s) > 30:
            return s
    return ""


def scan(side, v, include_all):
    recs = []

    def add(rel, typ, name, desc, tags, own=False):
        recs.append(dict(side=side, type=typ, name=name, path=rel, desc=re.sub(r"\s+", " ", desc or "").strip()[:400], tags=tags or "", own=own))

    def walk(sub, typ_of, read_n=6000, recursive=True, title_only=False):
        base = os.path.join(v, *sub.split("/"))
        if not os.path.isdir(base):
            return
        for d, dirs, files in os.walk(base):
            dirs[:] = [x for x in dirs if not x.startswith(".")]
            for fn in files:
                if not fn.endswith(".md") or fn.startswith("."):
                    continue
                full = os.path.join(d, fn)
                rel = os.path.relpath(full, v).replace("\\", "/")
                t = typ_of(rel, fn)
                if not t:
                    continue
                try:
                    with open(full, encoding="utf-8", errors="replace") as f:
                        txt = f.read(read_n)
                except OSError:
                    continue
                fm, body = parse_fm(txt)
                if title_only:
                    add(rel, t, fm.get("title") or h1(body) or fn[:-3], "", fm.get("tags", ""))
                    continue
                if rel.startswith("Library/skills/") or rel.startswith("Library/agents/"):
                    add(rel, t, fm.get("id") or fn[:-3], fm.get("description", ""), fm.get("tags", ""), fm.get("source") == "own")
                elif rel.startswith("Creators/videos/"):
                    if fn.endswith("-video-index.md"):
                        continue
                    sm = re.search(r"## Summary\n+(.+)", body)
                    add(rel, t, fm.get("title") or fn[:-3], (sm.group(1) if sm else ""), fm.get("tags", ""))
                else:
                    add(rel, t, h1(body) or fm.get("title") or fn[:-3], fm.get("description") or first_para(body), fm.get("tags", ""))

    walk("Library/skills", lambda r, f: "skill")
    walk("Library/agents", lambda r, f: "agent")
    walk("Creators/hubs", lambda r, f: "creator")
    walk("Creators/catalogue", lambda r, f: "creator")
    walk("Mentor", lambda r, f: "brain" if f == "Combined-Brain.md" else None, read_n=3000)
    walk("Creators/videos", lambda r, f: "video", read_n=2500)
    walk("Manager", lambda r, f: "manager" if (f.startswith("topic-") or f in ("Manager-README.md", "PROPOSALS.md")) else None, read_n=3000)
    walk("Roblox/roblox-kb", lambda r, f: "kb" if r.count("/") <= 3 and not f.startswith("case-studies-") else ("kb" if f.startswith("case-studies-") else None), read_n=2500)
    walk("Roblox/blender", lambda r, f: "kb" if r.count("/") <= 2 else None, read_n=2500)   # Blender research moved out of roblox-kb (vault polish O2)
    walk("learned", lambda r, f: "learned" if f != "README.md" else None, read_n=2500)   # curated community findings (learned/<topic>/<slug>.md)
    if include_all:
        walk("Imported", lambda r, f: "imported", title_only=True, read_n=600)
    return recs


def scan_games(side, v):
    """Games/ is the user's protected, never-cached area (per-game communities + Games/_Reusable/). Scanned live on every run."""
    recs = []
    base = os.path.join(v, "Games")
    if not os.path.isdir(base):
        return recs
    for d, dirs, files in os.walk(base):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for fn in files:
            if not fn.endswith(".md") or fn.startswith("."):
                continue
            full = os.path.join(d, fn)
            rel = os.path.relpath(full, v).replace("\\", "/")
            parts = rel.split("/")
            if len(parts) < 3 or (parts[1] == "_Reusable" and len(parts) < 4):
                continue
            try:
                with open(full, encoding="utf-8", errors="replace") as f:
                    txt = f.read(4000)
            except OSError:
                continue
            fm, body = parse_fm(txt)
            if parts[1] == "_Reusable":
                if fn.lower() != "readme.md":
                    continue
                recs.append(dict(side=side, type="reusable", name="%s (reusable, %s)" % (parts[2], fm.get("rating", "unrated").replace("/", "-")),
                                 path=rel, desc=re.sub(r"\s+", " ", fm.get("what") or fm.get("description") or first_para(body)).strip()[:400],
                                 tags=fm.get("tags", "") + " reusable " + parts[2], own=True))
            elif fn == "GAME.md" and len(parts) == 3:
                recs.append(dict(side=side, type="game", name="%s (your game, stage %s)" % (parts[1], fm.get("stage", "?")),
                                 path=rel, desc=re.sub(r"\s+", " ", fm.get("pitch") or first_para(body)).strip()[:400],
                                 tags="game " + parts[1] + " " + fm.get("genre", ""), own=True))
            elif len(parts) >= 3 and fn in ("design.md", "systems.md", "decisions.md"):
                recs.append(dict(side=side, type="game", name="%s %s" % (parts[1], fn[:-3]), path=rel,
                                 desc=re.sub(r"\s+", " ", first_para(body)).strip()[:400], tags="game " + parts[1], own=True))
    return recs


def scan_systems(side):
    """The kit's tested drop-in systems (claude-kit/systems/<Name>/README.md), scanned live. `vault` for these = the folder that holds claude-kit."""
    recs = []
    kit = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    base = os.path.join(kit, "systems")
    if not os.path.isdir(base):
        return recs
    for n in sorted(os.listdir(base)):
        full = os.path.join(base, n, "README.md")
        if not os.path.isdir(os.path.join(base, n, "src")):
            continue
        try:
            with open(full, encoding="utf-8", errors="replace") as f:
                txt = f.read(3000)
        except OSError:
            continue
        fm, body = parse_fm(txt)
        recs.append(dict(side=side, type="system", name="%s (kit system, %s)" % (n, "live-Studio-untested" if "NOT tested in live" in txt else "tested"),
                         path="%s/systems/%s/README.md" % (os.path.basename(kit), n),
                         desc=re.sub(r"\s+", " ", fm.get("what") or first_para(body)).strip()[:400],
                         tags=(fm.get("tags", "") + " system drop-in library " + n), own=False, root=os.path.dirname(kit)))
    return recs


def scan_skillpack(side):
    """The Roblox skill pack (claude-kit/skillpack/<category>/<name>/SKILL.md plus planned names from CATALOGUE.md), scanned live. Run with /rbx <name>."""
    kit = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    sp = os.path.join(kit, "tools", "skillpack.py")
    if not os.path.isfile(sp) or not os.path.isdir(os.path.join(kit, "skillpack")):
        return []
    try:
        spec = importlib.util.spec_from_file_location("skillpack_idx", sp)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        rows = m.records()
    except Exception:
        return []
    recs = []
    for r in rows:
        built = r["status"] == "built"
        recs.append(dict(side=side, type="skillpack", name=r["name"], path="%s/%s" % (os.path.basename(kit), r["path"]),
                         desc=("/rbx %s - " % r["name"] if built else "(planned, /rbx %s still works as best effort) " % r["name"]) + re.sub(r"\s+", " ", r["desc"]).strip()[:340],
                         tags="skillpack rbx %s %s" % (r["category"], r.get("tags", "")), own=False, root=os.path.dirname(kit), built=built))
    return recs


def cache_dir():
    d = os.environ.get("CLAUDE_KIT_CACHE")
    if d:
        return d
    c = os.environ.get("CLAUDE_CONFIG_DIR")
    return os.path.join(c if c else os.path.join(home(), ".claude"), "claude-kit", "cache")


def load_index(side, v, include_all, reindex):
    stamp = head_stamp(v) + ("+all" if include_all else "")
    key = hashlib.sha1(v.encode("utf-8")).hexdigest()[:10]
    cdir = cache_dir()
    cp = os.path.join(cdir, "vault-find-%s.json" % key)
    if not reindex and os.path.isfile(cp):
        try:
            d = json.load(open(cp, encoding="utf-8"))
            if d.get("stamp") == stamp and d.get("v") == 4:
                return d["recs"]
        except (OSError, ValueError):
            pass
    recs = scan(side, v, include_all)
    try:
        os.makedirs(cdir, exist_ok=True)
        json.dump(dict(v=4, stamp=stamp, recs=recs), open(cp, "w", encoding="utf-8"))
    except OSError:
        pass
    return recs


def picks_set(vaults):
    s = set()
    for side, v in vaults:
        p = os.path.join(v, "PICKS.md")
        if not os.path.isfile(p):
            p = os.path.join(v, "Library", "PICKS.md")
        if os.path.isfile(p):
            try:
                for m in re.finditer(r"\[\[([^\]|]+)", open(p, encoding="utf-8", errors="replace").read()):
                    s.add(m.group(1).strip())
            except OSError:
                pass
    return s


def rank(recs, query, picks):
    qt = toks(query)
    if not qt:
        return []
    qset = list(dict.fromkeys(qt))
    prep = []
    df = {w: 0 for w in qset}
    for r in recs:
        nt, tt, dt = set(toks(re.sub(r"^[SA]--[^-]+(?:-[^-]+)*--", "", r["name"]).replace("/", " ").replace("-", " "))), set(toks(r["tags"].replace("/", " ").replace("-", " "))), set(toks(r["desc"]))
        prep.append((nt, tt, dt))
        for w in qset:
            if w in nt or w in tt or w in dt:
                df[w] += 1
    n = max(len(recs), 1)
    idf = {w: math.log(1 + n / (1 + df[w])) for w in qset}
    scored = []
    for r, (nt, tt, dt) in zip(recs, prep):
        sc, hit = 0.0, 0
        for w in qset:
            s = 0.0
            if w in nt:
                s += 5
            if w in tt:
                s += 2.5
            if w in dt:
                s += 1.5
            if s:
                hit += 1
            sc += s * idf[w]
        if not hit:
            continue
        sc *= (0.5 + 0.5 * hit / len(qset)) ** 1.0 * (1 + 0.4 * (hit == len(qset)))
        ql = " ".join(qt)
        if ql and ql in " ".join(toks(r["desc"])):
            sc *= 1.3
        base = os.path.basename(r["path"])[:-3]
        if base in picks:
            sc *= 1.35
        if r["own"]:
            sc *= 1.25
        if r["type"] == "reusable":
            sc *= 1.3   # the user's own tested building blocks: use first
        elif r["type"] == "system":
            sc *= 1.2   # kit systems: after the user's own reusable items, before building
        elif r["type"] == "learned":
            sc *= 1.15   # curated findings from earlier work: check before researching again
        elif r["type"] == "skillpack":
            sc *= 1.1 if r.get("built") else 0.9   # pack skills: built ones first
        if r["type"] in ("video", "imported"):
            sc *= 0.55
        elif r["type"] in ("kb", "manager", "creator", "brain"):
            sc *= 0.8
        scored.append((sc, r))
    scored.sort(key=lambda x: -x[0])
    return scored


def main():
    ap = argparse.ArgumentParser(description="ranked search over both vaults")
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--type", default="any", choices=["any", "skill", "agent", "creator", "video", "manager", "kb", "brain", "imported", "game", "reusable", "system", "skillpack", "learned"])
    ap.add_argument("--side", default="both", choices=["both", "ai", "roblox"])
    ap.add_argument("--vault", action="append", default=[])
    ap.add_argument("--paths", action="store_true", help="print only vault-relative paths")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--reindex", action="store_true")
    ap.add_argument("--all", action="store_true", help="also index Imported/ by title")
    a = ap.parse_args()
    vaults = find_vaults(a.vault)
    if a.side != "both":
        vaults = [x for x in vaults if x[0] == a.side]
    if not vaults:
        print("vault-find: no vault found. Pass --vault <path> or set CLAUDES_VAULT / AI_LIBRARY_VAULT (default ~/Obsidian/claudes-vault, ~/Obsidian/ai-library-vault).", file=sys.stderr)
        return 2
    recs = []
    for side, v in vaults:
        for r in load_index(side, v, a.all, a.reindex) + (scan_games(side, v) + scan_systems(side) + scan_skillpack(side) if side == "roblox" else []):
            r = dict(r)
            r["vault"] = r.get("root") or v
            recs.append(r)
    if a.type != "any":
        recs = [r for r in recs if r["type"] == a.type]
    res = rank(recs, " ".join(a.query), picks_set(vaults))[: a.n]
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if a.json:
        print(json.dumps([dict(score=round(s, 2), **{k: r[k] for k in ("side", "type", "name", "path", "desc", "vault")}) for s, r in res], ensure_ascii=False))
        return 0
    if not res:
        print("vault-find: no match for %r. Try other words, or read CAPABILITIES.md at the vault root." % " ".join(a.query))
        return 1
    for i, (s, r) in enumerate(res, 1):
        if a.paths:
            print(os.path.join(r["vault"], *r["path"].split("/")))
            continue
        print("%d. [%s:%s] %s" % (i, r["side"], r["type"], r["name"]))
        print("   %s" % r["path"])
        if r["desc"]:
            print("   %s" % (r["desc"] if len(r["desc"]) <= 150 else r["desc"][:147].rstrip() + "..."))
    if not a.paths:
        print("(vault roots: %s)" % "; ".join("%s=%s" % (s, v) for s, v in vaults))
    return 0


if __name__ == "__main__":
    sys.exit(main())
