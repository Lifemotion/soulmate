<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/sparkling-heart_1f496.png" width="80" />
</p>

<h1 align="center">soulmate-expand</h1>

<p align="center">
  <strong>turn dry notes into warm, human-friendly prose</strong>
</p>

---

A Claude Code skill that expands your terse project memory files (`CLAUDE.md`, todos, preferences) into warm, human-readable prose — so your documentation is actually pleasant to read and maintain.

Dry, telegraphic notes are great for machines. But when you need to read, edit, or onboard someone — you want prose that feels human. Soulmate Expand does that transformation for you.

## What It Does

```
/soulmate-expand CLAUDE.md
```

```
CLAUDE.md              ← expanded, human-friendly (you read and edit this)
CLAUDE.compressed.md   ← compact backup (for reference)
```

Original never lost. You can always refer back to `.compressed.md`. Run the skill again to re-expand after edits.

## Before / After

<table>
<tr>
<td width="50%">

### Before (terse)

> "TypeScript strict mode always. No `any` unless unavoidable — comment why. Proper types catch bugs early."

</td>
<td width="50%">

### After (human)

> "Please always use TypeScript with strict mode enabled for all new code. Avoid using the `any` type unless there's genuinely no way around it, and if you do, leave a comment explaining your reasoning. Taking the time to properly type things really does catch a lot of bugs before they ever make it to runtime."

</td>
</tr>
</table>

**Same instructions. Actually pleasant to read.**

## Install

```bash
cp -r ~/.claude/skills/soulmate-expand <path-to-skill>
```

Or if you have the soulmate repo:

```bash
cp -r skills/soulmate-expand ~/.claude/skills/soulmate-expand
```

**Requires:** Python 3.10+

## Usage

```
/soulmate-expand <filepath>
```

Examples:
```
/soulmate-expand CLAUDE.md
/soulmate-expand docs/preferences.md
/soulmate-expand todos.md
```

### What files work

| Type | Expand? |
|------|---------|
| `.md`, `.txt`, `.rst` | Yes |
| Extensionless natural language | Yes |
| `.py`, `.js`, `.ts`, `.json`, `.yaml` | Skip (code/config) |
| `*.compressed.md` | Skip (backup files) |

## How It Works

```
/soulmate-expand CLAUDE.md
        |
detect file type        (no tokens)
        |
Claude expands          (tokens — one call)
        |
validate output         (no tokens)
  checks: headings, code blocks, URLs, file paths, bullets
        |
if errors: Claude fixes cherry-picked issues only   (tokens — targeted fix)
  does NOT re-expand — only patches broken parts
        |
retry up to 2 times
        |
write expanded    -> CLAUDE.md
write compressed  -> CLAUDE.compressed.md
```

Only two things use tokens: initial expansion + targeted fix if validation fails. Everything else is local Python.

## What Is Preserved

Soulmate expands natural language. It never touches:

- Code blocks (` ``` ` fenced or indented)
- Inline code (`` `backtick content` ``)
- URLs and links
- File paths (`/src/components/...`)
- Commands (`npm install`, `git commit`)
- Technical terms, library names, API names
- Headings (exact text preserved)
- Tables (structure preserved, cell text expanded)
- Dates, version numbers, numeric values

## Part of Soulmate

This skill is part of the [soulmate](https://github.com/Lifemotion/soulmate) toolkit — making Claude sound more human without losing accuracy.

- **soulmate** — make Claude *speak* with warmth and personality
- **soulmate-expand** — make your files *read* like they were written by a human
