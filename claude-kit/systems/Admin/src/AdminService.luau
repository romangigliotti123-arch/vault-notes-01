--!strict
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TextChatService = game:GetService("TextChatService")

local Admin = require(script.Parent.Admin)

export type StartOptions = {
	owners: { [number]: number },
	group: { id: number, rankToAdmin: { [number]: number } }?,
	extraCommands: { [string]: Admin.Command }?,
}

local Service = {}

function Service.Start(opts: StartOptions)
	local groupRank: { [number]: number } = {}

	local function getRank(userId: number): number
		local r = opts.owners[userId] or 0
		return math.max(r, groupRank[userId] or 0)
	end

	local function loadGroupRank(player: Player)
		local g = opts.group
		if not g then
			return
		end
		local ok, groups = pcall(function()
			return GroupService:GetGroupsAsync(player.UserId)
		end)
		if ok then
			local rank = 0
			for _, info in groups do
				if info.Id == g.id then
					rank = info.Rank
				end
			end
			local best = 0
			for minRank, adminRank in g.rankToAdmin do
				if rank >= minRank and adminRank > best then
					best = adminRank
				end
			end
			groupRank[player.UserId] = best
		end
	end

	local function findPlayers(query: string): { number }
		local q = string.lower(query)
		local exact, prefix = {}, {}
		for _, p in Players:GetPlayers() do
			local n = string.lower(p.Name)
			if n == q then
				table.insert(exact, p.UserId)
			elseif string.sub(n, 1, #q) == q then
				table.insert(prefix, p.UserId)
			end
		end
		return if #exact > 0 then exact else prefix
	end

	local replyRemote = Instance.new("RemoteEvent")
	replyRemote.Name = "AdminReply"
	replyRemote.Parent = ReplicatedStorage
	local function reply(userId: number, msg: string?)
		local p = Players:GetPlayerByUserId(userId)
		if p and msg then
			replyRemote:FireClient(p, msg)
		end
	end

	local commands: { [string]: Admin.Command } = {
		help = {
			minRank = 1,
			args = {},
			run = function()
				local names = {}
				local extra: { [string]: Admin.Command } = opts.extraCommands or {}
				for n in extra do
					table.insert(names, n)
				end
				table.sort(names)
				return "Commands: help, kick, announce"
					.. (if #names > 0 then ", " .. table.concat(names, ", ") else "")
			end,
		},
		kick = {
			minRank = 2,
			args = {
				{ name = "target", kind = "player" },
				{ name = "reason", kind = "rest", optional = true, max = 100 },
			},
			run = function(_, a)
				local p = Players:GetPlayerByUserId(a.target)
				if p then
					p:Kick(a.reason or "Removed by a moderator.")
				end
				return "Kicked."
			end,
		},
		announce = {
			minRank = 3,
			args = { { name = "text", kind = "rest", max = 150 } },
			run = function(_, a)
				for _, p in Players:GetPlayers() do
					replyRemote:FireClient(p, "[Announcement] " .. a.text)
				end
				return nil
			end,
		},
	}
	local extra: { [string]: Admin.Command } = opts.extraCommands or {}
	for n, c in extra do
		commands[string.lower(n)] = c
	end

	local admin = Admin.new({
		commands = commands,
		getRank = getRank,
		findPlayers = findPlayers,
		now = os.time,
		audit = function(e)
			print(
				string.format(
					"[AdminAudit] actor=%d rank=%d cmd=%s args=%q ok=%s note=%s",
					e.actor,
					e.rank,
					e.command,
					e.args,
					tostring(e.ok),
					tostring(e.note)
				)
			)
		end,
	})

	Players.PlayerAdded:Connect(loadGroupRank)
	for _, p in Players:GetPlayers() do
		task.spawn(loadGroupRank, p)
	end
	Players.PlayerRemoving:Connect(function(p)
		groupRank[p.UserId] = nil
	end)

	local remote = Instance.new("RemoteEvent")
	remote.Name = "AdminCommand"
	remote.Parent = ReplicatedStorage
	remote.OnServerEvent:Connect(function(player: Player, text: unknown)
		if type(text) ~= "string" then
			return
		end
		local r = admin:Execute(player.UserId, text)
		if r.handled then
			reply(player.UserId, r.message)
		end
	end)

	local general = TextChatService:FindFirstChild("TextChannels")
	local rbxGeneral = general and general:FindFirstChild("RBXGeneral")
	if rbxGeneral and rbxGeneral:IsA("TextChannel") then
		rbxGeneral.ShouldDeliverCallback = function(message: TextChatMessage, _: TextSource): boolean
			local source = message.TextSource
			if source and string.sub(message.Text, 1, 1) == "/" then
				local r = admin:Execute(source.UserId, message.Text)
				if r.handled then
					reply(source.UserId, r.message)
					return false
				end
			end
			return true
		end
	end
end

return Service
