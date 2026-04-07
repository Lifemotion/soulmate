#!/usr/bin/env python3
import re
from pathlib import Path

URL_REGEX = re.compile(r"https?://[^\s)]+")
CODE_BLOCK_REGEX = re.compile(r"```.*?```", re.DOTALL)
HEADING_REGEX = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)
BULLET_REGEX = re.compile(r"^\s*[-*+]\s+", re.MULTILINE)

# crude but effective path detection
PATH_REGEX = re.compile(r"(\./|\../|/|[A-Za-z]:\\)[\w\-/\\\.]+")


class ValidationResult:
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []

    def add_error(self, msg):
        self.is_valid = False
        self.errors.append(msg)

    def add_warning(self, msg):
        self.warnings.append(msg)


def read_file(path: Path) -> str:
    return path.read_text(errors="ignore")


# ---------- Extractors ----------


def extract_headings(text):
    return [(level, title.strip()) for level, title in HEADING_REGEX.findall(text)]


def extract_code_blocks(text):
    return CODE_BLOCK_REGEX.findall(text)


def extract_urls(text):
    return set(URL_REGEX.findall(text))


def extract_paths(text):
    return set(PATH_REGEX.findall(text))


def count_bullets(text):
    return len(BULLET_REGEX.findall(text))


# ---------- Validators ----------


def validate_headings(orig, expanded, result):
    h1 = extract_headings(orig)
    h2 = extract_headings(expanded)

    if len(h1) != len(h2):
        result.add_error(f"Heading count mismatch: {len(h1)} vs {len(h2)}")

    if h1 != h2:
        result.add_warning("Heading text/order changed")


def validate_code_blocks(orig, expanded, result):
    c1 = extract_code_blocks(orig)
    c2 = extract_code_blocks(expanded)

    if c1 != c2:
        result.add_error("Code blocks not preserved exactly")


def validate_urls(orig, expanded, result):
    u1 = extract_urls(orig)
    u2 = extract_urls(expanded)

    if u1 != u2:
        result.add_error(f"URL mismatch: lost={u1 - u2}, added={u2 - u1}")


def validate_paths(orig, expanded, result):
    p1 = extract_paths(orig)
    p2 = extract_paths(expanded)

    if p1 != p2:
        result.add_warning(f"Path mismatch: lost={p1 - p2}, added={p2 - p1}")


def validate_bullets(orig, expanded, result):
    b1 = count_bullets(orig)
    b2 = count_bullets(expanded)

    if b1 == 0:
        return

    # Expansion may add bullets for clarity, so allow growth but flag large reduction
    if b2 < b1 * 0.85:
        result.add_warning(f"Bullet count decreased too much: {b1} -> {b2}")


# ---------- Main ----------


def validate(original_path: Path, expanded_path: Path) -> ValidationResult:
    result = ValidationResult()

    orig = read_file(original_path)
    expanded = read_file(expanded_path)

    validate_headings(orig, expanded, result)
    validate_code_blocks(orig, expanded, result)
    validate_urls(orig, expanded, result)
    validate_paths(orig, expanded, result)
    validate_bullets(orig, expanded, result)

    return result


# ---------- CLI ----------

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python validate.py <original> <expanded>")
        sys.exit(1)

    orig = Path(sys.argv[1])
    expanded = Path(sys.argv[2])

    res = validate(orig, expanded)

    print(f"\nValid: {res.is_valid}")

    if res.errors:
        print("\nErrors:")
        for e in res.errors:
            print(f"  - {e}")

    if res.warnings:
        print("\nWarnings:")
        for w in res.warnings:
            print(f"  - {w}")
