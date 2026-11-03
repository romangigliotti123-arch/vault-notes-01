--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/trading-system-builder/scripts/tests/Trade.test.luau
local t = require("../../../../../systems/_check/harness")
local Inventory = require("../../../inventory-system-builder/scripts/Inventory")
local Wallet = require("../../../currency-system-builder/scripts/Wallet")
local Trade = require("../Trade")

local uidN, idN, clock = 0, 0, 100
local inv = Inventory.new({
	capacity = 4,
	newUid = function()
		uidN += 1
		return "u" .. uidN
	end,
	items = { Wood = { stack = 10, tradable = true }, Sword = { stack = 1, tradable = true }, Bound = { stack = 1 } },
})
local wallet = Wallet.new({ currencies = { Coins = {} } })

local function world()
	local datas = { [1] = {}, [2] = {} }
	local logs = {}
	local equipped = {}
	local trade = Trade.new({
		inventory = inv,
		wallet = wallet,
		currency = "Coins",
		getData = function(u)
			return datas[u]
		end,
		now = function()
			return clock
		end,
		newId = function()
			idN += 1
			return "t" .. idN
		end,
		lockSeconds = 2,
		log = function(e)
			table.insert(logs, e)
		end,
		locked = function(_, uid)
			return equipped[uid] == true
		end,
	})
	return trade, datas, logs, equipped
end

-- total of everything in the world, used to prove nothing is created or destroyed
local function totals(datas)
	local wood, swords, coins, uids = 0, 0, 0, {}
	for _, d in datas do
		wood += inv:count(d, "Wood")
		swords += inv:count(d, "Sword")
		coins += wallet:balance(d, "Coins")
		for _, u in inv:uids(d) do
			uids[u] = (uids[u] or 0) + 1
		end
	end
	for _, c in uids do
		t.eq(c, 1, "uid appears once")
	end
	return { wood, swords, coins }
end

local function setup()
	local trade, datas, logs, equipped = world()
	inv:add(datas[1], "Wood", 10)
	inv:add(datas[1], "Sword", 1)
	wallet:add(datas[1], "Coins", 100, "test")
	inv:add(datas[2], "Wood", 3)
	wallet:add(datas[2], "Coins", 50, "test")
	return trade, datas, logs, equipped
end

local function accepted(trade, id)
	clock += 5
	local v = trade:version(id)
	trade:accept(id, 1, v)
	return trade:accept(id, 2, v)
end

