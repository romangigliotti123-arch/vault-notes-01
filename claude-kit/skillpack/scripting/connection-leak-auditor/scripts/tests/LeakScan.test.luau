--!nocheck
-- Run: lune run LeakScan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local LeakScan = require("../LeakScan")
local Janitor = require("../Janitor")

local function rules(findings)
	local r = {}
	for _, f in findings do
		table.insert(r, f.rule)
	end
	table.sort(r)
	return r
end

t.test("busy loop without a yield is flagged, with task.wait is not", function()
	t.eq(rules(LeakScan.scan("while true do\n\tcompute()\nend")), { "busy-loop" })
	t.eq(rules(LeakScan.scan("while true do\n\tcompute()\n\ttask.wait(1)\nend")), {})
end)

t.test("an unstored Connect inside PlayerAdded is flagged, a stored one is not", function()
	local bad =
		"Players.PlayerAdded:Connect(function(player)\n\tplayer.CharacterAdded:Connect(function(char)\n\tend)\nend)"
	t.eq(rules(LeakScan.scan(bad)), { "repeat-connect" })
	local good =
		"Players.PlayerAdded:Connect(function(player)\n\tlocal c = player.CharacterAdded:Connect(function(char)\n\tend)\nend)"
	t.eq(rules(LeakScan.scan(good)), {})
end)

t.test("player-keyed state without PlayerRemoving is flagged", function()
	local src = "Players.PlayerAdded:Connect(function(player)\n\tstate[player] = {}\nend)"
	t.eq(rules(LeakScan.scan(src)), { "player-state-not-cleared" })
	local fixed = src .. "\nPlayers.PlayerRemoving:Connect(function(player)\n\tstate[player] = nil\nend)"
	t.eq(rules(LeakScan.scan(fixed)), {})
end)

t.test("Instance.new with no Destroy or Debris is flagged", function()
	t.eq(rules(LeakScan.scan("local p = Instance.new('Part')")), { "instances-not-destroyed" })
	t.eq(rules(LeakScan.scan("local p = Instance.new('Part')\nDebris:AddItem(p, 3)")), {})
end)

t.test("unpaired render step binds are flagged", function()
	t.eq(rules(LeakScan.scan("RunService:BindToRenderStep('x', 1, f)")), { "unpaired-render-bind" })
end)

t.test("commented-out code is ignored and summarize counts rules", function()
	t.eq(rules(LeakScan.scan("-- while true do\n-- end")), {})
	local f = LeakScan.scan("while true do\nend\nwhile true do\nend")
	t.eq(LeakScan.summarize(f)["busy-loop"], 2)
end)

t.test("Janitor releases newest first and Cleanup is idempotent", function()
	local log = {}
	local jan = Janitor.new()
	jan:Add(function()
		table.insert(log, "a")
	end)
	jan:Add({
		Destroy = function()
			table.insert(log, "b")
		end,
	})
	jan:Add({
		Disconnect = function()
			table.insert(log, "c")
		end,
	})
	t.eq(jan:Count(), 3)
	t.eq(jan:Cleanup(), nil)
	t.eq(log, { "c", "b", "a" })
	jan:Cleanup()
	t.eq(#log, 3)
	t.eq(jan:Count(), 0)
end)

t.test("Janitor keeps going after a failing item and returns the first error", function()
	local ran = false
	local jan = Janitor.new()
	jan:Add(function()
		ran = true
	end)
	jan:Add(function()
		error("boom")
	end)
	local err = jan:Cleanup()
	t.truthy(string.find(err, "boom", 1, true))
	t.truthy(ran)
end)

t.test("Janitor closes threads", function()
	local jan = Janitor.new()
	local co = coroutine.create(function()
		coroutine.yield()
	end)
	coroutine.resume(co)
	jan:Add(co)
	jan:Cleanup()
	t.eq(coroutine.status(co), "dead")
end)

t.done()
