--!strict

export type Data = { [any]: any }

export type Receipt = {
	PlayerId: number,
	PurchaseId: string,
	ProductId: number,
}

export type Product = {
	name: string,
	grant: (userId: number, data: Data) -> boolean,
}

export type Pass = {
	name: string,
	onOwned: ((userId: number) -> ())?,
}

export type Config = {
	products: { [number]: Product },
	passes: { [number]: Pass }?,
	getData: (userId: number) -> Data?,
	saveNow: (userId: number) -> boolean,
	ownsPass: (userId: number, passId: number) -> boolean,
	now: () -> number,
	wait: (number) -> any,
	maxReceipts: number?,
	passAttempts: number?,
	log: ((string) -> ())?,
}

export type Decision = "Granted" | "NotYet"

export type Shop = {
	ProcessReceipt: (self: Shop, receipt: Receipt) -> Decision,
	RefreshPasses: (self: Shop, userId: number) -> (),
	OnPassPromptFinished: (self: Shop, userId: number, passId: number, wasPurchased: boolean) -> boolean,
	HasPass: (self: Shop, userId: number, passId: number) -> boolean,
	ClearPlayer: (self: Shop, userId: number) -> (),
	ProductIdByName: (self: Shop, name: string) -> number?,
	PassIdByName: (self: Shop, name: string) -> number?,
}

type Impl = {
	_c: Config,
	_inFlight: { [string]: boolean },
	_owned: { [number]: { [number]: boolean } },
}

local Shop = {}
Shop.__index = Shop

local function log(self: Impl, msg: string)
	local f = self._c.log
	if f then
		f(msg)
	end
end

function Shop.new(config: Config): Shop
	local self = setmetatable({
		_c = config,
		_inFlight = {},
		_owned = {},
	}, Shop)
	return (self :: any) :: Shop
end

local function prune(receipts: { [string]: number }, max: number)
	local n = 0
	for _ in receipts do
		n += 1
	end
	if n <= max then
		return
	end
	local ids = {}
	for id in receipts do
		table.insert(ids, id)
	end
	table.sort(ids, function(a, b)
		return receipts[a] < receipts[b]
	end)
	for i = 1, n - max do
		receipts[ids[i]] = nil
	end
end

function Shop.ProcessReceipt(self: Impl, receipt: Receipt): Decision
	local c = self._c
	local pid = receipt.PurchaseId
	local product = c.products[receipt.ProductId]
	if product == nil then
		log(self, "unknown product id " .. tostring(receipt.ProductId) .. " (add it to Config.products)")
		return "NotYet"
	end
	if self._inFlight[pid] then
		return "NotYet"
	end
	local data = c.getData(receipt.PlayerId)
	if data == nil then
		return "NotYet"
	end
	local receipts = data.Receipts
	if type(receipts) ~= "table" then
		log(self, "player data has no Receipts table: add Receipts = {} to your PlayerData template")
		return "NotYet"
	end
	self._inFlight[pid] = true
	local decision: Decision = "NotYet"
	if receipts[pid] ~= nil then
		if c.saveNow(receipt.PlayerId) then
			decision = "Granted"
		end
	else
		local ok, granted = pcall(product.grant, receipt.PlayerId, data)
		if not ok then
			log(self, "grant error for " .. product.name .. ": " .. tostring(granted))
		elseif granted ~= true then
			log(self, "grant refused for " .. product.name)
		else
			receipts[pid] = c.now()
			prune(receipts, c.maxReceipts or 300)
			if c.saveNow(receipt.PlayerId) then
				decision = "Granted"
			end
		end
	end
	self._inFlight[pid] = nil
	return decision
end

local function verifyOwned(self: Impl, userId: number, passId: number): boolean
	local c = self._c
	for attempt = 1, c.passAttempts or 4 do
		local ok, owns = pcall(c.ownsPass, userId, passId)
		if ok then
			return owns == true
		end
		log(self, "ownsPass error: " .. tostring(owns))
		c.wait(attempt)
	end
	return false
end

local function markOwned(self: Impl, userId: number, passId: number)
	local mine = self._owned[userId]
	if mine == nil then
		mine = {}
		self._owned[userId] = mine
	end
	if mine[passId] then
		return
	end
	mine[passId] = true
	local pass = (self._c.passes or {})[passId]
	if pass and pass.onOwned then
		local ok, err = pcall(pass.onOwned, userId)
		if not ok then
			log(self, "onOwned error for " .. pass.name .. ": " .. tostring(err))
		end
	end
end

function Shop.RefreshPasses(self: Impl, userId: number)
	local passes: { [number]: Pass } = self._c.passes or {}
	for passId in passes do
		if verifyOwned(self, userId, passId) then
			markOwned(self, userId, passId)
		end
	end
end

function Shop.OnPassPromptFinished(self: Impl, userId: number, passId: number, wasPurchased: boolean): boolean
	if not wasPurchased or (self._c.passes or {})[passId] == nil then
		return false
	end
	if verifyOwned(self, userId, passId) then
		markOwned(self, userId, passId)
		return true
	end
	return false
end

function Shop.HasPass(self: Impl, userId: number, passId: number): boolean
	local mine = self._owned[userId]
	return mine ~= nil and mine[passId] == true
end

function Shop.ClearPlayer(self: Impl, userId: number)
	self._owned[userId] = nil
end

function Shop.ProductIdByName(self: Impl, name: string): number?
	for id, p in self._c.products do
		if p.name == name then
			return id
		end
	end
	return nil
end

function Shop.PassIdByName(self: Impl, name: string): number?
	local passes: { [number]: Pass } = self._c.passes or {}
	for id, p in passes do
		if p.name == name then
			return id
		end
	end
	return nil
end

return Shop
