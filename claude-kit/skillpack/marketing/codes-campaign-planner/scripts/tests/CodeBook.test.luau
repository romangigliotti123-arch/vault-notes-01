--!nocheck
local t = require("../../../../../systems/_check/harness")
local CodeBook = require("../CodeBook")

local book = {
	["EGG-ABC123"] = { reward = "Coins500", creator = "ethan", maxUses = 2, expiresAt = 2000 },
	["LAUNCH"] = { reward = "Pet", startsAt = 100 },
}

local function fresh()
	return { used = 0, mine = {} }
end

t.test("normalise forgives case and spaces, refuses junk", function()
	t.eq(CodeBook.normalise("  egg-abc 123 "), "EGG-ABC123")
	t.eq(CodeBook.normalise(""), nil)
	t.eq(CodeBook.normalise("a;b"), nil)
	t.eq(CodeBook.normalise(5), nil)
	t.eq(CodeBook.normalise(string.rep("A", 65)), nil)
end)

t.test("a valid code passes and returns the entry", function()
	local r = CodeBook.check(book, "egg-abc123", fresh(), 1000)
	t.truthy(r.ok)
	t.eq(r.code, "EGG-ABC123")
	t.eq(r.entry.reward, "Coins500")
end)

t.test("unknown and not-yet-started look the same to the player", function()
	t.eq(CodeBook.check(book, "NOPE", fresh(), 1000).reason, "unknown")
	t.eq(CodeBook.check(book, "LAUNCH", fresh(), 50).reason, "unknown")
	t.truthy(CodeBook.check(book, "LAUNCH", fresh(), 100).ok)
end)

t.test("expiry is exclusive", function()
	t.truthy(CodeBook.check(book, "EGG-ABC123", fresh(), 1999).ok)
	t.eq(CodeBook.check(book, "EGG-ABC123", fresh(), 2000).reason, "expired")
end)

t.test("per-player and global limits", function()
	local s = fresh()
	s.mine["EGG-ABC123"] = true
	t.eq(CodeBook.check(book, "EGG-ABC123", s, 1000).reason, "already_redeemed")
	local g = fresh()
	g.used = 2
	t.eq(CodeBook.check(book, "EGG-ABC123", g, 1000).reason, "used_up")
	g.used = 1
	t.truthy(CodeBook.check(book, "EGG-ABC123", g, 1000).ok)
end)

t.test("validateBook catches typos before launch", function()
	t.eq(#CodeBook.validateBook(book), 0)
	local bad = {
		["egg"] = { reward = "x" },
		["OK"] = { reward = "" },
		["TIME"] = { reward = "x", startsAt = 10, expiresAt = 5 },
		["USES"] = { reward = "x", maxUses = 0 },
	}
	t.eq(#CodeBook.validateBook(bad), 4)
end)

t.done()
