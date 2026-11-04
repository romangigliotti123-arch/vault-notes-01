--!nocheck
local t = require("../../../../../systems/_check/harness")
local Wallet = require("../../../currency-system-builder/scripts/Wallet")
local UpgradeTree = require("../UpgradeTree")

local wallet = Wallet.new({ currencies = { Coins = {} } })
local function make()
	return UpgradeTree.new({
		wallet = wallet,
		currency = "Coins",
		refund = 0.5,
		nodes = {
			speed = { cost = 100, growth = 2, maxLevel = 3 },
			dash = { cost = 500, maxLevel = 1, requires = { speed = 2 } },
		},
	})
end

t.test("costs grow per level and buying spends on the server wallet", function()
	local d, tree = {}, make()
	wallet:add(d, "Coins", 1000, "x")
	t.eq(tree:costOf("speed", 0), 100)
	t.eq(tree:costOf("speed", 2), 400)
	t.truthy((tree:buy(d, "speed")))
	t.eq(wallet:balance(d, "Coins"), 900)
	t.eq(tree:level(d, "speed"), 1)
end)

t.test("prerequisites and max level are enforced", function()
	local d, tree = {}, make()
	wallet:add(d, "Coins", 100000, "x")
	local ok, why = tree:buy(d, "dash")
	t.falsy(ok)
	t.eq(why, "requires speed")
	tree:buy(d, "speed")
	tree:buy(d, "speed")
	t.truthy((tree:buy(d, "dash")))
	tree:buy(d, "speed")
	local _, why2 = tree:buy(d, "speed")
	t.eq(why2, "max level")
end)

t.test("cannot afford changes nothing", function()
	local d, tree = {}, make()
	wallet:add(d, "Coins", 99, "x")
	t.falsy((tree:buy(d, "speed")))
	t.eq(wallet:balance(d, "Coins"), 99)
	t.eq(tree:level(d, "speed"), 0)
end)

t.test("respec refunds a floored share and never creates currency", function()
	local d, tree = {}, make()
	wallet:add(d, "Coins", 1000, "x")
	tree:buy(d, "speed")
	tree:buy(d, "speed")
	local before = wallet:balance(d, "Coins")
	t.eq(tree:spentTotal(d), 300)
	t.eq(tree:respec(d), 150)
	t.eq(wallet:balance(d, "Coins"), before + 150)
	t.eq(tree:level(d, "speed"), 0)
	t.truthy(wallet:balance(d, "Coins") < 1000)
end)

t.test("config errors: unknown or unreachable prerequisite and cycles", function()
	local w = wallet
	local function build(nodes)
		return pcall(UpgradeTree.new, { wallet = w, currency = "Coins", nodes = nodes })
	end
	t.falsy((build({ a = { cost = 1, maxLevel = 1, requires = { zz = 1 } } })))
	t.falsy((build({ a = { cost = 1, maxLevel = 1 }, b = { cost = 1, maxLevel = 1, requires = { a = 2 } } })))
	t.falsy((build({
		a = { cost = 1, maxLevel = 1, requires = { b = 1 } },
		b = { cost = 1, maxLevel = 1, requires = { a = 1 } },
	})))
end)

t.done()
