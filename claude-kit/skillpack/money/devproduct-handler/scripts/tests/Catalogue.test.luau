--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/money/devproduct-handler/scripts/tests/Catalogue.test.luau
local t = require("../../../../../systems/_check/harness")
local Shop = require("../../../../../systems/Shop/src/Shop")
local Catalogue = require("../Catalogue")

local TEMPLATE = { coins = 0, inventory = {}, Receipts = {} }

local function entries()
	return {
		{
			name = "Coins100",
			id = 111,
			grant = function(_uid, data)
				data.coins += 100
				return true
			end,
		},
		{
			name = "Slot",
			id = 222,
			grant = function(_uid, data)
				if #data.inventory >= 3 then
					return false
				end
				table.insert(data.inventory, "slot")
				return true
			end,
			refuseWith = { inventory = { 1, 2, 3 }, Receipts = {} },
		},
		{
			name = "Draft",
			id = 0,
			grant = function(_uid, data)
				data.coins += 1
				return true
			end,
		},
	}
end

t.test("build skips id 0 with a note and keys by id", function()
	local products, notes = Catalogue.build(entries())
	t.truthy(products[111] and products[222])
	t.eq(products[0], nil)
	t.eq(#notes, 1)
end)

t.test("duplicate id or name is an error", function()
	local dupId = entries()
	dupId[2].id = 111
	t.falsy(pcall(Catalogue.build, dupId))
	local dupName = entries()
	dupName[2].name = "Coins100"
	t.falsy(pcall(Catalogue.build, dupName))
end)

t.test("verify accepts good grants", function()
	t.eq(Catalogue.verify(entries(), TEMPLATE), {})
end)

t.test("verify flags a throwing grant, a no-op, a bad value and a refuse-after-change", function()
	local bad = {
		{
			name = "Throws",
			id = 1,
			grant = function()
				error("x")
			end,
		},
		{
			name = "NoOp",
			id = 2,
			grant = function()
				return true
			end,
		},
		{
			name = "Func",
			id = 3,
			grant = function(_u, d)
				d.cb = function() end
				return true
			end,
		},
		{
			name = "Sloppy",
			id = 4,
			grant = function(_u, d)
				d.coins += 1
				return false
			end,
			refuseWith = { coins = 0 },
		},
	}
	-- Throws 1, NoOp 1, Func 1, Sloppy 2 (fresh grant returns false, and it changed data before refusing)
	t.eq(#Catalogue.verify(bad, TEMPLATE), 5)
end)

t.test("end to end through the real Shop: duplicate PurchaseId grants once", function()
	local products = Catalogue.build(entries())
	local data = { coins = 0, inventory = {}, Receipts = {} }
	local clock = 0
	local shop = Shop.new({
		products = products,
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
			clock += 1
			return clock
		end,
		wait = function() end,
	})
	t.eq(shop:ProcessReceipt({ PlayerId = 1, PurchaseId = "p1", ProductId = 111 }), "Granted")
	t.eq(shop:ProcessReceipt({ PlayerId = 1, PurchaseId = "p1", ProductId = 111 }), "Granted")
	t.eq(data.coins, 100)
	t.eq(shop:ProcessReceipt({ PlayerId = 1, PurchaseId = "p2", ProductId = 999 }), "NotYet")
end)

t.done()
