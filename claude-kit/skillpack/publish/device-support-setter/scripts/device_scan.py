#!/usr/bin/env python3
"""device_scan.py <project> | --selftest

Per-device input support from the code: which of keyboard/mouse, touch and gamepad the scripts actually handle, plus console hazards.
Static leads only; a supported-devices setting is justified by playing on the device, which this does not do.
Rows: KEYBOARD (raw KeyCode / MouseButton handling), TOUCH (Touch types, TouchEnabled, TouchTap), GAMEPAD (Gamepad KeyCodes, GamepadEnabled),
ABSTRACT (InputAction system, ContextActionService, PreferredInput, InputActionLabel: one binding layer for all devices),
CHAT (chat UI that must be off on console per the console guidelines page; live-check), PIXEL (large fixed pixel UDim2 offsets).
Verdicts: FAIL when keyboard/mouse code exists with no touch, no gamepad and no abstract layer (a phone or console player cannot act);
WARN when only some are covered. Exit 1 on FAIL, 2 on bad args.
"""
import os
import re
import sys
import tempfile

RX = {
    "KEYBOARD": r"(Enum\.KeyCode\.[A-Z]\b|KeyCode\.(Space|LeftShift|E|F|Q)\b|UserInputType\.(MouseButton1|MouseButton2|Keyboard)|GetMouse\(\))",
    "TOUCH": r"(UserInputType\.Touch|TouchEnabled|TouchTap|TouchTapInWorld|TouchSwipe|TouchPinch|TouchStarted)",
    "GAMEPAD": r"(KeyCode\.(ButtonA|ButtonB|ButtonX|ButtonY|ButtonR2|ButtonL2|DPad\w+|Thumbstick\d)|GamepadEnabled|Gamepad1|UserInputType\.Gamepad)",
    "ABSTRACT": r"(InputAction\b|InputContext|InputBinding|ContextActionService|PreferredInput|InputActionLabel)",
    "CHAT": r"(ChatWindowConfiguration|TextChatService|StarterGui:SetCoreGuiEnabled\(\s*Enum\.CoreGuiType\.Chat)",
    "PIXEL": r"UDim2\.(new|fromOffset)\(\s*0\s*,\s*\d{3,}\s*,\s*0\s*,\s*\d{3,}",
}


def scan(root):
    res = {k: [] for k in RX}
    for d, _, names in os.walk(root):
        if any(p in d.replace("\\", "/") for p in ("/.git", "/Packages", "/node_modules")):
            continue
        for n in names:
            if not n.endswith((".luau", ".lua")):
                continue
            p = os.path.join(d, n)
            rel = os.path.relpath(p, root).replace("\\", "/")
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace").read().splitlines(), 1):
                if line.strip().startswith("--"):
                    continue
                for k, rx in RX.items():
                    if re.search(rx, line):
                        res[k].append("%s:%d" % (rel, i))
    return res


def verdict(res):
    out = []
    kb, tc, gp, ab = res["KEYBOARD"], res["TOUCH"], res["GAMEPAD"], res["ABSTRACT"]
    if kb and not (tc or gp or ab):
        out.append(("FAIL", "keyboard/mouse input only: phone and console players cannot act (add touch buttons / an input action layer)"))
    elif kb and not ab:
        missing = [n for n, h in (("touch", tc), ("gamepad", gp)) if not h]
        if missing:
            out.append(("WARN", "raw device handling without an abstract layer; no %s code found" % " or ".join(missing)))
    if not kb and not tc and not gp and not ab:
        out.append(("INFO", "no input code found by the scan"))
    if res["CHAT"]:
        out.append(("WARN", "chat code present: the console guidelines page says to disable the chat window on console (live-check); confirm per device"))
    if res["PIXEL"]:
        out.append(("WARN", "large fixed pixel UI sizes: use scale + constraints so UI fits phones and TVs"))
    if not out:
        out.append(("OK", "input layer present for the devices found; still play each device"))
    return out


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write("if input.KeyCode == Enum.KeyCode.E then end\n-- TouchTap\n")
        v = verdict(scan(d))
        assert v[0][0] == "FAIL", v
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write("local a = Enum.KeyCode.E\nContextActionService:BindAction('x', f, true)\nf.Position = UDim2.new(0, 400, 0, 300)\n")
        v = verdict(scan(d))
        assert [x[0] for x in v] == ["WARN"], v
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) != 1 or not os.path.isdir(argv[0]):
        print(__doc__)
        return 2
    res = scan(argv[0])
    for k, h in res.items():
        print("%-9s %3d lead(s) %s" % (k, len(h), ", ".join(h[:3])))
    v = verdict(res)
    for lv, m in v:
        print("[%s] %s" % (lv, m))
    return 1 if any(x[0] == "FAIL" for x in v) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
