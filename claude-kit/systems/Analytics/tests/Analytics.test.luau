--!nocheck
-- Run: lune run tests/Analytics.test.luau   (from the Analytics folder)
local t = require("../../_check/harness")
local Analytics = require("../src/Analytics")

local function make(over)
	local env = { calls = {}, logs = {}, clock = 1000, fail = false }
	local svc = {}
	for _, m in
		{
			"LogEconomyEvent",
			"LogOnboardingFunnelStepEvent",
			"LogFunnelStepEvent",
			"LogProgressionEvent",
			"LogCustomEvent",
		}
	do
		svc[m] = function(_, ...)
			if env.fail then
				error("service down")
			end
			table.insert(env.calls, { m = m, args = { ... } })
		end
	end
	local cfg = {
		service = svc,
		flowTypes = { Source = "ENUM_SOURCE", Sink = "ENUM_SINK" },
		progressionTypes = { Start = "P_START", Complete = "P_COMPLETE", Fail = "P_FAIL" },
		now = function()
			return env.clock
		end,
		customFieldKeys = { "CF1", "CF2", "CF3" },
		log = function(m)
			table.insert(env.logs, m)
		end,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return Analytics.new(cfg), env
end

local P = { UserId = 7 }

print("Analytics")

t.test("economy: maps Source/Sink to the enum and passes every argument through", function()
	local a, env = make()
	t.truthy(a:Economy(P, "Source", "Coins", 50, 150, "Gameplay", "quest_1"))
	local c = env.calls[1]
	t.eq(c.m, "LogEconomyEvent")
	t.eq(c.args[2], "ENUM_SOURCE")
	t.eq(c.args[3], "Coins")
	t.eq(c.args[4], 50)
	t.eq(c.args[5], 150)
	t.eq(c.args[7], "quest_1")
end)

t.test("economy: invalid arguments are dropped with a log, not thrown", function()
	local a, env = make()
	t.falsy(a:Economy(P, "Source", "Coins", -5, 10, "Gameplay", "x"))
	t.falsy(a:Economy(P, "Source", "Coins", 0, 10, "Gameplay", "x"))
	t.falsy(a:Economy(P, "Source", "Coins", 5, -1, "Gameplay", "x"))
	t.falsy(a:Economy(P, "Source", "Coins", 0 / 0, 1, "Gameplay", "x"))
	t.falsy(a:Economy(P, "Bogus" :: any, "Coins", 5, 1, "Gameplay", "x"))
	t.falsy(a:Economy(P, "Sink", "", 5, 1, "Gameplay", "x"))
	t.eq(#env.calls, 0)
	t.eq(#env.logs, 6)
end)

t.test("economy: the documented caps are enforced locally (5 currencies, 20 tx types, 100 skus)", function()
	local a, env = make({ maxPerMinute = 100000 })
	for i = 1, 6 do
		a:Economy(P, "Source", "cur" .. i, 1, 1, "Gameplay", "sku")
	end
	t.eq(#env.calls, 5)
	local a2, env3 = make({ maxPerMinute = 100000 })
	for i = 1, 21 do
		a2:Economy(P, "Source", "cur1", 1, 1, "tx" .. i, "sku")
	end
	t.eq(#env3.calls, 20)
	local b, env2 = make({ maxPerMinute = 100000 })
	for i = 1, 105 do
		b:Economy(P, "Source", "cur1", 1, 1, "tx1", "sku" .. i)
	end
	t.eq(#env2.calls, 100)
end)

t.test("onboarding: each step is sent once per player, out-of-range rejected", function()
	local a, env = make()
	t.truthy(a:Onboarding(P, 1, "Spawned"))
	t.falsy(a:Onboarding(P, 1, "Spawned"))
	t.truthy(a:Onboarding({ UserId = 8 }, 1, "Spawned"))
	t.falsy(a:Onboarding(P, 0, "bad"))
	t.falsy(a:Onboarding(P, 101, "bad"))
	t.falsy(a:Onboarding(P, 2.5, "bad"))
	t.eq(#env.calls, 2)
	a:ClearPlayer(P)
	t.truthy(a:Onboarding(P, 1, "Spawned"))
end)

t.test("funnel: dedupes per session, caps funnels at 10", function()
	local a, env = make()
	t.truthy(a:Funnel(P, "Shop", "s1", 1, "Open"))
	t.falsy(a:Funnel(P, "Shop", "s1", 1, "Open"))
	t.truthy(a:Funnel(P, "Shop", "s2", 1, "Open"))
	for i = 1, 12 do
		a:Funnel(P, "f" .. i, "s", 1, "Open")
	end
	local funnels = {}
	for _, c in env.calls do
		funnels[c.args[2]] = true
	end
	local n = 0
	for _ in funnels do
		n += 1
	end
	t.eq(n, 10)
end)

t.test("progression: path rules and status mapping", function()
	local a, env = make()
	t.truthy(a:Progression(P, "World1", "Complete", 3, "Level 3"))
	t.eq(env.calls[1].args[3], "P_COMPLETE")
	t.falsy(a:Progression(P, "bad,path", "Start", 1, "x"))
	t.falsy(a:Progression(P, "bad'path", "Start", 1, "x"))
	t.falsy(a:Progression(P, "", "Start", 1, "x"))
	t.falsy(a:Progression(P, "World1", "Weird" :: any, 1, "x"))
end)

t.test("custom events: value default 1, fields filtered to allowed keys", function()
	local a, env = make()
	t.truthy(a:Custom(P, "BossKilled", nil, { CF1 = "Dragon", evil = "x", CF2 = 5 :: any }))
	local c = env.calls[1]
	t.eq(c.args[3], 1)
	t.eq(c.args[4], { CF1 = "Dragon" })
	t.falsy(a:Custom(P, "", 1))
	t.falsy(a:Custom(P, "x", math.huge))
end)

t.test("rate limit: per player per event per minute, resets after 60 s", function()
	local a, env = make({ maxPerMinute = 3 })
	for _ = 1, 10 do
		a:Custom(P, "Tick", 1)
	end
	t.eq(#env.calls, 3)
	t.truthy(a:Custom({ UserId = 9 }, "Tick", 1)) -- other player unaffected
	env.clock += 61
	t.truthy(a:Custom(P, "Tick", 1))
end)

t.test("a failing AnalyticsService never throws into game code", function()
	local a, env = make()
	env.fail = true
	t.falsy(a:Custom(P, "x", 1))
	t.truthy(string.find(env.logs[1], "LogCustomEvent failed"))
end)

t.done()
