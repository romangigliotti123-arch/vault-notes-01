--!strict
local DataLoss = {}

export type Db = { rows: { [string]: any }, failNext: number, failAll: boolean, calls: number }
export type Clock = { t: number, wait: (seconds: number) -> () }
export type Factory = (jobId: string, store: any, clock: Clock, lostLog: { string }) -> any
export type Result = { name: string, ok: boolean, detail: string }

local function deepCopy(v: any): any
	if type(v) == "table" then
		local out = {}
		for k, x in v do
			out[k] = deepCopy(x)
		end
		return out
	end
	return v
end

function DataLoss.newDb(): Db
	return { rows = {}, failNext = 0, failAll = false, calls = 0 }
end

function DataLoss.newClock(): Clock
	local clock: Clock = {
		t = 1000,
		wait = function() end,
	}
	clock.wait = function(seconds: number)
		clock.t += seconds
	end
	return clock
end

function DataLoss.store(db: Db): any
	local s = {}
	function s.UpdateAsync(_self: any, key: string, transform: (old: any) -> any): any
		db.calls += 1
		if db.failAll then
			error("DataStore request was added to queue. (fake outage)")
		end
		if db.failNext > 0 then
			db.failNext -= 1
			error("DataStore request was added to queue. (fake throttle)")
		end
		local old = deepCopy(db.rows[key])
		local new = transform(old)
		if new == nil then
			return old
		end
		db.rows[key] = deepCopy(new)
		return deepCopy(new)
	end
	return s
end

type Scenario = { name: string, run: (f: Factory) -> (boolean, string) }

local function server(f: Factory, jobId: string, db: Db, clock: Clock): (any, { string })
	local lost: { string } = {}
	return f(jobId, DataLoss.store(db), clock, lost), lost
end

local function eq(a: any, b: any, what: string): (boolean, string)
	if a == b then
		return true, what .. " ok"
	end
	return false, `{what}: expected {tostring(b)}, got {tostring(a)}`
end

