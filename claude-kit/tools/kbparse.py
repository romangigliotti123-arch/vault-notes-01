#!/usr/bin/env python3
"""kbparse - shared parser for the Roblox knowledge base (roblox-kb topic files).

Used by kbq.py (cheap search CLI for agents) and build_tools.py (regenerates roblox-kb/_tools/*.md).
Nothing is hardcoded to a frozen file list: topic files are discovered at run time.
"""
import os
import re
import sys



SEARCHED = []   # (label, folder) of every place find_vault looked, for the error text


def _has_kb(p):
    return bool(p) and os.path.isdir(os.path.join(p, "Roblox", "roblox-kb"))


def _vault_candidates():
    """(label, folder) in priority order: explicit env / --vault, the vault that holds this tool, pointer, cwd, defaults. ONE-FOLDER layout: the tool sits in <vault>/.rbx/claude-kit/tools."""
    here = os.path.dirname(os.path.abspath(__file__))
    c = []
    for k in ("CLAUDES_VAULT", "RBX_DEV_VAULT"):
        if os.environ.get(k):
            c.append(("env " + k, os.environ[k]))
    kp = None
    try:
        if here not in sys.path:
            sys.path.insert(0, here)        # python -I drops the script folder from sys.path
        import kit_paths as kp  # noqa: E402
    except ImportError:
        kp = None
    if kp:
        try:
            c.append(("this tool's own location", kp.from_script(os.path.abspath(__file__))))
            c.append(("pointer " + kp.pointer_file(kp.config_dir()), kp.read_pointer(kp.config_dir())))
            c.append(("current folder and parents (%s)" % os.getcwd(), kp.from_cwd()))
            for d in kp.defaults():
                c.append(("default", d))
        except Exception:
            pass
    else:
        home = os.path.expanduser("~")
        for n in ("rbx-dev-vault", "claudes-vault"):
            c.append(("default", os.path.join(home, "Obsidian", n)))
    # legacy: running from <vault>/claude-kit/tools
    c.append(("legacy <vault>/claude-kit/tools", os.path.dirname(os.path.dirname(here))))
    return c


def find_vault():
    del SEARCHED[:]
    for label, p in _vault_candidates():
        if not p:
            SEARCHED.append((label, "(none)"))
            continue
        p = os.path.expanduser(os.path.expandvars(p))
        SEARCHED.append((label, p))
        if _has_kb(p):
            return p
    return None


def not_found_text():
    """Two lines for every 'vault not found' message: where it looked + the exact one-line fix."""
    find_vault()
    seen = []
    for label, p in SEARCHED:
        seen.append("%s: %s" % (label, str(p).replace("\\", "/")))
    kp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kit_paths.py").replace("\\", "/")
    return ("no vault with Roblox/roblox-kb found. Looked in: " + " | ".join(seen) + ".\n"
            "Fix: python \"" + kp + "\" --set \"<your vault folder>\"   (one time; or pass --vault <folder> to kbq.py, or set RBX_DEV_VAULT=<folder>; /rbx-update also repairs it)")


def find_assets():
    v = find_vault()
    for p in (os.environ.get("ROBLOX_ASSETS"), os.path.join(v, "Assets") if v else None, os.path.join(os.path.expanduser("~"), "roblox-assets"),
              os.path.join(os.environ.get("USERPROFILE", ""), "roblox-assets") if os.environ.get("USERPROFILE") else None):
        if p and os.path.isdir(p):
            return p
    return None


def _kb_dir():
    # ROBLOX_KB_DIR (explicit folder of topic files) wins; else <vault>/Roblox/roblox-kb
    if os.environ.get("ROBLOX_KB_DIR"):
        return os.environ["ROBLOX_KB_DIR"]
    v = find_vault()
    if v:
        return os.path.join(v, "Roblox", "roblox-kb")
    if os.environ.get("KBQ_WHERE"):
        return ""
    sys.stderr.write("kbq: " + not_found_text() + "\n")
    sys.exit(3)


KB_DIR = _kb_dir()
OUT_DIR = os.path.dirname(KB_DIR)  # <vault>/Roblox (docs, devforum, creator folders)

