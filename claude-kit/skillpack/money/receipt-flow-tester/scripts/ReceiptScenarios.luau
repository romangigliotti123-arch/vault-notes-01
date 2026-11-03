--!strict
-- ReceiptScenarios: the failure cases every ProcessReceipt must survive, run against YOUR wiring (a Shop built from your real catalogue).
-- You supply a factory that builds a fresh environment; this module runs the scenarios and reports pass/fail per case.
--   local results = ReceiptScenarios.run(function()
--       local env = buildMyShopWithFakes()   -- Shop.new({... getData, saveNow, ownsPass fakes ...})
--       return { shop = env.shop, reward = function() return env.data.coins end, setLoaded = ..., setSaveOk = ..., productId = 111, userId = 1, expectedDelta = 100 }
--   end)
--   for _, r in results do print(r.pass and "ok  " or "FAIL", r.name, r.detail) end
local ReceiptScenarios = {}

export type Env = {
	shop: any, -- anything with :ProcessReceipt(receipt) -> "Granted" | "NotYet"
	reward: () -> number, -- the observable that the product changes (coins, gems...)
	setLoaded: (boolean) -> (), -- false = player data not loaded / player gone
	setSaveOk: (boolean) -> (), -- false = the next saves fail
	productId: number, -- a known product id that adds `expectedDelta` to reward()
	userId: number,
	expectedDelta: number,
}
export type Result = { name: string, pass: boolean, detail: string }

local function receipt(env: Env, purchaseId: string, productId: number?)
	return { PlayerId = env.userId, PurchaseId = purchaseId, ProductId = productId or env.productId }
end

local scenarios: { { name: string, run: (Env) -> (boolean, string) } } = {
	{
		name = "first delivery grants exactly once",
		run = function(env)
			local before = env.reward()
			local d = env.shop:ProcessReceipt(receipt(env, "A"))
			local delta = env.reward() - before
			return d == "Granted" and delta == env.expectedDelta, `decision={d} delta={delta}`
		end,
	},
	{
		name = "the same PurchaseId delivered again never grants twice",
		run = function(env)
			env.shop:ProcessReceipt(receipt(env, "A"))
			local after = env.reward()
			local d = env.shop:ProcessReceipt(receipt(env, "A"))
			return d == "Granted" and env.reward() == after, `decision={d} reward={env.reward()} (was {after})`
		end,
	},
	{
		name = "player data not loaded answers NotYet and grants nothing",
		run = function(env)
			env.setLoaded(false)
			local before = env.reward()
			local d = env.shop:ProcessReceipt(receipt(env, "B"))
			env.setLoaded(true)
			return d == "NotYet" and env.reward() == before, `decision={d}`
		end,
	},
	{
		name = "save failure answers NotYet, then the retry grants once",
		run = function(env)
			local before = env.reward()
			env.setSaveOk(false)
			local first = env.shop:ProcessReceipt(receipt(env, "C"))
			env.setSaveOk(true)
			local second = env.shop:ProcessReceipt(receipt(env, "C"))
			local third = env.shop:ProcessReceipt(receipt(env, "C"))
			local delta = env.reward() - before
			return first == "NotYet" and second == "Granted" and third == "Granted" and delta == env.expectedDelta,
				`first={first} second={second} third={third} delta={delta}`
		end,
	},
	{
		name = "an unknown product id answers NotYet and grants nothing",
		run = function(env)
			local before = env.reward()
			local d = env.shop:ProcessReceipt(receipt(env, "D", -999))
			return d == "NotYet" and env.reward() == before, `decision={d}`
		end,
	},
}

function ReceiptScenarios.names(): { string }
	local out = {}
	for _, s in scenarios do
		table.insert(out, s.name)
	end
	return out
end

function ReceiptScenarios.run(factory: () -> Env): { Result }
	local out: { Result } = {}
	for _, s in scenarios do
		local ok, pass, detail = pcall(function()
			return s.run(factory())
		end)
		if not ok then
			table.insert(out, { name = s.name, pass = false, detail = `error: {tostring(pass)}` })
		else
			table.insert(out, { name = s.name, pass = pass :: any, detail = detail :: any })
		end
	end
	return out
end

function ReceiptScenarios.allPassed(results: { Result }): boolean
	for _, r in results do
		if not r.pass then
			return false
		end
	end
	return #results > 0
end

return ReceiptScenarios
