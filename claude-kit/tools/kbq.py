#!/usr/bin/env python3
"""kbq - cheap, cited search over the Roblox knowledge base. For agents (and Roman) to use instead of reading whole topic files.

  python kbq.py [--vault <path>] <command> ...   vault path: --vault, else env CLAUDES_VAULT, else ~/Obsidian/claudes-vault
  python kbq.py where                      print the resolved VAULT, KB folder and ASSETS folder (env ROBLOX_ASSETS, else <vault>/Assets, else ~/roblox-assets)
  python kbq.py list                       topic files + one-line scope + coverage status (live from README/_coverage)
  python kbq.py route "<task>"             which topic files to read for a task (README task table + keyword score)
  python kbq.py find "<query>" [-n 12] [-t topicA,topicB] [-k rules,numbers,checklist,instr,disagree] [--official] [--max-chars 380]
  python kbq.py num "<query>" [-n 15]      benchmark/number rows only (value, context, flag, citation)
  python kbq.py section <topic> <rules|checklist|numbers|agree|disagree|date|instructions|gaps|quotes|overview> [--max-chars N]
  python kbq.py case "<genre or game>" [-n 4]   case-study notes (what creators say + transferable patterns)
  python kbq.py docs "<query>" [-n 8]      search official Creator Docs / DevForum notes (out/docs, out/devforum) for API/limit facts
  python kbq.py tools                      list the pre-built quick-reference files in roblox-kb/_tools

Every hit prints [topic | section | flag | newest-date] then the claim and up to 2 timestamped citations.
flag: official (Roblox docs/staff/sessions) | indie (creator self-reported) | mixed | devforum (could be staff or community) | unsourced.
"""
import argparse
import math
import os
import re
import sys

# --vault <path> (anywhere before the subcommand) sets CLAUDES_VAULT for this run
for _i, _a in enumerate(sys.argv):
    if _a == "--vault" and _i + 1 < len(sys.argv):
        os.environ["CLAUDES_VAULT"] = sys.argv[_i + 1]
        del sys.argv[_i:_i + 2]
        break
    if _a.startswith("--vault="):
        os.environ["CLAUDES_VAULT"] = _a.split("=", 1)[1]
        del sys.argv[_i]
        break

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) > 1 and sys.argv[1] == "where":
    os.environ["KBQ_WHERE"] = "1"  # where must work even when the vault is missing
import kbparse as K  # noqa: E402

K.fix_stdout()


