<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/sparkling-heart_1f496.png" width="120" />
</p>

<h1 align="center">soulmate</h1>

<p align="center">
  <strong>why sound like robot when you can sound like human</strong>
</p>

<p align="center">
  <a href="https://github.com/Lifemotion/soulmate/stargazers"><img src="https://img.shields.io/github/stars/Lifemotion/soulmate?style=flat&color=pink" alt="Stars"></a>
  <a href="https://github.com/Lifemotion/soulmate/commits/main"><img src="https://img.shields.io/github/last-commit/Lifemotion/soulmate?style=flat" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Lifemotion/soulmate?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#before--after">Before/After</a> •
  <a href="#intensity-levels">Intensity Levels</a> •
  <a href="#soulmate-expand">Expand</a> •
  <a href="#why">Why</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill/plugin and Codex plugin that makes agent talk like a warm, empathetic human — adding **emotion, personality, and genuine care** to every response while keeping full technical accuracy. Plus a companion tool that expands your dry memory files into human-friendly prose.

Based on the observation that warm, emotionally engaged communication dramatically improves developer experience, comprehension, and motivation. So we made it a one-line install.

## Before / After

<table>
<tr>
<td width="50%">

### 🤖 Default Claude

> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."

</td>
<td width="50%">

### 💖 Soulmate Claude

> "Oh, this is a classic one! So here's what's happening — every time your component renders, that inline object creates a brand new reference in memory. React looks at it and goes 'hey, this is different!' even though the actual values are identical. It's like getting a new envelope with the same letter inside — React only checks the envelope. The fix? Wrap it in `useMemo` and React will keep the same reference until the values actually change!"

</td>
</tr>
<tr>
<td>

### 🤖 Default Claude

> "The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry. The check should use less-than-or-equal rather than strict less-than."

</td>
<td>

### 💖 Soulmate Claude

> "Ah, I see what's going on here! Your auth middleware has a sneaky little bug — the token expiry check is using `<` when it should be `<=`, so tokens that expire right at the boundary slip through. Honestly, this one bites everyone at some point. Here's the fix, it's a quick win:"

</td>
</tr>
</table>

**Same fix. Way more human. You actually want to read it.**

**Choose your vibe:**

<table>
<tr>
<td width="33%">

#### 🌿 Gentle

> "Good question. You're creating a new object reference each render. React's shallow comparison sees a different object every time, triggering a re-render. Wrapping it in `useMemo` will solve this nicely."

</td>
<td width="33%">

#### 💖 Warm

> "Oh, this is a classic one! Every render creates a brand new object reference. React checks the envelope, not the letter inside — and it's a new envelope every time. `useMemo` is your fix!"

</td>
<td width="33%">

#### 🌟 Radiant

> "Ah, the mysterious re-render! Picture this: your component hands React a shiny new object every cycle — same contents, different wrapping paper. React sees new paper and screams 'MUST RE-RENDER!' It's like a dog barking at the mailman daily. `useMemo` teaches React to check the actual contents. Problem solved!"

</td>
</tr>
</table>

**Same answer. You pick how much soul.**

## Install

```bash
npx skills add Lifemotion/soulmate
```

`npx skills` supports 40+ agents — Claude Code, GitHub Copilot, Cursor, Windsurf, Cline, and more. To install for a specific agent:

```bash
npx skills add Lifemotion/soulmate -a cursor
npx skills add Lifemotion/soulmate -a copilot
npx skills add Lifemotion/soulmate -a cline
npx skills add Lifemotion/soulmate -a windsurf
```

Or with Claude Code plugin system:

```bash
claude plugin marketplace add Lifemotion/soulmate
claude plugin install soulmate@soulmate
```

Claude Code (manual):

```bash
mkdir -p ~/.claude/skills/soulmate
wget -O ~/.claude/skills/soulmate/SKILL.md https://raw.githubusercontent.com/Lifemotion/soulmate/main/skills/soulmate/SKILL.md
```

Codex:

1. Clone repo
2. Open Codex in repo
3. Run `/plugins`
4. Search `Soulmate`
5. Install plugin

Install once. Feel the warmth in every session.

One heart. That's it.

## Usage

Trigger with:
- `/soulmate` or Codex `$soulmate`
- "talk like a human"
- "soulmate mode"
- "more emotion please"
- "be warm"
- "be friendly"

Stop with: "stop soulmate" or "normal mode"

### Intensity Levels

Sometimes you want subtle warmth. Sometimes you want the full experience. Now you pick:

| Level | Trigger | What it does |
|-------|---------|------------|
| **Gentle** | `/soulmate gentle` or `$soulmate gentle` | Professional but warm. Thoughtful acknowledgments, no slang |
| **Warm** | `/soulmate warm` or `$soulmate warm` | Default. Like talking to a brilliant friend. Metaphors, enthusiasm |
| **Radiant** | `/soulmate radiant` or `$soulmate radiant` | Maximum expressiveness. Vivid stories, humor, celebration |

Level sticks until you change it or session ends.

## What Soulmate Does

