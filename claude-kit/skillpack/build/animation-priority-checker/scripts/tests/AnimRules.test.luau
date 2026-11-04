--!nocheck
local t = require("../../../../../systems/_check/harness")
local AR = require("../AnimRules")

t.test("a correct idle passes", function()
	t.eq(AR.check("IdleBreathing", "Idle", true), {})
end)

t.test("idle on Action priority blocks other animations", function()
	local i = AR.check("idle_main", "Action", true)
	t.eq(#i, 1)
	t.eq(i[1].kind, "priority")
end)

t.test("walk on Idle priority is overridden by defaults", function()
	local i = AR.check("WalkForward", "Idle", true)
	t.eq(i[1].kind, "priority")
end)

t.test("run that does not loop is flagged", function()
	local i = AR.check("Run", "Movement", false)
	t.eq(#i, 1)
	t.eq(i[1].kind, "looped")
end)

t.test("an attack must be Action or higher and must not loop", function()
	t.eq(AR.check("SwordSlash", "Action2", false), {})
	t.eq(#AR.check("SwordSlash", "Movement", true), 2)
end)

t.test("unknown priority and Core on unmatched names are reported", function()
	t.eq(AR.check("Thing", "Banana", false)[1].kind, "priority")
	t.eq(#AR.check("Mystery", "Core", false), 1)
	t.eq(AR.check("Mystery", "Action", false), {})
end)

t.test("rank orders the seven levels", function()
	t.truthy(AR.rank("Action4") > AR.rank("Action"))
	t.truthy(AR.rank("Core") < AR.rank("Idle"))
	t.eq(AR.rank("Nope"), nil)
end)

t.done()
