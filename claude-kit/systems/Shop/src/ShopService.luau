--!strict
--[[
	Roblox glue for Shop. Server only. Owns MarketplaceService.ProcessReceipt (a game can only have ONE callback).

	local ShopService = require(script.Parent.ShopService)
	ShopService.Start({
		products = { [1234567] = { name = "Coins100", grant = function(userId, data) data.coins += 100 return true end } },
		passes = { [7654321] = { name = "VIP", onOwned = function(userId) ... end } },
		getData = function(userId) local p = Players:GetPlayerByUserId(userId) return p and PlayerDataService.Get(p) end,
		saveNow = function(userId) local p = Players:GetPlayerByUserId(userId) return p ~= nil and PlayerDataService.SaveNow(p) end,
	})
	Client: ReplicatedStorage.ShopRequest:FireServer("product", "Coins100")   -- by NAME, never by id or price
	Server: ShopService.HasPass(player, "VIP")
]]
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Shop = require(script.Parent.Shop)

export type StartOptions = {
	products: { [number]: Shop.Product },
	passes: { [number]: Shop.Pass }?,
	getData: (userId: number) -> Shop.Data?,
	saveNow: (userId: number) -> boolean,
}

local Service = {}
local shop: Shop.Shop? = nil

function Service.Start(opts: StartOptions)
	assert(shop == nil, "ShopService.Start called twice")
	local s = Shop.new({
		products = opts.products,
		passes = opts.passes,
		getData = opts.getData,
		saveNow = opts.saveNow,
		ownsPass = function(userId, passId)
			return MarketplaceService:UserOwnsGamePassAsync(userId, passId)
		end,
		now = os.time,
		wait = task.wait,
		log = function(m)
			warn("[Shop] " .. m)
		end,
	})
	shop = s

	MarketplaceService.ProcessReceipt = function(info)
		local d = s:ProcessReceipt({
			PlayerId = info.PlayerId,
			PurchaseId = info.PurchaseId,
			ProductId = info.ProductId,
		})
		return if d == "Granted"
			then Enum.ProductPurchaseDecision.PurchaseGranted
			else Enum.ProductPurchaseDecision.NotProcessedYet
	end

	MarketplaceService.PromptGamePassPurchaseFinished:Connect(function(player, passId, wasPurchased)
		s:OnPassPromptFinished(player.UserId, passId, wasPurchased)
	end)

	Players.PlayerAdded:Connect(function(player)
		task.spawn(function()
			s:RefreshPasses(player.UserId)
		end)
	end)
	for _, p in Players:GetPlayers() do
		task.spawn(function()
			s:RefreshPasses(p.UserId)
		end)
	end
	Players.PlayerRemoving:Connect(function(player)
		s:ClearPlayer(player.UserId)
	end)

	-- Client asks to see a purchase prompt. The client sends only a NAME; ids come from the server config.
	local remote = Instance.new("RemoteEvent")
	remote.Name = "ShopRequest"
	remote.Parent = ReplicatedStorage
	local last: { [Player]: number } = {}
	remote.OnServerEvent:Connect(function(player: Player, kind: unknown, name: unknown)
		if type(kind) ~= "string" or type(name) ~= "string" or #name > 50 then
			return
		end
		local now = os.clock()
		if now - (last[player] or 0) < 2 then
			return
		end
		last[player] = now
		if kind == "product" then
			local id = s:ProductIdByName(name)
			if id then
				MarketplaceService:PromptProductPurchase(player, id)
			end
		elseif kind == "pass" then
			local id = s:PassIdByName(name)
			if id and not s:HasPass(player.UserId, id) then
				MarketplaceService:PromptGamePassPurchase(player, id)
			end
		end
	end)
	Players.PlayerRemoving:Connect(function(player)
		last[player] = nil
	end)
end

function Service.HasPass(player: Player, passName: string): boolean
	local s = shop
	if s == nil then
		return false
	end
	local id = s:PassIdByName(passName)
	return id ~= nil and s:HasPass(player.UserId, id)
end

return Service
