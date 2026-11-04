--!nocheck
local t = require("../../../../../systems/_check/harness")
local RedeemService = require("../RedeemService")
local CodeBook = require("../../../../marketing/codes-campaign-planner/scripts/CodeBook")

local function setup(grantResult)
	local used = {}
	local log = {}
	local granted = {}
	local clock = 1000
	local svc = RedeemService.new({
		checker = CodeBook,
		book = {
			["EGG-ABC123"] = { reward = "Coins500", creator = "ethan", maxUses = 2 },
			["OPEN"] = { reward = "Hat" },
		},
		store = {
			read = function(code)
				return used[code] or 0
			end,
			take = function(code, maxUses)
				local n = used[code] or 0
				if maxUses and n >= maxUses then
					return false
				end
				used[code] = n + 1
				return true
			end,
			release = function(code)
				used[code] = (used[code] or 1) - 1
			end,
		},
		now = function()
			return clock
		end,
		grant = function(userId, code)
			if grantResult == false then
				return false
			end
			table.insert(granted, userId .. ":" .. code)
			return true
		end,
		markRedeemed = function() end,
		log = function(event, userId, fields)
			table.insert(log, { event = event, userId = userId, fields = fields })
		end,
	})
	return svc, used, log, granted, function(dt)
		clock += dt
	end
end

t.test("a valid code grants once, counts a use and logs without the typed text", function()
	local svc, used, log, granted = setup()
	local mine = {}
	local r = svc:Redeem(1, "  egg-abc123 ", mine)
	t.eq(r.ok, true)
	t.eq(r.reward, "Coins500")
	t.eq(used["EGG-ABC123"], 1)
	t.eq(granted[1], "1:EGG-ABC123")
	t.eq(mine["EGG-ABC123"], true)
	t.eq(log[1].event, "redeem_ok")
	t.eq(log[1].fields.creator, "ethan")
end)

t.test("the same player cannot redeem twice", function()
	local svc = setup()
	local mine = {}
	svc:Redeem(1, "OPEN", mine)
	local r = svc:Redeem(1, "OPEN", mine)
	t.eq(r.ok, false)
	t.eq(r.reason, "already_redeemed")
end)

t.test("global cap: the third player is refused and the counter stays at the cap", function()
	local svc, used = setup()
	t.eq(svc:Redeem(1, "EGG-ABC123", {}).ok, true)
	t.eq(svc:Redeem(2, "EGG-ABC123", {}).ok, true)
	local r = svc:Redeem(3, "EGG-ABC123", {})
	t.eq(r.reason, "used_up")
	t.eq(used["EGG-ABC123"], 2)
end)

t.test("a failed grant gives the use back and does not mark the player", function()
	local svc, used = setup(false)
	local mine = {}
	local r = svc:Redeem(1, "EGG-ABC123", mine)
	t.eq(r.reason, "grant_failed")
	t.eq(used["EGG-ABC123"], 0)
	t.eq(mine["EGG-ABC123"], nil)
end)

t.test("wrong guesses are throttled after five, then allowed again after the window", function()
	local svc, _, _, _, advance = setup()
	for i = 1, 5 do
		t.eq(svc:Redeem(9, "NOPE" .. i, {}).reason, "unknown")
	end
	t.eq(svc:Redeem(9, "OPEN", {}).reason, "slow_down")
	advance(61)
	t.eq(svc:Redeem(9, "OPEN", {}).ok, true)
end)

t.test("junk input and a throwing store never error out to the caller", function()
	local svc = setup()
	t.eq(svc:Redeem(1, 12345, {}).reason, "invalid")
	local broken = RedeemService.new({
		checker = CodeBook,
		book = { ["OPEN"] = { reward = "Hat" } },
		store = {
			read = function()
				error("datastore down")
			end,
			take = function()
				error("datastore down")
			end,
			release = function() end,
		},
		now = function()
			return 1
		end,
		grant = function()
			return true
		end,
		markRedeemed = function() end,
	})
	t.eq(broken:Redeem(1, "OPEN", {}).reason, "error")
	t.eq(broken:Redeem(1, "OPEN", {}).reason, "error")
end)

t.done()
