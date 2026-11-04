--!nocheck
local t = require("../../../../../systems/_check/harness")
local DataLoss = require("../DataLoss")
local PlayerData = require("../../../../../systems/PlayerData/src/PlayerData")

local function kitFactory(jobId, store, clock, lostLog)
	return PlayerData.new({
		store = store,
		jobId = jobId,
		template = { coins = 0 },
		now = function()
			return clock.t
		end,
		wait = clock.wait,
		spawn = function(fn)
			fn()
		end,
		onLost = function(_, why)
			table.insert(lostLog, why)
		end,
	})
end

local function naiveFactory(jobId, store, clock, lostLog)
	local sessions = {}
	local pd = {}
	function pd:LoadAsync(key)
		local ok, row = pcall(store.UpdateAsync, store, key, function(old)
			return old or { data = { coins = 0 } }
		end)
		if not ok then
			return nil, "failed"
		end
		local s = { Key = key, Data = row.data, State = "active" }
		sessions[key] = s
		return s
	end
	function pd:SaveAsync(s)
		return (pcall(store.UpdateAsync, store, s.Key, function()
			return { data = s.Data }
		end))
	end
	function pd:ReleaseAsync(s)
		return self:SaveAsync(s)
	end
	function pd:ReleaseAll()
		for _, s in sessions do
			self:SaveAsync(s)
		end
	end
	function pd:AutosaveDue()
		return 0
	end
	return pd
end

print("DataLoss")

t.test("the kit PlayerData passes every scenario", function()
	local results = DataLoss.runAll(kitFactory)
	t.eq(#results, 8)
	for _, r in results do
		t.truthy(r.ok, r.name .. " -> " .. r.detail)
	end
end)

t.test("a naive saver fails the lock and autosave scenarios, so the scenarios can fail", function()
	local failed = {}
	for _, r in DataLoss.runAll(naiveFactory) do
		if not r.ok then
			failed[r.name] = true
		end
	end
	t.truthy(failed["old server cannot overwrite after takeover"])
	t.truthy(failed["progress lost in a crash is bounded by the autosave interval"])
end)

t.test("report summarises and names failures", function()
	local r = DataLoss.report(DataLoss.runAll(naiveFactory))
	t.truthy(string.find(r, "FAIL", 1, true))
	t.truthy(string.find(DataLoss.report(DataLoss.runAll(kitFactory)), "8/8 scenarios passed", 1, true))
end)

t.test("scenario names are listed", function()
	t.eq(#DataLoss.scenarioNames(), 8)
end)

t.done()
