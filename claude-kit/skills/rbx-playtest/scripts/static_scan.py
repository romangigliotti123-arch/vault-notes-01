#!/usr/bin/env python3
"""static_scan.py - deterministic Luau red-flag scan for rbx-playtest. Stdlib only, read-only.

  python static_scan.py <project-dir-or-file> [--json]
  python static_scan.py <project-dir-or-file> --gate [--scorer critic|builder] [--game ID] [--write GAME_FOLDER]

Finds suspicious patterns with file:line (heuristics, not proof: every hit needs a human/Claude look). Severity: S1 blocker, S2 major, S3 minor, S4 note.
Checks: loadstring; wait/spawn/delay (deprecated); non-zero rbxassetid (should be 0 until set in Creator Hub); RemoteEvent/Function server handlers with
no type/range check in the next lines; DataStore calls without pcall nearby; no BindToClose / Release anywhere when DataStore is used; ProcessReceipt without
a recorded-receipt check; client-trusted currency (FireServer with amount/coins/cash args); HttpService calls; Instance.new("Script"); infinite loops without
task.wait; Humanoid property edits from LocalScripts about health/walkspeed that look like cheats; very long files (maintainability note).
Exit 0 always (the report is the product); prints a table or JSON.

--gate turns the findings into a SCORED security gate: SEC1 client-trusted remotes, SEC2 hardcoded secrets and webhooks, SEC3 server-only code or data in
client-visible folders (Rojo tree, else folder names), SEC4 DataStore and receipt safety, SEC5 backdoor patterns. 0-10 per check (S1 -4, S2 -2, S3 -1), pass mark 7,
JSON in the format of comment_scan.py. --write GAME_FOLDER saves GAME_FOLDER/security-scan/gate.json, where rbx-bench finds it. A low score never blocks;
only "code gates not run" caps the critic (rbx-critic/scripts/code_gates.py). Every finding is a lead for the skillpack exploit-audit, not proof.
"""
import json
import os
import re
import sys
import time

EXT = (".lua", ".luau")
RULES = [
    ("S1", r"\bloadstring\s*\(", "loadstring: remote code execution risk"),
    ("S3", r"(?<![\w.:])wait\s*\(", "wait(): use task.wait()"),
    ("S3", r"(?<![\w.:])spawn\s*\(", "spawn(): use task.spawn()"),
    ("S3", r"(?<![\w.:])delay\s*\(", "delay(): use task.delay()"),
    ("S2", r"rbxassetid://\s*[1-9]\d*", "non-zero asset id: must be an id the owner set in Creator Hub, never invented"),
    ("S3", r"HttpService\s*[:.]", "HttpService use: needs allow-list and no secrets in code"),
    ("S3", r"Instance\.new\(\s*[\"']Script[\"']", "runtime Script creation"),
    ("S2", r":FireServer\([^)]*\b(amount|coins|cash|gems|money|reward|price|damage)\b", "client sends a value the server should compute"),
]
SECRETS = [
    ("S1", r"discord(app)?\.com/api/webhooks/\d+/[\w-]+", "Discord webhook URL in code", True),
    ("S1", r"hooks\.slack\.com/services/T\w+/B\w+/\w+", "Slack webhook URL in code", True),
    ("S1", r"AK​IA[0-9A-Z]{16}|ghp​_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{20,}", "API key literal", True),
    ("S1", r"[\"']x-api-key[\"']\]?\s*[=:]\s*[\"'][A-Za-z0-9+/=_-]{20,}[\"']", "Open Cloud / API key literal in a header", False),
    ("S1", r"[\"']?Authorization[\"']?\]?\s*[=:]\s*[\"'](Bearer\s+|Basic\s+)?[A-Za-z0-9._+/=-]{20,}[\"']", "Authorization header with a literal credential", False),
    ("S2", r"(?i)\b(api[_-]?key|secret|token|password|webhook)\w*\s*=\s*[\"'](?=[A-Za-z0-9+/=_-]*\d)(?=[A-Za-z0-9+/=_-]*[A-Za-z])[A-Za-z0-9+/=_-]{20,}[\"']",
     "credential-looking string assigned in code", False),
]
BACKDOOR = [
    ("S1", r"\brequire\s*\(\s*\d{5,}\s*\)", "require(<asset id>): loads a remote module"),
    ("S2", r"\b(getfenv|setfenv)\s*\(", "getfenv/setfenv: environment tampering, typical of backdoors"),
    ("S2", r"InsertService\s*[:.]\s*LoadAsset(Version)?\s*\(", "InsertService:LoadAsset pulls an unreviewed model with scripts"),
    ("S2", r"(\\\d{2,3}){12,}", "long numeric escape string (obfuscated payload)"),
    ("S2", r"string\.char\s*\((\s*\d+\s*,){12,}", "string.char built payload (obfuscation)"),
]
SERVER_ONLY = re.compile(r"DataStoreService|ProfileStore|ProfileService|ProcessReceipt|ServerStorage|ServerScriptService|MessagingService"
                         r"|HttpService\s*[:.]\s*(Post|Get|Request)Async|\bAdmin(Ids|List|s)\b\s*=\s*\{")
