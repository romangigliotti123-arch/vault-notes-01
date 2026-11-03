--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/purchase-flow-tester/scripts/tests/PurchaseScenarios.test.luau
-- Rigs the kit's REAL Shop module, then a deliberately naive grant-on-every-receipt handler to prove the scenarios can fail.
local t = require("../../../../../systems/_check/harness")
local PurchaseScenarios = require("../PurchaseScenarios")
local Shop = require("../../../../../systems/Shop/src/Shop")

local function shopRig()
	local env = { data = { [1] = { coins = 0, Receipts = {} } }, saveOk = true, clock = 1000, loaded = { [1] = true } }
	local shop = Shop.new({
		products = {
			[111] = {
				name = "Coins100",
				grant = function(_, data)
					data.coins += 100
					return true
				end,
			},
			[222] = {
				name = "Broken",
				grant = function()
					error("boom")
				end,
			},
		},
		getData = function(uid)
			if env.loaded[uid] then
				return env.data[uid]
			end
			return nil
		end,
		saveNow = function()
			return env.saveOk
		end,
		ownsPass = function()
			return false
		end,
		now = function()
			env.clock += 1
			return env.clock
		end,
		wait = function() end,
	})
	return {
		process = function(r)
			return shop:ProcessReceipt(r)
		end,
		coins = function(uid)
			return env.data[uid].coins
		end,
		setSaveOk = function(ok)
			env.saveOk = ok
		end,
		setDataLoaded = function(uid, loaded)
			env.loaded[uid] = loaded
		end,
		productId = 111,
		reward = 100,
		badProductId = 222,
		unknownProductId = 999,
	}
end

local function naiveRig()
	local data = { coins = 0 }
	local loaded = true
	return {
		process = function(r)
			if r.ProductId == 111 then
				data.coins += 100 -- no receipt record, no save check, no data check
			end
			return "Granted"
		end,
		coins = function()
			return data.coins
		end,
		setSaveOk = function() end,
		setDataLoaded = function(_, l)
			loaded = l
		end,
		productId = 111,
		reward = 100,
		badProductId = nil,
		unknownProductId = 999,
	}
end

print("PurchaseScenarios")

t.test("the kit Shop passes every scenario", function()
	local results = PurchaseScenarios.runAll(shopRig)
	t.eq(#results, 7)
	for _, r in results do
		t.truthy(r.ok, r.name .. " -> " .. r.detail)
	end
end)

t.test("a naive handler fails duplicate, save-failure, missing-data and unknown-product scenarios", function()
	local failed = {}
	for _, r in PurchaseScenarios.runAll(naiveRig) do
		if not r.ok then
			failed[r.name] = true
		end
	end
	t.truthy(failed["the same PurchaseId repeated never grants twice"])
	t.truthy(failed["a failed save answers NotYet, and the retry grants exactly once"])
	t.truthy(failed["player data not loaded answers NotYet and grants nothing"])
	t.truthy(failed["an unknown product id answers NotYet"])
end)

t.test("report counts passes", function()
	t.truthy(string.find(PurchaseScenarios.report(PurchaseScenarios.runAll(shopRig)), "7/7 scenarios passed", 1, true))
end)

t.done()
