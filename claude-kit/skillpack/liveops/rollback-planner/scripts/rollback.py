#!/usr/bin/env python3
"""rollback.py - check a release manifest: can every change be undone, and what does undoing it cost? Stdlib only.

  python rollback.py release.json
  python rollback.py --selftest
  release.json = {"release": "update-12", "changes": [
      {"name": "boss health", "kind": "config", "revert": "restore previous config version", "previous_value_recorded": true},
      {"name": "new quest chain", "kind": "code", "revert": "republish previous version", "adds_save_fields": true, "old_code_reads_new_data": true},
      {"name": "currency rename migration", "kind": "data", "revert": "none", "backup": false}, ...]}
  kinds: config | code | data | asset | purchase | event

Rules come from Roblox/roblox-kb/updates-live-ops.md (roll back severe regressions first, then profile; test every update and watch the first minutes;
config values can change without a publish; a publish takes about 15 seconds to 1 minute to propagate and players move to the new version only as old servers empty;
restart strategy and a bleed-off window) and ab-testing-and-experiments.md (publishing a config draft is irreversible except by restoring a previous
version; gradual rollout of 15 minutes). The extra checks (data migrations need a backup and an old-code-readable format) are standard release practice, labelled
as this skill's rules. Exit 0 = no blocking finding, 1 = at least one BLOCK.
"""
import json
import sys


def check(rel):
    blocks, warns = [], []
    ch = rel.get("changes", [])
    if not ch:
        return ["manifest has no changes"], []
    for c in ch:
        n, k, rv = c.get("name", "?"), c.get("kind", "?"), (c.get("revert") or "").strip().lower()
        if k not in ("config", "code", "data", "asset", "purchase", "event"):
            blocks.append("%s: unknown kind %r" % (n, k))
            continue
        if not rv or rv == "none":
            if k in ("data", "purchase"):
                blocks.append("%s: %s change with no revert path" % (n, k))
            else:
                warns.append("%s: no revert described" % n)
        if k == "config" and not c.get("previous_value_recorded"):
            blocks.append("%s: record the previous config value/version before changing (draft publish is only undone by restoring a previous version)" % n)
        if k == "code" and c.get("adds_save_fields") and not c.get("old_code_reads_new_data"):
            blocks.append("%s: new save fields; old code must tolerate them or a code rollback corrupts/loses data" % n)
        if k == "data":
            if not c.get("backup"):
                blocks.append("%s: data migration without a backup/export of the affected records" % n)
            if not c.get("reversible_migration"):
                warns.append("%s: migration is one-way; rollback = restore from backup, which loses newer progress" % n)
        if k == "purchase" and not c.get("refund_plan"):
            warns.append("%s: purchasable change without a refund/compensation plan" % n)
        if k == "event" and not c.get("kill_flag"):
            warns.append("%s: event has no kill flag/config to disable it without a publish" % n)
    if not rel.get("watch_minutes"):
        warns.append("no watch window set: vault says watch errors and crash rate in the first minutes after publishing")
    if not rel.get("owner"):
        warns.append("no named decision owner for the rollback call")
    if not rel.get("trigger"):
        warns.append("no rollback trigger (e.g. client crash rate above 5%% for 5 minutes, vault example) defined")
    return blocks, warns


def selftest():
    ok = {"release": "r1", "owner": "me", "watch_minutes": 30, "trigger": "crash>5%", "changes": [
        {"name": "boss hp", "kind": "config", "revert": "restore config v7", "previous_value_recorded": True},
        {"name": "quests", "kind": "code", "revert": "republish v41", "adds_save_fields": True, "old_code_reads_new_data": True}]}
    b, w = check(ok)
    assert not b and not w, (b, w)
    bad = {"changes": [{"name": "rename", "kind": "data", "revert": "none"}, {"name": "hp", "kind": "config", "revert": "x"},
                       {"name": "q", "kind": "code", "revert": "x", "adds_save_fields": True}, {"name": "ev", "kind": "event", "revert": "x"}, {"name": "s", "kind": "weird"}]}
    b, w = check(bad)
    assert len(b) == 5 and any("no revert path" in x for x in b) and any("backup" in x for x in b), b
    assert any("kill flag" in x for x in w) and any("watch window" in x for x in w) and any("one-way" in x or "owner" in x for x in w)
    assert check({})[0]
    print("selftest ok (4 checks)")


def main(argv):
    if argv[:1] == ["--selftest"]:
        selftest()
        return 0
    if not argv:
        print(__doc__)
        return 2
    b, w = check(json.load(open(argv[0], encoding="utf-8")))
    for x in b:
        print("BLOCK:", x)
    for x in w:
        print("warn: ", x)
    print("%d blocking, %d warnings" % (len(b), len(w)))
    return 1 if b else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
