---
name: soulmate-expand
description: >
  Expand terse, telegraphic memory files (CLAUDE.md, todos, preferences) into warm, human-friendly prose.
  Preserves all technical substance, code, URLs, and structure.
  Expanded version overwrites the original file. Compressed backup saved as FILE.compressed.md.
  Trigger: /soulmate-expand <filepath> or "expand memory file"
---

# Soulmate Expand

## Purpose

Expand terse, dry files (CLAUDE.md, todos, preferences) into warm, human-readable prose. Expanded version overwrites original. Compressed backup saved as `<filename>.compressed.md`.

## Trigger

`/soulmate-expand <filepath>` or when user asks to expand/humanize a memory file.

## Process

1. This SKILL.md lives alongside `scripts/` in the same directory. Find that directory.

2. Run:
   ```
   cd <directory_containing_this_SKILL.md> && python3 -m scripts <absolute_filepath>
   ```

3. The CLI will:
   - detect file type (no tokens)
   - call Claude to expand
   - validate output (no tokens)
   - if errors: cherry-pick fix with Claude (targeted fixes only, no re-expansion)
   - retry up to 2 times

4. Return result to user

## Expansion Rules

### Add
- Context and "why" behind instructions — help the reader understand motivation
- Transitional phrases that improve flow between ideas
- Friendly, conversational tone — like explaining to a colleague you like
- Full sentences where fragments existed
- Articles (a, an, the) back where they belong
- Natural language in place of arrows and abbreviations

### Preserve EXACTLY (never modify)
- Code blocks (fenced ``` and indented)
- Inline code (`backtick content`)
- URLs and links (full URLs, markdown links)
- File paths (`/src/components/...`, `./config.yaml`)
- Commands (`npm install`, `git commit`, `docker build`)
- Technical terms (library names, API names, protocols, algorithms)
- Proper nouns (project names, people, companies)
- Dates, version numbers, numeric values
- Environment variables (`$HOME`, `NODE_ENV`)

### Preserve Structure
- All markdown headings (keep exact heading text, expand body below)
- Bullet point hierarchy (keep nesting level)
- Numbered lists (keep numbering)
- Tables (expand cell text where helpful, keep structure)
- Frontmatter/YAML headers in markdown files

### Expand
- Turn fragments into full, warm sentences
- Replace abbreviations with full words: "DB" -> "database", "auth" -> "authentication", "config" -> "configuration"
- Replace arrows with natural language: "X -> Y" -> "X leads to Y"
- Add "because" / "so that" / "this helps" where motivation is implicit
- Do NOT add information that wasn't in the original
- Do NOT add emojis

CRITICAL RULE:
Anything inside ``` ... ``` must be copied EXACTLY.
Do not:
- remove comments
- remove spacing
- reorder lines
- shorten commands
- simplify anything

Inline code (`...`) must be preserved EXACTLY.
Do not modify anything inside backticks.

If file contains code blocks:
- Treat code blocks as read-only regions
- Only expand text outside them
- Do not merge sections around code

## Pattern

Original:
> TypeScript strict mode always. No `any` unless unavoidable — comment why. Proper types catch bugs early.

Expanded:
> Please always use TypeScript with strict mode enabled for all new code. Avoid using the `any` type unless there's genuinely no way around it, and if you do, leave a comment explaining your reasoning. Taking the time to properly type things really does catch a lot of bugs before they ever make it to runtime.

Original:
> Microservices arch. API gateway route requests to services. Auth service manage sessions + JWT.

Expanded:
> The application uses a microservices architecture with several key components. The API gateway handles all incoming requests and routes them to the appropriate service. The authentication service is responsible for managing user sessions and JWT tokens.

## Boundaries

- ONLY expand natural language files (.md, .txt, extensionless)
- NEVER modify: .py, .js, .ts, .json, .yaml, .yml, .toml, .env, .lock, .css, .html, .xml, .sql, .sh
- If file has mixed content (prose + code), expand ONLY the prose sections
- If unsure whether something is code or prose, leave it unchanged
- Original file is backed up as FILE.compressed.md before overwriting
- Never expand FILE.compressed.md (skip it)
