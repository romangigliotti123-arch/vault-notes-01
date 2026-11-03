#!/usr/bin/env python3
"""analytics-pull - read-only fetch of a game's numbers from the Roblox Open Cloud Analytics Query API (beta). Stdlib only.

  python analytics-pull.py --universe <UniverseId> [--metric DailyActiveUsers --metric ForwardD1Retention ...] [--days 14]
                           [--granularity OneDay] [--breakdown Platform] [--json] [--dry-run] [--base-url URL]

Your API key stays on YOUR machine: it is read from the environment variable ROBLOX_ANALYTICS_API_KEY, or from the file
~/.config/roblox/analytics-api-key (one line). It is sent only as the x-api-key header to apis.roblox.com, never printed,
never written anywhere, and the tool refuses a key file that sits inside a vault/Games folder. Create the key in the Creator
Dashboard (Open Cloud > API Keys): add the experience under Access Permissions and grant `universe.analytics:read`
(system universe-analytics). Docs: create.roblox.com/docs/cloud/guides/analytics (checked 2026-11-01; the API is in beta, so
metric names and access can change; the page "Supported metrics" lists the allowed names and breakdowns).

Known metric names from the docs: DailyActiveUsers, DailyRevenue, ForwardD1Retention, PayingUsersCVR (and Funnel metrics).
Anything else: pass --metric <Name> exactly as the Supported-metrics page spells it. A rejected name is reported, never guessed.
Exit: 0 ok, 1 request/API error, 2 no key / bad input.
"""
import argparse, datetime, json, os, sys, time, urllib.error, urllib.request

BASE = "https://apis.roblox.com/analytics-query-api"
DEFAULT_METRICS = ["DailyActiveUsers", "ForwardD1Retention", "DailyRevenue", "PayingUsersCVR"]
KEY_FILE = os.path.join(os.path.expanduser("~"), ".config", "roblox", "analytics-api-key")


def load_key():
    k = os.environ.get("ROBLOX_ANALYTICS_API_KEY", "").strip()
    if k:
        return k
    if os.path.isfile(KEY_FILE):
        real = os.path.realpath(KEY_FILE).replace("\\", "/").lower()
        if "/games/" in real or "vault" in real:
            sys.exit("analytics-pull: refusing a key file inside a vault/Games folder (%s). Keep it outside the vault." % KEY_FILE)
        with open(KEY_FILE, encoding="utf-8") as f:
            return f.read().strip()
    return ""


def call(url, key, body=None, retries=3):
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, method="POST" if body is not None else "GET",
                                     headers={"x-api-key": key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors="replace")[:500]
            if e.code in (500, 503, 504) and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return e.code, {"error": txt}
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return 0, {"error": str(e)}
    return 0, {"error": "unreachable"}


def query(base, uid, key, metric, start, end, gran, breakdown):
    body = {"metric": metric, "granularity": gran, "startTime": start, "endTime": end}
    if breakdown:
        body["breakdown"] = breakdown
    code, js = call("%s/v1/universes/%s/metrics" % (base, uid), key, body)
    waited = 0
    while code in (200, 202) and js.get("done") is False and waited < 120:
        time.sleep(3)
        waited += 3
        code, js = call("%s/%s" % (base, js["path"].lstrip("/")), key)
    return code, js


def main():
    ap = argparse.ArgumentParser(description="pull numbers from the Roblox Open Cloud Analytics Query API")
    ap.add_argument("--universe", required=True)
    ap.add_argument("--metric", action="append")
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--granularity", default="OneDay")
    ap.add_argument("--breakdown", action="append")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--base-url", default=BASE)
    a = ap.parse_args()
    if not a.universe.isdigit():
        sys.exit("analytics-pull: --universe must be the numeric Universe ID (Creator Dashboard > the experience > Overview)")
    end = datetime.datetime.now(datetime.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - datetime.timedelta(days=a.days)
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    metrics = a.metric or DEFAULT_METRICS
    if a.dry_run:
        for m in metrics:
            print("POST %s/v1/universes/%s/metrics  x-api-key: <hidden>\n  %s" % (a.base_url, a.universe, json.dumps(
                {"metric": m, "granularity": a.granularity, "startTime": start.strftime(fmt), "endTime": end.strftime(fmt)})))
        return 0
    key = load_key()
    if not key:
        print("analytics-pull: no API key. Set ROBLOX_ANALYTICS_API_KEY or put it in %s (see --help). Without it, paste the Creator Dashboard numbers instead." % KEY_FILE, file=sys.stderr)
        return 2
    out, rc = {}, 0
    for m in metrics:
        code, js = query(a.base_url, a.universe, key, m, start.strftime(fmt), end.strftime(fmt), a.granularity, a.breakdown)
        if code != 200 or "error" in js and "response" not in js:
            rc = 1
            out[m] = {"error": ("HTTP %s: %s" % (code, str(js.get("error", js))[:300])).replace(key, "<key>")}
            continue
        series = js.get("response", {}).get("values", [])
        out[m] = [{"breakdowns": s.get("breakdowns", []), "points": [(p.get("time", "")[:10], p.get("value")) for p in s.get("dataPoints", [])]} for s in series]
    if a.json:
        print(json.dumps(out, indent=1))
        return rc
    print("Universe %s, %s to %s (UTC), granularity %s. Source: Open Cloud Analytics Query API (beta)." % (a.universe, start.date(), end.date(), a.granularity))
    for m, v in out.items():
        print("\n%s" % m)
        if isinstance(v, dict):
            print("  ERROR %s" % v["error"])
            continue
        for s in v:
            label = ",".join("%s=%s" % (b.get("dimension"), b.get("value")) for b in s["breakdowns"]) or "all"
            pts = s["points"]
            vals = [p[1] for p in pts if isinstance(p[1], (int, float))]
            avg = sum(vals) / len(vals) if vals else None
            print("  [%s] %d points%s; last: %s" % (label, len(pts), (", mean %.4g" % avg) if avg is not None else "", ", ".join("%s=%s" % p for p in pts[-3:])))
    return rc


if __name__ == "__main__":
    sys.exit(main())
