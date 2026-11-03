#!/usr/bin/env python3
"""ip_scan.py <project> [--terms terms.txt] [--json] | --selftest

Lead finder for copied or restricted material in text: names, descriptions, script comments, UI strings. Two lists:
  1. YOUR terms file (one name per line: brands, characters, songs, shows, games you suspect you echo; '#' comments). Nothing is built in
     about what is protected: that is a legal question for the owner, and rights holders can be anyone.
  2. Provenance cues built in: words that usually mean the material came from somewhere else (ripped, leaked, copied, 'from the toolbox',
     'free model', 'copyright', '(c)', 'all rights reserved', 'fan game', 'official', 'licensed by', 'not mine', 'credit to').
Output is leads with file:line. A hit is a prompt to check ownership or licence; no hit is not clearance. Exit 0 always (inventory),
2 on bad arguments.
"""
import json
import os
import re
import sys
import tempfile

CUES = [r"\bripped\b", r"\bleaked\b", r"\bcopied from\b", r"from the toolbox", r"free ?model", r"copyright", r"\(c\)", "©", r"all rights reserved",
        r"fan ?game", r"\bofficial\b", r"licensed by", r"not mine", r"credit to", r"\btaken from\b", r"\bport of\b", r"\bremake of\b"]
EXTS = (".luau", ".lua", ".md", ".txt", ".json", ".csv")


def terms_from(path):
    out = []
    for line in open(path, encoding="utf-8").read().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def scan(root, terms):
    cue_rx = [(c, re.compile(c, re.I)) for c in CUES]
    term_rx = [(t, re.compile(r"\b" + re.escape(t) + r"\b", re.I)) for t in terms]
    res = {"terms": [], "cues": []}
    for d, _, names in os.walk(root):
        if any(x in d.replace("\\", "/") for x in ("/.git", "/node_modules", "/Packages")):
            continue
        for n in names:
            if not n.endswith(EXTS):
                continue
            rel = os.path.relpath(os.path.join(d, n), root).replace("\\", "/")
            for i, line in enumerate(open(os.path.join(d, n), encoding="utf-8", errors="replace").read().splitlines(), 1):
                for t, rx in term_rx:
                    if rx.search(line):
                        res["terms"].append({"hit": t, "at": "%s:%d" % (rel, i), "line": line.strip()[:90]})
                for c, rx in cue_rx:
                    if rx.search(line):
                        res["cues"].append({"hit": c, "at": "%s:%d" % (rel, i), "line": line.strip()[:90]})
    return res


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w", encoding="utf-8").write("-- ripped from the toolbox\nlocal name = 'Super Mario Egg'\nprint('ok')\n")
        open(os.path.join(d, "t.txt"), "w").write("# comment\nSuper Mario\n\n")
        r = scan(d, terms_from(os.path.join(d, "t.txt")))
        assert any(x["hit"] == "Super Mario" for x in r["terms"]), r
        assert len([x for x in r["cues"] if x["at"].startswith("a.luau:1")]) == 2, r["cues"]
        assert not scan(d, [])["terms"]
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    rest = list(argv)
    terms = []
    if "--terms" in rest:
        i = rest.index("--terms")
        try:
            terms = terms_from(rest[i + 1])
        except (IndexError, OSError):
            print("bad --terms file")
            return 2
        del rest[i:i + 2]
    args = [a for a in rest if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    r = scan(args[0], terms)
    if "--json" in rest:
        print(json.dumps(r, indent=2))
        return 0
    print("%d term lead(s), %d provenance cue(s)" % (len(r["terms"]), len(r["cues"])))
    for k in ("terms", "cues"):
        for x in r[k][:20]:
            print("  [%s] %s  %s  | %s" % (k[:-1], x["hit"], x["at"], x["line"]))
    print("leads only: check ownership or licence for each; no hit is not clearance")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