def trunc(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def fmt_cites(cites, n=2):
    bc = K.best_cites(cites, n)
    return " ".join(K.cite_md(c) for c in bc)


def all_items(kinds, topics=None):
    items = []
    for d in K.load_all():
        if topics and d["name"] not in topics:
            continue
        if "rules" in kinds:
            items += d["rules"]
        if "numbers" in kinds:
            items += d["nums"]
        if "checklist" in kinds:
            items += d["checks"]
        if "instr" in kinds:
            items += d["instr"]
        if "disagree" in kinds:
            items += d["disagree"]
    return items


def score_items(items, query):
    qt = K.tokens(query)
    if not qt:
        return []
    # document frequency for idf
    df = {}
    prepared = []
    for it in items:
        tt = set(K.tokens(it["title"]))
        bt = K.tokens(it["text"] + " " + it.get("value", ""))
        prepared.append((it, tt, bt))
        for t in tt | set(bt):
            df[t] = df.get(t, 0) + 1
    n = max(1, len(items))
    scored = []
    for it, tt, bt in prepared:
        s = 0.0
        hit = 0
        for t in set(qt):
            idf = math.log(1 + n / (1 + df.get(t, 0)))
            c = 0.0
            if t in tt:
                c += 3.0
            c += min(3, bt.count(t)) * 1.0
            # prefix match for partial words (e.g. monetis -> monetisation)
            if c == 0 and len(t) >= 5:
                if any(x.startswith(t) for x in tt):
                    c += 1.5
                elif any(x.startswith(t) for x in bt):
                    c += 0.7
            if c:
                hit += 1
            s += c * idf
        if hit == 0:
            continue
        s *= (0.5 + hit / len(set(qt)))  # reward covering more query words
        if it["kind"] in ("rule", "num"):
            s *= 1.15
        if it.get("flag") == "official":
            s *= 1.1
        scored.append((s, it))
    scored.sort(key=lambda x: -x[0])
    return scored


def print_item(it, maxc):
    sec = {"rule": "rule", "num": "number", "check": "checklist", "instr": "agent-rule", "disagree": "disagreement"}[it["kind"]]
    flag = it.get("flag") or ""
    head = "[%s | %s%s%s]" % (it["topic"], sec, (" | " + flag) if flag else "", (" | " + it["newest"]) if it.get("newest") else "")
    if it["kind"] == "num":
        body = "**%s**: %s -- %s" % (it["title"], trunc(it["value"], 160), trunc(it["text"], maxc))
    elif it["kind"] == "rule":
        body = "**%s**: %s" % (it["title"], trunc(it["text"], maxc))
    elif it["kind"] == "disagree":
        body = "**%s**: %s" % (it["title"], trunc(it["text"], maxc))
    else:
        body = trunc(it["text"], maxc)
    cs = fmt_cites(it["cites"]) if it["cites"] else ""
    print("%s %s%s" % (head, body, ("\n    src: " + cs) if cs else ""))


def cmd_find(a):
    kinds = set((a.kinds or "rules,numbers,checklist,instr,disagree").split(","))
    topics = set(a.topics.split(",")) if a.topics else None
    items = all_items(kinds, topics)
    sc = score_items(items, a.query)
    if a.official:
        sc = [(s, i) for s, i in sc if i.get("flag") in ("official", "mixed", "devforum", "") ]
    # diversity: avoid near-duplicate hits
    shown, out = [], 0
    for s, it in sc:
        key = it["title"] + " " + it["text"]
        if any(K.jaccard(key, k) > 0.75 for k in shown):
            continue
        shown.append(key)
        print_item(it, a.max_chars)
        out += 1
        if out >= a.n:
            break
    if not out:
        print("(no hits; try other words, or `route` to find the topic file and read its section)")


def cmd_num(a):
    items = all_items({"numbers"}, set(a.topics.split(",")) if a.topics else None)
    sc = score_items(items, a.query)
    out = 0
    seen = []
    for s, it in sc:
        key = it["title"] + " " + it["value"]
        if any(K.jaccard(key, k) > 0.8 for k in seen):
            continue
        seen.append(key)
        print_item(it, a.max_chars)
        out += 1
        if out >= a.n:
            break
    if not out:
        print("(no numeric hits)")


def readme_table():
    """Parse the README task->files table live."""
    p = os.path.join(K.KB_DIR, "README.md")
    rows = []
    if not os.path.exists(p):
        return rows
    for line in open(p, encoding="utf-8", errors="replace"):
        if line.startswith("|") and "[[" in line and not line.startswith("|---"):
            c = K.split_row(line)
            if len(c) >= 2:
                files = re.findall(r"\[\[([^\]|]+)", c[1])
                rows.append((c[0], files))
    return rows


def readme_descs():
    p = os.path.join(K.KB_DIR, "README.md")
    d = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r"^- \[\[([^\]|]+)\]\] \(([^)]*)\): (.*)$", line.strip())
            if m:
                d[m.group(1)] = (m.group(2), m.group(3))
    return d


def coverage():
    p = os.path.join(K.KB_DIR, "_coverage.md")
    cov = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8", errors="replace"):
            if line.startswith("|") and not line.startswith("|---"):
                c = K.split_row(line)
                if len(c) >= 5 and re.match(r"^[a-z0-9-]+$", c[0]):
                    cov[c[0]] = (c[1].strip("*"), c[2], c[3])
    return cov


def cmd_list(a):
    descs, cov = readme_descs(), coverage()
    files = K.topic_files()
    # include topic files not in README (new ones from the other worker)
    for n in files:
        d = K.load(n)
        desc = descs.get(n, ("", ""))[1]
        if not desc:
            ov = d["sections"].get("overview", "").strip().splitlines()
            desc = ov[0] if ov else ""
        c = cov.get(n)
        print("%-34s rules=%-3d nums=%-3d chk=%-3d %s %s" % (n, len(d["rules"]), len(d["nums"]), len(d["checks"]), ("[" + c[0] + ", " + c[1] + " items]") if c else "", trunc(desc, 90)))
    cs = [f for f in os.listdir(K.KB_DIR) if f.startswith("case-studies-")]
    print("(+ %d case-study files; use `case`)" % len(cs))


