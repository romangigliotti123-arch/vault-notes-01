--!nocheck
local t = require("../../../../../systems/_check/harness")
local Migrations = require("../Migrations")

local TEMPLATE = { coins = 0, gems = 0, inventory = {}, settings = { music = true, sfx = true }, Receipts = {} }

local MIGRATIONS = {
	[1] = function(d)
		if d.money then
			d.coins = d.money
			d.money = nil
		end
		return d
	end,
	[2] = function(d)
		d.gems = d.gems or 0
		return d
	end,
}

t.test("old record is migrated step by step and keeps unknown keys", function()
	local rec = { v = 1, data = { money = 250, inventory = { "a" }, futureField = "keep" } }
	local d, err = Migrations.migrate(rec, 3, MIGRATIONS, TEMPLATE)
	t.eq(err, nil)
	t.eq(d.coins, 250)
	t.eq(d.money, nil)
	t.eq(d.futureField, "keep")
	t.eq(d.gems, 0)
	t.eq(rec.data.money, 250, "input must not be mutated")
end)

t.test("a record without v is treated as version 1", function()
	local d = Migrations.migrate({ data = { money = 5 } }, 2, MIGRATIONS, TEMPLATE)
	t.eq(d.coins, 5)
end)

t.test("record from a newer schema is refused", function()
	local d, err = Migrations.migrate({ v = 9, data = {} }, 3, MIGRATIONS, TEMPLATE)
	t.eq(d, nil)
	t.eq(err, "newer")
end)

t.test("missing migration is an error, not a skip", function()
	local d, err = Migrations.migrate({ v = 1, data = {} }, 4, MIGRATIONS, TEMPLATE)
	t.eq(d, nil)
	t.eq(err, "missing migration 3")
	t.eq(Migrations.missingSteps(1, 4, MIGRATIONS), { 3 })
	t.eq(Migrations.missingSteps(1, 3, MIGRATIONS), {})
end)

t.test("a throwing migration reports which one failed", function()
	local bad = {
		[1] = function()
			error("boom")
		end,
	}
	local d, err = Migrations.migrate({ v = 1, data = {} }, 2, bad, TEMPLATE)
	t.eq(d, nil)
	t.truthy(string.find(err, "migration 1 failed", 1, true))
end)

t.test("reconcile fills nested defaults but leaves arrays alone", function()
	local d = Migrations.migrate(
		{ v = 3, data = { settings = { music = false }, inventory = { "x", "y" } } },
		3,
		MIGRATIONS,
		TEMPLATE
	)
	t.eq(d.settings.music, false)
	t.eq(d.settings.sfx, true)
	t.eq(d.inventory, { "x", "y" })
	t.eq(d.Receipts, {})
end)

t.test("validateTemplate accepts a normal template", function()
	t.eq(Migrations.validateTemplate(TEMPLATE), {})
end)

t.test("validateTemplate flags unsaveable values and mixed tables", function()
	local bad = { fn = function() end, nan = 0 / 0, mixed = { 1, 2, name = "x" }, ok = 5 }
	local problems = Migrations.validateTemplate(bad)
	t.eq(#problems, 3)
end)

t.done()
