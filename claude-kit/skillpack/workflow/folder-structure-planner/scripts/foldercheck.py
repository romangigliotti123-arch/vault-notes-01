#!/usr/bin/env python3
"""foldercheck.py - check a Rojo project's folder layout against the kit's convention. Stdlib only.

  python foldercheck.py <project-dir>          reads <project-dir>/default.project.json and walks src/
  python foldercheck.py --selftest

Checks: default.project.json parses; every "$path" exists; no "$path" is "." or the repo root (map a dedicated folder, not the
whole repo); server scripts (*.server.luau) live under a server folder and client scripts (*.client.luau) under a client folder,
never under shared; no file names with spaces; no .lua (use .luau, one extension across the project); no two files that differ
only by case (Windows would merge them). Layout it expects (the kit template): src/server -> ServerScriptService,
src/shared -> ReplicatedStorage.Shared, src/client -> StarterPlayer.StarterPlayerScripts. Exit 0 pass, 1 fail.
"""
import json
import os
import sys
import tempfile


def walk_paths(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$path" and isinstance(v, str):
                out.append(v)
            else:
                walk_paths(v, out)
    return out


def check(root):
    errs = []
    pj = os.path.join(root, "default.project.json")
    if not os.path.isfile(pj):
        return ["no default.project.json in " + root]
    try:
        data = json.load(open(pj, encoding="utf-8"))
    except ValueError as e:
        return ["default.project.json does not parse: %s" % e]
    for p in walk_paths(data.get("tree", {}), []):
        if p in (".", "./", ""):
            errs.append("$path %r maps the whole repo; map a dedicated folder such as src/server" % p)
        elif not os.path.exists(os.path.join(root, p)):
            errs.append("$path does not exist: " + p)
    seen = {}
    for dp, dn, fn in os.walk(os.path.join(root, "src")):
        rel = os.path.relpath(dp, root).replace("\\", "/")
        for f in fn:
            path = rel + "/" + f
            low = path.lower()
            if low in seen and seen[low] != path:
                errs.append("case-only duplicate: %s vs %s" % (seen[low], path))
            seen[low] = path
            if " " in f:
                errs.append("space in file name: " + path)
            if f.endswith(".lua") and not f.endswith(".luau"):
                errs.append("use .luau not .lua: " + path)
            parts = rel.split("/")
            if f.endswith(".server.luau") and "server" not in parts:
                errs.append("server script outside a server folder: " + path)
            if f.endswith(".client.luau") and "client" not in parts:
                errs.append("client script outside a client folder: " + path)
            if "shared" in parts and (f.endswith(".server.luau") or f.endswith(".client.luau")):
                errs.append("Script/LocalScript under shared (only ModuleScripts replicate safely): " + path)
    return errs


def selftest():
    d = tempfile.mkdtemp()
    for sub in ("server", "shared", "client"):
        os.makedirs(os.path.join(d, "src", sub))
    open(os.path.join(d, "src", "server", "Main.server.luau"), "w").write("print(1)\n")
    open(os.path.join(d, "src", "shared", "Util.luau"), "w").write("return {}\n")
    tree = {"name": "g", "tree": {"$className": "DataModel", "ServerScriptService": {"$path": "src/server"}, "ReplicatedStorage": {"Shared": {"$path": "src/shared"}}}}
    json.dump(tree, open(os.path.join(d, "default.project.json"), "w"))
    assert check(d) == [], check(d)
    open(os.path.join(d, "src", "shared", "Bad.server.luau"), "w").write("x\n")
    open(os.path.join(d, "src", "server", "old.lua"), "w").write("x\n")
    open(os.path.join(d, "src", "server", "has space.luau"), "w").write("x\n")
    e = check(d)
    assert any("outside a server" in x for x in e) and any("use .luau" in x for x in e) and any("space" in x for x in e), e
    tree["tree"]["Workspace"] = {"$path": "nope"}
    tree["tree"]["Lighting"] = {"$path": "."}
    json.dump(tree, open(os.path.join(d, "default.project.json"), "w"))
    e = check(d)
    assert any("does not exist" in x for x in e) and any("whole repo" in x for x in e), e
    print("selftest ok (3 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 1
    errs = check(argv[0])
    for e in errs:
        print("FAIL:", e)
    print("PASS" if not errs else "FAIL (%d)" % len(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
