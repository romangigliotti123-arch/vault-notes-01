#!/usr/bin/env python3
"""compliance_gap.py <project> [--focus all|paid_random|ads|chat|ugc|region|data] [--json]   (python compliance_gap.py --selftest)

Static gap finder for the platform rules that are enforced in CODE: per-player PolicyService checks, text filtering, legacy chat,
third-party ad calls, personal data leaving the platform. It reads Luau/text files only. A FAIL means "the rule's code hook was not
found for a feature that needs it"; OK means a hook exists (not that it is correct); a missing hit is a lead, never proof.
Reuses age-rating-prep/scripts/feature_scan.py for the feature inventory. The live rules, names and thresholds are NOT built in:
read the Creator Docs page first (policies change). Exit 1 when any FAIL, 2 on bad arguments.
"""
import importlib.util
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FS_PATH = os.path.join(HERE, "..", "..", "age-rating-prep", "scripts", "feature_scan.py")
EXTS = (".luau", ".lua", ".md", ".txt", ".json")
FOCI = ("all", "paid_random", "ads", "chat", "ugc", "region", "data")

RX = {
    "policy_call": r"GetPolicyInfoForPlayerAsync",
    "paid_random_flag": r"ArePaidRandomItemsRestricted",
    "trading_flag": r"IsPaidItemTradingAllowed",
    "ads_flag": r"AreAdsAllowed",
    "ad_use": r"(AdGui|AdPortal|RewardedVideo|VideoAd|\bad ?placement)",
    "third_party_ad": r"(adserver|doubleclick|googlesyndication|adsterra|admob|unityads|applovin)",
    "random_item": r"(egg|crate|gacha|lootbox|loot_box|\bspin\b|\broll\b|mystery ?box|reroll|re-roll)",
    "robux_spend": r"(PromptProductPurchase|PromptGamePassPurchase|ProcessReceipt|PromptPurchase)",
    "trade": r"\b(trade|trading|gift)\b",
    "legacy_chat": r"(\.Chatted\b|Chat:Chat\(|Chat:FilterStringForBroadcast|LegacyChatService|\bChatService\b)",
    "text_input": r"(TextBox|FocusLost)",
    "filter": r"(FilterStringAsync|GetNonChatStringForBroadcastAsync|FilterStringForBroadcast|TextChannel|SendAsync|TextFilterResult)",
    "can_chat": r"(CanUserChatAsync|CanUsersChatAsync|CanUsersDirectChatAsync)",
    "rate": r"(cooldown|rateLimit|rate_limit|os\.clock|os\.time|tick\(\)|lastPost|lastSent)",
    "ugc_write": r"(UserText|plotName|signText|petName|CreateImageAsync|CreateEditableImage|SetAttribute\(['\"]Custom)",
    "out_http": r"HttpService:(PostAsync|RequestAsync)",
    "pii_word": r"(email|phone|address|real ?name|birthday|location)",
}


