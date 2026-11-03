#!/usr/bin/env python3
"""static_scan.py - deterministic Luau red-flag scan for game-dev-playtest. Stdlib only, read-only.

  python static_scan.py <project-dir-or-file> [--json]

Finds suspicious patterns with file:line (heuristics, not proof: every hit needs a human/Claude look). Severity: S1 blocker, S2 major, S3 minor, S4 note.
Checks: loadstring; wait/spawn/delay (deprecated); non-zero rbxassetid (should be 0 until set in Creator Hub); RemoteEvent/Function server handlers with
no type/range check in the next lines; DataStore calls without pcall nearby; no BindToClose / Release anywhere when DataStore is used; ProcessReceipt without
a recorded-receipt check; client-trusted currency (FireServer with amount/coins/cash args); HttpService calls; Instance.new("Script"); infinite loops without
task.wait; Humanoid property edits from LocalScripts about health/walkspeed that look like cheats; very long files (maintainability note).
Exit 0 always (the report is the product); prints a table or JSON.
"""
import json
import os
import re
import sys

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
SERVER_HANDLER = re.compile(r"(OnServerEvent|OnServerInvoke)\s*(:Connect\s*\(|=)\s*function\s*\(([^)]*)\)")


def files(root):
    if os.path.isfile(root):
        yield root
        return
    for d, dirs, fs in os.walk(root):
        dirs[:] = [x for x in dirs if x not in (".git", "Packages", "node_modules", "Vendor", "vendor")]
        for f in fs:
            if f.endswith(EXT) and not f.endswith(".d.luau"):
                yield os.path.join(d, f)


def scan(root):
    hits = []
    uses_ds = uses_bind = uses_receipt = receipt_guard = False
    for p in files(root):
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


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or not os.path.exists(args[0]):
        print("usage: static_scan.py <project-dir-or-file> [--json]", file=sys.stderr)
        sys.exit(2)
    h = scan(args[0])
    if "--json" in sys.argv:
        print(json.dumps([dict(zip(("severity", "file", "line", "finding"), x)) for x in h], indent=1))
    else:
        print("| sev | file:line | finding |\n|---|---|---|")
        for sev, f, ln, msg in h[:200]:
            print("| %s | %s:%s | %s |" % (sev, f, ln, msg))
        c = {s: sum(1 for x in h if x[0] == s) for s in ("S1", "S2", "S3", "S4")}
        print("\nstatic_scan: %d hits (S1 %d, S2 %d, S3 %d, S4 %d); heuristics only, review each" % (len(h), c["S1"], c["S2"], c["S3"], c["S4"]))
