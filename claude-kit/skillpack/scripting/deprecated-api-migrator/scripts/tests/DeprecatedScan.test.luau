--!nocheck
local t = require("../../../../../systems/_check/harness")
local DeprecatedScan = require("../DeprecatedScan")

local function ids(source)
	local out = {}
	for _, h in DeprecatedScan.scan(source) do
		table.insert(out, h.rule)
	end
	return out
end

t.test("bare wait/spawn/delay are found; task.* and method forms are not", function()
	t.eq(ids("wait(1)\nspawn(function() end)\ndelay(2, f)"), { "wait", "spawn", "delay" })
	t.eq(ids("task.wait(1)\ntask.spawn(f)\nevent:Wait()\nmy_wait(1)"), {})
end)

t.test("comments are ignored", function()
	t.eq(ids("-- wait(1)\nlocal x = 1 -- spawn(f)"), {})
end)

t.test("FindPartOnRay family is found as a method call", function()
	t.eq(ids("workspace:FindPartOnRayWithIgnoreList(ray, {})"), { "FindPartOnRayWithIgnoreList" })
end)

t.test("legacy movers and SetPrimaryPartCFrame are reported with a general confidence label", function()
	local hits = DeprecatedScan.scan("local bv = Instance.new('BodyVelocity')\nmodel:SetPrimaryPartCFrame(cf)")
	t.eq(#hits, 2)
	t.eq(hits[1].replacement, "LinearVelocity")
	t.eq(hits[1].confidence, "general")
	t.eq(hits[2].line, 2)
end)

t.test("purchase-finished events and PhysicsService collision methods carry vault confidence", function()
	local hits = DeprecatedScan.scan(
		"MarketplaceService.PromptProductPurchaseFinished:Connect(f)\nPhysicsService:RegisterCollisionGroup('A')"
	)
	t.eq(#hits, 2)
	t.eq(hits[1].confidence, "vault")
	t.eq(hits[2].confidence, "vault")
end)

t.test("LoadAnimation is only flagged when called on a Humanoid", function()
	t.eq(ids("humanoid:LoadAnimation(anim)"), { "Humanoid:LoadAnimation" })
	t.eq(ids("animator:LoadAnimation(anim)"), {})
end)

t.test("lowercase connect/remove and bare unpack", function()
	t.eq(ids("part.Touched:connect(f)\npart:remove()\nlocal a = unpack(t)\nlocal b = table.unpack(t)"), {
		"lowercase-connect",
		"lowercase-remove",
		"unpack",
	})
end)

t.test("summarize puts vault-backed rules first", function()
	local hits = DeprecatedScan.scan("unpack(a)\nwait(1)\nwait(2)")
	local s = DeprecatedScan.summarize(hits)
	t.eq(s[1].rule, "wait")
	t.eq(s[1].count, 2)
	t.eq(s[2].rule, "unpack")
end)

t.done()