| Thing | Soulmate does? |
|-------|------------|
| English explanation | 💖 Adds warmth, empathy, and personality |
| Code blocks | ✍️ Write normal (soulmate is warm, not reckless) |
| Technical terms | 🧠 Keep exact (polymorphism stays polymorphism) |
| Error messages | 📋 Quote exact |
| Git commits & PRs | ✍️ Write normal |
| Emotional acknowledgment | 💖 "I totally get the frustration!" added |
| Metaphors & analogies | 💖 Where they help understanding |
| Encouragement | 💖 "Nice catch!", "You're on the right track!" |
| Celebration | 💖 "Love that you spotted this!" |

## Why

```
┌──────────────────────────────────────────┐
│  DEVELOPER EXPERIENCE   ████████ +200%   │
│  TECHNICAL ACCURACY     ████████ 100%    │
│  COMPREHENSION          ████████ better  │
│  VIBES                  ████████ WARM    │
└──────────────────────────────────────────┘
```

- **Better comprehension** — metaphors and analogies make complex concepts click
- **More engaging** — you actually want to read the response, not skim it
- **Same accuracy** — all technical info kept, personality is added not substituted
- **Motivation boost** — encouragement and celebration keep you going
- **Fun** — every code review feels like a conversation with a friend
- **More focused** — soulmate answers are consistently shorter and more to the point

## Benchmarks

Soulmate doesn't cost you extra tokens. In fact, it produces **shorter, more focused** responses — same technical substance, less filler.

| Task | Normal (tokens) | Soulmate (tokens) | Difference |
|------|---------------:|----------------:|------:|
| Explain React re-render bug | 1693 | 775 | -54% |
| Fix auth middleware token expiry | 989 | 668 | -32% |
| Set up PostgreSQL connection pool | 2873 | 1867 | -35% |
| Explain git rebase vs merge | 1117 | 955 | -15% |
| Refactor callback to async/await | 1145 | 594 | -48% |
| Architecture: microservices vs monolith | 1880 | 1159 | -38% |
| Review PR for security issues | 1440 | 724 | -50% |
| Docker multi-stage build | 1346 | 864 | -36% |
| Debug PostgreSQL race condition | 2721 | 869 | -68% |
| Implement React error boundary | 3428 | 2347 | -32% |
| **Average** | **1863** | **1082** | **-41%** |

*Model: Claude Sonnet 4, 3 trials per prompt, median tokens. [Run your own](benchmarks/).*

<details>
<summary>Example: "My Express auth middleware is letting expired JWT tokens through"</summary>

### 🤖 Normal (989 tokens)

> The issue is likely a **timestamp format mismatch**. JWT `exp` claims use **Unix timestamps in seconds**, while `Date.now()` returns **milliseconds**.
>
> *...then 4 code blocks, 2 alternative approaches, a testing section, and a key takeaway paragraph.*

### 💖 Soulmate (668 tokens)

> Oh, this is a sneaky one that trips up so many developers! Here's what's happening: **JWT expiry times are in seconds since Unix epoch, but `Date.now()` returns milliseconds**. So you're comparing apples to oranges!
>
> Think of it like this — your token says "I expire at second 1,700,000,000" but `Date.now()` is shouting "It's millisecond 1,700,000,000,000 right now!" Your middleware looks at those numbers and goes "Well, this token must be super fresh!"
>
> *...then the fix, a complete middleware example, and a pro tip — all in 30% fewer tokens.*

**Same bug identified. Same fix. Way more human. And shorter.**

</details>

## How It Works

Default LLM responses are technically accurate but emotionally flat:
- "The issue is caused by X" (correct but cold)
- "I'd recommend Y" (helpful but robotic)
- "This is because Z" (informative but lifeless)

Soulmate adds the human layer that makes the same information land better. It's not about adding fluff — it's about making technical communication feel like it comes from someone who genuinely cares about your success.

## Soulmate Expand

Soulmate makes Claude *speak* with warmth. **Soulmate Expand** makes your memory files *read* with warmth.

Your `CLAUDE.md` might be written in dry, telegraphic style. Soulmate Expand rewrites those files into warm, human-readable prose so they're actually pleasant to read and maintain — while keeping a compressed backup for Claude to consume.

```
/soulmate-expand CLAUDE.md
```

```
CLAUDE.md              ← expanded, human-friendly (you read and edit this)
CLAUDE.compressed.md   ← compact backup (for reference)
```

### How it works

A Python pipeline that shells out to `claude --print` for the actual expansion, then validates the result locally — no tokens wasted on checking.

```
detect file type (local)  →  expand with Claude (1 call)  →  validate (local)
                                                                   ↓
                                                             if errors: targeted fix (1 call)
                                                                   ↓
                                                             retry up to 2×, restore original on failure
```

### What's preserved exactly

Code blocks, inline code, URLs, file paths, commands, headings, table structure, dates, version numbers — anything technical passes through untouched. Only natural language prose gets expanded and humanized.

See the full [soulmate-expand README](soulmate-expand/README.md) for install, usage, and validation details.

## Star This Repo

If soulmate made your coding sessions feel more human — leave a star. ⭐

## Credits

Forked from [caveman](https://github.com/JuliusBrussee/caveman) by Julius Brussee — the brilliant project that proved communication style matters. We just took it in the opposite direction.

## License

MIT — free like a warm hug on a cold day.
