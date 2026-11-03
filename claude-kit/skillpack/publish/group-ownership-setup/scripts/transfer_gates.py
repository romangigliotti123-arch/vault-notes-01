#!/usr/bin/env python3
"""transfer_gates.py --template | --selftest

Emits a game-ownership-transfer gate list in the format of publish-readiness-gate/scripts/gate.py, so the same arithmetic judges it:
    python transfer_gates.py --template > release/transfer.json   (fill status/evidence)
    python ../../publish-readiness-gate/scripts/gate.py release/transfer.json
The gates come from the Creator Docs game-ownership-transfer and groups pages (2026-10-28 snapshot): live-check each, they change.
Nothing here transfers anything: the transfer is the owner's action in Creator Hub.
"""
import importlib.util
import json
import os
import sys

GATES = [
    ("Owner email verified on the sending account", "Creator Hub account settings"),
    ("Private ModuleScripts and InsertService assets moved to the receiving group", "Asset Manager; list_assets.luau output"),
    ("User-owned packages recreated or replaced with group-owned ones", "Asset Manager > Packages"),
    ("Open Cloud API keys reviewed: re-created under an account that keeps access", "Creator Hub > API keys"),
    ("Place Copying disabled before private assets go into the group game", "Experience settings > Permissions"),
    ("Receiving group roles use least privilege; two-step verification on for money roles", "roles_check.py output on the role CSV"),
    ("Revenue split agreed in writing before the transfer", "doc or message link"),
    ("Title unchanged through the transfer", "settings screenshot or text"),
    ("No other edits made while the transfer request is pending (they are not carried over)", "Activity History"),
    ("Receiving side: payment details set, game released again after acceptance, permissions set", "post-transfer check"),
    ("Cooldown known: a received game cannot be re-transferred for a set period", "docs page, live-check the number"),
    ("Backup manifest verified before the transfer", "backup_check.py verify output"),
]


def template():
    return [{"gate": g, "status": "", "evidence": "", "owner": "", "waiver": "", "how": h} for g, h in GATES]


def selftest():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "publish-readiness-gate", "scripts", "gate.py")
    spec = importlib.util.spec_from_file_location("gate", p)
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    t = template()
    assert gate.evaluate(t)[0] == "NO-GO", "blank template must be NO-GO"
    for g in t:
        g["status"], g["evidence"] = "pass", "e"
    assert gate.evaluate(t)[0] == "GO"
    t[0]["evidence"] = ""
    assert gate.evaluate(t)[0] == "NO-GO"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps(template(), indent=2))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
