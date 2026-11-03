#!/usr/bin/env python3
"""settings_check.py <settings.json> | --template | --selftest

Checks a planned experience settings sheet for internal conflicts and for the numeric limits the Creator Docs publishing pages stated when
the vault was built (2026-10-28). Those numbers change: every limit can be overridden in the JSON under "limits", and the skill must
live-check the pages and pass the current values. The script never touches Creator Hub; the owner enters the settings.
Fields (all optional; missing = WARN "undecided"): name, description, genre, subgenre, genre_changed_days_ago, questionnaire_done,
audience, access ("public"|"private"|"friends"), max_players, devices[], private_servers{enabled,paid}, paid_access, place_size_bytes,
early_testers, thumbnails_active, icon_px[w,h], premium_or_fee_plan, exclude_from_recommendations.
Exit 1 on FAIL, 2 on bad input.
"""
import json
import sys

DEFAULT_LIMITS = {"place_bytes": 104857600, "early_testers": 10, "thumbs_min": 2, "thumbs_max": 5, "icon_min_px": 512,
                  "description_chars": 1000, "genre_change_days": 90}
FIELDS = ["name", "description", "genre", "access", "max_players", "devices", "questionnaire_done", "audience", "thumbnails_active", "icon_px"]


def check(s):
    L = dict(DEFAULT_LIMITS)
    L.update(s.get("limits") or {})
    out = []

    def add(lv, m):
        out.append((lv, m))

    for f in FIELDS:
        if s.get(f) in (None, "", []):
            add("WARN", "%s is undecided" % f)
    if s.get("questionnaire_done") is False:
        add("FAIL", "maturity questionnaire not done: experiences without it have restricted reach (live-check)")
    d = s.get("description")
    if isinstance(d, str) and len(d) > L["description_chars"]:
        add("FAIL", "description is %d chars, limit %d" % (len(d), L["description_chars"]))
    pb = s.get("place_size_bytes")
    if isinstance(pb, (int, float)) and pb > L["place_bytes"]:
        add("FAIL", "place is %d bytes, over %d: save/publish may fail; reduce or split into places" % (pb, L["place_bytes"]))
    elif isinstance(pb, (int, float)) and pb > 0.8 * L["place_bytes"]:
        add("WARN", "place is over 80%% of the size limit (%d bytes)" % pb)
    et = s.get("early_testers")
    if isinstance(et, int) and et > L["early_testers"]:
        add("FAIL", "%d early testers, limit %d" % (et, L["early_testers"]))
    t = s.get("thumbnails_active")
    if isinstance(t, int):
        if t < 1:
            add("FAIL", "no active thumbnail")
        elif t < L["thumbs_min"] or t > L["thumbs_max"]:
            add("WARN", "%d active thumbnails; the docs advise %d-%d for personalisation" % (t, L["thumbs_min"], L["thumbs_max"]))
    ic = s.get("icon_px")
    if isinstance(ic, list) and len(ic) == 2:
        if ic[0] != ic[1]:
            add("FAIL", "icon %dx%d is not square" % tuple(ic))
        elif ic[0] < L["icon_min_px"]:
            add("FAIL", "icon %dpx under the %dpx minimum" % (ic[0], L["icon_min_px"]))
    g = s.get("genre_changed_days_ago")
    if isinstance(g, (int, float)) and g < L["genre_change_days"] and s.get("genre_change_planned"):
        add("FAIL", "genre changed %d days ago; changes are limited to once per %d days" % (g, L["genre_change_days"]))
    ps = s.get("private_servers") or {}
    if ps.get("enabled") and s.get("access") not in (None, "public"):
        add("FAIL", "private servers need a public experience (access=%r)" % s.get("access"))
    if ps.get("enabled") and ps.get("paid") and s.get("paid_access"):
        add("FAIL", "paid access and paid private servers cannot be enabled together")
    mp = s.get("max_players")
    if isinstance(mp, int) and mp < 1:
        add("FAIL", "max_players must be at least 1")
    dv = s.get("devices") or []
    if dv and "phone" not in dv and "mobile" not in dv:
        add("WARN", "no phone in supported devices: most players are on phones; confirm this is intended")
    if s.get("audience") == "all_ages" and not (s.get("premium_or_fee_plan") or s.get("kids_select_ready")):
        add("WARN", "all-ages release has account/fee requirements: record the plan in premium_or_fee_plan (live-check)")
    if not any(lv == "FAIL" for lv, _ in out):
        add("OK", "no conflicts in the sheet (settings still entered by the owner in Creator Hub)")
    return out


def selftest():
    good = {"name": "x", "description": "d", "genre": "g", "access": "public", "max_players": 10, "devices": ["phone", "pc"], "questionnaire_done": True,
            "audience": "13+", "thumbnails_active": 3, "icon_px": [512, 512], "place_size_bytes": 10, "private_servers": {"enabled": True, "paid": True}}
    assert not any(x[0] == "FAIL" for x in check(good)), check(good)
    bad = dict(good, access="private", paid_access=True, place_size_bytes=200000000, early_testers=11, icon_px=[500, 500], questionnaire_done=False,
               description="x" * 1001, thumbnails_active=0)
    fails = [m for lv, m in check(bad) if lv == "FAIL"]
    assert len(fails) == 8, fails
    ov = dict(good, limits={"early_testers": 20}, early_testers=15)
    assert not any("early" in m for lv, m in check(ov) if lv == "FAIL")
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps({"name": "", "description": "", "genre": "", "subgenre": "", "questionnaire_done": None, "audience": "", "access": "",
                          "max_players": None, "devices": [], "private_servers": {"enabled": False, "paid": False}, "paid_access": False,
                          "place_size_bytes": None, "early_testers": 0, "thumbnails_active": None, "icon_px": [], "limits": {}}, indent=2))
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        s = json.load(open(argv[0], encoding="utf-8"))
        assert isinstance(s, dict)
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    rows = check(s)
    for lv, m in rows:
        print("[%s] %s" % (lv, m))
    print("limits are from the 2026-10-28 docs snapshot unless overridden in \"limits\": live-check before relying on them")
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
