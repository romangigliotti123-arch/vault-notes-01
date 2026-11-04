--!nocheck
local t = require("../../../../../systems/_check/harness")
local Shop = require("../../../../../systems/Shop/src/Shop")
local PassCatalogue = require("../PassCatalogue")

local function entries(extra)
	local list = {
		{
			name = "VIP",
			id = 900,
			benefit = "2x daily reward",
			onOwned = function() end,
		},
		{ name = "Draft", id = 0, benefit = "not created yet" },
	}
	for _, e in extra or {} do
		table.insert(list, e)
	end
	return list
end

t.test("build keys by id and skips id 0 with a note", function()
	local passes, notes = PassCatalogue.build(entries())
	t.truthy(passes[900])
	t.eq(passes[0], nil)
	t.eq(#notes, 1)
end)

t.test("rejects duplicates, missing benefit and passes that gate core progress", function()
	t.falsy(pcall(PassCatalogue.build, entries({ { name = "VIP", id = 901, benefit = "x" } })))
	t.falsy(pcall(PassCatalogue.build, entries({ { name = "Other", id = 900, benefit = "x" } })))
	t.falsy(pcall(PassCatalogue.build, entries({ { name = "NoBenefit", id = 902, benefit = "" } })))
	t.falsy(
		pcall(
			PassCatalogue.build,
			entries({ { name = "Gate", id = 903, benefit = "unlock level 10", coreProgress = true } })
		)
	)
end)

t.test("listing hides ids", function()
	local list = PassCatalogue.listing(entries())
	t.eq(list[1], { name = "VIP", benefit = "2x daily reward" })
end)

t.test("through the real Shop: ownership comes from Roblox, not from wasPurchased", function()
	local owned = false
	local granted = 0
	local passes = PassCatalogue.build({
		{
			name = "VIP",
			id = 900,
			benefit = "x",
			onOwned = function()
				granted += 1
			end,
		},
	})
	local shop = Shop.new({
		products = {},
		passes = passes,
		getData = function()
			return nil
		end,
		saveNow = function()
			return true
		end,
		ownsPass = function()
			return owned
		end,
		now = function()
			return 0
		end,
		wait = function() end,
	})
	t.falsy(shop:OnPassPromptFinished(1, 900, true))
	t.eq(granted, 0)
	owned = true
	t.truthy(shop:OnPassPromptFinished(1, 900, true))
	t.truthy(shop:HasPass(1, 900))
	t.eq(granted, 1)
end)

t.done()