CLIENT_NAMES = {"shared", "client", "replicatedstorage", "starterplayer", "startergui", "starterplayerscripts", "replicatedfirst", "starterpack"}
CLIENT_SERVICES = {"ReplicatedStorage", "StarterGui", "StarterPlayer", "StarterPack", "ReplicatedFirst", "Workspace"}
FIXES = {
    "SEC1": "validate type, range and ownership on the server; compute amounts server-side, never trust a client value (rbx-remote-sec)",
    "SEC2": "remove the secret from code and rotate it; keep keys and webhooks out of the place (a server-side proxy, never client-visible)",
    "SEC3": "move server-only code and data to ServerScriptService or ServerStorage; clients only get remotes",
    "SEC4": "wrap DataStore calls in pcall with retry, release on leave, BindToClose, idempotent receipts (rbx-datastore)",
    "SEC5": "delete the pattern; never require asset ids or run loadstring; audit the model it came from",
}
SERVER_HANDLER = re.compile(r"(OnServerEvent|OnServerInvoke)\s*(:Connect\s*\(|=)\s*function\s*\(([^)]*)\)")


def files(root, skip_tests=False):
    if os.path.isfile(root):
        yield root
        return
    skip = (".git", "Packages", "node_modules", "Vendor", "vendor") + (("tests", "test", "spec") if skip_tests else ())
    for d, dirs, fs in os.walk(root):
        dirs[:] = [x for x in dirs if x not in skip]
        for f in fs:
            if f.endswith(EXT) and not f.endswith(".d.luau"):
                yield os.path.join(d, f)


def scan(root, skip_tests=False):
    hits = []
    uses_ds = uses_bind = uses_receipt = receipt_guard = False
    for p in files(root, skip_tests):
        try:
            lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        rel = os.path.relpath(p, root if os.path.isdir(root) else os.path.dirname(root))
        text = "\n".join(lines)
        if re.search(r"GetDataStore|DataStoreService|ProfileStore|ProfileService", text):
            uses_ds = True
        if re.search(r"BindToClose", text):
            uses_bind = True
        if re.search(r"ProcessReceipt", text):
            uses_receipt = True
        if re.search(r"PurchaseId|receiptInfo\.PurchaseId|processed", text, re.I):
            receipt_guard = True
        if len(lines) > 600:
            hits.append(("S4", rel, 1, "file has %d lines: consider splitting" % len(lines)))
        for i, ln in enumerate(lines, 1):
            code = ln.split("--")[0]
            for sev, rx, msg in RULES:
                if re.search(rx, code):
                    hits.append((sev, rel, i, msg))
            m = SERVER_HANDLER.search(code)
            if m:
                window = "\n".join(lines[i - 1:i + 8])
                if not re.search(r"typeof\s*\(|type\s*\(|math\.clamp|assert\s*\(|tonumber\s*\(|:IsA\(|isfinite|~=\s*nil|== nil|\.Parent", window):
                    hits.append(("S1", rel, i, "server remote handler with no visible type/range/ownership check in the next 8 lines"))
            if re.search(r"(GetAsync|SetAsync|UpdateAsync|IncrementAsync|RemoveAsync)\s*\(", code):
                window = "\n".join(lines[max(0, i - 4):i + 2])
                if "pcall" not in window:
                    hits.append(("S2", rel, i, "DataStore call without pcall nearby"))
            if re.match(r"\s*while\s+true\s+do\s*$", code):
                window = "\n".join(lines[i - 1:i + 10])
                if not re.search(r"task\.wait|\.Heartbeat:Wait|:Wait\(\)|RenderStepped:Wait|Stepped:Wait", window):
                    hits.append(("S1", rel, i, "while true do loop with no yield in the next 10 lines (freezes the server)"))
    if uses_ds and not uses_bind:
        hits.append(("S1", "(project)", 0, "DataStore used but no BindToClose anywhere: saves can be lost on shutdown"))
    if uses_receipt and not receipt_guard:
        hits.append(("S1", "(project)", 0, "ProcessReceipt without a visible PurchaseId/processed check: double grants possible"))
    order = {"S1": 0, "S2": 1, "S3": 2, "S4": 3}
    hits.sort(key=lambda h: (order[h[0]], h[1], h[2]))
    return hits


def client_dirs(root):
    cur = os.path.abspath(root if os.path.isdir(root) else os.path.dirname(root))
    for _ in range(4):
        pj = os.path.join(cur, "default.project.json")
        if os.path.isfile(pj):
            try:
                tree = json.load(open(pj, encoding="utf-8-sig")).get("tree", {})
            except (OSError, ValueError):
                return None
            out = []

            def walk(node, client):
                if not isinstance(node, dict):
                    return
                for k, v in node.items():
                    if k == "$path" and client and isinstance(v, str):
                        out.append(os.path.normpath(os.path.join(cur, v)))
                    elif not k.startswith("$"):
                        walk(v, client or k in CLIENT_SERVICES)
            walk(tree, False)
            return out
        cur = os.path.dirname(cur)
    return None


