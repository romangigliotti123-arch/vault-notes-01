local CONFIG = {
	mode = "scan",
	root = "Workspace",
	chunk = 25,
	maxParts = 80000,
	afterApplyHook = nil,
}
local PLAN = nil

local ALLOWED = {
	CanQuery = "bool",
	CanTouch = "bool",
	CanCollide = "bool",
	Anchored = "bool",
	CastShadow = "bool",
	CollisionFidelity = "enum",
	RenderFidelity = "enum",
	Remove = "remove",
}
local VISUAL_PROPS = { CastShadow = true, RenderFidelity = true }
local HOLDER = "PerfPass_Removed"
local MARK = "PerfPass_OrigParent"

local HttpService = game:GetService("HttpService")
local function enc(v: any): string
	return HttpService:JSONEncode(v)
end
local function svc(name: string): any
	local ok, s = pcall(function()
		return game:GetService(name)
	end)
	return if ok then s else nil
end
local function rd(inst: any, prop: string): any
	local ok, v = pcall(function()
		return inst[prop]
	end)
	if ok then
		return v
	end
	return nil
end
local function num(n: number, d: number): number
	local m = 10 ^ d
	return math.floor(n * m + 0.5) / m
end
local function b(v: any): number
	return if v then 1 else 0
end
local function enumName(v: any): string
	if v == nil then
		return ""
	end
	return tostring(v.Name)
end
local function fnv(s: string): number
	local h = 2166136261
	for i = 1, #s do
		h = bit32.bxor(h, string.byte(s, i))
		h = (h * 16777619) % 4294967296
	end
	return h
end

local function ikey(inst: any): any
	local ok, k = pcall(function()
		return inst:GetDebugId()
	end)
	if ok and k then
		return k
	end
	return inst
end

local function resolve(path: string): any
	local cur: any = game
	for seg in string.gmatch(path, "[^%.]+") do
		cur = cur:FindFirstChild(seg)
		if not cur then
			return nil
		end
	end
	return cur
end

local KPROPS = {
	Decal = { "Texture", "Color3", "Transparency", "Face", "ZIndex" },
	Texture = {
		"Texture",
		"Color3",
		"Transparency",
		"Face",
		"ZIndex",
		"StudsPerTileU",
		"StudsPerTileV",
		"OffsetStudsU",
		"OffsetStudsV",
	},
	SurfaceAppearance = { "ColorMap", "NormalMap", "MetalnessMap", "RoughnessMap", "AlphaMode", "Color" },
	SpecialMesh = { "MeshId", "TextureId", "Scale", "Offset", "MeshType", "VertexColor" },
	BlockMesh = { "Scale", "Offset", "VertexColor" },
	CylinderMesh = { "Scale", "Offset", "VertexColor" },
	PointLight = { "Brightness", "Color", "Range", "Enabled", "Shadows" },
	SpotLight = { "Brightness", "Color", "Range", "Enabled", "Shadows", "Angle", "Face" },
	SurfaceLight = { "Brightness", "Color", "Range", "Enabled", "Shadows", "Angle", "Face" },
	ParticleEmitter = { "Texture", "Rate", "Enabled", "Lifetime", "Speed", "Size", "Color", "Transparency" },
	Fire = { "Enabled", "Color", "SecondaryColor", "Size", "Heat" },
	Smoke = { "Enabled", "Color", "Size", "Opacity", "RiseVelocity" },
	Sparkles = { "Enabled", "SparkleColor" },
}

local function kidSig(p: any): (string, string)
	local classes: { [string]: boolean } = {}
	local parts: { string } = {}
	for _, c in p:GetChildren() do
		classes[c.ClassName] = true
		local props = KPROPS[c.ClassName]
		if props then
			local bits = { c.ClassName }
			for _, pr in props do
				table.insert(bits, tostring(rd(c, pr)))
			end
			table.insert(parts, table.concat(bits, "|"))
		end
	end
	local names = {}
	for k in classes do
		table.insert(names, k)
	end
	table.sort(names)
	table.sort(parts)
	return table.concat(names, ","), tostring(fnv(table.concat(parts, "\n")))
