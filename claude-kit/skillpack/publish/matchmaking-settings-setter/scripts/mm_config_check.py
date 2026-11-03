#!/usr/bin/env python3
"""mm_config_check.py <matchmaking.json> | --template | --selftest

Validates a planned matchmaking configuration BEFORE it is entered in Creator Hub (the matchmaking pages are the authority; the product
changes, so signal and aggregation names are live-checked and can be overridden under "aggregations"). Config JSON:
  {"attributes": [{"name": "Skill", "type": "numeric|categorical", "source": "datastore", "datastore": "PlayerStats",
                   "key_template": "Player_{UserId}", "value_path": "rank.mmr", "scope": "global"}],
   "signals": [{"name": "SkillMatch", "attribute": "Skill", "aggregation": "average", "weight": 2.0}],
   "default_signals_weights": {"ping": 1.0}}
Checks: every signal names a defined attribute; aggregation is known for the attribute type (numeric: average/median/sum; categorical:
cluster/diversify); data-store attributes use the {UserId} token exactly and give a value path; weights are non-negative and at least one
is positive; names unique. Exit 1 on FAIL, 2 on bad input.
"""
import json
import sys

AGG = {"numeric": {"average", "median", "sum"}, "categorical": {"cluster", "diversify"}}


def check(c):
    out = []
    attrs = {}
    for a in c.get("attributes") or []:
        n = a.get("name")
        if not n:
            out.append(("FAIL", "attribute without a name"))
            continue
        if n in attrs:
            out.append(("FAIL", "duplicate attribute %r" % n))
        attrs[n] = a
        if a.get("type") not in AGG:
            out.append(("FAIL", "attribute %r type must be numeric or categorical" % n))
        if a.get("source") == "datastore":
            kt = str(a.get("key_template", ""))
            if "{UserId}" not in kt:
                out.append(("FAIL", "attribute %r key_template needs the exact token {UserId} (case-sensitive)" % n))
            if not a.get("value_path"):
                out.append(("FAIL", "attribute %r has no value_path into the stored JSON" % n))
    names, weights = set(), []
    for s in c.get("signals") or []:
        n = s.get("name")
        if n in names:
            out.append(("FAIL", "duplicate signal %r" % n))
        names.add(n)
        a = attrs.get(s.get("attribute"))
        if a is None:
            out.append(("FAIL", "signal %r uses undefined attribute %r (create attributes first)" % (n, s.get("attribute"))))
        else:
            allowed = set(c.get("aggregations", {}).get(a.get("type"), AGG.get(a.get("type"), set())))
            if s.get("aggregation") not in allowed:
                out.append(("FAIL", "signal %r: aggregation %r not valid for %s attribute (allowed %s)" % (n, s.get("aggregation"), a.get("type"), sorted(allowed))))
        w = s.get("weight")
        if not isinstance(w, (int, float)) or w < 0:
            out.append(("FAIL", "signal %r weight must be a number >= 0" % n))
        else:
            weights.append(w)
    for k, w in (c.get("default_signals_weights") or {}).items():
        if not isinstance(w, (int, float)) or w < 0:
            out.append(("FAIL", "default signal %r weight must be >= 0" % k))
        else:
            weights.append(w)
    if weights and not any(w > 0 for w in weights):
        out.append(("FAIL", "all weights are zero: matchmaking would have no preference"))
    if not weights:
        out.append(("WARN", "no signals configured: the platform defaults apply"))
    if not any(lv == "FAIL" for lv, _ in out):
        out.append(("OK", "config is consistent; use Preview and Test in Creator Hub before applying to live places"))
    return out


def selftest():
    good = {"attributes": [{"name": "Skill", "type": "numeric", "source": "datastore", "key_template": "P_{UserId}", "value_path": "mmr"},
                           {"name": "Mode", "type": "categorical"}],
            "signals": [{"name": "S", "attribute": "Skill", "aggregation": "average", "weight": 2}, {"name": "M", "attribute": "Mode", "aggregation": "cluster", "weight": 1}]}
    assert [x[0] for x in check(good)] == ["OK"], check(good)
    bad = {"attributes": [{"name": "Skill", "type": "numeric", "source": "datastore", "key_template": "P_{userId}"}],
           "signals": [{"name": "S", "attribute": "Skill", "aggregation": "cluster", "weight": 0}, {"name": "T", "attribute": "Nope", "aggregation": "sum", "weight": -1}]}
    f = [m for lv, m in check(bad) if lv == "FAIL"]
    assert len(f) == 6, f
    assert check({})[0][0] == "WARN"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps({"attributes": [{"name": "", "type": "numeric", "source": "datastore", "datastore": "", "key_template": "Player_{UserId}",
                                          "value_path": "", "scope": "global"}], "signals": [{"name": "", "attribute": "", "aggregation": "average", "weight": 1.0}],
                          "default_signals_weights": {}}, indent=2))
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        c = json.load(open(argv[0], encoding="utf-8"))
        assert isinstance(c, dict)
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    rows = check(c)
    for lv, m in rows:
        print("[%s] %s" % (lv, m))
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
