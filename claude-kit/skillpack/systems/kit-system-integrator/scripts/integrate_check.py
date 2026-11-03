#!/usr/bin/env python3
"""integrate_check.py <project-folder> [--json]   (python integrate_check.py --selftest)

Static wiring check for a Roblox project that uses the claude-kit systems (PlayerData, Shop, DailyRewards, Analytics, Admin).
It reads *.luau / *.lua files only and reports FAIL / WARN / INFO lines. It cannot run Roblox: everything it finds is a lead to
confirm in Studio, and a clean report is not a live test. Exit 0 = no FAIL, 1 = at least one FAIL, 2 = bad arguments.
"""
import json, os, re, sys, tempfile

SYSTEMS = ["PlayerData", "Shop", "DailyRewards", "Analytics", "Admin"]


def read_all(root):
    files = {}
    for d, _, names in os.walk(root):
        if any(p in d.replace("\\", "/") for p in ("/Packages/", "/node_modules/", "/.git/")):
            continue
        for n in names:
            if n.endswith((".luau", ".lua")):
                p = os.path.join(d, n)
                try:
                    files[os.path.relpath(p, root).replace("\\", "/")] = open(p, encoding="utf-8", errors="replace").read()
                except OSError:
                    pass
    return files


def where(files, pattern, skip=(), flags=0):
    rx = re.compile(pattern, flags)
    hits = []
    for path, text in files.items():
        if any(s in path for s in skip):
            continue
        for i, line in enumerate(text.splitlines(), 1):
            code = line.split("--")[0]
            if rx.search(code):
                hits.append("%s:%d" % (path, i))
    return hits


def check(root):
    files = read_all(root)
    out = []

    def add(level, msg):
        out.append({"level": level, "msg": msg})

    if not files:
        add("FAIL", "no Luau files found under %s" % root)
        return out
    present = {s: any(("/%s/" % s) in "/" + p or p.startswith(s + "/") for p in files) for s in SYSTEMS}
    for s in SYSTEMS:
        add("INFO", "%s: %s" % (s, "installed" if present[s] else "not installed"))

    # one ProcessReceipt owner
    pr = where(files, r"\.ProcessReceipt\s*=", skip=("/Shop/",))
    shop_pr = where({k: v for k, v in files.items() if "/Shop/" in "/" + k}, r"\.ProcessReceipt\s*=")
    total = len(pr) + len(shop_pr)
    if total > 1:
        add("FAIL", "MarketplaceService.ProcessReceipt is assigned %d times (%s): the last assignment wins and purchases get lost" % (total, ", ".join(pr + shop_pr)))
    elif pr and present["Shop"]:
        add("FAIL", "ProcessReceipt assigned outside the Shop system while Shop is installed: %s" % ", ".join(pr))
    elif total == 0 and present["Shop"]:
        add("WARN", "Shop installed but nothing assigns ProcessReceipt (is ShopService.Start called?)")

    # direct DataStore use next to PlayerData
    if present["PlayerData"]:
        direct = where(files, r":(GetAsync|SetAsync|IncrementAsync)\s*\(", skip=("/PlayerData/", "/tests/", "Leaderboard"))
        if direct:
            add("WARN", "direct DataStore calls beside PlayerData (check they are not player save data, or leaderboards): " + ", ".join(direct[:6]))
        if not where(files, r"BindToClose"):
            add("FAIL", "PlayerData installed but no BindToClose anywhere: data written in the last seconds is lost on shutdown")
        if not where(files, r"PlayerRemoving"):
            add("FAIL", "no PlayerRemoving handler: sessions are never released, the next server waits for the lock timeout")
        if not where(files, r"LoadAsync\s*\("):
            add("WARN", "PlayerData installed but nothing calls LoadAsync")
    # wiring of the other systems
    if present["Shop"] and not where(files, r"ShopService\.Start|ShopService\s*\.\s*Start", skip=("/Shop/",)):
        add("WARN", "Shop installed but ShopService.Start is not called outside the system folder")
    for name, call in (("DailyRewards", r"DailyRewards"), ("Analytics", r"Analytics"), ("Admin", r"Admin")):
        if present[name] and not where(files, call, skip=("/%s/" % name,)):
            add("WARN", "%s installed but never required from game code" % name)
    # server code in client containers
    leaks = [p for p in files if re.search(r"(^|/)(StarterGui|StarterPlayer|ReplicatedStorage|client|shared)/", p)
             and re.search(r"(DataStoreService|ProcessReceipt|UserOwnsGamePassAsync)", files[p])]
    if leaks:
        add("FAIL", "server-only APIs referenced in client-visible folders: " + ", ".join(leaks[:6]))
    # secrets
    sec = where(files, r"(api[_-]?key|secret|token)\s*=\s*[\"'][A-Za-z0-9_\-]{16,}[\"']", flags=re.I)
    if sec:
        add("FAIL", "possible hard-coded secret at " + ", ".join(sec[:4]))
    return out


def report(items, as_json):
    if as_json:
        print(json.dumps(items, indent=2))
    else:
        for i in items:
            print("%-5s %s" % (i["level"], i["msg"]))
        fails = sum(1 for i in items if i["level"] == "FAIL")
        warns = sum(1 for i in items if i["level"] == "WARN")
        print("summary: %d FAIL, %d WARN (static only, not a live test)" % (fails, warns))
    return 1 if any(i["level"] == "FAIL" for i in items) else 0


def selftest():
    with tempfile.TemporaryDirectory() as d:
        def w(rel, text):
            p = os.path.join(d, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w").write(text)
        w("src/server/Systems/PlayerData/PlayerData.luau", "return {}\n")
        w("src/server/Systems/Shop/Shop.luau", "MarketplaceService.ProcessReceipt = function() end\n")
        w("src/server/Main.server.luau", "local x = DS:SetAsync('k', 1)\nMarketplaceService.ProcessReceipt = function() end\n")
        w("src/shared/Bad.luau", "local d = game:GetService('DataStoreService')\n")
        w("src/server/Cfg.luau", "local apiKey = 'abcdefghijklmnop1234'\n")
        res = check(d)
        msgs = " | ".join(i["level"] + " " + i["msg"] for i in res)
        assert "assigned 2 times" in msgs, msgs
        assert "BindToClose" in msgs and "PlayerRemoving" in msgs, msgs
        assert "client-visible" in msgs, msgs
        assert "hard-coded secret" in msgs, msgs
        assert "direct DataStore" in msgs, msgs
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "src/server/Systems/PlayerData"))
        open(os.path.join(d, "src/server/Systems/PlayerData/PlayerData.luau"), "w").write("return {}\n")
        open(os.path.join(d, "src/server/Main.server.luau"), "w").write(
            "game:BindToClose(function() end)\nPlayers.PlayerRemoving:Connect(function() end)\nlocal s = PlayerData:LoadAsync('1')\n")
        res = check(d)
        assert not any(i["level"] == "FAIL" for i in res), res
    with tempfile.TemporaryDirectory() as d:
        assert check(d)[0]["level"] == "FAIL"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    return report(check(args[0]), "--json" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
