--!strict
-- PurchaseScenarios: receipt-handling scenarios for a developer-product flow, run headless. They test the RULES the vault gives for
-- ProcessReceipt: grant only after the data is updated and saved, the same PurchaseId never grants twice, anything uncertain answers
-- NotYet so Roblox retries, unknown products and missing data never grant. The rig adapts any implementation; the kit's Shop is the
-- reference (see the test). Real Robux purchases and the Roblox purchase prompt are NOT covered here (test those in Studio / live).
local PurchaseScenarios = {}

export type Receipt = { PlayerId: number, PurchaseId: string, ProductId: number }
-- A rig wraps one implementation + a fake player data store:
--   process(receipt) -> "Granted" | "NotYet"
--   coins(userId) -> number           coins currently in that player's data
--   setSaveOk(ok)                     make the persistence step succeed or fail
--   setDataLoaded(userId, loaded)     simulate data not loaded / player left
--   productId: a product that grants `reward` coins; badProductId: a product whose grant throws (or nil to skip that scenario)
export type Rig = {
	process: (Receipt) -> string,
	coins: (number) -> number,
	setSaveOk: (boolean) -> (),
	setDataLoaded: (number, boolean) -> (),
	productId: number,
	reward: number,
	badProductId: number?,
	unknownProductId: number,
}
export type Result = { name: string, ok: boolean, detail: string }
type Scenario = { name: string, run: (make: () -> Rig) -> (boolean, string) }

local function rc(id: string, product: number, uid: number?): Receipt
	return { PlayerId = uid or 1, PurchaseId = id, ProductId = product }
end

local SCENARIOS: { Scenario } = {
	{
		name = "a normal purchase grants once and answers Granted",
		run = function(make)
			local r = make()
			local d = r.process(rc("p1", r.productId))
			return d == "Granted" and r.coins(1) == r.reward, `decision {d}, coins {r.coins(1)}`
		end,
	},
	{
		name = "the same PurchaseId repeated never grants twice",
		run = function(make)
			local r = make()
			r.process(rc("p1", r.productId))
			local d = r.process(rc("p1", r.productId))
			return d == "Granted" and r.coins(1) == r.reward,
				`second decision {d}, coins {r.coins(1)} (want {r.reward})`
		end,
	},
	{
		name = "a failed save answers NotYet, and the retry grants exactly once",
		run = function(make)
			local r = make()
			r.setSaveOk(false)
			local first = r.process(rc("p1", r.productId))
			r.setSaveOk(true)
			local second = r.process(rc("p1", r.productId))
			return first == "NotYet" and second == "Granted" and r.coins(1) == r.reward,
				`first {first}, retry {second}, coins {r.coins(1)} (want {r.reward})`
		end,
	},
	{
		name = "player data not loaded answers NotYet and grants nothing",
		run = function(make)
			local r = make()
			r.setDataLoaded(1, false)
			local d = r.process(rc("p1", r.productId))
			r.setDataLoaded(1, true)
			return d == "NotYet" and r.coins(1) == 0, `decision {d}, coins {r.coins(1)}`
		end,
	},
	{
		name = "an unknown product id answers NotYet",
		run = function(make)
			local r = make()
			local d = r.process(rc("p1", r.unknownProductId))
			return d == "NotYet" and r.coins(1) == 0, `decision {d}, coins {r.coins(1)}`
		end,
	},
	{
		name = "a grant that throws answers NotYet and leaves data unchanged",
		run = function(make)
			local r = make()
			if r.badProductId == nil then
				return true, "skipped: rig has no throwing product"
			end
			local d = r.process(rc("p1", r.badProductId))
			return d == "NotYet" and r.coins(1) == 0, `decision {d}, coins {r.coins(1)}`
		end,
	},
	{
		name = "two different purchases both grant",
		run = function(make)
			local r = make()
			r.process(rc("p1", r.productId))
			r.process(rc("p2", r.productId))
			return r.coins(1) == r.reward * 2, `coins {r.coins(1)} (want {r.reward * 2})`
		end,
	},
}

function PurchaseScenarios.runAll(make: () -> Rig): { Result }
	local out: { Result } = {}
	for _, sc in SCENARIOS do
		local ok, a, b = pcall(sc.run, make)
		if ok then
			table.insert(out, { name = sc.name, ok = a :: boolean, detail = b :: string })
		else
			table.insert(out, { name = sc.name, ok = false, detail = "scenario errored: " .. tostring(a) })
		end
	end
	return out
end

function PurchaseScenarios.report(results: { Result }): string
	local failed = 0
	for _, r in results do
		if not r.ok then
			failed += 1
		end
	end
	local lines = { `PURCHASE FLOW: {#results - failed}/{#results} scenarios passed` }
	for _, r in results do
		table.insert(lines, `  {if r.ok then "PASS" else "FAIL"} {r.name}: {r.detail}`)
	end
	return table.concat(lines, "\n")
end

return PurchaseScenarios
