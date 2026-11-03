--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/currency-system-builder/scripts/tests/Wallet.test.luau
local t = require("../../../../../systems/_check/harness")
local Shop = require("../../../../../systems/Shop/src/Shop")
local Wallet = require("../Wallet")

local function make()
	return Wallet.new({ currencies = { Coins = { max = 1000 }, Gems = { start = 5 } } })
end

t.test("init gives start balances", function()
	local data = {}
	local w = make()
	t.eq(w:balance(data, "Coins"), 0)
	t.eq(w:balance(data, "Gems"), 5)
end)

t.test("rejects negative, zero, fractional, NaN, huge and unknown", function()
	local data, w = {}, make()
	for _, bad in { -5, 0, 1.5, 0 / 0, 1e15 } do
		local ok = w:add(data, "Coins", bad, "x")
		t.falsy(ok, "add " .. tostring(bad))
		t.falsy((w:spend(data, "Coins", bad, "x")))
	end
	t.falsy((w:add(data, "Cash", 1, "x")))
	t.eq(w:balance(data, "Coins"), 0)
end)

t.test("spend is all or nothing", function()
	local data, w = {}, make()
	w:add(data, "Coins", 30, "quest")
	local ok, why = w:spend(data, "Coins", 31, "shop")
	t.falsy(ok)
	t.eq(why, "insufficient")
	t.eq(w:balance(data, "Coins"), 30)
	t.truthy((w:spend(data, "Coins", 30, "shop")))
	t.eq(w:balance(data, "Coins"), 0)
end)

t.test("cap clamps and reports", function()
	local data, w = {}, make()
	local ok, why = w:add(data, "Coins", 5000, "drop")
	t.truthy(ok)
	t.eq(why, "capped")
	t.eq(w:balance(data, "Coins"), 1000)
end)

t.test("same key twice pays once", function()
	local data, w = {}, make()
	w:add(data, "Gems", 10, "pack", "purchase-1")
	local ok, why = w:add(data, "Gems", 10, "pack", "purchase-1")
	t.truthy(ok)
	t.eq(why, "duplicate")
	t.eq(w:balance(data, "Gems"), 15)
end)

t.test("key list is bounded", function()
	local data = {}
	local w = Wallet.new({ currencies = { Coins = {} }, keyLimit = 3 })
	for i = 1, 10 do
		w:add(data, "Coins", 1, "s", "k" .. i)
	end
	t.eq(#data.Wallet.keys, 3)
end)

t.test("report tracks sources and sinks", function()
	local data, w = {}, make()
	w:add(data, "Coins", 100, "quest")
	w:spend(data, "Coins", 40, "shop")
	local r = w:report(data)
	t.eq(r.sources.quest, 100)
	t.eq(r.sinks.shop, 40)
end)

t.test("works as a real Shop product grant: a retried receipt pays once", function()
	local data = { Receipts = {} }
	local w = make()
	local shop = Shop.new({
		products = {
			[77] = {
				name = "Gems10",
				grant = function(_, d)
					return (w:add(d, "Gems", 10, "robux:Gems10"))
				end,
			},
		},
		getData = function()
			return data
		end,
		saveNow = function()
			return true
		end,
		ownsPass = function()
			return false
		end,
		now = function()
			return 0
		end,
		wait = function() end,
	})
	local receipt = { PlayerId = 1, PurchaseId = "p-1", ProductId = 77 }
	t.eq(shop:ProcessReceipt(receipt), "Granted")
	t.eq(shop:ProcessReceipt(receipt), "Granted")
	t.eq(w:balance(data, "Gems"), 15)
end)

t.done()