end

local FIELDS_P = {
	"id",
	"pid",
	"cls",
	"name",
	"anch",
	"cc",
	"cq",
	"ct",
	"cs",
	"ml",
	"tr",
	"rf",
	"mat",
	"mv",
	"col",
	"shape",
	"sx",
	"sy",
	"sz",
	"cf",
	"cfid",
	"rfid",
	"meshid",
	"texid",
	"kids",
	"tags",
	"attrs",
	"ksig",
}
local FIELDS_C = { "id", "pid", "cls", "name", "kids", "tags", "attrs" }

local function partRow(p: any, id: number, pid: number): { any }
	local size = p.Size
	local kids, ksig = kidSig(p)
	local cfc = { p.CFrame:GetComponents() }
	for i, v in cfc do
		cfc[i] = num(v, 4)
	end
	local isMesh = p:IsA("MeshPart")
	return {
		id,
		pid,
		p.ClassName,
		p.Name,
		b(p.Anchored),
		b(p.CanCollide),
		b(rd(p, "CanQuery") ~= false),
		b(p.CanTouch),
		b(p.CastShadow),
		b(p.Massless),
		num(p.Transparency, 3),
		num(p.Reflectance, 3),
		enumName(p.Material),
		tostring(rd(p, "MaterialVariant") or ""),
		p.Color:ToHex(),
		if p:IsA("Part") then enumName(rd(p, "Shape")) else "",
		num(size.X, 3),
		num(size.Y, 3),
		num(size.Z, 3),
		cfc,
		if isMesh or p:IsA("PartOperation") then enumName(rd(p, "CollisionFidelity")) else "",
		if isMesh then enumName(rd(p, "RenderFidelity")) else "",
		if isMesh then tostring(rd(p, "MeshId") or "") else "",
		if isMesh then tostring(rd(p, "TextureID") or "") else "",
		kids,
		#p:GetTags(),
		(function()
			local n = 0
			for _ in p:GetAttributes() do
				n += 1
			end
			return n
		end)(),
		ksig,
	}
end

