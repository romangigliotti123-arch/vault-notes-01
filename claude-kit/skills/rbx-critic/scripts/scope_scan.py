#!/usr/bin/env python3
"""scope_scan.py: "smallest complete change" check of the code gates (stdlib only, read-only).

  python scope_scan.py <project folder> [--game ID] [--scorer critic|builder] [--write GAME_FOLDER] [--strict]

The rule (rbx-luau, Smallest complete change): no code nobody uses, no half-finished code, nothing rebuilt that the vault already ships, no speculative
extras. Checks, each 0-10 with pass mark 7:
  SC1 orphan ModuleScripts never required (not .server/.client, not Vendor/Packages; folders walked by a GetChildren+require loader are waived)
      SC1 and the export half of SC4 only apply to a game: a folder with no .server/.client entry script is a library, whose modules are its API
  SC2 stubs and placeholders: TODO/FIXME, "not implemented", print/error/warn("TODO"), empty or return-nil-only named functions
  SC3 reuse before build: own PlayerData/Shop/DailyRewards/Analytics/Admin code while the kit system exists (no Systems/<Name> folder in the project)
  SC4 speculative generality: exported functions and Config keys that nothing references
  SC5 size outliers: files over 400 code lines (Vendor and GENERATED files excluded)
Output: JSON in the format of the other gates. --write GAME_FOLDER saves GAME_FOLDER/scope-scan/gate.json, found by rbx-bench's scorecard.py.
Findings are leads (dynamic requires and Rojo init modules can fool it): scored, never blocking; exit 0 unless --strict.
"""
import json
import os
import re
import sys
import time

PASS_MIN = 7.0
SKIP_DIRS = {"packages", "node_modules", ".git", "vendor", "_packages", "benchmarks", "__pycache__", "tests", "test"}
LIFECYCLE = {"new", "init", "start", "stop", "destroy", "cleanup", "clear", "reset", "step", "update", "onstart", "oninit", "__index", "__tostring", "__call"}
STUB = re.compile(r"\b(TODO|FIXME|XXX)\b|(?i:not implemented|\bplaceholder\b)")
EMPTY_FN = re.compile(r"(?:local\s+)?function\s+([\w.:]+)\s*\([^)]*\)(?:\s*:\s*[^\n]+?)?\s+(?:return(?:\s+nil)?\s+)?end\b")
SYSTEMS = {
    "PlayerData": (re.compile(r"^(PlayerData(Service)?|DataService|DataManager|ProfileManager)$", re.I), re.compile(r"UpdateAsync|GetDataStore|SetAsync")),
    "Shop": (re.compile(r"^(Shop(Service)?|PurchaseService|ReceiptHandler)$", re.I), re.compile(r"ProcessReceipt|PromptProductPurchase")),
    "DailyRewards": (re.compile(r"^Daily(Reward|Rewards|Login|Bonus)(Service)?$", re.I), None),
    "Analytics": (re.compile(r"^Analytics(Service)?$", re.I), None),
    "Admin": (re.compile(r"^Admin(Service|Commands)?$", re.I), None),
}
FIX = {
    "SC1": "delete the module or require it where it belongs (a module nobody requires is dead code)",
    "SC2": "finish it or delete it; a stub or placeholder is not done",
    "SC3": "use the vault system: python .rbx/claude-kit/tools/games.py system add <Name> --project <dir>",
    "SC4": "delete the unused export or Config key (add it when something needs it)",
    "SC5": "split the file by responsibility or cut what is not needed",
}


def luau_files(root):
    if os.path.isfile(root):
        return [root]
    out = []
    for d, dn, fn in os.walk(root):
        dn[:] = sorted(x for x in dn if x.lower() not in SKIP_DIRS)
        for f in sorted(fn):
            if f.endswith((".lua", ".luau")) and not f.endswith(".d.luau"):
                out.append(os.path.join(d, f))
    return out


