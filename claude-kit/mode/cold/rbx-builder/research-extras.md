<!-- cold: rbx-builder/research-extras.md | read when: read only when kbq route/case/find results are thin for the genre or you need Manager conventions or a Library pick. -->

## From agents/rbx-builder.md :: 4. Creator playbooks: `rg -il "<genre word>" "$VAULT/Roblox"

4. Creator playbooks: `rg -il "<genre word>" "$VAULT/Roblox" --glob "*How to make successful Roblox games.md" | head`, open the top of at most 3; official genre playbook if present: `ls "$VAULT/Roblox/docs/Videos" | grep -i "<obby|tycoon|simulator|rpg|shooter|survival|sports|incremental>"`.
5. How to work: `head -n 60 "$VAULT/Manager/Manager-README.md"` and `rg -n "^#+ " "$VAULT/Manager/PROPOSALS.md" | head -40` (conventions only; skip if absent). Find a skill or agent: `ls "$VAULT/Library/skills/roblox" "$VAULT/Library/agents/roblox"`, or `rg -i "<words>" "$VAULT/Library/PICKS.md"`.
