--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/community/streamer-kit-builder/scripts/tests/StreamerAlias.test.luau
local t = require("../../../../../systems/_check/harness")
local StreamerAlias = require("../StreamerAlias")

t.test("alias is stable for the same id and salt", function()
	t.eq(StreamerAlias.alias(12345, "s1"), StreamerAlias.alias(12345, "s1"))
end)

t.test("alias changes with the salt and the id", function()
	t.truthy(StreamerAlias.alias(12345, "s1") ~= StreamerAlias.alias(12345, "s2"))
	t.truthy(StreamerAlias.alias(12345, "s1") ~= StreamerAlias.alias(12346, "s1"))
end)

t.test("alias shape: prefix, six look-alike-free symbols, never the id", function()
	for _, id in { 1, 99, 123456789, 4294967296 + 5, 987654321012 } do
		local a = StreamerAlias.alias(id, "x")
		t.truthy(string.match(a, "^Player%-[A-HJ-NP-Z2-9]+$") ~= nil, a)
		t.eq(#a, 13)
		t.falsy(string.find(a, tostring(id), 1, true))
	end
end)

t.test("a thousand-player server gets all-distinct aliases, whatever the input order", function()
	local ids = {}
	for i = 1, 1000 do
		table.insert(ids, 100000 + i * 7)
	end
	local a = StreamerAlias.uniqueAliases(ids, "salt")
	local rev = {}
	for i = #ids, 1, -1 do
		table.insert(rev, ids[i])
	end
	local b = StreamerAlias.uniqueAliases(rev, "salt")
	local seen, n = {}, 0
	for id, al in a do
		t.eq(b[id], al)
		t.falsy(seen[al], "duplicate alias")
		seen[al] = true
		n += 1
	end
	t.eq(n, 1000)
end)

t.done()