# Not topic files (reference/aggregate files); everything else that is not a case study is a topic.
NON_TOPIC = {"README", "_coverage", "sources", "quotes-by-topic", "all-numbers-and-benchmarks",
             "master-playbook", "tools-and-resources", "HOW-TO-USE"}
OFFICIAL_LABELS = {"Roblox", "Roblox Creators", "Roblox Creator Docs"}

LINK_RE = re.compile(r"\[([^\]]+?)\]\((https?://[^)\s]+)\)")
LABEL_RE = re.compile(r"^(?P<who>.+?) (?P<date>\d{4}-\d{2}(?:-\d{2})?)(?: (?P<ts>\d+:\d+(?::\d+)?))?$")
STOP = set("a an the and or of to in on for with is are be it its this that as at by from how what when do does "
           "my i we you your our should can will not no if then than into about vs per over under more most "
           "much many any all get got make made use using used game games roblox".split())


def topic_files(include_cases=False):
    out = []
    for fn in sorted(os.listdir(KB_DIR)):
        if not fn.endswith(".md") or fn.startswith("_"):
            continue
        name = fn[:-3]
        if name in NON_TOPIC:
            continue
        if name.startswith("case-studies-") and not include_cases:
            continue
        out.append(name)
    return out


def read(name):
    p = os.path.join(KB_DIR, name + ".md")
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def parse_cites(text):
    """Return list of dicts: who, date, ts, url, official(bool|None), label."""
    cites = []
    for m in LINK_RE.finditer(text):
        label, url = m.group(1), m.group(2)
        lm = LABEL_RE.match(label)
        if lm:
            who, date, ts = lm.group("who"), lm.group("date"), lm.group("ts") or ""
        else:
            who, date, ts = label, "", ""
        if "create.roblox.com" in url:
            off = True
        elif who in OFFICIAL_LABELS:
            off = True
        elif who == "Roblox DevForum":
            off = None  # staff posts are official, community posts are not: unknown from the label
        else:
            off = False
        cites.append({"who": who, "date": date, "ts": ts, "url": url, "official": off, "label": label})
    return cites


def flag_for(cites, text=""):
    """official | indie | mixed | devforum. Based on citation labels."""
    if not cites:
        return "unsourced"
    offs = [c["official"] for c in cites]
    if all(o is True for o in offs):
        f = "official"
    elif all(o is False for o in offs):
        f = "indie"
    elif all(o is None for o in offs):
        f = "devforum"
    elif any(o is True for o in offs):
        f = "mixed"
    else:
        f = "indie+devforum"
    return f


def best_cites(cites, n=2):
    """Pick up to n distinct citations, official and newest first."""
    seen, uniq = set(), []
    for c in cites:
        if c["url"] in seen:
            continue
        seen.add(c["url"])
        uniq.append(c)
    # within official group prefer newest date: stable sort by date desc then by group
    uniq.sort(key=lambda c: c["date"], reverse=True)
    uniq.sort(key=lambda c: 0 if c["official"] else 1 if c["official"] is None else 2)
    return uniq[:n]


def cite_md(c):
    return "[%s](%s)" % (c["label"], c["url"])


def split_sections(text):
    """Return dict normalized-section-key -> body, plus front matter dict."""
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
            text = text[end + 4:]
    secs, cur, buf = {}, "_head", []
    for line in text.splitlines():
        if line.startswith("## "):
            secs[cur] = "\n".join(buf)
            cur = norm_section(line[3:].strip())
            buf = []
        else:
            buf.append(line)
    secs[cur] = "\n".join(buf)
    return fm, secs


def norm_section(h):
    h = h.lower()
    for key, pat in (("rules", "rules and findings"), ("checklist", "checklist"), ("numbers", "numbers"),
                     ("agree", "where creators agree"), ("disagree", "where creators disagree"),
                     ("date", "date context"), ("instructions", "instructions for an agent"),
                     ("gaps", "not covered"), ("quotes", "quotes"), ("appendix", "appendix"),
                     ("overview", "overview")):
        if pat in h:
            return key
    return h


RULE_RE = re.compile(r"^- \*\*(?P<title>.+?)\*\*(?: \((?P<kind>[^)]*)\))?:? ?(?P<body>.*)$")