local SCENARIOS: { Scenario } = {
	{
		name = "transient load errors recover",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local pd = server(f, "A", db, clock)
			db.failNext = 3
			local s, why = pd:LoadAsync("p1")
			if s == nil then
				return false, "load gave up after 3 errors: " .. tostring(why)
			end
			return true, `loaded after {db.calls} DataStore calls`
		end,
	},
	{
		name = "load outage never overwrites saved data",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local a = server(f, "A", db, clock)
			local s = a:LoadAsync("p1")
			s.Data.coins = 500
			a:ReleaseAsync(s)
			local b = server(f, "B", db, clock)
			db.failAll = true
			local s2, why = b:LoadAsync("p1")
			db.failAll = false
			if s2 ~= nil then
				return false, "load reported success during an outage"
			end
			local ok, msg = eq(db.rows.p1.data.coins, 500, "stored coins after failed load")
			return ok, if ok then `refused with '{tostring(why)}', row untouched` else msg
		end,
	},
	{
		name = "save outage keeps data in memory and the next save lands",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local pd = server(f, "A", db, clock)
			local s = pd:LoadAsync("p1")
			s.Data.coins = 7
			db.failAll = true
			if pd:SaveAsync(s) then
				return false, "save claimed success during an outage"
			end
			if s.State ~= "active" or s.Data.coins ~= 7 then
				return false, `session dropped or data lost (state {s.State}, coins {s.Data.coins})`
			end
			db.failAll = false
			if not pd:SaveAsync(s) then
				return false, "next save after recovery failed"
			end
			return eq(db.rows.p1.data.coins, 7, "stored coins after recovery")
		end,
	},
	{
		name = "shutdown saves every session within 30 seconds",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local pd = server(f, "A", db, clock)
			for i = 1, 5 do
				local s = pd:LoadAsync("p" .. i)
				s.Data.coins = i * 10
			end
			local start = clock.t
			pd:ReleaseAll(25)
			for i = 1, 5 do
				local row = db.rows["p" .. i]
				if row.data.coins ~= i * 10 or row.lock ~= nil then
					return false, `p{i} not saved or still locked`
				end
			end
			local took = clock.t - start
			return took <= 30, `5 players released in {took}s of fake time`
		end,
	},
	{
		name = "shutdown during an outage corrupts nothing and the lock expires",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local a = server(f, "A", db, clock)
			local s = a:LoadAsync("p1")
			s.Data.coins = 10
			a:SaveAsync(s)
			s.Data.coins = 99
			db.failAll = true
			a:ReleaseAll(25)
			db.failAll = false
			if db.rows.p1.data.coins ~= 10 then
				return false, `row changed to {db.rows.p1.data.coins} during an outage`
			end
			clock.t += 700
			local b = server(f, "B", db, clock)
			local s2 = b:LoadAsync("p1")
			if s2 == nil then
				return false, "next server could not take over an expired lock"
			end
			return eq(s2.Data.coins, 10, "recovered coins (last good save, 89 unsaved lost)")
		end,
	},
	{
		name = "crash without release: takeover sees the last save",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local a = server(f, "A", db, clock)
			local s = a:LoadAsync("p1")
			s.Data.coins = 40
			a:SaveAsync(s)
			s.Data.coins = 41
			clock.t += 700
			local b = server(f, "B", db, clock)
			local s2 = b:LoadAsync("p1")
			if s2 == nil then
				return false, "takeover failed"
			end
			return eq(s2.Data.coins, 40, "coins after crash")
		end,
	},
	{
		name = "old server cannot overwrite after takeover",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local a, lostA = server(f, "A", db, clock)
			local sa = a:LoadAsync("p1")
			sa.Data.coins = 5
			a:SaveAsync(sa)
			clock.t += 700
			local b = server(f, "B", db, clock)
			local sb = b:LoadAsync("p1")
			sb.Data.coins = 50
			b:SaveAsync(sb)
			sa.Data.coins = 1
			if a:SaveAsync(sa) then
				return false, "stale server saved over the new owner"
			end
			local ok, msg = eq(db.rows.p1.data.coins, 50, "stored coins after stale save")
			if not ok then
				return ok, msg
			end
			return #lostA >= 1, `stale server notified: {#lostA} lost callback(s)`
		end,
	},
	{
		name = "progress lost in a crash is bounded by the autosave interval",
		run = function(f)
			local db, clock = DataLoss.newDb(), DataLoss.newClock()
			local a = server(f, "A", db, clock)
			local s = a:LoadAsync("p1")
			local earned = 0
			for _ = 1, 40 do
				clock.t += 30
				earned += 1
				s.Data.coins = earned
				a:AutosaveDue()
			end
			local saved = db.rows.p1.data.coins
			local lostSeconds = (earned - saved) * 30
			return lostSeconds <= 150, `{earned - saved} ticks ({lostSeconds}s of play) would be lost in a crash now`
		end,
	},
}

function DataLoss.runAll(f: Factory): { Result }
	local out: { Result } = {}
	for _, sc in SCENARIOS do
		local ok, a, b = pcall(sc.run, f)
		if ok then
			table.insert(out, { name = sc.name, ok = a :: boolean, detail = b :: string })
		else
			table.insert(out, { name = sc.name, ok = false, detail = "scenario errored: " .. tostring(a) })
		end
	end
	return out
end

function DataLoss.report(results: { Result }): string
	local failed = 0
	for _, r in results do
		if not r.ok then
			failed += 1
		end
	end
	local lines = { `DATA LOSS SIM: {#results - failed}/{#results} scenarios passed` }
	for _, r in results do
		table.insert(lines, `  {if r.ok then "PASS" else "FAIL"} {r.name}: {r.detail}`)
	end
	return table.concat(lines, "\n")
end

DataLoss.scenarioNames = function(): { string }
	local names = {}
	for _, s in SCENARIOS do
		table.insert(names, s.name)
	end
	return names
end

return DataLoss
