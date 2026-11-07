#!/usr/bin/env python3
"""skill-match.py "<task text>": which vault skill fits a described task (deterministic, stdlib, reads frontmatter only).

Reads name + description (+ disable-model-invocation) of <vault>/.claude/skills/*/SKILL.md (else the loaded vault-mode copy, else the kit's skills dir) and the extra trigger phrases in
tools/data/skill-match-hints.json. Scores with idf-weighted stemmed keywords (name words and trigger phrases count more). Prints up to 3 lines `score | /rbx-name | why` and one verdict line:
  MATCH: /rbx-x            clear winner
  AMBIGUOUS: /rbx-a or /rbx-b   the runner-up is close
  NO MATCH                 nothing fits (chat, question, small edit)
Always exits 0. Output is at most 4 lines."""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_SCORE = 5.0      # top score needed for MATCH / AMBIGUOUS
CLOSE = 0.72         # runner-up >= CLOSE * top  -> AMBIGUOUS
STOP = set("""a an the and or but if then so to of in on at by for with from into onto up out as is are was were be been am do does did have has had can could would should will shall may might must
i me my mine we our you your it its this that these those there here what which who whom how why when where not no yes please just also very really some any all more most much many few own
about over under again once than too only same other such get got let lets want need like make makes use using used thing things stuff something anything one two""".split())
KEEP = {"ui", "hud", "d1", "d7", "d30", "ads", "ad", "kb", "ecs", "oop", "npc", "gui", "api", "qa"}


def stem(w):
    if w in KEEP or len(w) <= 3:
        return w
    for suf, rep in (("ies", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", ""), ("ly", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[: -len(suf)] + rep
            break
    if len(w) > 4 and w[-1] == w[-2] and w[-1] not in "ls":
        w = w[:-1]
    return w


def toks(text):
    out = []
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        if w in STOP or (len(w) < 2 and w not in KEEP):
            continue
        out.append(stem(w))
    return out


def parse_front(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(6000)
    except OSError:
        return None
    m = re.match(r"---\s*\n(.*?)\n---", head, re.S)
    if not m:
        return None
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc = re.search(r'^description:\s*(?:"((?:[^"\\]|\\.)*)"|(.+))$', fm, re.M)
    if not name or not desc:
        return None
    d = (desc.group(1) if desc.group(1) is not None else desc.group(2)).replace('\\"', '"')
    return {"name": name.group(1).strip(), "desc": d, "dmi": bool(re.search(r"^disable-model-invocation:\s*true", fm, re.M))}


def skill_dirs():
    home = os.path.expanduser("~")
    c = []
    for base in (os.getcwd(), os.environ.get("CLAUDES_VAULT") or "", os.path.join(home, "Obsidian", "claudes-vault")):
        if base:
            c.append(os.path.join(base, ".claude", "skills"))
    c.append(os.path.join(os.path.dirname(HERE), "vault-mode", ".claude", "skills"))
    c.append(os.path.join(os.path.dirname(HERE), "skills"))
    return [d for d in c if os.path.isdir(d) and any(n.startswith("rbx") for n in os.listdir(d))]


def load_skills():
    dirs = skill_dirs()
    if not dirs:
        return {}
    root = dirs[0]
    out = {}
    for n in sorted(os.listdir(root)):
        fm = parse_front(os.path.join(root, n, "SKILL.md"))
        if fm and not fm["dmi"] and fm["name"].startswith("rbx"):
            out[fm["name"]] = fm
    return out


def load_hints():
    try:
        with open(os.path.join(HERE, "data", "skill-match-hints.json"), encoding="utf-8") as f:
            return {k: v for k, v in json.load(f).items() if not k.startswith("_")}
    except (OSError, ValueError):
        return {}


def build(skills, hints):
    """per skill: {stem: weight}, phrases [(tuple(stems), bonus)]"""
    docs = {}
    for name, s in skills.items():
        w = {}

        def add(ws, wt):
            for t in ws:
                if wt > w.get(t, 0):
                    w[t] = wt
        desc = s["desc"]
        first = re.split(r"(?<=[.;:])\s", desc, 1)[0]
        add(toks(desc), 1.0)
        add(toks(first), 1.5)
        add(toks(name.replace("rbx-", "").replace("-", " ")), 3.5)
        phr = []
        for q in re.findall(r"'([^']{4,60})'", desc):
            t = toks(q)
            add(t, 2.0)
            if len(t) > 1:
                phr.append((tuple(t), 3.0))
        for h in re.split(r"[;\n]", hints.get(name, "")):
            t = toks(h)
            if not t:
                continue
            add(t, 3.0)
            if len(t) > 1:
                phr.append((tuple(t), 4.0))
        docs[name] = (w, phr)
    return docs


def score(query, docs):
    q = toks(query)
    qs = set(q)
    df = {}
    for w, _ in docs.values():
        for t in w:
            df[t] = df.get(t, 0) + 1
    n = len(docs)
    res = []
    for name, (w, phr) in docs.items():
        sc, why, strong = 0.0, [], 0
        for t in qs:
            if t in w:
                v = w[t] * (1 + math.log(n / df[t])) / 1.0
                sc += v
                why.append((v, t))
                strong += w[t] >= 2.0
        for p, b in phr:
            if any(q[i:i + len(p)] == list(p) for i in range(len(q) - len(p) + 1)):
                sc += b
                why.append((b, " ".join(p)))
                strong += 2
        if strong < 2:
            sc = 0.0   # one lone keyword is not evidence of a task (needs a trigger phrase or two strong words)
        why.sort(reverse=True)
        res.append((sc, name, [t for _, t in why[:3]]))
    res.sort(key=lambda x: (-x[0], x[1]))
    return res


FOREIGN = {"python", "javascript", "typescript", "minecraft", "unity", "react", "sql", "css", "html", "java", "rust", "excel", "godot", "unreal", "flask", "django", "node"}


def match(query):
    ws = set(re.findall(r"[a-z]+", query.lower()))
    if ws & FOREIGN and not ws & {"roblox", "luau", "rbx", "vault"}:
        return [], "NO MATCH"
    skills = load_skills()
    if not skills:
        return [], "NO MATCH"
    res = score(query, build(skills, load_hints()))
    top = [r for r in res if r[0] > 0][:3]
    if not top or top[0][0] < MIN_SCORE:
        return top, "NO MATCH"
    if len(top) > 1 and top[1][0] >= CLOSE * top[0][0]:
        return top, "AMBIGUOUS: /%s or /%s" % (top[0][1], top[1][1])
    return top, "MATCH: /%s" % top[0][1]


def main(argv):
    text = " ".join(argv[1:]).strip()
    if not text:
        print("skill-match: usage skill-match.py \"<task text>\"")
        return 0
    top, verdict = match(text)
    for sc, name, why in top:
        print("%.1f | /%s | %s" % (sc, name, ", ".join(why)))
    print(verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