def parse_rules(body, topic):
    rules = []
    for line in body.splitlines():
        m = RULE_RE.match(line.strip())
        if not m:
            continue
        text = m.group("body")
        main, _, src = text.partition(" Sources:")
        if not src:
            main, _, src = text.partition("Sources:")
        cites = parse_cites(src if src else text)
        newest = ""
        nm = re.search(r"Newest source (\d{4}-\d{2}(?:-\d{2})?)", text)
        if nm:
            newest = nm.group(1)
        rules.append({"topic": topic, "kind": "rule", "title": m.group("title").strip(" :"),
                      "support": m.group("kind") or "", "text": main.strip(), "cites": cites,
                      "flag": flag_for(cites), "newest": newest})
    return rules


def parse_checklist(body, topic):
    items = []
    for line in body.splitlines():
        m = re.match(r"^- \[[ xX]\] (.+)$", line.strip())
        if m:
            items.append({"topic": topic, "kind": "check", "title": "", "text": m.group(1).strip(), "cites": [], "flag": "", "newest": ""})
    return items


def parse_instructions(body, topic):
    items = []
    for line in body.splitlines():
        m = re.match(r"^- (.+)$", line.strip())
        if m:
            items.append({"topic": topic, "kind": "instr", "title": "", "text": m.group(1).strip(), "cites": [], "flag": "", "newest": ""})
    return items


def split_row(line):
    cells, cur, depth = [], [], 0
    for ch in line.strip().strip("|"):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth = max(0, depth - 1)
        if ch == "|" and depth == 0:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur).strip())
    return cells


def parse_numbers(body, topic):
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Metric"):
            continue
        c = split_row(line)
        if len(c) < 3:
            continue
        metric, value, context = c[0], c[1], c[2]
        src = c[3] if len(c) > 3 else ""
        cites = parse_cites(src)
        rows.append({"topic": topic, "kind": "num", "title": metric, "value": value, "text": context,
                     "cites": cites, "flag": flag_for(cites), "newest": ""})
    return rows


def parse_disagree(body, topic):
    out, cur = [], None
    for line in body.splitlines():
        if line.startswith("- **"):
            if cur:
                out.append(cur)
            cur = {"topic": topic, "kind": "disagree", "title": line.strip()[2:].strip("* "), "text": "", "cites": [], "flag": "", "newest": ""}
        elif cur and line.strip().startswith("-"):
            cur["text"] += line.strip()[1:].strip() + " | "
    if cur:
        out.append(cur)
    return out


_cache = {}


def load(name):
    if name in _cache:
        return _cache[name]
    text = read(name)
    fm, secs = split_sections(text)
    d = {
        "name": name, "fm": fm, "sections": secs,
        "rules": parse_rules(secs.get("rules", ""), name),
        "checks": parse_checklist(secs.get("checklist", ""), name),
        "nums": parse_numbers(secs.get("numbers", ""), name),
        "instr": parse_instructions(secs.get("instructions", ""), name),
        "disagree": parse_disagree(secs.get("disagree", ""), name),
        "title": fm.get("title", name),
    }
    _cache[name] = d
    return d


def load_all(include_cases=False):
    return [load(n) for n in topic_files(include_cases)]


def tokens(s):
    toks = re.findall(r"[a-z0-9$%+]+", s.lower())
    out = []
    for t in toks:
        if t in STOP or len(t) < 2:
            continue
        if len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
        out.append(t)
    return out


def norm_key(s):
    return " ".join(sorted(set(tokens(s))))


def jaccard(a, b):
    a, b = set(tokens(a)), set(tokens(b))
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def dedupe(items, key=lambda x: x["text"], threshold=0.7):
    """Near-duplicate removal (token Jaccard). Keeps first; records count + topics of dropped copies."""
    kept, sets = [], []
    for it in items:
        ts = set(tokens(key(it)))
        dup = None
        if ts:
            for o, os_ in zip(kept, sets):
                inter = len(ts & os_)
                if inter and inter / len(ts | os_) >= threshold:
                    dup = o
                    break
        if dup is not None:
            dup["dups"] = dup.get("dups", 1) + 1
            dup.setdefault("also", []).append(it.get("topic", ""))
        else:
            it["dups"] = it.get("dups", 1)
            kept.append(it)
            sets.append(ts)
    return kept


def fix_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
