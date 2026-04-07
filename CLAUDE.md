# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

Soulmate is a system prompt skill/plugin that makes AI agents (Claude Code, Copilot, Cursor, 40+ others) communicate with warmth, empathy, and personality while preserving 100% technical accuracy. It includes a companion Python tool (soulmate-expand) that transforms terse documentation files into human-readable prose.

Forked from [caveman](https://github.com/JuliusBrussee/caveman) — same idea, opposite direction (warm instead of terse).

## Development Commands

### Benchmarks (requires `ANTHROPIC_API_KEY` in env or `.env.local`)
```bash
python3 benchmarks/run.py --dry-run              # preview config, no API calls
python3 benchmarks/run.py --trials 3              # run benchmarks (default 3 trials)
python3 benchmarks/run.py --update-readme         # run + update README benchmark table
python3 benchmarks/run.py --model <model-id>      # use specific model (default: claude-sonnet-4-20250514)
```

### Soulmate Expand
```bash
cd soulmate-expand && python3 -m scripts <filepath>     # expand a file
python3 soulmate-expand/scripts/benchmark.py             # run token count benchmarks on test fixtures
```

### Validation (used internally by soulmate-expand)
```bash
python3 soulmate-expand/scripts/validate.py    # validate expanded output against original
python3 soulmate-expand/scripts/detect.py      # detect if a file is expandable
```

Test fixtures live in `tests/soulmate-expand/` — pairs of `.md` and `.original.md` files.

## Architecture

### Core Skill: `skills/soulmate/SKILL.md`
The single source of truth for the soulmate system prompt. This is the only file you edit when changing soulmate's behavior. Three intensity levels (gentle, warm, radiant), auto-clarity rules for security/destructive ops, and boundaries (code/commits stay normal).

### CI Auto-Sync (`.github/workflows/sync-skill.yml`)
On push to `main` that touches `skills/soulmate/SKILL.md`, CI automatically copies it to:
- `soulmate/SKILL.md`
- `plugins/soulmate/skills/soulmate/SKILL.md`
- Rebuilds `soulmate.skill` ZIP

**Never edit these copies directly** — they are overwritten by CI.

### Soulmate Expand Pipeline (`soulmate-expand/scripts/`)
Python 3.10+. Flow: `detect.py` (file type check) -> `expand.py` (Claude expansion via `claude --print`, 1 API call) -> `validate.py` (local structure checks) -> targeted fix if validation fails (1 more API call max) -> writes expanded file + `.compressed.md` backup. Max 2 retries; restores original on failure.

### Distribution
- `soulmate.skill` — ZIP for `npx skills add`
- `plugins/soulmate/.codex-plugin/` — Codex plugin metadata
- `.claude-plugin/` — Claude Code plugin config (placeholder)

## Key Conventions

- **Single source of truth**: all SKILL.md changes go through `skills/soulmate/SKILL.md` only
- **PR format for prompt changes**: include before/after examples showing what changed and why
- **Benchmark results**: saved as JSON in `benchmarks/results/` (gitignored)
- **Python deps**: `anthropic` SDK for benchmarks; `tiktoken` (optional) for token counting in soulmate-expand
