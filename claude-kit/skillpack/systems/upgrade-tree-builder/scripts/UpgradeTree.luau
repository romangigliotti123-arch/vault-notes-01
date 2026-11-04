--!strict
local UpgradeTree = {}
UpgradeTree.__index = UpgradeTree

export type Data = { [any]: any }
export type Node = { cost: number, growth: number?, maxLevel: number, requires: { [string]: number }? }
export type Config = { wallet: any, currency: string, nodes: { [string]: Node }, refund: number? }
export type UpgradeTree = typeof(setmetatable({} :: { _c: Config }, UpgradeTree))

function UpgradeTree.new(config: Config): UpgradeTree
	for id, n in config.nodes do
		assert(
			n.cost >= 1 and n.maxLevel >= 1 and n.maxLevel == math.floor(n.maxLevel),
			`node {id}: cost >= 1 and integer maxLevel >= 1`
		)
		local reqs: { [string]: number } = n.requires or {}
		for req, lvl in reqs do
			assert(config.nodes[req] ~= nil, `node {id}: requires unknown node {req}`)
			assert(
				lvl >= 1 and lvl <= config.nodes[req].maxLevel,
				`node {id}: requires level {lvl} of {req}, which can never be reached`
			)
		end
	end
	local state: { [string]: number } = {}
	local function visit(id: string)
		assert(state[id] ~= 1, `upgrade tree has a cycle through {id}`)
		if state[id] == 2 then
			return
		end
		state[id] = 1
		local reqs: { [string]: number } = config.nodes[id].requires or {}
		for req in reqs do
			visit(req)
		end
		state[id] = 2
	end
	for id in config.nodes do
		visit(id)
	end
	assert((config.refund or 0.8) >= 0 and (config.refund or 0.8) <= 1, "refund must be between 0 and 1")
	return setmetatable({ _c = config }, UpgradeTree)
end

function UpgradeTree.init(_self: UpgradeTree, data: Data): Data
	local u = data.Upgrades
	if type(u) ~= "table" then
		u = { levels = {} }
		data.Upgrades = u
	end
	u.levels = u.levels or {}
	return u
end

function UpgradeTree.level(self: UpgradeTree, data: Data, id: string): number
	return self:init(data).levels[id] or 0
end

function UpgradeTree.costOf(self: UpgradeTree, id: string, level: number): number
	local n = self._c.nodes[id]
	return math.floor(n.cost * (n.growth or 1) ^ level)
end

function UpgradeTree.canBuy(self: UpgradeTree, data: Data, id: string): (boolean, string)
	local n = self._c.nodes[id]
	if n == nil then
		return false, "unknown upgrade"
	end
	local lvl = self:level(data, id)
	if lvl >= n.maxLevel then
		return false, "max level"
	end
	local reqs: { [string]: number } = n.requires or {}
	for req, need in reqs do
		if self:level(data, req) < need then
			return false, "requires " .. req
		end
	end
	if not self._c.wallet:canAfford(data, self._c.currency, self:costOf(id, lvl)) then
		return false, "cannot afford"
	end
	return true, "ok"
end

function UpgradeTree.buy(self: UpgradeTree, data: Data, id: string): (boolean, string)
	local ok, why = self:canBuy(data, id)
	if not ok then
		return false, why
	end
	local lvl = self:level(data, id)
	local spent = self._c.wallet:spend(data, self._c.currency, self:costOf(id, lvl), "upgrade:" .. id)
	if not spent then
		return false, "cannot afford"
	end
	self:init(data).levels[id] = lvl + 1
	return true, "ok"
end

function UpgradeTree.spentTotal(self: UpgradeTree, data: Data): number
	local total = 0
	for id, lvl in self:init(data).levels do
		for l = 0, lvl - 1 do
			total += self:costOf(id, l)
		end
	end
	return total
end

function UpgradeTree.respec(self: UpgradeTree, data: Data): number
	local refund = math.floor(self:spentTotal(data) * (self._c.refund or 0.8))
	local u = self:init(data)
	u.levels = {}
	if refund > 0 then
		self._c.wallet:add(data, self._c.currency, refund, "respec")
	end
	return refund
end

return UpgradeTree