t.test("happy path swaps items and coins, keeps the uid, conserves totals", function()
	local trade, datas, logs = setup()
	local before = totals(datas)
	local sword = inv:uids(datas[1])[1]
	local id = trade:open(1, 2)
	t.truthy(trade:setOffer(id, 1, { items = { { uid = sword }, { id = "Wood", qty = 4 } }, coins = 30 }))
	t.truthy(trade:setOffer(id, 2, { items = { { id = "Wood", qty = 1 } }, coins = 0 }))
	t.eq((accepted(trade, id)), "done")
	t.truthy(inv:findUid(datas[2], sword))
	t.eq(inv:findUid(datas[1], sword), nil)
	t.eq(inv:count(datas[1], "Wood"), 7)
	t.eq(inv:count(datas[2], "Wood"), 6)
	t.eq(wallet:balance(datas[2], "Coins"), 80)
	t.eq(totals(datas), before)
	t.eq(logs[#logs].event, "trade_done")
end)

t.test("changing an offer after accepting resets accepts and invalidates the old version", function()
	local trade, datas = setup()
	local id = trade:open(1, 2)
	trade:setOffer(id, 1, { items = { { id = "Wood", qty = 1 } }, coins = 0 })
	clock += 5
	local v = trade:version(id)
	trade:accept(id, 1, v)
	trade:setOffer(id, 1, { items = { { id = "Wood", qty = 9 } }, coins = 0 })
	local state, why = trade:accept(id, 2, v)
	t.eq(state, "error")
	t.eq(why, "offer changed")
	t.eq(inv:count(datas[1], "Wood"), 10)
end)

t.test("accept is refused inside the lock window after an offer change", function()
	local trade = setup()
	local id = trade:open(1, 2)
	trade:setOffer(id, 1, { items = {}, coins = 1 })
	local state, why = trade:accept(id, 1, trade:version(id))
	t.eq(state, "error")
	t.eq(why, "locked")
end)

t.test(
	"offers are checked against the real inventory: not owned, not tradable, negative, fractional, too many",
	function()
		local trade, datas = setup()
		local id = trade:open(1, 2)
		inv:add(datas[1], "Bound", 1)
		local bound = inv:findUid(datas[1], inv:uids(datas[1])[2]) and inv:uids(datas[1])[2]
		local bad = {
			{ items = { { uid = "forged" } }, coins = 0 },
			{ items = { { id = "Wood", qty = 11 } }, coins = 0 },
			{ items = { { id = "Wood", qty = -1 } }, coins = 0 },
			{ items = { { id = "Wood", qty = 1.5 } }, coins = 0 },
			{ items = { { id = "Bound", qty = 1 } }, coins = 0 },
			{ items = { { id = "Wood", qty = 6 }, { id = "Wood", qty = 6 } }, coins = 0 },
			{ items = {}, coins = -5 },
			{ items = {}, coins = 101 },
			{ items = {}, coins = 0 / 0 },
			{
				items = {
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
					{ id = "Wood", qty = 1 },
				},
				coins = 0,
			},
		}
		for i, offer in bad do
			t.falsy((trade:setOffer(id, 1, offer)), "bad offer " .. i)
		end
		t.falsy(bound == nil)
		t.falsy((trade:setOffer(id, 1, { items = { { uid = bound } }, coins = 0 })))
	end
)

t.test("same uid offered twice is refused", function()
	local trade, datas = setup()
	local sword = inv:uids(datas[1])[1]
	local id = trade:open(1, 2)
	t.falsy((trade:setOffer(id, 1, { items = { { uid = sword }, { uid = sword } }, coins = 0 })))
end)

t.test("item sold or dropped after the offer is caught at commit; nothing moves", function()
	local trade, datas = setup()
	local before = totals(datas)
	local id = trade:open(1, 2)
	trade:setOffer(id, 1, { items = { { id = "Wood", qty = 10 } }, coins = 0 })
	trade:setOffer(id, 2, { items = {}, coins = 10 })
	inv:remove(datas[1], "Wood", 5)
	before[1] -= 5
	t.eq((accepted(trade, id)), "error")
	t.eq(totals(datas), before)
	t.eq(trade:sessionOf(1), nil)
end)

t.test("receiver without room: rollback restores both sides exactly", function()
	local trade, datas = setup()
	for _ = 1, 3 do
		inv:add(datas[2], "Sword", 1)
	end
	inv:add(datas[2], "Wood", 7)
	t.eq(inv:freeSlots(datas[2]), 0)
	local snapshot = { inv:count(datas[1], "Wood"), inv:count(datas[2], "Wood"), wallet:balance(datas[1], "Coins") }
	local before = totals(datas)
	local id = trade:open(1, 2)
	trade:setOffer(id, 1, { items = { { id = "Wood", qty = 10 } }, coins = 20 })
	trade:setOffer(id, 2, { items = {}, coins = 0 })
	t.eq((accepted(trade, id)), "error")
	t.eq(totals(datas), before)
	t.eq({ inv:count(datas[1], "Wood"), inv:count(datas[2], "Wood"), wallet:balance(datas[1], "Coins") }, snapshot)
end)

t.test("a finished trade cannot be replayed (double accept is refused)", function()
	local trade, datas = setup()
	local id = trade:open(1, 2)
	trade:setOffer(id, 1, { items = {}, coins = 10 })
	local v = trade:version(id)
	t.eq((accepted(trade, id)), "done")
	local state = trade:accept(id, 1, v)
	t.eq(state, "error")
	t.eq(wallet:balance(datas[2], "Coins"), 60)
end)

t.test("one trade per player; leaving cancels and frees both", function()
	local trade = setup()
	local id = trade:open(1, 2)
	t.eq(trade:open(1, 2), nil)
	trade:playerLeft(2)
	t.eq(trade:sessionOf(1), nil)
	t.eq(trade:setOffer(id, 1, { items = {}, coins = 0 }), false)
end)

t.test("locked (equipped) items cannot be offered", function()
	local trade, datas, _, equipped = setup()
	local sword = inv:uids(datas[1])[1]
	equipped[sword] = true
	local id = trade:open(1, 2)
	local ok, why = trade:setOffer(id, 1, { items = { { uid = sword } }, coins = 0 })
	t.falsy(ok)
	t.eq(why, "item is locked")
end)

t.done()