def under(path, dirs):
    p = os.path.normpath(os.path.abspath(path))
    return any(p == d or p.startswith(d + os.sep) for d in (os.path.normpath(os.path.abspath(x)) for x in dirs))


def gate_hits(root):
    hits = []
    dirs = client_dirs(root)
    top = root if os.path.isdir(root) else os.path.dirname(root)
    for p in files(root, True):
        try:
            lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        rel = os.path.relpath(p, top)
        parts = {x.lower() for x in rel.replace("\\", "/").split("/")[:-1]}
        in_client = under(p, dirs) if dirs is not None else bool(parts & CLIENT_NAMES)
        if re.search(r"\.client\.luau?$", p):
            in_client = True
        for i, ln in enumerate(lines, 1):
            code = ln.split("--")[0]
            for sev, rx, msg, whole_line in SECRETS:
                if re.search(rx, ln if whole_line else code):
                    hits.append(("SEC2", sev, rel, i, msg))
            for sev, rx, msg in BACKDOOR:
                if re.search(rx, code):
                    hits.append(("SEC5", sev, rel, i, msg))
            if in_client and SERVER_ONLY.search(code):
                hits.append(("SEC3", "S1", rel, i, "server-only API or data in a client-visible folder (players can read it)"))
    return hits


def gate(root, game=None, scorer="critic"):
    rows = []
    for sev, f, ln, msg in scan(root, True):
        if "remote handler" in msg or "client sends" in msg:
            rows.append(("SEC1", sev, f, ln, msg))
        elif "DataStore" in msg or "ProcessReceipt" in msg:
            rows.append(("SEC4", sev, f, ln, msg))
        elif "loadstring" in msg:
            rows.append(("SEC5", sev, f, ln, msg))
    rows += gate_hits(root)
    cost = {"S1": 4.0, "S2": 2.0, "S3": 1.0, "S4": 0.0}
    checks, failing, reasons = {}, [], []
    for cid in ("SEC1", "SEC2", "SEC3", "SEC4", "SEC5"):
        mine = [r for r in rows if r[0] == cid]
        checks[cid] = max(0.0, round(10.0 - sum(cost[r[1]] for r in mine), 1))
        if mine:
            reasons.append("%s %.1f: %d finding(s)" % (cid, checks[cid], len(mine)))
        for r in mine[:6]:
            failing.append(dict(path="%s:%s" % (r[2], r[3]), check=cid, severity=r[1], found=r[4], fix=FIXES[cid]))
    return dict(kind="security-scan", scorer=scorer, game=game, severity="high", pass_min=7.0, scripted=True,
                result="pass" if min(checks.values()) >= 7.0 else "fail", checks=checks, reasons=reasons, failing=failing[:30],
                counts=dict(findings=len(rows), s1=sum(1 for r in rows if r[1] == "S1"), s2=sum(1 for r in rows if r[1] == "S2"),
                            s3=sum(1 for r in rows if r[1] == "S3")),
                suggested_fix="confirm or dismiss each finding, then fix; deep pass: skillpack exploit-audit" if rows else "none",
                time=time.strftime("%Y-%m-%dT%H:%M:%S"))


def write_gate(rec, folder):
    d = os.path.join(folder, "security-scan")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "gate.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rec, fh, indent=1)
        fh.write("\n")


def opt(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


if __name__ == "__main__":
    args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and sys.argv[i - 1] not in ("--scorer", "--game", "--write")]
    if not args or not os.path.exists(args[0]):
        print("usage: static_scan.py <project-dir-or-file> [--json | --gate [--scorer critic|builder] [--game ID] [--write GAME_FOLDER]]", file=sys.stderr)
        sys.exit(2)
    if "--gate" in sys.argv:
        rec = gate(args[0], opt("--game"), opt("--scorer", "critic"))
        if opt("--write"):
            write_gate(rec, opt("--write"))
        print(json.dumps(rec, indent=1))
        sys.exit(0)
    h = scan(args[0])
    if "--json" in sys.argv:
        print(json.dumps([dict(zip(("severity", "file", "line", "finding"), x)) for x in h], indent=1))
    else:
        print("| sev | file:line | finding |\n|---|---|---|")
        for sev, f, ln, msg in h[:200]:
            print("| %s | %s:%s | %s |" % (sev, f, ln, msg))
        c = {s: sum(1 for x in h if x[0] == s) for s in ("S1", "S2", "S3", "S4")}
        print("\nstatic_scan: %d hits (S1 %d, S2 %d, S3 %d, S4 %d); heuristics only, review each" % (len(h), c["S1"], c["S2"], c["S3"], c["S4"]))
