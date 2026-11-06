---
name: rbx-idea-creator
description: "Start from YOUR idea: '/rbx-idea-creator <idea>' revamps your own game idea into a full rated card (hook, retention, week 1, money, build ease), or with no idea it guides you with a few multiple-choice questions (category first, then finer ones) and builds the idea for you. Use for 'I have a game idea', 'help me come up with a game idea', 'guide me'."
argument-hint: "[your game idea, or leave empty to be guided]"
---

# Roblox idea creator

Takes the user's own idea (or guides them to one), develops the best variation of it, and shows the same short card as `rbx-ideas`. The pipeline is NOT repeated here: read the **Engine** section of `rbx-ideas` (`~/.claude/claude-kit/vault-mode/.claude/skills/rbx-ideas/SKILL.md` or the installed `rbx-ideas` skill, via the Skill tool or Read) and follow its steps, hard rules, defaults, saved-file format, card and "After the card" replies exactly. Difference: the seed comes from the user instead of the charts. Not for "what should I build" with no input from the user: that is `rbx-ideas`.

## With an idea (`/rbx-idea-creator <idea>`)

1. Keep their idea as the core; the Notes line under the TL;DR says `Using your idea: <idea in one line>`. Do not ask them to restate it or to answer questions; assume the defaults.
2. Run the rbx-ideas Engine on it. The sparks (step 2) are about 12 VARIATIONS that keep the user's core fantasy and verb and change the twist, constraint, social shape or setting; the same tests and banned list apply to the added twist, not to the user's core (never ban their idea for being a tycoon or an obby, but change what makes it generic). The user's idea overrides the engine's lane rule: a co-op or party idea stays co-op; the lane line in the Category then says so. Pick the single best variation (the engine's pick step; no menu, no pick turn), then develop it: sharpen the hook, fix the first 30 seconds, add a D1 reason, week-1 loop, ethical money, build ease. If the idea is a chart clone, say so in one line and change only what is needed to give it a new verb or combination (Keeps | New), staying as close to the user's intent as possible. If it breaks a hard rule, say which and offer the closest allowed version.
3. Same critic with novelty scoring and slop gate (rbx-judge, or `No independent critic - self-review only` in the Notes line when agents are unavailable; print nothing while it runs), red-team and saved file `research/idea-<slug>.md`; show the card (cap 40 lines, TL;DR as the first line, exactly one Done/You/Next footer).

## Without an idea (guided funnel)

Ask ONE question per round. With the AskUserQuestion tool: 4 fixed options plus "Surprise me" as a 5th that is not counted (the tool adds Other itself). Without it: a numbered list in plain text, up to 6 options plus "Surprise me", and say once that you are using a list. A skip is always fine: it means Claude picks the strongest option for the earlier answers and applies the default. Maximum 5 questions in total, each narrowing from the last. Keep questions and options short.

1. **Category** (always first). Options lead with the lanes of the rbx-ideas Engine, in this order: single-player adventure or RPG · open-world survival or crafting · open-world social hangout or MMO-lite · simulator or collector · obby or parkour (solo) · horror (solo) · co-op or party (needs friends) as ONE option among the rest · Other (type it). With a 4-option tool: the first 4 plus "More..." for the rest, never more than 2 screens. A skipped or "Surprise me" answer picks a single-player or open-world option, never co-op.
2. **Core fantasy** inside that category (for example, for a tycoon: run a shop, build a base, manage a team; for a voice-chat game: party game, hangout, mystery or detective).
3. **Play style**: solo, open world with optional friends, co-op with friends, or drop-in with strangers (default: solo or open world with optional friends; friends-only is the safe default for any social part).
4. **Session length**: 5 minutes, 15 minutes, or long sessions.
5. **Audience** (age band; all ages is the default, younger skews to easier progression).

Art and scope default to cartoon low-poly and money to cosmetics plus convenience passes; ask about them only if the user raises them or a skipped round left the choice open. Rounds after the first use options that depend on the earlier answers (not a fixed list). Stop early once category, fantasy and audience are known; every skipped round gets its default. Record each round in the saved file under `## Funnel answers` (answer, or `skipped -> default applied`). Voice chat is age-gated on Roblox and not available to all users: for a voice-chat idea give it an optional, non-essential role and a text-free fallback so the game works without it. Then run the Engine with the Notes line `Building your idea from: <answers in one line>` (under the TL;DR, part of the card template), with the answers as constraints (the sparks are fresh ideas that fit the answers, or variations of the user's idea), the one pick, the critic, the saved file and the card. Defaults never drift to co-op: an unanswered social shape means solo or open world.

## After the card

Same as rbx-ideas: "build it" creates `Games/<slug>/` with the seeded README (`games.py init <slug> --from-idea research/idea-<slug>.md`), "another" gives one different idea from the same answers (same lane rule), "plan" runs Phase B of rbx-ideas.

## Self-check

- [ ] The idea (or the funnel answers) is visibly the core of the card; the Engine's self-check of rbx-ideas passes.
- [ ] Funnel: category asked first, at most 5 rounds, each skippable with "Surprise me", options depend on earlier answers, no wall of questions in one message.
- [ ] No pipeline logic was copied here: the card, critic and saved file come from the rbx-ideas Engine.
