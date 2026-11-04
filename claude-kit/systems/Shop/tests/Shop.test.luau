--!nocheck
local t = require("../../_check/harness")
local Shop = require("../src/Shop")

local function make(over)
	local env = {
		data = { [1] = { coins = 0, Receipts = {} } },
		saves = 0,
		saveOk = true,
		clock = 1000,
		owned = {},
		ownsErrors = 0,
		granted = {},
		waits = {},
	}
	local cfg = {
		products = {
			[111] = {
				name = "Coins100",
				grant = function(uid, data)
					data.coins += 100
					table.insert(env.granted, uid)
					return true
				end,
			},
			[222] = {
				name = "Broken",
				grant = function()
					error("boom")
				end,
			},
			[333] = {
				name = "Refuses",
				grant = function()
					return false
				end,
			},
		},
		passes = {
			[900] = {
				name = "VIP",
				onOwned = function(uid)
					env.vipFor = (env.vipFor or 0) + 1
				end,
			},
		},
		getData = function(uid)
			return env.data[uid]
		end,
		saveNow = function()
			env.saves += 1
			return env.saveOk
		end,
		ownsPass = function(uid, pass)
			if env.ownsErrors > 0 then
				env.ownsErrors -= 1
				error("http 500")
			end
			return env.owned[uid .. ":" .. pass] == true
		end,
		now = function()
			env.clock += 1
			return env.clock
		end,
		wait = function(s)
			table.insert(env.waits, s)
		end,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return Shop.new(cfg), env
end

local function rc(id, product, uid)
	return { PlayerId = uid or 1, PurchaseId = id, ProductId = product or 111 }
end

print("Shop")

t.test("grants once, records the receipt, saves, answers Granted", function()
	local s, env = make()
	t.eq(s:ProcessReceipt(rc("a")), "Granted")
	t.eq(env.data[1].coins, 100)
	t.truthy(env.data[1].Receipts.a)
	t.eq(env.saves, 1)
end)

t.test("the same PurchaseId delivered again never grants twice", function()
	local s, env = make()
	s:ProcessReceipt(rc("a"))
	t.eq(s:ProcessReceipt(rc("a")), "Granted")
	t.eq(s:ProcessReceipt(rc("a")), "Granted")
	t.eq(env.data[1].coins, 100)
	t.eq(#env.granted, 1)
end)

t.test("player data not loaded: NotYet, nothing granted", function()
	local s, env = make()
	t.eq(s:ProcessReceipt(rc("a", 111, 2)), "NotYet")
	t.eq(#env.granted, 0)
end)

t.test("unknown product: NotYet and nothing recorded", function()
	local s, env = make()
	t.eq(s:ProcessReceipt(rc("a", 999)), "NotYet")
	t.eq(next(env.data[1].Receipts), nil)
end)

t.test("grant error or refusal: NotYet and no receipt recorded", function()
	local s, env = make()
	t.eq(s:ProcessReceipt(rc("a", 222)), "NotYet")
	t.eq(s:ProcessReceipt(rc("b", 333)), "NotYet")
	t.eq(next(env.data[1].Receipts), nil)
	t.eq(env.saves, 0)
end)

t.test("save failure: NotYet; retry returns Granted without a second grant", function()
	local s, env = make()
	env.saveOk = false
	t.eq(s:ProcessReceipt(rc("a")), "NotYet")
	t.eq(env.data[1].coins, 100)
	env.saveOk = true
	t.eq(s:ProcessReceipt(rc("a")), "Granted")
	t.eq(env.data[1].coins, 100)
end)

t.test("missing Receipts table in the data template is reported, never silently granted", function()
	local s, env = make()
	env.data[1].Receipts = nil
	t.eq(s:ProcessReceipt(rc("a")), "NotYet")
	t.eq(env.data[1].coins, 0)
end)

t.test("receipts are pruned to the newest maxReceipts", function()
	local s, env = make({ maxReceipts = 3 })
	for i = 1, 6 do
		s:ProcessReceipt(rc("r" .. i))
	end
	local n, ids = 0, {}
	for id in env.data[1].Receipts do
		n += 1
		ids[id] = true
	end
	t.eq(n, 3)
	t.truthy(ids.r6 and ids.r5 and ids.r4)
	t.eq(env.data[1].coins, 600)
end)

t.test("re-entrant delivery of the same receipt while a grant is in flight is deferred", function()
	local s, env
	local inner
	s, env = make({
		products = {
			[111] = {
				name = "Coins100",
				grant = function(uid, data)
					inner = s:ProcessReceipt(rc("a"))
					data.coins += 100
					return true
				end,
			},
		},
	})
	t.eq(s:ProcessReceipt(rc("a")), "Granted")
	t.eq(inner, "NotYet")
	t.eq(env.data[1].coins, 100)
end)

t.test("pass ownership: checked against Roblox on join, onOwned fires once", function()
	local s, env = make()
	env.owned["1:900"] = true
	s:RefreshPasses(1)
	s:RefreshPasses(1)
	t.truthy(s:HasPass(1, 900))
	t.eq(env.vipFor, 1)
	t.falsy(s:HasPass(2, 900))
end)

t.test("pass prompt finished: verified with Roblox, a spoofed wasPurchased grants nothing", function()
	local s, env = make()
	t.falsy(s:OnPassPromptFinished(1, 900, true))
	t.falsy(s:HasPass(1, 900))
	env.owned["1:900"] = true
	t.truthy(s:OnPassPromptFinished(1, 900, true))
	t.truthy(s:HasPass(1, 900))
	t.falsy(s:OnPassPromptFinished(1, 12345, true))
end)

t.test("ownership lookup errors are retried with backoff", function()
	local s, env = make()
	env.owned["1:900"] = true
	env.ownsErrors = 2
	s:RefreshPasses(1)
	t.truthy(s:HasPass(1, 900))
	t.eq(env.waits, { 1, 2 })
end)

t.test("ClearPlayer forgets passes; name lookups work", function()
	local s, env = make()
	env.owned["1:900"] = true
	s:RefreshPasses(1)
	s:ClearPlayer(1)
	t.falsy(s:HasPass(1, 900))
	t.eq(s:ProductIdByName("Coins100"), 111)
	t.eq(s:PassIdByName("VIP"), 900)
	t.eq(s:ProductIdByName("nope"), nil)
end)

t.done()
