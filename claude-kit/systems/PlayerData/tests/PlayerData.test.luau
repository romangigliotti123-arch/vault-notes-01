--!nocheck
-- Run: lune run tests/PlayerData.test.luau   (from the PlayerData folder)
local t = require("../../_check/harness")
local PlayerData = require("../src/PlayerData")

local function deepCopy(v: any): any
	if type(v) == "table" then
		local o = {}
		for k, x in v do
			o[k] = deepCopy(x)
		end
		return o
	end
	return v
end

-- Fake DataStore shared by several "servers". UpdateAsync mimics Roblox: transform(old) -> new | nil (cancel).
local function newDb()
	return { rows = {}, fail = 0, calls = 0 }
end

local function store(db)
	local s = {}
	function s:UpdateAsync(key, fn)
		db.calls += 1
		if db.fail > 0 then
			db.fail -= 1
			error("DataStore request was added to queue. (fake)")
		end
		local old = deepCopy(db.rows[key])
		local new = fn(old)
		if new == nil then
			return old -- real Roblox returns the unchanged value on cancel; code must not rely on nil
		end
		db.rows[key] = deepCopy(new)
		return deepCopy(new)
	end
	return s
end

local function server(db, jobId, clock, over)
	local waits = {}
	local lost = {}
	local cfg = {
		store = store(db),
		jobId = jobId,
		template = { coins = 0, inventory = {}, settings = { music = true } },
		version = 1,
		now = function()
			return clock.t
		end,
		wait = function(s)
			table.insert(waits, s)
			clock.t += s
			if clock.onWait then
				clock.onWait()
			end
			return s
		end,
		spawn = function(f)
			f()
		end,
		onLost = function(s, why)
			table.insert(lost, why)
		end,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return PlayerData.new(cfg), waits, lost
end

print("PlayerData")

t.test("new player gets template data and a lock", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock)
	local s = pd:LoadAsync("p1")
	t.truthy(s)
	t.eq(s.Data.coins, 0)
	t.eq(db.rows.p1.lock.owner, "A")
	t.eq(db.rows.p1.v, 1)
end)

t.test("save keeps the lock and refreshes it; release clears it", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock)
	local s = pd:LoadAsync("p1")
	s.Data.coins = 50
	clock.t = 1100
	t.truthy(pd:SaveAsync(s))
	t.eq(db.rows.p1.data.coins, 50)
	t.eq(db.rows.p1.lock.t, 1100)
	t.truthy(pd:ReleaseAsync(s))
	t.eq(db.rows.p1.lock, nil)
	t.eq(s.State, "released")
	t.eq(pd:ActiveCount(), 0)
end)

t.test("second server waits for the first to release, then loads saved data", function()
	local db, clock = newDb(), { t = 1000 }
	local a = server(db, "A", clock)
	local b, waits = server(db, "B", clock)
	local sa = a:LoadAsync("p1")
	sa.Data.coins = 7
	clock.onWait = function()
		a:ReleaseAsync(sa)
		clock.onWait = nil
	end
	local sb, err = b:LoadAsync("p1")
	t.truthy(sb, err)
	t.eq(sb.Data.coins, 7)
	t.eq(waits[1], 3)
	t.eq(db.rows.p1.lock.owner, "B")
end)

t.test("live foreign lock never released: gives up with 'locked' and does not touch data", function()
	local db, clock = newDb(), { t = 1000 }
	local a = server(db, "A", clock)
	local b = server(db, "B", clock, { lockWait = 9 })
	a:LoadAsync("p1")
	local before = deepCopy(db.rows.p1)
	local sb, err = b:LoadAsync("p1")
	t.eq(sb, nil)
	t.eq(err, "locked")
	t.eq(db.rows.p1, before)
end)

t.test("stale lock is taken over; the old server then loses its session instead of overwriting", function()
	local db, clock = newDb(), { t = 1000 }
	local a, _, lostA = server(db, "A", clock)
	local b = server(db, "B", clock, { lockTimeout = 600 })
	local sa = a:LoadAsync("p1")
	sa.Data.coins = 1
	clock.t = 2000 -- A "crashed" and never refreshed
	local sb = b:LoadAsync("p1")
	t.truthy(sb)
	sb.Data.coins = 99
	b:SaveAsync(sb)
	t.falsy(a:SaveAsync(sa))
	t.eq(sa.State, "lost")
	t.eq(lostA[1], "lost")
	t.eq(db.rows.p1.data.coins, 99)
end)

t.test("save errors retry with exponential backoff and then succeed", function()
	local db, clock = newDb(), { t = 1000 }
	local pd, waits = server(db, "A", clock)
	local s = pd:LoadAsync("p1")
	db.fail = 3
	t.truthy(pd:SaveAsync(s))
	t.eq(waits, { 1, 2, 4 })
end)

