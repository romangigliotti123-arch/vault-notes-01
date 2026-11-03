#!/usr/bin/env python3
"""loc_scan.py <project> [--json] | --selftest

Finds the localization work in code: hard-coded player-facing strings, string concatenation that breaks translation, and AutoLocalize
opt-outs. It does not translate and does not touch the Creator Hub translation table; translations are checked with
marketing/store-localization-writer/scripts/loc_check.py (placeholders, ratios, game name).
Rows: HARD_TEXT (`.Text = "literal"` or Text = "literal" in a table), CONCAT (`"Coins: " .. n`: use a formatted string with a named
placeholder so the order can change per language), AUTOLOCALIZE_OFF (opt-outs; each should be a name/sign that must not change),
GETTRANSLATOR (code that already translates). Strings with no letters, or one word of 2 characters or fewer, are skipped. Exit 0, 2 on bad args.
"""
import json
import os
import re
import sys
import tempfile

HARD = re.compile(r"""\.Text\s*=\s*(["'])([^"']*[A-Za-z]{3,}[^"']*)\1""")
TBL = re.compile(r"""\bText\s*=\s*(["'])([^"']*[A-Za-z]{3,}[^"']*)\1""")
CAT = re.compile(r"""(["'][^"']*[A-Za-z]{3,}[^"']*["']\s*\.\.\s*[\w(]|[\w)]\s*\.\.\s*["'][^"']*[A-Za-z]{3,}[^"']*["'])""")
AUTO = re.compile(r"AutoLocalize\s*=\s*false")
TRANS = re.compile(r"(GetTranslatorForPlayerAsync|GetTranslatorForLocaleAsync|LocalizationService|FormatByKey)")


def scan(root):
    res = {"HARD_TEXT": [], "CONCAT": [], "AUTOLOCALIZE_OFF": [], "GETTRANSLATOR": []}
    for d, _, names in os.walk(root):
        if any(x in d.replace("\\", "/") for x in ("/.git", "/Packages", "/node_modules")):
            continue
        for n in names:
            if not n.endswith((".luau", ".lua")):
                continue
            rel = os.path.relpath(os.path.join(d, n), root).replace("\\", "/")
            for i, line in enumerate(open(os.path.join(d, n), encoding="utf-8", errors="replace").read().splitlines(), 1):
                if line.strip().startswith("--"):
                    continue
                at = "%s:%d" % (rel, i)
                if (HARD.search(line) or TBL.search(line)) and "print(" not in line and "warn(" not in line:
                    res["HARD_TEXT"].append(at)
                if CAT.search(line) and "print(" not in line and "warn(" not in line and (".Text" in line or "Text =" in line or "Label" in line):
                    res["CONCAT"].append(at)
                if AUTO.search(line):
                    res["AUTOLOCALIZE_OFF"].append(at)
                if TRANS.search(line):
                    res["GETTRANSLATOR"].append(at)
    return res


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write(
            'label.Text = "Welcome to the shop"\nlabel.Text = "Coins: " .. coins\nprint("Debug message here")\nnpc.AutoLocalize = false\n'
            'local t = LocalizationService:GetTranslatorForPlayerAsync(p)\nx.Text = ""\n-- label.Text = "Commented text"\n')
        r = scan(d)
        assert r["HARD_TEXT"] == ["a.luau:1", "a.luau:2"], r
        assert r["CONCAT"] == ["a.luau:2"], r
        assert r["AUTOLOCALIZE_OFF"] == ["a.luau:4"] and r["GETTRANSLATOR"] == ["a.luau:5"], r
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    r = scan(args[0])
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    for k, h in r.items():
        print("%-17s %3d  %s" % (k, len(h), ", ".join(h[:4])))
    print("Studio-side GUI text in .rbxl instances is not seen by this scan: use the localization tools' text capture in Studio (live-check)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
