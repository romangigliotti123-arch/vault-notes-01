#!/usr/bin/env python3
"""rtbf_check.py <project> [--templates templates.json] [--json] | --selftest

Right-to-be-forgotten readiness. Finds DataStore/OrderedDataStore names and key expressions in Luau and checks that a deletion template
could match them: the user id must appear in the store NAME, the SCOPE, or the KEY as the exact case-sensitive token {UserId}-equivalent
(in code: a Player.UserId / userId interpolation). Optional templates.json (list of {"name_pattern","scope_pattern","key_pattern"}, max 100
per the Creator Docs; live-check) is compared to the stores found: a store no template names is a gap. The data-stores right-to-be-forgotten
page is the authority; this is a static lead finder. Exit 1 on FAIL, 2 on bad input.
"""
import json
import os
import re
import sys
import tempfile

GET = re.compile(r"(?:GetDataStore|GetOrderedDataStore)\(\s*(['\"])(.+?)\1(?:\s*,\s*(['\"])(.+?)\3)?")
KEYUSE = re.compile(r"(?:GetAsync|SetAsync|UpdateAsync|RemoveAsync|IncrementAsync)\(\s*([^,)]+)")
UID = re.compile(r"(UserId|userId|\.Id\b|%d|\{.*\})")


def find(root):
    stores, keys = [], []
    for d, _, names in os.walk(root):
        if any(p in d.replace("\\", "/") for p in ("/.git", "/Packages", "/node_modules")):
            continue
        for n in names:
            if not n.endswith((".luau", ".lua")):
                continue
            p = os.path.join(d, n)
            rel = os.path.relpath(p, root).replace("\\", "/")
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace").read().splitlines(), 1):
                if line.strip().startswith("--"):
                    continue
                for m in GET.finditer(line):
                    stores.append({"name": m.group(2), "scope": m.group(4) or "global", "at": "%s:%d" % (rel, i)})
                for m in KEYUSE.finditer(line):
                    keys.append({"expr": m.group(1).strip(), "at": "%s:%d" % (rel, i)})
    return stores, keys


def tmpl_match(store, templates):
    for t in templates:
        pat = t.get("name_pattern", "")
        rx = re.escape(pat).replace(re.escape("{UserId}"), r"\d+|\{UserId\}")
        if re.fullmatch(rx, store["name"]) or pat == store["name"]:
            return True
    return False


def check(stores, keys, templates=None):
    rows = []
    if not stores and not keys:
        return [("INFO", "no DataStore use found by scan", "")]
    for s in stores:
        in_name = "{UserId}" in s["name"] or "UserId" in s["name"]
        in_scope = "UserId" in s["scope"]
        if templates is not None and not tmpl_match(s, templates):
            rows.append(("FAIL", "store %r has no deletion template" % s["name"], s["at"]))
        elif not (in_name or in_scope):
            rows.append(("WARN", "store %r: user id not in name/scope, so it must be in every key (see key lines)" % s["name"], s["at"]))
        else:
            rows.append(("OK", "store %r carries the user id in name/scope" % s["name"], s["at"]))
    ukeys = [k for k in keys if UID.search(k["expr"])]
    nokeys = [k for k in keys if not UID.search(k["expr"])]
    if keys:
        rows.append(("INFO", "%d key expressions mention a user id, %d do not" % (len(ukeys), len(nokeys)), ""))
    for k in nokeys[:5]:
        rows.append(("WARN", "key %s has no user id: personal data under it cannot be auto-deleted" % k["expr"], k["at"]))
    return rows


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write(
            'local a = DataStoreService:GetDataStore("Player_Data")\nlocal b = DataStoreService:GetDataStore("Notes", "scope")\n'
            'a:GetAsync("User_" .. player.UserId)\nb:SetAsync("global_note", 1)\n-- c:GetDataStore("x")\n')
        s, k = find(d)
        assert [x["name"] for x in s] == ["Player_Data", "Notes"], s
        r = check(s, k)
        assert any(x[0] == "WARN" and "global_note" in x[1] for x in r), r
        r2 = check(s, k, [{"name_pattern": "Player_Data"}])
        assert any(x[0] == "FAIL" and "Notes" in x[1] for x in r2) and not any(x[0] == "FAIL" and "Player_Data" in x[1] for x in r2), r2
    assert tmpl_match({"name": "User_123"}, [{"name_pattern": "User_{UserId}"}])
    assert not tmpl_match({"name": "User_abc"}, [{"name_pattern": "User_{UserId}"}])
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    rest, templates = list(argv), None
    if "--templates" in rest:
        i = rest.index("--templates")
        try:
            templates = json.load(open(rest[i + 1], encoding="utf-8"))
            assert isinstance(templates, list)
            if len(templates) > 100:
                print("FAIL: more than 100 templates (limit from the docs; live-check)")
                return 1
        except Exception as e:
            print("bad templates: %s" % e)
            return 2
        del rest[i:i + 2]
    args = [a for a in rest if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    stores, keys = find(args[0])
    rows = check(stores, keys, templates)
    if "--json" in rest:
        print(json.dumps(rows, indent=2))
    else:
        for lv, msg, at in rows:
            print("[%s] %s%s" % (lv, msg, "  <- " + at if at else ""))
        print("static scan: compare with Data Stores Manager and live-check the RTBF page; test with a dummy account")
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
