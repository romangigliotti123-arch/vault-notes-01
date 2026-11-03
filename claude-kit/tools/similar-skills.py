#!/usr/bin/env python3
"""similar-skills.py: list the user's installed skills whose name or description looks like a kit skill (simple keyword overlap).
Read-only, stdlib. Used by install.ps1 / install.sh. Prints one line (nothing when no match):
  similar skills of yours (kit versions will be used): mine~kit-skill, ...
Usage: similar-skills.py --kit <claude-kit dir> --config <~/.claude dir>"""
import argparse, os, re

STOP = set("the and for with this that from your when use used uses into what them then than are you can its any one all not but how "
           "about also each will which their there skill skills user users claude code run runs make makes".split())
GENERIC = {"roblox", "game", "games", "dev", "skill", "check", "make", "vault", "kit", "mode", "rate", "plan", "new"}

def stem(w):
    w = w.lower()
    for suf in ("ies", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)] + ("y" if suf == "ies" else "")
    return w

def meta(path):
    try:
        t = open(path, encoding="utf-8", errors="replace").read(6000)
    except OSError:
        return None
    m = re.match(r"---\s*\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    d = re.search(r'^description:\s*(.*)$', fm, re.M)
    return (d.group(1) if d else "")

def toks(s):
    return {stem(w) for w in re.findall(r"[A-Za-z]{3,}", s) if w.lower() not in STOP}

def load(root, kit_names=None):
    out = {}
    if not os.path.isdir(root):
        return out
    for n in sorted(os.listdir(root)):
        f = os.path.join(root, n, "SKILL.md")
        if os.path.isfile(f):
            d = meta(f)
            if d is not None:
                out[n] = (toks(re.sub(r"[-_]", " ", n)), toks(d))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kit", required=True); ap.add_argument("--config", required=True)
    a = ap.parse_args()
    kit = load(os.path.join(a.kit, "skills"))
    mine = {k: v for k, v in load(os.path.join(a.config, "skills")).items() if k not in kit}
    hits = []
    for u, (un, ud) in mine.items():
        best = None
        for k, (kn, kd) in kit.items():
            ov = un & kn
            ng = ov - GENERIC
            ds = ud & kd
            score = 0
            if ng: score = 3
            elif len(ov) >= 2: score = 2
            elif len(ds) >= 8 and len(ds) / max(1, len(ud | kd)) >= 0.15: score = 1
            if score and (best is None or score > best[0]):
                best = (score, k)
        if best:
            hits.append("%s~%s" % (u, best[1]))
    if hits:
        print("similar skills of yours (kit versions will be used): " + ", ".join(hits[:12]) + (" ..." if len(hits) > 12 else ""))

if __name__ == "__main__":
    main()
