--!strict
local ReceiptScenarios = {}

export type Env = {
	shop: any,
	reward: () -> number,
	setLoaded: (boolean) -> (),
	setSaveOk: (boolean) -> (),
	productId: number,
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
