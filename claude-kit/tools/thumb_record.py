#!/usr/bin/env python3
"""thumb_record.py: your local ledger of thumbnail variant results, and the tally of which features win per genre (stdlib only, no network).

One JSON line per variant per test, in <claude config dir>/claude-kit/state/thumbnails/results.jsonl (override $VAULT_THUMB_DIR). It is yours: an update never touches it. Record what Creator Hub shows
for each active thumbnail after the test ran (protocol: [cold:rbx-thumbnail/protocol.md]); nothing is read from Roblox and nothing leaves the machine unless you turn sharing on.

  thumb_record.py add --test T --genre G --variant V [--control] [--asset thumbnail|icon|ad] --impressions N --qualified-plays N [--qptr F] [--ctr F] [--avg-playtime MIN]
        --date-start YYYY-MM-DD --date-end YYYY-MM-DD [--qptr-first-half F --qptr-second-half F] [--context update|event|none] [--segment S] [--rubric-score N] [--gates-ok yes|no]
        [--feature key=value ...] [--varies key ...] [--verdict winner|loser|inconclusive] [--game NAME] [--notes T]      (same test + variant replaces the line)
  thumb_record.py decide --test T [--write]    verdicts by the decision rule below, against the test's control
  thumb_record.py list [--genre G] [--test T]
  thumb_record.py summary [--genre G] [--json]  per genre, which features win; "not enough data" until the minimum counts are reached
  thumb_record.py share on|off|status | queue [--quiet]    opt-in: one redacted note per genre (feature tallies only, no game names) for the normal `learn.py flush`

Features: hero hero_size_pct emotion gaze_target palette value_contrast text text_words element_count action_pose style twist. Fractions are 0-1 (4.5% = 0.045).
ASSUMPTIONS (the vault's own, not Roblox's; tune them from your data): a thumbnail with under 1000 impressions is ignored; winner = at least 10% higher qPTR than the control over at least 7 days,
ahead in both halves of the run, average playtime per qualified play not worse; loser = the mirror (10% lower, behind in both halves); anything else = inconclusive.
Summary minimums: 10 decided variants per genre, 3 decided variants per feature value. Roblox allocates impressions unevenly (adaptive), so impressions are not demand.
"""
import argparse
import collections
import datetime
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit_state
import learn as L
import hiccup as H

MIN_IMPRESSIONS, MIN_DAYS, WIN_REL = 1000, 7, 0.10
MIN_DECIDED_GENRE, MIN_DECIDED_FEATURE, REPLACE_WEIGHTS_AT = 10, 3, 20
MAX_RECORDS = 5000
FEATURE_KEYS = ("hero", "hero_size_pct", "emotion", "gaze_target", "palette", "value_contrast", "text", "text_words", "element_count", "action_pose", "style", "twist")
INT_FEATURES = ("hero_size_pct", "text_words", "element_count")
FREE_TEXT = ("hero", "gaze_target", "style", "twist", "text")
GENRE_RX = re.compile(r"^[a-z0-9][a-z0-9-]{1,29}$")
ID_RX = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ._-]{0,39}$")
DATE_RX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VERDICTS = ("winner", "loser", "inconclusive")


def tdir():
    return os.environ.get("VAULT_THUMB_DIR") or kit_state.path("thumbnails", L.config_dir())


def ledger_path():
    return os.path.join(tdir(), "results.jsonl")


def load():
    out = []
    try:
        with open(ledger_path(), encoding="utf-8") as f:
            for ln in f:
                try:
                    r = json.loads(ln)
                except ValueError:
                    continue
                if isinstance(r, dict) and r.get("test_id") and r.get("variant_id"):
                    out.append(r)
    except OSError:
        pass
    return out


def save(rows):
    os.makedirs(tdir(), exist_ok=True)
    p = ledger_path()
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        for r in rows[-MAX_RECORDS:]:
            f.write(json.dumps(r, ensure_ascii=True, sort_keys=True) + "\n")
    os.replace(tmp, p)