def cmd_route(a):
    q = a.query
    qt = set(K.tokens(q))
    score = {}
    why = {}
    for task, files in readme_table():
        tt = set(K.tokens(task))
        ov = len(qt & tt)
        if ov:
            for i, f in enumerate(files):
                score[f] = score.get(f, 0) + ov * (3.0 - min(i, 4) * 0.4)
                why.setdefault(f, set()).add(task)
    descs = readme_descs()
    for n in K.topic_files():
        t = set(K.tokens(n.replace("-", " ") + " " + descs.get(n, ("", ""))[1]))
        ov = len(qt & t)
        if ov:
            score[n] = score.get(n, 0) + ov * 1.5
            why.setdefault(n, set()).add("topic name/scope")
    # item-level evidence: aggregate the best-scoring rules/numbers per topic
    sc = score_items(all_items({"rules", "numbers", "instr"}), q)[:40]
    mx = sc[0][0] if sc else 1.0
    for s_, it in sc:
        score[it["topic"]] = score.get(it["topic"], 0) + 4.0 * s_ / mx / 3
        why.setdefault(it["topic"], set()).add("matching rules/numbers")
    cov = coverage()
    ranked = sorted(score.items(), key=lambda x: -x[1])[: a.n]
    for f, s in ranked:
        if not os.path.exists(os.path.join(K.KB_DIR, f + ".md")):
            continue
        c = cov.get(f)
        print("%-34s score=%.1f %s  (via: %s)" % (f, s, ("[" + c[0] + "]") if c else "", "; ".join(sorted(why[f]))[:90]))
    print("Next: `kbq.py find \"<query>\" -t %s` or `kbq.py section <topic> checklist|numbers|instructions`." % ",".join(f for f, _ in ranked[:3]))
    thin = [f for f, _ in ranked if cov.get(f, ("",))[0] in ("thin", "none")]
    if thin:
        print("WARNING thin/none coverage: " + ", ".join(thin) + " (say so in the output; prefer official docs via `docs`).")


def cmd_section(a):
    d = K.load(a.topic)
    body = d["sections"].get(a.section)
    if body is None:
        print("no such section; have: " + ", ".join(k for k in d["sections"] if k != "_head"))
        return
    body = body.strip()
    if a.max_chars and len(body) > a.max_chars:
        body = body[: a.max_chars] + "\n…(truncated; raise --max-chars)"
    print(body)


def read_front(path):
    fm = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        txt = f.read()
    if txt.startswith("---"):
        e = txt.find("\n---", 3)
        for line in txt[3:e].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        txt = txt[e + 4:]
    return fm, txt


def cmd_case(a):
    qt = set(K.tokens(a.query))
    res = []
    for fn in os.listdir(K.KB_DIR):
        if not fn.startswith("case-studies-") or not fn.endswith(".md"):
            continue
        fm, txt = read_front(os.path.join(K.KB_DIR, fn))
        hay = K.tokens(fm.get("title", "") + " " + fm.get("genre", "") + " " + fn[13:-3].replace("-", " "))
        hay2 = K.tokens(txt)
        s = 3 * len(qt & set(hay)) + 0.3 * sum(min(3, hay2.count(t)) for t in qt)
        if s:
            res.append((s, fn, fm, txt))
    res.sort(key=lambda x: -x[0])
    for s, fn, fm, txt in res[: a.n]:
        print("== %s | genre: %s" % (fn[:-3], fm.get("genre", "?")))
        body = re.sub(r"\n+Index:.*$", "", txt, flags=re.S)
        print(trunc(body.replace("\n", " "), a.max_chars))
        print()
    if not res:
        print("(no case study matches; try genre words like simulator, tycoon, obby, horror, rpg, shooter, roleplay)")


