--!nocheck
local t = require("../../../../../systems/_check/harness")
local Race = require("../RaceScheduler")

print("RaceScheduler")

t.test("count matches the multinomial", function()
	t.eq(Race.count({ 2, 2 }), 6)
	t.eq(Race.count({ 3, 1 }), 4)
	t.eq(Race.count({ 2, 2, 2 }), 90)
end)

t.test("explore visits every interleaving exactly once", function()
	local seen = {}
	local r = Race.explore(function()
		return {}
	end, {
		{ name = "A", steps = { function() end, function() end } },
		{ name = "B", steps = { function() end, function() end } },
	}, function()
		return nil
	end)
	t.eq(r.runs, 6)
	t.eq(#r.failures, 0)
	t.falsy(r.truncated)
end)

local function stock(atomic)
	local function buyer(name)
		if atomic then
			return {
				name = name,
				steps = {
					function(s)
						if s.stock > 0 then
							s.stock -= 1
							s.sold += 1
						end
					end,
				},
			}
		end
		return {
			name = name,
			steps = {
				function(s)
					s["ok" .. name] = s.stock > 0
				end,
				function(s)
					if s["ok" .. name] then
						s.stock -= 1
						s.sold += 1
					end
				end,
			},
		}
	end
	return Race.explore(function()
		return { stock = 1, sold = 0 }
	end, { buyer("A"), buyer("B") }, function(s)
		if s.sold > 1 then
			return `oversold: sold {s.sold} of 1`
		end
		return nil
	end)
end

t.test("check then yield then act oversells and the failing schedule is named", function()
	local r = stock(false)
	t.truthy(#r.failures > 0)
	t.eq(r.failures[1].schedule, "A1 B1 A2 B2")
	t.truthy(string.find(Race.report(r), "oversold", 1, true))
end)

t.test("the same logic done atomically never oversells", function()
	local r = stock(true)
	t.eq(#r.failures, 0)
	t.eq(r.runs, 2)
end)

t.test("a leave between trade steps is found, and an erroring step is reported", function()
	local r = Race.explore(function()
		return { a = { "pet" }, b = {}, saved = nil }
	end, {
		{
			name = "trade",
			steps = {
				function(s)
					s.b = { "pet" }
				end,
				function(s)
					s.a = {}
				end,
			},
		},
		{
			name = "leave",
			steps = {
				function(s)
					s.saved = { table.unpack(s.a) }
				end,
			},
		},
	}, function(s)
		if #s.b == 1 and s.saved and #s.saved == 1 then
			return "pet exists in B and in A's saved data"
		end
		return nil
	end)
	t.truthy(#r.failures > 0)
	local e = Race.explore(function()
		return {}
	end, { { name = "X", steps = {
		function()
			error("boom")
		end,
	} } }, function()
		return nil
	end)
	t.truthy(string.find(e.failures[1].message, "errored", 1, true))
end)

t.test("maxRuns caps the exploration", function()
	local r = Race.explore(function()
		return {}
	end, {
		{ name = "A", steps = { function() end, function() end, function() end } },
		{ name = "B", steps = { function() end, function() end, function() end } },
	}, function()
		return nil
	end, 5)
	t.eq(r.runs, 5)
	t.truthy(r.truncated)
end)

t.done()