t.test("save gives up after saveAttempts but session stays active for the next autosave", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock, { saveAttempts = 2 })
	local s = pd:LoadAsync("p1")
	db.fail = 5
	t.falsy(pd:SaveAsync(s))
	t.eq(s.State, "active")
	db.fail = 0
	t.truthy(pd:SaveAsync(s))
end)

t.test("load fails after loadAttempts DataStore errors", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock, { loadAttempts = 3 })
	db.fail = 10
	local s, err = pd:LoadAsync("p1")
	t.eq(s, nil)
	t.eq(err, "failed")
end)

t.test("schema migration runs in order and reconcile adds new template keys", function()
	local db, clock = newDb(), { t = 1000 }
	db.rows.p1 = { v = 1, data = { coins = 5 }, saved = 1 }
	local pd = server(db, "A", clock, {
		version = 3,
		template = { coins = 0, gems = 0, settings = { music = true } },
		migrations = {
			[1] = function(d)
				d.gems = d.coins * 2
				return d
			end,
			[2] = function(d)
				d.migrated = true
				return d
			end,
		},
	})
	local s = pd:LoadAsync("p1")
	t.eq(s.Data.gems, 10)
	t.eq(s.Data.migrated, true)
	t.eq(s.Data.settings.music, true)
	t.eq(db.rows.p1.v, 3)
end)

t.test("missing migration fails the load without modifying the stored record", function()
	local db, clock = newDb(), { t = 1000 }
	db.rows.p1 = { v = 1, data = { coins = 5 }, saved = 1 }
	local before = deepCopy(db.rows.p1)
	local pd = server(db, "A", clock, { version = 2, loadAttempts = 2 })
	local s, err = pd:LoadAsync("p1")
	t.eq(s, nil)
	t.eq(err, "failed")
	t.eq(db.rows.p1, before)
end)

t.test("data from a newer schema is refused (rollback safety)", function()
	local db, clock = newDb(), { t = 1000 }
	db.rows.p1 = { v = 9, data = { coins = 5 }, saved = 1 }
	local pd = server(db, "A", clock)
	local s, err = pd:LoadAsync("p1")
	t.eq(s, nil)
	t.eq(err, "newer")
	t.eq(db.rows.p1.v, 9)
	t.eq(db.rows.p1.lock, nil)
end)

t.test("unserialisable data is refused and reported, nothing is written", function()
	local db, clock = newDb(), { t = 1000 }
	local pd, _, lost = server(db, "A", clock)
	local s = pd:LoadAsync("p1")
	local before = deepCopy(db.rows.p1)
	s.Data.bad = function() end
	t.falsy(pd:SaveAsync(s))
	t.eq(db.rows.p1, before)
	t.eq(lost[1], "unserialisable:Data.bad (function)")
	s.Data.bad = nil
	s.Data.n = 0 / 0
	t.falsy(pd:SaveAsync(s))
	s.Data.n = nil
	s.Data.mixed = { 1, 2, x = 3 }
	t.falsy(pd:SaveAsync(s))
end)

t.test("autosave only touches sessions older than the interval", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock, { autosaveInterval = 120 })
	local s = pd:LoadAsync("p1")
	s.Data.coins = 3
	clock.t = 1060
	t.eq(pd:AutosaveDue(), 0)
	clock.t = 1130
	t.eq(pd:AutosaveDue(), 1)
	t.eq(db.rows.p1.data.coins, 3)
	t.eq(s.LastSave, 1130)
end)

t.test("ReleaseAll (BindToClose) saves and unlocks every session", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock)
	for i = 1, 5 do
		pd:LoadAsync("p" .. i).Data.coins = i
	end
	pd:ReleaseAll()
	for i = 1, 5 do
		t.eq(db.rows["p" .. i].data.coins, i)
		t.eq(db.rows["p" .. i].lock, nil)
	end
	t.eq(pd:ActiveCount(), 0)
end)

t.test("player leaving mid-load: lock is released again", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock)
	local calls = 0
	local s, err = pd:LoadAsync("p1", function()
		calls += 1
		return calls >= 2
	end)
	t.eq(s, nil)
	t.eq(err, "cancelled")
	t.eq(db.rows.p1.lock, nil)
	t.eq(pd:ActiveCount(), 0)
end)

t.test("a mutation during an in-flight save does not corrupt the saved snapshot", function()
	local db, clock = newDb(), { t = 1000 }
	local pd = server(db, "A", clock)
	local s = pd:LoadAsync("p1")
	s.Data.coins = 1
	local realUpdate = pd._c.store.UpdateAsync
	pd._c.store.UpdateAsync = function(self, key, fn)
		s.Data.coins = 2 -- game code keeps running while the request is in flight
		return realUpdate(self, key, fn)
	end
	pd:SaveAsync(s)
	t.eq(db.rows.p1.data.coins, 1)
	t.eq(s.Data.coins, 2)
end)

t.done()