def strip_comments(src):
    out = []
    for ln in src.split("\n"):
        i = ln.find("--")
        out.append(ln if i < 0 else ln[:i])
    return "\n".join(out)


def module_name(path):
    stem = os.path.basename(path).rsplit(".", 1)[0]
    if stem in ("init", "init.server", "init.client"):
        return os.path.basename(os.path.dirname(path))
    return stem


def load(root):
    data = {}
    for p in luau_files(root):
        try:
            raw = open(p, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
        except OSError:
            continue
        data[p] = dict(raw=raw, code=strip_comments(raw))
    return data


def is_game(data):
    return any(re.search(r"\.(server|client)\.luau?$", p) for p in data)


def sc1(data, rel):
    if not is_game(data):
        return 10.0, [], 0
    args = []
    for v in data.values():
        for m in re.finditer(r"\brequire\s*\(", v["code"]):
            args.append(v["code"][m.end():m.end() + 240].split("\n")[0])
    blob = "\n".join(args)
    loader_dirs = [os.path.dirname(p) for p, v in data.items()
                   if re.search(r"Get(Children|Descendants)\s*\(", v["code"]) and re.search(r"\brequire\s*\(\s*[a-z_]\w*\s*\)", v["code"])]
    mods, orphans = [], []
    for p in data:
        base = os.path.basename(p)
        if re.search(r"\.(server|client)\.luau?$", base) or re.search(r"\.(spec|test)\.luau?$", base) or base.startswith("init."):
            continue
        n = module_name(p)
        mods.append(p)
        if re.search(r"\b%s\b" % re.escape(n), blob):
            continue
        if any(os.path.abspath(p).startswith(os.path.abspath(d) + os.sep) or os.path.dirname(p) == d for d in loader_dirs):
            continue
        orphans.append(p)
    score = 10.0 if not orphans else max(0.0, round(10.0 - 25.0 * len(orphans) / max(1, len(mods)), 1))
    if len(orphans) >= 3:
        score = min(score, 6.0)
    return score, [dict(path=rel(p), check="SC1", found="module %s is never required" % module_name(p), fix=FIX["SC1"]) for p in orphans], len(mods)


def sc2(data, rel):
    found = []
    for p, v in data.items():
        for i, ln in enumerate(v["raw"].split("\n"), 1):
            if STUB.search(ln):
                found.append(dict(path="%s:%d" % (rel(p), i), check="SC2", found=ln.strip()[:100], fix=FIX["SC2"]))
        for m in EMPTY_FN.finditer(v["code"]):
            line = v["code"][:m.start()].count("\n") + 1
            found.append(dict(path="%s:%d" % (rel(p), line), check="SC2", found="empty function %s" % m.group(1), fix=FIX["SC2"]))
    return max(0.0, round(10.0 - 4.0 * len(found), 1)), found


def sc3(data, rel, root):
    top = root if os.path.isdir(root) else os.path.dirname(root)
    have = set()
    for d, dn, fn in os.walk(top):
        if os.path.basename(os.path.dirname(d)).lower() == "systems":
            have.add(os.path.basename(d))
    found = []
    for p, v in data.items():
        n = module_name(p)
        for name, (rx, sig) in SYSTEMS.items():
            if name in have or not rx.match(n):
                continue
            if "/systems/" in p.replace("\\", "/").lower():
                continue
            if sig is not None and not sig.search(v["code"]):
                continue
            found.append(dict(path=rel(p), check="SC3", found="own %s code while the kit system %s exists" % (n, name), fix=FIX["SC3"].replace("<Name>", name)))
            break
    return max(0.0, round(10.0 - 3.5 * len(found), 1)), found


def sc4(data, rel):
    exports, cfg = [], []
    game = is_game(data)
    for p, v in data.items():
        if re.search(r"\.(server|client)\.luau?$", p) or "/vendor/" in p.replace("\\", "/").lower():
            continue
        for m in (re.finditer(r"^function\s+\w+[.:](\w+)\s*\(|^\w+\.(\w+)\s*=\s*function\b", v["code"], re.M) if game else ()):
            n = m.group(1) or m.group(2)
            if n.lower() not in LIFECYCLE and not n.startswith("_"):
                exports.append((p, n))
        if module_name(p).lower() in ("config", "settings", "constants"):
            for m in re.finditer(r"^\t([A-Za-z_]\w*)\s*=", v["code"], re.M):
                cfg.append((p, m.group(1)))
    corpus = {p: v["code"] for p, v in data.items()}
    found = []
    for p, n in exports + cfg:
        w = re.compile(r"\b%s\b" % re.escape(n))
        used = any(len(w.findall(c)) > 1 if q == p else bool(w.search(c)) for q, c in corpus.items())
        if not used:
            found.append(dict(path=rel(p), check="SC4", found="%s %s is never referenced" % ("Config key" if (p, n) in cfg else "export", n), fix=FIX["SC4"]))
    total = max(1, len(exports) + len(cfg))
    return max(0.0, round(10.0 - 20.0 * len(found) / total, 1)), found, total


def sc5(data, rel):
    found = []
    for p, v in data.items():
        if "/vendor/" in p.replace("\\", "/").lower() or re.search(r"^\s*--\s*GENERATED\b", v["raw"], re.M):
            continue
        n = sum(1 for ln in v["code"].split("\n") if ln.strip())
        if n > 400:
            found.append(dict(path=rel(p), check="SC5", found="%d code lines" % n, fix=FIX["SC5"]))
    return max(0.0, round(10.0 - 2.5 * len(found), 1)), found


def build(root, game=None, scorer="critic"):
    base = root if os.path.isdir(root) else os.path.dirname(root)
    rel = lambda p: os.path.relpath(p, base).replace(os.sep, "/")
    data = load(root)
    s1, f1, nmods = sc1(data, rel)
    s2, f2 = sc2(data, rel)
    s3, f3 = sc3(data, rel, root)
    s4, f4, nexp = sc4(data, rel)
    s5, f5 = sc5(data, rel)
    checks = {"SC1": s1, "SC2": s2, "SC3": s3, "SC4": s4, "SC5": s5}
    allf = f1 + f2 + f3 + f4 + f5
    names = {"SC1": "orphan modules", "SC2": "stubs or placeholders", "SC3": "own code for a kit system", "SC4": "unused exports or Config keys", "SC5": "oversized files"}
    reasons = ["%s %.1f: %d %s" % (c, v, sum(1 for f in allf if f["check"] == c), names[c]) for c, v in checks.items() if v < 10]
    return dict(kind="scope-scan", scorer=scorer, game=game, severity="medium", pass_min=PASS_MIN, scripted=True,
                result="pass" if min(checks.values()) >= PASS_MIN else "fail", checks=checks, reasons=reasons, failing=allf[:30],
                counts=dict(files=len(data), modules=nmods, exports=nexp, findings=len(allf)),
                suggested_fix="open each lead, delete what nothing uses, finish or delete stubs" if allf else "none", time=time.strftime("%Y-%m-%dT%H:%M:%S"))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    opts, paths = {"game": None, "scorer": "critic", "write": None}, []
    i = 0
    while i < len(argv):
        if argv[i] in ("--game", "--scorer", "--write"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
            continue
        if not argv[i].startswith("--"):
            paths.append(argv[i])
        i += 1
    if not paths or not os.path.exists(paths[0]):
        print("give a project folder", file=sys.stderr)
        return 2
    rec = build(paths[0], opts["game"], opts["scorer"])
    if opts["write"]:
        d = os.path.join(opts["write"], "scope-scan")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "gate.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(rec, fh, indent=1)
            fh.write("\n")
    print(json.dumps(rec, indent=1))
    return 1 if ("--strict" in argv and rec["result"] == "fail") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