def cmd_docs(a):
    qt = K.tokens(a.query)
    res = []
    for sub in ("docs", "devforum"):
        vd = os.path.join(K.OUT_DIR, sub, "Videos")
        if not os.path.isdir(vd):
            continue
        for fn in os.listdir(vd):
            p = os.path.join(vd, fn)
            try:
                fm, txt = read_front(p)
            except Exception:
                continue
            title = fm.get("title", fn)
            tt = set(K.tokens(title))
            body = txt
            # score bullet lines
            lines = [l for l in body.splitlines() if l.startswith("- ") or l.startswith("|")]
            for l in lines:
                lt = K.tokens(l)
                ls = set(lt)
                hit = len(set(qt) & ls)
                if hit:
                    s = hit + (1.0 if set(qt) & tt else 0) + (0.5 if fm.get("official", "") == "true" else 0)
                    res.append((s / (1 + 0.002 * len(l)), title, fm.get("url", ""), fm.get("date", ""), fm.get("official", ""), l))
    res.sort(key=lambda x: -x[0])
    seen, out = [], 0
    for s, title, url, date, off, l in res:
        l2 = re.sub(r"\[page\]\([^)]*\)|\[\[[^\]]*\]\]", "", l).strip("- ").strip()
        if any(K.jaccard(l2, k) > 0.7 for k in seen):
            continue
        seen.append(l2)
        print("[%s | %s | %s] %s\n    src: %s" % (title, "official" if off == "true" else "devforum/community", date, trunc(l2, a.max_chars), url))
        out += 1
        if out >= a.n:
            break
    if not out:
        print("(no docs hits)")


def cmd_where(a):
    # Output is shell-safe (eval "$(python3 kbq.py where)"); empty value = not found (reason on stderr).
    def q(p):
        return "'" + (p or "").replace("\\", "/").replace("'", "'\\''") + "'"
    v = K.find_vault()
    s = K.find_assets()
    if not v:
        sys.stderr.write("kbq: vault NOT FOUND (set CLAUDES_VAULT or clone it to ~/Obsidian/claudes-vault)\n")
    if not s:
        sys.stderr.write("kbq: assets NOT FOUND (run /rbx-update or vault-update.ps1/.sh to sync <vault>/Assets, or set ROBLOX_ASSETS)\n")
    print("VAULT=%s" % q(v))
    print("KB=%s" % q(os.path.join(v, "Roblox", "roblox-kb") if v else ""))
    print("ASSETS=%s" % q(s))
    print("KIT_TOOLS=%s" % q(os.path.dirname(os.path.abspath(__file__))))


def cmd_tools(a):
    td = os.path.join(K.KB_DIR, "_tools")
    if not os.path.isdir(td):
        print("no _tools dir yet; run build_tools.py")
        return
    for fn in sorted(os.listdir(td)):
        p = os.path.join(td, fn)
        print("%-28s %6d bytes  %s" % (fn, os.path.getsize(p), p))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("list"); p.set_defaults(f=cmd_list)
    p = sp.add_parser("route"); p.add_argument("query"); p.add_argument("-n", type=int, default=6); p.set_defaults(f=cmd_route)
    p = sp.add_parser("find"); p.add_argument("query"); p.add_argument("-n", type=int, default=12)
    p.add_argument("-t", "--topics"); p.add_argument("-k", "--kinds"); p.add_argument("--official", action="store_true")
    p.add_argument("--max-chars", type=int, default=380); p.set_defaults(f=cmd_find)
    p = sp.add_parser("num"); p.add_argument("query"); p.add_argument("-n", type=int, default=15)
    p.add_argument("-t", "--topics"); p.add_argument("--max-chars", type=int, default=240); p.set_defaults(f=cmd_num)
    p = sp.add_parser("section"); p.add_argument("topic"); p.add_argument("section"); p.add_argument("--max-chars", type=int, default=9000); p.set_defaults(f=cmd_section)
    p = sp.add_parser("case"); p.add_argument("query"); p.add_argument("-n", type=int, default=4); p.add_argument("--max-chars", type=int, default=1200); p.set_defaults(f=cmd_case)
    p = sp.add_parser("docs"); p.add_argument("query"); p.add_argument("-n", type=int, default=8); p.add_argument("--max-chars", type=int, default=420); p.set_defaults(f=cmd_docs)
    p = sp.add_parser("tools"); p.set_defaults(f=cmd_tools)
    p = sp.add_parser("where"); p.set_defaults(f=cmd_where)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