local function containerRow(c: any, id: number, pid: number): { any }
	local kids = kidSig(c)
	local n = 0
	for _ in c:GetAttributes() do
		n += 1
	end
	return { id, pid, c.ClassName, c.Name, kids, #c:GetTags(), n }
end

local function index(root: any)
	local list: { any } = {}
	local idOf: { [any]: number } = {}
	for _, d in root:GetDescendants() do
		if d:IsA("Terrain") then
			continue
		end
		if d:IsA("BasePart") or #d:GetChildren() > 0 then
			table.insert(list, d)
			idOf[ikey(d)] = #list
			if #list >= CONFIG.maxParts then
				break
			end
		end
	end
	return list, idOf
end

local function fingerprint(list: { any }): string
	local bits = table.create(#list)
	for i, d in list do
		bits[i] = i .. ":" .. d.ClassName .. ":" .. d.Name
	end
	return tostring(fnv(table.concat(bits, "\n")))
end

local function emit(tag: string, rows: { any })
	local i = 1
	while i <= #rows do
		local slice = table.move(rows, i, math.min(i + CONFIG.chunk - 1, #rows), 1, {})
		print(tag .. " " .. enc({ rows = slice }))
		i += CONFIG.chunk
	end
end

local KOUT = {
	"Raycast",
	"Spherecast",
	"Blockcast",
	"Shapecast",
	"GetPartBoundsInBox",
	"GetPartBoundsInRadius",
	"GetPartsInPart",
	"FindPartOnRay",
	"FindPartOnRayWithIgnoreList",
	"FindPartOnRayWithWhitelist",
	"FindPartsInRegion3",
	"FindPartsInRegion3WithIgnoreList",
	"FindPartsInRegion3WithWhiteList",
	"ViewportPointToRay",
	"ScreenPointToRay",
	"Target",
}
local KTOUCH = { "Touched", "TouchEnded", "GetTouchingParts" }
local KBULK = {
	"GetDescendants",
	"GetChildren",
	"GetTagged",
	"HumanoidRootPart",
	"LeftFoot",
	"RightFoot",
	"Character",
	"LowerTorso",
	"Torso",
	"Head",
}

local function strip(src: string): string
	for _, pat in
		{
			"Instance%.new%s*%b()",
			":IsA%s*%b()",
			"FindFirstChildOfClass%s*%b()",
			"FindFirstChildWhichIsA%s*%b()",
			"FindFirstAncestorOfClass%s*%b()",
			"FindFirstAncestorWhichIsA%s*%b()",
		}
	do
		src = string.gsub(src, pat, "")
	end
	return src
end

local function scriptInfo()
	local tokens: { [string]: boolean } = {}
	local strs: { [string]: boolean } = {}
	local info = { n = 0, unreadable = 0 }
	for _, s in game:GetDescendants() do
		if s:IsA("LuaSourceContainer") then
			info.n += 1
			local ok, src = pcall(function()
				return s.Source
			end)
			if not ok or type(src) ~= "string" then
				info.unreadable += 1
			else
				src = strip(src)
				for w in string.gmatch(src, "[%w_]+") do
					tokens[w] = true
				end
				for q in string.gmatch(src, '"([^"\n]*)"') do
					strs[q] = true
				end
				for q in string.gmatch(src, "'([^'\n]*)'") do
					strs[q] = true
				end
			end
		end
	end
	return tokens, strs, info
end

local function anyToken(tokens: { [string]: boolean }, list: { string }): boolean
	for _, k in list do
		if tokens[k] then
			return true
		end
	end
	return false
end

local function nameReferenced(name: string, tokens: { [string]: boolean }, strs: { [string]: boolean }): boolean
	local function hit(n: string): boolean
		if strs[n] then
			return true
		end
		local any = false
		for w in string.gmatch(n, "[%w_]+") do
			any = true
			if not tokens[w] then
				return false
			end
		end
		return any
	end
	if hit(name) then
		return true
	end
	local base = string.gsub(name, "[%d_%s]+$", "")
	return #base >= 3 and base ~= name and hit(base)
end

local REFPROPS = { "Part0", "Part1", "Attachment0", "Attachment1", "PrimaryPart", "Value", "Adornee" }
local function refTargets(root: any, idOf: { [any]: number }): { number }
	local seen: { [number]: boolean } = {}
	local out = {}
	for _, d in root:GetDescendants() do
		if
			d:IsA("JointInstance")
			or d:IsA("WeldConstraint")
			or d:IsA("Constraint")
			or d:IsA("Model")
			or d:IsA("ObjectValue")
			or d:IsA("Beam")
			or d:IsA("Trail")
			or d:IsA("Highlight")
			or d:IsA("SelectionBox")
			or d:IsA("GuiBase3d")
			or d:IsA("BillboardGui")
			or d:IsA("SurfaceGui")
		then
			for _, pr in REFPROPS do
				local v = rd(d, pr)
				if typeof(v) == "Instance" then
					local t: any = v
					if t:IsA("Attachment") then
						t = t.Parent
					end
					local id = t and idOf[ikey(t)]
					if id and not seen[id] then
						seen[id] = true
						table.insert(out, id)
					end
				end
			end
		end
	end
	table.sort(out)
	return out
end

local function counts(root: any)
	local c = {
		lights = 0,
		lightsShadow = 0,
		emitters = 0,
		emitterRate = 0,
		beams = 0,
		trails = 0,
		fx = 0,
		decals = 0,
		textures = 0,
		surfaceAppearance = 0,
		specialMesh = 0,
		sounds = 0,
		meshParts = 0,
		unions = 0,
		transparent = 0,
	}
	local meshIds: { [string]: number } = {}
	for _, d in root:GetDescendants() do
		if d:IsA("Light") then
			c.lights += 1
			c.lightsShadow += b(rd(d, "Shadows"))
		elseif d:IsA("ParticleEmitter") then
			c.emitters += 1
			c.emitterRate += tonumber(rd(d, "Rate")) or 0
		elseif d:IsA("Beam") then
			c.beams += 1
		elseif d:IsA("Trail") then
			c.trails += 1
		elseif d:IsA("Fire") or d:IsA("Smoke") or d:IsA("Sparkles") then
			c.fx += 1
		elseif d:IsA("Decal") then
			c.decals += 1
		elseif d:IsA("Texture") then
			c.textures += 1
		elseif d:IsA("SurfaceAppearance") then
			c.surfaceAppearance += 1
		elseif d:IsA("SpecialMesh") then
			c.specialMesh += 1
		elseif d:IsA("Sound") then
			c.sounds += 1
		elseif d:IsA("MeshPart") then
			c.meshParts += 1
			local m = tostring(rd(d, "MeshId") or "")
			meshIds[m] = (meshIds[m] or 0) + 1
		elseif d:IsA("PartOperation") then
			c.unions += 1
		end
		if d:IsA("BasePart") and d.Transparency > 0 and d.Transparency < 1 then
			c.transparent += 1
		end
	end
	local top = {}
	for m, n in meshIds do
		table.insert(top, { m, n })
	end
	table.sort(top, function(x, y)
		return x[2] > y[2]
	end)
	c.topMeshIds = table.move(top, 1, math.min(#top, 8), 1, {})
	c.distinctMeshIds = #top
	return c
end

local function statsBlock(): any
	local out: { [string]: any } = {}
	local st = svc("Stats")
	if st then
		for _, k in { "InstanceCount", "PrimitivesCount", "MovingPrimitivesCount", "ContactsCount" } do
			out[k] = rd(st, k)
		end
		local ok, mb = pcall(function()
			return st:GetTotalMemoryUsageMb()
		end)
		out.memoryMb = if ok then num(mb, 1) else nil
	end
	local ws = svc("Workspace")
	if ws then
		out.streamingEnabled = rd(ws, "StreamingEnabled")
		out.streamingTargetRadius = rd(ws, "StreamingTargetRadius")
		out.streamingMinRadius = rd(ws, "StreamingMinRadius")
	end
	return out
end

local function rowsFor(list: { any }, idOf: { [any]: number }, onlyPresent: boolean?, rootInst: any)
	local prow, crow = {}, {}
	for id, d in list do
		if onlyPresent and not d:IsDescendantOf(rootInst) then
			continue
		end
		local par = d.Parent
		local pid = (par and idOf[ikey(par)]) or 0
		if d:IsA("BasePart") then
			table.insert(prow, partRow(d, id, pid))
		else
			table.insert(crow, containerRow(d, id, pid))
		end
	end
	return prow, crow
end

local function scan(phase: string, rootInst: any, list: { any }, idOf: { [any]: number }, extra: any?)
	local prow, crow = rowsFor(list, idOf, phase == "after", rootInst)
	local head: { [string]: any } = {
		version = 1,
		phase = phase,
		game = game.Name,
		placeId = game.PlaceId,
		root = CONFIG.root,
		capturedAt = os.date("!%Y-%m-%dT%H:%M:%SZ"),
		fingerprint = fingerprint(list),
		nparts = #prow,
		ncontainers = #crow,
		fieldsP = FIELDS_P,
		fieldsC = FIELDS_C,
		capped = #list >= CONFIG.maxParts,
		stats = statsBlock(),
		counts = counts(rootInst),
	}
	if phase == "before" then
		local tokens, strs, info = scriptInfo()
		local names: { [string]: boolean } = {}
		for _, d in list do
			names[d.Name] = true
		end
		local refd = {}
		for n in names do
			if nameReferenced(n, tokens, strs) then
				table.insert(refd, n)
			end
		end
		table.sort(refd)
		head.scripts = { n = info.n, unreadable = info.unreadable }
		head.refnames = refd
		head.queryApi = anyToken(tokens, KOUT)
		head.bulkTouch = anyToken(tokens, KTOUCH) and anyToken(tokens, KBULK)
		head.jointRefs = refTargets(rootInst, idOf)
	end
	if extra then
		head.apply = extra
	end
	print("PERF_SCAN " .. enc(head))
	emit("PERF_P", prow)
	emit("PERF_C", crow)
	print("PERF_END " .. enc({ phase = phase, nparts = #prow, ncontainers = #crow }))
end

local function holder(create: boolean): any
	local ss = svc("ServerStorage")
	if not ss then
		return nil
	end
	local h = ss:FindFirstChild(HOLDER)
	if not h and create then
		h = Instance.new("Folder")
		h.Name = HOLDER
		h.Parent = ss
	end
	return h
end

local function setValue(inst: any, prop: string, value: any)
	if ALLOWED[prop] == "enum" then
		inst[prop] = Enum[prop][value]
	else
		inst[prop] = value
	end
end
local function curValue(inst: any, prop: string): any
	local v = rd(inst, prop)
	if ALLOWED[prop] == "enum" then
		return enumName(v)
	end
	return v
end

local function waypoint(name: string)
	local cs = svc("ChangeHistoryService")
	if cs then
		pcall(function()
			cs:SetWaypoint(name)
		end)
	end
end

local function visualTuple(row: { any }): string
	local bits = {}
	for i, v in row do
		local f = FIELDS_P[i]
		if
			f ~= "id"
			and f ~= "pid"
			and f ~= "anch"
			and f ~= "cc"
			and f ~= "cq"
			and f ~= "ct"
			and f ~= "ml"
			and f ~= "cfid"
		then
			bits[#bits + 1] = if type(v) == "table" then table.concat(v, ",") else tostring(v)
		end
	end
	return table.concat(bits, "|")
end

local function runApply(rootInst: any, list: { any }, idOf: { [any]: number })
	if PLAN.fingerprint ~= fingerprint(list) then
		print("PERF_APPLY " .. enc({
			status = "REFUSED",
			reason = "the game changed since the scan (fingerprint differs): scan again, then plan again",
		}))
		return
	end
	local allowVisual: { [string]: boolean } = {}
	for _, p in PLAN.allowVisual or {} do
		allowVisual[p] = true
	end
	local before: { [number]: string } = {}
	local clsOf: { [number]: string } = {}
	for id, d in list do
		if d:IsA("BasePart") then
			before[id] = visualTuple(partRow(d, id, 0))
			clsOf[id] = d.ClassName
		end
	end
	waypoint("PerfPass: before")
	local undo = {}
	local removed = {}
	local skipped = {}
	local applied = 0
	for _, item in PLAN.items do
		local kind = ALLOWED[item.prop]
		if not kind then
			table.insert(skipped, { rule = item.rule, reason = "property not allowed: " .. tostring(item.prop) })
			continue
		end
		if VISUAL_PROPS[item.prop] and not allowVisual[item.prop] then
			table.insert(skipped, { rule = item.rule, reason = "visual property without approval: " .. item.prop })
			continue
		end
		for _, id in item.ids do
			local inst = list[id]
			if not inst or not inst.Parent then
				table.insert(skipped, { id = id, reason = "gone" })
			elseif kind == "remove" then
				local h = holder(true)
				local mk = Instance.new("ObjectValue")
				mk.Name = MARK
				mk.Value = inst.Parent
				mk.Parent = inst
				table.insert(removed, { inst = inst, parent = inst.Parent, mark = mk })
				inst.Parent = h
				applied += 1
			elseif curValue(inst, item.prop) ~= item.from then
				table.insert(skipped, { id = id, reason = "current value differs from the scan" })
			else
				table.insert(undo, { inst = inst, prop = item.prop, old = item.from })
				setValue(inst, item.prop, item.to)
				applied += 1
			end
		end
	end
	if CONFIG.afterApplyHook then
		CONFIG.afterApplyHook(list, idOf)
	end
	local visualOK: { [number]: boolean } = {}
	for _, item in PLAN.items do
		if VISUAL_PROPS[item.prop] and allowVisual[item.prop] then
			for _, id in item.ids do
				visualOK[id] = true
			end
		end
	end
	local failByClass: { [string]: number } = {}
	local checkedByClass: { [string]: number } = {}
	local removedSet = {}
	for _, r in removed do
		removedSet[r.inst] = true
	end
	for id, d in list do
		local was = before[id]
		if was and not removedSet[d] then
			local c = clsOf[id]
			checkedByClass[c] = (checkedByClass[c] or 0) + 1
			if visualTuple(partRow(d, id, 0)) ~= was then
				local explained = visualOK[id] == true
				if not explained then
					failByClass[c] = (failByClass[c] or 0) + 1
				end
			end
		end
	end
	local bad = 0
	local lines = {}
	for c, n in checkedByClass do
		local f = failByClass[c] or 0
		bad += f
		table.insert(
			lines,
			string.format("APPEARANCE %s %s (%d checked, %d differ)", c, if f == 0 then "PASS" else "FAIL", n, f)
		)
	end
	table.sort(lines)
	for _, l in lines do
		print(l)
	end
	local status = "APPLIED"
	if bad > 0 then
		for i = #undo, 1, -1 do
			pcall(setValue, undo[i].inst, undo[i].prop, undo[i].old)
		end
		for _, r in removed do
			r.inst.Parent = r.parent
			r.mark:Destroy()
		end
		status = "REVERTED"
		applied = 0
		print("APPEARANCE DIFF FAIL: " .. bad .. " part(s) differ, everything was put back")
	else
		print("APPEARANCE DIFF PASS: no rendering property of any surviving part changed")
		waypoint("PerfPass: applied")
	end
	print("PERF_APPLY " .. enc({ status = status, applied = applied, skipped = skipped, differ = bad }))
	scan("after", rootInst, list, idOf, { status = status })
end

local function runRevert(rootInst: any)
	local h = holder(false)
	local marked = {}
	if h then
		for _, c in h:GetChildren() do
			if c:FindFirstChild(MARK) then
				table.insert(marked, c)
			end
		end
	end
	local removedIds = if #marked > 0 and PLAN and PLAN.removed then PLAN.removed else {}
	local function shifted(id: number): number
		local lo, hi = 1, #removedIds
		local below = 0
		while lo <= hi do
			local mid = (lo + hi) // 2
			if removedIds[mid] < id then
				below = mid
				lo = mid + 1
			else
				hi = mid - 1
			end
		end
		return id - below
	end
	local list = index(rootInst)
	local restored, guarded = 0, 0
	if PLAN then
		for _, item in PLAN.items do
			if ALLOWED[item.prop] and item.prop ~= "Remove" then
				for _, id in item.ids do
					local inst = list[shifted(id)]
					if not inst or (PLAN.names and PLAN.names[tostring(id)] ~= inst.ClassName .. ":" .. inst.Name) then
						guarded += 1
					elseif curValue(inst, item.prop) == item.from then
						setValue(inst, item.prop, item.to)
						restored += 1
					end
				end
			end
		end
	end
	local back = 0
	for _, c in marked do
		local mk = c:FindFirstChild(MARK)
		if mk and mk.Value then
			c.Parent = mk.Value
			mk:Destroy()
			back += 1
		end
	end
	if h and #h:GetChildren() == 0 then
		h:Destroy()
	end
	waypoint("PerfPass: reverted")
	print("PERF_REVERT " .. enc({
		status = if guarded == 0 then "OK" else "PARTIAL",
		restoredParts = back,
		restoredValues = restored,
		skippedByGuard = guarded,
	}))
end

local rootInst = resolve(CONFIG.root)
assert(rootInst, "root not found: " .. tostring(CONFIG.root))
local list, idOf = index(rootInst)
if CONFIG.mode == "scan" then
	scan("before", rootInst, list, idOf)
	print(
		"PERF: scan done ("
			.. #list
			.. " nodes). Next: python perf_gate.py analyze <this output saved as a text file> --game <name>"
	)
elseif CONFIG.mode == "apply" then
	assert(PLAN, "mode apply needs the PLAN that perf_gate.py plan writes into perf_apply.luau")
	runApply(rootInst, list, idOf)
elseif CONFIG.mode == "revert" then
	runRevert(rootInst)
end
