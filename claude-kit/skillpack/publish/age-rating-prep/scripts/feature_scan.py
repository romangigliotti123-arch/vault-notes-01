#!/usr/bin/env python3
"""feature_scan.py <project-folder> [--json]   (python feature_scan.py --selftest)

Builds a FEATURE INVENTORY of a Roblox project from its Luau/text files: which features exist that the experience maturity
questionnaire and the safety rules care about (chat, voice, user content, paid random items, trading, violence words, external
links, ...). It does NOT answer the questionnaire and does NOT know Roblox's current questions: the wording and the options must
be read live from Creator Hub. Each row is a lead with file:line evidence; a missing row means "not found by this scan", not "absent".
Exit 0 always (it is an inventory), 2 on bad arguments.
"""
import json, os, re, sys, tempfile

SIGNALS = [
    ("chat", "Player chat or custom text input", r"TextChatService|TextChannel|Chat:Chat|SendAsync|TextBox"),
    ("voice", "Voice chat", r"VoiceChatService|VoiceChat|AudioDeviceInput"),
    ("ugc_content", "User-generated content (names, text, images, builds, uploads)", r"AssetService|CreateImageAsync|PromptCreateAvatar|UGC|plot.*name|sign.*text|SetAttribute\(['\"]Custom"),
    ("paid_random", "Paid random items (eggs, crates, gacha)", r"(egg|crate|gacha|lootbox|loot_box|spin|roll)"),
    ("purchases", "In-experience purchases", r"PromptProductPurchase|PromptGamePassPurchase|ProcessReceipt|PromptPurchase"),
    ("trading", "Player-to-player trading or gifting", r"\b(trade|trading|gift)\b"),
    ("violence", "Combat / weapons / defeat", r"(weapon|sword|gun|shoot|damage|kill|blood|gore|explod)"),
    ("scary", "Horror or frightening content", r"(jumpscare|horror|scary|monster|zombie|creepy)"),
    ("social_hang", "Social hangout / dating / roleplay features", r"(dating|date |boyfriend|girlfriend|roleplay|rp )"),
    ("external_links", "Links or references to outside sites", r"https?://|discord\.gg|youtube\.com|twitter\.com"),
    ("gambling_like", "Betting, casino or wager mechanics", r"(bet|wager|casino|jackpot|slot machine|coinflip|gamble)"),
    ("alcohol_drugs", "Alcohol, smoking or drug references", r"(beer|wine|vodka|cigar|smok|weed|drug|vape)"),
    ("data_collection", "Data stored about players", r"DataStoreService|MemoryStoreService|HttpService:(Post|Request)Async|AnalyticsService"),
    ("web_requests", "Outside HTTP requests", r"HttpService:(GetAsync|PostAsync|RequestAsync)"),
]
EXTS = (".luau", ".lua", ".md", ".txt", ".json")


def scan(root):
    rows = {k: {"title": t, "hits": []} for k, t, _ in SIGNALS}
    rx = {k: re.compile(p, re.I) for k, _, p in SIGNALS}
    for d, _, names in os.walk(root):
        dd = d.replace("\\", "/")
        if any(p in dd for p in ("/.git", "/node_modules", "/Packages")):
            continue
        for n in names:
            if not n.endswith(EXTS):
                continue
            p = os.path.join(d, n)
            rel = os.path.relpath(p, root).replace("\\", "/")
            try:
                lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines, 1):
                for k, r in rx.items():
                    if r.search(line) and len(rows[k]["hits"]) < 8:
                        rows[k]["hits"].append("%s:%d %s" % (rel, i, line.strip()[:90]))
    return rows


def show(rows, as_json):
    if as_json:
        print(json.dumps(rows, indent=2))
        return
    for k, r in rows.items():
        print("%-16s %s  [%s]" % (k, r["title"], "%d lead(s)" % len(r["hits"]) if r["hits"] else "none found"))
        for h in r["hits"][:3]:
            print("      " + h)
    print("inventory only: read the live questionnaire in Creator Hub and answer from the code, not from this list")


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write(
            "local t = TextChatService\nlocal egg = Eggs.open()\nMarketplaceService:PromptProductPurchase(p, 1)\nprint('hello')\n-- https://example.com\n")
        open(os.path.join(d, "b.md"), "w").write("Players can trade swords\n")
        rows = scan(d)
        assert rows["chat"]["hits"], rows
        assert rows["paid_random"]["hits"] and rows["purchases"]["hits"]
        assert rows["trading"]["hits"] and rows["violence"]["hits"]
        assert rows["external_links"]["hits"]
        assert not rows["voice"]["hits"] and not rows["gambling_like"]["hits"]
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    show(scan(args[0]), "--json" in argv)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
