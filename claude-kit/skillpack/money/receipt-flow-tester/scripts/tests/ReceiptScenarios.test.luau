--!nocheck
local t = require("../../../../../systems/_check/harness")
local Shop = require("../../../../../systems/Shop/src/Shop")
local ReceiptScenarios = require("../ReceiptScenarios")

local function goodEnv()
	local env = { data = { [1] = { coins = 0, Receipts = {} } }, loaded = true, saveOk = true, clock = 0 }
	local shop = Shop.new({
		products = {
			[111] = {
				name = "Coins100",
				grant = function(_, data)
					data.coins += 100
					return true
				end,
			},
		},
		getData = function(uid)
			if not env.loaded then
				return nil
			end
			return env.data[uid]
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
		shop = shop,
		reward = function()
			return env.data[1].coins
		end,
		setLoaded = function(v)
			env.loaded = v
		end,
		setSaveOk = function(v)
			env.saveOk = v
		end,
		productId = 111,
		userId = 1,
		expectedDelta = 100,
	}
end

local function brokenEnv()
	local coins = 0
	local shop = {
		ProcessReceipt = function(_, r)
			if r.ProductId ~= 111 then
				return "Granted"
			end
			coins += 100
			return "Granted"
		end,
	}
	return {
		shop = shop,
		reward = function()
			return coins
		end,
		setLoaded = function() end,
		setSaveOk = function() end,
		productId = 111,
		userId = 1,
		expectedDelta = 100,
	}
end

t.test("the kit Shop passes every scenario", function()
	local results = ReceiptScenarios.run(goodEnv)
	t.eq(#results, #ReceiptScenarios.names())
	for _, r in results do
		t.truthy(r.pass, r.name .. " -> " .. r.detail)
	end
	t.truthy(ReceiptScenarios.allPassed(results))
end)

t.test("a naive handler fails the duplicate, unloaded, save-failure and unknown-product scenarios", function()
	local results = ReceiptScenarios.run(brokenEnv)
	local failed = {}
	for _, r in results do
		if not r.pass then
			table.insert(failed, r.name)
		end
	end
	t.eq(#failed, 4)
	t.falsy(ReceiptScenarios.allPassed(results))
end)

t.test("an error inside a scenario is reported as a failure, not thrown", function()
	local results = ReceiptScenarios.run(function()
		error("factory broke")
	end)
	t.falsy(results[1].pass)
	t.truthy(string.find(results[1].detail, "factory broke", 1, true))
end)

t.done()