def load_scan():
    spec = importlib.util.spec_from_file_location("feature_scan", FS_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read(root):
    out = []
    for d, _, names in os.walk(root):
        dd = d.replace("\\", "/")
        if any(p in dd for p in ("/.git", "/node_modules", "/Packages")):
            continue
        for n in names:
            if n.endswith(EXTS):
                p = os.path.join(d, n)
                try:
                    lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
                except OSError:
                    continue
                out.append((os.path.relpath(p, root).replace("\\", "/"), lines))
    return out


def hits(files, key):
    rx = re.compile(RX[key], re.I)
    res = []
    for rel, lines in files:
        if not rel.endswith((".luau", ".lua")):
            continue
        for i, line in enumerate(lines, 1):
            s = line.strip()
            if not s or s.startswith("--"):
                continue
            if rx.search(line):
                res.append("%s:%d" % (rel, i))
    return res


def lead(h):
    return ", ".join(h[:3]) + (" (+%d)" % (len(h) - 3) if len(h) > 3 else "")


def run(root, focus="all"):
    files = read(root)
    H = {k: hits(files, k) for k in RX}
    rows = []

    def add(level, f, msg, h=None):
        rows.append({"level": level, "focus": f, "msg": msg, "where": lead(h) if h else ""})

    def want(f):
        return focus in ("all", f)

    paid_feature = bool(H["random_item"] and H["robux_spend"])
    if want("paid_random"):
        if not paid_feature:
            add("INFO", "paid_random", "no random-item + Robux-purchase pair found by scan (a lead, not proof of absence)")
        else:
            add("INFO", "paid_random", "random-item and purchase code both present; paid random rules likely apply", H["random_item"])
            if H["paid_random_flag"]:
                add("OK", "paid_random", "ArePaidRandomItemsRestricted referenced", H["paid_random_flag"])
            else:
                add("FAIL", "paid_random", "no ArePaidRandomItemsRestricted check: restricted players must not get the paid random flow", H["random_item"])
            if H["trade"] and not H["trading_flag"]:
                add("FAIL", "paid_random", "trading/gifting code but no IsPaidItemTradingAllowed check", H["trade"])
    if want("ads"):
        if H["third_party_ad"]:
            add("FAIL", "ads", "third-party ad host named in code: only self-uploaded ad content is allowed", H["third_party_ad"])
        if H["ad_use"]:
            add("INFO", "ads", "ad code present", H["ad_use"])
            if H["ads_flag"]:
                add("OK", "ads", "AreAdsAllowed referenced", H["ads_flag"])
            else:
                add("FAIL", "ads", "no AreAdsAllowed check before showing ads", H["ad_use"])
        elif not H["third_party_ad"]:
            add("INFO", "ads", "no ad code found")
    if want("chat"):
        if H["legacy_chat"]:
            add("FAIL", "chat", "legacy chat API in use: migrate to TextChatService", H["legacy_chat"])
        if H["text_input"]:
            if H["filter"]:
                add("OK", "chat", "filter or TextChannel calls exist (verify each input path uses them)", H["filter"])
            else:
                add("FAIL", "chat", "player text input found but no filter/TextChannel call anywhere", H["text_input"])
            if not H["rate"]:
                add("WARN", "chat", "no rate-limit/cooldown signal (shared boards need server-side limits)", H["text_input"])
            if not H["can_chat"]:
                add("INFO", "chat", "no CanUserChatAsync-style check (needed only for custom direct-message flows)")
        elif not H["legacy_chat"]:
            add("INFO", "chat", "no player text input found")
    if want("ugc"):
        if H["ugc_write"]:
            if H["filter"]:
                add("OK", "ugc", "filter calls exist; confirm every UGC path is covered", H["ugc_write"])
            else:
                add("FAIL", "ugc", "user-created text/image paths found but no filter call", H["ugc_write"])
        else:
            add("INFO", "ugc", "no user-created content paths found by scan")
    if want("region"):
        if H["policy_call"]:
            add("OK", "region", "GetPolicyInfoForPlayerAsync used", H["policy_call"])
        elif paid_feature or H["ad_use"] or H["trade"]:
            add("WARN", "region", "features that can be restricted per player exist but PolicyService is never called")
        else:
            add("INFO", "region", "no PolicyService use and no restricted-feature signal found")
    if want("data"):
        if H["out_http"]:
            add("WARN", "data", "outbound HTTP writes: confirm no personal data leaves the platform", H["out_http"])
            both = sorted(set(H["pii_word"]) & set(H["out_http"]))
            if both:
                add("FAIL", "data", "personal-data word on a line that sends HTTP", both)
        else:
            add("INFO", "data", "no outbound HTTP writes found")
    return rows


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write(
            "local egg = open(egg)\nMarketplaceService:PromptProductPurchase(p, 1)\nlocal t = TextBox\nplayer.Chatted:Connect(f)\n"
            "-- GetPolicyInfoForPlayerAsync\nlocal u = 'adserver.example'\nAdGui.new()\n")
        r = run(d)
        lv = {(x["focus"], x["level"]) for x in r}
        assert ("paid_random", "FAIL") in lv and ("chat", "FAIL") in lv and ("ads", "FAIL") in lv, r
        assert ("region", "OK") not in lv, "commented policy call must not count"
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "b.luau"), "w").write(
            "local egg = open(egg)\nPromptProductPurchase()\nlocal pol = P:GetPolicyInfoForPlayerAsync(p)\nif pol.ArePaidRandomItemsRestricted then end\n"
            "TextChatService.x\nlocal ok = AreAdsAllowed\nAdGui.new()\n")
        r = run(d)
        assert not any(x["level"] == "FAIL" for x in r), r
        assert any(x["focus"] == "region" and x["level"] == "OK" for x in r)
    assert load_scan().SIGNALS, "feature_scan import failed"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    focus = "all"
    rest = list(argv)
    if "--focus" in rest:
        i = rest.index("--focus")
        focus = rest[i + 1] if i + 1 < len(rest) else ""
        del rest[i:i + 2]
    args = [a for a in rest if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]) or focus not in FOCI:
        print(__doc__)
        return 2
    rows = run(args[0], focus)
    if "--json" in rest:
        print(json.dumps(rows, indent=2))
    else:
        for r in rows:
            print("[%s] %s: %s%s" % (r["level"], r["focus"], r["msg"], "  <- " + r["where"] if r["where"] else ""))
        print("static scan only: live-check the rule pages; hooks found are not proof they are correct")
    return 1 if any(r["level"] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