def days_between(a, b):
    try:
        return (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days
    except ValueError:
        return 0


def frac(name, v):
    if v is None:
        return None
    if not 0 <= v <= 1:
        raise ValueError("%s is a fraction between 0 and 1 (4.5%% = 0.045), got %s" % (name, v))
    return float(v)


def parse_features(pairs):
    f = {}
    for p in pairs or []:
        if "=" not in p:
            raise ValueError("--feature needs key=value, got %r" % p)
        k, v = p.split("=", 1)
        k, v = k.strip(), v.strip()
        if k not in FEATURE_KEYS:
            raise ValueError("unknown feature %r (known: %s)" % (k, " ".join(FEATURE_KEYS)))
        if k in INT_FEATURES:
            if not v.isdigit():
                raise ValueError("feature %s needs a whole number" % k)
            f[k] = int(v)
        elif k == "action_pose":
            if v.lower() not in ("true", "false", "yes", "no"):
                raise ValueError("feature action_pose needs yes or no")
            f[k] = v.lower() in ("true", "yes")
        else:
            f[k] = " ".join(v.lower().split())[:60]
    return f


def make_record(a):
    genre = re.sub(r"[^a-z0-9]+", "-", (a.genre or "").lower()).strip("-")
    if not GENRE_RX.match(genre):
        raise ValueError("--genre must be a short word like obby, tycoon, simulator (letters, digits, hyphens)")
    for nm, v in (("--test", a.test), ("--variant", a.variant)):
        if not v or not ID_RX.match(v):
            raise ValueError("%s needs a short id (letters, digits, space . _ -)" % nm)
    for nm, v in (("--date-start", a.date_start), ("--date-end", a.date_end)):
        if not v or not DATE_RX.match(v):
            raise ValueError("%s must be YYYY-MM-DD" % nm)
    for nm, v in (("--impressions", a.impressions), ("--qualified-plays", a.qualified_plays)):
        if v is None or v < 0:
            raise ValueError("%s must be a whole number, 0 or more" % nm)
    if a.qualified_plays > a.impressions:
        raise ValueError("qualified plays cannot exceed impressions")
    days = days_between(a.date_start, a.date_end) + 1
    if days < 1:
        raise ValueError("--date-end is before --date-start")
    qptr = frac("--qptr", a.qptr)
    if qptr is None and a.impressions:
        qptr = round(a.qualified_plays / float(a.impressions), 6)
    feats = parse_features(a.feature)
    varies = []
    for k in a.varies or []:
        if k not in FEATURE_KEYS:
            raise ValueError("--varies %r is not a feature key" % k)
        varies.append(k)
    if a.verdict and a.verdict not in VERDICTS:
        raise ValueError("--verdict must be winner, loser or inconclusive")
    return {"test_id": a.test, "game": (a.game or "")[:60], "genre": genre, "asset": a.asset, "variant_id": a.variant, "is_control": bool(a.control), "features": feats, "varies": varies,
            "rubric_score": a.rubric_score, "rubric_gates_ok": None if a.gates_ok is None else a.gates_ok == "yes", "impressions": a.impressions, "qualified_plays": a.qualified_plays,
            "qptr": qptr, "ctr": frac("--ctr", a.ctr), "avg_playtime_min": a.avg_playtime, "qptr_first_half": frac("--qptr-first-half", a.qptr_first_half),
            "qptr_second_half": frac("--qptr-second-half", a.qptr_second_half), "winning_segment": (a.segment or "")[:40], "date_start": a.date_start, "date_end": a.date_end, "days": days,
            "context": a.context, "verdict": a.verdict or "inconclusive", "verdict_by": "user" if a.verdict else "none", "notes": (a.notes or "")[:300]}


def cmd_add(a):
    try:
        r = make_record(a)
    except ValueError as e:
        print("thumb_record: %s" % e, file=sys.stderr)
        return 2
    rows = [x for x in load() if not (x["test_id"] == r["test_id"] and x["variant_id"] == r["variant_id"])]
    rows.append(r)
    save(rows)
    print("recorded %s / %s (%s): impressions %d, qPTR %s, %d day(s), verdict %s" % (r["test_id"], r["variant_id"], r["genre"], r["impressions"], "n/a" if r["qptr"] is None else "%.4f" % r["qptr"], r["days"], r["verdict"]))
    return 0


def judge(v, c):
    """-> (verdict, reason) for a variant against the control by the assumption rule"""
    if v["impressions"] < MIN_IMPRESSIONS or c["impressions"] < MIN_IMPRESSIONS:
        return "inconclusive", "under %d impressions (%d vs control %d)" % (MIN_IMPRESSIONS, v["impressions"], c["impressions"])
    if v["days"] < MIN_DAYS or c["days"] < MIN_DAYS:
        return "inconclusive", "under %d days (%d)" % (MIN_DAYS, min(v["days"], c["days"]))
    if v["qptr"] is None or c["qptr"] is None or c["qptr"] <= 0:
        return "inconclusive", "qPTR missing or zero for the control"
    halves = [x.get(k) for x in (v, c) for k in ("qptr_first_half", "qptr_second_half")]
    if None in halves:
        return "inconclusive", "first/second-half qPTR not recorded for both (--qptr-first-half, --qptr-second-half): persistence unchecked"
    rel = v["qptr"] / c["qptr"] - 1
    ahead = v["qptr_first_half"] > c["qptr_first_half"] and v["qptr_second_half"] > c["qptr_second_half"]
    behind = v["qptr_first_half"] < c["qptr_first_half"] and v["qptr_second_half"] < c["qptr_second_half"]
    if rel >= WIN_REL and ahead:
        if v["avg_playtime_min"] is None or c["avg_playtime_min"] is None:
            return "inconclusive", "average playtime per qualified play missing: cannot rule out bait"
        if v["avg_playtime_min"] < c["avg_playtime_min"]:
            return "inconclusive", "qPTR %+.1f%% but average playtime is worse (%.2f vs %.2f min)" % (rel * 100, v["avg_playtime_min"], c["avg_playtime_min"])
        return "winner", "qPTR %+.1f%% vs control, ahead in both halves, playtime not worse" % (rel * 100)
    if rel <= -WIN_REL and behind:
        return "loser", "qPTR %+.1f%% vs control, behind in both halves" % (rel * 100)
    return "inconclusive", "qPTR %+.1f%% vs control (needs +/-%d%% and the same direction in both halves)" % (rel * 100, WIN_REL * 100)


def cmd_decide(a):
    rows = load()
    mine = [r for r in rows if r["test_id"] == a.test]
    ctl = [r for r in mine if r.get("is_control")]
    if not mine:
        print("thumb_record: no records for test %r" % a.test, file=sys.stderr)
        return 2
    if len(ctl) != 1:
        print("thumb_record: test %r needs exactly one control record (has %d)" % (a.test, len(ctl)), file=sys.stderr)
        return 2
    out = []
    for r in mine:
        if r is ctl[0]:
            continue
        v, why = judge(r, ctl[0])
        out.append((r, v, why))
        print("  %-10s %-12s %s" % (r["variant_id"], v, why))
        if a.write:
            r["verdict"], r["verdict_by"] = v, "rule"
    if a.write:
        save(rows)
        print("verdicts written (assumption rule: %d+ impressions, %d+ days, +/-%d%%, both halves)" % (MIN_IMPRESSIONS, MIN_DAYS, WIN_REL * 100))
    return 0


def cmd_list(a):
    rows = [r for r in load() if (not a.genre or r["genre"] == a.genre) and (not a.test or r["test_id"] == a.test)]
    if not rows:
        print("no records yet (thumb_record.py add ...)")
        return 0
    for r in sorted(rows, key=lambda x: (x["genre"], x["test_id"], x["variant_id"])):
        print("%-12s %-14s %-8s %s imp %-7d qPTR %-8s %2dd %s%s" % (r["genre"], r["test_id"][:14], r["variant_id"][:8], "C" if r["is_control"] else " ", r["impressions"],
                                                                  "n/a" if r["qptr"] is None else "%.4f" % r["qptr"], r["days"], r["verdict"], " (rule)" if r.get("verdict_by") == "rule" else ""))
    return 0


def bucket(k, v):
    if k == "hero_size_pct":
        return "hero_size", "under 35%" if v < 35 else "35-50%" if v <= 50 else "over 50%"
    if k == "text_words":
        return "text_words", "0" if v == 0 else "1-3" if v <= 3 else "4+"
    if k == "element_count":
        return "element_count", "1-2" if v <= 2 else "3+"
    if k == "action_pose":
        return k, "yes" if v else "no"
    return k, str(v)


def tally(rows):
    """decided non-control variants -> {(feature, value): [wins, losses]}; only the features a variant says it varied when it says so"""
    t = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        if r.get("is_control") or r.get("verdict") not in ("winner", "loser"):
            continue
        keys = r.get("varies") or [k for k in r.get("features", {}) if k not in FREE_TEXT]
        for k in keys:
            if k in r.get("features", {}):
                kk, vv = bucket(k, r["features"][k])
                t[(kk, vv)][0 if r["verdict"] == "winner" else 1] += 1
    return t


def summarise(rows, genre=None):
    by = collections.defaultdict(list)
    for r in rows:
        if not genre or r["genre"] == genre:
            by[r["genre"]].append(r)
    out = {}
    for g, rs in sorted(by.items()):
        decided = [r for r in rs if not r.get("is_control") and r.get("verdict") in ("winner", "loser")]
        e = {"records": len(rs), "tests": len({r["test_id"] for r in rs}), "decided": len(decided), "enough": len(decided) >= MIN_DECIDED_GENRE, "features": []}
        if e["enough"]:
            for (k, v), (w, l) in tally(rs).items():
                if w + l >= MIN_DECIDED_FEATURE:
                    e["features"].append({"feature": k, "value": v, "wins": w, "losses": l, "win_rate": round(w / float(w + l), 2)})
            e["features"].sort(key=lambda x: (-x["win_rate"], -(x["wins"] + x["losses"]), x["feature"], x["value"]))
        out[g] = e
    return out


def cmd_summary(a):
    s = summarise(load(), a.genre)
    if a.json:
        print(json.dumps(s, indent=1))
        return 0
    if not s:
        print("not enough data: no records%s yet. Run a thumbnail test (protocol.md) and record each variant with thumb_record.py add." % (" for genre " + a.genre if a.genre else ""))
        return 0
    for g, e in s.items():
        if not e["enough"]:
            print("%s: not enough data (%d decided variants of the %d needed; %d records in %d tests). Keep testing; verdicts need 7 days and about 1000 impressions each (assumptions)." % (g, e["decided"], MIN_DECIDED_GENRE, e["records"], e["tests"]))
            continue
        print("%s: %d decided variants from %d tests (assumption minimums: %d per genre, %d per feature value)" % (g, e["decided"], e["tests"], MIN_DECIDED_GENRE, MIN_DECIDED_FEATURE))
        if not e["features"]:
            print("  no feature value has %d decided variants yet" % MIN_DECIDED_FEATURE)
        for f in e["features"][:12]:
            print("  %-14s %-14s won %d of %d (%d%%)" % (f["feature"], f["value"], f["wins"], f["wins"] + f["losses"], round(100 * f["win_rate"])))
        if e["decided"] < REPLACE_WEIGHTS_AT:
            print("  these are leads: %d+ decided variants per genre before the rubric weights are replaced (rubric.md)" % REPLACE_WEIGHTS_AT)
        else:
            print("  enough to compare with the rubric weights (rubric.md): a feature that keeps winning deserves more weight")
    return 0


def settings_path():
    return os.path.join(tdir(), "settings.json")


def share_on():
    try:
        with open(settings_path(), encoding="utf-8") as f:
            return json.load(f).get("share") is True
    except (OSError, ValueError, AttributeError):
        return False


def cmd_share(a):
    if a.mode in ("on", "off"):
        os.makedirs(tdir(), exist_ok=True)
        with open(settings_path(), "w", encoding="utf-8", newline="\n") as f:
            json.dump({"share": a.mode == "on"}, f)
    print("thumbnail result sharing: %s. %s" % ("on" if share_on() else "off", "Per genre, once the minimums are met, feature tallies (no game names, no ids, no notes) are queued as roblox/thumbnails/<genre> notes and sent by `learn.py flush`; the vault owner curates them." if share_on() else "Results stay on this machine."))
    return 0


def make_note(g, e):
    lines = ["%s: %s won %d of %d decided variants" % (f["feature"], f["value"], f["wins"], f["wins"] + f["losses"]) for f in e["features"][:12]]
    body = ("Thumbnail personalization results for %s games: %d decided variants from %d tests. Verdicts follow an assumption rule (1000+ impressions, 7+ days, +/-10%% qPTR vs a control, "
            "same direction in both halves); read these as leads.\n%s" % (g, e["decided"], e["tests"], "\n".join(lines) or "no feature value has enough decided variants yet"))
    n = {"title": "Thumbnail feature results for %s games (%d decided variants)" % (g, e["decided"]), "topic": "roblox/thumbnails/" + g, "confidence": "medium", "source": H.platform_tag(), "created": H.today(),
         "body": body, "verified": "Tallied by thumb_record.py summary from the sender's own local ledger of Creator Hub qPTR, impressions and playtime per variant; no game names or ids included.", "schema": str(L.SCHEMA)}
    n["hash"] = L.note_hash(n["title"], n["body"], n["verified"])
    return n


def cmd_queue(a):
    if not share_on():
        if not a.quiet:
            print("thumb_record: sharing is off (thumb_record.py share on); nothing queued")
        return 0
    marker = os.path.join(tdir(), "queued.json")
    try:
        with open(marker, encoding="utf-8") as f:
            done = json.load(f)
    except (OSError, ValueError):
        done = {}
    q = L.queue_dir(None)
    pend = L.sub(q, "pending")
    sent = 0
    for g, e in summarise(load()).items():
        if not e["enough"] or not e["features"]:
            continue
        n = make_note(g, e)
        if done.get(g) == n["hash"]:
            continue
        problems, c, _red = L.check_note(n)
        if problems:
            if not a.quiet:
                print("thumb_record: %s note blocked: %s" % (g, ", ".join(p[0] for p in problems)))
            continue
        if len(os.listdir(pend)) >= L.MAX_PENDING:
            break
        with open(os.path.join(pend, "%s-%s.md" % (L.slugify(c["title"]), c["hash"][:8])), "w", encoding="utf-8", newline="\n") as f:
            f.write(L.render_note(c))
        done[g] = n["hash"]
        sent += 1
    if sent:
        os.makedirs(tdir(), exist_ok=True)
        with open(marker, "w", encoding="utf-8", newline="\n") as f:
            json.dump(done, f)
        if not a.quiet:
            print("thumb_record: queued %d note(s) for the next flush" % sent)
    elif not a.quiet:
        print("thumb_record: nothing new to queue")
    return 0


def main(argv=None):
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(prog="thumb_record.py", description="local ledger of thumbnail variant results and which features win")
    sp = ap.add_subparsers(dest="cmd")
    s = sp.add_parser("add")
    s.add_argument("--test"); s.add_argument("--genre"); s.add_argument("--variant"); s.add_argument("--control", action="store_true")
    s.add_argument("--asset", default="thumbnail", choices=("thumbnail", "icon", "ad"))
    s.add_argument("--impressions", type=int); s.add_argument("--qualified-plays", type=int); s.add_argument("--qptr", type=float); s.add_argument("--ctr", type=float)
    s.add_argument("--avg-playtime", type=float); s.add_argument("--date-start"); s.add_argument("--date-end")
    s.add_argument("--qptr-first-half", type=float); s.add_argument("--qptr-second-half", type=float)
    s.add_argument("--context", default="none", choices=("update", "event", "none")); s.add_argument("--segment")
    s.add_argument("--rubric-score", type=int); s.add_argument("--gates-ok", choices=("yes", "no"))
    s.add_argument("--feature", action="append"); s.add_argument("--varies", action="append")
    s.add_argument("--verdict"); s.add_argument("--game"); s.add_argument("--notes")
    s = sp.add_parser("decide"); s.add_argument("--test", required=True); s.add_argument("--write", action="store_true")
    s = sp.add_parser("list"); s.add_argument("--genre"); s.add_argument("--test")
    s = sp.add_parser("summary"); s.add_argument("--genre"); s.add_argument("--json", action="store_true")
    s = sp.add_parser("share"); s.add_argument("mode", nargs="?", choices=("on", "off", "status"), default="status")
    s = sp.add_parser("queue"); s.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    fn = {"add": cmd_add, "decide": cmd_decide, "list": cmd_list, "summary": cmd_summary, "share": cmd_share, "queue": cmd_queue}.get(a.cmd)
    if not fn:
        print(__doc__)
        return 2
    try:
        return fn(a)
    except KeyboardInterrupt:
        return 130
    except Exception as ex:
        if a.cmd == "queue" and a.quiet:
            return 0
        print("thumb_record: error: %s" % ex, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
