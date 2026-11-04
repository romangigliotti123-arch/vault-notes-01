--!nocheck
local t = require("../../../../../systems/_check/harness")
local SecretScan = require("../SecretScan")

local fakeKey = string.rep("a1b2", 8)

print("SecretScan")

t.test("api key header literal is critical and redacted", function()
	local f = SecretScan.scanText("ServerScriptService/Cloud.luau", `headers = \{ ["x-api-key"] = "{fakeKey}" \}`)
	t.eq(#f, 1)
	t.eq(f[1].severity, "CRITICAL")
	t.eq(f[1].line, 1)
	t.falsy(string.find(f[1].preview, fakeKey, 1, true))
	t.truthy(string.find(f[1].preview, "32 chars", 1, true))
end)

t.test("discord webhook url is critical", function()
	local f =
		SecretScan.scanText("a.luau", "local url = 'https://discord.com/api/webhooks/123456789/" .. fakeKey .. "'")
	t.eq(f[1].rule, "discord-webhook")
end)

t.test("placeholders and short values are ignored", function()
	t.eq(#SecretScan.scanText("a.luau", 'local apiKey = "YOUR_API_KEY_HERE"'), 0)
	t.eq(#SecretScan.scanText("a.luau", 'local token = "abc"'), 0)
	t.eq(#SecretScan.scanText("a.luau", 'local secret = "set in Creator Hub secrets"'), 0)
end)

t.test("commented-out secrets are skipped, but private key blocks are always reported", function()
	t.eq(#SecretScan.scanText("a.luau", `-- token = "{fakeKey}"`), 0)
	t.eq(#SecretScan.scanText("k.txt", "-----BEGIN RSA PRIV​ATE KEY-----"), 1)
end)

t.test("secret-named assignments are HIGH and report the right line", function()
	local f = SecretScan.scanText("a.luau", `local a = 1\nlocal webhookSecret = "{fakeKey}"\n`)
	t.eq(#f, 1)
	t.eq(f[1].line, 2)
	t.eq(f[1].severity, "HIGH")
end)

t.test("teleport data carrying a secret-ish name is flagged", function()
	local f = SecretScan.scanText("a.luau", "opts:SetTeleportData({ authToken = value })")
	t.eq(#f, 1)
	t.eq(#SecretScan.scanText("a.luau", "opts:SetTeleportData({ spawn = 'north' })"), 0)
end)

t.test("admin user id lists in client-readable scripts are flagged, server scripts are not", function()
	local code = "local ADMIN_IDS = { 1234567, 7654321 }"
	t.eq(#SecretScan.scanClientVisible("ReplicatedStorage/Config.luau", code), 1)
	t.eq(#SecretScan.scanClientVisible("ServerScriptService/Admin.luau", code), 0)
end)

t.test("report counts and never contains the value", function()
	local f = SecretScan.scanText("a.luau", `local apiKey = "{fakeKey}"`)
	local r = SecretScan.report(f)
	t.truthy(string.find(r, "1 findings", 1, true))
	t.falsy(string.find(r, fakeKey, 1, true))
	t.eq(SecretScan.report({}), "SECRETS: 0 findings (heuristic: not proof)")
end)

t.done()
