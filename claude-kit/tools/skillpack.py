#!/usr/bin/env python3
"""skillpack - index of the Roblox skill pack (claude-kit/skillpack/<category>/<name>/SKILL.md). Stdlib only.

  skillpack.py list [category]          categories with counts, or the skills of one category (built ones marked)
  skillpack.py find <words...> [-n 8]   ranked search over name, purpose and description (built and planned)
  skillpack.py path <name>              absolute path of the skill's SKILL.md (exit 3 = planned, not built yet; exit 1 = unknown)
  skillpack.py lint [name ...]          check built skills against the format in skillpack/QUALITY.md (exit 1 on a failure)
  skillpack.py catalogue [--write]      recount; with --write rewrite the status column of CATALOGUE.md from the folders on disk
  skillpack.py records                  JSON records (used by vault-find.py, mentor-hook.py and the vault generator)

CATALOGUE.md is the list of every planned skill: sections "## <category> - <title>", rows "| name | what it does | status |".
A skill is `built` when skillpack/<category>/<name>/SKILL.md exists; otherwise `planned`.
"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(os.path.dirname(HERE), "skillpack")
STOP = set("a an the and or of for to in on with by is are be it its this that i me my we you your do does need want how what which when where can could should would please use using make get from as at into about any all some new roblox game".split())
REQUIRED = ["When to use", "Inputs", "Procedure", "Studio MCP", "Fallback", "Evidence", "Output", "Acceptance", "Pitfalls", "Related"]


def stem(w):
    for suf in ("ing", "ers", "er", "ies", "es", "ed", "s"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[: -len(suf)] + ("y" if suf == "ies" else "")
    return w


def toks(t):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", (t or "").lower()) if w not in STOP and len(w) > 1]


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
        if m:
            v = m.group(2).strip()
            if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[m.group(1)] = v
    return fm, text[end + 4:]


def catalogue():
    """-> (categories [(id,title)], rows [dict(cat,name,purpose,status_in_file)])"""
    p = os.path.join(ROOT, "CATALOGUE.md")
    cats, rows, cur = [], [], None
    if not os.path.isfile(p):
        return cats, rows
    for ln in open(p, encoding="utf-8").read().replace("\r\n", "\n").split("\n"):
        m = re.match(r"^## (\S+) - (.+)$", ln)
        if m:
            cur = m.group(1)
            cats.append((cur, m.group(2).strip()))
            continue
        if cur and ln.startswith("|"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0] != "skill" and re.match(r"^[a-z0-9][a-z0-9-]*$", c[0]):
                rows.append(dict(cat=cur, name=c[0], purpose=c[1], status_in_file=c[2]))
    return cats, rows


def records():
    cats, rows = catalogue()
    titles = dict(cats)
    out = []
    for r in rows:
        f = os.path.join(ROOT, r["cat"], r["name"], "SKILL.md")
        built = os.path.isfile(f)
        d = dict(name=r["name"], category=r["cat"], category_title=titles.get(r["cat"], r["cat"]), purpose=r["purpose"], status="built" if built else "planned",
                 path="skillpack/%s/%s/SKILL.md" % (r["cat"], r["name"]), desc=r["purpose"], tags="", kb="", related="")
        if built:
            try:
                fm, _ = parse_fm(open(f, encoding="utf-8", errors="replace").read(6000))
                d["desc"] = fm.get("description") or r["purpose"]
                d["tags"] = fm.get("tags", "")
                d["kb"] = fm.get("kb", "")
                d["related"] = fm.get("related", "")
            except OSError:
                pass
        out.append(d)
    return out


def rank(recs, q):
    qt = list(dict.fromkeys(toks(q)))
    if not qt:
        return []
    prep, df = [], {w: 0 for w in qt}
    for r in recs:
        nt = set(toks(r["name"].replace("-", " ")))
        pt = set(toks(r["purpose"] + " " + r["tags"] + " " + r["category"]))
        dt = set(toks(r["desc"]))
        prep.append((nt, pt, dt))
        for w in qt:
            if w in nt or w in pt or w in dt:
                df[w] += 1
    n = max(len(recs), 1)
    idf = {w: math.log(1 + n / (1 + df[w])) for w in qt}
    res = []
    for r, (nt, pt, dt) in zip(recs, prep):
        sc, hit = 0.0, 0
        for w in qt:
            s = (5 if w in nt else 0) + (2.5 if w in pt else 0) + (1.0 if w in dt else 0)
            if s:
                hit += 1
            sc += s * idf[w]
        if not hit:
            continue
        sc *= (0.5 + 0.5 * hit / len(qt)) * (1 + 0.4 * (hit == len(qt)))
        if r["status"] == "built":
            sc *= 1.15
        res.append((sc, r))
    res.sort(key=lambda x: -x[0])
    return res


def lint_one(r):
    f = os.path.join(ROOT, r["category"], r["name"], "SKILL.md")
    errs = []
    txt = open(f, encoding="utf-8").read()
    fm, body = parse_fm(txt)
    if fm.get("name") != r["name"]:
        errs.append("frontmatter name != folder name")
    for k in ("description", "category", "kb", "related"):
        if not fm.get(k):
            errs.append("frontmatter %s missing" % k)
    if fm.get("category") and fm["category"] != r["category"]:
        errs.append("frontmatter category != folder")
    heads = [h.strip().lower() for h in re.findall(r"^##+ (.+)$", body, re.M)]
    for need in REQUIRED:
        if not any(need.lower() in h for h in heads):
            errs.append("missing section: " + need)
    if len(body.split()) < 350:
        errs.append("too short (%d words)" % len(body.split()))
    for pre, ref in set(re.findall(r"(?:([a-z0-9-]+)/)?scripts/([A-Za-z0-9_.-]+\.(?:luau|py))", body)):
        if pre and pre != r["name"]:
            hits = [os.path.join(ROOT, c, pre, "scripts", ref) for c in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, c))]
            ok = any(os.path.isfile(h) for h in hits) or pre in ("tests", "~")
        else:
            ok = os.path.isfile(os.path.join(ROOT, r["category"], r["name"], "scripts", ref))
        if not ok:
            errs.append("referenced script missing: %sscripts/%s" % (pre + "/" if pre else "", ref))
    vault_root = os.environ.get("CLAUDES_VAULT")
    if vault_root and os.path.isdir(vault_root):
        for rel in set(re.findall(r"(Roblox/[A-Za-z0-9_./-]+\.md|Mentor/[A-Za-z0-9_./-]+\.md)", fm.get("kb", "") + " " + body)):
            if not os.path.isfile(os.path.join(vault_root, *rel.split("/"))):
                errs.append("kb path not in vault: " + rel)
    return errs


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    cmd, rest = argv[0], argv[1:]
    if cmd == "records":
        print(json.dumps(records(), ensure_ascii=False))
        return 0
    recs = records()
    if cmd == "list":
        cats, _ = catalogue()
        if not rest:
            for cid, title in cats:
                c = [r for r in recs if r["category"] == cid]
                print("%-10s %2d/%2d built  %s" % (cid, sum(1 for r in c if r["status"] == "built"), len(c), title))
            print("(%d skills, %d built. /rbx list <category> for names)" % (len(recs), sum(1 for r in recs if r["status"] == "built")))
            return 0
        c = [r for r in recs if r["category"] == rest[0]]
        if not c:
            print("unknown category %r. Categories: %s" % (rest[0], ", ".join(x[0] for x in cats)))
            return 1
        for r in c:
            print("%s %-28s %s" % ("*" if r["status"] == "built" else " ", r["name"], r["purpose"]))
        print("(* = built; the others are planned: /rbx <name> still works, see the router)")
        return 0
    if cmd == "find":
        n = 8
        words = []
        i = 0
        while i < len(rest):
            if rest[i] == "-n":
                n = int(rest[i + 1])
                i += 2
            else:
                words.append(rest[i])
                i += 1
        res = rank(recs, " ".join(words))[:n]
        if not res:
            print("no skillpack match for %r (try /rbx list)" % " ".join(words))
            return 1
        for s, r in res:
            print("%s %-28s [%s] %s" % ("*" if r["status"] == "built" else " ", r["name"], r["category"], r["purpose"]))
        return 0
    if cmd == "path":
        name = rest[0].lstrip("/") if rest else ""
        r = next((x for x in recs if x["name"] == name), None)
        if not r:
            alt = [x["name"] for s, x in rank(recs, name.replace("-", " "))[:4]]
            print("unknown skill %r. Closest: %s" % (name, ", ".join(alt) or "none"))
            return 1
        if r["status"] != "built":
            print("PLANNED %s [%s]: %s" % (r["name"], r["category"], r["purpose"]))
            return 3
        print(os.path.join(ROOT, r["category"], r["name"], "SKILL.md"))
        return 0
    if cmd == "lint":
        built = [r for r in recs if r["status"] == "built" and (not rest or r["name"] in rest)]
        bad = 0
        for r in built:
            e = lint_one(r)
            print("%s %s%s" % ("FAIL" if e else "ok  ", r["name"], (": " + "; ".join(e)) if e else ""))
            bad += bool(e)
        known = {(r["category"], r["name"]) for r in recs}
        for cid in sorted(os.listdir(ROOT)) if os.path.isdir(ROOT) else []:
            d = os.path.join(ROOT, cid)
            if os.path.isdir(d):
                for nm in sorted(os.listdir(d)):
                    if os.path.isfile(os.path.join(d, nm, "SKILL.md")) and (cid, nm) not in known:
                        print("FAIL %s/%s: folder not in CATALOGUE.md" % (cid, nm))
                        bad += 1
        print("%d built checked, %d failing" % (len(built), bad))
        return 1 if bad else 0
    if cmd == "catalogue":
        p = os.path.join(ROOT, "CATALOGUE.md")
        lines = open(p, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
        st = {(r["category"], r["name"]): r["status"] for r in recs}
        cur, out, changed = None, [], 0
        for ln in lines:
            m = re.match(r"^## (\S+) - ", ln)
            if m:
                cur = m.group(1)
            elif cur and ln.startswith("|"):
                c = [x.strip() for x in ln.strip().strip("|").split("|")]
                if len(c) >= 3 and (cur, c[0]) in st and c[2] != st[(cur, c[0])]:
                    ln = "| %s | %s | %s |" % (c[0], c[1], st[(cur, c[0])])
                    changed += 1
            out.append(ln)
        total, built = len(recs), sum(1 for r in recs if r["status"] == "built")
        print("catalogue: %d skills, %d built, %d planned, %d status cells %s" % (total, built, total - built, changed, "rewritten" if "--write" in rest else "out of date (use --write)"))
        if "--write" in rest:
            txt = "\n".join(out)
            txt = re.sub(r"(?m)^Totals: .*$", "Totals: %d skills, %d built, %d planned." % (total, built, total - built), txt)
            open(p, "w", encoding="utf-8", newline="\n").write(txt)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
