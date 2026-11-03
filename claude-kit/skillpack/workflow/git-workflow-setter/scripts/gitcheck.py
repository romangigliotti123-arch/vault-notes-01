#!/usr/bin/env python3
"""gitcheck.py - check the three git conventions the workflow uses. Stdlib only.

  python gitcheck.py ignore .gitignore        required ignore entries for a Rojo project
  python gitcheck.py branch feat/shop-limit   branch name: <type>/<kebab-slug>, type in feat fix chore docs exp
  python gitcheck.py msg "feat(shop): add purchase rate limit"   conventional commit subject, <= 72 chars
  python gitcheck.py --selftest

Ignore must contain: Packages/ (Wally output), sourcemap.json (generated), *.rbxl and *.rbxlx autosaves/binaries (release builds only
if the user asks), .env and *.key (secrets), build/ . Branch names and commit subjects are what changelog.py groups, so keep them
regular. Exit 0 pass, 1 fail.
"""
import re
import sys

REQUIRED_IGNORE = ["Packages/", "sourcemap.json", "*.rbxl", "*.rbxlx", ".env", "*.key", "build/"]
TYPES = "feat|fix|chore|docs|exp|perf|refactor|test"
BRANCH = re.compile(r"^(?:feat|fix|chore|docs|exp)/[a-z0-9]+(?:-[a-z0-9]+)*$")
MSG = re.compile(r"^(?:%s)(?:\([a-z0-9-]+\))?!?: \S.*$" % TYPES)


def check_ignore(text):
    lines = {ln.strip().lstrip("/") for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")}
    return ["missing ignore entry: " + r for r in REQUIRED_IGNORE if r not in lines and r.rstrip("/") not in lines]


def check_branch(name):
    if name in ("main", "master", "develop"):
        return []
    return [] if BRANCH.match(name) else ["branch %r must look like feat/short-kebab-name (types: feat fix chore docs exp)" % name]


def check_msg(subject):
    e = []
    if not MSG.match(subject):
        e.append("subject must look like 'type(scope): what changed' (types: %s)" % TYPES.replace("|", " "))
    if len(subject) > 72:
        e.append("subject is %d chars, keep it <= 72" % len(subject))
    if subject.rstrip().endswith("."):
        e.append("no trailing full stop")
    return e


def selftest():
    good = "# x\nPackages/\n/sourcemap.json\n*.rbxl\n*.rbxlx\n.env\n*.key\nbuild\n"
    assert check_ignore(good) == [], check_ignore(good)
    assert check_ignore(good.replace(".env\n", "")) == ["missing ignore entry: .env"]
    assert check_branch("feat/shop-limit") == [] and check_branch("main") == []
    assert check_branch("Feature_Shop") and check_branch("feat/Shop")
    assert check_msg("feat(shop): add purchase rate limit") == []
    assert check_msg("fixed stuff") and check_msg("fix: x" + "y" * 80) and check_msg("fix: done.")
    print("selftest ok (6 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or argv[0] not in ("ignore", "branch", "msg"):
        print(__doc__)
        return 1
    kind, arg = argv[0], " ".join(argv[1:])
    if kind == "ignore":
        errs = check_ignore(open(arg, encoding="utf-8").read())
    elif kind == "branch":
        errs = check_branch(arg)
    else:
        errs = check_msg(arg)
    print("PASS" if not errs else "FAIL: " + "; ".join(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
