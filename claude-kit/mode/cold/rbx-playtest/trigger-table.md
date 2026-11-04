<!-- cold: rbx-playtest/trigger-table.md | read when: a trigger-scan lead (static_scan.py --triggers) needs explaining or you extend the TRIGGERS table. -->

# Token-triggered checks (research round 2; the idea of a token-to-checklist scan comes from a public Luau optimiser skill without a licence, so the table and wording are ours)

`static_scan.py --triggers` reads each Luau file once. A code token opens the SE check that matters for it, and a lead is only raised when the usual guard is missing in that file. Output per lead: `path:line  SE-n  what breaks -> fix`. Order and cost: TR1 exploits and data loss (3.0 per lead), TR2 crashes (2.0), TR3 leaks (1.0), TR4 performance and hygiene (0.5); pass mark 7 per tier; scored, never a block.

| token seen | opens | raised when the file lacks / has | tier |
|---|---|---|---|
| `OnServerEvent`/`OnServerInvoke` handler arg named price, cost, reward, payout | SE-9 | always: the value must come from server config | TR1 |
| remote handler | SE-4 | no clock, cooldown or debounce token | TR1 |
| `ProcessReceipt` | SE-10 | no `PurchaseId` | TR1 |
| `GetAsync`/`SetAsync`/`UpdateAsync` | SE-11 | no ProfileStore, session or lock word | TR1 |
| `SetAsync`/`UpdateAsync` | SE-14 | one of the previous 8 lines is Heartbeat, RenderStepped, Stepped, `.Changed` | TR1 |
| `GetDataStore`/`DataStoreService` | SE-15 | no `BindToClose` | TR1 |
| `typeof(x) == "number"` or `tonumber(` in a file with a remote handler | SE-12 | no `n ~= n`, `math.huge` or `isfinite` | TR2 |
| `:InvokeClient(` | SE-13 | always | TR2 |
| `PlayerAdded:Connect` | SE-18 | no `GetPlayers()` | TR2 |
| `workspace.A.B` in client code | SE-19 | no `WaitForChild` | TR2 |
| `[player] =` / `[plr] =` | SE-16 | no `PlayerRemoving` and no `[player] = nil` | TR3 |
| `CharacterAdded:Connect` | SE-17 | no Disconnect, Destroy, Cleaner, Maid, Janitor, Trove, Once, CharacterRemoving | TR3 |
| indented `Heartbeat/RenderStepped/Stepped/Touched/.Changed:Connect` | SE-2 | same cleanup words absent | TR3 |
| `FireClient/FireAllClients/FireServer` | SE-20 | one of the previous 8 lines is Heartbeat, RenderStepped, Stepped | TR4 |
| `Touched:Connect` with a remote fired in the next 8 lines | SE-20 | no debounce token | TR4 |
| handler whose 2nd arg is action, cmd, command, op, kind | SE-21 | always | TR4 |
| `wait(`, `spawn(`, `delay(` | SE-25 | always | TR4 |
| `Instance.new("X", parent)` | SE-27 | always | TR4 |
| `LoadAnimation(` | SE-28 | no `Animator` in the file | TR4 |
| `:: any` | SE-30 | always | TR4 |

Rules for the table: every row names an existing rbx-code-rate check id; a new row needs a seeded-bad and a clean fixture in `netlify-site/tools/test_research2.py`; comments are stripped before matching; at most 5 leads per rule per file. The scan is a heuristic: the kit systems showed no tier 1-3 leads and five `:: any` casts (deliberate in UpdateAsync callbacks), which is why every lead needs a TRUE/FALSE-POSITIVE verdict first (`rbx-playtest/fp-verdict.md`).
