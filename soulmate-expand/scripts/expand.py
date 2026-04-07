#!/usr/bin/env python3
"""
Soulmate Expand Orchestrator

Usage:
    python -m scripts <filepath>
"""

import subprocess
import sys
from pathlib import Path
from typing import List

from .detect import should_expand
from .validate import validate

MAX_RETRIES = 2


# ---------- Claude Calls ----------


def call_claude(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["claude", "--print"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Claude call failed:\n{e.stderr}")


def build_expand_prompt(original: str) -> str:
    return f"""
Expand this markdown into warm, human-friendly prose. Make it feel like it was written by
a thoughtful, caring person who genuinely wants the reader to succeed.

STRICT RULES:
- Do NOT modify anything inside ``` code blocks
- Do NOT modify anything inside inline backticks
- Preserve ALL URLs exactly
- Preserve ALL headings exactly
- Preserve file paths and commands

EXPANSION RULES:
- Turn terse, telegraphic notes into warm, readable sentences
- Add context and "why" where it helps understanding
- Use friendly, conversational tone — like explaining to a colleague you like
- Replace arrows and abbreviations with natural language
- Add transitional phrases that improve flow
- Keep the same structure (headings, bullets, etc.)
- Do NOT add information that wasn't in the original — only humanize what's there
- Do NOT add emojis

Only expand natural language. Code stays untouched.

TEXT:
{original}
"""


def build_fix_prompt(original: str, expanded: str, errors: List[str]) -> str:
    errors_str = "\n".join(f"- {e}" for e in errors)
    return f"""You are fixing an expanded markdown file. Specific validation errors were found.

CRITICAL RULES:
- DO NOT re-expand or rephrase the file
- ONLY fix the listed errors — leave everything else exactly as-is
- The ORIGINAL is provided as reference only (to restore missing content)
- Preserve warm, human tone in all untouched sections

ERRORS TO FIX:
{errors_str}

HOW TO FIX:
- Missing URL: find it in ORIGINAL, restore it exactly where it belongs in EXPANDED
- Code block mismatch: find the exact code block in ORIGINAL, restore it in EXPANDED
- Heading mismatch: restore the exact heading text from ORIGINAL into EXPANDED
- Do not touch any section not mentioned in the errors

ORIGINAL (reference only):
{original}

EXPANDED (fix this):
{expanded}

Return ONLY the fixed expanded file. No explanation.
"""


# ---------- Core Logic ----------


def expand_file(filepath: Path) -> bool:
    print(f"Processing: {filepath}")

    if not should_expand(filepath):
        print("Skipping (not natural language)")
        return False

    original_text = filepath.read_text(errors="ignore")
    backup_path = filepath.with_name(filepath.stem + ".compressed.md")

    # Step 1: Expand
    print("Expanding with Claude...")
    expanded = call_claude(build_expand_prompt(original_text))

    # Save original as compressed backup, write expanded to original path
    backup_path.write_text(original_text)
    filepath.write_text(expanded)

    # Step 2: Validate + Retry
    for attempt in range(MAX_RETRIES):
        print(f"\nValidation attempt {attempt + 1}")

        result = validate(backup_path, filepath)

        if result.is_valid:
            print("Validation passed")
            break

        print("Validation failed:")
        for err in result.errors:
            print(f"   - {err}")

        if attempt == MAX_RETRIES - 1:
            # Restore original on failure
            filepath.write_text(original_text)
            backup_path.unlink(missing_ok=True)
            print("Failed after retries — original restored")
            return False

        print("Fixing with Claude...")
        expanded = call_claude(
            build_fix_prompt(original_text, expanded, result.errors)
        )
        filepath.write_text(expanded)

    return True


# ---------- Main ----------


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scripts <filepath>")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"File not found: {filepath}")
        sys.exit(1)

    success = expand_file(filepath)

    if success:
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
